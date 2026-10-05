"""Killable local Codex CLI runtime for the cite-check fan-out.

The runner intentionally has one execution surface. A subprocess can be
terminated and reaped when a unit hangs. Hosts without a local CLI use the
documented native-worker fallback instead of a second runtime implementation.
"""

from __future__ import annotations

import asyncio
import json
import os
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol

DEFAULT_MODEL = "gpt-5.6-luna"
DEFAULT_EFFORT = "xhigh"
REPORTABLE_REASONING_EFFORTS = frozenset({"low", "medium", "high", "xhigh"})
EXIT_COMPLETE = 0
EXIT_INCOMPLETE = 1
EXIT_UNAVAILABLE = 3
EXIT_APPROVAL_REQUIRED = 4
EXIT_CANCELLED = 130


@dataclass(slots=True)
class WorkerFailure:
    code: str
    message: str
    retryable: bool = False
    cancelled: bool = False


@dataclass(slots=True)
class WorkerResponse:
    """Runtime response containing the worker's candidate result object."""

    payload: Any = None
    model: str | None = None
    effort: str | None = None
    input_tokens: int | None = None
    cached_input_tokens: int | None = None
    cache_write_input_tokens: int | None = None
    elapsed_ms: int | None = None
    failure: WorkerFailure | None = None


@dataclass(slots=True)
class WorkTask:
    run_id: str
    root: Path
    unit: dict[str, Any]
    authorities: list[dict[str, Any]]
    model: str
    effort: str
    schema: dict[str, Any]
    prompt: str
    unit_path: Path | None = None
    unit_text: str = ""
    context: dict[str, Any] | None = None


class WorkerRuntime(Protocol):
    surface: str

    async def run(self, task: WorkTask) -> WorkerResponse:
        """Run one task without changing supplied source files."""
        ...

    async def close(self) -> None:
        """Release runtime resources."""
        ...


def _as_attr(value: Any, *names: str) -> Any:
    for name in names:
        if isinstance(value, dict) and name in value:
            return value[name]
        if hasattr(value, name):
            return getattr(value, name)
    return None


def _camel(name: str) -> str:
    head, *tail = name.split("_")
    return head + "".join(part.title() for part in tail)


def _usage_value(usage: Any, name: str) -> int | None:
    value = _as_attr(usage, name, _camel(name))
    return value if isinstance(value, int) and not isinstance(value, bool) else None


def _classify_exception(exc: BaseException) -> WorkerFailure:
    message = str(exc).lower()
    name = exc.__class__.__name__.lower()
    if any(
        marker in message
        for marker in (
            "failed to initialize in-process app-server client",
            "failed to initialize sqlite state runtime",
            "attempt to write a readonly database",
        )
    ):
        return WorkerFailure(
            "host_approval_required",
            "local Codex startup was blocked by the outer host sandbox",
        )
    if isinstance(exc, (asyncio.TimeoutError, TimeoutError)) or "timeout" in message:
        return WorkerFailure(
            "timeout", "worker exceeded its time limit", retryable=True
        )
    if isinstance(exc, (asyncio.CancelledError, KeyboardInterrupt)) or any(
        token in message or token in name for token in ("interrupt", "cancel")
    ):
        return WorkerFailure("cancelled", "worker cancelled", cancelled=True)
    if any(
        token in message or token in name
        for token in ("overload", "rate", "busy", "capacity", "temporarily")
    ):
        return WorkerFailure(
            "transient_runtime",
            "runtime reported a transient capacity error",
            retryable=True,
        )
    if any(
        token in message or token in name
        for token in ("invalid schema", "invalid_json_schema", "schema validation")
    ):
        return WorkerFailure("schema_request", "Codex rejected the output schema")
    if isinstance(exc, PermissionError) or any(
        token in message or token in name
        for token in (
            "transport",
            "connection",
            "sandbox",
            "bubblewrap",
            "bwrap",
            "eacces",
            "eperm",
            "permission denied",
            "access denied",
        )
    ):
        return WorkerFailure("runtime_startup", "local Codex runtime could not start")
    if any(
        token in message or token in name
        for token in ("auth", "401", "credential", "login", "permission")
    ):
        return WorkerFailure(
            "authentication", "local Codex authentication is unavailable"
        )
    return WorkerFailure("runtime_error", "local Codex worker failed")


def _extract_final(payload: Any) -> Any:
    if isinstance(payload, (dict, list)):
        return payload
    if not isinstance(payload, str):
        return payload
    try:
        return json.loads(payload)
    except json.JSONDecodeError:
        return payload


