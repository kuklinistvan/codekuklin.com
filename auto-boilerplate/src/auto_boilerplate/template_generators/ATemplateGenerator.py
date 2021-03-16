import abc
from typing import List

from auto_boilerplate.file_tools.FileTemplate import FileTemplate
from auto_boilerplate.template_generators.ITemplateGenerator import ITemplateGenerator


class ATemplateGenerator(ITemplateGenerator):
    _project_root: str

    def __init__(self, project_root: str) -> None:
        self._project_root = project_root

    @abc.abstractmethod
    def generate_templates(self) -> List[FileTemplate]:
        raise NotImplementedError();
