#!/usr/bin/env python3
"""
check_receipt.py — audit a `check` note's discovery coverage receipt before the
note goes out.

Every other gate in this skill is mechanical: the fetch proves the publisher,
the version check proves the text, the quote check proves the words. Discovery
had none, and discovery is where the only invisible failure lives. A `check`
whose quotes all verify is still wrong if nobody thought of the instrument, and
nothing downstream can tell — the note reads exactly like a complete one.

So this script checks the receipt, not the research. It cannot know whether the
right regulators were named. It can know that the row for regulators was filled
in rather than left blank, that a branch nobody worked says `unresolved` instead
of saying nothing, that a dynamic source consulted without an access date is
being reported as a permanent fact when it is a Tuesday fact, and that a
negative finding says which of the four kinds of nothing it is. Those are the
failures that survive review, because an incomplete receipt and a complete one
look the same at a glance.

The method version is read from references/discovery.md rather than written
here. A note recording a superseded method is a note that cannot be rerun
against the current one, which is the whole reason the version line exists.

Usage:
    python3 check_receipt.py <note.md>
    python3 check_receipt.py <note.md> --json <dir>/receipt.json

Exit 0 when the receipt is whole. Stdlib only.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REFERENCE = Path(__file__).resolve().parent.parent / "references" / "discovery.md"
METHOD_LINE = re.compile(r"Method version:\s*\*{0,2}(discovery/v\d+)")
# Found in the note however the note words the line around it.
METHOD_TOKEN = re.compile(r"discovery/v\d+")

# Section 6's table. The key is matched against the row's first cell, so a note
# may title a row more fully than the reference does.
REQUIRED_ROWS = (
    ("actor", "Actors and roles"),
    ("lifecycle", "Lifecycle"),
    ("regulator", "Regulators"),
    ("geographic", "Geographic perimeter"),
    ("pre market", "Pre-market permissions"),
    ("dynamic", "Dynamic official sources"),
    ("future", "Future-effective law"),
    ("feature", "Feature-dependent regimes"),
)
FEATURE_ROW = "feature"
STATUSES = {"complete", "partial", "unresolved"}
FEATURE_STATUSES = {"resolved", "unresolved"}
WORKED = {"complete", "partial", "resolved"}

# A row that says nothing is the failure section 6 names outright, and these are
# the ways a row says nothing while looking filled in.
PLACEHOLDERS = {"", "n a", "na", "none", "tbd", "to do", "see above", "as above"}

MONTHS = (
    "january|february|march|april|may|june|july|august|september|october"
    "|november|december"
)
DATE = re.compile(
    rf"\d{{4}}-\d{{2}}-\d{{2}}"
    rf"|\d{{1,2}}\s+(?:{MONTHS})\s+\d{{4}}"
    rf"|(?:{MONTHS})\s+\d{{1,2}},?\s+\d{{4}}",
    re.IGNORECASE,
)

FENCE = re.compile(r"^```.*?^```", re.MULTILINE | re.DOTALL)

# Section 7. The claim patterns are deliberately narrow: this fires on a stated
# negative finding, not on ordinary hedging.
NEGATIVE_CLAIM = re.compile(
    r"nothing (?:was )?found|found nothing|nothing (?:that )?catches"
    r"|no responsive|no applicable|no relevant instrument"
    r"|(?:is|are) not (?:caught|covered|regulated)",
    re.IGNORECASE,
)
CLASSIFIED = re.compile(
    r"exclud|exclusion|exempt|expressly outside"
    r"|element|not met on|supplied facts"
    r"|after the searches|searches (?:named|recorded|in the receipt)"
    r"|not investigated",
    re.IGNORECASE,
)

OMISSION = re.compile(r"omission challenge", re.IGNORECASE)
OMISSION_ANSWER_CHARS = 40


def normalise(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def receipt_rows(text: str) -> list[list[str]] | None:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if not line.lstrip().startswith("|"):
            continue
        header = cells(line)
        if normalise(header[0]) != "dimension":
            continue
        rows = []
        for candidate in lines[index + 1 :]:
            if not candidate.lstrip().startswith("|"):
                break
            row = cells(candidate)
            if all(set(cell) <= set("-: ") for cell in row):
                continue
            rows.append(row)
        return rows
    return None


def finding(code: str, message: str, row: str | None = None) -> dict:
    return {"finding": code, "row": row, "message": message}


def check_method(text: str, method: str) -> list[dict]:
    if method in text:
        return []
    found = METHOD_TOKEN.search(text)
    if found:
        return [
            finding(
                "method-superseded",
                f"The note records method {found.group(0)}; the current method is "
                f"{method}.\n  A note carrying a superseded method version cannot be "
                "rerun against this one.",
            )
        ]
    return [
        finding(
            "method-missing",
            f"The note does not record its discovery method version ({method}).\n"
            "  Without it, a later run cannot tell a re-check for amendments from a "
            "rerun of\n  the search itself.",
        )
    ]


def check_rows(rows: list[list[str]]) -> list[dict]:
    findings = []
    found: dict[str, list[str]] = {}
    for row in rows:
        if len(row) < 3:
            findings.append(
                finding(
                    "row-malformed",
                    f"A row has no status and evidence cells: {row[0] or '(unnamed)'}",
                    row[0] or None,
                )
            )
            continue
        label = normalise(row[0])
        for key, _name in REQUIRED_ROWS:
            if key in label:
                found.setdefault(key, row)
                break

    for key, name in REQUIRED_ROWS:
        row = found.get(key)
        if row is None:
            findings.append(
                finding(
                    "row-missing",
                    f"The receipt has no row for {name}.\n"
                    "  A dimension nobody searched is a branch nobody searched, and a "
                    "missing row\n  reads as an answered one.",
                    key,
                )
            )
            continue
        status = normalise(row[1])
        allowed = FEATURE_STATUSES if key == FEATURE_ROW else STATUSES
        if status not in allowed:
            findings.append(
                finding(
                    "row-status",
                    f"{name} has status {row[1] or '(blank)'!r}.\n"
                    f"  Use one of: {', '.join(sorted(allowed))}.",
                    key,
                )
            )
        if normalise(row[2]) in PLACEHOLDERS:
            findings.append(
                finding(
                    "row-evidence",
                    f"{name} carries no evidence.\n"
                    "  An unresolved row still says what was not worked; a worked row "
                    "names what\n  was searched. Neither is left blank.",
                    key,
                )
            )
            continue
        if status not in WORKED:
            continue
        dates = DATE.findall(row[2])
        if key == "dynamic" and not dates:
            findings.append(
                finding(
                    "row-undated",
                    f"{name} records no access date.\n"
                    "  A sanctions list checked in June is a June fact, and without "
                    "the date it\n  reads as a standing one.",
                    key,
                )
            )
        if key == "future" and len(dates) < 2:
            findings.append(
                finding(
                    "row-undated",
                    f"{name} records {'no dates' if not dates else 'only one date'}; "
                    "it needs the research\n  cutoff and the target date. A `check` is "
                    "dated at launch, not at research,\n  and the gap between the two "
                    "is what this row exists to show.",
                    key,
                )
            )
    return findings


def check_negatives(text: str) -> list[dict]:
    body = FENCE.sub("", text)
    findings = []
    for block in re.split(r"\n\s*\n", body):
        stripped = block.strip()
        if not stripped or not NEGATIVE_CLAIM.search(stripped):
            continue
        if CLASSIFIED.search(stripped):
            continue
        excerpt = re.sub(r"\s+", " ", stripped)[:120]
        findings.append(
            finding(
                "negative-unqualified",
                f"An unqualified negative finding:\n    {excerpt}\n"
                "  Say which of the four kinds of nothing this is — expressly "
                "excluded, test not\n  met on the supplied facts, nothing found after "
                "the searches named, or not\n  investigated. The last two are "
                "research and its absence, and they do not\n  read differently unless "
                "you write them differently.",
            )
        )
    return findings


def check_omission(text: str) -> list[dict]:
    body = FENCE.sub("", text)
    match = OMISSION.search(body)
    if match is None:
        return [
            finding(
                "challenge-missing",
                "The note does not record the omission challenge.\n"
                "  A fresh-context reviewer gets the receipt and the one-line conduct "
                "description,\n  and one question: name the regulator or regime most "
                "likely to be missing.\n  references/discovery.md section 8.",
            )
        ]
    # The phrase is usually a heading, so the answer is what follows it up to the
    # next one.
    rest = body[match.end() :]
    end = re.search(r"(?m)^#", rest)
    answer = re.sub(r"[\s:—–-]+", " ", rest[: end.start() if end else None]).strip()
    if len(answer) >= OMISSION_ANSWER_CHARS:
        return []
    return [
        finding(
            "challenge-unanswered",
            "The omission challenge is named but carries no answer.\n"
            "  Record what came back: the regulator or regime named as most likely "
            "missing,\n  and whether it became a worked branch or a stated gap. An "
            "unanswered challenge\n  is a gap in the receipt.",
        )
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    parser.add_argument("note", type=Path)
    parser.add_argument("--json", type=Path, help="write the findings for the record")
    args = parser.parse_args()

    try:
        reference = REFERENCE.read_text(encoding="utf-8")
    except OSError as error:
        sys.exit(f"Could not read the discovery method file: {error}")
    method_match = METHOD_LINE.search(reference)
    if not method_match:
        sys.exit(f"{REFERENCE} names no method version; nothing to check against.")
    method = method_match.group(1)

    try:
        text = args.note.read_text(encoding="utf-8")
    except OSError as error:
        sys.exit(f"Could not read {args.note}: {error}")

    rows = receipt_rows(text)
    if rows is None:
        findings = [
            finding(
                "receipt-missing",
                f"{args.note} carries no discovery coverage receipt.\n"
                "  A `check` note whose quotes all verify is still incomplete without "
                "it: the\n  spine proves the text you fetched and says nothing about "
                "the instrument nobody\n  named. references/discovery.md section 6 has "
                "the table.",
            )
        ]
    else:
        findings = (
            check_method(text, method)
            + check_rows(rows)
            + check_negatives(text)
            + check_omission(text)
        )

    if args.json:
        args.json.write_text(
            json.dumps(
                {"note": str(args.note), "method": method, "findings": findings},
                indent=2,
                ensure_ascii=False,
            )
            + "\n",
            encoding="utf-8",
        )

    if findings:
        sys.exit(
            f"{args.note}\n"
            f"  The discovery coverage receipt is not deliverable "
            f"({len(findings)} finding{'' if len(findings) == 1 else 's'}).\n\n"
            + "\n\n".join(f"  {item['message']}" for item in findings)
        )

    print(
        f"{args.note}\n"
        f"  receipt  {len(REQUIRED_ROWS)} dimensions, all recorded\n"
        f"  method   {method}\n"
        "  Negative findings are classified and the omission challenge is answered.\n"
        "  This checks that the receipt is whole, not that the research was right."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
