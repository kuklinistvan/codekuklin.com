from typing import List

from auto_boilerplate.file_tools.FileTemplate import FileTemplate
from auto_boilerplate.template_generators.ATemplateGenerator import ATemplateGenerator

from urllib.request import urlopen

import json
import yaml


class XkcdMetadataGenerator(ATemplateGenerator):
    _comic_ids: List[int]

    def __init__(self, comic_ids: List[int], project_root: str):
        super().__init__(project_root)
        self._comic_ids = comic_ids

    def generate_templates(self) -> List[FileTemplate]:
        yaml_content: str = ""

        if input("Type y, if you are okay with contacting xkcd.com for metadata: ") == "y":
            for comic_id in self._comic_ids:
                yaml_content += \
                    XkcdMetadataGenerator._convert_xkcd_json_to_yaml(
                        XkcdMetadataGenerator._get_json_of_xkcd(comic_id))

            return [FileTemplate(self._project_root + "/_data/xkcd.yml", yaml_content)]

        else:
            return []

    @staticmethod
    def _convert_xkcd_json_to_yaml(json_in: str) -> str:
        json_data = json.loads(json_in)
        yaml_out = {str(json_data['num']): json_data}
        return yaml.dump(yaml_out)

    @staticmethod
    def _get_json_of_xkcd(id: int) -> str:
        return urlopen("https://xkcd.com/" + str(id) + "/info.0.json").read().decode("utf-8")
