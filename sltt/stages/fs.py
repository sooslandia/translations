import logging
import shutil
from abc import abstractmethod

from sltt import schema
from sltt.message_manager import message_manager
from sltt.stages.base import BaseStage
from sltt.stages.utils import filter_directory

logger = logging.getLogger(__name__)


class FSStage(BaseStage):
    config: schema.FSStage

    def __init__(self, source_root, target_root, config: schema.FSStage):
        super().__init__(source_root, target_root, config)
        self.source_path = self.source_root / config.source
        self.target_path = self.target_root / config.target

    @abstractmethod
    def run(self):
        return super().run()


class CopyFileStage(FSStage):
    config: schema.CopyFileStage

    def run(self):
        super().run()
        logger.debug(f"Copying from {self.source_path} to {self.target_path}")
        if not self.source_path.is_file():
            logger.warning(f"File {self.source_path} not found")
            message_manager.register(
                [f"File {self.source_path.relative_to(self.source_root)} not found"]
            )
            return
        self.target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(self.source_path, self.target_path)
        self._add_to_staging(self.target_path)
        logger.debug("File copied")


class CopyDirectoryContentsStage(FSStage):
    config: schema.CopyDirectoryContentsStage

    def run(self):
        super().run()
        logger.debug(
            f"Copying directory contents from {self.source_path} to {self.target_path}"
        )
        if not self.source_path.is_dir():
            logger.warning(
                f"Failed to copy directory contents, {self.source_path} not a directory"
            )
            message_manager.register(
                [
                    "Source directory not found: "
                    f"{self.source_path.relative_to(self.source_root)}"
                ]
            )
            return
        self.target_path.mkdir(parents=True, exist_ok=True)
        copied_files_total = 0
        for file in filter_directory(
            self.source_path,
            self.config.get_patterns(),
            recursive=self.config.recursive,
        ):
            dest_path = self.target_path / (file.relative_to(self.source_path))
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(file, dest_path)
            self._add_to_staging(dest_path)
            copied_files_total += 1
        logger.debug(f"Copied {copied_files_total} files")
