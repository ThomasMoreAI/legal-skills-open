#!/usr/bin/env python3
"""Start one /timenarratives run: build the request, site the run, compile.

The host supplies only what the lawyer said: their name, the matter, the
selected paths, and optionally inline notes, a client name, aliases, or a date
window. Everything else the request schema needs is defaulted here so nothing
has to be asked. The run directory is always a new sibling of the source root.
"""

from __future__ import annotations

import argparse
import json
import re
import secrets
from datetime import UTC, datetime
from pathlib import Path

from build_packet import PacketBuildError, compile_packet_to_directory
from folder_selection import expand_folders
from packet_core import REQUEST_VERSION, validate_request
from safe_output import OutputSafetyError, write_new_bytes
from source_paths import SourcePathError, validate_source_root

ALL_SOURCE_TYPES = ["text", "email", "docx", "user_note", "conversation"]


def _slug(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").lower()
    return slug[:40] or "run"


def _now_rfc3339() -> str:
    return datetime.now(UTC).astimezone().isoformat(timespec="seconds")


def _relative(path: str, source_root: Path | None) -> str:
    """Portable POSIX form; an absolute path under the root is relativised."""
    if source_root is not None:
        candidate = Path(path)
        if candidate.is_absolute():
            try:
                # Preserve link components for the source-path checks; resolving
                # here would turn an absolute alias into an apparently ordinary path.
                path = str(candidate.relative_to(source_root.absolute()))
            except (OSError, ValueError):
                pass
    return path.replace("\\", "/").removeprefix("./")


def build_request(
    *,
    lawyer: str,
    matter: str,
    paths: list[str],
    folders: list[str] | None = None,
    conversations: list[tuple[str, str]] | None = None,
    notes: list[str] | None = None,
    client: str | None = None,
    aliases: list[str] | None = None,
    since: str | None = None,
    until: str | None = None,
    as_of: str | None = None,
    source_root: Path | None = None,
) -> dict:
    """Return a schema-valid request with every optional field defaulted."""
    selected_paths = [_relative(path, source_root) for path in paths]
    if folders:
        if source_root is None:
            raise PacketBuildError("selected folders require a source root")
        selected_paths = expand_folders(
            source_root,
            [_relative(folder, source_root) for folder in folders],
            selected_paths,
        )
    selections: list[dict] = [{"kind": "file", "path": path} for path in selected_paths]
    selections.extend({"kind": "user_note", "text": note} for note in notes or [])
    selections.extend(
        {
            "kind": "conversation",
            "conversationId": identity,
            "path": _relative(path, source_root),
        }
        for identity, path in conversations or []
    )
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    request = {
        "schemaVersion": REQUEST_VERSION,
        "runId": f"tn-{_slug(matter)}-{stamp}",
        "actor": {
            "id": f"lawyer-{_slug(lawyer)}",
            "name": lawyer,
            "aliases": aliases or [],
        },
        "matter": {"id": matter, "client": client, "aliases": []},
        "selections": selections,
        "filters": {
            "sourceTypes": ALL_SOURCE_TYPES,
            "since": since,
            "until": until,
            "asOf": as_of if as_of is not None else _now_rfc3339(),
        },
    }
    return validate_request(request)


def _summary(packet: dict, run_dir: Path) -> dict:
    containers = {row["containerId"]: row for row in packet["containers"]}
    roots = packet["roots"]
    unreadable = [
        {"source": containers[r["containerId"]]["displayName"], "reason": r["reason"]}
        for r in roots
        if r["disposition"] == "unreadable"
    ]
    return {
        "status": packet["status"],
        "runDir": str(run_dir),
        "packet": str(run_dir / "artifacts" / "packet.private.json"),
        "request": str(run_dir / "request.json"),
        "selected": len(roots),
        "readable": sum(1 for r in roots if r["disposition"] != "unreadable"),
        "duplicates": sum(1 for r in roots if r["disposition"] == "exactDuplicate"),
        "needsConfirmation": sum(
            1 for r in roots if r["disposition"] == "requiresConfirmation"
        ),
        "unreadable": unreadable,
        "limitations": packet["limitations"],
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lawyer", required=True, help="name identifying the work")
    parser.add_argument("--matter", required=True, help="matter as the user gave it")
    parser.add_argument("--source-root", required=True)
    parser.add_argument("paths", nargs="*", help="selected files under --source-root")
    parser.add_argument(
        "--folder",
        action="append",
        default=[],
        help=(
            "selected folder including subfolders; '.' expressly selects source root"
        ),
    )
    parser.add_argument("--note", action="append", default=[], help="inline note")
    parser.add_argument(
        "--conversation",
        nargs=2,
        action="append",
        default=[],
        metavar=("ID", "PATH"),
        help="selected conversation snapshot",
    )
    parser.add_argument("--client")
    parser.add_argument("--alias", action="append", default=[])
    parser.add_argument("--since")
    parser.add_argument("--until")
    parser.add_argument(
        "--as-of", help="explicit RFC3339 observation clock for reproducible replay"
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if not args.paths and not args.folder and not args.note and not args.conversation:
        print(json.dumps({"status": "no_sources_selected"}))
        return 1
    try:
        source_root = validate_source_root(Path(args.source_root))
        request = build_request(
            lawyer=args.lawyer,
            matter=args.matter,
            paths=args.paths,
            folders=args.folder,
            notes=args.note,
            conversations=args.conversation,
            client=args.client,
            aliases=args.alias,
            since=args.since,
            until=args.until,
            as_of=args.as_of,
            source_root=source_root,
        )
    except (SourcePathError, PacketBuildError) as exc:
        print(json.dumps({"status": "invalid_request", "error": str(exc)}))
        return 1
    token = secrets.token_hex(4)
    run_dir = source_root.parent / f".timenarratives-run-{_slug(args.matter)}-{token}"
    try:
        packet = compile_packet_to_directory(request, source_root, run_dir)
        payload = json.dumps(request, ensure_ascii=False, indent=2) + "\n"
        write_new_bytes(
            run_dir / "request.json",
            payload.encode("utf-8"),
            forbidden_roots=(source_root,),
        )
    except OutputSafetyError as exc:
        print(json.dumps({"status": "operational_failure", "error": exc.args[0]}))
        return 2
    except OSError:
        print(
            json.dumps({"status": "operational_failure", "error": "run_write_failed"})
        )
        return 2
    except PacketBuildError as exc:
        print(json.dumps({"status": "invalid_request", "error": str(exc)}))
        return 1
    print(json.dumps(_summary(packet, run_dir), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
