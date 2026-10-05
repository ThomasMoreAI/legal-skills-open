#!/usr/bin/env python3
"""Validate maker checkpoints and merge a coverage-complete findings ledger."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

from finding_validation import (
    dump_atomic,
    expected_job_id,
    expected_plan_id,
    hash_id,
    source_cache,
    validate_result,
)
from reconcile_counts import privilege_holds, unit_map


def load(path, kind, required):
    try:
        with open(path, encoding="utf-8") as handle:
            value = json.load(handle)
    except (OSError, json.JSONDecodeError) as error:
        sys.exit(f"merge_finding_results: cannot read {kind}: {error}")
    for key in required:
        if key not in value:
            sys.exit(f"merge_finding_results: {kind} missing key {key!r}")
    return value


def framework_index(framework):
    lenses = {}
    all_issues = set()
    for lens in framework.get("lenses", []):
        lens_id = lens.get("lens_id")
        if not isinstance(lens_id, str) or lens_id in lenses:
            sys.exit("merge_finding_results: framework lens IDs are invalid")
        items = {}
        for item in lens.get("items", []):
            issue_id = item.get("issue_id")
            if not isinstance(issue_id, str) or issue_id in items:
                sys.exit(
                    f"merge_finding_results: issue IDs in lens {lens_id} are invalid"
                )
            if issue_id in all_issues:
                sys.exit(
                    f"merge_finding_results: issue ID {issue_id} repeats across lenses"
                )
            all_issues.add(issue_id)
            items[issue_id] = item
        lenses[lens_id] = items
    return lenses


def validate_plan(plan, framework, manifest, families, clusters):
    errors = []
    if plan.get("approved") is not True:
        errors.append("review plan is not lawyer-approved")
    approval = plan.get("approval")
    if not isinstance(approval, dict) or approval.get("by") != "lawyer":
        errors.append("review plan has no lawyer approval receipt")
    elif approval.get("plan_id") != plan.get("plan_id"):
        errors.append("review plan approval receipt names a different plan")
    if plan.get("framework_version") != framework.get("framework_version"):
        errors.append("review plan framework version does not match")
    framework_digest = hashlib.sha256(
        json.dumps(framework, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    if plan.get("framework_digest") != framework_digest:
        errors.append("review plan framework digest does not match")
    if plan.get("tier") not in {"sample", "targeted", "full"}:
        errors.append("review plan tier is invalid")
    if plan.get("tier") != "sample" and framework.get("approved") is not True:
        errors.append("non-sample review requires an approved framework")
    relation_confirmed = all(
        artifact is None or artifact.get("confirmed") is True
        for artifact in (families, clusters)
    )
    if relation_confirmed is not True:
        errors.append("review requires a confirmed family/cluster map")
    jobs = plan.get("jobs")
    if not isinstance(jobs, list):
        return [], {}, errors + ["review plan has no jobs array"]
    if plan.get("version") != 1:
        errors.append("review plan version is unsupported")
    if plan.get("plan_id") != expected_plan_id(plan):
        errors.append("review plan ID does not match its dispatch payload")

    docs = {document["id"]: document for document in manifest.get("documents", [])}
    family_units = {
        family.get("family_id")
        for family in (families or {}).get("families", [])
        if len(family.get("members", [])) > 1
    }
    map_errors = []
    to_unit = unit_map(manifest, families, clusters, map_errors)
    errors.extend(map_errors)
    lenses = framework_index(framework)
    seen_jobs = set()
    seen_pairs = set()
    normalized = []
    units_in_jobs = set()
    represented_units = set()
    for index, job in enumerate(jobs):
        if not isinstance(job, dict):
            errors.append(f"review plan job {index} is not an object")
            continue
        job_id = job.get("job_id")
        unit_id = job.get("unit_id")
        lens_id = job.get("lens_id")
        if job_id in seen_jobs:
            errors.append(f"review plan repeats job ID {job_id}")
        seen_jobs.add(job_id)
        pair = (unit_id, lens_id)
        if pair in seen_pairs:
            errors.append(f"review plan repeats unit/lens {unit_id}/{lens_id}")
        seen_pairs.add(pair)
        if lens_id not in lenses:
            errors.append(f"review plan job {job_id} has unknown lens {lens_id}")
            continue
        if job_id != expected_job_id(framework["framework_version"], unit_id, lens_id):
            errors.append(f"review plan job {job_id} has an invalid stable ID")
        issue_ids = job.get("issue_ids")
        if issue_ids != list(lenses[lens_id]):
            errors.append(f"review plan job {job_id} has wrong issue coverage")
        member_ids = job.get("member_ids")
        parked_member_ids = job.get("parked_member_ids")
        if (
            not isinstance(member_ids, list)
            or not member_ids
            or len(member_ids) != len(set(member_ids))
        ):
            errors.append(f"review plan job {job_id} has invalid members")
            continue
        if not isinstance(parked_member_ids, list) or len(parked_member_ids) != len(
            set(parked_member_ids)
        ):
            errors.append(f"review plan job {job_id} has invalid parked members")
            continue
        unit_documents = sorted(
            doc_id for doc_id in docs if to_unit.get(doc_id) == unit_id
        )
        expected_members = sorted(
            doc_id
            for doc_id in unit_documents
            if docs[doc_id].get("readability") in {"native", "scanned"}
        )
        expected_parked = sorted(set(unit_documents) - set(expected_members))
        if member_ids != expected_members:
            errors.append(f"review plan job {job_id} omits or adds reviewable members")
        if parked_member_ids != expected_parked:
            errors.append(f"review plan job {job_id} has wrong parked members")
        if job.get("contains_image") is not any(
            docs[doc_id].get("readability") == "scanned" for doc_id in expected_members
        ):
            errors.append(f"review plan job {job_id} has wrong image flag")
        if job.get("contains_unreadable") is not bool(expected_parked):
            errors.append(f"review plan job {job_id} has wrong unreadable flag")
        if job.get("requires_current_position") is not (unit_id in family_units):
            errors.append(f"review plan job {job_id} has wrong current-position flag")
        for field in (
            "estimated_image_pages",
            "estimated_input_tokens",
            "estimated_text_chars",
            "unknown_image_documents",
        ):
            if not isinstance(job.get(field), int) or job[field] < 0:
                errors.append(f"review plan job {job_id} has invalid {field}")
        for doc_id in member_ids:
            if doc_id not in docs:
                errors.append(f"review plan job {job_id} has unknown doc {doc_id}")
            elif to_unit.get(doc_id) != unit_id:
                errors.append(
                    f"review plan job {job_id} maps doc {doc_id} to wrong unit"
                )
        units_in_jobs.add(unit_id)
        represented_units.add(unit_id)
        normalized.append(job)
    expected_lenses = set(lenses)
    for unit_id in units_in_jobs:
        actual = {job["lens_id"] for job in normalized if job["unit_id"] == unit_id}
        if actual != expected_lenses:
            errors.append(f"review plan unit {unit_id} omits a framework lens")
    if plan.get("tier") == "sample" and len(units_in_jobs) > 5:
        errors.append("sample review plan exceeds five units")
    parked_units = plan.get("parked_units")
    if not isinstance(parked_units, list):
        errors.append("review plan parked_units must be an array")
    else:
        seen_parked = set()
        for index, item in enumerate(parked_units):
            if not isinstance(item, dict) or set(item) != {
                "member_ids",
                "reason",
                "unit_id",
            }:
                errors.append(f"review plan parked unit {index} has invalid shape")
                continue
            unit_id = item.get("unit_id")
            if unit_id in seen_parked or unit_id in represented_units:
                errors.append(f"review plan repeats or overlaps parked unit {unit_id}")
            seen_parked.add(unit_id)
            expected = sorted(
                doc_id for doc_id in docs if to_unit.get(doc_id) == unit_id
            )
            if not expected or item.get("member_ids") != expected:
                errors.append(f"review plan parked unit {unit_id} has wrong members")
            if not isinstance(item.get("reason"), str) or not item["reason"].strip():
                errors.append(f"review plan parked unit {unit_id} has no reason")
            if plan.get("tier") == "full" and str(item.get("reason", "")).startswith(
                "outside-approved-"
            ):
                errors.append("full review plan cannot park a unit as outside scope")
        expected_units = {
            mapped_unit for doc_id, mapped_unit in to_unit.items() if doc_id in docs
        }
        accounted_units = represented_units | seen_parked
        if accounted_units != expected_units:
            missing = sorted(expected_units - accounted_units)
            extra = sorted(accounted_units - expected_units)
            detail = []
            if missing:
                detail.append("missing " + ", ".join(missing))
            if extra:
                detail.append("extra " + ", ".join(extra))
            errors.append(
                "review plan does not account for every unit: " + "; ".join(detail)
            )
        expected_summary = {
            "estimated_image_pages": sum(
                item.get("estimated_image_pages", 0)
                if isinstance(item.get("estimated_image_pages"), int)
                else 0
                for item in normalized
            ),
            "estimated_input_tokens": sum(
                item.get("estimated_input_tokens", 0)
                if isinstance(item.get("estimated_input_tokens"), int)
                else 0
                for item in normalized
            ),
            "estimated_text_chars": sum(
                item.get("estimated_text_chars", 0)
                if isinstance(item.get("estimated_text_chars"), int)
                else 0
                for item in normalized
            ),
            "jobs": len(normalized),
            "parked_units": len(parked_units),
            "unique_units": len(represented_units),
            "unknown_image_documents": sum(
                item.get("unknown_image_documents", 0)
                if isinstance(item.get("unknown_image_documents"), int)
                else 0
                for item in normalized
            ),
        }
        if plan.get("summary") != expected_summary:
            errors.append("review plan summary does not match its jobs")
    return sorted(normalized, key=lambda item: item["job_id"]), lenses, errors


def merge_candidates(candidates, existing):
    ruled = sorted(
        (existing or {}).get("ruled", []), key=lambda item: item.get("doc_id", "")
    )
    ruled_ids = {item.get("doc_id") for item in ruled}
    grouped = {}
    for candidate in list((existing or {}).get("candidates", [])) + candidates:
        doc_id = candidate.get("doc_id")
        if not doc_id or doc_id in ruled_ids:
            continue
        grouped.setdefault(doc_id, []).append(candidate)
    pending = []
    for doc_id in sorted(grouped):
        items = sorted(
            grouped[doc_id],
            key=lambda item: (item.get("reason", ""), item.get("quote", "")),
        )
        first = dict(items[0])
        first["signals"] = sorted(
            {signal for item in items for signal in item.get("signals", [])}
        )
        first["reason"] = " | ".join(
            sorted({item.get("reason", "") for item in items if item.get("reason")})
        )
        pending.append(first)
    return {"candidates": pending, "ruled": ruled}


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--review-plan", required=True)
    parser.add_argument("--framework", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--room-root", required=True)
    parser.add_argument("--families", default=None)
    parser.add_argument("--clusters", default=None)
    parser.add_argument("--results", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--privilege-queue-out", default=None)
    parser.add_argument("--existing-privilege-queue", default=None)
    parser.add_argument("--extractor", choices=["auto", "stdlib"], default="auto")
    args = parser.parse_args()

    if args.existing_privilege_queue and not args.privilege_queue_out:
        sys.exit(
            "merge_finding_results: --existing-privilege-queue requires "
            "--privilege-queue-out"
        )
    if args.privilege_queue_out and Path(args.privilege_queue_out) == Path(args.out):
        sys.exit(
            "merge_finding_results: findings and privilege queue outputs must differ"
        )

    existing_queue = (
        load(
            args.existing_privilege_queue,
            "existing privilege queue",
            ["candidates", "ruled"],
        )
        if args.existing_privilege_queue
        else None
    )

    plan = load(args.review_plan, "review plan", ["jobs", "plan_id", "tier"])
    framework = load(
        args.framework, "framework", ["framework_version", "approved", "lenses"]
    )
    manifest = load(args.manifest, "manifest", ["documents", "counts"])
    families = load(args.families, "families", ["families"]) if args.families else None
    clusters = load(args.clusters, "clusters", ["threads"]) if args.clusters else None
    jobs, lenses, plan_errors = validate_plan(
        plan, framework, manifest, families, clusters
    )
    if plan_errors:
        sys.exit("merge_finding_results: " + "; ".join(plan_errors))
    docs, text_for = source_cache(
        manifest, os.path.abspath(args.room_root), args.extractor
    )

    accepted_findings = []
    accepted_candidates = []
    parked = []
    reports = []
    seen_finding_ids = set()
    results_dir = Path(args.results)
    for job in jobs:
        job = {
            **job,
            "framework_version": framework["framework_version"],
            "review_plan_id": plan["plan_id"],
        }
        result_path = results_dir / f"{job['job_id']}.json"
        errors = []
        for doc_id in job["member_ids"]:
            document = docs[doc_id]
            source_path = os.path.join(args.room_root, str(document["path"]))
            try:
                if hash_id(source_path) != doc_id:
                    errors.append(f"manifest identity changed for {document['path']}")
            except OSError:
                errors.append(f"cannot read source document {document['path']}")
        result = None
        if not result_path.is_file():
            errors.append("maker checkpoint missing")
        else:
            try:
                result = json.loads(result_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                errors.append("cannot read maker checkpoint")
        findings = candidates = []
        if result is not None and not errors:
            if result.get("framework_version") != framework["framework_version"]:
                errors.append("maker framework version does not match")
            try:
                findings, candidates, validation_errors = validate_result(
                    result, job, lenses[job["lens_id"]], docs, text_for
                )
                errors.extend(validation_errors)
            except OSError as error:
                errors.append(str(error))
        duplicate_ids = [
            finding["finding_id"]
            for finding in findings
            if finding["finding_id"] in seen_finding_ids
        ]
        if duplicate_ids:
            errors.append("duplicate finding IDs: " + ", ".join(duplicate_ids))
        if errors:
            parked.append(
                {
                    "job_id": job["job_id"],
                    "lens_id": job["lens_id"],
                    "member_ids": job["member_ids"],
                    "reason": "; ".join(errors),
                    "unit_id": job["unit_id"],
                }
            )
        else:
            accepted_findings.extend(findings)
            accepted_candidates.extend(candidates)
            seen_finding_ids.update(finding["finding_id"] for finding in findings)
        reports.append(
            {
                "errors": errors,
                "job_id": job["job_id"],
                "status": "parked" if errors else "accepted",
            }
        )

    for unit in plan.get("parked_units", []):
        if not any(
            docs[doc_id].get("readability") in {"native", "scanned"}
            for doc_id in unit.get("member_ids", [])
            if doc_id in docs
        ):
            continue
        for lens_id in lenses:
            parked.append(
                {
                    "job_id": expected_job_id(
                        framework["framework_version"], unit["unit_id"], lens_id
                    ),
                    "lens_id": lens_id,
                    "member_ids": unit.get("member_ids", []),
                    "reason": unit.get("reason", "unit parked during planning"),
                    "unit_id": unit["unit_id"],
                }
            )
    if accepted_candidates and not args.privilege_queue_out:
        sys.exit(
            "merge_finding_results: privilege candidates exist but no "
            "--privilege-queue-out was supplied"
        )

    final_queue = (
        merge_candidates(accepted_candidates, existing_queue)
        if args.privilege_queue_out
        else None
    )
    if final_queue is not None:
        hold_errors = []
        held_docs = privilege_holds(final_queue, docs, hold_errors)
        map_errors = []
        to_unit = unit_map(manifest, families, clusters, map_errors)
        hold_errors.extend(map_errors)
        if hold_errors:
            sys.exit("merge_finding_results: " + "; ".join(hold_errors))
        held_units = {to_unit[doc_id] for doc_id in held_docs}
        if held_units:
            accepted_findings = [
                finding
                for finding in accepted_findings
                if finding.get("unit_id") not in held_units
            ]
            parked_keys = {
                (item.get("unit_id"), item.get("lens_id")) for item in parked
            }
            reports_by_job = {item["job_id"]: item for item in reports}
            for job in jobs:
                if job["unit_id"] not in held_units:
                    continue
                key = (job["unit_id"], job["lens_id"])
                if key not in parked_keys:
                    parked.append(
                        {
                            "job_id": job["job_id"],
                            "lens_id": job["lens_id"],
                            "member_ids": job["member_ids"],
                            "reason": "privilege-candidate-awaiting-lawyer-ruling",
                            "unit_id": job["unit_id"],
                        }
                    )
                    parked_keys.add(key)
                report = reports_by_job[job["job_id"]]
                if report["status"] == "accepted":
                    report["status"] = "parked"
                    report["errors"] = ["privilege candidate awaiting lawyer ruling"]

    ledger = {
        "findings": sorted(
            accepted_findings, key=lambda item: item.get("finding_id", "")
        ),
        "framework_version": framework["framework_version"],
        "parked": sorted(parked, key=lambda item: (item["lens_id"], item["unit_id"])),
        "review_plan_id": plan["plan_id"],
    }
    dump_atomic(args.out, ledger)
    report_path = Path(args.out).with_name("finding-merge-report.json")
    dump_atomic(
        report_path,
        {
            "accepted_jobs": sum(item["status"] == "accepted" for item in reports),
            "jobs": reports,
            "parked_jobs": len(parked),
            "review_plan_id": plan["plan_id"],
            "version": 1,
        },
    )

    if args.privilege_queue_out:
        dump_atomic(args.privilege_queue_out, final_queue)
    print(
        f"Wrote {args.out}: {len(accepted_findings)} finding(s), "
        f"{len(parked)} parked job(s)"
    )


if __name__ == "__main__":
    main()
