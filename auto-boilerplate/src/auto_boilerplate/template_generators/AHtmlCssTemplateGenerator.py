import abc
import os
from typing import List

from auto_boilerplate.file_tools.FileTemplate import FileTemplate
from auto_boilerplate.template_generators.ATemplateGenerator import ATemplateGenerator


class AHtmlCssTemplateGenerator(ATemplateGenerator):
    _names: List[str]

    def __init__(self, names: List[str], project_root: str) -> None:
        super().__init__(project_root)
        self._names = names

    def generate_templates(self) -> List[FileTemplate]:
        result: List[FileTemplate] = []

        for name in self._names:
            result += self._generate_html_scss_templates(
                self._html_folder_path_relto_project_root(),
                self._sass_folder_path_relto_project_root(),
                name,
                self._css_prefix()
            )

        return result

    @staticmethod
    def _generate_html_with_wrapper_only(css_name: str) -> str:
        return '<div class="{}-wrapper">\n\n</div>'.format(css_name)

    @staticmethod
    def _generate_html_scss_templates(html_folder_path: str, sass_folder_path: str, name: str, css_prefix: str) -> \
            List[FileTemplate]:

        result: List[FileTemplate] = []

        AHtmlCssTemplateGenerator._make_template_if_file_does_not_exist(
            result,
            html_folder_path + "/" + name + ".html",
            AHtmlCssTemplateGenerator._generate_html_with_wrapper_only(
                AHtmlCssTemplateGenerator._css_name(css_prefix + name))
        )

        AHtmlCssTemplateGenerator._make_template_if_file_does_not_exist(
            result,
            sass_folder_path + "/" + name.replace("_", "-") + ".scss",
            ""
        )

        return result

    @staticmethod
    def _make_template_if_file_does_not_exist(target: List[FileTemplate], path: str, content: str) -> None:
        if not os.path.exists(path):
            return target.append(FileTemplate(AHtmlCssTemplateGenerator._slash_purify(path), content))

    @staticmethod
    def _css_name(name: str) -> str:
        return name.replace("_", "-")

    @staticmethod
    def _slash_purify(path: str) -> str:
        new_path: str = path
        while "//" in new_path:
            new_path = new_path.replace("//", "/")

        return new_path

    @abc.abstractmethod
    def _html_folder_path_relto_project_root(self) -> str:
        raise NotImplementedError()

    @abc.abstractmethod
    def _sass_folder_path_relto_project_root(self) -> str:
        raise NotImplementedError()

    @abc.abstractmethod
    def _css_prefix(self) -> str:
        raise NotImplementedError()
