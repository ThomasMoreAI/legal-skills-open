#!/usr/bin/env python3
"""Validate fresh reader results and produce canonical metadata records.

This script is the deterministic receive side of the agentic reading loop.
The host orchestrator writes one schema-conforming JSON result per planned ID
to --reader-results. This merger verifies identity, shape, dates, evidence
alignment, and quotes before any claim reaches metadata/. Regex-banked records
are independently revalidated, and audit reads replace their regex record.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any

from document_text import extract_document_text, normalize_quote

DOC_TYPES = {
    "agreement",
    "amendment",
    "sow",
    "schedule",
    "exhibit",
    "guaranty",
    "other",
}
REF_KINDS = {
    "parent-agreement",
    "amendment",
    "sow",
    "schedule",
    "exhibit",
    "guaranty",
    "other",
}
READABILITY = {"native", "scanned", "suspect", "encrypted", "corrupt"}
DISPOSITIONS = {
    "deferred-to-review",
    "parked-unreadable",
    "reader-required",
    "regex-audit",
    "regex-banked",
}
READER_KEYS = {
    "doc_id",
    "receipt_mode",
    "doc_type",
    "title",
    "parties",
    "dated",
    "references",
    "evidence",
}
EVIDENCE_KEYS = {"doc_type", "title", "dated", "parties"}


def load(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def dump_atomic(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(value, handle, indent=2, sort_keys=True)
            handle.write("\n")
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except OSError:
            pass
        raise


def blank_record(doc_id, status):
    return {
        "dated": None,
        "doc_type": None,
        "evidence": {"dated": None, "doc_type": None, "parties": [], "title": None},
        "id": doc_id,
        "parties": [],
        "references": [],
        "status": status,
        "title": None,
    }


def valid_iso_date(value):
    if value is None:
        return True
    if not isinstance(value, str):
        return False
    try:
        return dt.date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def hash_id(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()[:12]


def quote_present(quote, text):
    return (
        isinstance(quote, str)
        and bool(quote.strip())
        and normalize_quote(quote) in text
    )


def validate_reader(result, expected_id, source_text, read_mode, page_count):
    errors = []
    if not isinstance(result, dict) or set(result) != READER_KEYS:
        return ["reader result has unexpected or missing top-level keys"]
    if result.get("doc_id") != expected_id:
        errors.append(f"doc_id must equal {expected_id}")
    expected_receipt_mode = "image-transcription" if read_mode == "image" else "text"
    if result.get("receipt_mode") != expected_receipt_mode:
        errors.append(f"receipt_mode must be {expected_receipt_mode}")
    doc_type = result.get("doc_type")
    if doc_type not in DOC_TYPES:
        errors.append("doc_type is not canonical")
    title = result.get("title")
    if title is not None and (not isinstance(title, str) or not title.strip()):
        errors.append("title must be a non-empty string or null")
    parties = result.get("parties")
    if not isinstance(parties, list) or any(
        not isinstance(item, str) or not item.strip() for item in parties
    ):
        errors.append("parties must be an array of non-empty strings")
        parties = []
    if len(parties) != len(set(parties)):
        errors.append("parties must not repeat values")
    if not valid_iso_date(result.get("dated")):
        errors.append("dated must be a real ISO date or null")
    evidence = result.get("evidence")
    if not isinstance(evidence, dict) or set(evidence) != EVIDENCE_KEYS:
        errors.append("evidence has unexpected or missing keys")
        evidence = {}

    def receipt(item, label):
        if not isinstance(item, dict) or set(item) != {"quote", "page"}:
            errors.append(f"{label} must contain only quote and page")
            return
        quote = item.get("quote")
        page = item.get("page")
        if read_mode == "text":
            if page is not None:
                errors.append(f"{label}.page must be null for text receipts")
            if not quote_present(quote, source_text):
                errors.append(f"{label} quote was not found")
        else:
            if not isinstance(quote, str) or not quote.strip():
                errors.append(f"{label} transcription is empty")
            if not isinstance(page, int) or page < 1:
                errors.append(f"{label}.page must be a positive integer")
            elif isinstance(page_count, int) and page > page_count:
                errors.append(f"{label}.page exceeds the manifest page count")

    def scalar(field, required):
        item = evidence.get(field)
        if not required:
            if item is not None:
                errors.append(
                    f"evidence.{field} must be null when the claim is null or other"
                )
            return
        receipt(item, f"evidence.{field}")

    scalar("doc_type", doc_type in DOC_TYPES - {"other"})
    scalar("title", isinstance(title, str))
    scalar("dated", isinstance(result.get("dated"), str))
    party_evidence = evidence.get("parties")
    if not isinstance(party_evidence, list):
        errors.append("evidence.parties must be an array")
    else:
        values = []
        for index, item in enumerate(party_evidence):
            if not isinstance(item, dict) or set(item) != {"value", "quote", "page"}:
                errors.append(
                    f"evidence.parties[{index}] must contain value, quote, and page"
                )
                continue
            values.append(item.get("value"))
            receipt(
                {"quote": item.get("quote"), "page": item.get("page")},
                f"evidence.parties[{index}]",
            )
        if values != parties:
            errors.append("evidence.parties values must match parties in order")

    references = result.get("references")
    if not isinstance(references, list):
        errors.append("references must be an array")
    else:
        for index, reference in enumerate(references):
            if not isinstance(reference, dict) or set(reference) != {
                "kind",
                "text",
                "quote",
                "page",
                "gap_eligible",
            }:
                errors.append(f"references[{index}] has unexpected or missing keys")
                continue
            if reference.get("kind") not in REF_KINDS:
                errors.append(f"references[{index}].kind is not canonical")
            if (
                not isinstance(reference.get("text"), str)
                or not reference["text"].strip()
            ):
                errors.append(f"references[{index}].text must be non-empty")
            if not isinstance(reference.get("gap_eligible"), bool):
                errors.append(f"references[{index}].gap_eligible must be boolean")
            receipt(
                {"quote": reference.get("quote"), "page": reference.get("page")},
                f"references[{index}]",
            )
    return errors


def compile_reader(result, doc_id, source):
    evidence = result["evidence"]

    def sourced(item):
        return None if item is None else {**item, "source": source}

    status = (
        "complete"
        if result["doc_type"] != "other" and result["title"] and result["dated"]
        else "metadata-incomplete"
    )
    return {
        "dated": result["dated"],
        "doc_type": result["doc_type"],
        "evidence": {
            "dated": sourced(evidence["dated"]),
            "doc_type": sourced(evidence["doc_type"]),
            "parties": [sourced(item) for item in evidence["parties"]],
            "title": sourced(evidence["title"]),
        },
        "id": doc_id,
        "parties": result["parties"],
        "references": [
            {**reference, "source": source} for reference in result["references"]
        ],
        "status": status,
        "title": result["title"],
    }


def regex_quotes(record):
    claims = []
    for field in ("dated", "doc_type", "title"):
        item = record.get("evidence", {}).get(field)
        if item:
            claims.append(item.get("quote"))
    for item in record.get("evidence", {}).get("parties", []):
        claims.append(item.get("quote"))
    for item in record.get("references", []):
        claims.append(item.get("quote"))
    return claims


def compile_banked(record, doc_id, source_text):
    errors = []
    if record.get("id") != doc_id or record.get("status") != "regex-banked":
        errors.append("regex record is not bankable")
    if record.get("doc_type") not in DOC_TYPES - {"other"}:
        errors.append("regex document type is not canonical")
    for quote in regex_quotes(record):
        if not quote_present(quote, source_text):
            errors.append("regex receipt was not found")
    if not record.get("doc_type") or not record.get("title") or not record.get("dated"):
        errors.append("regex identity fields are incomplete")
    elif not valid_iso_date(record.get("dated")):
        errors.append("regex date is not a real ISO date")
    if errors:
        return blank_record(doc_id, "quote-unverified"), errors
    compiled = dict(record)
    compiled["status"] = "complete"
    return compiled, []


def compare_audit(regex_record, reader_record):
    def comparable(field, value):
        if field != "references" or not isinstance(value, list):
            return value
        return [
            {key: item.get(key) for key in ("kind", "text", "quote", "gap_eligible")}
            for item in value
            if isinstance(item, dict)
        ]

    fields = {}
    for field in ("doc_type", "title", "parties", "dated", "references"):
        left = comparable(field, regex_record.get(field))
        right = comparable(field, reader_record.get(field))
        fields[field] = "agree" if left == right else "disagree"
    return fields


def validate_plan(manifest, plan):
    errors = []
    if plan.get("version") != 1:
        errors.append("read plan version is unsupported")
    payload = {key: value for key, value in plan.items() if key != "plan_id"}
    expected_plan_id = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()[:16]
    if plan.get("plan_id") != expected_plan_id:
        errors.append("read plan ID does not match its payload")
    deferral_policy = plan.get("deferral_policy")
    if "deferral_policy" in plan and deferral_policy != "defer-non-unit-metadata":
        errors.append("read plan deferral_policy is unsupported")
    manifest_paths = {}
    manifest_documents = {}
    for document in manifest.get("documents", []):
        doc_id = document.get("id")
        path = document.get("path")
        if not isinstance(doc_id, str) or not isinstance(path, str):
            errors.append("manifest document is missing string id/path")
            continue
        manifest_paths.setdefault(doc_id, set()).add(path)
        manifest_documents.setdefault(doc_id, []).append(document)
    rows = plan.get("documents")
    if not isinstance(rows, list):
        return None, manifest_paths, ["read plan has no documents array"]
    scope = plan.get("scope")
    if scope is None:
        expected_ids = set(manifest_paths)
    elif (
        isinstance(scope, dict)
        and scope.get("kind") in {"manifest", "include-ids"}
        and isinstance(scope.get("ids"), list)
        and all(isinstance(doc_id, str) for doc_id in scope["ids"])
        and len(scope["ids"]) == len(set(scope["ids"]))
    ):
        expected_ids = set(scope["ids"])
        unknown = sorted(expected_ids - set(manifest_paths))
        if unknown:
            errors.append(
                "read plan scope has IDs absent from manifest: " + ", ".join(unknown)
            )
        if scope.get("kind") == "manifest" and expected_ids != set(manifest_paths):
            errors.append("manifest read-plan scope does not contain every manifest ID")
    else:
        expected_ids = set()
        errors.append("read plan scope is invalid")
    seen = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            errors.append(f"read plan row {index} is not an object")
            continue
        doc_id = row.get("id")
        if doc_id in seen:
            errors.append(f"read plan repeats id {doc_id}")
        seen.add(doc_id)
        if doc_id not in manifest_paths:
            errors.append(f"read plan id {doc_id} is absent from manifest")
            continue
        if doc_id not in expected_ids:
            errors.append(f"read plan id {doc_id} is outside its declared scope")
        aliases = row.get("aliases")
        if not isinstance(aliases, list) or aliases != sorted(manifest_paths[doc_id]):
            errors.append(f"read plan aliases for {doc_id} do not match manifest")
        if row.get("canonical_path") != min(manifest_paths[doc_id]):
            errors.append(f"read plan canonical path for {doc_id} is not deterministic")
        canonical_document = min(
            manifest_documents[doc_id], key=lambda item: item["path"]
        )
        expected_readability = canonical_document.get("readability")
        if row.get("readability") not in READABILITY:
            errors.append(f"read plan readability for {doc_id} is invalid")
        elif row.get("readability") != expected_readability:
            errors.append(f"read plan readability for {doc_id} differs from manifest")
        expected_mode = "image" if expected_readability == "scanned" else "text"
        if row.get("read_mode") not in {"text", "image"}:
            errors.append(f"read plan mode for {doc_id} is invalid")
        elif row.get("read_mode") != expected_mode:
            errors.append(f"read plan mode for {doc_id} differs from manifest routing")
        reader_input = row.get("reader_input")
        if (
            row.get("read_mode") == "text"
            and row.get("disposition")
            not in {"deferred-to-review", "parked-unreadable"}
            and (
                not isinstance(reader_input, str)
                or not reader_input.startswith("reader-inputs/")
            )
        ):
            errors.append(f"read plan text input for {doc_id} is invalid")
        if row.get("read_mode") == "image" and reader_input is not None:
            errors.append(f"read plan image input for {doc_id} must be null")
        if row.get("disposition") == "deferred-to-review":
            if deferral_policy != "defer-non-unit-metadata":
                errors.append(
                    f"deferred row {doc_id} requires deferral_policy "
                    "defer-non-unit-metadata"
                )
            if reader_input is not None:
                errors.append(f"deferred row {doc_id} must have null reader_input")
        if row.get("disposition") not in DISPOSITIONS:
            errors.append(f"read plan disposition for {doc_id} is invalid")
        elif (
            expected_readability not in {"native", "scanned"}
            and row.get("disposition") != "parked-unreadable"
        ):
            errors.append(f"read plan must park unreadable document {doc_id}")
        elif expected_readability == "scanned" and row.get("disposition") not in {
            "deferred-to-review",
            "reader-required",
            "parked-unreadable",
        }:
            errors.append(f"read plan must send scanned document {doc_id} to a reader")
        estimate = row.get("estimated_text_chars", 0)
        if not isinstance(estimate, int) or estimate < 0:
            errors.append(f"read plan text estimate for {doc_id} is invalid")
    missing = sorted(expected_ids - seen)
    if missing:
        errors.append("read plan omits scoped ids: " + ", ".join(missing))
    return rows, manifest_paths, errors


def image_confirmations(path, rows):
    if not path:
        return set()
    try:
        data = load(path)
    except (OSError, json.JSONDecodeError) as error:
        sys.exit(f"merge_metadata_reads: cannot read image confirmations: {error}")
    confirmed = data.get("confirmed") if isinstance(data, dict) else None
    if not isinstance(confirmed, list):
        sys.exit("merge_metadata_reads: image confirmations need a confirmed array")
    image_ids = {row.get("id") for row in rows if row.get("read_mode") == "image"}
    seen = set()
    errors = []
    for index, item in enumerate(confirmed):
        if not isinstance(item, dict) or set(item) != {"by", "doc_id"}:
            errors.append(f"confirmation {index} has invalid shape")
            continue
        doc_id = item.get("doc_id")
        if item.get("by") != "lawyer":
            errors.append(f"confirmation for {doc_id} was not made by a lawyer")
        if doc_id not in image_ids:
            errors.append(f"confirmation for {doc_id} is not an image read")
        if doc_id in seen:
            errors.append(f"confirmation repeats {doc_id}")
        seen.add(doc_id)
    if errors:
        sys.exit("merge_metadata_reads: " + "; ".join(errors))
    return seen


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--room-root", required=True)
    parser.add_argument("--read-plan", required=True)
    parser.add_argument("--regex-metadata", required=True)
    parser.add_argument("--reader-results", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--image-confirmations", default=None)
    parser.add_argument("--extractor", choices=["auto", "stdlib"], default="auto")
    args = parser.parse_args()

    try:
        manifest = load(args.manifest)
        plan = load(args.read_plan)
    except (OSError, json.JSONDecodeError) as error:
        sys.exit(f"merge_metadata_reads: {error}")
    rows, manifest_paths, plan_errors = validate_plan(manifest, plan)
    plan_root = Path(args.read_plan).resolve().parent
    input_root = (plan_root / "reader-inputs").resolve()
    for row in rows or []:
        reader_input = row.get("reader_input")
        if not isinstance(reader_input, str):
            continue
        candidate = (plan_root / reader_input).resolve()
        try:
            candidate.relative_to(input_root)
        except ValueError:
            plan_errors.append(
                f"reader input for {row.get('id')} escapes reader-inputs"
            )
            continue
        if not candidate.is_file():
            plan_errors.append(f"reader input for {row.get('id')} is missing")

    for row in rows or []:
        if row.get("disposition") != "deferred-to-review":
            continue
        result_path = Path(args.reader_results) / f"{row.get('id')}.json"
        if result_path.exists():
            plan_errors.append(f"reader result exists for deferred ID {row.get('id')}")
    if plan_errors:
        sys.exit("merge_metadata_reads: " + "; ".join(plan_errors))
    confirmed_images = image_confirmations(args.image_confirmations, rows)
    paths = {doc_id: min(values) for doc_id, values in manifest_paths.items()}
    manifest_docs = {
        document["id"]: document for document in manifest.get("documents", [])
    }

    output = Path(args.outdir) / "metadata"
    expected_names = {f"{row['id']}.json" for row in rows}
    stale_names = sorted(
        path.name for path in output.glob("*.json") if path.name not in expected_names
    )
    if stale_names:
        sys.exit(
            "merge_metadata_reads: metadata output contains records outside this "
            "read plan: " + ", ".join(stale_names)
        )
    reports: list[dict[str, Any]] = []
    image_review = []
    counts = {}
    for row in sorted(rows, key=lambda item: item.get("id", "")):
        doc_id = row.get("id")
        disposition = row.get("disposition")
        reason = None
        audit = None
        errors = []
        record = blank_record(doc_id, "metadata-incomplete")
        rel_path = paths.get(doc_id)
        source_text = ""
        if disposition != "deferred-to-review" and not rel_path:
            errors.append("document is absent from manifest")
        if disposition != "deferred-to-review" and rel_path:
            try:
                absolute_path = os.path.join(args.room_root, rel_path)
                actual_id = hash_id(absolute_path)
                if actual_id != doc_id:
                    raise OSError(
                        f"manifest identity changed for {rel_path}: "
                        f"expected {doc_id}, got {actual_id}"
                    )
                source_text = normalize_quote(
                    extract_document_text(absolute_path, args.extractor)
                )
            except OSError:
                errors.append(f"cannot read source document {rel_path}")
        regex_record = None
        regex_path = Path(args.regex_metadata) / f"{doc_id}.json"
        if disposition != "deferred-to-review" and regex_path.exists():
            try:
                regex_record = load(regex_path)
            except (OSError, json.JSONDecodeError):
                errors.append("cannot read regex record")

        if disposition == "deferred-to-review":
            record = blank_record(doc_id, "deferred-to-review")
            reason = "deferred-to-review"
        elif disposition == "parked-unreadable":
            reason = row.get("reason") or "unreadable"
        elif disposition == "regex-banked":
            if regex_record is None:
                errors.append("banked regex record is missing")
            elif not errors:
                record, errors = compile_banked(regex_record, doc_id, source_text)
            reason = "regex-banked" if not errors else "regex-bank-failed"
        elif disposition in {"reader-required", "regex-audit"}:
            if disposition == "regex-audit" and regex_record is None:
                errors.append("audit regex record is missing")
            result_path = Path(args.reader_results) / f"{doc_id}.json"
            if not result_path.exists():
                errors.append("required fresh reader result is missing")
                reason = "reader-result-missing"
            else:
                try:
                    reader_result = load(result_path)
                except (OSError, json.JSONDecodeError):
                    errors.append("cannot read reader result")
                    reader_result = None
                if reader_result is not None and not errors:
                    errors = validate_reader(
                        reader_result,
                        doc_id,
                        source_text,
                        row.get("read_mode"),
                        manifest_docs.get(doc_id, {}).get("pages"),
                    )
                    if not errors:
                        if row.get("read_mode") == "image":
                            confirmed = doc_id in confirmed_images
                            image_review.append(
                                {
                                    "doc_id": doc_id,
                                    "result": reader_result,
                                    "status": (
                                        "lawyer-confirmed"
                                        if confirmed
                                        else "awaiting-lawyer"
                                    ),
                                }
                            )
                            if confirmed:
                                record = compile_reader(
                                    reader_result,
                                    doc_id,
                                    "image-read-human-confirmed",
                                )
                                reason = "image-reader-accepted-human-confirmed"
                            else:
                                reason = "image-read-awaits-human-verification"
                        else:
                            record = compile_reader(reader_result, doc_id, "model-read")
                            reason = "reader-accepted"
                            if (
                                disposition == "regex-audit"
                                and regex_record is not None
                            ):
                                audit = compare_audit(regex_record, record)
                if errors and reason is None:
                    reason = "reader-result-rejected"
        else:
            errors.append(f"unknown read-plan disposition {disposition!r}")
            reason = "invalid-read-plan"

        if errors:
            failed_receipt = any(
                "quote" in error or "receipt" in error for error in errors
            )
            record = blank_record(
                doc_id,
                "quote-unverified" if failed_receipt else "metadata-incomplete",
            )
        dump_atomic(output / f"{doc_id}.json", record)
        counts[record["status"]] = counts.get(record["status"], 0) + 1
        reports.append(
            {
                "audit": audit,
                "disposition": disposition,
                "errors": errors,
                "id": doc_id,
                "reason": reason,
                "status": record["status"],
            }
        )

    audit_disagreements = [
        item["id"]
        for item in reports
        if isinstance(item["audit"], dict) and "disagree" in item["audit"].values()
    ]
    if audit_disagreements:
        for item in reports:
            if item["disposition"] != "regex-banked":
                continue
            dump_atomic(
                output / f"{item['id']}.json",
                blank_record(item["id"], "metadata-incomplete"),
            )
            item["reason"] = "regex-bank-invalidated-by-audit"
            item["status"] = "metadata-incomplete"
        counts = {}
        for item in reports:
            counts[item["status"]] = counts.get(item["status"], 0) + 1

    banked = sum(1 for item in reports if item["reason"] == "regex-banked")
    deferred = sum(1 for item in reports if item["disposition"] == "deferred-to-review")
    parked = sum(1 for item in reports if item["disposition"] == "parked-unreadable")
    reader_accepted = sum(
        1
        for item in reports
        if item["reason"]
        in {"reader-accepted", "image-reader-accepted-human-confirmed"}
    )
    report = {
        "audit_disagreements": audit_disagreements,
        "banked": banked,
        "counts": counts,
        "deferred": deferred,
        "documents": reports,
        "parked": parked,
        "partition_complete": (
            reader_accepted + banked + deferred + parked == len(reports)
        ),
        "planned": len(reports),
        "reader_accepted": reader_accepted,
        "read_plan_id": plan["plan_id"],
        "requires_full_regex_read": bool(audit_disagreements),
        "version": 1,
    }
    dump_atomic(Path(args.outdir) / "metadata-merge-report.json", report)
    dump_atomic(
        Path(args.outdir) / "image-metadata-review.json",
        {
            "documents": sorted(image_review, key=lambda item: item["doc_id"]),
            "read_plan_id": plan["plan_id"],
            "version": 1,
        },
    )
    print(
        f"Wrote {len(reports)} canonical metadata records; "
        f"{report['reader_accepted']} fresh reader result(s) accepted"
    )
    if any(item["errors"] for item in reports):
        print(
            "Some records were parked; see metadata-merge-report.json", file=sys.stderr
        )
    if audit_disagreements:
        print(
            "Regex audit disagreed; rerun prep with --expand-bank before "
            "relationship mapping",
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()
