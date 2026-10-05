#!/usr/bin/env python3
"""Assemble contract families from candidates, rule edges, and model edges.

Rule edges: within candidate pairs, a document's reference string matches
another document's title (token overlap >= 0.6), date (exact when both the
reference and the target carry one), and parties (>= 1 shared normalized
party); relation inferred from the referencing doc_type (amendment -> amends,
sow -> sow-under, schedule/exhibit -> schedule-of, guaranty -> guarantees).
Near-duplicates (different hashes, identical normalized title and equal
dated) get duplicate-of edges. Model edges load from --model-edges; when
--room-root is given each quote is re-verified against the source document
and failures are parked (listed on stderr, never entered). Union-find over
accepted edges yields families.json; reference strings matching no document
append deduplicated referenced-absent entries to gap-report.json.

Usage:
    python3 build_families.py --manifest manifest.json --metadata metadata/ \
        --candidates candidates.json --out families.json \
        --gap-report gap-report.json \
        [--model-edges model-edges.json] [--edge-plan-out edge-plan.json] \
        [--room-root room/]
"""

import argparse
import hashlib
import json
import os
import re
import sys
import unicodedata

from document_text import extract_document_text

ENTITY_SUFFIXES = {"inc", "llc", "ltd", "corp", "co", "lp", "llp", "plc", "gmbh", "pty"}
TITLE_OVERLAP = 0.6
RELATION_BY_DOC_TYPE = (
    ("amendment", "amends"),
    ("sow", "sow-under"),
    ("schedule", "schedule-of"),
    ("exhibit", "schedule-of"),
    ("guaranty", "guarantees"),
)
RELATIONS = {
    "amends",
    "sow-under",
    "schedule-of",
    "guarantees",
    "supersedes",
    "duplicate-of",
}
BASE_DOC_TYPE_TOKENS = {"master", "base", "agreement"}
MONTHS: dict[str, int] = {
    m: i
    for i, m in enumerate(
        "january february march april may june july august "
        "september october november december".split(),
        1,
    )
}
FAR_FUTURE = "9999-12-31"


def tokens(s):
    return re.sub(r"[^\w\s]+", " ", (s or "").casefold()).split()


def norm_party(name):
    toks = tokens(name)
    while toks and toks[-1] in ENTITY_SUFFIXES:
        toks.pop()
    return " ".join(toks)


def normalize(s):
    s = s.replace("\u00ad", "")
    s = unicodedata.normalize("NFKC", s)
    return re.sub(r"\s+", " ", s.casefold()).strip()


def extract_text(path):
    return extract_document_text(path)


