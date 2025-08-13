import json
from pathlib import Path


class LanguageManager:
    def __init__(self, languages_file_path: Path):
        self.languages_file_path = languages_file_path
        self._languages = {}
        self._initialized = False

    def _initialize(self):
        if self._initialized:
            return
        self._languages = json.loads(self.languages_file_path.read_bytes())
        self._initialized = True

    def get_language_code(self, language_name: str) -> str | None:
        self._initialize()
        language_name = language_name.lower()
        for code, name in self._languages.items():
            if name == language_name:
                return code

    def get_language_name(self, language_code: str) -> str | None:
        self._initialize()
        return self._languages.get(language_code, None)
