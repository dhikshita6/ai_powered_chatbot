# import subprocess
# from radon.complexity import cc_visit
# from radon.metrics import mi_visit

# from core.parser.python_parser import parse_file
# from core.docstring_engine.generator import generate_docstring


# def review_file(path):
#     code = path.read_text()
#     tree, items = parse_file(path)

#     # ---- Metrics ----
#     complexity = sum(c.complexity for c in cc_visit(code))
#     maintainability = mi_visit(code, False)

#     issues = []

#     if complexity > 10:
#         issues.append(("warning", "High cyclomatic complexity"))

#     if maintainability < 65:
#         issues.append(("warning", "Low maintainability index"))

#     # ---- Docstring validation (PEP-257) ----
#     pydoc = subprocess.run(
#         ["pydocstyle", str(path)],
#         capture_output=True,
#         text=True
#     ).stdout

#     if pydoc:
#         issues.append(("info", "PEP-257 docstring issues found"))

#     # ---- Docstring previews ----
#     previews = []
#     for item in items:
#         if item["type"] == "function" and not item["has_docstring"]:
#             previews.append({
#                 "name": item["name"],
#                 "lineno": item["lineno"],
#                 "docstring": generate_docstring(item["name"])
#             })

#     return {
#         "file": str(path),
#         "issues": issues,
#         "docstring_previews": previews,
#         "complexity": complexity,
#         "maintainability": maintainability
#     }
import ast
import subprocess
from radon.complexity import cc_visit
from radon.metrics import mi_visit

from core.parser.python_parser import parse_file
from core.docstring_engine.generator import generate_docstring


def review_file(path):
    _, functions = parse_file(path)

    previews = []
    for fn in functions:
        if not fn["has_docstring"]:
            previews.append({
                "name": fn["name"],
                "lineno": fn["lineno"],
                "docstring": generate_docstring(fn["name"])
            })

    return {"docstring_previews": previews}


def validate_file(path):
    results = []

    # Syntax check
    try:
        ast.parse(path.read_text())
        results.append(("success", "Syntax is valid"))
    except SyntaxError as e:
        results.append(("error", f"Syntax error: {e}"))
        return results

    # PEP-257 check
    pydoc = subprocess.run(
        ["python", "-m", "pydocstyle", str(path)],
        capture_output=True,
        text=True
    ).stdout

    if pydoc:
        results.append(("warning", "PEP-257 docstring issues found"))
    else:
        results.append(("success", "No PEP-257 issues"))

    return results


def compute_metrics(path):
    code = path.read_text()

    return {
        "complexity": sum(c.complexity for c in cc_visit(code)),
        "maintainability": mi_visit(code, False)
    }
