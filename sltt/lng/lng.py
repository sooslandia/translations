import json
from pathlib import Path

from sltt.lng.exceptions import LngLoadingError, LngValidationError
from sltt.lng.language_manager import LanguageManager
from sltt.settings import config


class Lng(dict):
    language_manager = LanguageManager(config.languages_file_path)

    def __init__(self, culture: str, language: str):
        self.culture = culture
        self.language = language
        self.validate()

    def validate(self):
        language_name = self.language_manager.get_language_name(self.culture)
        if language_name is None:
            raise LngValidationError(f'Unknown culture: "{self.culture[:50]}"')
        if language_name != self.language:
            raise LngValidationError(
                f'Invalid language name. Language for culture "{self.culture}" must be '
                f'"{language_name}, not "{self.language[:50]}"'
            )

    @classmethod
    def load_from_file(cls, file: Path) -> "Lng":
        data = file.read_bytes()
        try:
            lng_data = json.loads(data)
        except Exception:
            raise LngLoadingError("Failed to load json object")
        culture = lng_data.pop("Culture", "")
        language = lng_data.pop("Language", "")
        lng = cls(culture=culture, language=language)
        lng |= lng_data
        return lng

    def __str__(self):
        lng_data = {"Culture": self.culture, "Language": self.language} | self
        return json.dumps(lng_data, ensure_ascii=False, indent=2, sort_keys=True)

    def save_to_file(self, file: Path):
        file.write_bytes(str(self).encode())
