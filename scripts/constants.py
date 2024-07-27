import re

BRACES_PLACEHOLDER_REGEX = re.compile(r"(?:(?<=[^{])|^)\{(\d+)\}")
PERCENT_PLACEHOLDER_REGEX = re.compile(r"(?:(?<=[^%])|^)%(\d+)")

RESX_FILE_REGEX = re.compile(r"^(.*?)((?<=\.)[a-z]{2})?\.resx$")
PO_FILE_REGEX = re.compile(r"^[a-z]{2}.po$")
LNG_FILE_REGEX = re.compile(r"^[a-z]*?.lng$")
DOCS_DIR_REGEX = re.compile(r"^[a-z]{2}$")

EMAIL_ADDRESS = "contact@sooslandia.ru"
