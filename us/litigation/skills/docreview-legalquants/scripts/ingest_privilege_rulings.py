#!/usr/bin/env python3
"""Validate lawyer privilege rulings and write a new ruled queue copy."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from copy import deepcopy
from pathlib import Path


class RulingError(ValueError):
    pass


def load(path: str, kind: str) -> dict:
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise RulingError(f"cannot read {kind}: {error}") from error
    if not isinstance(value, dict):
        raise RulingError(f"{kind} must be a JSON object")
    return value


def digest(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def validate(receipt: dict, queue: dict, manifest: dict) -> dict[str, dict]:
    expected_keys = {
        "artifact",
        "candidate_doc_ids",
        "manifest_digest",
        "queue_digest",
        "ruled_by",
        "ruling_source",
        "rulings",
        "version",
    }
    if set(receipt) != expected_keys:
        raise RulingError("rulings receipt has unexpected or missing fields")
    if receipt["artifact"] != "privilege-rulings" or receipt["version"] != 1:
        raise RulingError("unsupported rulings artifact or version")
    if receipt["ruling_source"] not in {"offline-export", "conversation"}:
        raise RulingError("unsupported ruling source")
    if receipt["ruled_by"] != "lawyer":
        raise RulingError("privilege rulings must be made by the lawyer")
    if receipt["queue_digest"] != digest(queue):
        raise RulingError("queue digest mismatch")
    if receipt["manifest_digest"] != digest(manifest):
        raise RulingError("manifest digest mismatch")
    candidates = queue.get("candidates")
    ruled = queue.get("ruled")
    if not isinstance(candidates, list) or not isinstance(ruled, list):
        raise RulingError("queue candidates and ruled must be arrays")
    expected_ids = sorted(item.get("doc_id") for item in candidates)
    if not expected_ids or any(not isinstance(item, str) for item in expected_ids):
        raise RulingError("queue has no valid pending candidates")
    if receipt["candidate_doc_ids"] != expected_ids:
        raise RulingError("candidate scope drift")
    documents = {item.get("id") for item in manifest.get("documents", [])}
    if any(doc_id not in documents for doc_id in expected_ids):
        raise RulingError("candidate is absent from the manifest")
    rows = receipt.get("rulings")
    if not isinstance(rows, list) or len(rows) != len(expected_ids):
        raise RulingError("rulings must cover every candidate exactly once")
    by_id = {}
    for row in rows:
        if not isinstance(row, dict) or set(row) != {"doc_id", "note", "ruling"}:
            raise RulingError("a ruling has unexpected or missing fields")
        doc_id = row.get("doc_id")
        if doc_id in by_id:
            raise RulingError(f"duplicate ruling for {doc_id}")
        if row.get("ruling") not in {"privileged", "not-privileged", "needs-review"}:
            raise RulingError(f"invalid privilege ruling for {doc_id}")
        if not isinstance(row.get("note"), str):
            raise RulingError(f"ruling note for {doc_id} must be text")
        by_id[doc_id] = row
    if sorted(by_id) != expected_ids:
        raise RulingError("rulings do not match the candidate scope")
    return by_id


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rulings", required=True)
    parser.add_argument("--queue", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    try:
        paths = [
            Path(value).resolve()
            for value in (args.rulings, args.queue, args.manifest, args.out)
        ]
        if len(set(paths)) != len(paths):
            raise RulingError("output must be a distinct new artifact path")
        receipt = load(args.rulings, "rulings")
        queue = load(args.queue, "queue")
        manifest = load(args.manifest, "manifest")
        by_id = validate(receipt, queue, manifest)
    except RulingError as error:
        print(f"ingest_privilege_rulings: {error}", file=sys.stderr)
        raise SystemExit(1) from error

    additions = []
    for candidate in sorted(queue["candidates"], key=lambda item: item["doc_id"]):
        decision = by_id[candidate["doc_id"]]
        item = deepcopy(candidate)
        item.update(
            {
                "by": "lawyer",
                "lawyer_note": decision["note"],
                "ruling": decision["ruling"],
            }
        )
        additions.append(item)
    output = {
        "candidates": [],
        "ruled": sorted(
            deepcopy(queue["ruled"]) + additions,
            key=lambda item: item.get("doc_id", ""),
        ),
    }
    destination = Path(args.out)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"recorded {len(additions)} lawyer privilege ruling(s)")


if __name__ == "__main__":
    main()
