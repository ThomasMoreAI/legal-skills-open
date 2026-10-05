#!/usr/bin/env python3
"""Validate a TimeNarratives map and optional digest-bound confirmation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from canonical_json import JsonFileError, pretty_json_bytes, read_json_object
from map_semantics import validate_confirmation, validate_map
from safe_output import write_new_bytes


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packet", required=True)
    parser.add_argument("--map", dest="mapping", required=True)
    parser.add_argument("--confirmation")
    parser.add_argument("--out")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        packet = read_json_object(args.packet)
        mapping = read_json_object(args.mapping)
        confirmation = (
            read_json_object(args.confirmation)
            if args.confirmation is not None
            else None
        )
    except JsonFileError as exc:
        print(json.dumps({"status": "operational_fault", "error": exc.code}))
        return 2
    result = validate_map(packet, mapping)
    faults = list(result["faults"])
    if confirmation is not None:
        faults.extend(validate_confirmation(packet, mapping, confirmation)["faults"])
    output = {
        "status": "contract_fault" if faults else "passed",
        "mapDigest": result["mapDigest"],
        "faults": faults,
    }
    if not faults:
        output["confirmationToken"] = f"TN-{result['mapDigest'][:16]}"
    if args.out is not None and not faults:
        try:
            protected = [args.packet, args.mapping]
            if args.confirmation is not None:
                protected.append(args.confirmation)
            write_new_bytes(
                Path(args.out),
                pretty_json_bytes(output),
                protected_paths=protected,
            )
        except BaseException:
            print(
                json.dumps(
                    {
                        "status": "operational_fault",
                        "error": "output_write_failed",
                    }
                )
            )
            return 2
    print(json.dumps(output, sort_keys=True))
    return 1 if faults else 0


if __name__ == "__main__":
    raise SystemExit(main())
