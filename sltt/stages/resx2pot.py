import logging

from polib import POEntry, POFile

from sltt import schema
from sltt.message_manager import message_manager
from sltt.resx.resx import Resx
from sltt.stages.base import BaseStage
from sltt.stages.constants import BRACES_PLACEHOLDER_REGEX
from sltt.stages.utils import (
    file_has_changes,
    file_should_be_updated,
    generate_pot_metadata,
)

logger = logging.getLogger(__name__)


class ConvertResx2PotStage(BaseStage):
    config: schema.ConvertResx2PotStage

    def run(self):
        super().run()
        source = self.source_root / self.config.source_components_dir
        target = self.target_root / self.config.target_pot_file_path
        logger.debug(f"Converting resx to pot: source: {source}, target: {target}")
        if not source.is_dir():
            logger.warning(f"Failed to convert resx to pot, {source} not a directory")
            message_manager.register(
                [
                    f"Resx components directory not found: {source.relative_to(self.source_root)}"
                ],
            )
            return
        target.parent.mkdir(parents=True, exist_ok=True)
        pot = POFile()
        pot.metadata = generate_pot_metadata(self.config.package)
        total_files_processed = 0
        pot_should_be_updated = file_should_be_updated(target)
        resx_files = list(source.rglob("*.resx"))
        resx_has_changes = any(file_has_changes(i) for i in resx_files)
        if not pot_should_be_updated and not resx_has_changes:
            logger.debug("No changes detected, skipping conversion")
            return
        namespaces = set()
        for resx_file in resx_files:
            logger.debug(f"Processing file {resx_file}")
            resx = Resx.load_from_file(resx_file)
            logger.debug(f"Namespace: {resx.namespace}, language: {resx.language}")
            if resx.namespace in namespaces:
                raise ValueError("Resx namespace duplicated!")
            namespaces.add(resx.namespace)
            self._process_component(pot, resx)
            total_files_processed += 1
        pot_content = str(pot).encode()
        target.write_bytes(pot_content)
        self._add_to_staging(target)
        logger.debug(f"Conversion done, total files processed: {total_files_processed}")

    def _process_component(self, pot: POFile, resx: Resx) -> None:
        for resx_identifier, string in resx.items():
            flags = []
            if BRACES_PLACEHOLDER_REGEX.match(string):
                flags.append("python-brace-format")
            identifier = f"{resx.namespace}_{resx_identifier}"
            entry = POEntry(msgctxt=identifier, msgid=string, flags=flags)
            pot.append(entry)
