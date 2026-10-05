"""Small dependency-free evaluator for the JSON Schema subset shipped here."""

from __future__ import annotations

import json
import math
import re
from datetime import datetime
from typing import Any

Issue = dict[str, str]
RFC3339 = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$"
)
KEYWORDS = frozenset(
    "$schema $id title description deprecated $defs $ref type "
    "additionalProperties required "
    "properties const enum anyOf oneOf items minItems maxItems uniqueItems minLength "
    "maxLength pattern format minimum".split()
)


def _issue(path: str) -> Issue:
    return {"code": "packet_structure", "path": path}


def _resolve(root: dict[str, Any], reference: str) -> dict[str, Any]:
    if not reference.startswith("#/"):
        raise ValueError("only local JSON Schema references are supported")
    value: Any = root
    for token in reference[2:].split("/"):
        key = token.replace("~1", "/").replace("~0", "~")
        value = value[key]
    if not isinstance(value, dict):
        raise ValueError("JSON Schema reference must resolve to an object")
    return value


def _assert_supported(schema: dict[str, Any], path: str = "$") -> None:
    unknown = set(schema) - KEYWORDS
    if unknown:
        names = ", ".join(sorted(unknown))
        raise ValueError(f"unsupported JSON Schema keyword at {path}: {names}")
    for group in ("$defs", "properties"):
        children = schema.get(group, {})
        if isinstance(children, dict):
            for name, child in children.items():
                if isinstance(child, dict):
                    _assert_supported(child, f"{path}.{group}.{name}")
    item_schema = schema.get("items")
    if isinstance(item_schema, dict):
        _assert_supported(item_schema, f"{path}.items")
    for keyword in ("anyOf", "oneOf"):
        branches = schema.get(keyword, [])
        if isinstance(branches, list):
            for index, branch in enumerate(branches):
                if isinstance(branch, dict):
                    _assert_supported(branch, f"{path}.{keyword}[{index}]")


def _matches_type(value: Any, expected: str) -> bool:
    if expected == "null":
        return value is None
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return (
            isinstance(value, (int, float))
            and not isinstance(value, bool)
            and math.isfinite(value)
        )
    if expected == "string":
        return isinstance(value, str)
    if expected == "array":
        return isinstance(value, list)
    if expected == "object":
        return isinstance(value, dict)
    raise ValueError(f"unsupported JSON Schema type: {expected}")


def _json_equal(left: Any, right: Any) -> bool:
    if isinstance(left, bool) or isinstance(right, bool):
        return isinstance(left, bool) and isinstance(right, bool) and left is right
    if left is None or right is None:
        return left is right
    numbers = (int, float)
    if isinstance(left, numbers) and isinstance(right, numbers):
        return left == right
    if type(left) is not type(right):
        return False
    if isinstance(left, list):
        return len(left) == len(right) and all(
            _json_equal(a, b) for a, b in zip(left, right, strict=True)
        )
    if isinstance(left, dict):
        return left.keys() == right.keys() and all(
            _json_equal(left[key], right[key]) for key in left
        )
    return left == right


def _valid_datetime(value: str) -> bool:
    if RFC3339.fullmatch(value) is None:
        return False
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return True


def _validate(
    value: Any,
    schema: dict[str, Any],
    root: dict[str, Any],
    path: str,
) -> list[Issue]:
    if "$ref" in schema:
        return _validate(value, _resolve(root, schema["$ref"]), root, path)
    out: list[Issue] = []
    if "anyOf" in schema:
        branch_results = [
            _validate(value, branch, root, path) for branch in schema["anyOf"]
        ]
        if not any(not result for result in branch_results):
            out.append(_issue(path))
    if "oneOf" in schema:
        matches = sum(
            not _validate(value, branch, root, path) for branch in schema["oneOf"]
        )
        if matches != 1:
            out.append(_issue(path))
    if "const" in schema and not _json_equal(value, schema["const"]):
        out.append(_issue(path))
    if "enum" in schema and not any(
        _json_equal(value, candidate) for candidate in schema["enum"]
    ):
        out.append(_issue(path))
    expected = schema.get("type")
    if expected is not None:
        choices = expected if isinstance(expected, list) else [expected]
        if not any(_matches_type(value, choice) for choice in choices):
            out.append(_issue(path))
            return out
    if isinstance(value, dict):
        properties = schema.get("properties", {})
        required = schema.get("required", [])
        for key in required:
            if key not in value:
                out.append(_issue(f"{path}.{key}"))
        if schema.get("additionalProperties") is False and not set(value) <= set(
            properties
        ):
            out.append(_issue(path))
        for key, item in value.items():
            child_schema = properties.get(key)
            if isinstance(child_schema, dict):
                out.extend(_validate(item, child_schema, root, f"{path}.{key}"))
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            out.append(_issue(path))
        maximum = schema.get("maxItems")
        if isinstance(maximum, int) and len(value) > maximum:
            out.append(_issue(path))
        if schema.get("uniqueItems") is True:
            markers = [
                json.dumps(item, ensure_ascii=False, sort_keys=True) for item in value
            ]
            if len(markers) != len(set(markers)):
                out.append(_issue(path))
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(value):
                out.extend(_validate(item, item_schema, root, f"{path}[{index}]"))
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            out.append(_issue(path))
        maximum = schema.get("maxLength")
        if isinstance(maximum, int) and len(value) > maximum:
            out.append(_issue(path))
        pattern = schema.get("pattern")
        if isinstance(pattern, str) and re.search(pattern, value) is None:
            out.append(_issue(path))
        if schema.get("format") == "date-time" and not _valid_datetime(value):
            out.append(_issue(path))
    if (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and "minimum" in schema
        and value < schema["minimum"]
    ):
        out.append(_issue(path))
    return out


def validate_schema_subset(
    value: Any, schema: dict[str, Any], *, path: str = "$"
) -> list[Issue]:
    _assert_supported(schema)
    return _validate(value, schema, schema, path)
