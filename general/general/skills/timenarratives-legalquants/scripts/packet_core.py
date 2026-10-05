"""Versioned request, packet identity, filtering and partition primitives."""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime
from typing import Any

from packet_records import container_record as container_record
from packet_records import root_record as root_record
from packet_records import unreadable_container_record as unreadable_container_record

REQUEST_VERSION = "timenarratives.request.v1"
PACKET_VERSION = "timenarratives.packet.v1"
ID_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9._-]{0,127}$")
EXTERNAL_ID_PATTERN = re.compile(r"^(?=.*\S)[^\x00-\x1f\x7f]{1,256}$")
RFC3339_PATTERN = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$"
)
SOURCE_TYPES = {"text", "email", "docx", "user_note", "conversation"}
PARTITION_KEYS = (
    "ready",
    "requiresConfirmation",
    "exactDuplicate",
    "excluded",
    "unreadable",
    "expanded",
)
LIMITS = {
    "selectedRoots": 30,
    "selectedContainerBytes": 25 * 1024 * 1024,
    "selectedPacketBytes": 100 * 1024 * 1024,
    "derivedContainers": 100,
    "terminalUnits": 1000,
    "modelVisibleUtf8Bytes": 300 * 1024,
}
ALIAS_COUNT_LIMIT = 20
ALIAS_LENGTH_LIMIT = 256


class PacketBuildError(ValueError):
    pass


def canonical_digest(value: Any) -> str:
    encoded = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def parse_time(value: Any, label: str, *, nullable: bool) -> datetime | None:
    if value is None and nullable:
        return None
    if not isinstance(value, str) or not value or not RFC3339_PATTERN.fullmatch(value):
        raise PacketBuildError(f"{label} must be an RFC3339 timestamp")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise PacketBuildError(f"{label} must be an RFC3339 timestamp") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise PacketBuildError(f"{label} must include an offset")
    return parsed


def _exact_keys(
    value: dict, expected: set[str], label: str, *, optional: set[str] | None = None
) -> None:
    optional_keys = optional or set()
    keys = set(value)
    if not expected <= keys or keys - expected - optional_keys:
        raise PacketBuildError(f"{label} has missing or unexpected fields")


def _validate_aliases(value: Any, label: str) -> None:
    if not isinstance(value, list) or len(value) > ALIAS_COUNT_LIMIT:
        raise PacketBuildError(f"{label} must be a bounded list")
    if any(
        not isinstance(alias, str)
        or not alias.strip()
        or len(alias) > ALIAS_LENGTH_LIMIT
        for alias in value
    ):
        raise PacketBuildError(f"{label} contains an invalid alias")
    if len(value) != len(set(value)):
        raise PacketBuildError(f"{label} contains duplicate aliases")


def _valid_external_text(value: Any, maximum: int) -> bool:
    return (
        isinstance(value, str)
        and len(value) <= maximum
        and EXTERNAL_ID_PATTERN.fullmatch(value) is not None
    )


def validate_request(value: Any) -> dict:
    if not isinstance(value, dict):
        raise PacketBuildError("request must be an object")
    _exact_keys(
        value,
        {
            "schemaVersion",
            "runId",
            "actor",
            "matter",
            "selections",
            "filters",
        },
        "request",
        optional={"authorityConfirmed"},
    )
    if "authorityConfirmed" in value and value["authorityConfirmed"] is not True:
        raise PacketBuildError("authorityConfirmed must be true when supplied")
    if value["schemaVersion"] != REQUEST_VERSION:
        raise PacketBuildError("unsupported request schemaVersion")
    if not isinstance(value["runId"], str) or not ID_PATTERN.fullmatch(value["runId"]):
        raise PacketBuildError("runId is not a safe identifier")
    actor = value["actor"]
    if not isinstance(actor, dict):
        raise PacketBuildError("actor must be an object")
    _exact_keys(actor, {"id", "name", "aliases"}, "actor")
    if not _valid_external_text(actor["id"], 256):
        raise PacketBuildError("actor.id is not a valid external identity")
    if not _valid_external_text(actor["name"], 200):
        raise PacketBuildError("actor.name is not a valid bounded name")
    _validate_aliases(actor["aliases"], "actor.aliases")
    matter = value["matter"]
    if not isinstance(matter, dict):
        raise PacketBuildError("matter must be an object")
    _exact_keys(matter, {"id", "client", "aliases"}, "matter")
    if not _valid_external_text(matter["id"], 256):
        raise PacketBuildError("matter.id is not a valid external identity")
    if matter["client"] is not None and not _valid_external_text(matter["client"], 256):
        raise PacketBuildError("matter.client is not a valid bounded name or null")
    _validate_aliases(matter["aliases"], "matter.aliases")
    _validate_selections(value["selections"])
    _validate_filters(value["filters"])
    has_time_filter = any(
        value["filters"][key] is not None for key in ("since", "until")
    )
    if has_time_filter and any(
        selection["kind"] == "user_note" for selection in value["selections"]
    ):
        raise PacketBuildError(
            "user_note selections cannot be combined with time filters"
        )
    return value


