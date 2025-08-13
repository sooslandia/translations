from typing import Annotated, get_origin

from sltt import schema
from sltt.stages.base import BaseStage
from sltt.stages.fs import CopyDirectoryContentsStage, CopyFileStage
from sltt.stages.lng2pot import ConvertLng2PotStage
from sltt.stages.md2html import ConvertMd2HtmlStage
from sltt.stages.md2pot import ConvertMd2PotStage
from sltt.stages.po2lng import ConvertPo2LngStage
from sltt.stages.po2md import ConvertPo2MdStage
from sltt.stages.po2pot import ConvertPo2PotStage
from sltt.stages.po2resx import ConvertPo2ResxStage
from sltt.stages.resx2pot import ConvertResx2PotStage


class StageRegistry(dict):
    def get(self, key: schema.Stage) -> BaseStage | None:
        result = super().get(key.__class__, None)
        if result is not None:
            return result
        for k, v in self.items():
            origin = get_origin(k)
            if origin is not None and issubclass(origin, Annotated):
                k = k.__origin__
            if isinstance(key, k):
                return v
        return None


stage_registry: StageRegistry[schema.Stage, BaseStage] = StageRegistry(
    {
        schema.CopyFileStage: CopyFileStage,
        schema.CopyDirectoryContentsStage: CopyDirectoryContentsStage,
        schema.ConvertLng2PotStage: ConvertLng2PotStage,
        schema.ConvertMd2PotStage: ConvertMd2PotStage,
        schema.ConvertPo2LngStage: ConvertPo2LngStage,
        schema.ConvertPo2PotStage: ConvertPo2PotStage,
        schema.ConvertPo2MdStage: ConvertPo2MdStage,
        schema.ConvertResx2PotStage: ConvertResx2PotStage,
        schema.ConvertPo2ResxStage: ConvertPo2ResxStage,
        schema.ConvertMd2HtmlStage: ConvertMd2HtmlStage,
    }
)
