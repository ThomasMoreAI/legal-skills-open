#!/usr/bin/env python3
"""
Generate a Markdown compliance checklist for an Israeli tender.

Usage:
    python compliance_checklist.py --tender "Example Tender 12/2026" \
        --statutory "רישום ברשם החברות" "אישור ניהול ספרים" \
        --discretionary "ניסיון של 3 שנים" "מחזור שנתי 2M NIS"

Output:
    Prints a filled Markdown table the user can paste into a proposal draft.

Append "::Ready", "::Needs work" or "::Blocker" to a condition to set its status
(default: Needs work). Any Blocker prints a STOP line.

This script does not parse tender PDFs. It is a deterministic formatter.
The parsing, extraction, and classification of threshold conditions is the
responsibility of the skill instructions, not this helper.
"""

import argparse
import sys
from datetime import date


STATUSES = {"ready": "Ready", "needs work": "Needs work", "blocker": "Blocker"}


def split_status(condition: str) -> tuple[str, str]:
    """A condition may end with "::Ready", "::Needs work" or "::Blocker"; default is Needs work."""
    if "::" in condition:
        text, _, status = condition.rpartition("::")
        if status.strip().lower() in STATUSES:
            return text.strip(), STATUSES[status.strip().lower()]
    return condition, "Needs work"


def build_row(num: int, condition: str, kind: str) -> str:
    text, status = split_status(condition)
    return (
        f"| {num} | {text} | {kind} | "
        "_(fill in evidence document)_ | "
        f"_(fill in source)_ | {status} |"
    )


def build_table(statutory: list[str], discretionary: list[str]) -> str:
    header = (
        "| # | Condition (verbatim from tender) | Statutory or Discretionary | "
        "Evidence to attach | Source | Status |\n"
        "|---|----------------------------------|-----------------------------|"
        "---------------------|--------|--------|"
    )
    rows: list[str] = []
    counter = 1
    for cond in statutory:
        rows.append(build_row(counter, cond, "6(a) statutory"))
        counter += 1
    for cond in discretionary:
        rows.append(build_row(counter, cond, "6(b) discretionary"))
        counter += 1
    return header + "\n" + "\n".join(rows)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a tender compliance checklist as Markdown."
    )
    parser.add_argument(
        "--tender",
        required=True,
        help="Tender name or reference number for the checklist heading.",
    )
    parser.add_argument(
        "--statutory",
        nargs="*",
        default=[],
        help="Statutory threshold conditions extracted from the tender (Takana 6(a)).",
    )
    parser.add_argument(
        "--discretionary",
        nargs="*",
        default=[],
        help="Discretionary threshold conditions extracted from the tender (Takana 6(b)).",
    )
    args = parser.parse_args()

    if not args.statutory and not args.discretionary:
        print("No threshold conditions provided. Pass --statutory and/or --discretionary.", file=sys.stderr)
        return 1

    print(f"# Compliance Checklist - {args.tender}")
    print()
    print(f"_Generated on {date.today().isoformat()}_")
    print()
    print(build_table(args.statutory, args.discretionary))
    print()
    blockers = [c for c in args.statutory + args.discretionary if split_status(c)[1] == "Blocker"]
    if blockers:
        print(f"**STOP: {len(blockers)} blocker(s).** Do not continue drafting until each is resolved.")
        print()
    print("## Rule")
    print()
    print(
        "If any row is marked **Blocker**, stop and flag it before continuing to "
        "draft the proposal. A tender you cannot qualify for is not worth the "
        "drafting effort."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
