#!/usr/bin/env python3
"""Resolve quoted evidence in a draft map to exact byte spans, then validate.

The model never computes an offset or a hash. It quotes the unit text; this
script finds the unique span, fills startByte / endByte / spanSha256, removes
the quote, and runs the map validator on the result. A quote that is absent or
occurs more than once is a named fault, with the nearest unit text shown so the
quote can be corrected rather than guessed.
"""

from __future__ import annotations

import argparse
import copy
import difflib
import hashlib
import json
from pathlib import Path
from typing import Any

from canonical_json import JsonFileError, pretty_json_bytes, read_json_object
from map_semantics import validate_map
from safe_output import OutputSafetyError, write_new_bytes

Fault = dict[str, str]


def _nearest(text: str, quote: str) -> str:
    window = max(len(quote), 40)
    step = max(1, window // 4)
    best, best_ratio = "", 0.0
    for start in range(0, max(1, len(text) - window + 1), step):
        candidate = text[start : start + window]
        ratio = difflib.SequenceMatcher(None, candidate, quote).ratio()
        if ratio > best_ratio:
            best, best_ratio = candidate, ratio
    return best


def resolve(
    packet: dict[str, Any], draft: dict[str, Any]
) -> tuple[dict[str, Any], list[Fault]]:
    """Return (map, faults); the map is complete only when faults is empty."""
    units = {
        unit["unitId"]: unit
        for unit in packet.get("units", [])
        if isinstance(unit, dict) and isinstance(unit.get("unitId"), str)
    }
    mapping = copy.deepcopy(draft)
    faults: list[Fault] = []
    atoms = mapping.get("atoms")
    if not isinstance(atoms, list):
        return mapping, [{"code": "expected_array", "path": "$.atoms"}]
    for index, atom in enumerate(atoms):
        path = f"$.atoms[{index}].quote"
        if not isinstance(atom, dict):
            faults.append({"code": "expected_object", "path": path})
            continue
        quote = atom.pop("quote", None)
        unit_id = atom.get("unitId")
        unit = units.get(unit_id) if isinstance(unit_id, str) else None
        if not isinstance(quote, str) or not quote:
            faults.append({"code": "quote_missing", "path": path})
            continue
        if unit is None or not isinstance(unit.get("canonicalText"), str):
            faults.append({"code": "unresolved_atom_unit", "path": path})
            continue
        text = unit["canonicalText"]
        first = text.find(quote)
        if first < 0:
            nearest = _nearest(text, quote)
            faults.append({"code": "quote_not_found", "path": path, "nearest": nearest})
            continue
        if text.find(quote, first + 1) >= 0:
            faults.append({"code": "quote_ambiguous", "path": path})
            continue
        start = len(text[:first].encode("utf-8"))
        span = quote.encode("utf-8")
        atom["startByte"] = start
        atom["endByte"] = start + len(span)
        atom["spanSha256"] = hashlib.sha256(span).hexdigest()
    return mapping, faults


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packet", required=True)
    parser.add_argument("--draft", required=True)
    parser.add_argument("--source-root", required=True, help="selected sources")
    parser.add_argument("--out", required=True, help="new map.json (never replaced)")
    args = parser.parse_args(argv)
    try:
        packet = read_json_object(args.packet)
        draft = read_json_object(args.draft)
    except JsonFileError as exc:
        print(json.dumps({"status": "operational_fault", "error": exc.code}))
        return 2
    mapping, faults = resolve(packet, draft)
    if not faults:
        faults = list(validate_map(packet, mapping)["faults"])
    if faults:
        print(json.dumps({"status": "contract_fault", "faults": faults}))
        return 1
    try:
        write_new_bytes(
            Path(args.out),
            pretty_json_bytes(mapping),
            protected_paths=(args.packet, args.draft),
            forbidden_roots=(Path(args.source_root),),
        )
    except OutputSafetyError as exc:
        print(json.dumps({"status": "operational_fault", "error": exc.args[0]}))
        return 2
    print(json.dumps({"status": "passed", "map": args.out}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
