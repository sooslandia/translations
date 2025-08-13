from typing import Annotated, Literal

from pydantic import BaseModel, Field, model_validator

from sltt.enums import Po2MdStageMode


class GlobPattern(BaseModel):
    type: Literal["glob"] = "glob"
    glob: str


class RegexPattern(BaseModel):
    type: Literal["regex"] = "regex"
    regex: str


Pattern = Annotated[GlobPattern | RegexPattern, Field(discriminator="type")]


class FSStage(BaseModel):
    source: str
    target: str


class CopyFileStage(FSStage):
    type: Literal["copy_file"] = "copy_file"


class CopyDirectoryContentsStage(FSStage):
    type: Literal["copy_directory_contents"] = "copy_directory_contents"
    pattern: str | None = None
    patterns: list[Pattern] = []
    recursive: bool = False

    @model_validator(mode="after")
    def validate_patterns(self):
        if self.pattern is None and not self.patterns:
            raise ValueError("Patterns must be specified")
        if self.pattern is not None and self.patterns:
            raise ValueError("pattern and patterns field must not be used together")
        return self

    def get_patterns(self) -> list[Pattern]:
        if self.pattern is not None:
            if isinstance(self.pattern, str):
                return [GlobPattern(glob=self.pattern)]
            return [self.pattern]
        return self.patterns


class ConvertLng2PotStage(BaseModel):
    type: Literal["convert_lng2pot"] = "convert_lng2pot"
    source_lng_file_path: str
    target_pot_file_path: str
    package: str


class ConvertMd2PotStage(BaseModel):
    type: Literal["convert_md2pot"] = "convert_md2pot"
    source_md_files_dir: str
    target_pot_files_dir: str
    package: str


class ConvertPo2PotStage(BaseModel):
    type: Literal["convert_po2pot"] = "convert_po2pot"
    source_po_file_path: str
    target_pot_file_path: str


class ConvertPo2LngStage(BaseModel):
    type: Literal["convert_po2lng"] = "convert_po2lng"
    source_po_files_dir: str
    target_lng_files_dir: str
    reference_lng_file_path: str
    include_files: Annotated[list[str], Field(default_factory=list)]
    exclude_files: Annotated[list[str], Field(default_factory=list)]

    @model_validator(mode="after")
    def validate_inclusions(self):
        if self.include_files and self.exclude_files:
            raise ValueError(
                "include_files and exclude_files are mutually exclusive params"
            )
        return self


class ConvertPo2MdBase(BaseModel):
    type: Literal["convert_po2md"] = "convert_po2md"
    base_md_files_dir: str
    ignore_base_changes: bool = False


class ConvertPo2MdSingle(ConvertPo2MdBase):
    mode: Literal[Po2MdStageMode.SINGLE] = Po2MdStageMode.SINGLE
    source_po_files_dir: str
    target_md_files_dir: str


class ConvertPo2MdMultiple(ConvertPo2MdBase):
    mode: Literal[Po2MdStageMode.MULTIPLE] = Po2MdStageMode.MULTIPLE
    source_docs_dir: str
    target_docs_dir: str
    excluded_dirs: Annotated[list[str], Field(default_factory=list)]


ConvertPo2MdStage = Annotated[
    ConvertPo2MdSingle | ConvertPo2MdMultiple, Field(discriminator="mode")
]


class ConvertMd2HtmlStage(BaseModel):
    type: Literal["convert_md2html"] = "convert_md2html"
    source_md_docs_dir: str
    target_html_docs_dir: str


class ConvertResx2PotStage(BaseModel):
    type: Literal["convert_resx2pot"] = "convert_resx2pot"
    source_components_dir: str
    target_pot_file_path: str
    package: str


class ConvertPo2ResxStage(BaseModel):
    type: Literal["convert_po2resx"] = "convert_po2resx"
    source_po_files_dir: str
    target_components_dir: str
    base_components_dir: str


Stage = Annotated[
    CopyFileStage
    | CopyDirectoryContentsStage
    | ConvertLng2PotStage
    | ConvertMd2PotStage
    | ConvertPo2PotStage
    | ConvertPo2LngStage
    | ConvertPo2MdStage
    | ConvertMd2HtmlStage
    | ConvertResx2PotStage
    | ConvertPo2ResxStage,
    Field(discriminator="type"),
]


class PullConfig(BaseModel):
    repository: str
    stages: list[Stage]


class PushConfig(BaseModel):
    repository: str
    stages: list[Stage]


class Project(BaseModel):
    name: str
    pull_configs: list[PullConfig]
    source_conversions: list[Stage]
    translation_conversions: list[Stage]
    push_configs: list[PushConfig]
    preview_config: list[Stage]