def _validate_selections(selections: Any) -> None:
    if not isinstance(selections, list) or not selections:
        raise PacketBuildError("selections must be a non-empty ordered list")
    if len(selections) > LIMITS["selectedRoots"]:
        raise PacketBuildError("selected root cap exceeded")
    conversations: dict[str, str] = {}
    for selection in selections:
        if not isinstance(selection, dict) or selection.get("kind") not in {
            "file",
            "user_note",
            "conversation",
        }:
            raise PacketBuildError("unsupported selection kind")
        if selection["kind"] in {"file", "conversation"}:
            keys = {"kind", "path"}
            if selection["kind"] == "conversation":
                keys.add("conversationId")
            _exact_keys(selection, keys, "source selection")
            if not isinstance(selection["path"], str):
                raise PacketBuildError("source selection path must be a string")
            if selection["kind"] == "conversation" and not _valid_external_text(
                selection["conversationId"], 256
            ):
                raise PacketBuildError("conversationId must be a bounded identity")
            if selection["kind"] == "conversation":
                identity = selection["conversationId"]
                if conversations.get(identity, selection["path"]) != selection["path"]:
                    raise PacketBuildError("duplicate_conversation_selection")
                conversations[identity] = selection["path"]
        else:
            _exact_keys(selection, {"kind", "text"}, "user_note selection")
            if not isinstance(selection["text"], str) or not selection["text"].strip():
                raise PacketBuildError("user_note text must be non-empty")


def _validate_filters(filters: Any) -> None:
    if not isinstance(filters, dict):
        raise PacketBuildError("filters must be an object")
    _exact_keys(filters, {"sourceTypes", "since", "until", "asOf"}, "filters")
    source_types = filters["sourceTypes"]
    if (
        not isinstance(source_types, list)
        or not all(
            isinstance(item, str) and item in SOURCE_TYPES for item in source_types
        )
        or len(source_types) != len(set(source_types))
    ):
        raise PacketBuildError(
            "filters.sourceTypes contains an unsupported or duplicate value"
        )
    since = parse_time(filters["since"], "filters.since", nullable=True)
    until = parse_time(filters["until"], "filters.until", nullable=True)
    as_of = parse_time(filters["asOf"], "filters.asOf", nullable=False)
    if since and until and since > until:
        raise PacketBuildError("filters.since is after filters.until")
    if since and as_of and since > as_of:
        raise PacketBuildError("filters.since is after filters.asOf")
    if until and as_of and until > as_of:
        raise PacketBuildError("filters.until is after filters.asOf")


def empty_partition() -> dict[str, list[str]]:
    return {name: [] for name in PARTITION_KEYS}


def build_partition(rows: list[dict], id_field: str) -> dict[str, list[str]]:
    partition = empty_partition()
    for row in rows:
        disposition = row["disposition"]
        if disposition not in partition:
            raise PacketBuildError(f"unknown disposition: {disposition}")
        partition[disposition].append(row[id_field])
    return partition


def packet_status(roots: list[dict], units: list[dict], errors: list[str]) -> str:
    if errors or any(row["disposition"] == "unreadable" for row in roots) or not units:
        return "incomplete"
    if any(row["disposition"] == "requiresConfirmation" for row in roots):
        return "requires_confirmation"
    return "ready_for_semantic_analysis"


def finalize_packet(
    request: dict,
    roots: list[dict],
    containers: list[dict],
    leaves: list[dict],
    parts: list[dict],
    units: list[dict],
    errors: list[str],
    limitations: list[str],
) -> dict:
    model_bytes = sum(len(unit["canonicalText"].encode("utf-8")) for unit in units)
    if len(units) > LIMITS["terminalUnits"]:
        errors.append("terminal_unit_cap_exceeded")
    if model_bytes > LIMITS["modelVisibleUtf8Bytes"]:
        errors.append("model_visible_budget_exceeded")
    unique_errors = list(dict.fromkeys(errors))
    packet = {
        "schemaVersion": PACKET_VERSION,
        "runId": request["runId"],
        "requestDigestSha256": canonical_digest(request),
        "actor": request["actor"],
        "matter": request["matter"],
        "filters": request["filters"],
        "status": packet_status(roots, units, unique_errors),
        "limits": LIMITS,
        "roots": roots,
        "containers": containers,
        "mimeLeaves": leaves,
        "parts": parts,
        "units": units,
        "partitions": {
            "selectedRoots": build_partition(roots, "rootId"),
            "containers": build_partition(containers, "containerId"),
            "mimeLeaves": build_partition(leaves, "mimeLeafId"),
            "parts": build_partition(parts, "partId"),
        },
        "budget": {
            "modelVisibleUtf8Bytes": model_bytes,
            "modelVisibleUtf8Limit": LIMITS["modelVisibleUtf8Bytes"],
            "withinLimit": model_bytes <= LIMITS["modelVisibleUtf8Bytes"],
        },
        "errors": unique_errors,
        "limitations": limitations,
    }
    packet["packetDigestSha256"] = canonical_digest(packet)
    return packet