def hash_id(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()[:12]


def receipt_source(value):
    if value == "image-read-human-confirmed":
        return value
    return "model-read" if value in {"model", "model-read"} else "regex"


def scalar_source(metadata, field):
    item = (metadata.get("evidence") or {}).get(field)
    return receipt_source(item.get("source")) if isinstance(item, dict) else "regex"


def ref_date(text):
    m = re.search(r"\b(\d{4})-(\d{1,2})-(\d{1,2})\b", text)
    if m:
        return "%04d-%02d-%02d" % tuple(int(g) for g in m.groups())
    m = re.search(
        r"\b(" + "|".join(MONTHS) + r")\.?\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})\b",
        text,
        re.IGNORECASE,
    )
    if m:
        return "%04d-%02d-%02d" % (
            int(m.group(3)),
            MONTHS[m.group(1).casefold()],
            int(m.group(2)),
        )
    return None


def infer_relation(doc_type):
    toks = set(tokens(doc_type))
    for key, relation in RELATION_BY_DOC_TYPE:
        if key in toks:
            return relation
    return None


def title_overlap(ref_toks, title):
    ttoks = set(tokens(title))
    return len(ttoks & ref_toks) / len(ttoks) if ttoks else 0.0


def ref_designator(text):
    """An 'Exhibit B ...' or 'Schedule 2 ...' reference names a document that
    IS that exhibit or schedule. Returns the designator tokens the target's
    title must contain, else a base agreement the reference merely mentions
    ('Exhibit B to the Master Services Agreement') would match instead."""
    toks = tokens(text)
    if len(toks) >= 2 and toks[0] in ("exhibit", "schedule"):
        return {toks[0], toks[1]}
    return None


def date_ok(rdate, dated):
    return rdate is None or dated is None or rdate == dated


def party_set(m):
    return {norm_party(p) for p in m.get("parties") or [] if norm_party(p)}


def load_metadata(mdir):
    meta = {}
    for name in sorted(os.listdir(mdir)):
        if not name.endswith(".json"):
            continue
        with open(os.path.join(mdir, name), encoding="utf-8") as f:
            rec = json.load(f)
        if rec.get("id"):
            meta[rec["id"]] = rec
    return meta


def main():
    ap = argparse.ArgumentParser(
        description="Assemble contract families and referenced-absent gaps."
    )
    ap.add_argument("--manifest", required=True, help="Path to manifest.json.")
    ap.add_argument("--metadata", required=True, help="Metadata directory.")
    ap.add_argument("--candidates", required=True, help="candidates.json path.")
    ap.add_argument("--out", required=True, help="families.json output path.")
    ap.add_argument(
        "--gap-report",
        required=True,
        help="gap-report.json to append referenced-absent entries to.",
    )
    ap.add_argument(
        "--model-edges",
        default=None,
        help="Optional model-edges.json: [{src, dst, relation, quote}].",
    )
    ap.add_argument(
        "--edge-plan-out",
        default=None,
        help="Optional isolated pair plan for unresolved candidate residue.",
    )
    ap.add_argument(
        "--room-root",
        default=None,
        help="Data-room root; when given, model-edge quotes are "
        "re-verified against the source document.",
    )
    args = ap.parse_args()

    try:
        with open(args.manifest, encoding="utf-8") as f:
            manifest = json.load(f)
        with open(args.candidates, encoding="utf-8") as f:
            candidates = json.load(f)
        meta = load_metadata(args.metadata)
        model_edges = []
        if args.model_edges:
            with open(args.model_edges, encoding="utf-8") as f:
                model_edges = json.load(f)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)

    # A byte-duplicate file yields two manifest rows sharing one id; collapse
    # to unique ids so no self edge or one-member family can form from them.
    # Per schemas.md the duplicate is a gap entry (manifest stage), not an edge.
    doc_ids = sorted({d["id"] for d in manifest["documents"]})
    paths = {d["id"]: d["path"] for d in manifest["documents"]}
    cand_pairs = sorted(
        (p["a"], p["b"]) for p in candidates.get("pairs", []) if p["a"] != p["b"]
    )
    partners = {}
    for a, b in cand_pairs:
        partners.setdefault(a, set()).add(b)
        partners.setdefault(b, set()).add(a)

    edges = {}  # (src, dst, relation) -> edge dict; rule edges enter first

    # rule edges from reference strings, within candidate pairs only
    for src in doc_ids:
        m = meta.get(src, {})
        relation = infer_relation(m.get("doc_type"))
        if relation is None:
            continue
        sparties = party_set(m)
        for ref in m.get("references") or []:
            text = (ref.get("text") or "").strip()
            if not text:
                continue
            rtoks = set(tokens(text))
            rdate = ref_date(text)
            req = ref_designator(text)
            for dst in sorted(partners.get(src, ())):
                dm = meta.get(dst, {})
                if req and not req <= set(tokens(dm.get("title"))):
                    continue
                if title_overlap(rtoks, dm.get("title")) < TITLE_OVERLAP:
                    continue
                if not date_ok(rdate, dm.get("dated")):
                    continue
                if not sparties & party_set(dm):
                    continue
                edges[(src, dst, relation)] = {
                    "src": src,
                    "dst": dst,
                    "relation": relation,
                    "provenance": "rule",
                    "evidence_source": receipt_source(ref.get("source")),
                    "quote": ref.get("quote") or text,
                }

    # near-duplicates: hashes differ (distinct ids), title and dated equal
    for a, b in cand_pairs:
        ma, mb = meta.get(a, {}), meta.get(b, {})
        ta, tb = normalize(ma.get("title") or ""), normalize(mb.get("title") or "")
        if ta and ta == tb and ma.get("dated") == mb.get("dated"):
            src, dst = max(a, b), min(a, b)
            edges[(src, dst, "duplicate-of")] = {
                "src": src,
                "dst": dst,
                "relation": "duplicate-of",
                "provenance": "rule",
                "evidence_source": (
                    "image-read-human-confirmed"
                    if "image-read-human-confirmed"
                    in {
                        scalar_source(ma, "title"),
                        scalar_source(ma, "dated"),
                        scalar_source(mb, "title"),
                        scalar_source(mb, "dated"),
                    }
                    else "model-read"
                    if "model-read"
                    in {
                        scalar_source(ma, "title"),
                        scalar_source(ma, "dated"),
                        scalar_source(mb, "title"),
                        scalar_source(mb, "dated"),
                    }
                    else "regex"
                ),
                "quote": ma.get("title") or mb.get("title"),
            }

    # model edges: already quote-verified upstream; re-verified when the
    # room root is available, and parked on any failure
    parked = 0
    text_cache = {}
    for e in model_edges:
        src, dst = e.get("src"), e.get("dst")
        relation, quote = e.get("relation"), e.get("quote")
        reason = None
        if src not in paths or dst not in paths:
            reason = "src or dst not in manifest"
        elif relation not in RELATIONS:
            reason = f"unknown relation {relation!r}"
        elif not quote:
            reason = "model edge carries no quote"
        elif args.room_root:
            endpoint_paths = {
                endpoint: os.path.join(args.room_root, paths[endpoint])
                for endpoint in (src, dst)
            }
            try:
                changed = [
                    endpoint
                    for endpoint, endpoint_path in endpoint_paths.items()
                    if hash_id(endpoint_path) != endpoint
                ]
            except OSError as exc:
                print(f"error: {exc}", file=sys.stderr)
                sys.exit(1)
            if changed:
                reason = "manifest identity changed for " + ", ".join(changed)
            doc_path = endpoint_paths[src]
            if doc_path not in text_cache:
                try:
                    text_cache[doc_path] = normalize(extract_text(doc_path))
                except OSError as exc:
                    print(f"error: {exc}", file=sys.stderr)
                    sys.exit(1)
            if reason is None and normalize(quote) not in text_cache[doc_path]:
                reason = "quote not found in source document"
        if reason:
            parked += 1
            print(
                f"parked model edge: {src} -> {dst} ({relation}): {reason}",
                file=sys.stderr,
            )
            continue
        key = (src, dst, relation)
        if key not in edges:
            edges[key] = {
                "src": src,
                "dst": dst,
                "relation": relation,
                "provenance": "model",
                "evidence_source": "model-edge",
                "quote": quote,
            }

    # union-find over accepted edges
    parent = {did: did for did in doc_ids}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[max(ra, rb)] = min(ra, rb)

    for src, dst, _ in edges:
        union(src, dst)

    if args.edge_plan_out:
        jobs = []
        for a, b in cand_pairs:
            if find(a) == find(b):
                continue
            pair = [meta.get(a, {}), meta.get(b, {})]
            metadata_raw = json.dumps(pair, sort_keys=True, separators=(",", ":"))
            job_raw = f"{a}\0{b}".encode()
            jobs.append(
                {
                    "a": a,
                    "b": b,
                    "job_id": hashlib.sha256(job_raw).hexdigest()[:16],
                    "metadata_digest": hashlib.sha256(
                        metadata_raw.encode()
                    ).hexdigest(),
                }
            )
        jobs.sort(key=lambda item: item["job_id"])
        plan_raw = json.dumps(jobs, sort_keys=True, separators=(",", ":"))
        edge_plan = {
            "jobs": jobs,
            "plan_id": hashlib.sha256(plan_raw.encode()).hexdigest()[:16],
            "version": 1,
        }
        edge_plan_path = os.path.abspath(args.edge_plan_out)
        os.makedirs(os.path.dirname(edge_plan_path), exist_ok=True)
        with open(edge_plan_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(edge_plan, sort_keys=True, indent=2) + "\n")

    components = {}
    for did in doc_ids:
        components.setdefault(find(did), []).append(did)

    def sort_key(did):
        return (meta.get(did, {}).get("dated") or FAR_FUTURE, did)

    families = []
    orphans = []
    for comp in components.values():
        if len(comp) < 2:
            orphans.extend(comp)
            continue
        preferred = [
            d
            for d in comp
            if set(tokens(meta.get(d, {}).get("doc_type"))) & BASE_DOC_TYPE_TOKENS
        ]
        base = min(preferred or comp, key=sort_key)
        rest = sorted((d for d in comp if d != base), key=sort_key)
        members = [{"id": base, "role": "base", "order": 0}]
        for i, d in enumerate(rest, 1):
            members.append(
                {
                    "id": d,
                    "order": i,
                    "role": meta.get(d, {}).get("doc_type") or "document",
                }
            )
        cset = set(comp)
        fam_edges = sorted(
            (e for k, e in edges.items() if k[0] in cset),
            key=lambda e: (e["src"], e["dst"], e["relation"]),
        )
        families.append({"family_id": base, "members": members, "edges": fam_edges})
    families.sort(key=lambda fam: fam["family_id"])
    orphans.sort()

    # referenced-absent gaps: reference strings matching no document at all
    gap_new = set()
    for src in doc_ids:
        for ref in meta.get(src, {}).get("references") or []:
            if ref.get("gap_eligible") is not True:
                continue
            text = (ref.get("text") or "").strip()
            if not text:
                continue
            rtoks = set(tokens(text))
            rdate = ref_date(text)
            req = ref_designator(text)
            matched = any(
                dst != src
                and (not req or req <= set(tokens(meta.get(dst, {}).get("title"))))
                and title_overlap(rtoks, meta.get(dst, {}).get("title"))
                >= TITLE_OVERLAP
                and date_ok(rdate, meta.get(dst, {}).get("dated"))
                for dst in doc_ids
            )
            if not matched:
                gap_new.add(
                    (
                        f"Reference '{text}' in {src} matches no document",
                        ref.get("quote") or text,
                    )
                )

    gap = {"entries": []}
    if os.path.exists(args.gap_report):
        with open(args.gap_report, encoding="utf-8") as f:
            gap = json.load(f)
    existing = gap.get("entries", [])
    added = 0
    for detail, evidence in sorted(gap_new):
        entry = {"type": "referenced-absent", "detail": detail, "evidence": evidence}
        if entry not in existing:
            existing.append(entry)
            added += 1
    # keep the canonical (type, detail, evidence) order after appending
    existing.sort(
        key=lambda e: (e.get("type", ""), e.get("detail", ""), e.get("evidence", ""))
    )
    gap["entries"] = existing
    with open(args.gap_report, "w", encoding="utf-8") as f:
        f.write(json.dumps(gap, sort_keys=True, indent=2) + "\n")

    with open(args.out, "w", encoding="utf-8") as f:
        f.write(
            json.dumps(
                {"families": families, "orphans": orphans}, sort_keys=True, indent=2
            )
            + "\n"
        )
    print(
        f"{args.out}: {len(families)} family(ies), {len(orphans)} orphan(s), "
        f"{len(edges)} edge(s) accepted, {parked} model edge(s) parked, "
        f"{added} gap entry(ies) added"
    )


if __name__ == "__main__":
    main()
