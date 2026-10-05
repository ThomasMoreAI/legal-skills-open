#!/usr/bin/env python3
"""
ropa_completeness_checker.py — Validate ROPA (Records of Processing Activities)
structure and completeness per GDPR Article 30.

Reads a ROPA YAML; emits per-activity completeness check, missing fields,
warnings for stale or incomplete entries.

Stdlib only. Markdown or JSON.

Usage:
    python3 ropa_completeness_checker.py --ropa ropa.yaml
    python3 ropa_completeness_checker.py --ropa ropa.yaml --format json
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def parse_yaml(text: str) -> dict[str, Any]:
    lines: list[tuple[int, str]] = []
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        lines.append((indent, line[indent:]))
    result, _ = _parse_block(lines, 0, 0)
    return result if isinstance(result, dict) else {}


def _parse_block(lines, idx, indent):
    if idx >= len(lines):
        return None, idx
    first_indent = lines[idx][0]
    if first_indent < indent:
        return None, idx
    first_line = lines[idx][1]
    if first_line.startswith("- "):
        return _parse_seq(lines, idx, first_indent)
    return _parse_map(lines, idx, first_indent)


def _parse_map(lines, idx, indent):
    out: dict[str, Any] = {}
    while idx < len(lines):
        cur_indent, content = lines[idx]
        if cur_indent < indent:
            break
        if cur_indent > indent:
            idx += 1
            continue
        if ":" not in content:
            idx += 1
            continue
        key, _, rest = content.partition(":")
        key = key.strip().strip('"').strip("'")
        rest = rest.strip()
        if rest:
            out[key] = _scalar(rest)
            idx += 1
        else:
            idx += 1
            if idx < len(lines) and lines[idx][0] > indent:
                value, idx = _parse_block(lines, idx, lines[idx][0])
                out[key] = value if value is not None else {}
            else:
                out[key] = {}
    return out, idx


def _parse_seq(lines, idx, indent):
    out: list[Any] = []
    while idx < len(lines):
        cur_indent, content = lines[idx]
        if cur_indent < indent:
            break
        if not content.startswith("- "):
            break
        rest = content[2:].strip()
        if not rest:
            idx += 1
            if idx < len(lines) and lines[idx][0] > indent:
                value, idx = _parse_block(lines, idx, lines[idx][0])
                out.append(value if value is not None else {})
            else:
                out.append(None)
        elif ":" in rest:
            synth = [(indent + 2, rest)]
            j = idx + 1
            while j < len(lines) and lines[j][0] > indent:
                synth.append(lines[j])
                j += 1
            value, _ = _parse_map(synth, 0, indent + 2)
            out.append(value)
            idx = j
        else:
            out.append(_scalar(rest))
            idx += 1
    return out, idx


def _scalar(s: str):
    s = s.strip()
    if s.startswith('"') and s.endswith('"'):
        return s[1:-1]
    if s.startswith("'") and s.endswith("'"):
        return s[1:-1]
    if s.lower() in ("true", "yes"):
        return True
    if s.lower() in ("false", "no"):
        return False
    if s.lower() in ("null", "~", ""):
        return None
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        pass
    return s


REQUIRED_ARTICLE_30_FIELDS = [
    "purpose",
    "data_subjects",
    "data_categories",
    "recipients",
    "international_transfers",
    "retention_period",
    "security_measures",
    "lawful_basis",
]

OPTIONAL_BUT_RECOMMENDED = [
    "dpia_reference",
    "special_category_data_flag",
    "controller_contact",
    "dpo_contact",
    "last_updated",
]


@dataclass
class ActivityCheck:
    activity_name: str
    missing_required: list[str]
    missing_recommended: list[str]
    warnings: list[str]
    completeness_score: int


def check_activity(activity: dict[str, Any]) -> ActivityCheck:
    name = activity.get("name", "<unnamed>")
    missing_req = [f for f in REQUIRED_ARTICLE_30_FIELDS if not activity.get(f)]
    missing_rec = [f for f in OPTIONAL_BUT_RECOMMENDED if not activity.get(f)]
    warnings: list[str] = []

    # Specific quality checks
    lawful_basis = str(activity.get("lawful_basis", "")).lower()
    valid_bases = ["consent", "contract", "legal_obligation", "vital_interests",
                   "public_task", "legitimate_interests"]
    if lawful_basis and lawful_basis not in valid_bases:
        warnings.append(f"Lawful basis '{lawful_basis}' is not one of the 6 GDPR-recognized bases")

    if activity.get("special_category_data_flag") and not activity.get("article_9_lawful_basis"):
        warnings.append("Special-category data flagged but Article 9 lawful basis missing")

    if activity.get("international_transfers") and not activity.get("transfer_mechanism"):
        warnings.append("International transfer indicated but no transfer mechanism documented")

    last_updated = activity.get("last_updated")
    if last_updated:
        try:
            d = datetime.fromisoformat(str(last_updated).replace("Z", "+00:00"))
            age_days = (datetime.now(timezone.utc) - d).days
            if age_days > 365:
                warnings.append(f"Activity not updated in {age_days} days (>365)")
        except ValueError:
            warnings.append(f"Invalid last_updated date format: {last_updated}")

    retention = str(activity.get("retention_period", "")).lower()
    if retention in ("as long as necessary", "ongoing", "indefinite", ""):
        warnings.append("Retention period is vague; should be specific time period or specific criteria")

    total_fields = len(REQUIRED_ARTICLE_30_FIELDS) + len(OPTIONAL_BUT_RECOMMENDED)
    earned = total_fields - len(missing_req) - len(missing_rec)
    completeness = int(100 * earned / total_fields)

    return ActivityCheck(
        activity_name=name,
        missing_required=missing_req,
        missing_recommended=missing_rec,
        warnings=warnings,
        completeness_score=completeness,
    )


def render_markdown(checks: list[ActivityCheck]) -> str:
    out = ["# ROPA Completeness Report", ""]
    out.append(f"_Activities analyzed: {len(checks)}_")
    out.append("")
    avg = sum(c.completeness_score for c in checks) // len(checks) if checks else 0
    out.append(f"**Average completeness**: {avg}/100")
    out.append("")
    fully_compliant = sum(1 for c in checks if not c.missing_required and not c.warnings)
    out.append(f"**Fully compliant activities**: {fully_compliant}/{len(checks)}")
    out.append("")
    out.append("## Per-Activity Summary")
    out.append("")
    out.append("| Activity | Score | Missing Required | Warnings |")
    out.append("|----------|-------|------------------|----------|")
    for c in checks:
        out.append(f"| {c.activity_name} | {c.completeness_score} | {len(c.missing_required)} | {len(c.warnings)} |")
    out.append("")
    out.append("## Detailed Issues")
    out.append("")
    for c in checks:
        if c.missing_required or c.warnings:
            out.append(f"### {c.activity_name} ({c.completeness_score}/100)")
            if c.missing_required:
                out.append("- **Missing required (Article 30)**:")
                for m in c.missing_required:
                    out.append(f"  - [ ] {m}")
            if c.missing_recommended:
                out.append("- **Missing recommended**:")
                for m in c.missing_recommended:
                    out.append(f"  - [ ] {m}")
            if c.warnings:
                out.append("- **Warnings**:")
                for w in c.warnings:
                    out.append(f"  - ⚠️ {w}")
            out.append("")
    return "\n".join(out)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Validate ROPA completeness per GDPR Article 30",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument("--ropa", required=True, help="ROPA YAML")
    p.add_argument("--format", choices=["markdown", "json"], default="markdown")
    p.add_argument("--output", help="Output file path")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    try:
        doc = parse_yaml(Path(args.ropa).read_text())
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    activities = doc.get("activities", []) or []
    if not activities:
        print("error: no activities found in ROPA YAML (expected 'activities:' list)", file=sys.stderr)
        return 2
    checks = [check_activity(a) for a in activities if isinstance(a, dict)]
    if args.format == "json":
        out = json.dumps({"checks": [asdict(c) for c in checks]}, indent=2, default=str)
    else:
        out = render_markdown(checks)
    if args.output:
        Path(args.output).write_text(out)
        print(f"wrote {args.output}", file=sys.stderr)
    else:
        print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
