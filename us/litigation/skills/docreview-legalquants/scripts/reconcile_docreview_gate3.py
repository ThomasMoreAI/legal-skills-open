#!/usr/bin/env python3
"""Reconcile document-review coverage plus lawyer-confirmed image-review bundles.

This docreview-owned wrapper composes the shared coverage reconciler with an
additive image-confirmation overlay. It never rewrites findings, model statuses,
quote-verification receipts, or evidence text. A valid lawyer confirmation may
satisfy only the shared reconciler's expected human-required image-verification
error for the exact ledger-bound document bundle.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import sys
import tempfile
from pathlib import Path
from types import ModuleType
from typing import Any, NoReturn, cast

JsonObject = dict[str, Any]
CONFIRMATION_KEYS = {
    "confirmation",
    "confirmed_by",
    "doc_id",
    "finding_ids",
    "note",
    "proposal_digest",
}


def fail(message: str) -> NoReturn:
    sys.exit(f"reconcile_docreview_gate3: {message}")


def load(path: str, kind: str) -> JsonObject:
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"cannot read {kind} at {path}: {error}")
    if not isinstance(value, dict):
        fail(f"{kind} must be an object")
    return cast(JsonObject, value)


def canonical_digest(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return "sha256:" + hashlib.sha256(raw.encode()).hexdigest()


def proposal_ledger(findings: JsonObject) -> JsonObject:
    proposal = cast(JsonObject, json.loads(json.dumps(findings)))
    proposal.pop("image_confirmations", None)
    rows = proposal.get("findings")
    if not isinstance(rows, list):
        fail("findings ledger has no findings array")
    for raw_row in cast(list[Any], rows):
        if not isinstance(raw_row, dict):
            fail("findings ledger contains a non-object finding")
        raw_row.pop("lawyer_ruling", None)
    return proposal


def is_image_review_row(row: JsonObject) -> bool:
    verification = row.get("quote_verification")
    reason = row.get("human_review_reason")
    return bool(
        row.get("receipt_mode") == "image-transcription"
        or (isinstance(reason, str) and "image" in reason.lower())
        or (
            isinstance(verification, dict)
            and verification.get("status") == "human-required"
            and "image" in str(verification.get("reason", "")).lower()
        )
    )


def image_bundles(findings: JsonObject) -> dict[str, list[JsonObject]]:
    proposal = proposal_ledger(findings)
    grouped: dict[str, list[JsonObject]] = {}
    for raw_row in cast(list[Any], proposal["findings"]):
        row = cast(JsonObject, raw_row)
        if not is_image_review_row(row):
            continue
        doc_id = row.get("doc_id")
        finding_id = row.get("finding_id")
        if not isinstance(doc_id, str) or not isinstance(finding_id, str):
            fail("image-review finding has an invalid subject")
        grouped.setdefault(doc_id, []).append(row)
    return {
        doc_id: sorted(rows, key=lambda row: row["finding_id"])
        for doc_id, rows in grouped.items()
    }


def shared_reconciler() -> ModuleType:
    scripts = Path(__file__).resolve().parent
    candidates = [scripts / "shared" / "reconcile_counts.py"]
    for candidate in candidates:
        if not candidate.is_file():
            continue
        spec = importlib.util.spec_from_file_location(
            "lq_shared_reconcile_counts", candidate
        )
        if spec is None or spec.loader is None:
            continue
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    fail("cannot locate the packaged shared reconcile_counts.py")


def validate_bindings(
    manifest: JsonObject, findings: JsonObject, framework: JsonObject
) -> None:
    frame = framework.get("frame")
    if not isinstance(frame, dict) or frame.get("kind") != "requests":
        fail("framework must have frame.kind 'requests'")
    corpus_id = manifest.get("corpus_id")
    if not isinstance(corpus_id, str) or not corpus_id:
        fail("manifest has no corpus_id")
    if frame.get("corpus_id") != corpus_id:
        fail("framework and manifest corpus IDs differ")
    if findings.get("framework_version") != framework.get("framework_version"):
        fail("findings and framework versions differ")


def validate_image_confirmations(
    findings: JsonObject, bundles: dict[str, list[JsonObject]]
) -> tuple[set[str], list[str], list[JsonObject]]:
    errors: list[str] = []
    raw_confirmations = findings.get("image_confirmations", [])
    if not isinstance(raw_confirmations, list):
        return set(), ["findings image_confirmations overlay must be an array"], []
    by_doc: dict[str, JsonObject] = {}
    for index, raw_row in enumerate(cast(list[Any], raw_confirmations)):
        if not isinstance(raw_row, dict) or set(raw_row) != CONFIRMATION_KEYS:
            errors.append(f"image confirmation {index} has invalid shape")
            continue
        row = cast(JsonObject, raw_row)
        doc_id = row.get("doc_id")
        if not isinstance(doc_id, str) or not doc_id:
            errors.append(f"image confirmation {index} has invalid document identity")
            continue
        if doc_id in by_doc:
            errors.append(f"image confirmation repeats document {doc_id}")
            continue
        by_doc[doc_id] = row

    confirmed: set[str] = set()
    document_rows: list[JsonObject] = []
    for doc_id, rows in sorted(bundles.items()):
        expected_ids = [cast(str, row["finding_id"]) for row in rows]
        expected_digest = canonical_digest(rows)
        confirmation = by_doc.pop(doc_id, None)
        state = "missing"
        if confirmation is None:
            errors.append(f"image review for {doc_id} lacks a lawyer confirmation")
        else:
            state = str(confirmation.get("confirmation", "invalid"))
            if confirmation.get("confirmed_by") != "lawyer":
                errors.append(f"image confirmation for {doc_id} is not lawyer-authored")
            if confirmation.get("confirmation") not in {"confirmed", "needs-review"}:
                errors.append(f"image confirmation for {doc_id} is invalid")
            if not isinstance(confirmation.get("note"), str):
                errors.append(f"image confirmation for {doc_id} has an invalid note")
            if confirmation.get("finding_ids") != expected_ids:
                errors.append(f"image confirmation for {doc_id} has stale finding IDs")
            if confirmation.get("proposal_digest") != expected_digest:
                errors.append(
                    f"image confirmation for {doc_id} has a stale proposal digest"
                )
            exact = (
                confirmation.get("confirmed_by") == "lawyer"
                and confirmation.get("confirmation") == "confirmed"
                and isinstance(confirmation.get("note"), str)
                and confirmation.get("finding_ids") == expected_ids
                and confirmation.get("proposal_digest") == expected_digest
            )
            if confirmation.get("confirmation") == "needs-review":
                errors.append(f"image review for {doc_id} still needs lawyer review")
            if exact:
                confirmed.add(doc_id)
        counts = {"present": 0, "absent": 0, "unresolved": 0}
        for row in rows:
            status = str(row.get("status", ""))
            if status in counts:
                counts[status] += 1
        document_rows.append(
            {
                "confirmation": state,
                "doc_id": doc_id,
                "finding_calls": len(rows),
                "proposal_digest": expected_digest,
                "status_counts": counts,
            }
        )
    for doc_id in sorted(by_doc):
        errors.append(f"image confirmation references non-image document {doc_id}")
    return confirmed, errors, document_rows


def write_json(path: str, value: JsonObject) -> None:
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(
        prefix=f".{output.name}.", suffix=".tmp", dir=output.parent
    )
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(value, handle, indent=2, sort_keys=True)
            handle.write("\n")
        os.replace(temporary, output)
    except Exception:
        try:
            os.unlink(temporary)
        except OSError:
            pass
        raise


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--findings", required=True)
    parser.add_argument("--framework", required=True)
    parser.add_argument("--families", default=None)
    parser.add_argument("--clusters", default=None)
    parser.add_argument("--privilege-queue", default=None)
    parser.add_argument("--review-plan", default=None)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    input_paths = [
        value
        for value in (
            args.manifest,
            args.findings,
            args.framework,
            args.families,
            args.clusters,
            args.privilege_queue,
            args.review_plan,
        )
        if value is not None
    ]
    resolved_inputs = {
        Path(value).expanduser().absolute().resolve() for value in input_paths
    }
    resolved_output = Path(args.out).expanduser().absolute().resolve()
    if resolved_output in resolved_inputs:
        fail("--out must be a distinct new artifact path; inputs are immutable")

    manifest = load(args.manifest, "manifest")
    findings = load(args.findings, "findings")
    framework = load(args.framework, "framework")
    families = load(args.families, "families") if args.families else None
    clusters = load(args.clusters, "clusters") if args.clusters else None
    privilege_queue = (
        load(args.privilege_queue, "privilege queue") if args.privilege_queue else None
    )
    review_plan = load(args.review_plan, "review plan") if args.review_plan else None
    validate_bindings(manifest, findings, framework)

    shared = shared_reconciler()
    base = shared.reconcile(
        manifest,
        findings,
        framework,
        families,
        clusters,
        privilege_queue,
        review_plan,
    )
    bundles = image_bundles(findings)
    confirmed_docs, image_errors, document_rows = validate_image_confirmations(
        findings, bundles
    )

    base_errors = list(base["errors"])
    satisfied: list[str] = []
    for doc_id in sorted(confirmed_docs):
        for row in bundles[doc_id]:
            if row.get("status") != "present":
                continue
            message = (
                f"finding {row.get('finding_id')} is present without confirmed "
                "quote verification"
            )
            if message in base_errors:
                base_errors.remove(message)
                satisfied.append(message)

    errors = base_errors + image_errors
    lens_ok = all(bool(info.get("ok")) for info in base["per_lens"].values())
    ok = lens_ok and not errors
    frame = cast(JsonObject, framework["frame"])
    report: JsonObject = {
        "artifact": "docreview-gate3-reconciliation",
        "base_confirmation_errors_satisfied_by_overlay": sorted(satisfied),
        "base_coverage": {
            "lines": base["lines"],
            "per_lens": base["per_lens"],
            "totals": base["totals"],
        },
        "bindings": {
            "corpus_id": manifest["corpus_id"],
            "frame_id": frame.get("frame_id"),
            "framework_digest": canonical_digest(framework),
            "framework_version": framework.get("framework_version"),
            "ledger_digest": canonical_digest(proposal_ledger(findings)),
            "review_plan_id": findings.get("review_plan_id"),
        },
        "errors": errors,
        "image_confirmation": {
            "confirmed_documents": len(confirmed_docs),
            "documents": document_rows,
            "expected_documents": len(bundles),
            "finding_calls": sum(len(rows) for rows in bundles.values()),
            "pending_documents": len(bundles) - len(confirmed_docs),
        },
        "ok": ok,
        "version": 1,
    }
    try:
        write_json(args.out, report)
    except OSError as error:
        fail(f"cannot write {args.out}: {error}")
    print(
        f"{'RECONCILED' if ok else 'NOT RECONCILED'}: "
        f"{len(confirmed_docs)} of {len(bundles)} image document(s) confirmed"
    )
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
