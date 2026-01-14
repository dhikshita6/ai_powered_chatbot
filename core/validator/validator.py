# def quality_score(complexity, maintainability, issues):
#     score = 100
#     score -= complexity * 2
#     score -= max(0, 70 - maintainability)
#     score -= len(issues) * 3
#     return max(score, 0)
import ast
import radon.complexity as cc


def validate_docstrings(path):
    """
    Validate presence of docstrings in functions.
    Returns a list of issues.
    """
    with open(path, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)
    errors = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if not ast.get_docstring(node):
                errors.append({
                    "function": node.name,
                    "message": "Missing docstring",
                    "line": node.lineno
                })

    return errors


def compute_complexity(source):
    """
    Compute cyclomatic complexity using radon.
    """
    return [
        {
            "name": block.name,
            "complexity": block.complexity
        }
        for block in cc.cc_visit(source)
    ]


def compute_maintainability(source):
    """
    Dummy maintainability score (can be upgraded later).
    """
    return 75.0
