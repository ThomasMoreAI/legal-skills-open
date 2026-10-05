#!/usr/bin/env python3
"""Validate isolated pair decisions and compile model-edges.json."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

RELATIONS = {
    "amends",
    "sow-under",
    "schedule-of",
    "guarantees",
    "supersedes",
    "duplicate-of",
}
RESULT_KEYS = {"a", "b", "decision", "dst", "job_id", "quote", "relation", "src"}


def load(path, kind):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        sys.exit(f"merge_edge_results: cannot read {kind}: {error}")


def metadata_dir(path):
    records = {}
    try:
        for item in sorted(Path(path).glob("*.json")):
            record = json.loads(item.read_text(encoding="utf-8"))
            if isinstance(record, dict) and isinstance(record.get("id"), str):
                records[record["id"]] = record
    except (OSError, json.JSONDecodeError) as error:
        sys.exit(f"merge_edge_results: cannot read metadata: {error}")
    return records


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def receipt_quotes(node):
    quotes = []
    if isinstance(node, dict):
        if isinstance(node.get("quote"), str):
            quotes.append(node["quote"])
        for value in node.values():
            quotes.extend(receipt_quotes(value))
    elif isinstance(node, list):
        for value in node:
            quotes.extend(receipt_quotes(value))
    return quotes


def validate_plan(plan, records):
    if not isinstance(plan, dict) or plan.get("version") != 1:
        sys.exit("merge_edge_results: unsupported edge plan")
    jobs = plan.get("jobs")
    if not isinstance(jobs, list):
        sys.exit("merge_edge_results: edge plan has no jobs array")
    expected_plan = hashlib.sha256(canonical(jobs).encode()).hexdigest()[:16]
    if plan.get("plan_id") != expected_plan:
        sys.exit("merge_edge_results: edge plan ID is invalid")
    seen = set()
    for job in jobs:
        if not isinstance(job, dict) or set(job) != {
            "a",
            "b",
            "job_id",
            "metadata_digest",
        }:
            sys.exit("merge_edge_results: edge plan job has invalid shape")
        a, b = job.get("a"), job.get("b")
        if not isinstance(a, str) or not isinstance(b, str) or a >= b:
            sys.exit("merge_edge_results: edge plan pair is not canonical")
        expected_job = hashlib.sha256(f"{a}\0{b}".encode()).hexdigest()[:16]
        if job.get("job_id") != expected_job or expected_job in seen:
            sys.exit("merge_edge_results: edge plan job ID is invalid or repeated")
        seen.add(expected_job)
        if a not in records or b not in records:
            sys.exit(f"merge_edge_results: metadata is missing for {a}/{b}")
        digest = hashlib.sha256(
            canonical([records[a], records[b]]).encode()
        ).hexdigest()
        if job.get("metadata_digest") != digest:
            sys.exit(f"merge_edge_results: metadata drifted for {a}/{b}")
    return jobs


def validate_result(result, job, records):
    errors = []
    if not isinstance(result, dict) or set(result) != RESULT_KEYS:
        return ["unexpected or missing result keys"]
    for field in ("a", "b", "job_id"):
        if result.get(field) != job[field]:
            errors.append(f"{field} does not match the plan")
    decision = result.get("decision")
    if decision not in {"linked", "not-linked", "unresolved"}:
        errors.append("decision is invalid")
        return errors
    if decision != "linked":
        if any(
            result.get(field) is not None
            for field in ("src", "dst", "relation", "quote")
        ):
            errors.append("non-linked decision must leave edge fields null")
        return errors
    src, dst = result.get("src"), result.get("dst")
    if {src, dst} != {job["a"], job["b"]} or src == dst:
        errors.append("linked edge endpoints do not match the pair")
    if result.get("relation") not in RELATIONS:
        errors.append("linked edge relation is invalid")
    quote = result.get("quote")
    if not isinstance(quote, str) or not quote.strip():
        errors.append("linked edge has no quote")
    elif src in records and quote not in receipt_quotes(records[src]):
        errors.append("linked edge quote is not a receipt in source metadata")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--edge-plan", required=True)
    parser.add_argument("--metadata", required=True)
    parser.add_argument("--results", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    plan = load(args.edge_plan, "edge plan")
    records = metadata_dir(args.metadata)
    jobs = validate_plan(plan, records)
    edges = []
    report = []
    for job in jobs:
        path = Path(args.results) / f"{job['job_id']}.json"
        if not path.is_file():
            report.append(
                {
                    "errors": ["edge checkpoint missing"],
                    "job_id": job["job_id"],
                    "status": "parked",
                }
            )
            continue
        result = load(path, f"edge result {job['job_id']}")
        errors = validate_result(result, job, records)
        if not errors and result["decision"] == "linked":
            edges.append(
                {
                    "dst": result["dst"],
                    "quote": result["quote"],
                    "relation": result["relation"],
                    "src": result["src"],
                }
            )
        report.append(
            {
                "decision": result.get("decision") if not errors else None,
                "errors": errors,
                "job_id": job["job_id"],
                "status": "parked" if errors else "accepted",
            }
        )
    edges.sort(key=lambda item: (item["src"], item["dst"], item["relation"]))
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(edges, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    output.with_name("edge-merge-report.json").write_text(
        json.dumps(
            {"edge_plan_id": plan["plan_id"], "jobs": report, "version": 1},
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {args.out}: {len(edges)} accepted model edge(s)")


if __name__ == "__main__":
    main()
