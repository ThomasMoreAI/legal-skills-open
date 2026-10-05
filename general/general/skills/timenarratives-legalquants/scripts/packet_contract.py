"""Shipped stdlib structural gate for the private TimeNarratives packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from schema_subset import validate_schema_subset

_SCHEMA_PATH = (
    Path(__file__).resolve().parents[1]
    / "schemas"
    / "timenarratives-packet.schema.json"
)
_SCHEMA = json.loads(_SCHEMA_PATH.read_text(encoding="utf-8"))


def validate_packet_structure(value: Any) -> list[dict[str, str]]:
    issues = validate_schema_subset(value, _SCHEMA, path="$packet")
    unique = {(issue["code"], issue["path"]): issue for issue in issues}
    return [unique[key] for key in sorted(unique)]
