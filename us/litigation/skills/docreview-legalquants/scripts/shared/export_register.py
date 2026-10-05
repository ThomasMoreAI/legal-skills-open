#!/usr/bin/env python3
"""Export the further-enquiries register as register.csv plus register.json.

Usage:
    python3 export_register.py --findings findings.json --gaps gap-report.json \
        [--families families.json] --manifest manifest.json \
        [--framework framework.json] --out register.csv

One row per underlying ask: a missing document (gap entries of type
index-missing or referenced-absent), an unresolved finding (the clarification
its unresolved_when rule implies; --framework supplies the rule text, else the
finding's own characterization stands in), or a cross-document inconsistency
(findings on one issue within one family with conflicting present and absent
statuses). Rows deduplicate on (category, ask); source_refs merge. Ordering is
deterministic by (category, register_id). register.json is written beside the
CSV with the same rows.
"""

import argparse
import csv
import hashlib
import json
import os
import sys

import reconcile_counts

MISSING_GAP_TYPES = {"index-missing", "referenced-absent"}
CSV_COLUMNS = ["register_id", "category", "ask", "evidence", "source_refs"]


def load(path, kind, required_keys):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"export_register: cannot read {kind} at {path}: {e}")
    for k in required_keys:
        if k not in data:
            sys.exit(f"export_register: {kind} missing key '{k}'")
    return data


def register_id(category, source_refs):
    h = hashlib.sha256(f"{category}|{source_refs}".encode()).hexdigest()[:12]
    return f"{category}-{h}"


def doc_path(doc_id, docs):
    d = docs.get(doc_id)
    return d.get("path", doc_id) if d else doc_id


def issue_lookup(framework):
    """issue_id -> (question, unresolved_when). Empty when no framework given."""
    table = {}
    if not framework:
        return table
    for lens in framework.get("lenses", []):
        for item in lens.get("items", []):
            table[item.get("issue_id", "")] = (
                item.get("question", ""),
                item.get("evidence", {}).get("unresolved_when", ""),
            )
    return table


def one_sentence(s):
    s = " ".join(str(s).split()).strip()
    if s and not s.endswith("."):
        s += "."
    return s


def gap_rows(gaps):
    rows = []
    entries = sorted(
        (e for e in gaps.get("entries", []) if e.get("type") in MISSING_GAP_TYPES),
        key=lambda e: (e.get("type", ""), e.get("detail", "")),
    )
    for e in entries:
        detail = e.get("detail", "")
        rows.append(
            {
                "category": "missing-document",
                "ask": one_sentence(f"Supply the missing document: {detail}"),
                "evidence": e.get("evidence", ""),
                "source_refs": f"gap:{e.get('type', '')}:{e.get('evidence', '')}",
            }
        )
    return rows


def unresolved_rows(findings, docs, issues):
    rows = []
    unresolved = sorted(
        (f for f in findings.get("findings", []) if f.get("status") == "unresolved"),
        key=lambda f: f.get("finding_id", ""),
    )
    for f in unresolved:
        path = doc_path(f.get("doc_id", ""), docs)
        question, rule = issues.get(f.get("issue_id", ""), ("", ""))
        if question and rule:
            ask = f"To answer '{question}' for {path}, clarify: {rule}"
        else:
            ask = (
                "Clarify the unresolved finding on "
                f"{f.get('issue_id', '')} for {path}: "
                f"{f.get('characterization', '')}"
            )
        rows.append(
            {
                "category": "unresolved",
                "ask": one_sentence(ask),
                "evidence": (f.get("quote") or "").strip()
                or f.get("characterization", ""),
                "source_refs": f.get("finding_id", ""),
            }
        )
    return rows


def inconsistency_rows(findings, families, docs):
    family_ids = {
        family.get("family_id", "") for family in families.get("families", [])
    }
    groups = {}
    for f in findings.get("findings", []):
        if f.get("unit_id") in family_ids:
            groups.setdefault((f.get("issue_id", ""), f.get("unit_id", "")), []).append(
                f
            )
    rows = []
    for issue_id, unit_id in sorted(groups):
        members = sorted(
            groups[(issue_id, unit_id)], key=lambda f: f.get("finding_id", "")
        )
        present = [f for f in members if f.get("status") == "present"]
        absent = [f for f in members if f.get("status") == "absent"]
        if not (present and absent):
            continue
        fam_label = doc_path(unit_id, docs)
        p_paths = ", ".join(doc_path(f.get("doc_id", ""), docs) for f in present)
        a_paths = ", ".join(doc_path(f.get("doc_id", ""), docs) for f in absent)
        ask = (
            f"Reconcile the conflicting positions on {issue_id} within the family "
            f"based on {fam_label}: {p_paths} reports present while {a_paths} "
            "reports absent"
        )
        refs = ";".join(sorted(f.get("finding_id", "") for f in present + absent))
        rows.append(
            {
                "category": "inconsistency",
                "ask": one_sentence(ask),
                "evidence": (present[0].get("quote") or "").strip()
                or present[0].get("characterization", ""),
                "source_refs": refs,
            }
        )
    return rows


