#!/usr/bin/env python3
"""Normalize common billing exports into a schema"""
"""Codex created this script"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from xlsx_utils import read_xlsx, write_xlsx

CANONICAL_FIELDS = [
    "source_file",
    "source_record_index",
    "invoice_id",
    "invoice_status",
    "invoice_date",
    "billing_period",
    "currency",
    "matter_id",
    "matter_name",
    "matter_type",
    "matter_phase",
    "line_id",
    "line_type",
    "timekeeper_name",
    "timekeeper_title",
    "timekeeper_office",
    "timekeeper_approval_status",
    "hours",
    "units",
    "standard_rate",
    "approved_rate",
    "billed_rate",
    "net_effective_rate",
    "billed_amount",
    "adjusted_amount",
    "paid_amount",
    "discount_amount",
    "tax_amount",
    "expense_amount",
    "utbms_code",
    "ledes_code",
    "narrative",
    "budget_phase",
]

ALIASES = {
    "invoice number": "invoice_id",
    "invoice no": "invoice_id",
    "invoice_id": "invoice_id",
    "invoice status": "invoice_status",
    "invoice date": "invoice_date",
    "billing period": "billing_period",
    "currency": "currency",
    "matter id": "matter_id",
    "matter number": "matter_id",
    "matter": "matter_name",
    "matter name": "matter_name",
    "matter type": "matter_type",
    "phase": "matter_phase",
    "line id": "line_id",
    "line number": "line_id",
    "line type": "line_type",
    "type": "line_type",
    "timekeeper": "timekeeper_name",
    "timekeeper name": "timekeeper_name",
    "keeper name": "timekeeper_name",
    "role": "timekeeper_title",
    "title": "timekeeper_title",
    "timekeeper title": "timekeeper_title",
    "office": "timekeeper_office",
    "approval status": "timekeeper_approval_status",
    "hours": "hours",
    "units": "units",
    "std rate": "standard_rate",
    "standard rate": "standard_rate",
    "approved rate": "approved_rate",
    "agreed rate": "approved_rate",
    "rate": "billed_rate",
    "billed rate": "billed_rate",
    "effective rate": "net_effective_rate",
    "amount": "billed_amount",
    "billed amount": "billed_amount",
    "adjusted amount": "adjusted_amount",
    "paid amount": "paid_amount",
    "discount": "discount_amount",
    "tax": "tax_amount",
    "expense": "expense_amount",
    "utbms": "utbms_code",
    "task code": "utbms_code",
    "ledes code": "ledes_code",
    "description": "narrative",
    "narrative": "narrative",
    "budget phase": "budget_phase",
}


def normalize_header(value: str) -> str:
    key = " ".join(value.strip().lower().replace("_", " ").split())
    return ALIASES.get(key, "")


def load_csv_like(path: Path, delimiter: str | None = None) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        sample = handle.read(4096)
        handle.seek(0)
        if delimiter is None:
            delimiter = "|" if "|" in sample.splitlines()[0] else None
        if delimiter is None:
            try:
                delimiter = csv.Sniffer().sniff(sample).delimiter
            except csv.Error:
                delimiter = ","
        reader = csv.DictReader(handle, delimiter=delimiter)
        return [dict(row) for row in reader]


def load_json(path: Path) -> list[dict[str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return [dict(item) for item in data]
    if isinstance(data, dict):
        for key in ("rows", "records", "data"):
            if isinstance(data.get(key), list):
                return [dict(item) for item in data[key]]
    raise ValueError("Expected a list of records or an object with rows/records/data")


def load_rows(path: Path, sheet_name: str | None = None) -> list[dict[str, str]]:
    suffix = path.suffix.lower()
    if suffix in {".csv", ".tsv"}:
        return load_csv_like(path, "\t" if suffix == ".tsv" else None)
    if suffix in {".txt", ".ledes"}:
        return load_csv_like(path, "|")
    if suffix == ".json":
        return load_json(path)
    if suffix == ".xlsx":
        return read_xlsx(path, sheet_name)
    raise ValueError(f"Unsupported input type: {suffix}")


def normalize_rows(rows: list[dict[str, str]], source_file: str) -> list[dict[str, str]]:
    normalized: list[dict[str, str]] = []
    for index, row in enumerate(rows, start=1):
        result = {field: "" for field in CANONICAL_FIELDS}
        result["source_file"] = source_file
        result["source_record_index"] = str(index)
        extras = []
        for key, value in row.items():
            canonical = normalize_header(str(key))
            if canonical:
                result[canonical] = "" if value is None else str(value)
            elif value not in (None, ""):
                extras.append(f"{key}={value}")
        if extras:
            result["narrative"] = (result["narrative"] + " | " if result["narrative"] else "") + "; ".join(extras)
        normalized.append(result)
    return normalized


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CANONICAL_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Path to the source file")
    parser.add_argument("--output", required=True, help="Path to the normalized output")
    parser.add_argument("--sheet", help="Workbook sheet name for XLSX input")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    rows = load_rows(input_path, args.sheet)
    normalized = normalize_rows(rows, input_path.name)

    if output_path.suffix.lower() == ".json":
        output_path.write_text(json.dumps(normalized, indent=2), encoding="utf-8")
    elif output_path.suffix.lower() == ".xlsx":
        write_xlsx(output_path, CANONICAL_FIELDS, [[row[field] for field in CANONICAL_FIELDS] for row in normalized], "Normalized")
    else:
        write_csv(output_path, normalized)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
