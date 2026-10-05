#!/usr/bin/env python3
"""Verify coverage: for each lens, findings plus parked equals reviewable units.

Usage:
    python3 reconcile_counts.py --manifest manifest.json --findings findings.json \
        --framework framework.json [--families families.json]

Reviewable units are manifest documents with readability native or scanned,
collapsed to unique unit ids (a family or thread counts once). A reviewed
unit must have exactly one result for every issue in every lens. Global checks
cover identity, receipts, current-position assertions, material checker
confirmation, privilege holds, and manifest membership.

Exit 0 when every lens reconciles and no global check fails, 1 otherwise,
with a precise per-lens report on stdout. Importable:
reconcile(manifest, findings, framework, families=None) -> result dict.
render_report.py refuses to issue the Gate 3 report unless this passes.
"""

import argparse
import hashlib
import json
import sys
from typing import Any

REVIEWABLE = {"native", "scanned"}


def review_plan_id(plan):
    payload = {
        "framework_digest": plan.get("framework_digest"),
        "framework_version": plan.get("framework_version"),
        "jobs": plan.get("jobs"),
        "parked_units": plan.get("parked_units"),
        "summary": plan.get("summary"),
        "tier": plan.get("tier"),
        "version": plan.get("version"),
    }
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def load(path, kind, required_keys):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"reconcile_counts: cannot read {kind} at {path}: {e}")
    for k in required_keys:
        if k not in data:
            sys.exit(f"reconcile_counts: {kind} missing key '{k}'")
    return data


def unit_map(manifest, families, clusters=None, errors=None):
    """Map doc IDs to units, collapsing family members into one family ID."""
    errors = errors if errors is not None else []
    to_unit = {}
    manifest_ids = {document.get("id") for document in manifest.get("documents", [])}

    def assign(doc_id, unit_id, source):
        prior = to_unit.get(doc_id)
        if prior is not None and prior != unit_id:
            errors.append(
                f"doc {doc_id} is assigned to both {prior} and {unit_id} ({source})"
            )
        else:
            to_unit[doc_id] = unit_id

    if families:
        for fam in families.get("families", []):
            fid = fam.get("family_id", "")
            if not fid:
                errors.append("family map contains a family without family_id")
            for m in fam.get("members", []):
                doc_id = m.get("id")
                if doc_id not in manifest_ids:
                    errors.append(
                        f"family map references doc {doc_id} absent from manifest"
                    )
                    continue
                assign(doc_id, fid, "family map")
    if clusters:
        for thread in clusters.get("threads", []):
            tid = thread.get("cluster_id") or thread.get("thread_id", "")
            if not tid:
                errors.append("thread map contains a thread without cluster_id")
            for doc_id in thread.get("members", []):
                if doc_id not in manifest_ids:
                    errors.append(
                        f"thread map references doc {doc_id} absent from manifest"
                    )
                    continue
                assign(doc_id, tid, "thread map")
    for d in manifest.get("documents", []):
        to_unit.setdefault(d["id"], d["id"])
    return to_unit


def privilege_holds(queue, docs, errors):
    if not queue:
        return set()
    candidates = queue.get("candidates", [])
    ruled = queue.get("ruled", [])
    pending = set()
    for item in candidates:
        doc_id = item.get("doc_id", "")
        if doc_id not in docs:
            errors.append(
                f"privilege candidate references doc {doc_id} absent from the manifest"
            )
        if doc_id in pending:
            errors.append(f"privilege queue repeats pending doc {doc_id}")
        pending.add(doc_id)
    rulings = {}
    for item in ruled:
        doc_id = item.get("doc_id", "")
        if doc_id not in docs:
            errors.append(
                f"privilege ruling references doc {doc_id} absent from the manifest"
            )
        if doc_id in rulings:
            errors.append(f"privilege queue repeats ruled doc {doc_id}")
        if item.get("by") != "lawyer":
            errors.append(f"privilege ruling for {doc_id} was not recorded by lawyer")
        if item.get("ruling") not in {"privileged", "not-privileged", "needs-review"}:
            errors.append(f"privilege ruling for {doc_id} is invalid")
        rulings[doc_id] = item.get("ruling")
    overlap = pending & set(rulings)
    for doc_id in sorted(overlap):
        errors.append(f"privilege doc {doc_id} appears in both pending and ruled lanes")
    return pending | {
        doc_id
        for doc_id, ruling in rulings.items()
        if ruling in {"privileged", "needs-review"}
    }


