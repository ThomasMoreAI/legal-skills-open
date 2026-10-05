#!/usr/bin/env python3
"""Validate a review-setup receipt and write approved artifact copies."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from copy import deepcopy
from pathlib import Path


class ApprovalError(ValueError):
    pass


def load(path: str, kind: str):
    try:
        with open(path, encoding="utf-8") as handle:
            value = json.load(handle)
    except (OSError, json.JSONDecodeError) as error:
        raise ApprovalError(f"cannot read {kind}: {error}") from error
    if not isinstance(value, dict):
        raise ApprovalError(f"{kind} must be a JSON object")
    return value


def digest(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def string_list(value: object, label: str) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise ApprovalError(f"{label} must be a string array")
    if value != sorted(set(value)):
        raise ApprovalError(f"{label} must be sorted and unique")
    return value


def require_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise ApprovalError(f"{label} drift")


def validate_approval(
    approval, manifest, framework, clusters, read_plan, review_plan
) -> None:
    required = {
        "approval_source",
        "approved_by",
        "artifact",
        "authorization",
        "clusters_digest",
        "corpus_id",
        "decisions",
        "framework_digest",
        "issue_ids",
        "manifest_digest",
        "read_plan_digest",
        "read_plan_id",
        "review_plan_digest",
        "review_plan_id",
        "unit_ids",
        "version",
    }
    missing = sorted(required - set(approval))
    extra = sorted(set(approval) - required)
    if missing:
        raise ApprovalError("approval is missing: " + ", ".join(missing))
    if extra:
        raise ApprovalError("approval has unsupported fields: " + ", ".join(extra))
    if approval["artifact"] != "review-setup-approval" or approval["version"] != 1:
        raise ApprovalError("unsupported approval artifact or version")
    if approval["approval_source"] not in {"offline-export", "conversation"}:
        raise ApprovalError("unsupported approval source")
    if approval["approved_by"] != "lawyer":
        raise ApprovalError("approval must be made by the lawyer")
    if approval["authorization"] != "sample-only":
        raise ApprovalError("approval must authorize only the sample")
    decisions = approval["decisions"]
    expected_decisions = {
        "collection_coverage_confirmed": True,
        "metadata_policy_confirmed": True,
        "review_questions_confirmed": True,
        "sample_confirmed": True,
    }
    if decisions != expected_decisions:
        raise ApprovalError("all four setup decisions must be explicitly confirmed")

    require_equal(approval["corpus_id"], manifest.get("corpus_id"), "corpus")
    require_equal(approval["manifest_digest"], digest(manifest), "manifest")
    require_equal(approval["framework_digest"], digest(framework), "framework")
    require_equal(approval["clusters_digest"], digest(clusters), "clusters")
    require_equal(approval["read_plan_digest"], digest(read_plan), "read plan")
    require_equal(approval["review_plan_digest"], digest(review_plan), "review plan")
    require_equal(approval["read_plan_id"], read_plan.get("plan_id"), "read-plan ID")
    require_equal(
        approval["review_plan_id"], review_plan.get("plan_id"), "review-plan ID"
    )
    require_equal(
        review_plan.get("framework_digest"), digest(framework), "plan framework"
    )
    if review_plan.get("tier") != "sample":
        raise ApprovalError("only a sample plan can use this approval")
    if (
        review_plan.get("approved") is not False
        or review_plan.get("approval") is not None
    ):
        raise ApprovalError("review plan is not an unapproved source plan")

    jobs = review_plan.get("jobs")
    if not isinstance(jobs, list) or not jobs:
        raise ApprovalError("review plan has no sample jobs")
    expected_units = sorted(
        {job.get("unit_id") for job in jobs if isinstance(job.get("unit_id"), str)}
    )
    expected_issues = sorted(
        {
            issue_id
            for job in jobs
            for issue_id in job.get("issue_ids", [])
            if isinstance(issue_id, str)
        }
    )
    require_equal(
        string_list(approval["unit_ids"], "unit_ids"), expected_units, "unit scope"
    )
    require_equal(
        string_list(approval["issue_ids"], "issue_ids"),
        expected_issues,
        "review-question scope",
    )


def dump(path: str, value: object) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--approval", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--framework", required=True)
    parser.add_argument("--clusters", required=True)
    parser.add_argument("--read-plan", required=True)
    parser.add_argument("--review-plan", required=True)
    parser.add_argument("--approved-plan-out", required=True)
    parser.add_argument("--confirmed-clusters-out", required=True)
    args = parser.parse_args()

    try:
        approval = load(args.approval, "approval")
        manifest = load(args.manifest, "manifest")
        framework = load(args.framework, "framework")
        clusters = load(args.clusters, "clusters")
        read_plan = load(args.read_plan, "read plan")
        review_plan = load(args.review_plan, "review plan")
        output_paths = {
            str(Path(args.approved_plan_out).resolve()),
            str(Path(args.confirmed_clusters_out).resolve()),
        }
        input_paths = {
            str(Path(value).resolve())
            for value in (
                args.approval,
                args.manifest,
                args.framework,
                args.clusters,
                args.read_plan,
                args.review_plan,
            )
        }
        if len(output_paths) != 2 or output_paths & input_paths:
            raise ApprovalError("outputs must be distinct new artifact paths")
        validate_approval(
            approval, manifest, framework, clusters, read_plan, review_plan
        )
    except ApprovalError as error:
        print(f"ingest_review_setup_approval: {error}", file=sys.stderr)
        sys.exit(1)

    approved_plan = deepcopy(review_plan)
    approved_plan["approved"] = True
    approved_plan["approval"] = {
        "by": "lawyer",
        "plan_id": review_plan["plan_id"],
    }
    confirmed_clusters = deepcopy(clusters)
    confirmed_clusters["confirmed"] = True
    dump(args.approved_plan_out, approved_plan)
    dump(args.confirmed_clusters_out, confirmed_clusters)
    print(
        f"approved sample plan {review_plan['plan_id']} and confirmed relationship map"
    )


if __name__ == "__main__":
    main()
