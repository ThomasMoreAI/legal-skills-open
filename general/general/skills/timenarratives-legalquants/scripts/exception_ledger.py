"""Deterministic, redacted TimeNarratives exception-ledger derivation."""

from __future__ import annotations

import re
from typing import Any

Issue = dict[str, str]
SAFE_VALUE = re.compile(r"^[A-Za-z][A-Za-z0-9._-]{0,127}$")
ITEM_TYPES = {"root", "container", "mimeLeaf", "part", "unit", "unitAssessment"}
PACKET_EXCEPTIONS = {
    "requiresConfirmation",
    "exactDuplicate",
    "excluded",
    "unreadable",
}
ASSESSMENT_EXCEPTIONS = {
    "read_but_unused",
    "excluded_other_actor",
    "excluded_other_matter",
    "excluded_non_work",
    "needs_confirmation",
}
UNIT_TERMINALS = {
    "context_only",
    "ineligible",
    "excluded",
    "unreadable",
    "exact_duplicate",
}
ALL_DISPOSITIONS = (
    PACKET_EXCEPTIONS
    | ASSESSMENT_EXCEPTIONS
    | UNIT_TERMINALS
    | {"attestation_confirmed"}
)
ENTRY_KEYS = {"itemType", "itemId", "disposition", "reason"}


def _safe_reason(value: Any, fallback: str) -> str:
    if isinstance(value, str) and SAFE_VALUE.fullmatch(value) is not None:
        return value
    return fallback


def _entry(item_type: str, item_id: Any, row: dict[str, Any]) -> dict[str, str]:
    disposition = row.get("disposition")
    assert isinstance(disposition, str)
    return {
        "itemType": item_type,
        "itemId": item_id if isinstance(item_id, str) else "invalidId",
        "disposition": disposition,
        "reason": _safe_reason(row.get("reason"), disposition),
    }


def _attestation_entry(item_type: str, item_id: Any) -> dict[str, str]:
    return {
        "itemType": item_type,
        "itemId": item_id if isinstance(item_id, str) else "invalidId",
        "disposition": "attestation_confirmed",
        "reason": "user_attestation",
    }


def build_exception_ledger(
    packet: dict[str, Any], mapping: dict[str, Any]
) -> list[dict[str, str]]:
    ledger: list[dict[str, str]] = []
    for field, item_type, id_field in (
        ("roots", "root", "rootId"),
        ("containers", "container", "containerId"),
        ("mimeLeaves", "mimeLeaf", "mimeLeafId"),
        ("parts", "part", "partId"),
    ):
        for row in packet.get(field, []):
            if row.get("disposition") in PACKET_EXCEPTIONS:
                is_note = (
                    row.get("kind") == "user_note"
                    or row.get("sourceType") == "user_note"
                )
                ledger.append(
                    _attestation_entry(item_type, row.get(id_field))
                    if row.get("disposition") == "requiresConfirmation" and is_note
                    else _entry(item_type, row.get(id_field), row)
                )
    for row in mapping.get("unitAssessment", []):
        if row.get("disposition") in ASSESSMENT_EXCEPTIONS:
            ledger.append(_entry("unitAssessment", row.get("unitId"), row))
    assessed = {row.get("unitId") for row in mapping.get("unitAssessment", [])}
    for unit in packet.get("units", []):
        if unit.get("unitId") not in assessed:
            disposition = unit.get("coverageDisposition")
            if disposition == "pending":
                disposition = unit.get("eligibility")
            row = {"disposition": disposition, "reason": disposition}
            ledger.append(_entry("unit", unit.get("unitId"), row))
    return ledger


def validate_exception_ledger(value: Any, counts: Any = None) -> list[Issue]:
    if not isinstance(value, list):
        return [{"code": "expected_array", "path": "$.receipt.exceptionLedger"}]
    out: list[Issue] = []
    seen: set[tuple[str, str, str, str]] = set()
    for index, row in enumerate(value):
        path = f"$.receipt.exceptionLedger[{index}]"
        if not isinstance(row, dict):
            out.append({"code": "expected_object", "path": path})
            continue
        for key in sorted(ENTRY_KEYS - set(row)):
            out.append({"code": "missing_field", "path": f"{path}.{key}"})
        for key in sorted(set(row) - ENTRY_KEYS):
            out.append({"code": "unknown_field", "path": f"{path}.{key}"})
        if not ENTRY_KEYS <= set(row):
            continue
        if row["itemType"] not in ITEM_TYPES:
            out.append({"code": "invalid_enum", "path": f"{path}.itemType"})
        if row["disposition"] not in ALL_DISPOSITIONS:
            out.append({"code": "invalid_enum", "path": f"{path}.disposition"})
        for key in ("itemId", "reason"):
            item = row[key]
            if not isinstance(item, str) or SAFE_VALUE.fullmatch(item) is None:
                out.append({"code": "invalid_safe_value", "path": f"{path}.{key}"})
        identity = (
            str(row["itemType"]),
            str(row["itemId"]),
            str(row["disposition"]),
            str(row["reason"]),
        )
        if identity in seen:
            out.append({"code": "duplicate_array_item", "path": path})
        seen.add(identity)
    if isinstance(counts, dict):
        unit_entries = sum(
            row.get("itemType") == "unit" for row in value if isinstance(row, dict)
        )
        if (
            counts.get("accountedUnits") != counts.get("units")
            or counts.get("accountedUnits")
            != counts.get("assessedUnits", 0) + unit_entries
        ):
            out.append(
                {
                    "code": "receipt_arithmetic",
                    "path": "$.receipt.counts.accountedUnits",
                }
            )
    return out
