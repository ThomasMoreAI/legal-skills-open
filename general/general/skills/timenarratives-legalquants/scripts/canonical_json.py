"""Canonical JSON identity and atomic file helpers for TimeNarratives."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


class JsonFileError(ValueError):
    """A JSON artifact is unreadable, duplicated, or not an object."""

    def __init__(self, code: str) -> None:
        self.code = code
        super().__init__(code)


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise JsonFileError("input_duplicate_key")
        value[key] = item
    return value


def canonical_bytes(value: object) -> bytes:
    """Return stable UTF-8 JSON bytes with no insignificant whitespace."""
    try:
        text = json.dumps(
            value,
            allow_nan=False,
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        )
    except (TypeError, ValueError) as exc:
        raise JsonFileError("value_not_canonical_json") from exc
    try:
        return text.encode("utf-8")
    except UnicodeEncodeError:
        escaped = json.dumps(
            value,
            allow_nan=False,
            ensure_ascii=True,
            separators=(",", ":"),
            sort_keys=True,
        )
        return escaped.encode("ascii")


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def packet_sha256(packet: dict[str, Any]) -> str:
    """Hash a packet while excluding its self-identifying digest field."""
    subject = dict(packet)
    subject.pop("packetDigestSha256", None)
    return canonical_sha256(subject)


def _reject_constant(value: str) -> None:
    raise JsonFileError("input_invalid_json")


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise JsonFileError("input_invalid_json")
    return parsed


def parse_json_object(raw: str) -> dict[str, Any]:
    """Parse already bounded JSON without accepting duplicate object keys."""
    try:
        value = json.loads(
            raw,
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
            parse_float=_finite_float,
        )
    except json.JSONDecodeError as exc:
        raise JsonFileError("input_invalid_json") from exc
    if not isinstance(value, dict):
        raise JsonFileError("input_not_object")
    return value


def read_json_object(path: str | Path) -> dict[str, Any]:
    try:
        raw = Path(path).read_text(encoding="utf-8")
    except OSError as exc:
        raise JsonFileError("input_unreadable") from exc
    except UnicodeDecodeError as exc:
        raise JsonFileError("input_invalid_utf8") from exc
    return parse_json_object(raw)


def pretty_json_bytes(value: object) -> bytes:
    try:
        text = json.dumps(
            value,
            allow_nan=False,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    except (TypeError, ValueError) as exc:
        raise JsonFileError("value_not_canonical_json") from exc
    return text.encode("utf-8") + b"\n"
