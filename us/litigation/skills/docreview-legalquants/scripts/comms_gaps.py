#!/usr/bin/env python3
"""Detect Stage 2 disputes gaps from message and cluster data.

Emits entries in the diligence gap-report.json shape ({"entries": [...]}).
Two gap types, "custodian-gap" and "thread-gap", extend the shared diligence
gap-report enum for comms corpora.

Detectors, all deterministic:

  custodian-gap  (1) a custodian's calendar month with zero messages where
                 both neighboring months have >= 5;
                 (2) with --index: a custodian present in the represented
                 collection index (production load file / ESI custodian
                 list) with zero produced messages. Whole-custodian absence
                 is undetectable from the production alone; it needs the
                 represented index.
  thread-gap     (1) a thread whose in-reply-to/references cite a
                 message-id absent from the corpus;
                 (2) archive copy quorum: within a thread, a message
                 lacking a copy in an archive folder where every other
                 message of the thread (same custodian) has one. Archive
                 folders are identified from the data: top-level folders
                 holding copies of >= 25% of the custodian's distinct
                 messages.

Usage:
    python3 comms_gaps.py --messages messages.json --clusters clusters.json \\
        --gap-report gap-report.json [--index represented-index.json]
"""

import argparse
import json
import os

from cluster_comms import normalize_messages

MONTH_NEIGHBOR_MIN = 5
ARCHIVE_COVERAGE = 0.25


def month_add(month, delta):
    y, m = int(month[:4]), int(month[5:7])
    m += delta
    y += (m - 1) // 12
    m = (m - 1) % 12 + 1
    return f"{y:04d}-{m:02d}"


def custodian_month_gaps(rollup):
    entries = []
    for cust in sorted(rollup):
        months = {k: v for k, v in rollup[cust].items() if k != "undated"}
        if len(months) < 3:
            continue
        lo, hi = min(months), max(months)
        cur = month_add(lo, 1)
        while cur < hi:
            prev_n = months.get(month_add(cur, -1), 0)
            next_n = months.get(month_add(cur, 1), 0)
            if (
                months.get(cur, 0) == 0
                and prev_n >= MONTH_NEIGHBOR_MIN
                and next_n >= MONTH_NEIGHBOR_MIN
            ):
                entries.append(
                    {
                        "type": "custodian-gap",
                        "detail": (
                            f"custodian {cust} has zero messages in {cur}; "
                            f"{month_add(cur, -1)} has {prev_n} and "
                            f"{month_add(cur, 1)} has {next_n}"
                        ),
                        "evidence": "custodian-month rollup",
                    }
                )
            cur = month_add(cur, 1)
    return entries


def absent_custodian_gaps(rollup, index_path):
    with open(index_path, encoding="utf-8") as f:
        index = json.load(f)
    expected = {}
    for rec in index.get("messages", []):
        cust = rec.get("custodian")
        if cust:
            expected[cust] = expected.get(cust, 0) + 1
    entries = []
    for cust in sorted(expected):
        if cust not in rollup:
            entries.append(
                {
                    "type": "custodian-gap",
                    "detail": (
                        f"custodian {cust} appears in the represented "
                        f"collection index with {expected[cust]} messages "
                        f"but zero were produced"
                    ),
                    "evidence": "index reconciliation",
                }
            )
    return entries


def thread_subject(thread, messages):
    subjects = thread["basis"]["normalized_subjects"]
    return subjects[0] if subjects else "(no subject)"


def referenced_absent_gaps(threads, messages):
    known_mids = {m["message_id"] for m in messages.values() if m["message_id"]}
    entries = []
    for thread in threads:
        subj = thread_subject(thread, messages)
        missing = set()
        for did in thread["members"]:
            m = messages[did]
            for mid in m["in_reply_to"] + m["references"]:
                if mid not in known_mids:
                    missing.add(mid)
        for mid in sorted(missing):
            entries.append(
                {
                    "type": "thread-gap",
                    "detail": (
                        f"thread '{subj}' cites message-id {mid} absent from the corpus"
                    ),
                    "evidence": f"reference chain in {thread['cluster_id']}",
                }
            )
    return entries


