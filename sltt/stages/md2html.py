import logging
import subprocess
import time
from pathlib import Path

from sltt import schema
from sltt.message_manager import message_manager
from sltt.stages.base import BaseStage
from sltt.stages.utils import (
    file_has_changes,
    file_should_be_updated,
)

logger = logging.getLogger(__name__)


class ConvertMd2HtmlStage(BaseStage):
    config: schema.ConvertMd2HtmlStage

    def run(self):
        super().run()
        source = self.source_root / self.config.source_md_docs_dir
        target = self.target_root / self.config.target_html_docs_dir
        logger.debug(f"Converting md files to html, source: {source}, target: {target}")
        if not source.is_dir():
            logger.warning(f"Failed to convert md to html, {source} not a directory")
            message_manager.register(
                [f"Source directory not found: {source.relative_to(self.source_root)}"]
            )
            return
        target.parent.mkdir(parents=True, exist_ok=True)
        for md_file_path in source.rglob("*.md"):
            target_html_file_path = target / md_file_path.relative_to(
                source
            ).with_suffix(".html")
            logger.debug(f"Converting {md_file_path} to {target_html_file_path}")
            if not file_has_changes(md_file_path) and not file_should_be_updated(
                target_html_file_path
            ):
                logger.debug("No changes required, skipping conversion")
                continue
            target_html_file_path.parent.mkdir(parents=True, exist_ok=True)
            self._convert_md_to_html(md_file_path, target_html_file_path)
            self._add_to_staging(target_html_file_path)
        logger.debug("md2html conversion finished")

    def _convert_md_to_html(self, md_file_path: Path, html_file_path: Path):
        process = subprocess.Popen(
            [
                "pandoc",
                "-s",
                "-o",
                html_file_path.as_posix(),
                md_file_path.as_posix(),
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        start_time = time.time()
        while process.poll() is None:
            time.sleep(0.1)
            if time.time() - start_time > 5:
                raise TimeoutError("md2html conversion timeout")
        if process.returncode != 0:
            raise RuntimeError(
                f"md2html conversion failed, pandoc exited with code {process.returncode}"
            )
        if not html_file_path.is_file():
            raise RuntimeError(
                "md2html conversion failed, pandoc did not generated html file"
            )
