#!/usr/bin/env python3
"""Form candidate blocks for /diligence relationship resolution.

Reads manifest.json plus the metadata dir, normalizes party names (casefold,
strip punctuation and entity suffixes), and groups documents linked by any of:
shared normalized party, shared title token trigram, shared filename or
index-number prefix, or an explicit cross-reference (a reference string
matching another document's title tokens within tolerance). Emits
candidates.json: blocks with basis labels and candidate pairs within blocks
only. Block ids b001, b002... are ordered by sorted member ids.

Usage:
    python3 block_candidates.py --manifest manifest.json \
        --metadata metadata/ --out candidates.json
"""

import argparse
import itertools
import json
import os
import re
import sys

ENTITY_SUFFIXES = {"inc", "llc", "ltd", "corp", "co", "lp", "llp", "plc", "gmbh", "pty"}
XREF_TITLE_OVERLAP = 0.6


def tokens(s):
    return re.sub(r"[^\w\s]+", " ", (s or "").casefold()).split()


def norm_party(name):
    toks = tokens(name)
    while toks and toks[-1] in ENTITY_SUFFIXES:
        toks.pop()
    return " ".join(toks)


def index_prefix(path):
    parts = path.split("/")
    stem = re.sub(r"\.[^.]+$", "", parts[-1])
    m = re.match(r"(\d+(?:\.\d+)+)", stem)
    if m:
        return ".".join(m.group(1).split(".")[:-1])
    for part in reversed(parts[:-1]):
        m = re.match(r"(\d+(?:\.\d+)+)", part)
        if m:
            return m.group(1)
    return None


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
        description="Form candidate blocks from manifest plus metadata."
    )
    ap.add_argument("--manifest", required=True, help="Path to manifest.json.")
    ap.add_argument("--metadata", required=True, help="Metadata directory.")
    ap.add_argument("--out", required=True, help="candidates.json output path.")
    args = ap.parse_args()

    try:
        with open(args.manifest, encoding="utf-8") as f:
            manifest = json.load(f)
        meta = load_metadata(args.metadata)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)

    deferred = sum(
        1 for record in meta.values() if record.get("status") == "deferred-to-review"
    )
    if deferred:
        noun = "document" if deferred == 1 else "documents"
        print(
            f"metadata was deferred for {deferred} {noun}; family assembly "
            "requires canonical metadata; rerun the read plan without deferral "
            "for these IDs",
            file=sys.stderr,
        )
        sys.exit(1)

    # A byte-duplicate file yields two manifest rows sharing one id;
    # collapse to unique ids so no self pair (a == b) can ever form.
    doc_ids = sorted({d["id"] for d in manifest["documents"]})
    paths = {d["id"]: d["path"] for d in manifest["documents"]}

    groups = {}  # label -> set of doc ids sharing that feature

    def add(label, doc_id):
        groups.setdefault(label, set()).add(doc_id)

    for did in doc_ids:
        m = meta.get(did, {})
        path = paths[did]
        for p in m.get("parties") or []:
            np = norm_party(p)
            if np:
                add("party:" + np, did)
        ttoks = tokens(m.get("title"))
        for i in range(len(ttoks) - 2):
            add("title:" + " ".join(ttoks[i : i + 3]), did)
        ipfx = index_prefix(path)
        if ipfx:
            add("index:" + ipfx, did)
        stoks = tokens(re.sub(r"\.[^.]+$", "", path.rsplit("/", 1)[-1]))
        while stoks and stoks[0].isdigit():
            stoks.pop(0)
        if len(stoks) >= 2:
            add("file:" + " ".join(stoks[:2]), did)

    # explicit cross-references: reference text vs other documents' titles
    xrefs = []
    for src in doc_ids:
        for ref in meta.get(src, {}).get("references") or []:
            rtoks = set(tokens(ref.get("text")))
            if not rtoks:
                continue
            for dst in doc_ids:
                if dst == src:
                    continue
                ttoks = set(tokens(meta.get(dst, {}).get("title")))
                if not ttoks:
                    continue
                if len(ttoks & rtoks) / len(ttoks) >= XREF_TITLE_OVERLAP:
                    xrefs.append((src, dst))

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

    for members in groups.values():
        ms = sorted(members)
        for other in ms[1:]:
            union(ms[0], other)
    for src, dst in xrefs:
        union(src, dst)

    components = {}
    for did in doc_ids:
        components.setdefault(find(did), []).append(did)
    member_lists = sorted(sorted(ms) for ms in components.values() if len(ms) >= 2)

    blocks = []
    pairs = []
    for n, members in enumerate(member_lists, 1):
        block_id = f"b{n:03d}"
        mset = set(members)
        basis = sorted(
            {label for label, g in groups.items() if len(g & mset) >= 2}
            | {f"xref:{s}->{d}" for s, d in xrefs if s in mset and d in mset}
        )
        blocks.append({"block_id": block_id, "basis": basis, "members": members})
        for a, b in itertools.combinations(members, 2):
            pairs.append({"a": a, "b": b, "block": block_id})

    out = {"blocks": blocks, "pairs": pairs}
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(json.dumps(out, sort_keys=True, indent=2) + "\n")
    print(
        f"{args.out}: {len(blocks)} block(s), {len(pairs)} pair(s) "
        f"over {len(doc_ids)} document(s)"
    )


if __name__ == "__main__":
    main()
