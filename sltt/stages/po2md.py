import logging
from pathlib import Path

from mdpo.po2md import Po2Md

from sltt import schema
from sltt.enums import Po2MdStageMode
from sltt.message_manager import MessageList, message_manager
from sltt.stages.base import BaseStage
from sltt.stages.utils import (
    file_has_changes,
    file_should_be_updated,
)

logger = logging.getLogger(__name__)


class ConvertPo2MdStage(BaseStage):
    config: schema.ConvertPo2MdStage

    def run(self):
        super().run()
        if self.config.mode == Po2MdStageMode.SINGLE:
            source_dir = self.source_root / self.config.source_po_files_dir
            target_dir = self.target_root / self.config.target_md_files_dir
        elif self.config.mode == Po2MdStageMode.MULTIPLE:
            source_dir = self.source_root / self.config.source_docs_dir
            target_dir = self.target_root / self.config.target_docs_dir
        else:
            raise ValueError(f"Unknown po2md mode: {self.config.mode}")
        base_md_files_dir = self.source_root / self.config.base_md_files_dir
        logger.debug(
            f"Generating md from po: mode {self.config.mode.name}, source dir: {source_dir}, target dir: {target_dir}"
        )
        if not source_dir.is_dir():
            logger.warning(
                f"Failed to generate md from po, {source_dir} not a directory"
            )
            message_manager.register(
                [
                    f"Source directory not found: {source_dir.relative_to(self.source_root)}"
                ]
            )
            return
        if not base_md_files_dir.is_dir():
            logger.warning(
                f"Failed to generate md from po, base md files dir {base_md_files_dir} not a directory"
            )
            message_manager.register(
                [
                    f"Base md files directory not found: {base_md_files_dir.relative_to(self.source_root)}"
                ],
            )
            return
        errors = []
        target_dir.mkdir(parents=True, exist_ok=True)
        if self.config.mode == Po2MdStageMode.SINGLE:
            language_dir_errors = self._run_single(source_dir, target_dir)
            logger.debug("Single conversion finished")
            if language_dir_errors:
                errors += [
                    f"Errors when processing {source_dir.relative(self.source_root)}",
                    language_dir_errors,
                ]
        else:
            total_dirs_processed = 0
            for po_language_docs_dir in source_dir.glob("*"):
                if not po_language_docs_dir.is_dir():
                    continue
                if po_language_docs_dir.name in self.config.excluded_dirs:
                    continue
                md_language_docs_dir = target_dir / (
                    po_language_docs_dir.relative_to(source_dir)
                )
                md_language_docs_dir.mkdir(exist_ok=True)
                language_dir_errors = self._run_single(
                    po_language_docs_dir, md_language_docs_dir
                )
                if language_dir_errors:
                    errors += [
                        "Errors when processing "
                        f"{po_language_docs_dir.relative(self.source_root)}",
                        language_dir_errors,
                    ]
                total_dirs_processed += 1
            logger.debug(f"Multiple doc dirs processed, count: {total_dirs_processed}")
        if errors:
            message_manager.register(errors)

    def _run_single(self, po_files_dir: Path, md_files_dir: Path) -> MessageList:
        logger.debug(
            f"Generating md files from po files, source dir: {po_files_dir}, target dir: {md_files_dir}"
        )
        md_files_dir.mkdir(parents=True, exist_ok=True)
        total_files_processed = 0
        errors = []
        for po_file_path in po_files_dir.glob("*.po"):
            if not po_file_path.is_file():
                continue
            md_file_path = md_files_dir / (
                po_file_path.relative_to(po_files_dir)
            ).with_suffix(".md")
            base_md_file_path = (
                self.source_root / self.config.base_md_files_dir / md_file_path.name
            )
            if not base_md_file_path.is_file():
                logger.warning(f"Base md file not found for {po_file_path}")
                errors.append(
                    f"Base md file for {po_file_path.relative_to(self.source_root)} not found"
                )
                continue
            if (
                not file_has_changes(po_file_path)
                and not file_should_be_updated(md_file_path)
                and (
                    self.config.ignore_base_changes
                    or not file_has_changes(base_md_file_path)
                )
            ):
                logger.debug(
                    f"No changes detected in files {po_file_path}, {md_file_path} and {base_md_file_path}, skipping conversion"
                )
                continue
            md = self._generate_md_from_po(po_file_path, base_md_file_path)
            md_file_path.write_bytes(md.encode())
            self._add_to_staging(md_file_path)
            logger.debug(f"po file {po_file_path} converted to {md_file_path}")
            total_files_processed += 1
        logger.debug(
            f"Language po2md conversion finished, total files processed: {total_files_processed}"
        )
        return errors

    def _generate_md_from_po(self, po_file_path: Path, base_md_file_path: Path) -> str:
        translator = Po2Md(str(po_file_path), wrapwidth=0)
        return translator.translate(base_md_file_path)
