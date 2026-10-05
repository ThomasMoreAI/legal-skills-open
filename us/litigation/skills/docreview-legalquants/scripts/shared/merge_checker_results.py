#!/usr/bin/env python3
"""Merge fresh-context checker verdicts into high-band findings."""

import argparse
import hashlib
import json
import os
import sys
import tempfile
from pathlib import Path

from build_checker_plan import canonical_digest, checker_plan_id, hash_id
from reconcile_counts import unit_map

VERDICTS = {"confirmed", "refuted", "unresolved"}
KEYS = {
    "checker_plan_id",
    "finding_id",
    "verdict",
    "objection",
    "quote_supported",
}


def result_name(finding_id):
    return hashlib.sha256(finding_id.encode()).hexdigest()[:16] + ".json"


def validate(result, finding_id, checker_plan_id):
    errors = []
    if not isinstance(result, dict) or set(result) != KEYS:
        return ["unexpected or missing checker keys"]
    if result.get("checker_plan_id") != checker_plan_id:
        errors.append("checker_plan_id mismatch")
    if result.get("finding_id") != finding_id:
        errors.append("finding_id mismatch")
    if result.get("verdict") not in VERDICTS:
        errors.append("invalid verdict")
    if not isinstance(result.get("quote_supported"), bool):
        errors.append("quote_supported must be boolean")
    objection = result.get("objection")
    if result.get("verdict") == "confirmed" and objection is not None:
        errors.append("confirmed verdict must have null objection")
    if (
        result.get("verdict") == "confirmed"
        and result.get("quote_supported") is not True
    ):
        errors.append("confirmed verdict requires quote_supported=true")
    if result.get("verdict") in {"refuted", "unresolved"} and (
        not isinstance(objection, str) or not objection.strip()
    ):
        errors.append("non-confirmed verdict requires an objection")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--findings", required=True)
    parser.add_argument("--framework", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--room-root", required=True)
    parser.add_argument("--families", default=None)
    parser.add_argument("--clusters", default=None)
    parser.add_argument("--checker-plan", required=True)
    parser.add_argument("--checker-results", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    try:
        data = json.loads(Path(args.findings).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        sys.exit(f"merge_checker_results: {error}")
    findings = data.get("findings")
    if not isinstance(findings, list):
        sys.exit("merge_checker_results: findings array missing")
    try:
        framework = json.loads(Path(args.framework).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        sys.exit(f"merge_checker_results: cannot read framework: {error}")
    try:
        manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
        families = (
            json.loads(Path(args.families).read_text(encoding="utf-8"))
            if args.families
            else None
        )
        clusters = (
            json.loads(Path(args.clusters).read_text(encoding="utf-8"))
            if args.clusters
            else None
        )
    except (OSError, json.JSONDecodeError) as error:
        sys.exit(f"merge_checker_results: cannot read unit map: {error}")
    if any(
        artifact is not None and artifact.get("confirmed") is not True
        for artifact in (families, clusters)
    ):
        sys.exit("merge_checker_results: family/cluster map is not confirmed")
    map_errors = []
    to_unit = unit_map(manifest, families, clusters, map_errors)
    if map_errors:
        sys.exit("merge_checker_results: " + "; ".join(map_errors))
    docs = {document["id"]: document for document in manifest.get("documents", [])}
    unit_docs = {}
    for doc_id in docs:
        unit_docs.setdefault(to_unit[doc_id], []).append(doc_id)
    try:
        plan = json.loads(Path(args.checker_plan).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        sys.exit(f"merge_checker_results: cannot read checker plan: {error}")
    if not isinstance(plan, dict) or plan.get("version") != 1:
        sys.exit("merge_checker_results: unsupported checker plan")
    if plan.get("source_findings_digest") != canonical_digest(data):
        sys.exit(
            "merge_checker_results: checker plan names a different findings ledger"
        )
    if plan.get("framework_version") != data.get("framework_version"):
        sys.exit("merge_checker_results: checker plan framework version mismatch")
    if plan.get("framework_digest") != canonical_digest(framework):
        sys.exit("merge_checker_results: checker plan framework digest mismatch")
    if framework.get("framework_version") != data.get("framework_version"):
        sys.exit("merge_checker_results: framework and findings versions differ")
    if plan.get("plan_id") != checker_plan_id(plan):
        sys.exit("merge_checker_results: checker plan ID is invalid")
    jobs = plan.get("jobs")
    if not isinstance(jobs, list):
        sys.exit("merge_checker_results: checker plan has no jobs array")
    jobs_by_finding = {}
    for job in jobs:
        if not isinstance(job, dict) or set(job) != {
            "finding_id",
            "issue_id",
            "job_id",
            "lens_id",
            "member_ids",
            "result_file",
            "unit_id",
        }:
            sys.exit("merge_checker_results: checker plan job has invalid shape")
        finding_id = job.get("finding_id")
        if not isinstance(finding_id, str) or not finding_id:
            sys.exit("merge_checker_results: checker plan job has no finding ID")
        member_ids = job.get("member_ids")
        if (
            not isinstance(member_ids, list)
            or not member_ids
            or len(member_ids) != len(set(member_ids))
            or any(not isinstance(doc_id, str) for doc_id in member_ids)
        ):
            sys.exit(
                "merge_checker_results: checker job members are invalid for "
                f"{finding_id}"
            )
        if finding_id in jobs_by_finding:
            sys.exit(f"merge_checker_results: checker plan repeats {finding_id}")
        if job.get("result_file") != result_name(finding_id):
            sys.exit(
                f"merge_checker_results: checker result name is wrong for {finding_id}"
            )
        if job.get("job_id") != result_name(finding_id)[:-5]:
            sys.exit(f"merge_checker_results: checker job ID is wrong for {finding_id}")
        expected_members = sorted(unit_docs.get(job.get("unit_id"), []))
        if member_ids != expected_members:
            sys.exit(
                f"merge_checker_results: checker unit is incomplete for {finding_id}"
            )
        for doc_id in member_ids:
            document = docs[doc_id]
            source_path = os.path.join(args.room_root, document["path"])
            try:
                if hash_id(source_path) != doc_id:
                    sys.exit(
                        f"merge_checker_results: manifest identity changed for {doc_id}"
                    )
            except OSError as error:
                sys.exit(f"merge_checker_results: cannot read {doc_id}: {error}")
        jobs_by_finding[finding_id] = job
    expected_high = {
        finding.get("finding_id")
        for finding in findings
        if finding.get("status") == "present" and finding.get("band") == "high"
    }
    if set(jobs_by_finding) != expected_high:
        sys.exit(
            "merge_checker_results: checker plan does not cover exact high findings"
        )
    report = []
    seen = set()
    for finding in findings:
        if finding.get("status") != "present" or finding.get("band") != "high":
            continue
        finding_id = finding.get("finding_id", "")
        if not finding_id:
            finding["status"] = "unresolved"
            finding["verification"] = {
                "checker": "adversarial",
                "objection": "high-band finding has no finding_id",
                "status": "unresolved",
            }
            report.append({"errors": ["finding_id missing"], "finding_id": ""})
            continue
        if finding_id in seen:
            finding["status"] = "unresolved"
            finding["verification"] = {
                "checker": "adversarial",
                "objection": "duplicate high-band finding_id",
                "status": "unresolved",
            }
            report.append({"errors": ["finding_id repeated"], "finding_id": finding_id})
            continue
        seen.add(finding_id)
        job = jobs_by_finding[finding_id]
        if (
            job.get("issue_id") != finding.get("issue_id")
            or job.get("lens_id") != finding.get("lens_id")
            or job.get("unit_id") != finding.get("unit_id")
            or finding.get("doc_id") not in job.get("member_ids", [])
        ):
            sys.exit(f"merge_checker_results: checker job drifted for {finding_id}")
        path = Path(args.checker_results) / job["result_file"]
        errors = []
        result = None
        if (finding.get("quote_verification") or {}).get("status") != "confirmed":
            errors.append("deterministic quote verification is not confirmed")
        if not path.is_file():
            errors.append("checker result missing")
        else:
            try:
                result = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                errors.append("cannot read checker result")
        if result is not None and not errors:
            errors = validate(result, finding_id, plan["plan_id"])
        if errors:
            finding["status"] = "unresolved"
            finding["verification"] = {
                "checker": "adversarial",
                "objection": "; ".join(errors),
                "status": "unresolved",
            }
        else:
            assert result is not None
            verdict = result["verdict"]
            finding["verification"] = {
                "checker": "adversarial",
                "objection": result["objection"],
                "status": verdict,
            }
            if verdict != "confirmed" or not result["quote_supported"]:
                finding["status"] = "unresolved"
        report.append({"errors": errors, "finding_id": finding_id})
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=output.name + ".", dir=output.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2, sort_keys=True)
            handle.write("\n")
        os.replace(temporary, output)
    except BaseException:
        try:
            os.unlink(temporary)
        except OSError:
            pass
        raise
    report_path = output.with_name("checker-merge-report.json")
    report_path.write_text(
        json.dumps(
            {"checker_plan_id": plan["plan_id"], "findings": report, "version": 1},
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Merged {len(report)} high-band checker result(s)")


if __name__ == "__main__":
    main()
