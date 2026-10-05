#!/usr/bin/env python3
"""Derive framework-readback.json from a valid framework.json.

One row per item, plain English, no schema jargon:
    {"items": [{"lens", "issue_id", "question", "hit_rule",
                "materiality", "evidence_required"}]}

materiality is a one-liner composed from the bands ("default medium; high
when ...; low when ..."). An item the compiler left at default medium with
zero bands renders as "default (medium); tune during sample review". hit_rule appends
exclusions as "does not count: X; Y" when present. Ordering is
deterministic: lenses as they appear in the framework, then item order.
The framework is validated (validate_framework logic) before rendering;
invalid input is refused.

Usage:
    python3 render_readback.py --framework framework.json \
        --out framework-readback.json

Exit codes: 0 written, 1 invalid framework, 2 I/O.
"""

import argparse
import json
import os
import sys
from typing import Any

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate_framework  # noqa: E402

UNTUNED = "default (medium); tune during sample review"


def target_designator(target):
    series = target.get("series")
    element = target.get("element", "")
    return f"{series}-{element}" if series is not None else str(element)


def materiality_line(materiality):
    """Plain-English one-liner from default plus bands."""
    default = materiality["default"]
    bands = materiality["bands"]
    if default == "medium" and not bands:
        return UNTUNED
    parts = [f"default {default}"]
    for b in bands:
        parts.append("{} when {}".format(b["band"], b["when"]))
    return "; ".join(parts)


def hit_rule_line(item):
    """Hit rule with exclusions folded in as plain English."""
    rule = item["hit_rule"]
    exclusions = item["exclusions"]
    if exclusions:
        return "{} does not count: {}".format(rule, "; ".join(exclusions))
    return rule


def build_readback(framework):
    items = []
    frame = framework.get("frame")
    for lens in framework["lenses"]:
        for item in lens["items"]:
            row = {
                "lens": lens["name"],
                "issue_id": item["issue_id"],
                "question": item["question"],
                "hit_rule": hit_rule_line(item),
                "materiality": materiality_line(item["materiality"]),
                "evidence_required": item["evidence"]["required"],
            }
            target = item.get("target_ref")
            if isinstance(frame, dict) and isinstance(target, dict):
                row["target"] = "{} no. {}".format(
                    target.get("instrument_id", ""), target_designator(target)
                )
            items.append(row)
    readback: dict[str, Any] = {"items": items}
    if isinstance(frame, dict):
        covered = {}
        for lens in framework["lenses"]:
            for item in lens["items"]:
                target = item.get("target_ref")
                if isinstance(target, dict):
                    instrument_id = target.get("instrument_id")
                    covered[instrument_id] = covered.get(instrument_id, 0) + 1
        coverage = []
        by_kind = {}
        staged_elements = 0
        for instrument in sorted(
            frame.get("instruments", []), key=lambda row: row.get("instrument_id", "")
        ):
            element_count = instrument["element_count"]
            kind = instrument["kind"]
            by_kind[kind] = by_kind.get(kind, 0) + element_count
            if instrument["staged"]:
                staged_elements += element_count
            coverage.append(
                {
                    "covered": covered.get(instrument["instrument_id"], 0),
                    "element_count": element_count,
                    "instrument_id": instrument["instrument_id"],
                    "kind": kind,
                    "label": instrument["label"],
                    "staged": instrument["staged"],
                }
            )
        readback["census_totals"] = {
            "by_kind": by_kind,
            "covered": sum(row["covered"] for row in coverage),
            "elements": sum(row["element_count"] for row in coverage),
            "staged_elements": staged_elements,
        }
        readback["instrument_coverage"] = coverage
    return readback


def main():
    ap = argparse.ArgumentParser(
        description="Render the plain-English read-back from framework.json."
    )
    ap.add_argument("--framework", required=True, help="framework.json to render.")
    ap.add_argument("--out", required=True, help="Path for framework-readback.json.")
    args = ap.parse_args()

    try:
        framework = validate_framework.load_json(args.framework, "framework")
        schema = validate_framework.load_json(
            validate_framework.DEFAULT_SCHEMA, "schema"
        )
    except ValueError as e:
        print(f"FATAL: {e}", file=sys.stderr)
        sys.exit(2)

    # Approval state is irrelevant to rendering; validity is not.
    errors, unknown = validate_framework.validate(
        framework, schema, allow_approved=True
    )
    if unknown:
        print(
            "note: schema uses keyword(s) the validator does not enforce: {}".format(
                ", ".join(sorted(unknown))
            ),
            file=sys.stderr,
        )
    if errors:
        print(
            "REFUSED: %s is not a valid framework (%d error(s)); "
            "no read-back written" % (args.framework, len(errors)),
            file=sys.stderr,
        )
        for e in errors:
            print("  " + e, file=sys.stderr)
        sys.exit(1)

    readback = build_readback(framework)
    try:
        with open(args.out, "w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(readback, indent=2, sort_keys=True) + "\n")
    except OSError as e:
        print(f"FATAL: cannot write {args.out}: {e}", file=sys.stderr)
        sys.exit(2)
    print("wrote %s: %d item(s)" % (args.out, len(readback["items"])))


if __name__ == "__main__":
    main()
