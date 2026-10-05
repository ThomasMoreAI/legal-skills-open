"""Atomic packet output and the command-line boundary."""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Any

from canonical_json import pretty_json_bytes
from packet_core import PacketBuildError
from safe_output import OutputSafetyError, publish_owned_directory, write_new_bytes
from source_paths import SourcePathError, validate_source_root

CompilePacket = Callable[[Any, Path], dict]


class RequestFormatError(ValueError):
    pass


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise RequestFormatError("duplicate request key")
        value[key] = item
    return value


def _reject_constant(value: str) -> None:
    raise RequestFormatError("non-standard JSON numeric constant")


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise RequestFormatError("non-finite JSON number")
    return parsed


def _read_request(path: Path) -> Any:
    text = path.read_text(encoding="utf-8")
    return json.loads(
        text,
        object_pairs_hook=_unique_object,
        parse_constant=_reject_constant,
        parse_float=_finite_float,
    )


def compile_to_file(
    compile_packet: CompilePacket,
    request: Any,
    source_root: Path,
    output: Path,
) -> dict:
    target = Path(output)
    result = compile_packet(request, Path(source_root))
    write_new_bytes(target, pretty_json_bytes(result), forbidden_roots=(source_root,))
    return result


def compile_to_directory(
    compile_packet: CompilePacket,
    request: Any,
    source_root: Path,
    run_dir: Path,
) -> dict:
    result = compile_packet(request, Path(source_root))
    publish_owned_directory(
        Path(run_dir),
        {"packet.private.json": pretty_json_bytes(result)},
        forbidden_roots=(source_root,),
    )
    return result


def _failure(code: str, exit_code: int) -> int:
    print(f"packet build failed: {code}", file=sys.stderr)
    return exit_code


def run_cli(
    compile_packet: CompilePacket,
    argv: list[str] | None = None,
    *,
    description: str | None = None,
) -> int:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--request", required=True)
    parser.add_argument("--source-root", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    try:
        request = _read_request(Path(args.request))
    except OSError:
        return _failure("operational_failure", 2)
    except (UnicodeError, json.JSONDecodeError, RequestFormatError):
        return _failure("invalid_request", 1)
    try:
        source_root = validate_source_root(Path(args.source_root))
    except SourcePathError:
        return _failure("operational_failure", 2)
    try:
        result = compile_packet(request, source_root)
    except PacketBuildError:
        return _failure("invalid_request", 1)
    except Exception:
        return _failure("operational_failure", 2)
    try:
        write_new_bytes(
            Path(args.out),
            pretty_json_bytes(result),
            protected_paths=(args.request,),
            forbidden_roots=(source_root,),
        )
    except OutputSafetyError as exc:
        return _failure(f"operational_failure:{exc.args[0]}", 2)
    except BaseException:
        return _failure("operational_failure", 2)
    print(json.dumps({"status": result["status"], "runId": result["runId"]}))
    return 0
