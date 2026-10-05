#!/usr/bin/env python3
"""Materialize deterministic compact-worker assignments from an approved plan."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from finding_validation import dump_atomic, expected_plan_id


def load(path: str, kind: str) -> dict[str, Any]:
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        sys.exit(f"prepare_review_jobs: cannot read {kind}: {error}")
    if not isinstance(value, dict):
        sys.exit(f"prepare_review_jobs: {kind} must be an object")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--review-plan", required=True)
    parser.add_argument("--framework", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--room-root", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    plan = load(args.review_plan, "review plan")
    framework = load(args.framework, "framework")
    manifest = load(args.manifest, "manifest")
    if plan.get("approved") is not True:
        sys.exit("prepare_review_jobs: review plan is not lawyer-approved")
    approval = plan.get("approval")
    if not isinstance(approval, dict) or approval.get("by") != "lawyer":
        sys.exit("prepare_review_jobs: review plan lacks a lawyer approval receipt")
    if plan.get("plan_id") != expected_plan_id(plan):
        sys.exit("prepare_review_jobs: review plan ID does not match its payload")
    if approval.get("plan_id") != plan.get("plan_id"):
        sys.exit("prepare_review_jobs: approval receipt names a different plan")
    documents = {
        item.get("id"): item
        for item in manifest.get("documents", [])
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }
    lenses = {
        item.get("lens_id"): item
        for item in framework.get("lenses", [])
        if isinstance(item, dict) and isinstance(item.get("lens_id"), str)
    }
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    expected_names = set()
    for job in plan.get("jobs", []):
        if not isinstance(job, dict):
            sys.exit("prepare_review_jobs: review plan contains a non-object job")
        job_id = job.get("job_id")
        lens_id = job.get("lens_id")
        member_ids = job.get("member_ids")
        if not isinstance(job_id, str) or not isinstance(member_ids, list):
            sys.exit("prepare_review_jobs: review plan job is malformed")
        lens = lenses.get(lens_id)
        if lens is None:
            sys.exit(f"prepare_review_jobs: job {job_id} names an unknown lens")
        member_documents = []
        for ordinal, doc_id in enumerate(member_ids, 1):
            document = documents.get(doc_id)
            if document is None:
                sys.exit(f"prepare_review_jobs: job {job_id} names an unknown document")
            member_documents.append(
                {
                    "id": doc_id,
                    "ordinal": ordinal,
                    "pages": document.get("pages"),
                    "path": document.get("path"),
                    "readability": document.get("readability"),
                    "title": Path(str(document.get("path", doc_id))).name,
                }
            )
        issue_items = lens.get("items", [])
        if job.get("issue_ids") != [
            item.get("issue_id") for item in issue_items if isinstance(item, dict)
        ]:
            sys.exit(f"prepare_review_jobs: job {job_id} issue coverage drifted")
        assignment = {
            "document_listing": [
                f"Document {item['ordinal']} = {item['title']}"
                for item in member_documents
            ],
            "documents": member_documents,
            "framework_version": plan["framework_version"],
            "issue_items": issue_items,
            "job_id": job_id,
            "lens_id": lens_id,
            "member_ids": member_ids,
            "requires_current_position": job.get("requires_current_position", False),
            "review_plan_id": plan["plan_id"],
            "unit_id": job.get("unit_id"),
        }
        name = f"{job_id}.json"
        expected_names.add(name)
        dump_atomic(out / name, assignment)
    stale = sorted(
        path for path in out.glob("*.json") if path.name not in expected_names
    )
    if stale:
        sys.exit(
            "prepare_review_jobs: output contains stale assignments: "
            + ", ".join(path.name for path in stale)
        )
    print(json.dumps({"assignments": len(expected_names)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
