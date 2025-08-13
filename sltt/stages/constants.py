import re

from sltt.settings import config

BRACES_PLACEHOLDER_REGEX = re.compile(r"(?:(?:\{\{)*|^)\{(\d)\}")
PERCENT_PLACEHOLDER_REGEX = re.compile(r"(?:(?<!\\%)|^)%(\d+)")

RESX_FILE_REGEX = re.compile(r"^(.*?)((?<=\.)[a-z]{2})?\.resx$")
PO_FILE_REGEX = re.compile(r"^[a-z]{2}.po$")
LNG_FILE_REGEX = re.compile(r"^[a-z]*?.lng$")
DOCS_DIR_REGEX = re.compile(r"^[a-z]{2}$")
MAX_SIMILAR_ERROR_ITEMS = 10
POT_METADATA = {
    "Project-Id-Version": "",
    "Report-Msgid-Bugs-To": config.email_address,
    "POT-Creation-Date": "",
    "PO-Revision-Date": "YEAR-MO-DA HO:MI+ZONE",
    "Last-Translator": "FULL NAME <EMAIL@ADDRESS>",
    "Language-Team": "LANGUAGE <LL@li.org>",
    "Language": "",
    "MIME-Version": "1.0",
    "Content-Type": "text/plain; charset=utf-8",
    "Content-Transfer-Encoding": "8bit",
}
