#!/usr/bin/env python3
"""Validate offline lawyer feedback and write an additive findings overlay.

The source findings ledger and framework are immutable inputs. The output is a
deterministic copy whose only permitted difference is a ``lawyer_ruling`` field
on findings named by the feedback artifact and an additive, document-level
``image_confirmations`` overlay.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any, NoReturn, cast

JsonObject = dict[str, Any]

RULINGS = {"responsive", "not-responsive", "needs-review", "privileged"}
IMAGE_CONFIRMATIONS = {"confirmed", "needs-review"}
TOP_LEVEL_KEYS = {
    "artifact",
    "corpus_id",
    "frame_id",
    "framework_digest",
    "framework_version",
    "ledger_digest",
    "review_plan_id",
    "rulings",
    "source",
    "version",
}
OPTIONAL_TOP_LEVEL_KEYS = {"image_confirmations"}
RULING_KEYS = {
    "doc_id",
    "finding_id",
    "issue_id",
    "machine_status",
    "note",
    "ruled_by",
    "ruling",
}
OVERLAY_KEYS = {"note", "ruled_by", "ruling"}
IMAGE_CONFIRMATION_KEYS = {
    "confirmation",
    "confirmed_by",
    "doc_id",
    "finding_ids",
    "note",
    "proposal_digest",
}


def fail(message: str) -> NoReturn:
    sys.exit(f"ingest_review_feedback: {message}")


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
    """Return the immutable proposal ledger, excluding only lawyer overlays."""

    proposal = cast(JsonObject, json.loads(json.dumps(findings)))
    proposal.pop("image_confirmations", None)
    rows = proposal.get("findings")
    if not isinstance(rows, list):
        fail("findings ledger has no findings array")
    for raw_row in cast(list[Any], rows):
        if not isinstance(raw_row, dict):
            fail("findings ledger contains a non-object finding")
        row = cast(JsonObject, raw_row)
        row.pop("lawyer_ruling", None)
    return proposal


def validate_overlay(value: object, finding_id: str) -> None:
    if not isinstance(value, dict) or set(value) != OVERLAY_KEYS:
        fail(f"existing lawyer overlay has invalid shape for {finding_id}")
    overlay = cast(JsonObject, value)
    if overlay.get("ruling") not in RULINGS:
        fail(f"existing lawyer overlay has invalid ruling for {finding_id}")
    if overlay.get("ruled_by") != "lawyer":
        fail(f"existing lawyer overlay is not lawyer-authored for {finding_id}")
    if not isinstance(overlay.get("note"), str):
        fail(f"existing lawyer overlay note is invalid for {finding_id}")


def validate_feedback(
    feedback: JsonObject,
) -> tuple[list[JsonObject], list[JsonObject] | None]:
    keys = set(feedback)
    allowed = TOP_LEVEL_KEYS | OPTIONAL_TOP_LEVEL_KEYS
    if not TOP_LEVEL_KEYS <= keys or not keys <= allowed:
        missing = sorted(TOP_LEVEL_KEYS - keys)
        extra = sorted(keys - allowed)
        fail(f"feedback keys are invalid; missing={missing}, extra={extra}")
    if feedback.get("artifact") != "review-feedback" or feedback.get("version") != 1:
        fail("unsupported feedback artifact")
    for key in (
        "corpus_id",
        "frame_id",
        "framework_digest",
        "ledger_digest",
        "review_plan_id",
        "source",
    ):
        if not isinstance(feedback.get(key), str) or not feedback[key]:
            fail(f"feedback {key} must be a non-empty string")
    if not isinstance(feedback.get("framework_version"), int) or isinstance(
        feedback.get("framework_version"), bool
    ):
        fail("feedback framework_version must be an integer")
    rows = feedback.get("rulings")
    if not isinstance(rows, list):
        fail("feedback rulings must be an array")
    seen: set[str] = set()
    validated: list[JsonObject] = []
    for index, raw_row in enumerate(cast(list[Any], rows)):
        if not isinstance(raw_row, dict) or set(raw_row) != RULING_KEYS:
            fail(f"feedback ruling {index} has unexpected or missing keys")
        row = cast(JsonObject, raw_row)
        finding_id = row.get("finding_id")
        issue_id = row.get("issue_id")
        doc_id = row.get("doc_id")
        if not all(
            isinstance(value, str) and value for value in (finding_id, issue_id, doc_id)
        ):
            fail(f"feedback ruling {index} has an invalid subject")
        finding_id = cast(str, finding_id)
        issue_id = cast(str, issue_id)
        doc_id = cast(str, doc_id)
        if finding_id != f"{issue_id}/{doc_id}":
            fail(f"feedback ruling {finding_id!r} has an invalid stable ID")
        if finding_id in seen:
            fail(f"feedback repeats finding {finding_id!r}")
        seen.add(finding_id)
        if row.get("machine_status") not in {"present", "absent", "unresolved"}:
            fail(f"feedback ruling {finding_id!r} has an invalid machine status")
        if row.get("ruling") not in RULINGS:
            fail(f"feedback ruling {finding_id!r} has an invalid lawyer ruling")
        if row.get("ruled_by") != "lawyer":
            fail(f"feedback ruling {finding_id!r} is not lawyer-authored")
        if not isinstance(row.get("note"), str):
            fail(f"feedback ruling {finding_id!r} has an invalid note")
        validated.append(row)
    raw_confirmations = feedback.get("image_confirmations")
    confirmations: list[JsonObject] | None = None
    if "image_confirmations" in feedback:
        if not isinstance(raw_confirmations, list):
            fail("feedback image_confirmations must be an array")
        confirmations = []
        seen_docs: set[str] = set()
        for index, raw_row in enumerate(cast(list[Any], raw_confirmations)):
            if not isinstance(raw_row, dict) or set(raw_row) != IMAGE_CONFIRMATION_KEYS:
                fail(
                    f"feedback image confirmation {index} has unexpected or "
                    "missing keys"
                )
            row = cast(JsonObject, raw_row)
            doc_id = row.get("doc_id")
            if not isinstance(doc_id, str) or not doc_id:
                fail(f"feedback image confirmation {index} has an invalid document")
            if doc_id in seen_docs:
                fail(f"feedback repeats image confirmation for {doc_id!r}")
            seen_docs.add(doc_id)
            if row.get("confirmation") not in IMAGE_CONFIRMATIONS:
                fail(f"feedback image confirmation for {doc_id!r} is invalid")
            if row.get("confirmed_by") != "lawyer":
                fail(
                    f"feedback image confirmation for {doc_id!r} is not lawyer-authored"
                )
            finding_ids = row.get("finding_ids")
            if (
                not isinstance(finding_ids, list)
                or not finding_ids
                or any(not isinstance(value, str) or not value for value in finding_ids)
                or finding_ids != sorted(set(finding_ids))
            ):
                fail(
                    f"feedback image confirmation for {doc_id!r} has invalid "
                    "finding IDs"
                )
            digest = row.get("proposal_digest")
            if (
                not isinstance(digest, str)
                or len(digest) != 71
                or not digest.startswith("sha256:")
                or any(char not in "0123456789abcdef" for char in digest[7:])
            ):
                fail(
                    f"feedback image confirmation for {doc_id!r} has invalid "
                    "proposal digest"
                )
            if not isinstance(row.get("note"), str):
                fail(f"feedback image confirmation for {doc_id!r} has an invalid note")
            confirmations.append(row)
        confirmations.sort(key=lambda row: row["doc_id"])
    return sorted(validated, key=lambda row: row["finding_id"]), confirmations


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


def image_bundles(findings: JsonObject) -> dict[str, tuple[list[str], str]]:
    proposal = proposal_ledger(findings)
    grouped: dict[str, list[JsonObject]] = {}
    for raw_row in cast(list[Any], proposal.get("findings", [])):
        if not isinstance(raw_row, dict):
            fail("findings ledger contains a non-object finding")
        row = cast(JsonObject, raw_row)
        if not is_image_review_row(row):
            continue
        doc_id = row.get("doc_id")
        finding_id = row.get("finding_id")
        if not isinstance(doc_id, str) or not isinstance(finding_id, str):
            fail("image-review finding has an invalid subject")
        grouped.setdefault(doc_id, []).append(row)
    bundles: dict[str, tuple[list[str], str]] = {}
    for doc_id, rows in grouped.items():
        ordered = sorted(rows, key=lambda row: row["finding_id"])
        bundles[doc_id] = (
            [cast(str, row["finding_id"]) for row in ordered],
            canonical_digest(ordered),
        )
    return bundles


def validate_image_confirmation_subjects(
    confirmations: list[JsonObject], findings: JsonObject
) -> None:
    bundles = image_bundles(findings)
    for row in confirmations:
        doc_id = cast(str, row["doc_id"])
        expected = bundles.get(doc_id)
        if expected is None:
            fail(f"image confirmation references non-image document {doc_id!r}")
        expected_ids, expected_digest = expected
        if row["finding_ids"] != expected_ids:
            fail(f"image confirmation for {doc_id!r} has stale finding IDs")
        if row["proposal_digest"] != expected_digest:
            fail(f"image confirmation for {doc_id!r} has a stale proposal digest")


def validate_bindings(
    feedback: JsonObject,
    findings: JsonObject,
    framework: JsonObject,
    manifest: JsonObject,
) -> None:
    raw_frame = framework.get("frame")
    if not isinstance(raw_frame, dict) or raw_frame.get("kind") != "requests":
        fail("framework must have frame.kind 'requests'")
    frame = cast(JsonObject, raw_frame)
    if feedback["framework_version"] != framework.get("framework_version"):
        fail("framework version mismatch")
    if findings.get("framework_version") != framework.get("framework_version"):
        fail("findings and framework versions differ")
    if feedback["framework_digest"] != canonical_digest(framework):
        fail("framework digest mismatch; feedback is stale")
    if feedback["ledger_digest"] != canonical_digest(proposal_ledger(findings)):
        fail("ledger digest mismatch; feedback is stale")
    if feedback["review_plan_id"] != findings.get("review_plan_id"):
        fail("review plan mismatch; feedback is stale")
    if feedback["frame_id"] != frame.get("frame_id"):
        fail("frame ID mismatch; feedback is stale")
    corpus_id = manifest.get("corpus_id")
    if not isinstance(corpus_id, str) or not corpus_id:
        fail("manifest has no corpus_id")
    if frame.get("corpus_id") != corpus_id:
        fail("framework and manifest corpus IDs differ")
    if feedback["corpus_id"] != corpus_id:
        fail("corpus ID mismatch; feedback is stale")


def apply_overlay(
    findings: JsonObject,
    rulings: list[JsonObject],
    image_confirmations: list[JsonObject] | None,
) -> JsonObject:
    output = cast(JsonObject, json.loads(json.dumps(findings)))
    existing_confirmations = output.pop("image_confirmations", None)
    if existing_confirmations is not None:
        if not isinstance(existing_confirmations, list):
            fail("existing image confirmation overlay has invalid shape")
        seen_docs: set[str] = set()
        for index, raw_row in enumerate(cast(list[Any], existing_confirmations)):
            if not isinstance(raw_row, dict) or set(raw_row) != IMAGE_CONFIRMATION_KEYS:
                fail(f"existing image confirmation overlay {index} has invalid shape")
            doc_id = raw_row.get("doc_id")
            if not isinstance(doc_id, str) or not doc_id or doc_id in seen_docs:
                fail(
                    f"existing image confirmation overlay {index} has invalid "
                    "document identity"
                )
            seen_docs.add(doc_id)
            if raw_row.get("confirmation") not in IMAGE_CONFIRMATIONS:
                fail(f"existing image confirmation for {doc_id!r} is invalid")
            if raw_row.get("confirmed_by") != "lawyer":
                fail(
                    f"existing image confirmation for {doc_id!r} is not lawyer-authored"
                )
            if not isinstance(raw_row.get("finding_ids"), list) or not isinstance(
                raw_row.get("note"), str
            ):
                fail(f"existing image confirmation for {doc_id!r} has invalid shape")
        validate_image_confirmation_subjects(
            cast(list[JsonObject], existing_confirmations), findings
        )
    rows = output.get("findings")
    if not isinstance(rows, list):
        fail("findings ledger has no findings array")
    by_id: dict[str, JsonObject] = {}
    for raw_row in cast(list[Any], rows):
        if not isinstance(raw_row, dict):
            fail("findings ledger contains a non-object finding")
        row = cast(JsonObject, raw_row)
        finding_id = row.get("finding_id")
        issue_id = row.get("issue_id")
        doc_id = row.get("doc_id")
        if not all(
            isinstance(value, str) and value for value in (finding_id, issue_id, doc_id)
        ):
            fail("source finding has an invalid subject")
        finding_id = cast(str, finding_id)
        issue_id = cast(str, issue_id)
        doc_id = cast(str, doc_id)
        if finding_id != f"{issue_id}/{doc_id}":
            fail(f"source finding {finding_id!r} has an invalid stable ID")
        if finding_id in by_id:
            fail(f"source findings repeat {finding_id!r}")
        if "lawyer_ruling" in row:
            validate_overlay(row["lawyer_ruling"], finding_id)
            del row["lawyer_ruling"]
        by_id[finding_id] = row
    for ruling in rulings:
        finding_id = ruling["finding_id"]
        row = by_id.get(finding_id)
        if row is None:
            fail(f"feedback references unknown finding {finding_id!r}")
        for key in ("issue_id", "doc_id"):
            if ruling[key] != row.get(key):
                fail(f"feedback subject drifted for {finding_id!r}")
        if ruling["machine_status"] != row.get("status"):
            fail(f"feedback machine status drifted for {finding_id!r}")
        row["lawyer_ruling"] = {
            "note": ruling["note"],
            "ruled_by": "lawyer",
            "ruling": ruling["ruling"],
        }
    if image_confirmations is not None:
        output["image_confirmations"] = image_confirmations
    elif existing_confirmations is not None:
        output["image_confirmations"] = existing_confirmations
    return output


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
    parser.add_argument("--feedback", required=True)
    parser.add_argument("--findings", required=True)
    parser.add_argument("--framework", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    paths = [
        Path(value).expanduser().absolute().resolve()
        for value in (
            args.feedback,
            args.findings,
            args.framework,
            args.manifest,
            args.out,
        )
    ]
    if len(set(paths)) != len(paths):
        fail("--out must be a distinct new artifact path; inputs are immutable")
    feedback = load(args.feedback, "feedback")
    findings = load(args.findings, "findings")
    framework = load(args.framework, "framework")
    manifest = load(args.manifest, "manifest")
    rulings, image_confirmations = validate_feedback(feedback)
    validate_bindings(feedback, findings, framework, manifest)
    if image_confirmations is not None:
        validate_image_confirmation_subjects(image_confirmations, findings)
    output = apply_overlay(findings, rulings, image_confirmations)
    try:
        write_json(args.out, output)
    except OSError as error:
        fail(f"cannot write {args.out}: {error}")
    print(
        f"wrote {args.out}: {len(rulings)} lawyer ruling(s), "
        f"{len(image_confirmations or [])} image confirmation(s)"
    )


if __name__ == "__main__":
    main()
