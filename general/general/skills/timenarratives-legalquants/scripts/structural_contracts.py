# Dependency-free structural mirrors of the published JSON contracts.

from __future__ import annotations

import re
from collections import Counter
from typing import Any

from assessment_contract import assessment_pair_valid
from narrative_contract import MAX_TEXT_CODEPOINTS, narrative_text_faults
from packet_contract import validate_packet_structure
from packet_edges import validate_packet_edges
from packet_semantics import validate_packet_semantic_state

Issue = dict[str, str]
ID = re.compile(r"^[A-Za-z][A-Za-z0-9._-]{0,127}$")
EXTERNAL_ID = re.compile(r"^(?=.*\S)[^\x00-\x1f\x7f]{1,256}$")
SHA = re.compile(r"^[0-9a-f]{64}$")
TOKEN = re.compile(r"^TN-[0-9a-f]{16}$")
PARTITION_KEYS = set(
    "ready requiresConfirmation exactDuplicate excluded unreadable expanded".split()
)

TOP_LEVEL: dict[str, set[str]] = {
    "map": set(
        (
            "schemaVersion runId packetDigest unitAssessment atoms events "
            "workstreams clauses"
        ).split()
    ),
    "confirmation": set(
        (
            "schemaVersion runId packetDigest mapDigest decision recording "
            "confirmationToken"
        ).split()
    ),
    "deliverable": set(
        "schemaVersion runId status narratives checkQuestions receipt".split()
    ),
}


def issue(code: str, path: str) -> Issue:
    return {"code": code, "path": path}


def _closed(value: Any, keys: set[str], path: str, out: list[Issue]) -> bool:
    if not isinstance(value, dict):
        out.append(issue("expected_object", path))
        return False
    missing = keys - set(value)
    extra = set(value) - keys
    for key in sorted(missing):
        out.append(issue("missing_field", f"{path}.{key}"))
    for key in sorted(extra):
        out.append(issue("unknown_field", f"{path}.{key}"))
    return not missing


def _text(
    value: Any,
    path: str,
    out: list[Issue],
    *,
    maximum: int = 600,
    nullable: bool = False,
) -> None:
    if nullable and value is None:
        return
    if not isinstance(value, str) or not value or len(value) > maximum:
        out.append(issue("expected_text", path))


def _id(value: Any, path: str, out: list[Issue]) -> None:
    if not isinstance(value, str) or ID.fullmatch(value) is None:
        out.append(issue("invalid_id", path))


def _external_id(value: Any, path: str, out: list[Issue]) -> None:
    if not isinstance(value, str) or EXTERNAL_ID.fullmatch(value) is None:
        out.append(issue("invalid_external_id", path))


def _hash(value: Any, path: str, out: list[Issue]) -> None:
    if not isinstance(value, str) or SHA.fullmatch(value) is None:
        out.append(issue("invalid_sha256", path))


def _records(value: Any, path: str, out: list[Issue]) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        out.append(issue("expected_array", path))
        return []
    records: list[dict[str, Any]] = []
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            out.append(issue("expected_object", f"{path}[{index}]"))
        else:
            records.append(item)
    return records


def _id_list(value: Any, path: str, out: list[Issue], *, nonempty: bool) -> None:
    if not isinstance(value, list) or (nonempty and not value):
        out.append(issue("expected_id_array", path))
        return
    seen: set[str] = set()
    for index, item in enumerate(value):
        _id(item, f"{path}[{index}]", out)
        if isinstance(item, str) and item in seen:
            out.append(issue("duplicate_array_item", f"{path}[{index}]"))
        if isinstance(item, str):
            seen.add(item)


