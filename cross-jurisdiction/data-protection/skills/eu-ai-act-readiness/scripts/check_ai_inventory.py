#!/usr/bin/env python3
"""Check the structure and completeness of an EU AI Act inventory CSV.

This dependency-free tool does not verify facts or make legal classifications.
It reports IDs, missing fields, vocabulary/date issues, staleness heuristics, and
event/keyword signals for manual review against current law and qualified counsel.
"""

from __future__ import annotations

import argparse
from collections import Counter
import csv
from datetime import date, datetime
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
import tempfile
from typing import Any, Iterable


REQUIRED_COLUMNS = (
    "system_id",
    "system_name",
    "owner",
    "business_purpose",
    "lifecycle_status",
    "jurisdictions",
    "eu_nexus",
    "operator_roles",
    "affected_groups",
    "vendor_or_model",
    "system_version",
    "model_version",
    "use_case_screen",
    "foreseeable_misuse",
    "material_modifications",
    "degree_of_automation",
    "human_oversight",
    "launch_date",
    "last_assessed",
    "reassessment_triggers",
    "trigger_events_since_last_assessment",
    "risk_status",
    "classification_basis",
    "classification_confidence",
    "article_50_status",
    "evidence_links",
    "counsel_status",
)
ALLOWED_EU_NEXUS = {"yes", "no", "unknown", "pending"}
ALLOWED_ROLES = {
    "provider",
    "deployer",
    "importer",
    "distributor",
    "product-manufacturer",
    "authorised-representative",
    "gpai-provider",
    "unknown",
    "pending",
}
ALLOWED_RISK = {
    "pending",
    "potential-prohibited",
    "potential-high-risk-annex-i",
    "potential-high-risk-annex-iii",
    "article-50-review",
    "gpai-review",
    "other-or-minimal-risk",
    "potentially-out-of-scope",
}
ALLOWED_LIFECYCLE = {"idea", "pilot", "development", "live", "paused", "retired", "unknown"}
ALLOWED_USE_CASE_SCREEN = {"not-screened", "pending", "screened-no-escalation", "escalation-required"}
ALLOWED_CONFIDENCE = {"unknown", "low", "medium", "high"}
ALLOWED_MATERIAL_MODIFICATIONS = {"none-known", "pending-review", "identified", "unknown"}
ALLOWED_AUTOMATION = {"assistive", "decision-support", "partially-automated", "fully-automated", "unknown"}
ALLOWED_ARTICLE_50_STATUS = {
    "not-assessed",
    "pending-fact-review",
    "potentially-applicable",
    "controls-documented-not-tested",
    "controls-tested-by-owner",
    "not-applicable-basis-pending-counsel",
}
ALLOWED_COUNSEL_STATUS = {
    "not-reviewed",
    "review-requested",
    "in-review",
    "counsel-reviewed",
    "not-applicable-pending-basis",
}
ALLOWED_TRIGGER_EVENTS = {
    "none-known",
    "new-use",
    "model-or-system-version-change",
    "vendor-change",
    "geography-change",
    "role-change",
    "material-modification",
    "incident",
    "legal-update",
    "unknown",
}
REVIEW_SIGNALS: dict[str, tuple[str, ...]] = {
    "article_5_review": (
        r"social scor", r"subliminal", r"manipulat", r"exploit(?:ing)? vulnerab",
        r"emotion recognition", r"biometric categor", r"facial (?:image )?scrap",
        r"predict(?:ive|ing) polic", r"real[- ]time remote biometric",
        r"non[- ]consensual (?:sexual|intimate)", r"nudif", r"child sexual abuse",
    ),
    "annex_iii_or_rights_review": (
        r"recruit", r"hiring", r"resume", r"employee", r"promotion", r"termination",
        r"education", r"admission", r"exam", r"student", r"credit", r"loan",
        r"insurance", r"benefit", r"emergency dispatch", r"critical infrastructure",
        r"law enforcement", r"migration", r"asylum", r"border", r"judge", r"court",
        r"vot(?:e|ing|er)", r"election", r"biometric",
    ),
    "article_50_review": (
        r"chatbot", r"virtual assistant", r"interact(?:s|ion)? with (?:a )?(?:person|human)",
        r"synthetic (?:audio|image|video|text|content)", r"deep ?fake",
        r"emotion recognition", r"biometric categor", r"public interest",
    ),
    "gpai_review": (
        r"general[- ]purpose (?:ai|model)", r"foundation model", r"base model",
        r"model provider", r"pretrain", r"training content",
    ),
}


