import logging

from polib import POEntry, POFile, pofile

from sltt import schema
from sltt.message_manager import message_manager
from sltt.stages.base import BaseStage
from sltt.stages.utils import (
    file_has_changes,
    file_should_be_updated,
    generate_pot_metadata,
)

logger = logging.getLogger(__name__)


class ConvertPo2PotStage(BaseStage):
    config: schema.ConvertPo2PotStage

    def run(self):
        super().run()
        source = self.source_root / self.config.source_po_file_path
        target = self.target_root / self.config.target_pot_file_path
        logger.debug(
            f"Converting po file to pot file, source: {source}, target: {target}"
        )
        if not source.is_file():
            logger.warning(f"Failed to convert po to pot, {source} not found")
            message_manager.register(
                [f"PO-file not found: {source.relative_to(self.source_root)}"]
            )
            return
        if not file_has_changes(source) and not file_should_be_updated(target):
            logger.debug("No changes detected, skipping conversion")
            return
        source_po = pofile(pofile=str(source))
        target_pot = POFile()
        target_pot.metadata = generate_pot_metadata(
            source_po.metadata["Project-Id-Version"]
        )
        for s in source_po.translated_entries():
            t = POEntry(
                msgctxt=s.msgctxt,
                msgid=s.msgstr,
                flags=s.flags,
                comment=s.comment,
                tcomment=s.tcomment,
                occurrences=s.occurrences,
            )
            target_pot.append(t)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(str(target_pot).encode())
        self._add_to_staging(target)
        logger.debug("po2pot conversion finished")
