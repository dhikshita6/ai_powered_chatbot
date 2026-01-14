from pathlib import Path
from core.review_engine.ai_review import review_file
from core.reporter.coverage_reporter import write_report

def scan(path="."):
    for f in Path(path).rglob("*.py"):
        review_file(f)
    print("Scan complete")

def report(path="."):
    write_report(Path(path))