def _coerce_response(value: Any, model: str, effort: str) -> WorkerResponse:
    del model, effort
    if isinstance(value, WorkerResponse):
        return value
    if isinstance(value, WorkerFailure):
        return WorkerResponse(failure=value, model="unknown", effort="unknown")
    return WorkerResponse(payload=value, model="unknown", effort="unknown")


def _looks_like_unit_result(value: Any) -> bool:
    return (
        isinstance(value, dict)
        and isinstance(value.get("unitId"), str)
        and value.get("disposition") in {"no_citations_found", "citations_found"}
        and isinstance(value.get("citations"), list)
    )


def _extract_cli_json(path: Path, stdout: str) -> Any:
    if path.exists():
        try:
            candidate = _extract_final(json.loads(path.read_text(encoding="utf-8")))
            if _looks_like_unit_result(candidate):
                return candidate
        except (OSError, json.JSONDecodeError):
            pass
    candidates: list[Any] = []
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        candidates.append(event)
        if isinstance(event, dict):
            for key in (
                "final_response",
                "finalResponse",
                "output_text",
                "text",
                "content",
            ):
                if key in event:
                    candidates.append(event[key])
            item = event.get("item")
            if isinstance(item, dict):
                for key in ("text", "content", "output_text"):
                    if key in item:
                        candidates.append(item[key])
    for candidate in reversed(candidates):
        parsed = _extract_final(candidate)
        if _looks_like_unit_result(parsed):
            return parsed
    return None


def _cli_actual_model(stdout: str) -> str | None:
    return _cli_runtime_field(stdout, ("actual_model", "actualModel", "model"))


def _cli_actual_effort(stdout: str) -> str | None:
    value = _cli_runtime_field(
        stdout,
        (
            "actual_effort",
            "actualEffort",
            "reasoning_effort",
            "reasoningEffort",
            "effort",
        ),
    )
    return value if value in REPORTABLE_REASONING_EFFORTS else None


def _cli_runtime_field(stdout: str, names: tuple[str, ...]) -> str | None:
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(event, dict) or not isinstance(event.get("type"), str):
            continue
        if event["type"].startswith("item."):
            continue
        for name in names:
            value = event.get(name)
            if isinstance(value, str) and value:
                return value
    return None


def _cli_metrics(stdout: str) -> dict[str, int | None]:
    values: dict[str, int | None] = {
        "input_tokens": None,
        "cached_input_tokens": None,
        "cache_write_input_tokens": None,
    }
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        usage = event.get("usage") if isinstance(event, dict) else None
        for name in values:
            value = _usage_value(usage, name)
            if value is not None:
                values[name] = value
    return values


def _codex_output_schema(schema: dict[str, Any]) -> dict[str, Any]:
    """Make the canonical schema acceptable to Codex strict output mode."""

    compatible = json.loads(json.dumps(schema))

    def transform(value: Any, *, root: bool = False) -> None:
        if isinstance(value, dict):
            value.pop("allOf", None)
            value.pop("uniqueItems", None)
            value.pop("pattern", None)
            if root:
                value.pop("anyOf", None)
            for key in ("$schema", "$id", "title", "description"):
                value.pop(key, None)
            if "const" in value and "type" not in value:
                constant = value["const"]
                value["type"] = "string" if isinstance(constant, str) else "boolean"
            properties = value.get("properties")
            if isinstance(properties, dict):
                value["required"] = list(properties)
                value["additionalProperties"] = False
            for child in value.values():
                transform(child)
        elif isinstance(value, list):
            for child in value:
                transform(child)

    transform(compatible, root=True)
    return compatible


