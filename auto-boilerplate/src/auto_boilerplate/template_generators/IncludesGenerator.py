from typing import List

from auto_boilerplate.template_generators.AHtmlCssTemplateGenerator import AHtmlCssTemplateGenerator


class IncludesGenerator(AHtmlCssTemplateGenerator):

    def __init__(self, names: List[str], project_root: str) -> None:
        super().__init__(names, project_root)

    def _html_folder_path_relto_project_root(self) -> str:
        return "_includes"

    def _sass_folder_path_relto_project_root(self) -> str:
        return "_sass/includes"

    def _css_prefix(self) -> str:
        return ""
