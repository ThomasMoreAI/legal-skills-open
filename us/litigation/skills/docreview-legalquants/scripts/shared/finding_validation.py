#!/usr/bin/env python3
"""Shared deterministic validation for maker checkpoints."""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
from pathlib import Path
from typing import Any

from document_text import extract_document_text, normalize_quote

RESULT_KEYS = {
    "review_plan_id",
    "framework_version",
    "unit_id",
    "lens_id",
    "findings",
    "privilege_candidates",
}
FINDING_KEYS = {
    "finding_id",
    "issue_id",
    "doc_id",
    "status",
    "receipt_mode",
    "page",
    "section",
    "quote",
    "characterization",
    "band",
    "band_basis",
    "current_position",
}
CANDIDATE_KEYS = {
    "doc_id",
    "reason",
    "quote",
    "receipt_mode",
    "page",
    "signals",
}
STATUSES = {"present", "absent", "unresolved"}
BANDS = {"high", "medium", "low"}
SIGNALS = {"attorney-domain", "legend", "legal-advice-content", "counsel-name"}


def dump_atomic(path: str | Path, value: object) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(
        prefix=destination.name + ".", dir=destination.parent
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(value, handle, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, destination)
        directory_fd = os.open(destination.parent, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    except BaseException:
        try:
            os.unlink(temporary)
        except OSError:
            pass
        raise


def hash_id(path: str | Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()[:12]


def expected_job_id(framework_version: object, unit_id: object, lens_id: object) -> str:
    raw = f"{framework_version}\0{unit_id}\0{lens_id}".encode()
    return hashlib.sha256(raw).hexdigest()[:16]


def expected_plan_id(plan: dict[str, object]) -> str:
    payload = {
        "framework_digest": plan.get("framework_digest"),
        "framework_version": plan.get("framework_version"),
        "jobs": plan.get("jobs"),
        "parked_units": plan.get("parked_units"),
        "summary": plan.get("summary"),
        "tier": plan.get("tier"),
        "version": plan.get("version"),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode()).hexdigest()[:16]


def source_cache(
    manifest: dict[str, Any], room_root: str, extractor: str
) -> tuple[dict[str, dict[str, object]], object]:
    docs: dict[str, dict[str, object]] = {}
    raw_documents = manifest.get("documents", [])
    if not isinstance(raw_documents, list):
        raise OSError("manifest documents must be an array")
    for document in sorted(raw_documents, key=lambda item: (item["id"], item["path"])):
        docs.setdefault(document["id"], document)
    cache: dict[str, str | None] = {}

    def text_for(doc_id: str) -> str | None:
        if doc_id in cache:
            return cache[doc_id]
        document = docs[doc_id]
        if document.get("readability") != "native":
            cache[doc_id] = None
            return None
        path = os.path.join(room_root, str(document["path"]))
        try:
            if hash_id(path) != doc_id:
                raise OSError
            extracted = extract_document_text(path, extractor)
        except OSError as error:
            raise OSError(f"cannot read source document {document['path']}") from error
        cache[doc_id] = normalize_quote(extracted)
        return cache[doc_id]

    return docs, text_for


def validate_receipt(item, document, text_for, label):
    errors = []
    quote = item.get("quote")
    mode = item.get("receipt_mode")
    page = item.get("page")
    if not isinstance(quote, str) or not quote.strip():
        return [f"{label} has no quote"]
    if document.get("readability") == "native":
        if mode != "text" or page is not None:
            errors.append(f"{label} must use a text receipt with null page")
        elif normalize_quote(quote) not in text_for(document["id"]):
            errors.append(f"{label} quote is absent from visible text")
    elif document.get("readability") == "scanned":
        if mode != "image-transcription" or not isinstance(page, int) or page < 1:
            errors.append(f"{label} must carry an image transcription and page")
        pages = document.get("pages")
        if isinstance(pages, int) and isinstance(page, int) and page > pages:
            errors.append(f"{label} page exceeds the manifest page count")
    else:
        errors.append(f"{label} references an unreadable document")
    return errors


def validate_result(result, job, lens_items, docs, text_for):
    errors = []
    if not isinstance(result, dict) or set(result) != RESULT_KEYS:
        return [], [], ["maker result has unexpected or missing top-level keys"]
    if result.get("review_plan_id") != job["review_plan_id"]:
        errors.append("maker review_plan_id does not match the job")
    if result.get("framework_version") != job["framework_version"]:
        errors.append("maker framework version does not match the job")
    if result.get("unit_id") != job["unit_id"]:
        errors.append("maker unit_id does not match the job")
    if result.get("lens_id") != job["lens_id"]:
        errors.append("maker lens_id does not match the job")
    raw_findings = result.get("findings")
    if not isinstance(raw_findings, list):
        return [], [], errors + ["maker findings must be an array"]
    actual_issues = [
        item.get("issue_id") for item in raw_findings if isinstance(item, dict)
    ]
    if actual_issues != job["issue_ids"]:
        errors.append("maker result does not cover every job issue in order")
    compiled = []
    for index, finding in enumerate(raw_findings):
        label = f"finding {index}"
        if not isinstance(finding, dict) or set(finding) != FINDING_KEYS:
            errors.append(f"{label} has unexpected or missing keys")
            continue
        issue_id = finding.get("issue_id")
        doc_id = finding.get("doc_id")
        status = finding.get("status")
        if issue_id not in lens_items:
            errors.append(f"{label} has an unknown issue_id")
            continue
        if doc_id not in job["member_ids"]:
            errors.append(f"{label} cites a document outside the unit")
            continue
        if finding.get("finding_id") != f"{issue_id}/{doc_id}":
            errors.append(f"{label} has an invalid stable finding_id")
        if status not in STATUSES:
            errors.append(f"{label} has an invalid status")
        item = lens_items[issue_id]
        characterization = finding.get("characterization")
        cap = (item.get("answer_shape") or {}).get("characterization_max_words")
        if not isinstance(characterization, str) or not characterization.strip():
            errors.append(f"{label} has no characterization")
        elif isinstance(cap, int) and len(characterization.split()) > cap:
            errors.append(f"{label} exceeds its characterization word cap")
        quote = finding.get("quote")
        if quote is not None:
            errors.extend(validate_receipt(finding, docs[doc_id], text_for, label))
        elif finding.get("receipt_mode") is not None or finding.get("page") is not None:
            errors.append(f"{label} has receipt metadata without a quote")
        if status == "present":
            if (
                not isinstance(finding.get("section"), str)
                or not finding["section"].strip()
            ):
                errors.append(f"{label} is present without a section")
            if item.get("materiality"):
                if finding.get("band") not in BANDS:
                    errors.append(f"{label} is present without a valid band")
                if (
                    not isinstance(finding.get("band_basis"), str)
                    or not finding["band_basis"].strip()
                ):
                    errors.append(f"{label} is present without a band basis")
            elif (
                finding.get("band") is not None or finding.get("band_basis") is not None
            ):
                errors.append(
                    f"{label} carries a materiality band that was not requested"
                )
            if quote is None:
                errors.append(f"{label} is present without quoted evidence")
            if (
                job.get("requires_current_position")
                and finding.get("current_position") is not True
            ):
                errors.append(f"{label} does not establish the current family position")
        else:
            if finding.get("band") is not None or finding.get("band_basis") is not None:
                errors.append(f"{label} is non-present but carries a materiality band")
            if quote is None and finding.get("section") is not None:
                errors.append(f"{label} has a section without quoted evidence")
        canonical = {**finding, "lens_id": job["lens_id"], "unit_id": job["unit_id"]}
        if quote is not None:
            if docs[doc_id].get("readability") == "native":
                canonical["quote_verification"] = {
                    "checker": "deterministic-visible-text",
                    "reason": None,
                    "status": "confirmed",
                }
            else:
                canonical["quote_verification"] = {
                    "checker": "human-image-lane",
                    "reason": "image transcription is not script-verifiable",
                    "status": "human-required",
                }
        if job.get("contains_image"):
            canonical["human_review_reason"] = (
                "unit contains image material; image review is not script-verifiable"
            )
        if job.get("contains_unreadable"):
            canonical["human_review_reason"] = (
                "unit contains unreadable parked material"
            )
            if canonical["status"] != "unresolved":
                canonical["status"] = "unresolved"
                canonical["current_position"] = False
        compiled.append(canonical)
    candidates = result.get("privilege_candidates")
    if not isinstance(candidates, list):
        errors.append("privilege_candidates must be an array")
        candidates = []
    accepted_candidates = []
    for index, candidate in enumerate(candidates):
        label = f"privilege candidate {index}"
        if not isinstance(candidate, dict) or set(candidate) != CANDIDATE_KEYS:
            errors.append(f"{label} has unexpected or missing keys")
            continue
        doc_id = candidate.get("doc_id")
        if doc_id not in job["member_ids"]:
            errors.append(f"{label} cites a document outside the unit")
            continue
        signals = candidate.get("signals")
        if (
            not isinstance(signals, list)
            or not signals
            or len(signals) != len(set(signals))
            or not set(signals) <= SIGNALS
        ):
            errors.append(f"{label} has invalid signals")
        if (
            not isinstance(candidate.get("reason"), str)
            or not candidate["reason"].strip()
        ):
            errors.append(f"{label} has no reason")
        errors.extend(validate_receipt(candidate, docs[doc_id], text_for, label))
        accepted_candidates.append(candidate)
    return compiled, accepted_candidates, errors
