from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import List

import pandas as pd
from rich.console import Console
from rich.table import Table

from integrity_data_foundation.validators import validate_dataframe, normalize_dataframe, ValidationIssue

console = Console()

def _issues_to_table(issues: List[ValidationIssue]) -> Table:
    t = Table(title="Validation Report")
    t.add_column("Row", justify="right")
    t.add_column("Severity")
    t.add_column("Field")
    t.add_column("Message")
    t.add_column("Value")
    for i in issues:
        t.add_row(str(i.row_index), i.severity, i.field, i.message, "" if i.value is None else str(i.value))
    return t

def run(input_dir: Path, output_dir: Path) -> int:
    input_path = input_dir / "integrity_sample.csv"
    if not input_path.exists():
        console.print(f"[red]Missing input file:[/red] {input_path}")
        return 2

    df = pd.read_csv(input_path)
    _, issues = validate_dataframe(df)

    output_dir.mkdir(parents=True, exist_ok=True)

    issues_path = output_dir / "validation_issues.json"
    issues_json = [
        {"row_index": i.row_index, "field": i.field, "severity": i.severity, "message": i.message, "value": i.value}
        for i in issues
    ]
    issues_path.write_text(json.dumps(issues_json, indent=2), encoding="utf-8")

    console.print(_issues_to_table(issues))

    norm = normalize_dataframe(df)
    norm_path = output_dir / "normalized_integrity_data.csv"
    norm.to_csv(norm_path, index=False)

    has_errors = any(i.severity == "error" for i in issues)
    if has_errors:
        console.print("[yellow]Completed with validation errors. Review the report before using outputs.[/yellow]")
        return 1

    console.print("[green]Completed successfully.[/green]")
    return 0

def main() -> None:
    p = argparse.ArgumentParser(description="Integrity Data Foundation baseline pipeline")
    p.add_argument("--input", required=True, help="Input directory containing integrity_sample.csv")
    p.add_argument("--output", required=True, help="Output directory for normalized data and reports")
    args = p.parse_args()
    code = run(Path(args.input), Path(args.output))
    raise SystemExit(code)

if __name__ == "__main__":
    main()
