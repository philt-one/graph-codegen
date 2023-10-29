import ast
from typing import List


def unparse_node(node: ast.AST) -> str:
    """Return the source code from an AST node."""
    return ast.unparse(node)


def node_name(node: ast.AST) -> str | List[str]:
    """Retrieves the name(s) of an AST node."""
    match type(node):
        case ast.Import:
            return [alias.name for alias in node.names]
        case ast.ImportFrom:
            return [f"{node.module}.{alias.name}" for alias in node.names]
        case ast.FunctionDef | ast.ClassDef:
            return node.name
        case ast.Assign:
            return [target.name for target in node.targets]
        case _:
            raise Exception(f"{type(node)} not supported yet")
