import logging
from pathlib import Path

from mdpo.md2po import Md2Po
from polib import POFile

from sltt import schema
from sltt.message_manager import message_manager
from sltt.stages.base import BaseStage
from sltt.stages.utils import (
    file_has_changes,
    file_should_be_updated,
    generate_pot_metadata,
)

logger = logging.getLogger(__name__)


class ConvertMd2PotStage(BaseStage):
    config: schema.ConvertMd2PotStage

    def run(self):
        super().run()
        md_files_dir = self.source_root / self.config.source_md_files_dir
        pot_files_dir = self.target_root / self.config.target_pot_files_dir
        logger.debug(
            f"Generating pot files from md files, source dir: {md_files_dir}, target dir: {pot_files_dir}"
        )
        if not md_files_dir.is_dir():
            logger.warning(
                f"Failed to generate pot from md, {md_files_dir} not a directory"
            )
            message_manager.register(
                [
                    "Source directory not found: "
                    f"{md_files_dir.relative_to(self.source_root)}"
                ]
            )
            return
        pot_files_dir.mkdir(parents=True, exist_ok=True)
        total_files_processed = 0
        for md_file_path in md_files_dir.glob("*.md"):
            if not md_file_path.is_file():
                continue
            pot_file_path = pot_files_dir / (
                md_file_path.relative_to(md_files_dir)
            ).with_suffix(".pot")
            if not file_has_changes(md_file_path) and not file_should_be_updated(
                pot_file_path
            ):
                logger.debug(
                    f"No changes detected in files {md_file_path} and {pot_file_path}, skipping conversion"
                )
                continue
            po = self._generate_po_from_md(md_file_path)
            self._add_pot_metadata(po)
            pot_file_path.write_bytes(str(po).encode())
            self._add_to_staging(pot_file_path)
            logger.debug(f"MD file {md_file_path} converted to {pot_file_path}")
            total_files_processed += 1
        logger.debug(
            f"md2pot conversion finished, total files processed: {total_files_processed}"
        )

    def _generate_po_from_md(self, md_file: Path) -> POFile:
        extractor = Md2Po(files_or_content=md_file.read_bytes().decode(), location=True)
        extractor._current_markdown_filepath = md_file.name
        return extractor.extract()

    def _add_pot_metadata(self, po: POFile) -> None:
        po.metadata |= generate_pot_metadata(self.config.package)
