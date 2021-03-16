from .AFileTools import AFileTools

import os


class NoopFileTools(AFileTools):
    def create_if_does_not_exist(self, path: str):
        if self.does_file_exist(path):
            print("* ALREADY PRESENT: {}".format(path))
        else:
            print("* NEW, WOULD CREATE: {}".format(path))

    def overwrite(self, path: str, content: str):
        print("Would overwrite file on path {}".format(path))
        print("...with content:\n{}".format(content))
