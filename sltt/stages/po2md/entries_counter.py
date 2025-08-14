from pathlib import Path

from polib import pofile


class Po2MdEntriesCounter:
    def __init__(self, po_file: Path):
        po = pofile(pofile=str(po_file))
        self._translated_entries = {
            (e.msgctxt, e.msgid): e.msgstr for e in po.translated_entries()
        }
        self._requested_translated_entries = set()
        self._requested_untranslated_entries = set()

    def __call__(self, translator, msgid, msgstr, msgctxt, tcomment, flags) -> bool:
        if msgid == "":
            # mdpo requests empty string for some reason
            return True
        key = (msgctxt, msgid)
        if key in self._translated_entries:
            self._requested_translated_entries.add(key)
        else:
            self._requested_untranslated_entries.add(key)
        return True

    @property
    def untranslated_entries_count(self) -> int:
        return len(self._requested_untranslated_entries)

    @property
    def translated_entries_count(self) -> int:
        return len(self._requested_translated_entries)

    @property
    def total_entries_count(self) -> int:
        return len(self._requested_untranslated_entries) + len(
            self._requested_translated_entries
        )
