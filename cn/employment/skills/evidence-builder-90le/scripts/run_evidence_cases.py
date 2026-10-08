#!/usr/bin/env python3
"""Validate evidence-builder matrix and evidence case expectations."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


SKILL_ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_MATRIX = SKILL_ROOT / "references" / "evidence-matrix.json"
DEFAULT_CASES = SKILL_ROOT / "tests" / "evidence_cases.json"
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


def item_ids(items: list[dict[str, Any]]) -> set[str]:
    return {item["id"] for item in items}


def map_item_ids(matrix: dict[str, Any], termination_map: str) -> set[str]:
    result: set[str] = set()
    map_data = matrix["termination_maps"][termination_map]

    for bundle_name in map_data.get("include_common_bundles", []):
        result.update(item_ids(matrix["common_bundles"][bundle_name]["items"]))
    result.update(item_ids(map_data.get("items", [])))
    return result


def map_source_anchors(matrix: dict[str, Any], termination_map: str) -> set[str]:
    result = set(matrix["termination_maps"][termination_map]["source_anchors"])
    for bundle_name in matrix["termination_maps"][termination_map].get(
        "include_common_bundles", []
    ):
        result.update(matrix["common_bundles"][bundle_name]["source_anchors"])
    return result


def all_matrix_anchors(matrix: dict[str, Any]) -> set[str]:
    anchors: set[str] = set()
    for bundle in matrix["common_bundles"].values():
        anchors.update(bundle.get("source_anchors", []))
    for map_data in matrix["termination_maps"].values():
        anchors.update(map_data.get("source_anchors", []))
    return anchors


def validate(matrix_path: Path, cases_path: Path, legal_map_path: Path) -> dict[str, Any]:
    matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
    cases = json.loads(cases_path.read_text(encoding="utf-8"))
    legal_anchors = collect_legal_anchors(legal_map_path)

    matrix_anchor_failures = sorted(all_matrix_anchors(matrix) - legal_anchors)
    matrix_items = [
        *(item for bundle in matrix["common_bundles"].values() for item in bundle["items"]),
        *(item for map_data in matrix["termination_maps"].values() for item in map_data["items"]),
    ]
    missing_item_labels = [item["id"] for item in matrix_items if not item.get("label")]
    human_fields = [
        *matrix["priority_levels"].values(),
        *matrix["global_safety_rules"],
        *(item.get(field, "") for item in matrix_items for field in ("label", "proves", "lawful_source", "collection_note")),
    ]
    non_chinese_human_fields = [
        value for value in human_fields if value and not re.search(r"[\u3400-\u9fff]", value)
    ]
    failures: list[dict[str, Any]] = []
    results: list[dict[str, Any]] = []

    for case in cases:
        case_failures: list[dict[str, Any]] = []
        maps = set(case["termination_maps"])
        missing_maps = sorted(maps - set(matrix["termination_maps"]))
        if missing_maps:
            case_failures.append({"missing_maps": missing_maps})

        available_items: set[str] = set()
        available_anchors: set[str] = set()
        for termination_map in maps:
            if termination_map not in matrix["termination_maps"]:
                continue
            available_items.update(map_item_ids(matrix, termination_map))
            available_anchors.update(map_source_anchors(matrix, termination_map))

        missing_items = sorted(set(case["expected_item_ids"]) - available_items)
        if missing_items:
            case_failures.append({"missing_item_ids": missing_items})

        missing_anchors = sorted(set(case["expected_source_anchors"]) - available_anchors)
        if missing_anchors:
            case_failures.append({"missing_source_anchors": missing_anchors})

        status = "pass" if not case_failures else "fail"
        if case_failures:
            failures.append({"case": case["id"], "failures": case_failures})

        results.append(
            {
                "id": case["id"],
                "status": status,
                "termination_maps": sorted(maps),
                "expected_item_ids": case["expected_item_ids"],
                "expected_source_anchors": case["expected_source_anchors"],
            }
        )

    if matrix_anchor_failures:
        failures.append({"matrix_anchor_failures": matrix_anchor_failures})
    if missing_item_labels:
        failures.append({"missing_item_labels": missing_item_labels})
    if non_chinese_human_fields:
        failures.append({"non_chinese_human_fields": non_chinese_human_fields})

    return {
        "matrix_path": str(matrix_path),
        "cases_path": str(cases_path),
        "legal_map_path": str(legal_map_path),
        "total": len(cases),
        "passed": len(cases) - sum(1 for item in failures if "case" in item),
        "failed": len(failures),
        "matrix_anchor_failures": matrix_anchor_failures,
        "item_count": len(matrix_items),
        "human_field_count": len(human_fields),
        "missing_item_labels": missing_item_labels,
        "non_chinese_human_fields": non_chinese_human_fields,
        "results": results,
        "failures": failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--matrix", type=Path, default=DEFAULT_MATRIX)
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    parser.add_argument("--legal-map", type=Path, default=DEFAULT_LEGAL_MAP)
    args = parser.parse_args()

    result = validate(
        args.matrix.resolve(),
        args.cases.resolve(),
        args.legal_map.resolve(),
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
