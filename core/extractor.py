import ast
import os
from typing import List, Dict


class PyAstExtractor:
    def __init__(self, path: str | os.PathLike):
        self.path = path
        self.name = self._remove_extension(os.path.basename(path))
        self.tree = self._get_tree()

    def _remove_extension(self, filename) -> str:
        return os.path.splitext(filename)[0]

    def _get_tree(self) -> ast.Module:
        with open(self.path, "r") as source:
            return ast.parse(source.read())

    def get_functions(self) -> List[str]:
        """Extract all top-level function nodes from the AST."""
        return [node for node in self.tree.body if isinstance(node, ast.FunctionDef)]

    def get_classes(self) -> List[str]:
        """Extract all top-level class nodes from the AST."""
        return [node for node in self.tree.body if isinstance(node, ast.ClassDef)]

    def get_imports(self) -> List[str]:
        """Extract all top-level imported modules nodes from the AST."""
        return [node for node in self.tree.body if isinstance(node, ast.Import)]

    def get_dependencies(self) -> Dict[str, List[str]]:
        """Extract all dependencies (imports, functions, classes) from the AST."""
        return {
            "imports": self.get_imports(),
            "functions": self.get_functions(),
            "classes": self.get_classes(),
        }
