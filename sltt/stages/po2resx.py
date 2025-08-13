import logging
from pathlib import Path
from typing import TypedDict

from polib import pofile

from sltt import schema
from sltt.message_manager import MessageList, message_manager
from sltt.resx.resx import Resx
from sltt.stages.base_po import BasePoStage
from sltt.stages.utils import (
    file_has_changes,
    file_should_be_updated,
    validate_placeholders,
)

logger = logging.getLogger(__name__)


class ResxData(TypedDict):
    resx: Resx
    has_changes: bool


BaseResx = dict[Path, ResxData]


class ConvertPo2ResxStage(BasePoStage):
    config: schema.ConvertPo2ResxStage

    def run(self):
        super().run()
        source = self.source_root / self.config.source_po_files_dir
        target = self.target_root / self.config.target_components_dir
        base_components_dir = self.source_root / self.config.base_components_dir
        logger.debug(f"Converting po to resx: source: {source}, target: {target}")
        if not source.is_dir():
            logger.warning(f"Failed to convert po to resx, {source} not a directory")
            message_manager.register(
                [f"Source directory not found: {source.relative_to(self.source_root)}"]
            )
            return
        if not base_components_dir.is_dir():
            logger.warning(
                f"Failed to convert po to resx, base directory not found: {base_components_dir}"
            )
            message_manager.register(
                [
                    f"Base resx components directory not found: {base_components_dir.relative_to(self.source_root)}"
                ]
            )
            return
        target.parent.mkdir(parents=True, exist_ok=True)
        base_resx: BaseResx = {}
        logger.debug("Loading base resx files")
        total_base_resx_loaded = 0
        for resx_file in base_components_dir.rglob("*.resx"):
            resx = Resx.load_from_file(resx_file)
            base_resx[resx_file] = {
                "resx": resx,
                "has_changes": file_has_changes(resx_file),
            }
            logger.debug(
                f"Loaded resx. Namespace: {resx.namespace}, language: {resx.language}"
            )
            total_base_resx_loaded += 1
        logger.debug(f"Loaded {total_base_resx_loaded} base resx files")
        total_po_files_processed = 0
        errors = []
        for po_file_path in source.glob("*.po"):
            if not po_file_path.is_file():
                continue
            language_code, language_name, po_file_errors = self.validate_po_file_name(
                po_file_path
            )
            errors.extend(po_file_errors)
            if language_code is None or language_name is None:
                continue
            po_file_errors = self._process_po_file(
                po_file_path, base_resx, language_code, language_name
            )
            if po_file_errors:
                errors += [
                    f"Errors when converting {po_file_path.relative_to(self.source_root)}",
                    po_file_errors,
                ]
            [i["resx"].reset() for i in base_resx.values()]
            total_po_files_processed += 1
        if errors:
            message_manager.register(errors)
        logger.debug(
            f"Conversion done, total files processed: {total_po_files_processed}"
        )

    def _process_po_file(
        self,
        po_file_path: Path,
        base_resx: BaseResx,
        language_code: str,
        language_name: str,
    ) -> MessageList:
        base_components_dir = self.source_root / self.config.base_components_dir
        target = self.target_root / self.config.target_components_dir
        logger.debug(f"Processing po file {po_file_path}")
        po_file_has_changes = file_has_changes(po_file_path)
        source_po = pofile(pofile=str(po_file_path))
        translated_entries = {
            e.msgctxt: e.msgstr for e in source_po.translated_entries()
        }
        errors = []
        missing_strings = []
        placeholder_errors = []
        for resx_file, resx_data in base_resx.items():
            target_resx_file_path = target / resx_file.relative_to(
                base_components_dir
            ).with_stem(f"{resx_data['resx'].namespace}.{language_code}")
            logger.debug(f"Extracting strings for {resx_data['resx'].namespace}")
            if (
                not po_file_has_changes
                and not resx_data["has_changes"]
                and not file_should_be_updated(target_resx_file_path)
            ):
                logger.debug("No changes required")
                continue
            resx_missing_strings, resx_placeholder_errors = self._update_resx_from_po(
                resx_data["resx"], translated_entries
            )
            missing_strings.extend(resx_missing_strings)
            placeholder_errors.extend(resx_placeholder_errors)
            target_resx_file_path.parent.mkdir(parents=True, exist_ok=True)
            resx_data["resx"].save_to_file(target_resx_file_path)
            self._add_to_staging(target_resx_file_path)
        errors += self.generate_error_list(
            po_file_path, missing_strings, placeholder_errors
        )
        return errors

    def _update_resx_from_po(
        self, resx: Resx, translated_po_entries: dict[str, str]
    ) -> tuple[list[str], list[str]]:
        missing_strings = []
        placeholder_errors = []
        for resx_key, resx_value in resx.items():
            identifier = f"{resx.namespace}_{resx_key}"
            translated_string = translated_po_entries.get(identifier)
            if translated_string is None:
                missing_strings.append(f"{identifier} - {resx_value[:200]}")
                continue
            translated_string_placeholder_errors = [
                f"{identifier} - {i}"
                for i in validate_placeholders(resx_value, translated_string)
            ]
            placeholder_errors.extend(translated_string_placeholder_errors)
            if translated_string_placeholder_errors:
                continue
            resx[resx_key] = translated_string
        return missing_strings, placeholder_errors
