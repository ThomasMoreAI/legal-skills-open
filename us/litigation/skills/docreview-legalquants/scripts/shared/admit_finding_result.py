#!/usr/bin/env python3
"""Admit one compact worker response into a canonical maker checkpoint."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from finding_validation import RESULT_KEYS, dump_atomic, source_cache, validate_result

CONTRACT = "finding-worker/2"
ABSENT_CHARACTERIZATION = "No responsive evidence found in the reviewed unit."
CORE_KEYS = {"n", "issue_id", "status"}
PRESENT_KEYS = CORE_KEYS | {
    "characterization",
    "current_position",
    "doc",
    "page",
    "quote",
    "receipt_mode",
    "section",
}
MATERIALITY_KEYS = {"band", "band_basis"}
UNRESOLVED_KEYS = CORE_KEYS | {"reason"}
TOP_LEVEL_KEYS = {
    "contract",
    "determinations",
    "job_id",
    "privilege_candidates",
    "review_plan_id",
}
PRIVILEGE_KEYS = {
    "doc",
    "page",
    "quote",
    "reason",
    "receipt_mode",
    "signals",
}


class Rejected(ValueError):
    """A worker response failed deterministic admission."""

    def __init__(self, *codes: str):
        super().__init__(", ".join(codes))
        self.codes = sorted(set(codes))


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise OSError(f"cannot read {path}: {error}") from error


def doc_id_for(ordinal: object, member_ids: list[str]) -> str:
    if not isinstance(ordinal, int) or isinstance(ordinal, bool):
        raise Rejected("doc-ordinal-out-of-range")
    if ordinal < 1 or ordinal > len(member_ids):
        raise Rejected("doc-ordinal-out-of-range")
    return member_ids[ordinal - 1]


def finding_from_v2(
    determination: object,
    index: int,
    issue_items: list[dict[str, object]],
    member_ids: list[str],
) -> dict[str, object]:
    if not isinstance(determination, dict):
        raise Rejected("status-invalid")
    if determination.get("n") != index + 1:
        raise Rejected("issue-order-mismatch")
    issue_id = issue_items[index].get("issue_id")
    if determination.get("issue_id") != issue_id:
        raise Rejected("issue-echo-mismatch")
    status = determination.get("status")
    if status not in {"absent", "present", "unresolved"}:
        raise Rejected("status-invalid")
    if status == "absent":
        if set(determination) != CORE_KEYS:
            raise Rejected("absent-extra-fields")
        doc_id = min(member_ids)
        return {
            "band": None,
            "band_basis": None,
            "characterization": ABSENT_CHARACTERIZATION,
            "current_position": False,
            "doc_id": doc_id,
            "finding_id": f"{issue_id}/{doc_id}",
            "issue_id": issue_id,
            "page": None,
            "quote": None,
            "receipt_mode": None,
            "section": None,
            "status": status,
        }
    if status == "unresolved":
        if set(determination) != UNRESOLVED_KEYS:
            raise Rejected("unresolved-missing-reason")
        reason = determination.get("reason")
        if not isinstance(reason, str) or not reason.strip():
            raise Rejected("unresolved-missing-reason")
        doc_id = min(member_ids)
        return {
            "band": None,
            "band_basis": None,
            "characterization": reason,
            "current_position": False,
            "doc_id": doc_id,
            "finding_id": f"{issue_id}/{doc_id}",
            "issue_id": issue_id,
            "page": None,
            "quote": None,
            "receipt_mode": None,
            "section": None,
            "status": status,
        }
    materiality = issue_items[index].get("materiality")
    expected_keys = PRESENT_KEYS | (MATERIALITY_KEYS if materiality else set())
    if set(determination) != expected_keys:
        raise Rejected("present-missing-receipt")
    doc_id = doc_id_for(determination.get("doc"), member_ids)
    characterization = determination.get("characterization")
    if not isinstance(characterization, str) or not characterization.strip():
        raise Rejected("characterization-empty")
    answer_shape = issue_items[index].get("answer_shape")
    cap = (
        answer_shape.get("characterization_max_words")
        if isinstance(answer_shape, dict)
        else None
    )
    if isinstance(cap, int) and len(characterization.split()) > cap:
        raise Rejected("characterization-over-cap")
    return {
        "band": determination.get("band") if materiality else None,
        "band_basis": determination.get("band_basis") if materiality else None,
        "characterization": characterization,
        "current_position": determination.get("current_position"),
        "doc_id": doc_id,
        "finding_id": f"{issue_id}/{doc_id}",
        "issue_id": issue_id,
        "page": determination.get("page"),
        "quote": determination.get("quote"),
        "receipt_mode": determination.get("receipt_mode"),
        "section": determination.get("section"),
        "status": status,
    }


def expand_v2(raw: object, assignment: dict[str, Any]) -> dict[str, object]:
    if not isinstance(raw, dict) or set(raw) != TOP_LEVEL_KEYS:
        raise Rejected("raw-unparseable")
    if raw.get("contract") != CONTRACT:
        raise Rejected("raw-unparseable")
    if raw.get("review_plan_id") != assignment.get("review_plan_id") or raw.get(
        "job_id"
    ) != assignment.get("job_id"):
        raise Rejected("plan-binding-mismatch")
    issue_items = assignment.get("issue_items")
    member_ids = assignment.get("member_ids")
    determinations = raw.get("determinations")
    if not isinstance(issue_items, list) or not all(
        isinstance(item, dict) for item in issue_items
    ):
        raise OSError("assignment has invalid issue_items")
    if (
        not isinstance(member_ids, list)
        or not member_ids
        or not all(isinstance(item, str) for item in member_ids)
    ):
        raise OSError("assignment has invalid member_ids")
    if not isinstance(determinations, list) or len(determinations) != len(issue_items):
        raise Rejected("coverage-incomplete")
    ordinals = [item.get("n") for item in determinations if isinstance(item, dict)]
    if len(ordinals) != len(set(ordinals)):
        raise Rejected("duplicate-determination")
    findings = [
        finding_from_v2(item, index, issue_items, member_ids)
        for index, item in enumerate(determinations)
    ]
    raw_candidates = raw.get("privilege_candidates")
    if not isinstance(raw_candidates, list):
        raise Rejected("raw-unparseable")
    candidates = []
    for candidate in raw_candidates:
        if not isinstance(candidate, dict) or set(candidate) != PRIVILEGE_KEYS:
            raise Rejected("raw-unparseable")
        candidates.append(
            {
                **{key: value for key, value in candidate.items() if key != "doc"},
                "doc_id": doc_id_for(candidate.get("doc"), member_ids),
            }
        )
    return {
        "findings": findings,
        "framework_version": assignment["framework_version"],
        "lens_id": assignment["lens_id"],
        "privilege_candidates": candidates,
        "review_plan_id": assignment["review_plan_id"],
        "unit_id": assignment["unit_id"],
    }


def classify_validation_errors(errors: list[str]) -> list[str]:
    codes = []
    for error in errors:
        if "quote is absent" in error:
            codes.append("quote-not-in-source")
        elif "page exceeds" in error:
            codes.append("page-out-of-range")
        elif "receipt" in error or "quoted evidence" in error:
            codes.append("receipt-mode-invalid")
        elif "characterization" in error:
            codes.append("characterization-empty")
        elif "stable finding_id" in error:
            codes.append("plan-binding-mismatch")
        else:
            codes.append("status-invalid")
    return sorted(set(codes))


def admit(
    assignment: dict[str, Any], raw: object, room_root: Path
) -> tuple[dict[str, object], str]:
    if isinstance(raw, dict) and raw.get("contract") == CONTRACT:
        result = expand_v2(raw, assignment)
        contract = CONTRACT
    elif isinstance(raw, dict) and set(raw) == RESULT_KEYS:
        result = raw
        contract = "finding-worker/1"
    else:
        raise Rejected("raw-unparseable")
    documents = assignment.get("documents")
    if not isinstance(documents, list) or not all(
        isinstance(document, dict) for document in documents
    ):
        raise OSError("assignment has invalid documents")
    docs, text_for = source_cache({"documents": documents}, str(room_root), "stdlib")
    issue_items = assignment.get("issue_items", [])
    if not isinstance(issue_items, list) or not all(
        isinstance(item, dict) for item in issue_items
    ):
        raise OSError("assignment has invalid issue_items")
    job = {
        "contains_image": any(
            document.get("readability") == "scanned" for document in documents
        ),
        "contains_unreadable": False,
        "framework_version": assignment.get("framework_version"),
        "issue_ids": [item.get("issue_id") for item in issue_items],
        "lens_id": assignment.get("lens_id"),
        "member_ids": assignment.get("member_ids"),
        "requires_current_position": assignment.get("requires_current_position", False),
        "review_plan_id": assignment.get("review_plan_id"),
        "unit_id": assignment.get("unit_id"),
    }
    lens_items = {item["issue_id"]: item for item in issue_items}
    _, _, errors = validate_result(result, job, lens_items, docs, text_for)
    if errors:
        raise Rejected(*classify_validation_errors(errors))
    return result, contract


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--assignment", required=True)
    parser.add_argument("--raw", required=True)
    parser.add_argument("--room-root", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--receipt", required=True)
    args = parser.parse_args()
    try:
        assignment_value = load_json(Path(args.assignment))
        raw_path = Path(args.raw)
        raw_value = load_json(raw_path)
        if not isinstance(assignment_value, dict):
            raise OSError("assignment must be an object")
        result, contract = admit(assignment_value, raw_value, Path(args.room_root))
        receipt = {
            "admitted_by": "admit_finding_result.py",
            "contract": contract,
            "doc_ordinal_map": {
                str(index): doc_id
                for index, doc_id in enumerate(
                    assignment_value.get("member_ids", []), 1
                )
            },
            "expansion_rules_version": 2 if contract == CONTRACT else 1,
            "issue_order": [
                item["issue_id"] for item in assignment_value.get("issue_items", [])
            ],
            "raw_attempt_path": raw_path.as_posix(),
            "raw_sha256": hashlib.sha256(raw_path.read_bytes()).hexdigest(),
        }
        dump_atomic(args.out, result)
        dump_atomic(args.receipt, receipt)
    except Rejected as error:
        print(json.dumps({"admitted": False, "codes": error.codes}, sort_keys=True))
        return 1
    except OSError as error:
        print(f"admit_finding_result: {error}", file=sys.stderr)
        return 2
    print(json.dumps({"admitted": True}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
