#!/usr/bin/env python3
"""Export issue-log to CSV, markdown, or XLSX"""
"""Codex created this script"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from xlsx_utils import read_xlsx, write_xlsx

FIELDS = [
    "invoice_id",
    "line_id",
    "matter_id",
    "matter_name",
    "timekeeper_name",
    "timekeeper_title",
    "issue_label",
    "issue_summary",
    "rule_or_term_reference",
    "evidence_reference",
    "billed_value",
    "challenged_value",
    "confidence",
    "recommended_action",
    "status",
    "notes",
]


def load_records(path: Path) -> list[dict[str, str]]:
    suffix = path.suffix.lower()
    if suffix == ".json":
        return [dict(item) for item in json.loads(path.read_text(encoding="utf-8"))]
    if suffix == ".xlsx":
        return read_xlsx(path)
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def normalize(records: list[dict[str, str]]) -> list[dict[str, str]]:
    normalized = []
    for record in records:
        normalized.append({field: str(record.get(field, "")) for field in FIELDS})
    return normalized


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path: Path, rows: list[dict[str, str]]) -> None:
    headers = [
        "Invoice ID",
        "Line ID",
        "Matter",
        "Timekeeper",
        "Issue Label",
        "Issue Summary",
        "Rule or Term",
        "Evidence",
        "Billed Value",
        "Challenged Value",
        "Confidence",
        "Recommended Action",
        "Status",
    ]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        values = [
            row["invoice_id"],
            row["line_id"],
            row["matter_name"] or row["matter_id"],
            row["timekeeper_name"],
            row["issue_label"],
            row["issue_summary"],
            row["rule_or_term_reference"],
            row["evidence_reference"],
            row["billed_value"],
            row["challenged_value"],
            row["confidence"],
            row["recommended_action"],
            row["status"],
        ]
        lines.append("| " + " | ".join(value.replace("\n", " ") for value in values) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    rows = normalize(load_records(input_path))

    if output_path.suffix.lower() == ".xlsx":
        write_xlsx(output_path, FIELDS, [[row[field] for field in FIELDS] for row in rows], "Issue Log")
    elif output_path.suffix.lower() in {".md", ".markdown"}:
        write_markdown(output_path, rows)
    elif output_path.suffix.lower() == ".json":
        output_path.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    else:
        write_csv(output_path, rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
