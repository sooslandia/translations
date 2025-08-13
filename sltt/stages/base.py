import logging
from abc import ABC, abstractmethod
from pathlib import Path

import git

from sltt.stages.utils import add_files_to_index

logger = logging.getLogger(__name__)


class BaseStage(ABC):
    def __init__(self, source_root: Path, target_root: Path, config):
        self.source_root = source_root
        self.target_root = target_root
        self.config = config
        self._staging: list[Path] = []

    @abstractmethod
    def run(self):
        pass

    def _add_to_staging(self, file: Path):
        self._staging.append(file)

    def stage_changes(self, repo: git.Repo):
        logger.debug(f"Staging {len(self._staging)} files")
        if not self._staging:
            return
        add_files_to_index(repo, self._staging)
        self._staging.clear()
