"""Adapt the strict DOCX parser result into packet dispositions."""

from __future__ import annotations

from typing import Any

from packet_filters import apply_selected_source_filter

DOCX_STATUSES = {"ready", "partial", "unreadable"}


def _mark_unreadable(container: dict, root: dict, reason: str) -> None:
    container.update(disposition="unreadable", reason=reason)
    root.update(disposition="unreadable", reason=reason)


def _valid_inventory(parsed: Any) -> bool:
    if not isinstance(parsed, dict) or parsed.get("disposition") not in DOCX_STATUSES:
        return False
    parts = parsed.get("parts")
    units = parsed.get("units")
    list_keys = ("limitations", "notes", "affectedParts")
    string_lists = [parsed.get(key) for key in list_keys]
    return (
        isinstance(parts, list)
        and all(
            isinstance(part, dict) and isinstance(part.get("unitIds"), list)
            for part in parts
        )
        and isinstance(units, list)
        and all(
            isinstance(unit, dict) and "assertedByActorId" in unit for unit in units
        )
        and all(
            isinstance(values, list) and all(isinstance(item, str) for item in values)
            for values in string_lists
        )
    )


def parse_docx_for_packet(
    data: bytes, container: dict, root: dict, filters: dict
) -> dict[str, list]:
    try:
        from docx_units import parse_docx  # type: ignore[import-not-found]
    except ImportError:
        _mark_unreadable(container, root, "docx_parser_unavailable")
        return {
            "parts": [],
            "units": [],
            "errors": ["docx_parser_unavailable"],
            "limitations": [],
        }
    try:
        parsed = parse_docx(data, container["containerId"])
    except Exception:  # parser boundary: never expose selected source content
        _mark_unreadable(container, root, "docx_parse_failed")
        return {
            "parts": [],
            "units": [],
            "errors": ["docx_parse_failed"],
            "limitations": [],
        }
    if not _valid_inventory(parsed):
        _mark_unreadable(container, root, "docx_parser_status_invalid")
        return {
            "parts": [],
            "units": [],
            "errors": ["docx_parser_status_invalid"],
            "limitations": [],
        }
    container.update(
        sourceTime=parsed.get("sourceTime"),
        sourceTimeKind=parsed.get("sourceTimeKind"),
        sourceAuthor=parsed.get("sourceAuthor"),
    )
    status = parsed["disposition"]
    reason = parsed.get("reason")
    result = {
        "parts": parsed["parts"],
        "units": parsed["units"],
        "errors": [],
        "limitations": parsed["limitations"],
    }
    if status == "unreadable":
        _mark_unreadable(container, root, reason or "docx_unreadable")
        result["errors"].append("docx_unreadable")
        return result
    if not apply_selected_source_filter(container, root, filters):
        result["parts"] = []
        result["units"] = []
        return result
    affected = set(parsed["affectedParts"])
    if status == "partial":
        container.update(
            disposition="requiresConfirmation", reason=reason or "docx_partial"
        )
        root.update(disposition="requiresConfirmation", reason=reason or "docx_partial")
        result["errors"].append("docx_partial")
    for unit in result["units"]:
        part = (unit.get("metadata") or {}).get("partName")
        downgrade = (status == "partial" and part in affected) or (
            container["filterDisposition"] == "filter_indeterminate"
        )
        if downgrade and unit["eligibility"] == "eligible":
            unit["eligibility"] = "requires_confirmation"
    return result
