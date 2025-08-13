from pathlib import Path
from xml.etree import ElementTree

from sltt.stages.constants import RESX_FILE_REGEX


class Resx(dict):
    def __init__(self, root: ElementTree.Element, namespace: str, language: str):
        self._root = root
        self.namespace = namespace
        self.language = language
        self._snapshot = None

    @classmethod
    def load_from_file(cls, file: Path) -> "Resx":
        namespace, language = cls.parse_resx_filename(file.name)
        if language is None:
            language = "en"
        data = file.read_bytes().decode()
        root = ElementTree.fromstring(data)
        resx = cls(root=root, namespace=namespace, language=language)
        for data in root.iterfind("data"):
            name = data.attrib["name"]
            text = data.find("value").text
            resx[name] = text
        resx.snapshot()
        return resx

    @staticmethod
    def parse_resx_filename(resx_filename):
        """Returns (namespace, lang-code) tuple.
        Lang code could be None for english files.
        """
        match = RESX_FILE_REGEX.match(resx_filename)
        return match[1], match[2]

    def snapshot(self):
        self._snapshot = dict(self)

    def reset(self):
        if self._snapshot is None:
            raise ValueError("No snapshot taken")
        self.update(self._snapshot)

    def __str__(self):
        for data in self._root.iterfind("data"):
            name = data.attrib["name"]
            value = data.find("value")
            new_value = self.get(name)
            if new_value is not None:
                value.text = new_value
        # Call with `unicode` encoding will return string, with other will return bytes
        return ElementTree.tostring(self._root, encoding="unicode")

    def save_to_file(self, file: Path):
        file.write_bytes(str(self).encode())