def build_rows(findings, gaps, families, manifest, framework=None):
    docs = {d["id"]: d for d in manifest.get("documents", [])}
    issues = issue_lookup(framework)
    raw = (
        gap_rows(gaps)
        + unresolved_rows(findings, docs, issues)
        + inconsistency_rows(findings, families, docs)
    )
    # Dedup: one row per underlying ask; merge source refs.
    merged = {}
    for r in raw:
        key = (r["category"], r["ask"].casefold())
        if key in merged:
            refs = set(merged[key]["source_refs"].split(";")) | set(
                r["source_refs"].split(";")
            )
            merged[key]["source_refs"] = ";".join(sorted(refs))
        else:
            merged[key] = r
    rows = []
    for r in merged.values():
        r["register_id"] = register_id(r["category"], r["source_refs"])
        rows.append({c: r[c] for c in CSV_COLUMNS})
    rows.sort(key=lambda r: (r["category"], r["register_id"]))
    return rows


def main():
    ap = argparse.ArgumentParser(description="Export the further-enquiries register.")
    ap.add_argument("--findings", required=True)
    ap.add_argument("--gaps", required=True)
    ap.add_argument(
        "--families",
        default=None,
        help="Confirmed family map. Optional for discovery runs with only clusters.",
    )
    ap.add_argument("--manifest", required=True)
    ap.add_argument(
        "--framework",
        default=None,
        help="optional; supplies question and unresolved_when text for asks",
    )
    ap.add_argument("--clusters", default=None)
    ap.add_argument("--privilege-queue", default=None)
    ap.add_argument(
        "--out",
        required=True,
        help="path for register.csv; register.json lands beside it",
    )
    args = ap.parse_args()

    findings = load(args.findings, "findings", ["findings"])
    gaps = load(args.gaps, "gap report", ["entries"])
    families = (
        load(args.families, "families", ["families"])
        if args.families
        else {"confirmed": True, "families": [], "orphans": []}
    )
    manifest = load(args.manifest, "manifest", ["documents", "counts"])
    framework = (
        load(args.framework, "framework", ["framework_version", "lenses"])
        if args.framework
        else None
    )
    clusters = load(args.clusters, "clusters", ["threads"]) if args.clusters else None
    privilege_queue = (
        load(args.privilege_queue, "privilege queue", ["candidates", "ruled"])
        if args.privilege_queue
        else None
    )

    if privilege_queue:
        docs = {doc["id"]: doc for doc in manifest.get("documents", [])}
        errors = []
        to_unit = reconcile_counts.unit_map(manifest, families, clusters, errors)
        held_docs = reconcile_counts.privilege_holds(privilege_queue, docs, errors)
        held_units = {to_unit[doc_id] for doc_id in held_docs if doc_id in to_unit}
        for finding in findings.get("findings", []):
            doc_id = finding.get("doc_id", "")
            unit_id = finding.get("unit_id") or to_unit.get(doc_id)
            if doc_id in held_docs or unit_id in held_units:
                errors.append(
                    f"finding {finding.get('finding_id', '<no id>')} touches "
                    f"privilege-held unit {unit_id}"
                )
        if errors:
            sys.exit("export_register: " + "; ".join(errors))

    rows = build_rows(findings, gaps, families, manifest, framework)

    with open(args.out, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        w.writerow(CSV_COLUMNS)
        for r in rows:
            w.writerow([r[c] for c in CSV_COLUMNS])

    json_path = os.path.splitext(args.out)[0] + ".json"
    with open(json_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump({"rows": rows}, f, sort_keys=True, indent=2)
        f.write("\n")

    print(f"wrote {args.out} and {json_path} ({len(rows)} rows)")


if __name__ == "__main__":
    main()