class OutputPathError(Exception):
    """Raised when a report destination could overwrite the inventory."""


def lexical_path(path: Path) -> Path:
    return Path(os.path.abspath(os.path.normpath(os.fspath(path))))


def resolved_path(path: Path) -> Path:
    try:
        return path.resolve(strict=False)
    except (OSError, RuntimeError) as exc:
        raise OutputPathError(f"cannot resolve path safely: {path}: {exc}") from exc


def validate_output_path(output: Path, inputs: Iterable[Path]) -> Path:
    output_lexical = lexical_path(output)
    output_resolved = resolved_path(output)
    try:
        output_stat = output.lstat()
    except FileNotFoundError:
        output_exists = False
    except OSError as exc:
        raise OutputPathError(f"cannot inspect output path: {output}: {exc}") from exc
    else:
        output_exists = True
        if not stat.S_ISREG(output_stat.st_mode):
            raise OutputPathError(f"output exists and is not a regular file: {output}")

    for source in inputs:
        if output_lexical == lexical_path(source) or output_resolved == resolved_path(source):
            raise OutputPathError(f"output aliases an input path: {output}")
        if output_exists and source.exists():
            try:
                if os.path.samefile(output, source):
                    raise OutputPathError(f"output aliases an input inode: {output}")
            except OutputPathError:
                raise
            except OSError as exc:
                raise OutputPathError(
                    f"cannot safely compare output and input paths: {output}: {exc}"
                ) from exc

    parent = output_lexical.parent
    if not parent.exists():
        raise OutputPathError(f"output directory does not exist: {parent}")
    if not parent.is_dir():
        raise OutputPathError(f"output parent is not a directory: {parent}")
    return output_resolved


def atomic_write_text(output: Path, payload: str, inputs: Iterable[Path]) -> None:
    input_paths = tuple(inputs)
    destination = validate_output_path(output, input_paths)
    parent = destination.parent
    temp_path: Path | None = None
    try:
        file_descriptor, temp_name = tempfile.mkstemp(
            prefix=f".{output.name}.", suffix=".tmp", dir=parent
        )
        temp_path = Path(temp_name)
        with os.fdopen(file_descriptor, "w", encoding="utf-8", newline="") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        destination = validate_output_path(output, input_paths)
        if destination.parent != parent:
            raise OutputPathError(f"output directory changed during write: {output.parent}")
        os.replace(temp_path, destination)
        temp_path = None
    except OutputPathError:
        raise
    except OSError as exc:
        raise OutputPathError(f"unable to write output atomically: {output}: {exc}") from exc
    finally:
        if temp_path is not None:
            try:
                temp_path.unlink()
            except FileNotFoundError:
                pass
            except OSError:
                pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_iso_date(value: str) -> date | None:
    try:
        return datetime.strptime(value.strip(), "%Y-%m-%d").date()
    except ValueError:
        return None


def split_values(value: str) -> set[str]:
    return {part.strip().lower() for part in re.split(r"[;,|]", value) if part.strip()}


def record_signals(row: dict[str, str]) -> list[str]:
    searchable = " ".join(
        row.get(field, "")
        for field in (
            "business_purpose", "affected_groups", "vendor_or_model", "use_case_screen",
            "foreseeable_misuse", "material_modifications", "degree_of_automation",
            "human_oversight", "classification_basis",
        )
    ).lower()
    signals: list[str] = []
    for category, patterns in REVIEW_SIGNALS.items():
        if any(re.search(pattern, searchable, re.I) for pattern in patterns):
            signals.append(category)
    return signals


def vocabulary_issue(row: dict[str, str], field: str, allowed: set[str]) -> str | None:
    value = row.get(field, "").strip().lower()
    if value and value not in allowed:
        return f"{field}={value!r}"
    return None


