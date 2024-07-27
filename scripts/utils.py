import os
import shlex
import subprocess
from pathlib import Path

from constants import (
    BRACES_PLACEHOLDER_REGEX,
    PERCENT_PLACEHOLDER_REGEX,
    RESX_FILE_REGEX,
)


def _percent_to_braces(match):
    n = int(match[1])
    return f"{{{n-1}}}"  # {0} for example


def _braces_to_percent(match):
    n = int(match[1])
    return f"%{n+1}"


def convert_braces_to_percents(string):
    return BRACES_PLACEHOLDER_REGEX.sub(_braces_to_percent, string)


def convert_percents_to_braces(string):
    return PERCENT_PLACEHOLDER_REGEX.sub(_percent_to_braces, string)


def file_updated(file_path):
    file_path = Path(file_path).resolve()
    quoted_file_path = shlex.quote(file_path.name)
    previous_commit = os.environ.get("BEFORE_PUSH_COMMIT_SHA", "HEAD~1")
    return_code = subprocess.call(
        ["bash", "-c", f"[[ $(git diff {previous_commit} -- {quoted_file_path}) ]]"],
        cwd=str(file_path.parent),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    # 0 means we have some diff
    return return_code == 0


def parse_resx_filename(resx_filename):
    match = RESX_FILE_REGEX.match(resx_filename)
    return match[1], match[2]


def get_percent_placeholders(string):
    return PERCENT_PLACEHOLDER_REGEX.findall(string)
