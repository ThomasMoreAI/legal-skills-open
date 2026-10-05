#!/usr/bin/env python3
"""Validate a framework.json against framework.schema.json, stdlib only.

Schema enforcement is driven by the schema file itself: type, enum, const,
pattern, minLength, maxLength, minimum, maximum, minItems, maxItems,
required, properties, additionalProperties, items, and anyOf are applied
recursively, so schema edits keep working without code changes. Keywords
the checker does not implement are reported as a note, never silently
ignored into a false pass.

Semantic checks beyond the schema include frame/target invariants for enumerated
request instruments. Census bijection is enforced when --instruments is given.

Usage:
    python3 validate_framework.py --framework framework.json \
        [--schema ../references/framework.schema.json] [--allow-approved]

Exit codes: 0 valid, 1 invalid, 2 I/O or unusable schema.
"""

import argparse
import json
import os
import re
import sys


def resolve_default_schema():
    """Find the schema in source, direct-package, or relocated-shared layout."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.normpath(
            os.path.join(script_dir, "..", "references", "framework.schema.json")
        ),
        os.path.normpath(
            os.path.join(
                script_dir,
                "..",
                "..",
                "references",
                "shared",
                "framework.schema.json",
            )
        ),
    ]
    return next((path for path in candidates if os.path.isfile(path)), candidates[0])


DEFAULT_SCHEMA = resolve_default_schema()

TYPE_CHECKS = {
    "object": lambda v: isinstance(v, dict),
    "array": lambda v: isinstance(v, list),
    "string": lambda v: isinstance(v, str),
    "integer": lambda v: isinstance(v, int) and not isinstance(v, bool),
    "number": lambda v: isinstance(v, (int, float)) and not isinstance(v, bool),
    "boolean": lambda v: isinstance(v, bool),
    "null": lambda v: v is None,
}

# Keywords this checker enforces, plus pure metadata it may skip.
HANDLED = {
    "type",
    "enum",
    "const",
    "pattern",
    "minLength",
    "maxLength",
    "minimum",
    "maximum",
    "minItems",
    "maxItems",
    "required",
    "properties",
    "additionalProperties",
    "items",
    "anyOf",
}
METADATA = {"$schema", "$id", "title", "description", "examples", "default"}
SERIES_PATTERN = re.compile(r"^[A-Z]+$")


def served_designator(series, number):
    return f"{series}-{number}" if series is not None else str(number)


def target_sort_key(key):
    instrument_id, series, number = key
    return (
        str(instrument_id),
        series if isinstance(series, str) else repr(series),
        number if isinstance(number, int) and not isinstance(number, bool) else -1,
    )


def type_name(value):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int):
        return "integer"
    if isinstance(value, float):
        return "number"
    return {dict: "object", list: "array", str: "string"}.get(
        type(value), type(value).__name__
    )


def json_equal(a, b):
    """Equality that keeps booleans apart from 0/1."""
    if isinstance(a, bool) != isinstance(b, bool):
        return False
    return a == b


def check_schema(value, schema, path, errors, unknown):
    """Apply one schema node to value, appending error strings with JSON paths."""
    for k in schema:
        if k not in HANDLED and k not in METADATA:
            unknown.add(k)

    if "anyOf" in schema:
        branch_fails = []
        for branch in schema["anyOf"]:
            trial = []
            check_schema(value, branch, path, trial, unknown)
            if not trial:
                branch_fails = None
                break
            branch_fails.append(trial[0])
        if branch_fails is not None:
            errors.append(
                "{}: no anyOf alternative matched ({})".format(
                    path, " | ".join(branch_fails)
                )
            )

    if "type" in schema:
        types = schema["type"]
        if not isinstance(types, list):
            types = [types]
        if not any(TYPE_CHECKS[t](value) for t in types):
            errors.append(
                "{}: expected type {}, got {}".format(
                    path, "/".join(types), type_name(value)
                )
            )
            return  # remaining keywords assume the declared type

    if "enum" in schema and not any(json_equal(value, o) for o in schema["enum"]):
        errors.append("{}: {!r} is not one of {}".format(path, value, schema["enum"]))
    if "const" in schema and not json_equal(value, schema["const"]):
        errors.append(
            "{}: must be exactly {!r}, got {!r}".format(path, schema["const"], value)
        )

    if isinstance(value, str):
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errors.append(
                "{}: {!r} does not match pattern {}".format(
                    path, value, schema["pattern"]
                )
            )
        if "minLength" in schema and len(value) < schema["minLength"]:
            errors.append(
                "%s: string shorter than minLength %d" % (path, schema["minLength"])
            )
        if "maxLength" in schema and len(value) > schema["maxLength"]:
            errors.append(
                "%s: string longer than maxLength %d" % (path, schema["maxLength"])
            )

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append(
                "{}: {!r} is below minimum {!r}".format(path, value, schema["minimum"])
            )
        if "maximum" in schema and value > schema["maximum"]:
            errors.append(
                "{}: {!r} is above maximum {!r}".format(path, value, schema["maximum"])
            )

    if isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            errors.append(
                "%s: array has %d item(s), minItems is %d"
                % (path, len(value), schema["minItems"])
            )
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            errors.append(
                "%s: array has %d item(s), maxItems is %d"
                % (path, len(value), schema["maxItems"])
            )
        if "items" in schema:
            for i, elem in enumerate(value):
                check_schema(
                    elem, schema["items"], "%s[%d]" % (path, i), errors, unknown
                )

    if isinstance(value, dict):
        props = schema.get("properties", {})
        for req in schema.get("required", []):
            if req not in value:
                errors.append(f"{path}: missing required property '{req}'")
        for k, v in value.items():
            if k in props:
                check_schema(v, props[k], f"{path}.{k}", errors, unknown)
            elif "additionalProperties" in schema:
                ap = schema["additionalProperties"]
                if ap is False:
                    errors.append(f"{path}: unexpected property '{k}'")
                elif isinstance(ap, dict):
                    check_schema(v, ap, f"{path}.{k}", errors, unknown)

    return errors


def semantic_errors(fw, allow_approved=False, instruments=None, manifest=None):
    """Cross-field checks the schema language cannot express."""
    errors = []
    if not isinstance(fw, dict):
        return errors

    v = fw.get("framework_version")
    if isinstance(v, int) and not isinstance(v, bool) and v < 1:
        errors.append("$.framework_version: must be >= 1, got %d" % v)
    if fw.get("approved") is True and not allow_approved:
        errors.append(
            "$.approved: must be false before sample-framework approval "
            "(pass --allow-approved to accept an approved framework)"
        )

    lenses = fw.get("lenses")
    if not isinstance(lenses, list):
        return errors
    lens_ids = {}
    issue_ids = {}
    for i, lens in enumerate(lenses):
        if not isinstance(lens, dict):
            continue
        lid = lens.get("lens_id")
        lpath = "$.lenses[%d]" % i
        if isinstance(lid, str):
            if lid in lens_ids:
                errors.append(
                    f"{lpath}.lens_id: duplicate lens_id {lid!r} (first used at {lens_ids[lid]})"
                )
            else:
                lens_ids[lid] = lpath
        items = lens.get("items")
        if not isinstance(items, list):
            continue
        for j, item in enumerate(items):
            if not isinstance(item, dict):
                continue
            iid = item.get("issue_id")
            ipath = "%s.items[%d]" % (lpath, j)
            if isinstance(iid, str):
                if iid in issue_ids:
                    errors.append(
                        f"{ipath}.issue_id: duplicate issue_id {iid!r} (first used at {issue_ids[iid]}); "
                        "issue_id must be unique across all lenses"
                    )
                else:
                    issue_ids[iid] = ipath
    for i, lens in enumerate(lenses):
        if not isinstance(lens, dict):
            continue
        for j, item in enumerate(lens.get("items") or []):
            if not isinstance(item, dict):
                continue
            owner = item.get("overlap_owner")
            if owner is not None and isinstance(owner, str) and owner not in lens_ids:
                errors.append(
                    "$.lenses[%d].items[%d].overlap_owner: %r is not a "
                    "lens_id defined in this framework" % (i, j, owner)
                )
    frame = fw.get("frame")
    if not isinstance(frame, dict):
        return errors

    frame_rows = frame.get("instruments")
    if not isinstance(frame_rows, list):
        return errors
    frame_by_id = {}
    for index, row in enumerate(frame_rows):
        if not isinstance(row, dict):
            continue
        instrument_id = row.get("instrument_id")
        if not isinstance(instrument_id, str):
            continue
        if instrument_id in frame_by_id:
            errors.append(
                f"$.frame.instruments[{index}].instrument_id: duplicate "
                f"instrument_id {instrument_id!r}"
            )
        else:
            frame_by_id[instrument_id] = row

    frame_corpus = frame.get("corpus_id")
    manifest_corpus = manifest.get("corpus_id") if isinstance(manifest, dict) else None
    if (
        isinstance(frame_corpus, str)
        and isinstance(manifest_corpus, str)
        and frame_corpus != manifest_corpus
    ):
        errors.append(
            f"$.frame.corpus_id: {frame_corpus!r} does not match manifest "
            f"corpus_id {manifest_corpus!r}"
        )

    frame_kind = frame.get("kind")
    if frame_kind == "issues":
        for i, lens in enumerate(lenses):
            if not isinstance(lens, dict):
                continue
            for j, item in enumerate(lens.get("items") or []):
                if isinstance(item, dict) and "target_ref" in item:
                    errors.append(
                        f"$.lenses[{i}].items[{j}].target_ref: forbidden in an "
                        "issues frame"
                    )
        return errors
    if frame_kind != "requests":
        return errors

    targets = {}
    instrument_target_counts = {instrument_id: 0 for instrument_id in frame_by_id}
    for i, lens in enumerate(lenses):
        if not isinstance(lens, dict):
            continue
        lens_id = lens.get("lens_id")
        for j, item in enumerate(lens.get("items") or []):
            if not isinstance(item, dict):
                continue
            path = f"$.lenses[{i}].items[{j}]"
            target = item.get("target_ref")
            if not isinstance(target, dict):
                errors.append(
                    f"{path}.target_ref: every requests-frame item requires one "
                    "singular target_ref"
                )
                continue
            instrument_id = target.get("instrument_id")
            element = target.get("element")
            series = target.get("series")
            series_key = (
                series if series is None or isinstance(series, str) else repr(series)
            )
            if instrument_id not in frame_by_id:
                errors.append(
                    f"{path}.target_ref.instrument_id: {instrument_id!r} is not "
                    "declared in frame.instruments"
                )
                continue
            frame_row = frame_by_id[instrument_id]
            if frame_row.get("staged") is True:
                errors.append(
                    f"{path}.target_ref: staged instrument {instrument_id!r} "
                    "cannot be targeted"
                )
            instrument_target_counts[instrument_id] += 1
            if not (
                isinstance(lens_id, str)
                and (
                    lens_id == instrument_id or lens_id.startswith(instrument_id + "-")
                )
            ):
                errors.append(
                    f"{path}.target_ref: instrument {instrument_id!r} does not "
                    f"align with lens {lens_id!r}"
                )
            key = (instrument_id, series_key, element)
            targets.setdefault(key, []).append(path)
    for key, paths in sorted(
        targets.items(), key=lambda pair: target_sort_key(pair[0])
    ):
        if len(paths) > 1:
            errors.append(
                f"$.frame: target {key[0]} no. "
                f"{served_designator(key[1], key[2])} is targeted more than "
                f"once ({', '.join(paths)})"
            )
    for instrument_id, row in sorted(frame_by_id.items()):
        if (
            row.get("staged") is not True
            and instrument_target_counts[instrument_id] == 0
        ):
            errors.append(
                f"$.frame.instruments: non-staged instrument {instrument_id!r} "
                "has no lens items"
            )

    if instruments is None:
        return errors
    census_rows = (
        instruments.get("instruments") if isinstance(instruments, dict) else None
    )
    if not isinstance(census_rows, list):
        errors.append("instruments.json: missing instruments array")
        return errors
    census_by_id = {}
    element_sets = {}
    for index, row in enumerate(census_rows):
        if not isinstance(row, dict):
            errors.append(f"instruments.json.instruments[{index}]: must be an object")
            continue
        instrument_id = row.get("instrument_id")
        if not isinstance(instrument_id, str):
            errors.append(
                f"instruments.json.instruments[{index}]: missing instrument_id"
            )
            continue
        if instrument_id in census_by_id:
            errors.append(
                f"instruments.json: duplicate instrument_id {instrument_id!r}"
            )
            continue
        census_by_id[instrument_id] = row
        identities = []
        for element_index, element_row in enumerate(row.get("elements") or []):
            if not isinstance(element_row, dict) or not isinstance(
                element_row.get("no"), int
            ):
                continue
            series = element_row.get("series")
            if "series" in element_row and not (
                isinstance(series, str) and SERIES_PATTERN.fullmatch(series)
            ):
                errors.append(
                    f"instruments.json: instrument {instrument_id!r} element row "
                    f"{element_index} has invalid series {series!r}; expected ^[A-Z]+$"
                )
                continue
            identity = (series, element_row["no"])
            if identity in identities:
                errors.append(
                    f"instruments.json: instrument {instrument_id!r} has duplicate "
                    f"element designator {served_designator(*identity)}"
                )
            identities.append(identity)
        element_sets[instrument_id] = set(identities)
    missing_frame = sorted(set(census_by_id) - set(frame_by_id))
    extra_frame = sorted(set(frame_by_id) - set(census_by_id))
    if missing_frame:
        errors.append(
            "$.frame.instruments: census instrument(s) missing from frame: "
            + ", ".join(missing_frame)
        )
    if extra_frame:
        errors.append(
            "$.frame.instruments: frame instrument(s) absent from census: "
            + ", ".join(extra_frame)
        )
    for instrument_id in sorted(set(frame_by_id) & set(census_by_id)):
        frame_row = frame_by_id[instrument_id]
        census_row = census_by_id[instrument_id]
        if frame_row.get("kind") != census_row.get("kind"):
            errors.append(
                f"$.frame.instruments: {instrument_id!r} kind does not match census"
            )
        if frame_row.get("element_count") != len(census_row.get("elements") or []):
            errors.append(
                f"$.frame.instruments: {instrument_id!r} element_count does not "
                "match census"
            )
        for key in sorted(
            (target for target in targets if target[0] == instrument_id),
            key=target_sort_key,
        ):
            identity = (key[1], key[2])
            if identity not in element_sets[instrument_id]:
                errors.append(
                    f"$.frame: target {instrument_id} no. "
                    f"{served_designator(*identity)} does not exist "
                    "in instruments.json"
                )
        if frame_row.get("staged") is True:
            continue
        for identity in sorted(
            element_sets[instrument_id],
            key=lambda value: (value[0] or "", value[1]),
        ):
            count = len(targets.get((instrument_id, identity[0], identity[1]), []))
            designator = served_designator(*identity)
            if count == 0:
                errors.append(
                    f"$.frame: {instrument_id} no. {designator} is not targeted"
                )
            elif count > 1:
                errors.append(
                    f"$.frame: {instrument_id} no. {designator} is targeted "
                    f"{count} times"
                )
    return errors


def validate(framework, schema, allow_approved=False, instruments=None, manifest=None):
    """Full validation. Returns (errors, unknown_keywords)."""
    errors = []
    unknown = set()
    check_schema(framework, schema, "$", errors, unknown)
    errors.extend(semantic_errors(framework, allow_approved, instruments, manifest))
    return errors, unknown


def load_json(path, kind):
    """Load a JSON file or raise ValueError with a readable message."""
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        raise ValueError(f"cannot read {kind} at {path}: {e}") from e


def main():
    ap = argparse.ArgumentParser(
        description="Validate framework.json against framework.schema.json."
    )
    ap.add_argument("--framework", required=True, help="framework.json to validate.")
    ap.add_argument(
        "--schema",
        default=DEFAULT_SCHEMA,
        help=f"Schema file (default: {DEFAULT_SCHEMA}).",
    )
    ap.add_argument(
        "--instruments",
        default=None,
        help="Optional instruments.json census for requests-mode bijection checks.",
    )
    ap.add_argument(
        "--manifest",
        default=None,
        help="Optional manifest.json for frame corpus_id binding.",
    )
    ap.add_argument(
        "--allow-approved",
        action="store_true",
        help="Accept approved: true after sample-framework approval.",
    )
    args = ap.parse_args()

    try:
        framework = load_json(args.framework, "framework")
        schema = load_json(args.schema, "schema")
        instruments = (
            load_json(args.instruments, "instruments") if args.instruments else None
        )
        manifest = load_json(args.manifest, "manifest") if args.manifest else None
    except ValueError as e:
        print(f"FATAL: {e}", file=sys.stderr)
        sys.exit(2)

    errors, unknown = validate(
        framework, schema, args.allow_approved, instruments, manifest
    )
    if unknown:
        print(
            "note: schema uses keyword(s) this checker does not enforce: {}".format(
                ", ".join(sorted(unknown))
            ),
            file=sys.stderr,
        )
    if errors:
        print("INVALID: %s (%d error(s))" % (args.framework, len(errors)))
        for e in errors:
            print("  " + e)
        sys.exit(1)
    if (
        isinstance(framework.get("frame"), dict)
        and framework["frame"].get("kind") == "requests"
        and instruments is None
    ):
        print(
            "note: requests-mode structural checks passed, but census/bijection "
            "was not proven; rerun with --instruments",
            file=sys.stderr,
        )
    n_items = sum(len(lens.get("items", [])) for lens in framework.get("lenses", []))
    print(
        "OK: %s is valid (%d lens(es), %d item(s), version %s)"
        % (
            args.framework,
            len(framework.get("lenses", [])),
            n_items,
            framework.get("framework_version"),
        )
    )


if __name__ == "__main__":
    main()
