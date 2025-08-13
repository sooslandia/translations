from pathlib import Path
from typing import Annotated

from pydantic import AfterValidator, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

AbsolutePath = Annotated[Path, AfterValidator(lambda p: p.resolve())]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
    repository_dir: AbsolutePath
    github_token: SecretStr = ""
    projects_dir: AbsolutePath
    base_commit_sha: str
    email_address: str

    @property
    def projects_file(self) -> Path:
        return self.repository_dir / "projects.yml"

    @property
    def workspace_dir(self) -> Path:
        return self.repository_dir / "workspace"

    @property
    def source_repositories_dir(self) -> Path:
        return self.workspace_dir / "repos"

    @property
    def preview_dir(self) -> Path:
        return self.workspace_dir / "preview"

    @property
    def git_askpass(self) -> Path:
        return self.repository_dir / "sltt/git_askpass.py"

    @property
    def languages_file_path(self) -> Path:
        return self.repository_dir / "languages.json"

    @property
    def error_messages_file_path(self) -> Path:
        return self.repository_dir / "sltt-errors.txt"


config = Settings()
__all__ = ["config"]
