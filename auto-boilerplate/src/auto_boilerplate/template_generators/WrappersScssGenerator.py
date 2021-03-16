from typing import List

import auto_boilerplate.template_generators.ATemplateGenerator
from auto_boilerplate.file_tools.FileTemplate import FileTemplate


class WrappersScssGenerator(auto_boilerplate.template_generators.ATemplateGenerator.ATemplateGenerator):
    _includes: List[str]
    _layouts: List[str]

    def __init__(self, includes: List[str], layouts: List[str], project_root: str) -> None:
        super().__init__(project_root)
        self._includes = includes
        self._layouts = layouts

    def generate_templates(self) -> List[FileTemplate]:
        return [FileTemplate(self._project_root + "/_sass/wrappers.scss", self.generate())]

    def generate(self) -> str:
        result = ""

        for layout in self._layouts:
            dashed_layout = layout.replace("_", "-")

            result += '.layout-{}-wrapper {{\n'.format(dashed_layout)
            result += '    @import "layouts/{}";\n'.format(dashed_layout)
            result += "}\n\n"

        for include in self._includes:
            dashed_include = include.replace("_", "-")

            result += '.{}-wrapper {{\n'.format(dashed_include)
            result += '    @import "includes/{}";\n'.format(dashed_include)
            result += '}\n\n'

        return result
