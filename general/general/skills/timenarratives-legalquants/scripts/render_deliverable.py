#!/usr/bin/env python3
"""Validate and atomically render a confirmed TimeNarratives map."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from build_packet import PacketBuildError, compile_packet
from canonical_json import (
    JsonFileError,
    canonical_bytes,
    canonical_sha256,
    pretty_json_bytes,
    read_json_object,
)
from deliverable_markdown import render_markdown
from map_semantics import validate_confirmation, validate_map
from output_privacy import scan_rendered
from receipt import build_deliverable
from safe_output import OutputSafetyError, publish_owned_directory
from source_paths import SourcePathError, validate_source_root
from structural_contracts import validate_structure


class FreshnessOperationalError(RuntimeError):
    """The selected packet could not be recompiled for freshness."""


class FreshnessContractError(ValueError):
    """The current selected packet no longer matches the confirmed packet."""

    def __init__(self, faults: list[dict[str, str]]) -> None:
        self.faults = faults
        super().__init__("source_packet_stale")


def build_rendered(
    packet: dict[str, Any], mapping: dict[str, Any], confirmation: dict[str, Any]
) -> dict[str, Any]:
    map_result = validate_map(packet, mapping)
    faults = list(map_result["faults"])
    confirmation_result = validate_confirmation(packet, mapping, confirmation)
    faults.extend(confirmation_result["faults"])
    if faults:
        return {"faults": faults, "deliverable": None, "markdown": None}
    deliverable = build_deliverable(
        packet,
        mapping,
        confirmation,
        map_result["eventSupport"],
        map_result["mapDigest"],
    )
    markdown = render_markdown(deliverable)
    faults.extend(validate_structure("deliverable", deliverable))
    faults.extend(scan_rendered(deliverable, markdown, packet))
    if faults:
        return {"faults": faults, "deliverable": None, "markdown": None}
    return {"faults": [], "deliverable": deliverable, "markdown": markdown}


def internal_confirmation(
    packet: dict[str, Any], mapping: dict[str, Any]
) -> dict[str, Any]:
    """Session-recorded approval bound to the current packet and map digests."""
    map_digest = canonical_sha256(mapping)
    return {
        "schemaVersion": "timenarratives.confirmation.v1",
        "runId": packet.get("runId"),
        "packetDigest": packet.get("packetDigestSha256"),
        "mapDigest": map_digest,
        "decision": "confirmed",
        "recording": "session_recorded_user_confirmation",
        "confirmationToken": f"TN-{map_digest[:16]}",
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", required=True)
    parser.add_argument("--source-root", required=True)
    parser.add_argument("--packet", required=True)
    parser.add_argument("--map", dest="mapping", required=True)
    approval = parser.add_mutually_exclusive_group(required=True)
    approval.add_argument("--confirmation")
    approval.add_argument(
        "--user-approved",
        action="store_true",
        help="the user approved the displayed draft in ordinary language; "
        "record that approval against the current map digest",
    )
    parser.add_argument(
        "--reviewed-map-digest",
        help="mapDigest retained when the draft was displayed, before user approval",
    )
    parser.add_argument("--out-dir", required=True)
    return parser


def _freshness_faults(
    packet: dict[str, Any],
    bound_request: dict[str, Any],
    request_path: str | Path,
    source_root: Path,
) -> list[dict[str, str]]:
    try:
        request = read_json_object(request_path)
        request_matches = canonical_bytes(request) == canonical_bytes(
            bound_request
        ) and canonical_sha256(request) == packet.get("requestDigestSha256")
    except JsonFileError:
        request_matches = False
    if not request_matches:
        return [{"code": "source_packet_stale", "path": "$.requestDigestSha256"}]
    try:
        current = compile_packet(request, source_root)
    except PacketBuildError:
        return [{"code": "source_packet_stale", "path": "$.requestDigestSha256"}]
    except Exception as exc:
        raise FreshnessOperationalError("freshness_recompile_failed") from exc
    try:
        matches = canonical_bytes(current) == canonical_bytes(packet)
    except JsonFileError:
        matches = False
    if not matches:
        return [{"code": "source_packet_stale", "path": "$.packetDigestSha256"}]
    return []


def _operational_fault(code: str) -> int:
    print(json.dumps({"status": "operational_fault", "error": code}))
    return 2


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        request = read_json_object(args.request)
        packet = read_json_object(args.packet)
        mapping = read_json_object(args.mapping)
        if args.user_approved and args.reviewed_map_digest != canonical_sha256(mapping):
            print(
                json.dumps(
                    {
                        "status": "contract_fault",
                        "faults": [
                            {"code": "reviewed_map_mismatch", "path": "$.mapDigest"}
                        ],
                    }
                )
            )
            return 1
        confirmation = (
            internal_confirmation(packet, mapping)
            if args.user_approved
            else read_json_object(args.confirmation)
        )
        source_root = validate_source_root(Path(args.source_root))
    except JsonFileError as exc:
        return _operational_fault(exc.code)
    except SourcePathError:
        return _operational_fault("input_unavailable")
    try:
        result = build_rendered(packet, mapping, confirmation)
    except Exception:
        return _operational_fault("validation_failed")
    if result["faults"]:
        print(json.dumps({"status": "contract_fault", "faults": result["faults"]}))
        return 1
    assert isinstance(result["deliverable"], dict)
    assert isinstance(result["markdown"], str)

    def require_current_packet() -> None:
        faults = _freshness_faults(packet, request, args.request, source_root)
        if faults:
            raise FreshnessContractError(faults)

    try:
        publish_owned_directory(
            Path(args.out_dir),
            {
                "deliverable.json": pretty_json_bytes(result["deliverable"]),
                "narratives.md": result["markdown"].encode("utf-8"),
            },
            protected_paths=tuple(
                path
                for path in (args.request, args.packet, args.mapping, args.confirmation)
                if path is not None
            ),
            forbidden_roots=(source_root,),
            before_publish=require_current_packet,
        )
    except FreshnessContractError as exc:
        print(json.dumps({"status": "contract_fault", "faults": exc.faults}))
        return 1
    except FreshnessOperationalError:
        return _operational_fault("freshness_check_failed")
    except OutputSafetyError:
        return _operational_fault("output_publication_failed")
    except BaseException:
        return _operational_fault("output_publication_failed")
    print(
        json.dumps(
            {
                "status": "rendered",
                "artifactDirectory": "artifacts",
                "json": "artifacts/deliverable.json",
                "markdown": "artifacts/narratives.md",
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
