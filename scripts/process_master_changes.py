import json
import logging
import os
import subprocess
from pathlib import Path
from xml.etree import ElementTree

from constants import EMAIL_ADDRESS
from utils import (
    convert_braces_to_percents,
    convert_percents_to_braces,
    file_updated,
    parse_resx_filename,
)

REPOSITORY_DIR = Path(".")
PROJECTS_DIR = Path(os.environ["PROJECTS_DIR"])

logger = logging.getLogger("process_master_changes")
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
logger.addHandler(console_handler)


def process_project(project_path):
    logger.info(f"Processing project {project_path}")
    convert_resx_files(project_path)
    generate_pot_file(project_path)
    process_docs(project_path)
    logger.info("Project processed")


def convert_resx_files(project_path):
    logger.info("Processing resx files")
    english_lng_file = project_path / "english.lng"
    english_files = []
    has_changes = False
    for file in project_path.glob("*.resx"):
        if parse_resx_filename(file.name)[1] is None:
            english_files.append(file)
            if not has_changes and file_updated(file):
                has_changes = True
    logger.info(f"Found {len(english_files)} english resx files")
    if not has_changes and english_lng_file.exists():
        logger.info("No changed english resx files found")
        return
    lng = {"Culture": "en", "Language": "english"}
    for file in english_files:
        lng |= parse_resx(file)
    lng = json.dumps(lng, indent=2, ensure_ascii=False, sort_keys=True)
    with english_lng_file.open("w", encoding="utf-8", newline="") as f:
        f.write(lng)
    logger.info("Resx files processed")


def parse_resx(file):
    logger.info(f"Parsing resx file {file}")
    namespace, _ = parse_resx_filename(file.name)
    logger.info(f"File namespace is {namespace}")
    with file.open("r", encoding="utf-8") as f:
        root = ElementTree.fromstring(f.read())
    lng = {}
    for data in root.iterfind("data"):
        name = data.attrib["name"]
        text = data.find("value").text
        text = convert_braces_to_percents(text)
        lng[f"{namespace}_{name}"] = text
    logger.info("Resx file parsed")
    return lng


def generate_pot_file(project_path):
    logger.info("Generating pot file from english lng file")
    pot_file = project_path / (project_path.name + ".pot")
    english_file = project_path / "english.lng"
    if not file_updated(english_file) and pot_file.exists():
        logger.info("File is not changed")
        return
    with english_file.open("r") as f:
        lng = json.load(f)
    lng.pop("Culture")
    source = []
    for identifier, string in lng.items():
        source.append(f"# {identifier}")
        source.append(get_source_line_for_pot(convert_percents_to_braces(string)))
    source = "\n".join(source)
    source += "\n"
    pot = generate_pot_file_from_source(source, project_path.name)
    with pot_file.open("w", encoding="utf-8", newline="") as f:
        f.write(pot)
    logger.info("Pot file generated")


def get_source_line_for_pot(string):
    quote = None
    for q in ['"', "'", '"""', "'''"]:
        if q not in string:
            quote = q
            break
    if quote is None:
        raise RuntimeError(f"Failed to find quotes for string {string[:200]}")
    return f"_({quote}{string}{quote})"


def generate_pot_file_from_source(source, package_name):
    logger.info("Generating pot file from source")
    process = subprocess.Popen(
        [
            "xgettext",
            "-o",
            "-",
            "--language=Python",
            "--no-location",
            "--add-comments",
            f"--msgid-bugs-address={EMAIL_ADDRESS}",
            f"--package-name={package_name}",
            "-",
        ],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    process.stdin.write(source.encode())
    process.stdin.flush()
    process.stdin.close()  # EOF
    pot = b""
    while process.poll() is None:
        pot += process.stdout.read()
    if process.returncode != 0:
        raise RuntimeError(f"xgettext failed with code {process.returncode}")
    logger.info("Pot generated from source")
    return pot.decode()


def process_docs(project_path):
    logger.info("Processing docs")
    docs_path = project_path / "docs"
    if not docs_path.is_dir():
        logger.info("No docs in project")
        return
    en_docs_path = docs_path / "en"
    process_en_docs(en_docs_path)
    logger.info("Docs processed")


def process_en_docs(en_docs_path):
    logger.info(f"Processing english docs: {en_docs_path}")
    for md_file in en_docs_path.glob("*.md"):
        process_docs_md_file(md_file)
    logger.info("English docs processed")


def process_docs_md_file(md_file):
    logger.info(f"Processing docs md file {md_file}")
    package_name = md_file.relative_to(REPOSITORY_DIR).parts[0]
    pot_file = md_file.with_suffix(".pot")
    if not file_updated(md_file) and pot_file.exists():
        logger.info("Md file is not changed")
        return
    process = subprocess.Popen(
        [
            "md2po",
            "-d",
            "Content-Type: text/plain; charset=utf-8",
            md_file,
        ],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
    )
    po = b""
    while process.poll() is None:
        po += process.stdout.read()
    if process.returncode != 0:
        raise RuntimeError(f"md2po failed with code {process.returncode}")
    process = subprocess.Popen(
        [
            "xgettext",
            "-o",
            "-",
            "--language=po",
            "--add-comments",
            f"--msgid-bugs-address={EMAIL_ADDRESS}",
            f"--package-name={package_name}",
            "-",
        ],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    process.stdin.write(po)
    process.stdin.flush()
    process.stdin.close()  # EOF
    pot = b""
    while process.poll() is None:
        pot += process.stdout.read()
    if process.returncode != 0:
        raise RuntimeError(f"xgettext failed with code {process.returncode}")
    with pot_file.open("wb") as f:
        f.write(pot)
    logger.info("Md file processed")


def main():
    with (REPOSITORY_DIR / "projects.txt").open("r", encoding="utf-8") as f:
        project_dirs = [i for i in f.read().split("\n") if i]
    for project_dir in project_dirs:
        process_project(PROJECTS_DIR / project_dir)


if __name__ == "__main__":
    main()
