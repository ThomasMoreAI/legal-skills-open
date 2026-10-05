#!/usr/bin/env python3
"""
gdpr_readiness_score.py — Score GDPR audit readiness per area (0-100).

Reads a controls YAML; emits per-area score + overall + sprint recommendation.

Stdlib only. Markdown or JSON.

Usage:
    python3 gdpr_readiness_score.py --config gdpr-controls.yaml
    python3 gdpr_readiness_score.py --config gdpr-controls.yaml --format json
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, asdict
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


# Areas + per-area checklist + weight
GDPR_CHECKLIST = {
    "ROPA": {
        "ropa_exists": 25,
        "ropa_current_within_12mo": 25,
        "all_processing_activities_documented": 20,
        "lawful_basis_per_activity": 15,
        "special_category_data_flagged": 15,
    },
    "Privacy_Notices": {
        "notice_published": 20,
        "all_required_information_included": 30,
        "easily_accessible_no_dark_patterns": 20,
        "translations_for_member_states": 15,
        "current_within_12mo": 15,
    },
    "Data_Subject_Rights": {
        "process_documented": 25,
        "one_month_response_tracking": 25,
        "identity_verification_method": 20,
        "request_records_maintained": 30,
    },
    "DPIA": {
        "high_risk_processing_identified": 25,
        "dpia_conducted_per_high_risk": 30,
        "dpo_consulted_per_dpia": 20,
        "mitigations_implemented": 25,
    },
    "DPA_Vendor_Agreements": {
        "dpa_with_all_processors": 35,
        "article_28_required_clauses": 25,
        "sub_processor_list_current": 20,
        "annual_dpa_review": 20,
    },
    "Security_Article_32": {
        "encryption_at_rest_in_transit": 20,
        "access_controls": 20,
        "backup_with_restore_testing": 20,
        "regular_security_testing": 20,
        "annual_review_of_measures": 20,
    },
    "Breach_Notification": {
        "breach_response_process": 30,
        "72_hour_notification_capability": 30,
        "breach_register": 20,
        "subject_notification_capability": 20,
    },
    "International_Transfers": {
        "mechanism_per_transfer": 30,
        "scc_2021_version": 25,
        "tia_for_us_transfers": 25,
        "supplementary_measures_documented": 20,
    },
    "Consent": {
        "freely_given_no_bundling": 25,
        "specific_per_purpose": 25,
        "unambiguous_affirmative_action": 25,
        "withdrawable_easily": 25,
    },
    "DPO": {
        "dpo_appointed_if_required": 50,
        "dpo_contact_published": 25,
        "dpo_consulted_on_high_risk": 25,
    },
}


@dataclass
class AreaScore:
    area: str
    score: int
    missing_items: list[str]


@dataclass
class Report:
    overall_score: int
    area_scores: list[AreaScore]
    recommended_sprint_weeks: int
    sprint_reasoning: str


def score_area(area: str, controls: dict[str, Any]) -> AreaScore:
    checklist = GDPR_CHECKLIST.get(area, {})
    earned = 0
    missing = []
    for item, weight in checklist.items():
        if controls.get(item, False):
            earned += weight
        else:
            missing.append(item)
    return AreaScore(area=area, score=earned, missing_items=missing)


def recommend_sprint(overall: int) -> tuple[int, str]:
    if overall >= 90:
        return 4, "Strong readiness; 4-week sprint for periodic audit"
    if overall >= 75:
        return 8, "Moderate gaps; 8-week sprint"
    if overall >= 60:
        return 12, "Significant gaps; 12-week sprint or defer audit"
    return 0, "Substantial gaps; defer audit; multi-quarter remediation needed"


def report(doc: dict[str, Any]) -> Report:
    areas_data = doc.get("areas", {}) or {}
    scores: list[AreaScore] = []
    for area in GDPR_CHECKLIST:
        controls = areas_data.get(area, {}) or {}
        scores.append(score_area(area, controls))
    overall = sum(s.score for s in scores) // len(scores) if scores else 0
    weeks, reasoning = recommend_sprint(overall)
    return Report(overall_score=overall, area_scores=scores, recommended_sprint_weeks=weeks, sprint_reasoning=reasoning)


def render_markdown(r: Report) -> str:
    out = ["# GDPR Readiness Score", ""]
    out.append(f"## Overall: {r.overall_score}/100")
    out.append("")
    out.append(f"**Recommendation**: {r.sprint_reasoning}")
    out.append("")
    out.append("## Per-Area Scores")
    out.append("")
    out.append("| Area | Score | Missing |")
    out.append("|------|-------|---------|")
    for s in r.area_scores:
        out.append(f"| {s.area} | {s.score}/100 | {len(s.missing_items)} items |")
    out.append("")
    out.append("## Gaps")
    out.append("")
    for s in r.area_scores:
        if s.missing_items:
            out.append(f"### {s.area}")
            for m in s.missing_items:
                out.append(f"- [ ] {m}")
            out.append("")
    return "\n".join(out)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Score GDPR audit readiness",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument("--config", required=True, help="GDPR controls YAML")
    p.add_argument("--format", choices=["markdown", "json"], default="markdown")
    p.add_argument("--output", help="Output file path")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    try:
        doc = parse_yaml(Path(args.config).read_text())
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    r = report(doc)
    if args.format == "json":
        out = json.dumps(asdict(r), indent=2, default=str)
    else:
        out = render_markdown(r)
    if args.output:
        Path(args.output).write_text(out)
        print(f"wrote {args.output}", file=sys.stderr)
    else:
        print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