def inspect_row(row: dict[str, str], as_of: date, stale_after_days: int) -> dict[str, Any]:
    system_id = row.get("system_id", "").strip() or "<missing-system-id>"
    gaps = [column for column in REQUIRED_COLUMNS if not row.get(column, "").strip()]
    vocabulary_issues = [
        issue for issue in (
            vocabulary_issue(row, "eu_nexus", ALLOWED_EU_NEXUS),
            vocabulary_issue(row, "lifecycle_status", ALLOWED_LIFECYCLE),
            vocabulary_issue(row, "risk_status", ALLOWED_RISK),
            vocabulary_issue(row, "use_case_screen", ALLOWED_USE_CASE_SCREEN),
            vocabulary_issue(row, "classification_confidence", ALLOWED_CONFIDENCE),
            vocabulary_issue(row, "material_modifications", ALLOWED_MATERIAL_MODIFICATIONS),
            vocabulary_issue(row, "degree_of_automation", ALLOWED_AUTOMATION),
            vocabulary_issue(row, "article_50_status", ALLOWED_ARTICLE_50_STATUS),
            vocabulary_issue(row, "counsel_status", ALLOWED_COUNSEL_STATUS),
        ) if issue
    ]
    roles = split_values(row.get("operator_roles", ""))
    invalid_roles = sorted(roles - ALLOWED_ROLES)
    if invalid_roles:
        vocabulary_issues.append("operator_roles=" + ",".join(invalid_roles))

    events = split_values(row.get("trigger_events_since_last_assessment", ""))
    invalid_events = sorted(events - ALLOWED_TRIGGER_EVENTS)
    if invalid_events:
        vocabulary_issues.append("trigger_events_since_last_assessment=" + ",".join(invalid_events))
    if "none-known" in events and len(events) > 1:
        vocabulary_issues.append("trigger_events_since_last_assessment='none-known' cannot be combined")

    date_issues: list[str] = []
    for field in ("launch_date", "last_assessed"):
        value = row.get(field, "").strip()
        if value and parse_iso_date(value) is None:
            date_issues.append(f"{field} must use YYYY-MM-DD")
    last_assessed = parse_iso_date(row.get("last_assessed", ""))
    age_days = (as_of - last_assessed).days if last_assessed else None
    if age_days is not None and age_days < 0:
        date_issues.append("last_assessed is after the assessment date")
    stale_by_age = age_days is not None and age_days > stale_after_days
    event_reassessment_due = bool(events - {"none-known"})
    material_modification = row.get("material_modifications", "").strip().lower()
    if material_modification == "identified":
        event_reassessment_due = True

    reassessment_reasons: list[str] = []
    if last_assessed is None:
        reassessment_reasons.append("last_assessed missing or invalid")
    if stale_by_age:
        reassessment_reasons.append(f"administrative age threshold exceeded ({stale_after_days} days)")
    if events - {"none-known"}:
        reassessment_reasons.append("post-assessment trigger event recorded")
    if material_modification == "identified" and "material-modification" not in events:
        reassessment_reasons.append("material modification identified but not listed as a trigger event")

    signals = record_signals(row)
    eu_nexus = row.get("eu_nexus", "").strip().lower()
    risk_status = row.get("risk_status", "").strip().lower()
    if eu_nexus == "no" and signals:
        signals.append("confirm_eu_nexus_before_dismissing_signals")
    if row.get("lifecycle_status", "").strip().lower() == "live" and risk_status in {"", "pending"}:
        signals.append("live_system_with_pending_risk_status")
    counsel_status = row.get("counsel_status", "").strip().lower()
    if counsel_status in {"", "not-reviewed", "review-requested", "in-review"} and risk_status.startswith("potential-"):
        signals.append("potential_high_impact_status_needs_counsel_review")
    if event_reassessment_due:
        signals.append("event_triggered_reassessment_due")

    return {
        "system_id": system_id,
        "structural_completeness": {
            "missing_required_fields": gaps,
            "controlled_vocabulary_issues": vocabulary_issues,
            "date_format_or_sequence_issues": date_issues,
        },
        "assessment_age_days": age_days,
        "age_staleness_threshold_days": stale_after_days,
        "assessment_stale_by_administrative_age_threshold": stale_by_age,
        "event_triggered_reassessment_due": event_reassessment_due,
        "reassessment_reasons": reassessment_reasons,
        "manual_review_signals": sorted(set(signals)),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inventory", type=Path, help="CSV inventory using the bundled template headers")
    parser.add_argument("--as-of", required=True, help="Assessment date in YYYY-MM-DD format")
    parser.add_argument(
        "--stale-after-days", type=int, default=365,
        help="Administrative age flag; not a statutory deadline (default: 365)",
    )
    parser.add_argument(
        "--output", type=Path,
        help="Atomically write JSON to a regular file; inventory aliases are refused",
    )
    parser.add_argument("--pretty", action="store_true", help="Indent JSON output")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    as_of = parse_iso_date(args.as_of)
    if as_of is None:
        print("error: --as-of must use YYYY-MM-DD", file=sys.stderr)
        return 2
    if args.stale_after_days < 1:
        print("error: --stale-after-days must be at least 1", file=sys.stderr)
        return 2
    if not args.inventory.is_file():
        print(f"error: file does not exist: {args.inventory}", file=sys.stderr)
        return 2
    if args.output:
        try:
            validate_output_path(args.output, [args.inventory])
        except OutputPathError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
    try:
        with args.inventory.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            headers = reader.fieldnames or []
            missing_columns = [column for column in REQUIRED_COLUMNS if column not in headers]
            extra_columns = [column for column in headers if column not in REQUIRED_COLUMNS]
            duplicate_columns = sorted(name for name, count in Counter(headers).items() if count > 1)
            records = [inspect_row(row, as_of, args.stale_after_days) for row in reader]
    except (OSError, UnicodeDecodeError, csv.Error) as exc:
        print(f"error: unable to read inventory: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2

    ids = [record["system_id"] for record in records if record["system_id"] != "<missing-system-id>"]
    duplicate_ids = sorted(system_id for system_id, count in Counter(ids).items() if count > 1)
    structurally_complete_records = sum(
        not record["structural_completeness"]["missing_required_fields"]
        and not record["structural_completeness"]["controlled_vocabulary_issues"]
        and not record["structural_completeness"]["date_format_or_sequence_issues"]
        for record in records
    )
    report = {
        "inventory_path": str(args.inventory.resolve()),
        "sha256": sha256(args.inventory),
        "as_of": as_of.isoformat(),
        "scope_label": "structural/completeness screening only—not semantic fact verification or legal verification",
        "method": "CSV schema, field presence, controlled vocabulary, date, age-staleness, event-trigger, and keyword checks only",
        "columns": {
            "missing_required": missing_columns,
            "unexpected_extra": extra_columns,
            "duplicate_headers": duplicate_columns,
        },
        "summary": {
            "records": len(records),
            "records_without_structural_vocabulary_or_date_issues": structurally_complete_records,
            "duplicate_system_ids": duplicate_ids,
            "records_with_manual_review_signals": sum(bool(record["manual_review_signals"]) for record in records),
            "records_stale_by_administrative_age_threshold": sum(
                record["assessment_stale_by_administrative_age_threshold"] for record in records
            ),
            "records_with_event_triggered_reassessment_due": sum(
                record["event_triggered_reassessment_due"] for record in records
            ),
        },
        "controlled_vocabularies": {
            "article_50_status": sorted(ALLOWED_ARTICLE_50_STATUS),
            "counsel_status": sorted(ALLOWED_COUNSEL_STATUS),
            "trigger_events_since_last_assessment": sorted(ALLOWED_TRIGGER_EVENTS),
        },
        "records": records,
        "limitations": [
            "Passing structural checks does not verify that inventory facts, evidence, classifications, controls, or legal conclusions are correct.",
            "The age threshold is an administrative prompt, not an AI Act deadline; a relevant event can require reassessment immediately regardless of age.",
            "Keyword signals can be false positives and omissions; manually assess actual intended use, foreseeable misuse, operation, jurisdiction, and version.",
            "The tool does not determine territorial scope, operator role, prohibited status, risk class, exemption, obligation, or deadline.",
            "Verify current official EU and Member State sources and obtain qualified legal review.",
            "System IDs and invalid controlled-vocabulary values may be emitted to locate gaps; other source row values are not copied into the report.",
        ],
    }
    payload = json.dumps(report, indent=2 if args.pretty else None, sort_keys=True) + "\n"
    if args.output:
        try:
            validate_output_path(args.output, [args.inventory])
            atomic_write_text(args.output, payload, [args.inventory])
        except OutputPathError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
    else:
        sys.stdout.write(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
