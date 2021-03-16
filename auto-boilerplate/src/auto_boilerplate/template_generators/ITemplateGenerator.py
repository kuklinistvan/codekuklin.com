import abc
from typing import List

from auto_boilerplate.file_tools.FileTemplate import FileTemplate


class ITemplateGenerator:
    @abc.abstractmethod
    def generate_templates(self) -> List[FileTemplate]:
        raise NotImplementedError()