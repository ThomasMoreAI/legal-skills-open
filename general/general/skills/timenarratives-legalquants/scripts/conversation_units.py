"""Strict, ordered conversation snapshots; source dates are not activity dates.

Snapshots are host-supplied documentary evidence, never authentication. The
selected file remains untouched; message parts hash original UTF-8 bodies while
units use the existing derived newline normalisation. Scope bounds select message
timestamps only. Use null bounds when described activity dates differ from them.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from urllib.parse import quote

from canonical_json import JsonFileError, parse_json_object
from packet_core import PacketBuildError, parse_time
from packet_filters import _filter_source, apply_selected_source_type_filter
from schema_subset import validate_schema_subset
from text_units import TextDecodeError, make_text_units

SCHEMA = json.loads(
    (
        Path(__file__).resolve().parents[1]
        / "schemas"
        / "timenarratives-conversation.schema.json"
    ).read_text(encoding="utf-8")
)


def validate_snapshot(data: bytes, selection: dict, filters: dict) -> dict:
    try:
        snapshot = parse_json_object(data.decode("utf-8", errors="strict"))
    except (JsonFileError, UnicodeDecodeError, RecursionError) as exc:
        raise PacketBuildError("malformed_conversation") from exc
    if validate_schema_subset(snapshot, SCHEMA):
        raise PacketBuildError("malformed_conversation")
    if snapshot["conversationId"] != selection["conversationId"]:
        raise PacketBuildError("conversation_id_mismatch")
    for bound in ("since", "until"):
        if parse_time(snapshot["scope"][bound], bound, nullable=True) != parse_time(
            filters[bound], bound, nullable=True
        ):
            raise PacketBuildError("conversation_scope_mismatch")
    coverage = snapshot["coverage"]
    if (coverage["status"] == "partial") != bool(coverage["gaps"]):
        raise PacketBuildError("conversation_coverage_mismatch")
    ids = [message["messageId"] for message in snapshot["messages"]]
    if len(ids) != len(set(ids)):
        raise PacketBuildError("duplicate_conversation_message")
    try:
        # Reject escaped surrogates/NUL anywhere, including provenance metadata.
        json.dumps(snapshot, ensure_ascii=False).encode("utf-8")
        bodies = [message["text"] for message in snapshot["messages"]]
        if any("\x00" in text for text in bodies + coverage["gaps"]):
            raise PacketBuildError("malformed_conversation")
    except UnicodeEncodeError as exc:
        raise PacketBuildError("malformed_conversation") from exc
    return snapshot


def message_state(message: dict, origin: str, filters: dict) -> tuple[str, str, str]:
    observed = parse_time(message["timestamp"], "timestamp", nullable=True)
    as_of = parse_time(filters["asOf"], "asOf", nullable=False)
    if observed is not None and as_of is not None and observed > as_of:
        return "excluded", "context_only", "source_after_as_of"
    disposition, reason = _filter_source("conversation", message["timestamp"], filters)
    if disposition == "excluded":
        return "excluded", "context_only", reason or "time_filter"
    if origin == "summary" or message["role"] != "user":
        return "ready", "context_only", "conversation_context"
    if disposition == "filter_indeterminate":
        return "requiresConfirmation", "requires_confirmation", "source_time_missing"
    return "ready", "eligible", ""


def message_locator(conversation_id: str, message: dict) -> str:
    return (
        f"conversation:{quote(conversation_id, safe='')}"
        f"/message:{quote(message['messageId'], safe='')}"
        f"/index:{message['index']}/role:{message['role']}"
    )


def _message_records(
    container: dict, message: dict, index: int, filters: dict, unit_start: int
) -> tuple[dict, list[dict]]:
    metadata = {key: value for key, value in message.items() if key != "text"}
    metadata["index"] = index
    snapshot = container["conversation"]
    locator = message_locator(snapshot["conversationId"], metadata)
    disposition, eligibility, reason = message_state(
        message, snapshot["origin"], filters
    )
    part_id = f"{container['containerId']}-M{index + 1:04d}"
    body = message["text"].encode("utf-8")
    units = make_text_units(
        container["containerId"],
        body,
        kind="conversation_message",
        role="current"
        if eligibility in {"eligible", "requires_confirmation"}
        else "context",
        eligibility=eligibility,
        source_author=message["author"],
        source_time=message["timestamp"],
        origin_id=part_id,
        locator_prefix=locator,
        unit_start=unit_start,
    )
    for unit in units:
        unit["assertedByActorId"] = None
        if disposition == "excluded":
            unit["coverageDisposition"] = "excluded"
    part = {
        "partId": part_id,
        "containerId": container["containerId"],
        "locator": locator,
        "mediaType": "text/plain",
        "rawSha256": hashlib.sha256(body).hexdigest(),
        "byteLength": len(body),
        "role": "conversation_user" if message["role"] == "user" else "context",
        "unitIds": [unit["unitId"] for unit in units],
        "disposition": disposition,
        "reason": reason or None,
        "conversationMessage": metadata,
    }
    return part, units


def parse_conversation_for_packet(
    data: bytes, selection: dict, container: dict, root: dict, filters: dict
) -> dict:
    result: dict = {"parts": [], "units": [], "errors": [], "limitations": []}
    try:
        snapshot = validate_snapshot(data, selection, filters)
        container["conversation"] = {
            key: value
            for key, value in snapshot.items()
            if key not in {"schemaVersion", "messages"}
        }
        if not apply_selected_source_type_filter(container, root, filters):
            return result
        for index, message in enumerate(snapshot["messages"]):
            part, units = _message_records(
                container, message, index, filters, len(result["units"]) + 1
            )
            result["parts"].append(part)
            result["units"].extend(units)
        if snapshot["coverage"]["status"] == "partial":
            result["limitations"].append("conversation_partial_coverage")
        if snapshot["origin"] == "summary":
            result["limitations"].append("conversation_summary_context_only")
        times = []
        for message in snapshot["messages"]:
            if message["timestamp"] is not None:
                timestamp = parse_time(
                    message["timestamp"], "timestamp", nullable=False
                )
                assert timestamp is not None  # nullable=False rejects absent values.
                times.append(timestamp)
        if times != sorted(times):
            result["limitations"].append("conversation_timestamp_order_conflict")
        if any(p["disposition"] == "requiresConfirmation" for p in result["parts"]):
            result["limitations"].append("conversation_message_time_missing")
        if result["limitations"]:
            root.update(
                disposition="requiresConfirmation", reason=result["limitations"][0]
            )
            container.update(disposition="requiresConfirmation", reason=root["reason"])
    except (PacketBuildError, TextDecodeError) as exc:
        reason = (
            str(exc) if isinstance(exc, PacketBuildError) else "malformed_conversation"
        )
        root.update(disposition="unreadable", reason=reason)
        container.update(disposition="unreadable", reason=reason)
        result = {"parts": [], "units": [], "errors": [reason], "limitations": []}
    return result
