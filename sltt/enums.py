from enum import IntFlag, StrEnum, auto


class PipelineType(IntFlag):
    PULL = auto()
    SOURCE_CONVERSIONS = auto()
    TRANSLATION_CONVERSIONS = auto()
    PUSH = auto()
    PREVIEW = auto()


class Po2MdStageMode(StrEnum):
    SINGLE = "single"
    MULTIPLE = "multiple"
