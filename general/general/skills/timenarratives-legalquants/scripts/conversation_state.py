"""Bind conversation evidence eligibility to ordered message provenance."""

from __future__ import annotations

from conversation_units import message_locator, message_state
from packet_core import parse_time


def conversation_state_faults(packet: dict) -> list[dict[str, str]]:
    faults: list[dict[str, str]] = []

    def fault(path: str) -> None:
        faults.append({"code": "invalid_conversation_state", "path": path})

    containers = {row["containerId"]: row for row in packet["containers"]}
    parts = {row["partId"]: row for row in packet["parts"]}
    units = {row["unitId"]: row for row in packet["units"]}
    for root in packet["roots"]:
        container = containers.get(root["containerId"], {})
        if (root["kind"] == "conversation") != (
            container.get("sourceType") == "conversation"
        ):
            fault(f"$packet.roots.{root['rootId']}.kind")
    for container_id, container in containers.items():
        is_conversation = container["sourceType"] == "conversation"
        metadata = container.get("conversation")
        if not is_conversation:
            if metadata is not None:
                fault(f"$packet.containers.{container_id}.conversation")
            continue
        path = f"$packet.containers.{container_id}"
        if metadata is None:
            if container["disposition"] not in {"unreadable", "exactDuplicate"}:
                fault(path)
            continue
        if container["parentContainerId"] is not None:
            fault(path + ".parentContainerId")
        for bound in ("since", "until"):
            if parse_time(metadata["scope"][bound], bound, nullable=True) != parse_time(
                packet["filters"][bound], bound, nullable=True
            ):
                fault(path + ".conversation.scope")
        owned = [
            part for part in packet["parts"] if part["containerId"] == container_id
        ]
        indices = [part.get("conversationMessage", {}).get("index") for part in owned]
        ids = [part.get("conversationMessage", {}).get("messageId") for part in owned]
        if indices != list(range(len(owned))) or len(ids) != len(set(ids)):
            fault(path + ".messages")
        for part in owned:
            _check_message(part, metadata, packet["filters"], units, fault)
    for part in packet["parts"]:
        container = containers.get(part["containerId"], {})
        if (
            "conversationMessage" in part
            and container.get("sourceType") != "conversation"
        ):
            fault(f"$packet.parts.{part['partId']}.conversationMessage")
    for unit in packet["units"]:
        container = containers.get(unit["containerId"], {})
        is_conversation = container.get("sourceType") == "conversation"
        if is_conversation != (unit["kind"] == "conversation_message"):
            fault(f"$packet.units.{unit['unitId']}.kind")
        if is_conversation:
            part = parts.get(unit["originId"])
            if part is None or "conversationMessage" not in part:
                fault(f"$packet.units.{unit['unitId']}.originId")
    return faults


def _check_message(
    part: dict, snapshot: dict, filters: dict, units: dict, fault
) -> None:
    path = f"$packet.parts.{part['partId']}"
    metadata = part.get("conversationMessage")
    if metadata is None:
        fault(path + ".conversationMessage")
        return
    locator = message_locator(snapshot["conversationId"], metadata)
    disposition, eligibility, reason = message_state(
        metadata, snapshot["origin"], filters
    )
    expected = {
        "locator": locator,
        "disposition": disposition,
        "reason": reason or None,
        "role": "conversation_user" if metadata["role"] == "user" else "context",
    }
    for key, value in expected.items():
        if part[key] != value:
            fault(path + "." + key)
    offset = 0
    for unit_id in part["unitIds"]:
        unit = units.get(unit_id)
        if unit is None:
            continue  # The shared provenance-edge gate reports missing unit IDs.
        expected_unit = {
            "eligibility": eligibility,
            "role": "current"
            if eligibility in {"eligible", "requires_confirmation"}
            else "context",
            "sourceClass": "documentary_supported",
            "assertedByActorId": None,
            "sourceAuthor": metadata["author"],
            "sourceTime": metadata["timestamp"],
            "originId": part["partId"],
            "containerId": part["containerId"],
            "coverageDisposition": "excluded"
            if disposition == "excluded"
            else "pending",
            "utf8Start": offset,
            "locator": f"{locator}#utf8={unit['utf8Start']}:{unit['utf8End']}",
        }
        for key, value in expected_unit.items():
            if unit[key] != value:
                fault(f"$packet.units.{unit_id}.{key}")
        offset = unit["utf8End"]
