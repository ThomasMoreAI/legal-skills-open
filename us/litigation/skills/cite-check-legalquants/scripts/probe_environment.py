#!/usr/bin/env python3
"""Passively inspect the local capabilities used by ``/cite-check``.

The probe does not call a model or read matter content. It checks only the
local file/process mechanics and the ``codex exec`` flags required by the
runner. Package branding and install location do not establish runtime capability.
A missing capability is an ordinary reason to use the documented host-worker or
sequential fallback.

The receipt contains no environment values, credentials, prompts, source text,
or absolute executable paths.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "cite-check.environment-capability.v1"
DEFAULT_TIMEOUT_MS = 2_000
MAX_TIMEOUT_MS = 10_000
FANOUT_WIDTH = 2

REQUIRED_CODEX_FLAGS = (
    "exec",
    "ephemeral",
    "json",
    "readOnlySandbox",
    "outputSchema",
)


def _safe_version(output: str) -> str | None:
    """Return one short, control-free version line without command output."""

    for raw in output.splitlines():
        line = " ".join(raw.split())
        if line:
            return line[:160]
    return None


def _run_command(
    command: list[str], *, cwd: Path, timeout_ms: int
) -> tuple[int | None, str, str]:
    """Run a bounded local command and cap all returned diagnostics."""

    try:
        completed = subprocess.run(
            command,
            cwd=cwd,
            stdin=subprocess.DEVNULL,
            capture_output=True,
            text=True,
            check=False,
            timeout=timeout_ms / 1_000,
        )
    except subprocess.TimeoutExpired as exc:
        return None, _safe_version(str(exc.stdout or "")) or "", "timeout"
    except (OSError, ValueError) as exc:
        return None, "", exc.__class__.__name__
    return completed.returncode, completed.stdout[:32_768], completed.stderr[:1_024]


def _flag_presence(
    help_text: str, flags: dict[str, tuple[str, ...]]
) -> dict[str, bool]:
    text = help_text.lower()
    return {
        name: any(token.lower() in text for token in tokens)
        for name, tokens in flags.items()
    }


def _inspect_codex(run_dir: Path, timeout_ms: int) -> dict[str, Any]:
    executable = shutil.which("codex")
    flags = {
        "exec": ("\n  exec ", "usage: codex exec"),
        "ephemeral": ("--ephemeral",),
        "json": ("--json",),
        "readOnlySandbox": ("read-only",),
        "outputSchema": ("--output-schema",),
    }
    result: dict[str, Any] = {
        "available": executable is not None,
        "executable": "codex" if executable is not None else None,
        "version": None,
        "help": {
            "status": "not_run",
            "flags": {key: False for key in flags},
        },
        "canary": {"status": "not_run", "reason": "passive_probe"},
    }
    if executable is None:
        result["help"]["status"] = "unavailable"
        result["canary"] = {"status": "not_run", "reason": "cli_unavailable"}
        return result

    version_code, version_stdout, version_stderr = _run_command(
        [executable, "--version"], cwd=run_dir, timeout_ms=timeout_ms
    )
    result["version"] = _safe_version(version_stdout or version_stderr)
    help_code, help_stdout, help_stderr = _run_command(
        [executable, "exec", "--help"], cwd=run_dir, timeout_ms=timeout_ms
    )
    if help_code is None:
        result["help"] = {
            "status": "timeout" if help_stderr == "timeout" else "error",
            "flags": {key: False for key in flags},
        }
    else:
        result["help"] = {
            "status": "pass" if help_code == 0 else "error",
            "flags": _flag_presence(help_stdout + help_stderr, flags),
        }
    result["versionCommandExitCode"] = version_code
    return result


def _probe_local(run_dir: Path, timeout_ms: int) -> dict[str, Any]:
    result: dict[str, Any] = {
        "filesystem": {"status": "fail"},
        "subprocess": {"status": "fail"},
        "processFanout": {"status": "fail", "width": FANOUT_WIDTH},
    }
    try:
        with tempfile.TemporaryDirectory(
            prefix=".environment-probe-", dir=run_dir
        ) as work:
            work_path = Path(work)
            marker = work_path / "marker.txt"
            marker.write_bytes(b"cite-check-environment-probe\n")
            result["filesystem"] = {
                "status": (
                    "pass"
                    if marker.read_bytes() == b"cite-check-environment-probe\n"
                    else "fail"
                )
            }
            child = [
                sys.executable,
                "-c",
                "import sys; sys.stdout.write(sys.argv[1])",
                "probe-child-0",
            ]
            code, stdout, _ = _run_command(child, cwd=work_path, timeout_ms=timeout_ms)
            result["subprocess"] = {
                "status": "pass" if code == 0 and stdout == "probe-child-0" else "fail",
                "exitCode": code,
            }

            def run_child(index: int) -> bool:
                command = [
                    sys.executable,
                    "-c",
                    "import sys; sys.stdout.write(sys.argv[1])",
                    f"probe-child-{index}",
                ]
                code, stdout, _ = _run_command(
                    command, cwd=work_path, timeout_ms=timeout_ms
                )
                return code == 0 and stdout == f"probe-child-{index}"

            with concurrent.futures.ThreadPoolExecutor(
                max_workers=FANOUT_WIDTH
            ) as pool:
                checks = list(pool.map(run_child, range(FANOUT_WIDTH)))
            result["processFanout"] = {
                "status": "pass" if all(checks) else "fail",
                "width": FANOUT_WIDTH,
            }
    except (OSError, RuntimeError, ValueError) as exc:
        result["errorClass"] = exc.__class__.__name__
    return result


def _check_passed(local: dict[str, Any], name: str) -> bool:
    value = local.get(name)
    return isinstance(value, dict) and value.get("status") == "pass"


def _codex_supported(codex: dict[str, Any]) -> bool:
    help_result = codex.get("help")
    flags = help_result.get("flags") if isinstance(help_result, dict) else None
    return (
        codex.get("available") is True
        and isinstance(help_result, dict)
        and help_result.get("status") == "pass"
        and isinstance(flags, dict)
        and all(flags.get(name) is True for name in REQUIRED_CODEX_FLAGS)
    )


def _recommendation(codex: dict[str, Any], local: dict[str, Any]) -> dict[str, Any]:
    subprocess_ready = _check_passed(local, "subprocess")
    fanout_ready = _check_passed(local, "processFanout")
    filesystem_ready = _check_passed(local, "filesystem")
    codex_ready = _codex_supported(codex)
    runner_ready = (
        codex_ready and filesystem_ready and subprocess_ready and fanout_ready
    )
    codex["packagedRunnerEligible"] = runner_ready

    if runner_ready:
        return {
            "path": "packaged_codex_runner",
            "reasonCodes": [
                "codex_cli_flags_observed",
                "local_filesystem_observed",
                "local_subprocess_observed",
                "local_process_fanout_observed",
            ],
        }

    reasons: list[str] = []
    if codex.get("available") is not True:
        reasons.append("codex_cli_not_available")
    elif not codex_ready:
        reasons.append("required_codex_cli_flags_not_observed")
    if not filesystem_ready:
        reasons.append("local_filesystem_unavailable")
    if not subprocess_ready:
        reasons.append("local_subprocess_unavailable")
    if not fanout_ready:
        reasons.append("local_process_fanout_unavailable")

    if fanout_ready:
        return {
            "path": "native_workers_or_sequential",
            "reasonCodes": reasons + ["host_worker_fallback"],
        }
    return {
        "path": "sequential",
        "reasonCodes": reasons + ["sequential_fallback"],
    }


def validate_receipt(receipt: Any) -> str | None:
    """Return a reason unless the packaged runner's capability checks passed."""

    if not isinstance(receipt, dict):
        return "receipt must be a JSON object"
    if receipt.get("schemaVersion") != SCHEMA_VERSION:
        return "receipt schemaVersion is missing or unsupported"

    local = receipt.get("local")
    if not isinstance(local, dict):
        return "receipt local capability evidence is missing"
    for name, label in (
        ("filesystem", "filesystem"),
        ("subprocess", "subprocess"),
        ("processFanout", "process fan-out"),
    ):
        if not _check_passed(local, name):
            return f"receipt local {label} check did not pass"

    runtimes = receipt.get("runtimes")
    if not isinstance(runtimes, dict):
        return "receipt runtime evidence is missing"
    codex = runtimes.get("codex")
    if not isinstance(codex, dict) or not _codex_supported(codex):
        return "receipt does not establish the required codex exec capabilities"
    canary = codex.get("canary")
    if not isinstance(canary, dict) or canary.get("status") != "not_run":
        return "receipt is not a passive environment probe receipt"

    passive = receipt.get("probe")
    if not isinstance(passive, dict):
        return "receipt passive-probe markers are missing"
    if passive.get("modelCalled") is not False:
        return "environment probe must not call a model"
    if passive.get("matterContentUsed") is not False:
        return "environment probe must not use matter content"

    recommendation = receipt.get("recommendation")
    if (
        not isinstance(recommendation, dict)
        or recommendation.get("path") != "packaged_codex_runner"
    ):
        return "receipt does not recommend the packaged Codex runner"

    return None


