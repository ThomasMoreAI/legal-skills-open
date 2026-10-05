"""Pure derivation of TimeNarratives output and coverage receipt."""

from __future__ import annotations

import re
from typing import Any

from exception_ledger import build_exception_ledger, validate_exception_ledger
from narrative_contract import narrative_text_faults
from packet_semantics import packet_has_unresolved_state
from prohibited_output import scan_text

QUESTION_REASONS = {
    "actor_unclear",
    "matter_unclear",
    "action_unclear",
    "object_unclear",
    "source_unsupported",
    "source_unreadable",
    "source_partially_read",
}
IDENTIFIER = re.compile(r"^[A-Za-z][A-Za-z0-9._-]{0,127}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
CONFIRMATION_TOKEN = re.compile(r"^TN-[0-9a-f]{16}$")
COUNT_KEYS = {
    "selectedRoots",
    "containers",
    "mimeLeaves",
    "parts",
    "units",
    "accountedUnits",
    "analyzableUnits",
    "assessedUnits",
    "usedUnits",
    "needsConfirmationUnits",
    "events",
    "workstreams",
    "narratives",
    "packetErrors",
    "packetLimitations",
    "exceptionLedgerItems",
}


def _issue(code: str, path: str) -> dict[str, str]:
    return {"code": code, "path": path}


def _closed_record(
    value: Any, keys: set[str], path: str, out: list[dict[str, str]]
) -> bool:
    if not isinstance(value, dict):
        out.append(_issue("expected_object", path))
        return False
    for key in sorted(keys - set(value)):
        out.append(_issue("missing_field", f"{path}.{key}"))
    for key in sorted(set(value) - keys):
        out.append(_issue("unknown_field", f"{path}.{key}"))
    return keys <= set(value)


def _valid_id(value: Any) -> bool:
    return isinstance(value, str) and IDENTIFIER.fullmatch(value) is not None


def _validate_narratives(value: Any, out: list[dict[str, str]]) -> None:
    if not isinstance(value, list):
        out.append(_issue("expected_array", "$.narratives"))
        return
    keys = {"workstreamId", "text", "eventIds", "supportClass"}
    for index, row in enumerate(value):
        path = f"$.narratives[{index}]"
        if not _closed_record(row, keys, path, out):
            continue
        if not _valid_id(row["workstreamId"]):
            out.append(_issue("invalid_id", f"{path}.workstreamId"))
        text = row["text"]
        for code in narrative_text_faults(text):
            out.append(_issue(code, f"{path}.text"))
        event_ids = row["eventIds"]
        if (
            not isinstance(event_ids, list)
            or not event_ids
            or any(not _valid_id(item) for item in event_ids)
            or len(set(event_ids)) != len(event_ids)
        ):
            out.append(_issue("expected_id_array", f"{path}.eventIds"))
        if row["supportClass"] not in {
            "documentary_supported",
            "user_attested",
        }:
            out.append(_issue("invalid_enum", f"{path}.supportClass"))


def _validate_questions(value: Any, out: list[dict[str, str]]) -> None:
    if not isinstance(value, list):
        out.append(_issue("expected_array", "$.checkQuestions"))
        return
    for index, row in enumerate(value):
        path = f"$.checkQuestions[{index}]"
        if not _closed_record(row, {"unitId", "reason", "source"}, path, out):
            continue
        if not _valid_id(row["unitId"]):
            out.append(_issue("invalid_id", f"{path}.unitId"))
        if row["reason"] not in QUESTION_REASONS:
            out.append(_issue("invalid_enum", f"{path}.reason"))
        source = row["source"]
        if not isinstance(source, str) or not source.strip() or len(source) > 256:
            out.append(_issue("invalid_source_label", f"{path}.source"))


def _validate_nonnegative_counts(
    value: Any, keys: set[str], path: str, out: list[dict[str, str]]
) -> None:
    if not _closed_record(value, keys, path, out):
        return
    for key in keys:
        count = value[key]
        if isinstance(count, bool) or not isinstance(count, int) or count < 0:
            out.append(_issue("invalid_integer", f"{path}.{key}"))


def validate_deliverable_structure(value: dict[str, Any]) -> list[dict[str, str]]:
    """Validate nested deliverable fields without a JSON Schema dependency."""
    out: list[dict[str, str]] = []
    if value.get("schemaVersion") != "timenarratives.deliverable.v1":
        out.append(_issue("schema_version", "$.schemaVersion"))
    if not _valid_id(value.get("runId")):
        out.append(_issue("invalid_id", "$.runId"))
    if value.get("status") not in {
        "ready_for_user_review",
        "partial_withheld",
        "no_supported_activity",
        "incomplete",
    }:
        out.append(_issue("invalid_enum", "$.status"))
    _validate_narratives(value.get("narratives"), out)
    _validate_questions(value.get("checkQuestions"), out)
    receipt = value.get("receipt")
    receipt_keys = {
        "packetDigest",
        "mapDigest",
        "confirmationToken",
        "packetScope",
        "packetReconciliation",
        "workdayCompleteness",
        "postingState",
        "counts",
        "supportCounts",
        "exceptionLedger",
    }
    if not _closed_record(receipt, receipt_keys, "$.receipt", out):
        return out
    assert isinstance(receipt, dict)
    for key in ("packetDigest", "mapDigest"):
        value_at_key = receipt[key]
        if not isinstance(value_at_key, str) or SHA256.fullmatch(value_at_key) is None:
            out.append(_issue("invalid_sha256", f"$.receipt.{key}"))
    token = receipt["confirmationToken"]
    if not isinstance(token, str) or CONFIRMATION_TOKEN.fullmatch(token) is None:
        out.append(_issue("confirmation_token", "$.receipt.confirmationToken"))
    constants = {
        "packetScope": "expressly_selected_only",
        "packetReconciliation": "complete",
        "workdayCompleteness": "not_assessed",
        "postingState": "unposted_draft",
    }
    for key, expected in constants.items():
        if receipt[key] != expected:
            out.append(_issue("invalid_const", f"$.receipt.{key}"))
    _validate_nonnegative_counts(receipt["counts"], COUNT_KEYS, "$.receipt.counts", out)
    _validate_nonnegative_counts(
        receipt["supportCounts"],
        {"documentarySupported", "userAttested"},
        "$.receipt.supportCounts",
        out,
    )
    out.extend(validate_exception_ledger(receipt["exceptionLedger"], receipt["counts"]))
    return out


def _assessable_count(packet: dict[str, Any]) -> int:
    return sum(
        1
        for unit in packet.get("units", [])
        if unit.get("coverageDisposition") == "pending"
        and unit.get("eligibility") in {"eligible", "requires_confirmation"}
    )


def _status(packet: dict[str, Any], mapping: dict[str, Any]) -> str:
    assessments = mapping["unitAssessment"]
    has_questions = any(
        row["disposition"] == "needs_confirmation" for row in assessments
    )
    limited = packet_has_unresolved_state(packet)
    events = mapping["events"]
    if events:
        return (
            "partial_withheld" if has_questions or limited else "ready_for_user_review"
        )
    return "incomplete" if has_questions or limited else "no_supported_activity"


def _narratives(
    mapping: dict[str, Any], event_support: dict[str, str]
) -> list[dict[str, Any]]:
    by_workstream = {row["workstreamId"]: row for row in mapping["clauses"]}
    narratives: list[dict[str, Any]] = []
    for workstream in mapping["workstreams"]:
        clause = by_workstream[workstream["workstreamId"]]
        classes = {event_support[event_id] for event_id in clause["eventIds"]}
        support = (
            "user_attested" if "user_attested" in classes else "documentary_supported"
        )
        narratives.append(
            {
                "workstreamId": workstream["workstreamId"],
                "text": clause["text"],
                "eventIds": clause["eventIds"],
                "supportClass": support,
            }
        )
    return narratives


def _safe_label(container_id: str, display_name: Any) -> str:
    """A file name may carry prohibited tokens; fall back to the container id."""
    if not isinstance(display_name, str) or not display_name.strip():
        return container_id
    return container_id if scan_text(display_name, "$label") else display_name


def _source_labels(packet: dict[str, Any]) -> dict[str, str]:
    """Unit id -> the selected file's display name (never a path or excerpt)."""
    containers = {
        row["containerId"]: _safe_label(row["containerId"], row.get("displayName"))
        for row in packet.get("containers", [])
        if isinstance(row, dict) and isinstance(row.get("containerId"), str)
    }
    return {
        unit["unitId"]: containers.get(unit["containerId"], unit["containerId"])
        for unit in packet.get("units", [])
        if isinstance(unit, dict) and isinstance(unit.get("unitId"), str)
    }


def build_deliverable(
    packet: dict[str, Any],
    mapping: dict[str, Any],
    confirmation: dict[str, Any],
    event_support: dict[str, str],
    map_digest: str,
) -> dict[str, Any]:
    narratives = _narratives(mapping, event_support)
    exception_ledger = build_exception_ledger(packet, mapping)
    labels = _source_labels(packet)
    questions = [
        {
            "unitId": row["unitId"],
            "reason": row["reason"],
            "source": labels.get(row["unitId"], row["unitId"]),
        }
        for row in mapping["unitAssessment"]
        if row["disposition"] == "needs_confirmation"
        and row["reason"] in QUESTION_REASONS
    ]
    support_counts = {
        "documentarySupported": sum(
            value == "documentary_supported" for value in event_support.values()
        ),
        "userAttested": sum(
            value == "user_attested" for value in event_support.values()
        ),
    }
    assessments = mapping["unitAssessment"]
    counts = {
        "selectedRoots": len(packet.get("roots", [])),
        "containers": len(packet.get("containers", [])),
        "mimeLeaves": len(packet.get("mimeLeaves", [])),
        "parts": len(packet.get("parts", [])),
        "units": len(packet.get("units", [])),
        "accountedUnits": len(assessments)
        + sum(row["itemType"] == "unit" for row in exception_ledger),
        "analyzableUnits": _assessable_count(packet),
        "assessedUnits": len(assessments),
        "usedUnits": sum(row["disposition"] == "used" for row in assessments),
        "needsConfirmationUnits": sum(
            row["disposition"] == "needs_confirmation" for row in assessments
        ),
        "events": len(mapping["events"]),
        "workstreams": len(mapping["workstreams"]),
        "narratives": len(narratives),
        "packetErrors": len(packet.get("errors", [])),
        "packetLimitations": len(packet.get("limitations", [])),
        "exceptionLedgerItems": len(exception_ledger),
    }
    return {
        "schemaVersion": "timenarratives.deliverable.v1",
        "runId": packet["runId"],
        "status": _status(packet, mapping),
        "narratives": narratives,
        "checkQuestions": questions,
        "receipt": {
            "packetDigest": packet["packetDigestSha256"],
            "mapDigest": map_digest,
            "confirmationToken": confirmation["confirmationToken"],
            "packetScope": "expressly_selected_only",
            "packetReconciliation": "complete",
            "workdayCompleteness": "not_assessed",
            "postingState": "unposted_draft",
            "counts": counts,
            "supportCounts": support_counts,
            "exceptionLedger": exception_ledger,
        },
    }