def _map_contract(value: dict[str, Any], out: list[Issue]) -> None:
    if value.get("schemaVersion") != "timenarratives.map.v1":
        out.append(issue("schema_version", "$.schemaVersion"))
    _id(value.get("runId"), "$.runId", out)
    _hash(value.get("packetDigest"), "$.packetDigest", out)
    dispositions = set(
        "used read_but_unused excluded_other_actor excluded_other_matter "
        "excluded_non_work needs_confirmation".split()
    )
    reasons: set[str | None] = {None}
    reasons.update(
        "actor_unclear matter_unclear action_unclear object_unclear "
        "source_unsupported source_unreadable source_partially_read "
        "other_actor other_matter non_work not_relevant".split()
    )
    for index, row in enumerate(
        _records(value.get("unitAssessment"), "$.unitAssessment", out)
    ):
        path = f"$.unitAssessment[{index}]"
        _closed(row, {"unitId", "disposition", "reason"}, path, out)
        _id(row.get("unitId"), f"{path}.unitId", out)
        if row.get("disposition") not in dispositions:
            out.append(issue("invalid_enum", f"{path}.disposition"))
        if row.get("reason") not in reasons:
            out.append(issue("invalid_enum", f"{path}.reason"))
        elif not assessment_pair_valid(row.get("disposition"), row.get("reason")):
            out.append(issue("assessment_reason", f"{path}.reason"))
    components = {"actor", "action", "object", "matter", "purpose"}
    for index, row in enumerate(_records(value.get("atoms"), "$.atoms", out)):
        path = f"$.atoms[{index}]"
        keys = {"atomId", "unitId", "startByte", "endByte", "spanSha256", "components"}
        _closed(row, keys, path, out)
        _id(row.get("atomId"), f"{path}.atomId", out)
        _id(row.get("unitId"), f"{path}.unitId", out)
        for key, minimum in (("startByte", 0), ("endByte", 1)):
            number = row.get(key)
            if (
                isinstance(number, bool)
                or not isinstance(number, int)
                or number < minimum
            ):
                out.append(issue("invalid_integer", f"{path}.{key}"))
        _hash(row.get("spanSha256"), f"{path}.spanSha256", out)
        listed = row.get("components")
        if (
            not isinstance(listed, list)
            or not listed
            or any(
                not isinstance(item, str) or item not in components for item in listed
            )
            or len(set(listed)) != len(listed)
        ):
            out.append(issue("invalid_components", f"{path}.components"))
    _event_contract(value.get("events"), out)
    _workstream_contract(value.get("workstreams"), out)
    _clause_contract(value.get("clauses"), out)


def _event_contract(value: Any, out: list[Issue]) -> None:
    keys = {
        "eventId",
        "assertedBy",
        "performedByActorId",
        "namedTimekeeperActorId",
        "action",
        "object",
        "purpose",
        "matterId",
        "workstreamId",
        "atomIds",
    }
    for index, row in enumerate(_records(value, "$.events", out)):
        path = f"$.events[{index}]"
        _closed(row, keys, path, out)
        for key in ("eventId", "workstreamId"):
            _id(row.get(key), f"{path}.{key}", out)
        for key in ("performedByActorId", "namedTimekeeperActorId", "matterId"):
            _external_id(row.get(key), f"{path}.{key}", out)
        _text(row.get("assertedBy"), f"{path}.assertedBy", out, maximum=200)
        for key in ("action", "object"):
            _text(row.get(key), f"{path}.{key}", out, maximum=300)
        _text(row.get("purpose"), f"{path}.purpose", out, maximum=500, nullable=True)
        _id_list(row.get("atomIds"), f"{path}.atomIds", out, nonempty=True)


def _workstream_contract(value: Any, out: list[Issue]) -> None:
    for index, row in enumerate(_records(value, "$.workstreams", out)):
        path = f"$.workstreams[{index}]"
        _closed(row, {"workstreamId", "label", "category"}, path, out)
        _id(row.get("workstreamId"), f"{path}.workstreamId", out)
        _text(row.get("label"), f"{path}.label", out, maximum=160)
        if row.get("category") not in {"substantive", "administrative", "other"}:
            out.append(issue("invalid_enum", f"{path}.category"))


def _clause_contract(value: Any, out: list[Issue]) -> None:
    keys = {"clauseId", "workstreamId", "clauseOwnerActorId", "eventIds", "text"}
    for index, row in enumerate(_records(value, "$.clauses", out)):
        path = f"$.clauses[{index}]"
        _closed(row, keys, path, out)
        for key in ("clauseId", "workstreamId"):
            _id(row.get(key), f"{path}.{key}", out)
        _external_id(row.get("clauseOwnerActorId"), f"{path}.clauseOwnerActorId", out)
        _id_list(row.get("eventIds"), f"{path}.eventIds", out, nonempty=True)
        text = row.get("text")
        _text(text, f"{path}.text", out, maximum=MAX_TEXT_CODEPOINTS)
        if isinstance(text, str) and 0 < len(text) <= MAX_TEXT_CODEPOINTS:
            for code in narrative_text_faults(text):
                out.append(issue(code, f"{path}.text"))


