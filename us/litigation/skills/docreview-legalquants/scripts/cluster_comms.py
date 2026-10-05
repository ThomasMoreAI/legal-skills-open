#!/usr/bin/env python3
"""Build the Stage 2 disputes relationship layer from messages into clusters.

Replaces the diligence block_candidates/build_families pair for comms
corpora. Three deterministic groupings, each with provenance:

  threads    normalized-subject (re:/fw:/fwd: prefixes stripped, whitespace
             collapsed, casefolded) unioned with in-reply-to/references
             chains, via union-find; clusters of >= 2 members are emitted
  channels   recurring participant sets (normalized addresses, sorted);
             a channel is a participant set seen >= 3 times
  custodian_months  per custodian, message counts by sender-local month;
             the gap report's raw material

Every cluster: stable id (sha256-12 of its sorted member ids), member ids
sorted, basis. Deterministic: sorted keys, sorted collections, no
timestamps, no absolute paths.

Usage:
    python3 cluster_comms.py --messages messages.json --out clusters.json
"""

import argparse
import hashlib
import json
import re
from typing import Any

RE_PREFIX = re.compile(r"^\s*(re|fw|fwd)\s*:\s*", re.IGNORECASE)
CHANNEL_MIN = 3


def string_list(value):
    if value is None:
        return []
    if isinstance(value, str):
        return [value] if value else []
    if isinstance(value, list):
        return [item for item in value if isinstance(item, str) and item]
    return []


def normalize_messages(messages):
    """Normalize documented/legacy records to the canonical parser contract."""
    normalized = {}
    for doc_id in sorted(messages):
        raw = messages[doc_id] if isinstance(messages[doc_id], dict) else {}
        date = raw.get("date") if isinstance(raw.get("date"), str) else None
        normalized[doc_id] = {
            "body_fp": raw.get("body_fp")
            if isinstance(raw.get("body_fp"), str)
            else None,
            "cc": string_list(raw.get("cc")),
            "custodian": raw.get("custodian")
            if isinstance(raw.get("custodian"), str)
            else None,
            "date": date,
            "date_local": (
                raw.get("date_local")
                if isinstance(raw.get("date_local"), str)
                else date
            ),
            "duplicate_paths": string_list(raw.get("duplicate_paths")),
            "folder": raw.get("folder") if isinstance(raw.get("folder"), str) else "",
            "from": raw.get("from") if isinstance(raw.get("from"), str) else None,
            "has_attachments": bool(raw.get("has_attachments")),
            "in_reply_to": string_list(raw.get("in_reply_to")),
            "message_id": raw.get("message_id")
            if isinstance(raw.get("message_id"), str)
            else None,
            "path": raw.get("path") if isinstance(raw.get("path"), str) else "",
            "references": string_list(raw.get("references")),
            "subject": raw.get("subject")
            if isinstance(raw.get("subject"), str)
            else "",
            "to": string_list(raw.get("to")),
        }
    return normalized


def norm_subject(s):
    s = s or ""
    prev = None
    while prev != s:
        prev = s
        s = RE_PREFIX.sub("", s)
    return " ".join(s.casefold().split())


def sha12(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        self.parent.setdefault(x, x)
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            # deterministic root choice
            lo, hi = sorted((ra, rb))
            self.parent[hi] = lo


def build_threads(messages):
    uf = UnionFind()
    by_subject = {}
    by_mid = {}
    for did in sorted(messages):
        uf.find(did)
        m = messages[did]
        subj = norm_subject(m["subject"])
        if subj:
            by_subject.setdefault(subj, []).append(did)
        if m["message_id"]:
            by_mid.setdefault(m["message_id"], []).append(did)
    for subj in sorted(by_subject):
        docs = by_subject[subj]
        for other in docs[1:]:
            uf.union(docs[0], other)
    ref_links = {}
    for did in sorted(messages):
        m = messages[did]
        for mid in sorted(set(m["in_reply_to"] + m["references"])):
            for target in by_mid.get(mid, []):
                if target != did:
                    uf.union(did, target)
                    ref_links[uf.find(did)] = ref_links.get(uf.find(did), 0) + 1
    groups = {}
    for did in sorted(messages):
        groups.setdefault(uf.find(did), []).append(did)
    threads: list[dict[str, Any]] = []
    for root in sorted(groups):
        members = sorted(groups[root])
        if len(members) < 2:
            continue
        subjects = sorted(
            {norm_subject(messages[d]["subject"]) for d in members} - {""}
        )
        threads.append(
            {
                "cluster_id": "t" + sha12("|".join(members)),
                "members": members,
                "basis": {
                    "kind": "thread",
                    "normalized_subjects": subjects,
                    "reference_links": ref_links.get(root, 0),
                },
            }
        )
    threads.sort(key=lambda t: t["cluster_id"])
    return threads


def build_channels(messages):
    by_set = {}
    for did in sorted(messages):
        m = messages[did]
        parts = set(m["to"]) | set(m["cc"])
        if m["from"]:
            parts.add(m["from"])
        if not parts:
            continue
        key = tuple(sorted(parts))
        by_set.setdefault(key, []).append(did)
    channels: list[dict[str, Any]] = []
    for key in sorted(by_set):
        members = sorted(by_set[key])
        if len(members) < CHANNEL_MIN:
            continue
        channels.append(
            {
                "cluster_id": "c" + sha12("|".join(members)),
                "members": members,
                "basis": {
                    "kind": "participant-set",
                    "participants": list(key),
                    "occurrences": len(members),
                },
            }
        )
    channels.sort(key=lambda c: c["cluster_id"])
    return channels


def build_custodian_months(messages):
    # local calendar month: collections are cut in sender-local time
    rollup = {}
    for did in sorted(messages):
        m = messages[did]
        cust = m["custodian"] or "(root)"
        month = m["date_local"][:7] if m.get("date_local") else "undated"
        rollup.setdefault(cust, {}).setdefault(month, 0)
        rollup[cust][month] += 1
    return rollup


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--messages", required=True, help="messages.json input.")
    ap.add_argument("--out", required=True, help="Path for clusters.json.")
    args = ap.parse_args()

    with open(args.messages, encoding="utf-8") as f:
        messages = normalize_messages(json.load(f)["messages"])

    clusters = {
        "threads": build_threads(messages),
        "channels": build_channels(messages),
        "custodian_months": build_custodian_months(messages),
    }
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(json.dumps(clusters, indent=2, sort_keys=True) + "\n")
    print(
        f"Wrote {args.out}: {len(clusters['threads'])} threads, "
        f"{len(clusters['channels'])} channels, "
        f"{len(clusters['custodian_months'])} custodians"
    )


if __name__ == "__main__":
    main()
