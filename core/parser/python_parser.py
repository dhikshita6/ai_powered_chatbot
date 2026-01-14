# # # import ast
# # # from pathlib import Path


# # # class FunctionVisitor(ast.NodeVisitor):
# # #     def __init__(self):
# # #         self.functions = []

# # #     def visit_FunctionDef(self, node):
# # #         self.functions.append({
# # #             "name": node.name,
# # #             "lineno": node.lineno,
# # #             "has_docstring": ast.get_docstring(node) is not None
# # #         })
# # #         self.generic_visit(node)


# # # class PythonParser:
# # #     """
# # #     AST-based Python parser that extracts function information.
# # #     """

# # #     def parse_file(self, path):
# # #         path = Path(path)
# # #         source = path.read_text(encoding="utf-8")
# # #         tree = ast.parse(source)

# # #         visitor = FunctionVisitor()
# # #         visitor.visit(tree)

# # #         return {
# # #             "file": str(path),
# # #             "functions": visitor.functions,
# # #             "has_docstring": ast.get_docstring(tree) is not None
# # #         }

# # import ast
# # import textwrap
# # from pathlib import Path


# # class PythonParser:
# #     def parse_file(self, path):
# #         path = Path(path)
# #         source = path.read_text(encoding="utf-8")

# #         # ✅ Safety: normalize indentation
# #         source = textwrap.dedent(source)

# #         try:
# #             tree = ast.parse(source)
# #         except (IndentationError, SyntaxError) as e:
# #             # ❌ Do not crash the app
# #             return {
# #                 "file": str(path),
# #                 "functions": [],
# #                 "error": str(e)
# #             }

# #         functions = []
# #         for node in ast.walk(tree):
# #             if isinstance(node, ast.FunctionDef):
# #                 functions.append({
# #                     "name": node.name,
# #                     "params": [a.arg for a in node.args.args],
# #                     "lineno": node.lineno,
# #                     "docstring": ast.get_docstring(node)
# #                 })

# #         return {
# #             "file": str(path),
# #             "functions": functions
# #         }
# # core/parser/python_parser.py

# import ast
# from pathlib import Path
# from typing import List, Dict


# class PythonParser:
#     """
#     AST-based Python parser that extracts function metadata.
#     """

#     def parse_file(self, file_path: str) -> Dict:
#         path = Path(file_path)
#         source = path.read_text(encoding="utf-8")

#         try:
#             tree = ast.parse(source)
#         except (SyntaxError, IndentationError) as e:
#             return {
#                 "file_path": str(path),
#                 "functions": [],
#                 "error": str(e),
#             }

#         functions = []

#         for node in ast.walk(tree):
#             if isinstance(node, ast.FunctionDef):
#                 functions.append({
#                     "name": node.name,
#                     "args": [{"name": a.arg} for a in node.args.args],
#                     "has_docstring": ast.get_docstring(node) is not None,
#                     "docstring": ast.get_docstring(node),
#                     "start_line": node.lineno,
#                 })

#         return {
#             "file_path": str(path),
#             "functions": functions,
#         }


# def parse_path(path: str) -> List[Dict]:
#     """
#     Parse all Python files in a directory.
#     """
#     base = Path(path)
#     parser = PythonParser()
#     results = []

#     for py_file in base.rglob("*.py"):
#         results.append(parser.parse_file(py_file))

#     return results
import ast
from pathlib import Path

def parse_file(path):
    source = Path(path).read_text(encoding="utf-8")
    tree = ast.parse(source)

    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append({
                "name": node.name,
                "args": [{"name": a.arg, "annotation": None} for a in node.args.args],
                "returns": None,
                "has_docstring": ast.get_docstring(node) is not None,
                "docstring": ast.get_docstring(node),
                "start_line": node.lineno,
                "indent": node.col_offset
            })

    return {
        "file_path": str(path),
        "functions": functions
    }

def parse_path(path):
    results = []
    for file in Path(path).rglob("*.py"):
        results.append(parse_file(file))
    return results
