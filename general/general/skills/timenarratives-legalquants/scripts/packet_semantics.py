"""Semantic compiler-state gates beyond structural packet validity."""

from __future__ import annotations

from typing import Any

from conversation_state import conversation_state_faults

Issue = dict[str, str]
CAP_ERRORS = frozenset(
    {
        "selected_container_bytes_exceeded",
        "selected_packet_bytes_exceeded",
        "derived_container_cap_exceeded",
        "terminal_unit_cap_exceeded",
        "model_visible_budget_exceeded",
    }
)


def _issue(code: str, path: str) -> Issue:
    return {"code": code, "path": path}


def _inventories(packet: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    roots = {
        row["rootId"]: row
        for row in packet["roots"]
        if isinstance(row, dict) and isinstance(row.get("rootId"), str)
    }
    containers = {
        row["containerId"]: row
        for row in packet["containers"]
        if isinstance(row, dict) and isinstance(row.get("containerId"), str)
    }
    return roots, containers


def _note_state_faults(packet: dict[str, Any]) -> list[Issue]:
    out: list[Issue] = []
    actor = packet["actor"]
    roots, containers = _inventories(packet)
    note_units: set[str] = set()
    for index, unit in enumerate(packet["units"]):
        path = f"$packet.units[{index}]"
        markers = (
            unit["kind"] == "user_note",
            unit["sourceClass"] == "user_attested",
            unit["role"] == "attested",
        )
        if not any(markers):
            container = containers.get(unit["containerId"])
            if unit["assertedByActorId"] is not None or (
                container is not None and container["sourceType"] == "user_note"
            ):
                out.append(_issue("invalid_user_note_state", path))
            continue
        container = containers.get(unit["containerId"])
        root = roots.get(container["rootId"]) if container is not None else None
        valid = all(markers) and (
            unit["eligibility"] == "requires_confirmation"
            and unit["assertedByActorId"] == actor["id"]
            and unit["sourceAuthor"] == actor["name"]
            and unit["originId"] == unit["containerId"]
            and container is not None
            and container["sourceType"] == "user_note"
            and container["sourceAuthor"] is None
            and container["disposition"] == "requiresConfirmation"
            and container["reason"] == "user_attestation"
            and root is not None
            and root["kind"] == "user_note"
            and root["selectedPath"] is None
            and root["disposition"] == "requiresConfirmation"
        )
        if not valid:
            out.append(_issue("invalid_user_note_state", path))
        if container is not None:
            note_units.add(container["containerId"])
    for index, container in enumerate(packet["containers"]):
        if (container["sourceType"] == "user_note") != (
            container["containerId"] in note_units
        ):
            out.append(
                _issue("invalid_user_note_state", f"$packet.containers[{index}]")
            )
    for index, root in enumerate(packet["roots"]):
        expected = root["containerId"] in note_units
        if (root["kind"] == "user_note") != expected:
            out.append(_issue("invalid_user_note_state", f"$packet.roots[{index}]"))
    return out


def validate_packet_semantic_state(packet: dict[str, Any]) -> list[Issue]:
    out = _note_state_faults(packet)
    out.extend(conversation_state_faults(packet))
    if packet["budget"]["withinLimit"] is False:
        out.append(_issue("packet_budget_exceeded", "$packet.budget.withinLimit"))
    for index, code in enumerate(packet["errors"]):
        if code in CAP_ERRORS:
            out.append(_issue("packet_cap_exceeded", f"$packet.errors[{index}]"))
    return out


def packet_has_unresolved_state(packet: dict[str, Any]) -> bool:
    if packet["errors"] or packet["limitations"] or packet["status"] == "incomplete":
        return True
    layouts = (
        ("roots", "kind"),
        ("containers", "sourceType"),
        ("mimeLeaves", None),
        ("parts", None),
    )
    return any(
        row["disposition"] == "requiresConfirmation"
        and (note_key is None or row[note_key] != "user_note")
        for field, note_key in layouts
        for row in packet[field]
    )
