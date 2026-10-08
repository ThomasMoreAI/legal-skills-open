#!/usr/bin/env python3
"""Validate arbitration-drafter schema and case expectations."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


SKILL_ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_SCHEMA = SKILL_ROOT / "references" / "arbitration-draft-schema.json"
DEFAULT_CASES = SKILL_ROOT / "tests" / "arbitration_cases.json"
DEFAULT_LEGAL_MAP = (
    PLUGIN_ROOT / "skills" / "layoff-defense" / "references" / "legal-map.md"
)


def collect_legal_anchors(legal_map_path: Path) -> set[str]:
    text = legal_map_path.read_text(encoding="utf-8")
    anchors: set[str] = set()
    current_source: str | None = None

    for line in text.splitlines():
        source_heading = re.match(r"### `([^`]+)`", line)
        if source_heading:
            current_source = source_heading.group(1)
            continue

        article = re.match(r"- `(art[0-9]+)`:", line)
        if article and current_source:
            anchors.add(f"{current_source}#{article.group(1)}")

    return anchors


def all_schema_anchors(schema: dict[str, Any]) -> set[str]:
    anchors = set(schema.get("core_source_anchors", []))
    for section in schema["draft_sections"].values():
        anchors.update(section.get("source_anchors", []))
    for claim in schema["claim_templates"].values():
        anchors.update(claim.get("source_anchors", []))
    return anchors


def anchors_for_claims(schema: dict[str, Any], claim_types: set[str]) -> set[str]:
    anchors = set(schema.get("core_source_anchors", []))
    for section in schema["draft_sections"].values():
        anchors.update(section.get("source_anchors", []))
    for claim_type in claim_types:
        claim = schema["claim_templates"].get(claim_type)
        if claim:
            anchors.update(claim.get("source_anchors", []))
    return anchors


def evidence_for_claims(schema: dict[str, Any], claim_types: set[str]) -> set[str]:
    evidence: set[str] = set()
    for claim_type in claim_types:
        claim = schema["claim_templates"].get(claim_type)
        if claim:
            evidence.update(claim.get("evidence_needed", []))
    return evidence


def disqualifying_risks_for_claims(schema: dict[str, Any], claim_types: set[str]) -> set[str]:
    risks: set[str] = set()
    for claim_type in claim_types:
        claim = schema["claim_templates"].get(claim_type)
        if claim:
            risks.update(claim.get("disqualifying_risks", []))
    return risks


def validate(schema_path: Path, cases_path: Path, legal_map_path: Path) -> dict[str, Any]:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    cases = json.loads(cases_path.read_text(encoding="utf-8"))
    legal_anchors = collect_legal_anchors(legal_map_path)

    schema_anchor_failures = sorted(all_schema_anchors(schema) - legal_anchors)
    missing_amount_rule_text = [
        claim_type
        for claim_type, template in schema["claim_templates"].items()
        if not template.get("amount_rule_text")
    ]
    human_fields = [
        schema["source_note"],
        *(template["label"] for template in schema["claim_templates"].values()),
        *(template.get("amount_rule_text", "") for template in schema["claim_templates"].values()),
        *(template["draft_note"] for template in schema["claim_templates"].values()),
        *schema["draft_application_outline"],
        *schema["global_safety_rules"],
    ]
    english_guidance = re.compile(r"\b(?:Use|Verify|State|Only|List|Local|Check|Do|If)\b")
    non_chinese_human_fields = [
        value
        for value in human_fields
        if value
        and (not re.search(r"[\u3400-\u9fff]", value) or english_guidance.search(value))
    ]
    failures: list[dict[str, Any]] = []
    results: list[dict[str, Any]] = []

    available_sections = set(schema["draft_sections"])
    available_claims = set(schema["claim_templates"])

    for case in cases:
        case_failures: list[dict[str, Any]] = []
        claim_types = set(case["claim_types"])
        missing_claims = sorted(claim_types - available_claims)
        if missing_claims:
            case_failures.append({"missing_claim_types": missing_claims})

        missing_sections = sorted(set(case["expected_sections"]) - available_sections)
        if missing_sections:
            case_failures.append({"missing_sections": missing_sections})

        available_anchors = anchors_for_claims(schema, claim_types)
        missing_anchors = sorted(set(case["expected_source_anchors"]) - available_anchors)
        if missing_anchors:
            case_failures.append({"missing_source_anchors": missing_anchors})

        available_evidence = evidence_for_claims(schema, claim_types)
        missing_evidence = sorted(
            set(case["expected_evidence_needed"]) - available_evidence
        )
        if missing_evidence:
            case_failures.append({"missing_evidence_needed": missing_evidence})

        expected_disqualifying_risks = set(case.get("expected_disqualifying_risks", []))
        available_disqualifying_risks = disqualifying_risks_for_claims(schema, claim_types)
        missing_disqualifying_risks = sorted(
            expected_disqualifying_risks - available_disqualifying_risks
        )
        if missing_disqualifying_risks:
            case_failures.append(
                {"missing_disqualifying_risks": missing_disqualifying_risks}
            )

        status = "pass" if not case_failures else "fail"
        if case_failures:
            failures.append({"case": case["id"], "failures": case_failures})

        results.append(
            {
                "id": case["id"],
                "status": status,
                "claim_types": sorted(claim_types),
                "expected_sections": case["expected_sections"],
                "expected_source_anchors": case["expected_source_anchors"],
                "expected_evidence_needed": case["expected_evidence_needed"],
                "expected_disqualifying_risks": case.get("expected_disqualifying_risks", []),
            }
        )

    if schema_anchor_failures:
        failures.append({"schema_anchor_failures": schema_anchor_failures})
    if missing_amount_rule_text:
        failures.append({"missing_amount_rule_text": missing_amount_rule_text})
    if non_chinese_human_fields:
        failures.append({"non_chinese_human_fields": non_chinese_human_fields})

    return {
        "schema_path": str(schema_path),
        "cases_path": str(cases_path),
        "legal_map_path": str(legal_map_path),
        "total": len(cases),
        "passed": len(cases) - sum(1 for item in failures if "case" in item),
        "failed": len(failures),
        "schema_anchor_failures": schema_anchor_failures,
        "human_field_count": len(human_fields),
        "missing_amount_rule_text": missing_amount_rule_text,
        "non_chinese_human_fields": non_chinese_human_fields,
        "results": results,
        "failures": failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    parser.add_argument("--legal-map", type=Path, default=DEFAULT_LEGAL_MAP)
    args = parser.parse_args()

    result = validate(
        args.schema.resolve(),
        args.cases.resolve(),
        args.legal_map.resolve(),
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
