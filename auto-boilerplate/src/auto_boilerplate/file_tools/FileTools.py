from .AFileTools import AFileTools
from pathlib import Path


class FileTools(AFileTools):
    def create_if_does_not_exist(self, path: str):
        Path(path).touch()

    def overwrite(self, path: str, content: str):
        with open(path, "w") as stream:
            stream.write(content)
