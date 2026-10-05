#!/usr/bin/env python3
"""Build the deterministic fresh-context dispatch plan for high findings."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

from reconcile_counts import privilege_holds, unit_map


def load(path, kind, required):
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        sys.exit(f"build_checker_plan: cannot read {kind}: {error}")
    for key in required:
        if key not in value:
            sys.exit(f"build_checker_plan: {kind} missing key {key!r}")
    return value


def canonical_digest(value):
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode()).hexdigest()


def result_name(finding_id):
    return hashlib.sha256(finding_id.encode()).hexdigest()[:16] + ".json"


def hash_id(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()[:12]


def checker_plan_id(plan):
    payload = {
        "framework_digest": plan["framework_digest"],
        "framework_version": plan["framework_version"],
        "jobs": plan["jobs"],
        "source_findings_digest": plan["source_findings_digest"],
        "version": plan["version"],
    }
    return canonical_digest(payload)[:16]


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--findings", required=True)
    parser.add_argument("--framework", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--room-root", required=True)
    parser.add_argument("--families", default=None)
    parser.add_argument("--clusters", default=None)
    parser.add_argument("--privilege-queue", default=None)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    findings = load(args.findings, "findings", ["framework_version", "findings"])
    framework = load(args.framework, "framework", ["framework_version", "lenses"])
    manifest = load(args.manifest, "manifest", ["documents", "counts"])
    families = load(args.families, "families", ["families"]) if args.families else None
    clusters = load(args.clusters, "clusters", ["threads"]) if args.clusters else None
    queue = (
        load(args.privilege_queue, "privilege queue", ["candidates", "ruled"])
        if args.privilege_queue
        else None
    )
    errors = []
    if findings["framework_version"] != framework["framework_version"]:
        errors.append("findings and framework versions do not match")
    if any(
        artifact is not None and artifact.get("confirmed") is not True
        for artifact in (families, clusters)
    ):
        errors.append("checker planning requires confirmed family/cluster maps")

    docs = {document["id"]: document for document in manifest["documents"]}
    for doc_id, document in sorted(docs.items()):
        path = os.path.join(args.room_root, document["path"])
        try:
            if hash_id(path) != doc_id:
                errors.append(f"manifest identity changed for {document['path']}")
        except OSError as error:
            errors.append(f"cannot read {document['path']}: {error}")
    to_unit = unit_map(manifest, families, clusters, errors)
    unit_docs = {}
    for doc_id in docs:
        unit_docs.setdefault(to_unit[doc_id], []).append(doc_id)
    issues = {}
    for lens in framework["lenses"]:
        lens_id = lens.get("lens_id")
        for item in lens.get("items", []):
            issue_id = item.get("issue_id")
            if issue_id in issues:
                errors.append(f"framework repeats issue ID {issue_id}")
            issues[issue_id] = lens_id
    held_docs = privilege_holds(queue, docs, errors)
    held_units = {to_unit[doc_id] for doc_id in held_docs if doc_id in to_unit}

    jobs = []
    seen = set()
    for finding in findings["findings"]:
        if finding.get("status") != "present" or finding.get("band") != "high":
            continue
        finding_id = finding.get("finding_id")
        doc_id = finding.get("doc_id")
        unit_id = finding.get("unit_id")
        issue_id = finding.get("issue_id")
        lens_id = finding.get("lens_id")
        if not isinstance(finding_id, str) or not finding_id:
            errors.append("high finding has no finding_id")
            continue
        if finding_id in seen:
            errors.append(f"high finding ID repeats: {finding_id}")
            continue
        seen.add(finding_id)
        if doc_id not in docs:
            errors.append(f"high finding {finding_id} cites an unknown document")
            continue
        expected_unit = to_unit[doc_id]
        if unit_id != expected_unit:
            errors.append(f"high finding {finding_id} names the wrong unit")
        if finding_id != f"{issue_id}/{doc_id}":
            errors.append(f"high finding {finding_id} has an invalid stable ID")
        if issues.get(issue_id) != lens_id:
            errors.append(f"high finding {finding_id} names the wrong lens or issue")
        if (finding.get("quote_verification") or {}).get("status") != "confirmed":
            errors.append(f"high finding {finding_id} lacks a confirmed text quote")
        if unit_id in held_units:
            errors.append(f"high finding {finding_id} touches a privilege-held unit")
        jobs.append(
            {
                "finding_id": finding_id,
                "issue_id": issue_id,
                "job_id": result_name(finding_id)[:-5],
                "lens_id": lens_id,
                "member_ids": sorted(unit_docs.get(unit_id, [])),
                "result_file": result_name(finding_id),
                "unit_id": unit_id,
            }
        )
    if errors:
        sys.exit("build_checker_plan: " + "; ".join(errors))
    jobs.sort(key=lambda item: item["job_id"])
    plan = {
        "framework_digest": canonical_digest(framework),
        "framework_version": framework["framework_version"],
        "jobs": jobs,
        "source_findings_digest": canonical_digest(findings),
        "version": 1,
    }
    plan["plan_id"] = checker_plan_id(plan)
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(plan, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"Wrote {args.out}: {len(jobs)} independent checker job(s)")


if __name__ == "__main__":
    main()
