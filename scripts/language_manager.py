import json


class LanguageManager:
    def initialize(self, languages_file_path):
        with open(languages_file_path, "rb") as f:
            self.languages = json.load(f)

    def get_language_code(self, language_name):
        language_name = language_name.lower()
        for code, name in self.languages:
            if name.lower() == language_name:
                return code

    def get_language_name(self, language_code):
        for code, name in self.languages:
            if code == language_code:
                return name


language_manager = LanguageManager()
