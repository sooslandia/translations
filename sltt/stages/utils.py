import datetime
import re
from pathlib import Path

from git import BaseIndexEntry, Blob, Repo
from gitdb import IStream

from sltt import schema
from sltt.repo_registry import repo_registry
from sltt.settings import config
from sltt.stages.constants import (
    BRACES_PLACEHOLDER_REGEX,
    PERCENT_PLACEHOLDER_REGEX,
    POT_METADATA,
    RESX_FILE_REGEX,
)


def filter_directory(
    directory: Path, patterns: list[schema.Pattern], *, recursive: bool = False
) -> list[Path]:
    result = []
    glob_func = directory.rglob if recursive else directory.glob
    for pattern in patterns:
        if isinstance(pattern, schema.GlobPattern):
            result.extend(glob_func(pattern.glob))
        elif isinstance(pattern, schema.RegexPattern):
            for element in glob_func("*"):
                if re.match(pattern.regex, element.name):
                    result.append(element)
        else:
            raise ValueError(f"Unknown pattern type: {type(pattern)}")
    result = [i for i in result if i.is_file()]
    return result


def generate_pot_metadata(package: str) -> dict:
    date = datetime.datetime.now(datetime.timezone.utc)
    metadata = POT_METADATA.copy()
    metadata["Project-Id-Version"] = package
    metadata["POT-Creation-Date"] = f"{date:%Y-%m-%d %H:%M+0000}"
    return metadata


def file_has_changes(file_path: Path) -> bool:
    repo = repo_registry.get_repo(config.projects_dir)
    base_commit = repo.commit(config.base_commit_sha)
    diff = base_commit.diff(paths=[file_path])
    return bool(diff)


def file_should_be_updated(file_path: Path):
    return not file_path.exists() or file_has_changes(file_path)


def add_files_to_index(repo: Repo, files: list[Path]):
    """Add files to repository index with mode 100644, ignoring actual mode.
    It is useful for filesystems with limited unix mode functionality,
    because default gitpython implementation ignores core.filemode config value.
    """
    entries = []
    for file_path in files:
        with file_path.open("rb") as f:
            istream = repo.odb.store(IStream(Blob.type, file_path.stat().st_size, f))
        entry = BaseIndexEntry(
            (
                0o100644,
                istream.binsha,
                0,
                file_path.relative_to(repo.working_dir).as_posix(),
            )
        )
        entries.append(entry)
    repo.index.add(entries)


def parse_resx_filename(resx_filename):
    """Returns (namespace, lang-code) tuple.
    Lang code could be None for english files.
    """
    match = RESX_FILE_REGEX.match(resx_filename)
    return match[1], match[2]


def _percent_to_braces(match):
    n = int(match[1])
    return f"{{{n - 1}}}"  # {0} for example


def convert_percents_to_braces(string):
    return PERCENT_PLACEHOLDER_REGEX.sub(_percent_to_braces, string)


def _braces_to_percent(match):
    n = int(match[1])
    return f"%{n + 1}"


def convert_braces_to_percents(string):
    return BRACES_PLACEHOLDER_REGEX.sub(_braces_to_percent, string)


def _get_brace_placeholders(string):
    return BRACES_PLACEHOLDER_REGEX.findall(string)


def validate_placeholders(original_string: str, translated_string: str) -> list[str]:
    original_placeholders = _get_brace_placeholders(original_string)
    translated_placeholders = _get_brace_placeholders(translated_string)
    errors = []
    for p in original_placeholders:
        if (count := translated_placeholders.count(p)) == 1:
            continue
        if count == 0:
            errors.append(f"Placeholder {{{p}}} not found")
        else:
            errors.append(f"Placeholder {{{p}}} duplicated")
    for p in translated_placeholders:
        if p not in original_placeholders:
            errors.append(f"Extra placeholder {{{p}}} found in translated string")
    return errors
