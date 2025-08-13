import logging

from polib import POEntry, POFile

from sltt import schema
from sltt.lng import Lng
from sltt.lng.exceptions import LngException
from sltt.message_manager import message_manager
from sltt.stages.base import BaseStage
from sltt.stages.utils import (
    convert_percents_to_braces,
    file_has_changes,
    file_should_be_updated,
    generate_pot_metadata,
)

logger = logging.getLogger(__name__)


class ConvertLng2PotStage(BaseStage):
    config: schema.ConvertLng2PotStage

    def run(self):
        super().run()
        source = self.source_root / self.config.source_lng_file_path
        target = self.target_root / self.config.target_pot_file_path
        logger.debug(f"Converting lng to pot: source: {source}, target: {target}")
        if not source.is_file():
            logger.warning(f"Failed to convert lng to pot, {source} not found")
            message_manager.register(
                [f"LNG file not found: {source.relative_to(self.source_root)}"]
            )
            return
        if not file_has_changes(source) and not file_should_be_updated(target):
            logger.debug("No changes detected, skipping conversion")
            return
        try:
            lng = Lng.load_from_file(source)
        except LngException as e:
            logger.warning(f"Failed to load lng file: {e}")
            message_manager.register(
                [f"Failed to load {source.relative_to(self.source_root)}", e.message]
            )
            return
        pot = POFile()
        pot.metadata = generate_pot_metadata(self.config.package)
        for identifier, string in lng.items():
            converted_string = convert_percents_to_braces(string)
            flags = []
            if string != converted_string:
                # If the modification was made, we have at least one brace pair
                flags.append("python-brace-format")
            entry = POEntry(msgctxt=identifier, msgid=converted_string, flags=flags)
            pot.append(entry)
        pot_content = str(pot).encode()
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(pot_content)
        self._add_to_staging(target)
        logger.debug("Conversion done")
