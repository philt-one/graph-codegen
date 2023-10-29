import ast
import os


class PyAstExtractor:
    def __init__(self, path: str | os.PathLike):
        self.path = path
        self.name = self._remove_extension(os.path.basename(path))
        self.tree = self.get_tree()
        self.body = self.tree.body

    def _remove_extension(self, filename) -> str:
        return os.path.splitext(filename)[0]

    def get_tree(self) -> ast.Module:
        with open(self.path, "r") as source:
            return ast.parse(source.read())
