import os
from typing import List

import yaml
from auto_boilerplate.template_generators.ITemplateGenerator import ITemplateGenerator
from auto_boilerplate.file_tools.FileTemplate import FileTemplate
from auto_boilerplate.template_generators.IncludesGenerator import IncludesGenerator
from auto_boilerplate.template_generators.LayoutsGenerator import LayoutsGenerator
from auto_boilerplate.template_generators.WrappersScssGenerator import WrappersScssGenerator
from auto_boilerplate.template_generators.XkcdMetadataGenerator import XkcdMetadataGenerator


class Data:
    project_root: str
    includes: List[str]
    layouts: List[str]
    xkcds: List[int]

    def __init__(self, project_root: str, includes: List[str], layouts: List[str], xkcds: List[int]):
        self.project_root = project_root
        self.includes = includes
        self.layouts = layouts
        self.xkcds = xkcds

    @staticmethod
    def from_yaml(yaml_path: str):
        yml_dir = os.path.dirname(os.path.abspath(yaml_path))

        with open(yaml_path, 'r') as stream:
            yaml_obj = yaml.safe_load(stream)

        return Data(yml_dir, yaml_obj['includes'], yaml_obj['layouts'], yaml_obj['xkcds'])

    def get_file_list_to_be_created(self) -> List[FileTemplate]:
        result: List[FileTemplate] = []
        generators: List[ITemplateGenerator] = [
            IncludesGenerator(self.includes, self.project_root),
            LayoutsGenerator(self.layouts, self.project_root),
            WrappersScssGenerator(self.includes, self.layouts, self.project_root),
            XkcdMetadataGenerator(self.xkcds, self.project_root)
        ]

        for generator in generators:
            result += generator.generate_templates()

        return result

