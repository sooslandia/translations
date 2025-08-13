import logging
from abc import abstractmethod
from pathlib import Path

from sltt.lng.lng import Lng
from sltt.message_manager import MessageList
from sltt.stages.base import BaseStage
from sltt.stages.constants import MAX_SIMILAR_ERROR_ITEMS, PO_FILE_REGEX

logger = logging.getLogger(__name__)


class BasePoStage(BaseStage):
    @abstractmethod
    def run(self):
        return super().run()

    def validate_po_file_name(
        self, po_file: Path
    ) -> tuple[str | None, str | None, MessageList]:
        errors = []
        if not PO_FILE_REGEX.match(str(po_file.name)):
            logger.warning(f"Found po file with invalid name: {po_file}")
            errors.append(
                f'PO-file has invalid name: "{po_file.name}", PO-files must have name "<two-letter-code>.po"'
            )
            return None, None, errors
        language_code = po_file.stem
        language_name = Lng.language_manager.get_language_name(language_code)
        if language_name is None:
            logger.warning(
                f"Invalid po file found, failed to find name by code: {po_file}"
            )
            errors.append(
                f'PO-file has invalid name: "{po_file.name}", failed to find corresponding language name for code {po_file.stem}"'
            )
            return None, None, errors
        return language_code, language_name, errors

    def generate_error_list(
        self,
        source_po_file_path: Path,
        missing_strings: list[str],
        placeholder_errors: list[str],
    ) -> MessageList:
        errors = []
        if missing_strings:
            stripped_missing_strings = missing_strings[:MAX_SIMILAR_ERROR_ITEMS]
            if len(missing_strings) > MAX_SIMILAR_ERROR_ITEMS:
                stripped_missing_strings.append(
                    f"{len(missing_strings) - MAX_SIMILAR_ERROR_ITEMS} more..."
                )
            errors += ["Missing strings", stripped_missing_strings]
            logger.warning(
                f"{len(missing_strings)} missing strings in po file {source_po_file_path}"
            )
        if placeholder_errors:
            stripped_placeholder_errors = placeholder_errors[:MAX_SIMILAR_ERROR_ITEMS]
            if len(placeholder_errors) > MAX_SIMILAR_ERROR_ITEMS:
                stripped_placeholder_errors.append(
                    f"{len(placeholder_errors) - MAX_SIMILAR_ERROR_ITEMS} more..."
                )
            errors += ["Placeholder errors", stripped_placeholder_errors]
            logger.warning(
                f"{len(placeholder_errors)} placeholder errors in po file {source_po_file_path}"
            )
        return errors
