from abc import abstractmethod


class IFileTools:

    @abstractmethod
    def does_file_exist(self, path: str) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def create_if_does_not_exist(self, path: str):
        raise NotImplementedError()

    @abstractmethod
    def overwrite(self, path: str, content: str):
        raise NotImplementedError()