def archive_folders(messages):
    """Per custodian: top-level folders holding >= 25% of distinct messages."""
    groups = {}
    for _did, m in sorted(messages.items()):
        if not m.get("body_fp"):
            continue
        top = m["folder"].split("/")[0] if m["folder"] else ""
        key = (m["from"], m["date"], m["body_fp"])
        groups.setdefault(m["custodian"], {}).setdefault(key, set()).add(top)
    archive = {}
    for cust, g in groups.items():
        cov = {}
        for folders in g.values():
            for f in folders:
                cov[f] = cov.get(f, 0) + 1
        archive[cust] = {
            f for f, c in cov.items() if f and c / len(g) >= ARCHIVE_COVERAGE
        }
    return archive


def copy_quorum_gaps(threads, messages):
    archive = archive_folders(messages)
    entries = []
    for thread in threads:
        subj = thread_subject(thread, messages)
        by_cust = {}
        for did in thread["members"]:
            m = messages[did]
            by_cust.setdefault(m["custodian"], []).append(did)
        for cust in sorted(by_cust, key=lambda c: c or ""):
            arch = archive.get(cust, set())
            if not arch:
                continue
            content = {}
            for did in by_cust[cust]:
                m = messages[did]
                if not m.get("body_fp"):
                    continue
                top = m["folder"].split("/")[0] if m["folder"] else ""
                key = (m["from"] or "", m["date"] or "", m["body_fp"])
                content.setdefault(key, set()).add(top)
            if len(content) < 2:
                continue
            flagged = []
            for key in sorted(content):
                others = [f for k, f in content.items() if k != key]
                quorum = set.intersection(*others) & arch
                missing = sorted(quorum - content[key])
                for folder in missing:
                    flagged.append(
                        f"message dated {key[1] or 'undated'} from "
                        f"{key[0] or 'unknown'} lacks the {folder} copy held "
                        f"by every other message in the thread"
                    )
            if flagged:
                entries.append(
                    {
                        "type": "thread-gap",
                        "detail": (f"thread '{subj}' in {cust}: " + "; ".join(flagged)),
                        "evidence": f"archive copy quorum in {thread['cluster_id']}",
                    }
                )
    return entries


def message_level_scope_gap(messages, non_messages):
    """Expose productions that contain artifacts but no parseable messages."""
    if messages or not non_messages:
        return []
    count = len(non_messages)
    return [
        {
            "type": "thread-gap",
            "detail": (
                f"production contains {count} non-message artifact"
                f"{'s' if count != 1 else ''} and zero parseable native messages; "
                "custodian and thread gap detection has no message-level data"
            ),
            "evidence": "message parser scope",
        }
    ]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--messages", required=True, help="messages.json input.")
    ap.add_argument("--clusters", required=True, help="clusters.json input.")
    ap.add_argument(
        "--gap-report", required=True, help="Shared gap-report.json to merge in place."
    )
    ap.add_argument(
        "--index",
        default=None,
        help="Optional represented collection index (load file "
        "or bench index.json); enables whole-custodian "
        "absence detection.",
    )
    args = ap.parse_args()

    with open(args.messages, encoding="utf-8") as f:
        message_data = json.load(f)
    messages = normalize_messages(message_data["messages"])
    non_messages = message_data.get("non_messages", [])
    with open(args.clusters, encoding="utf-8") as f:
        clusters = json.load(f)

    entries = []
    entries += message_level_scope_gap(messages, non_messages)
    entries += custodian_month_gaps(clusters["custodian_months"])
    if args.index:
        entries += absent_custodian_gaps(clusters["custodian_months"], args.index)
    entries += referenced_absent_gaps(clusters["threads"], messages)
    entries += copy_quorum_gaps(clusters["threads"], messages)

    existing = []
    if os.path.exists(args.gap_report):
        with open(args.gap_report, encoding="utf-8") as f:
            existing = json.load(f).get("entries", [])
    merged = existing + entries
    deduped = {
        (
            entry.get("type", ""),
            entry.get("detail", ""),
            entry.get("evidence", ""),
        ): entry
        for entry in merged
    }
    entries = [deduped[key] for key in sorted(deduped)]
    with open(args.gap_report, "w", encoding="utf-8") as f:
        f.write(json.dumps({"entries": entries}, indent=2, sort_keys=True) + "\n")
    by_type = {}
    for e in entries:
        by_type[e["type"]] = by_type.get(e["type"], 0) + 1
    summary = ", ".join(f"{n} {t}" for t, n in sorted(by_type.items()))
    print(f"Wrote {args.gap_report}: {summary or '0 entries'}")


if __name__ == "__main__":
    main()
