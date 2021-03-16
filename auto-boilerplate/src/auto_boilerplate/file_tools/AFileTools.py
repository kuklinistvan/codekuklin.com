import os

from .IFileTools import IFileTools


class AFileTools(IFileTools):
    def does_file_exist(self, path: str) -> bool:
        return os.path.exists(path)
