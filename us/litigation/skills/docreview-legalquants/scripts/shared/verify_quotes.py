#!/usr/bin/env python3
"""Verify metadata receipts or present-finding quotes against visible text.

Metadata mode recursively verifies every regex, legacy model, and model-read
receipt. Findings mode verifies each present text finding against its own
doc_id. Image transcriptions remain present in the human-review lane because
they cannot be verified against visible extracted text. With --write, failed
metadata is blanked before parking and a failed text finding is downgraded to
unresolved, so downstream consumers cannot use an unverified text claim merely
by ignoring its status.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys

from document_text import extract_document_text, normalize_quote
from finding_validation import dump_atomic

RECEIPT_SOURCES = {"regex", "model", "model-read"}
HUMAN_RECEIPT_SOURCES = {"image-read-human-confirmed"}


def build_id_map(root):
    ids = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort()
        for name in sorted(filenames):
            if name.startswith("."):
                continue
            path = os.path.join(dirpath, name)
            digest = hashlib.sha256()
            with open(path, "rb") as handle:
                for chunk in iter(lambda: handle.read(1 << 20), b""):
                    digest.update(chunk)
            ids.setdefault("sha256:" + digest.hexdigest()[:12], path)
    return ids


def receipt_quotes(node, out):
    if isinstance(node, dict):
        if node.get("source") in RECEIPT_SOURCES:
            out.append(node.get("quote"))
        for key in sorted(node):
            receipt_quotes(node[key], out)
    elif isinstance(node, list):
        for item in node:
            receipt_quotes(item, out)


def human_receipt_count(node):
    if isinstance(node, dict):
        return int(node.get("source") in HUMAN_RECEIPT_SOURCES) + sum(
            human_receipt_count(value) for value in node.values()
        )
    if isinstance(node, list):
        return sum(human_receipt_count(item) for item in node)
    return 0


def blank_metadata(data):
    data.update(
        {
            "dated": None,
            "doc_type": None,
            "evidence": {"dated": None, "doc_type": None, "parties": [], "title": None},
            "parties": [],
            "references": [],
            "status": "quote-unverified",
            "title": None,
        }
    )


def text_for(doc_id, id_map, cache, extractor):
    path = id_map.get(doc_id)
    if path is None:
        return None, "no document in room hashes to this id"
    if path not in cache:
        cache[path] = normalize_quote(extract_document_text(path, extractor))
    return cache[path], None


def verify_metadata(paths, id_map, extractor, write):
    cache = {}
    failed_files = 0
    for path in paths:
        try:
            with open(path, encoding="utf-8") as handle:
                data = json.load(handle)
        except (OSError, json.JSONDecodeError) as error:
            raise OSError(f"cannot read {path}: {error}") from error
        quotes = []
        receipt_quotes(data, quotes)
        human_receipts = human_receipt_count(data)
        text, text_error = text_for(data.get("id"), id_map, cache, extractor)
        failures = []
        for quote in quotes:
            if text_error:
                failures.append((quote, text_error))
            elif not isinstance(quote, str) or not quote.strip():
                failures.append((quote, "receipt has no quote"))
            elif normalize_quote(quote) not in text:
                failures.append((quote, "quote not found in visible document text"))
        if failures:
            failed_files += 1
            print(f"{path}: quote-unverified ({len(failures)} failing)")
            for quote, reason in failures:
                print(f"{path}: {reason}: {quote!r}", file=sys.stderr)
            if write:
                blank_metadata(data)
                dump_atomic(path, data)
        else:
            suffix = (
                f", {human_receipts} lawyer-confirmed image transcription(s) "
                "not script-verified"
                if human_receipts
                else ""
            )
            print(f"{path}: ok ({len(quotes)} receipt quote(s){suffix})")
    return failed_files


def downgrade_finding(finding, reason):
    finding["status"] = "unresolved"
    finding["section"] = None
    finding["quote"] = None
    finding["characterization"] = "Quote verification failed; human review required."
    finding["band"] = None
    finding["band_basis"] = None
    finding["current_position"] = False
    finding["quote_verification"] = {
        "checker": "deterministic-visible-text",
        "reason": reason,
        "status": "failed",
    }


def verify_findings(path, id_map, extractor, write):
    try:
        with open(path, encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError) as error:
        raise OSError(f"cannot read {path}: {error}") from error
    findings = data.get("findings")
    if not isinstance(findings, list):
        raise OSError(f"findings file has no findings array: {path}")
    cache = {}
    checked = failed = 0
    for finding in findings:
        if finding.get("status") != "present":
            continue
        checked += 1
        if finding.get("receipt_mode") == "image-transcription":
            reason = "image transcription is not script-verifiable"
            print(
                f"{finding.get('finding_id', '<no id>')}: {reason}; human review required"
            )
            continue
        text, text_error = text_for(finding.get("doc_id"), id_map, cache, extractor)
        quote = finding.get("quote")
        reason = text_error
        if reason is None and (not isinstance(quote, str) or not quote.strip()):
            reason = "present finding has no quote"
        if reason is None and normalize_quote(quote) not in text:
            reason = "quote not found in visible document text"
        if reason:
            failed += 1
            print(f"{finding.get('finding_id', '<no id>')}: {reason}", file=sys.stderr)
            if write:
                downgrade_finding(finding, reason)
        else:
            finding["quote_verification"] = {
                "checker": "deterministic-visible-text",
                "reason": None,
                "status": "confirmed",
            }
    if write:
        dump_atomic(path, data)
    print(f"{checked} present finding(s) checked, {failed} failed")
    return failed


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    inputs = parser.add_mutually_exclusive_group(required=True)
    inputs.add_argument("--metadata", help="Metadata JSON file or directory.")
    inputs.add_argument("--findings", help="findings.json file.")
    parser.add_argument("--room-root", required=True)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--extractor", choices=["auto", "stdlib"], default="auto")
    args = parser.parse_args()
    if not os.path.isdir(args.room_root):
        sys.exit(f"error: no such room root: {args.room_root}")
    try:
        id_map = build_id_map(args.room_root)
        if args.metadata:
            if os.path.isdir(args.metadata):
                paths = sorted(
                    os.path.join(args.metadata, name)
                    for name in os.listdir(args.metadata)
                    if name.endswith(".json")
                )
            elif os.path.isfile(args.metadata):
                paths = [args.metadata]
            else:
                sys.exit(f"error: no such metadata path: {args.metadata}")
            failed = verify_metadata(paths, id_map, args.extractor, args.write)
            mode = "applied" if args.write else "dry-run"
            print(f"{len(paths)} metadata file(s) checked, {failed} failed ({mode})")
        else:
            verify_findings(args.findings, id_map, args.extractor, args.write)
    except OSError as error:
        sys.exit(f"error: {error}")


if __name__ == "__main__":
    main()