def _confirmation_contract(value: dict[str, Any], out: list[Issue]) -> None:
    expected = {
        "schemaVersion": "timenarratives.confirmation.v1",
        "decision": "confirmed",
        "recording": "session_recorded_user_confirmation",
    }
    for key, wanted in expected.items():
        if value.get(key) != wanted:
            out.append(issue(f"confirmation_{key}", f"$.{key}"))
    _id(value.get("runId"), "$.runId", out)
    _hash(value.get("packetDigest"), "$.packetDigest", out)
    _hash(value.get("mapDigest"), "$.mapDigest", out)
    token = value.get("confirmationToken")
    if not isinstance(token, str) or TOKEN.fullmatch(token) is None:
        out.append(issue("confirmation_token", "$.confirmationToken"))


def validate_structure(kind: str, value: Any) -> list[Issue]:
    out: list[Issue] = []
    keys = TOP_LEVEL.get(kind)
    if keys is None:
        return [issue("unknown_contract", "$")]
    if not _closed(value, keys, "$", out):
        return out
    assert isinstance(value, dict)
    if kind == "map":
        _map_contract(value, out)
    elif kind == "confirmation":
        _confirmation_contract(value, out)
    else:
        _deliverable_contract(value, out)
    return out


def validate_packet_reconciliation(packet: Any) -> list[Issue]:
    # Verify the packet partitions later described as complete.
    out: list[Issue] = []
    if not isinstance(packet, dict):
        return [issue("packet_shape", "$packet")]
    partitions = packet.get("partitions")
    if not isinstance(partitions, dict):
        return [issue("packet_partition", "$packet.partitions")]
    layout = (
        ("selectedRoots", "roots", "rootId"),
        ("containers", "containers", "containerId"),
        ("mimeLeaves", "mimeLeaves", "mimeLeafId"),
        ("parts", "parts", "partId"),
    )
    for partition_name, rows_name, id_field in layout:
        rows = packet.get(rows_name)
        partition = partitions.get(partition_name)
        path = f"$packet.partitions.{partition_name}"
        if not isinstance(rows, list) or not isinstance(partition, dict):
            out.append(issue("packet_partition", path))
            continue
        if set(partition) != PARTITION_KEYS or not all(
            isinstance(values, list) for values in partition.values()
        ):
            out.append(issue("packet_partition", path))
            continue
        row_ids = [row.get(id_field) for row in rows if isinstance(row, dict)]
        partition_ids = [item for values in partition.values() for item in values]
        dispositions = {
            row.get(id_field): row.get("disposition")
            for row in rows
            if isinstance(row, dict)
        }
        closes = len(row_ids) == len(rows) and len(row_ids) == len(set(row_ids))
        closes = closes and Counter(partition_ids) == Counter(row_ids)
        closes = closes and all(
            dispositions.get(identifier) == category
            for category, identifiers in partition.items()
            for identifier in identifiers
        )
        if not closes:
            out.append(issue("packet_partition", path))
    out.extend(validate_packet_edges(packet))
    return out


def validate_packet_semantic_boundary(packet: Any) -> list[Issue]:
    # Require a reconciled packet with actor- and matter-bound source evidence.
    out = validate_packet_structure(packet)
    if out:
        return out
    out.extend(validate_packet_reconciliation(packet))
    if not isinstance(packet, dict):
        return out
    units = packet.get("units", [])
    if not isinstance(units, list) or any(not isinstance(unit, dict) for unit in units):
        out.append(issue("packet_unit_shape", "$packet.units"))
        return out
    unit_ids = [
        unit.get("unitId") for unit in units if isinstance(unit.get("unitId"), str)
    ]
    if len(unit_ids) != len(set(unit_ids)):
        out.append(issue("duplicate_id", "$packet.units"))
    out.extend(validate_packet_semantic_state(packet))
    return out


def _deliverable_contract(value: dict[str, Any], out: list[Issue]) -> None:
    from receipt import validate_deliverable_structure

    out.extend(validate_deliverable_structure(value))