def reconcile(
    manifest,
    findings,
    framework,
    families=None,
    clusters=None,
    privilege_queue=None,
    review_plan=None,
):
    """Return {"ok", "lines", "errors", "totals", "per_lens", plus unit lists}."""
    docs = {d["id"]: d for d in manifest.get("documents", [])}
    errors = []
    if families is not None and families.get("confirmed") is not True:
        errors.append("family map is not lawyer-confirmed")
    if clusters is not None and clusters.get("confirmed") is not True:
        errors.append("cluster map is not lawyer-confirmed")
    to_unit = unit_map(manifest, families, clusters, errors)

    unit_docs = {}
    for did in docs:
        unit_docs.setdefault(to_unit[did], set()).add(did)
    family_units = {
        family.get("family_id", "")
        for family in (families or {}).get("families", [])
        if len(family.get("members", [])) > 1
    }
    all_units = set(unit_docs)
    reviewable = {
        u
        for u, ds in unit_docs.items()
        if any(docs[d].get("readability") in REVIEWABLE for d in ds)
    }
    unreadable = all_units - reviewable

    fw_v = framework.get("framework_version")
    fi_v = findings.get("framework_version")
    if fw_v != fi_v:
        errors.append(
            f"findings carry framework_version {fi_v} but framework is version {fw_v}"
        )

    ledger_plan_id = findings.get("review_plan_id")
    if ledger_plan_id is not None and review_plan is None:
        errors.append("findings name a review plan but no review plan was supplied")
    if review_plan is not None:
        if review_plan.get("plan_id") != review_plan_id(review_plan):
            errors.append("review plan ID does not match its dispatch payload")
        if review_plan.get("plan_id") != ledger_plan_id:
            errors.append("findings and review plan IDs do not match")
        if review_plan.get("approved") is not True:
            errors.append("review plan is not approved")
        approval = review_plan.get("approval")
        if not isinstance(approval, dict) or approval.get("by") != "lawyer":
            errors.append("review plan lacks a lawyer approval receipt")
        elif approval.get("plan_id") != review_plan.get("plan_id"):
            errors.append("review plan approval receipt names a different plan")
        if review_plan.get("framework_version") != fw_v:
            errors.append("review plan and framework versions do not match")
        framework_digest = hashlib.sha256(
            json.dumps(framework, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
        if review_plan.get("framework_digest") != framework_digest:
            errors.append("review plan and framework digests do not match")

    lens_ids = [lens["lens_id"] for lens in framework.get("lenses", [])]
    if len(lens_ids) != len(set(lens_ids)):
        errors.append("framework repeats a lens ID")
    lens_issues = {
        lens["lens_id"]: {item["issue_id"]: item for item in lens.get("items", [])}
        for lens in framework.get("lenses", [])
    }

    parked_by_lens = {lens_id: set() for lens_id in lens_ids}
    for p in findings.get("parked", []):
        lens_id = p.get("lens_id")
        if lens_id is not None and lens_id not in parked_by_lens:
            errors.append(f"parked entry references unknown lens {lens_id}")
            continue
        unit_id = p.get("unit_id")
        if unit_id is None:
            did = p.get("doc_id", "")
            if did not in docs:
                errors.append(
                    f"parked entry references doc {did} absent from the manifest"
                )
                continue
            unit_id = to_unit[did]
        elif unit_id not in unit_docs:
            errors.append(
                f"parked entry references unit {unit_id} absent from the manifest"
            )
            continue
        member_ids = p.get("member_ids")
        if member_ids is not None:
            if (
                not isinstance(member_ids, list)
                or len(member_ids) != len(set(member_ids))
                or any(doc_id not in unit_docs[unit_id] for doc_id in member_ids)
            ):
                errors.append(f"parked entry for unit {unit_id} has invalid members")
        target_lenses = [lens_id] if lens_id is not None else lens_ids
        for target in target_lenses:
            if unit_id in parked_by_lens[target]:
                errors.append(f"unit {unit_id} repeats a parked entry in lens {target}")
            parked_by_lens[target].add(unit_id)
    held_docs = privilege_holds(privilege_queue, docs, errors)
    held_units = {to_unit[doc_id] for doc_id in held_docs if doc_id in to_unit}
    for lens_id in lens_ids:
        parked_by_lens[lens_id] |= held_units
    per_lens: dict[str, dict[str, Any]] = {
        lens_id: {
            "found_units": set(),
            "issues_by_unit": {},
            "status_counts": {"present": 0, "absent": 0, "unresolved": 0},
        }
        for lens_id in lens_ids
    }
    seen_issue_units = set()

    for f in findings.get("findings", []):
        fid = f.get("finding_id", "<no id>")
        did = f.get("doc_id", "")
        if did not in docs:
            errors.append(
                f"finding {fid} references doc {did} absent from the manifest"
            )
            continue
        status = f.get("status", "")
        if status not in {"present", "absent", "unresolved"}:
            errors.append(f"finding {fid} has invalid status '{status}'")
        if status == "present" and not (f.get("quote") or "").strip():
            errors.append(f"finding {fid} has status present with an empty quote")
        if status == "present" and (
            (f.get("quote_verification") or {}).get("status") != "confirmed"
        ):
            errors.append(
                f"finding {fid} is present without confirmed quote verification"
            )
        unit = f.get("unit_id") or to_unit[did]
        if unit != to_unit[did]:
            errors.append(
                f"finding {fid} claims unit {unit} but doc {did} maps to {to_unit[did]}"
            )
        if did in held_docs or unit in held_units:
            errors.append(f"finding {fid} references privilege-held unit {unit}")
        lid = f.get("lens_id", "")
        if lid not in per_lens:
            errors.append(f"finding {fid} references unknown lens '{lid}'")
            continue
        issue_id = f.get("issue_id", "")
        item = lens_issues[lid].get(issue_id)
        if item is None:
            errors.append(
                f"finding {fid} references issue '{issue_id}' outside lens '{lid}'"
            )
            continue
        expected_id = f"{issue_id}/{did}"
        if fid != expected_id:
            errors.append(f"finding {fid} must have stable id {expected_id}")
        issue_unit = (lid, issue_id, unit)
        if issue_unit in seen_issue_units:
            errors.append(f"unit {unit} repeats issue {issue_id} in lens {lid}")
        seen_issue_units.add(issue_unit)
        per_lens[lid]["issues_by_unit"].setdefault(unit, set()).add(issue_id)
        if status == "present":
            if not isinstance(f.get("section"), str) or not f["section"].strip():
                errors.append(f"finding {fid} is present without a section")
            if f.get("band") not in {"high", "medium", "low"}:
                errors.append(f"finding {fid} is present without a valid band")
            if not isinstance(f.get("band_basis"), str) or not f["band_basis"].strip():
                errors.append(f"finding {fid} is present without a band basis")
            word_cap = (item.get("answer_shape") or {}).get(
                "characterization_max_words"
            )
            characterization = f.get("characterization", "")
            if not isinstance(characterization, str) or not characterization.strip():
                errors.append(f"finding {fid} is present without a characterization")
            elif isinstance(word_cap, int) and len(characterization.split()) > word_cap:
                errors.append(
                    f"finding {fid} exceeds characterization word cap {word_cap}"
                )
            if unit in family_units and f.get("current_position") is not True:
                errors.append(
                    f"finding {fid} is present in a multi-document unit without "
                    "current_position=true"
                )
            if f.get("band") == "high" and (
                (f.get("verification") or {}).get("status") != "confirmed"
                or (f.get("verification") or {}).get("checker") != "adversarial"
            ):
                errors.append(
                    f"finding {fid} is high-band without adversarial confirmation"
                )
        counts = per_lens[lid]["status_counts"]
        counts[status] = counts.get(status, 0) + 1

    lines = []
    ok = not errors
    for lid in lens_ids:
        info = per_lens[lid]
        parked_units = parked_by_lens[lid]
        expected_issues = set(lens_issues[lid])
        for unit, found_issues in sorted(info["issues_by_unit"].items()):
            if found_issues == expected_issues:
                info["found_units"].add(unit)
                continue
            missing_issues = sorted(expected_issues - found_issues)
            extra_issues = sorted(found_issues - expected_issues)
            detail = []
            if missing_issues:
                detail.append("missing " + ", ".join(missing_issues))
            if extra_issues:
                detail.append("extra " + ", ".join(extra_issues))
            errors.append(
                f"unit {unit} has incomplete issue coverage in lens {lid}: "
                + "; ".join(detail)
            )
        covered = info["found_units"] | parked_units
        missing = sorted(reviewable - covered)
        extra = sorted(covered - reviewable)
        overlap = sorted(info["found_units"] & parked_units)
        lens_ok = not missing and not extra and not overlap
        info.update(
            missing=missing,
            extra=extra,
            overlap=overlap,
            ok=lens_ok,
            parked=len(parked_units),
            found_units=sorted(info["found_units"]),
            issues_by_unit={
                unit: sorted(issue_ids)
                for unit, issue_ids in sorted(info["issues_by_unit"].items())
            },
        )
        line = (
            f"lens {lid}: {len(info['found_units'])} finding units + "
            f"{len(parked_units)} parked = {len(covered)} of "
            f"{len(reviewable)} reviewable units: "
            f"{'OK' if lens_ok else 'FAIL'}"
        )
        if missing:
            line += f" (missing: {', '.join(missing)})"
        if extra:
            line += f" (not reviewable: {', '.join(extra)})"
        if overlap:
            line += f" (both found and parked: {', '.join(overlap)})"
        lines.append(line)
        ok = ok and lens_ok

    ok = ok and not errors

    found_union = set()
    for lid in lens_ids:
        found_union |= set(per_lens[lid]["found_units"])
    parked_union = set().union(*parked_by_lens.values()) if parked_by_lens else set()
    totals = {
        "units": len(all_units),
        "reviewable": len(reviewable),
        "unreadable": len(unreadable),
        "parked": len(parked_union),
        "reviewed": len(found_union - parked_union),
    }
    return {
        "ok": ok,
        "lines": lines,
        "errors": errors,
        "totals": totals,
        "per_lens": per_lens,
        "reviewable_units": sorted(reviewable),
        "unreadable_units": sorted(unreadable),
        "parked_units": sorted(parked_union),
    }


def main():
    ap = argparse.ArgumentParser(
        description="Reconcile findings coverage against the manifest."
    )
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--findings", required=True)
    ap.add_argument("--framework", required=True)
    ap.add_argument("--families", default=None)
    ap.add_argument("--clusters", default=None)
    ap.add_argument("--privilege-queue", default=None)
    ap.add_argument("--review-plan", default=None)
    args = ap.parse_args()

    manifest = load(args.manifest, "manifest", ["documents", "counts"])
    findings = load(args.findings, "findings", ["findings"])
    framework = load(args.framework, "framework", ["framework_version", "lenses"])
    families = load(args.families, "families", ["families"]) if args.families else None
    clusters = load(args.clusters, "clusters", ["threads"]) if args.clusters else None
    privilege_queue = (
        load(args.privilege_queue, "privilege queue", ["candidates", "ruled"])
        if args.privilege_queue
        else None
    )
    review_plan = (
        load(args.review_plan, "review plan", ["plan_id", "jobs"])
        if args.review_plan
        else None
    )

    r = reconcile(
        manifest,
        findings,
        framework,
        families,
        clusters,
        privilege_queue,
        review_plan,
    )
    t = r["totals"]
    print(
        f"units: {t['units']} total, {t['reviewable']} reviewable, "
        f"{t['unreadable']} unreadable"
    )
    print(
        f"equation: {t['reviewed']} reviewed + {t['parked']} parked + "
        f"{t['unreadable']} unreadable = {t['units']} manifest units"
    )
    for line in r["lines"]:
        print(line)
    for e in r["errors"]:
        print(f"error: {e}")
    print("RECONCILED" if r["ok"] else "NOT RECONCILED")
    sys.exit(0 if r["ok"] else 1)


if __name__ == "__main__":
    main()
