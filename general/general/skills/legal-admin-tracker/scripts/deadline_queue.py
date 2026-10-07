#!/usr/bin/env python3
"""Build urgent-first deadline queue from CSV."""

import argparse
import csv
from datetime import date, datetime
from pathlib import Path


def parse_date(s: str):
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except Exception:
        return None


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()

    today = date.today()
    rows = []
    with open(args.input, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            due = parse_date((r.get("due_date") or "").strip())
            days = (due - today).days if due else 10**9
            rows.append((days, r))

    rows.sort(key=lambda x: x[0])

    lines = ["# Deadline Queue", ""]
    for days, r in rows:
        due = r.get("due_date", "")
        item = r.get("item", "")
        status = r.get("status", "")
        if days == 10**9:
            urgency = "unknown-date"
        elif days < 0:
            urgency = "overdue"
        elif days <= 7:
            urgency = "urgent"
        else:
            urgency = "normal"
        lines.append(f"- [{urgency}] {item} | due={due or 'unknown'} | status={status}")

    Path(args.out).write_text("\n".join(lines) + "\n")
    print(f"Wrote deadline queue: {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