async def _run_cli_process(
    command: list[str], *, cwd: Path, input_text: str, timeout: float
) -> subprocess.CompletedProcess[str]:
    """Run and reap one CLI child, including on timeout or cancellation."""

    process = await asyncio.create_subprocess_exec(
        *command,
        cwd=str(cwd),
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    async def terminate() -> tuple[bytes, bytes]:
        if process.returncode is None:
            try:
                process.kill()
            except ProcessLookupError:
                pass
        stdout, stderr = await process.communicate()
        return stdout or b"", stderr or b""

    try:
        stdout, stderr = await asyncio.wait_for(
            process.communicate(input_text.encode("utf-8")), timeout=timeout
        )
    except TimeoutError as exc:
        await terminate()
        raise subprocess.TimeoutExpired(command, timeout) from exc
    except asyncio.CancelledError:
        cleanup = asyncio.create_task(terminate())
        try:
            await asyncio.shield(cleanup)
        except asyncio.CancelledError:
            await asyncio.shield(cleanup)
        raise
    returncode = process.returncode
    if returncode is None:
        returncode = await process.wait()
    return subprocess.CompletedProcess(
        command,
        returncode,
        stdout.decode("utf-8", errors="replace"),
        stderr.decode("utf-8", errors="replace"),
    )


class CliRuntime:
    surface = "codex_exec"

    def __init__(
        self,
        executable: str,
        model: str,
        effort: str,
        schema_path: Path,
        root: Path,
        timeout: float = 300.0,
    ) -> None:
        self.executable = executable
        self.model = model
        self.effort = effort
        self.schema_path = schema_path
        self.root = root
        self.timeout = timeout

    async def run(self, task: WorkTask) -> WorkerResponse:
        with tempfile.TemporaryDirectory(prefix="cite-check-cli-") as temp_dir:
            output_path = Path(temp_dir) / "last-message.json"
            schema_path = Path(temp_dir) / "codex-output-schema.json"
            try:
                schema = json.loads(self.schema_path.read_text(encoding="utf-8"))
                schema_path.write_text(
                    json.dumps(_codex_output_schema(schema), ensure_ascii=False),
                    encoding="utf-8",
                )
            except (OSError, json.JSONDecodeError, ValueError):
                return WorkerResponse(
                    failure=WorkerFailure(
                        "schema_request", "Codex output schema could not be prepared"
                    ),
                    model="unknown",
                    effort="unknown",
                )
            command = [
                self.executable,
                "exec",
                "--ephemeral",
                "--json",
                "--sandbox",
                "read-only",
                "--skip-git-repo-check",
                "-m",
                self.model,
                "-c",
                f'model_reasoning_effort="{self.effort}"',
                "--output-schema",
                str(schema_path),
                "-o",
                str(output_path),
                "-",
            ]
            try:
                completed = await _run_cli_process(
                    command, cwd=self.root, input_text=task.prompt, timeout=self.timeout
                )
            except subprocess.TimeoutExpired:
                return WorkerResponse(
                    failure=WorkerFailure(
                        "timeout", "codex exec timed out", retryable=True
                    ),
                    model="unknown",
                    effort="unknown",
                )
            except OSError as exc:
                return WorkerResponse(
                    failure=WorkerFailure(
                        "runtime_startup",
                        f"codex executable could not start: {exc.__class__.__name__}",
                    ),
                    model="unknown",
                    effort="unknown",
                )
            if completed.returncode != 0:
                text = "\n".join(
                    part
                    for part in (completed.stdout[:1000], completed.stderr[:1000])
                    if part
                )
                failure = _classify_exception(RuntimeError(text))
                if failure.code == "runtime_error":
                    failure = WorkerFailure(
                        "codex_exec_failed", "codex exec returned a nonzero status"
                    )
                return WorkerResponse(
                    failure=failure, model="unknown", effort="unknown"
                )
            metrics = _cli_metrics(completed.stdout)
            return WorkerResponse(
                payload=_extract_cli_json(output_path, completed.stdout),
                model=_cli_actual_model(completed.stdout) or "unknown",
                effort=_cli_actual_effort(completed.stdout) or "unknown",
                input_tokens=metrics["input_tokens"],
                cached_input_tokens=metrics["cached_input_tokens"],
                cache_write_input_tokens=metrics["cache_write_input_tokens"],
            )

    async def close(self) -> None:
        return None


def _executable_identity(path: str | Path | None) -> str | None:
    """Resolve an executable to its underlying file identity."""

    if path is None:
        return None
    try:
        candidate = Path(path).expanduser()
        if not candidate.is_file() or not os.access(candidate, os.X_OK):
            return None
        return str(candidate.resolve(strict=True))
    except (OSError, RuntimeError, ValueError):
        return None


def _find_cli(executable: str | None = None) -> str | None:
    """Return only the PATH Codex executable, rejecting wrapper substitution."""

    default = shutil.which("codex")
    default_identity = _executable_identity(default)
    if default_identity is None:
        return None
    if executable is not None and _executable_identity(executable) != default_identity:
        return None
    return default_identity


def runtime_model(runtime: WorkerRuntime | None) -> str:
    return str(getattr(runtime, "model", DEFAULT_MODEL))


def runtime_effort(runtime: WorkerRuntime | None) -> str:
    return str(getattr(runtime, "effort", DEFAULT_EFFORT))
