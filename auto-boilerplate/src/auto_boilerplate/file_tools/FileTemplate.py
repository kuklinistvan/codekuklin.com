class FileTemplate:
    path: str
    content: str

    def __init__(self, path: str, content: str) -> None:
        self.path = path
        self.content = content