def probe(
    run_dir: Path,
    *,
    timeout_ms: int = DEFAULT_TIMEOUT_MS,
) -> dict[str, Any]:
    run_dir = run_dir.resolve()
    run_dir.mkdir(parents=True, exist_ok=True)
    local = _probe_local(run_dir, timeout_ms)
    codex = _inspect_codex(run_dir, timeout_ms)
    recommendation = _recommendation(codex, local)
    return {
        "schemaVersion": SCHEMA_VERSION,
        "python": {
            "available": True,
            "executable": Path(sys.executable).name,
            "version": ".".join(str(value) for value in sys.version_info[:3]),
        },
        "local": local,
        "runtimes": {"codex": codex},
        "nativeWorkers": {
            "status": "unknown",
            "source": "host_reported_capability",
        },
        "probe": {
            "modelCalled": False,
            "matterContentUsed": False,
        },
        "recommendation": recommendation,
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Passively inspect cite-check environment capabilities without model calls."
        )
    )
    parser.add_argument(
        "--run-dir",
        type=Path,
        required=True,
        help="Dedicated disposable probe directory.",
    )
    parser.add_argument("--timeout-ms", type=int, default=DEFAULT_TIMEOUT_MS)
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit the machine-readable receipt (the default).",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if not 100 <= args.timeout_ms <= MAX_TIMEOUT_MS:
        print(
            json.dumps({"error": "timeout-ms must be between 100 and 10000"}),
            file=sys.stderr,
        )
        return 2
    try:
        receipt = probe(args.run_dir, timeout_ms=args.timeout_ms)
    except (OSError, ValueError, RuntimeError) as exc:
        print(
            json.dumps(
                {"error": {"code": "probe_error", "class": exc.__class__.__name__}}
            ),
            file=sys.stderr,
        )
        return 3
    print(
        json.dumps(receipt, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
