import logging
from pathlib import Path
from typing import Generator

from polib import pofile

from sltt import schema
from sltt.lng.exceptions import LngException
from sltt.lng.lng import Lng
from sltt.message_manager import MessageList, message_manager
from sltt.stages.base_po import BasePoStage
from sltt.stages.utils import (
    convert_braces_to_percents,
    convert_percents_to_braces,
    file_has_changes,
    file_should_be_updated,
    validate_placeholders,
)

logger = logging.getLogger(__name__)


class ConvertPo2LngStage(BasePoStage):
    config: schema.ConvertPo2LngStage

    def run(self):
        super().run()
        source_po_dir = self.source_root / self.config.source_po_files_dir
        target_lng_dir = self.target_root / self.config.target_lng_files_dir
        reference_lng_file_path = self.source_root / self.config.reference_lng_file_path
        logger.debug(
            f"Converting po files to lng files, source dir: {source_po_dir}, target dir: {target_lng_dir}"
        )
        if not source_po_dir.is_dir():
            logger.warning(
                f"Failed to convert po to lng, {source_po_dir} not a directory"
            )
            message_manager.register(
                [
                    "Source directory not found: "
                    f"{source_po_dir.relative_to(self.source_root)}"
                ]
            )
            return
        if not reference_lng_file_path.is_file():
            logger.warning(
                f"Failed to convert po to lng, reference lng file not found: {reference_lng_file_path}"
            )
            message_manager.register(
                [
                    "Reference lng file not found: "
                    f"{reference_lng_file_path.relative_to(self.source_root)}"
                ],
            )
            return
        try:
            reference_lng = Lng.load_from_file(reference_lng_file_path)
        except LngException as e:
            logger.warning(f"Failed to load reference lng file: {e}")
            message_manager.register(
                [
                    "Failed to load reference lng file: "
                    f"{reference_lng_file_path.relative_to(self.source_root)}",
                    e.message,
                ],
            )
            return
        target_lng_dir.mkdir(parents=True, exist_ok=True)
        total_files_processed = 0
        reference_lng_has_changed = file_has_changes(reference_lng_file_path)
        errors = []
        for po_file_path in self._iter_po_files(source_po_dir):
            if not po_file_path.is_file():
                continue
            language_code, language_name, po_file_errors = self.validate_po_file_name(
                po_file_path
            )
            errors.extend(po_file_errors)
            if language_code is None or language_name is None:
                continue
            lng_file_path = target_lng_dir / (
                po_file_path.relative_to(source_po_dir)
            ).with_stem(language_name).with_suffix(".lng")
            if (
                not reference_lng_has_changed
                and not file_has_changes(po_file_path)
                and not file_should_be_updated(lng_file_path)
            ):
                logger.debug(
                    f"No changes detected in files {po_file_path} and {lng_file_path}, skipping conversion"
                )
                continue
            lng, lng_errors = self._convert_po2lng(
                po_file_path,
                reference_lng,
                language_code,
                language_name,
            )
            if lng_errors:
                errors += [
                    f"Errors when converting {po_file_path.relative_to(self.source_root)}",
                    lng_errors,
                ]
            lng.save_to_file(lng_file_path)
            self._add_to_staging(lng_file_path)
            logger.debug(f"po file {po_file_path} converted to {lng_file_path}")
            total_files_processed += 1
        logger.debug(
            f"po2lng conversion finished, total files processed: {total_files_processed}"
        )
        if errors:
            message_manager.register(errors)

    def _iter_po_files(self, source_po_dir: Path) -> Generator[Path, None, None]:
        po_files_gen = source_po_dir.glob("*.po")
        if not self.config.include_files and not self.config.exclude_files:
            yield from po_files_gen
        elif self.config.include_files:
            for file in po_files_gen:
                if file.name not in self.config.include_files:
                    continue
                yield file
        else:
            for file in po_files_gen:
                if file.name in self.config.exclude_files:
                    continue
                yield file

    def _convert_po2lng(
        self,
        source_po_file_path: Path,
        reference_lng: Lng,
        language_code: str,
        language_name: str,
    ) -> tuple[Lng, MessageList]:
        logger.info(f"Converting po file {source_po_file_path} to lng")
        source_po = pofile(pofile=str(source_po_file_path))
        lng = Lng(language_code, language_name)
        translated_entries = {
            e.msgctxt: e.msgstr for e in source_po.translated_entries()
        }
        errors = []
        missing_strings = []
        placeholder_errors = []
        for identifier, string in reference_lng.items():
            translated_string = translated_entries.get(identifier)
            if translated_string is None:
                missing_strings.append(f"{identifier} - {string[:200]}")
                continue
            translated_string_placeholder_errors = [
                f"{identifier} - {i}"
                for i in validate_placeholders(
                    convert_percents_to_braces(reference_lng[identifier]),
                    translated_string,
                )
            ]
            placeholder_errors.extend(translated_string_placeholder_errors)
            if translated_string_placeholder_errors:
                continue
            lng[identifier] = convert_braces_to_percents(translated_string)
        errors += self.generate_error_list(
            source_po_file_path, missing_strings, placeholder_errors
        )
        return lng, errors
