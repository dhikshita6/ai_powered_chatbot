# class CoverageReporter:
#     def compute(self, parsed):
#         total = len(parsed["functions"])
#         documented = sum(1 for f in parsed["functions"] if f["docstring"])
#         return round((documented / total) * 100, 2) if total else 100.0
def compute_coverage(parsed_files, threshold=80):
    """
    Compute docstring coverage.
    """
    total_functions = 0
    documented = 0

    for file in parsed_files:
        for fn in file.get("functions", []):
            total_functions += 1
            if fn.get("has_docstring"):
                documented += 1

    coverage_percent = (
        round((documented / total_functions) * 100, 2)
        if total_functions > 0 else 0
    )

    return {
        "total_functions": total_functions,
        "documented": documented,
        "coverage_percent": coverage_percent,
        "meets_threshold": coverage_percent >= threshold
    }


def write_report(report, output_path):
    """
    Write coverage report to JSON file.
    """
    import json
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
