#!/usr/bin/env python3
"""Run compact review jobs with bounded concurrency and durable checkpoints."""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import shlex
import signal
import subprocess
import sys
import threading
import time
from collections import deque
from dataclasses import dataclass
from pathlib import Path

from finding_validation import dump_atomic

DEFAULT_WORKERS = 5
MIN_WORKERS = 1
MAX_WORKERS = 12
DEFAULT_JUDGMENT_ATTEMPTS = 3
DEFAULT_TRANSPORT_ATTEMPTS = 5
DEFAULT_BACKOFF_BASE = 5.0
DEFAULT_BACKOFF_CAP = 300.0
DEFAULT_CIRCUIT_BREAKER = 60.0
DISCLOSURE = (
    "Concurrency is tunable with --workers N: higher values may reduce wall time "
    "but increase resource use and throttling risk."
)
PERMANENT_CONFIG_MARKERS = ("invalid_json_schema", "invalid json schema", "http 400")


@dataclass(frozen=True)
class Outcome:
    job_id: str
    kind: str
    codes: tuple[str, ...] = ()
    signature: str | None = None


class RunState:
    def __init__(self, run_dir: Path):
        self.run_dir = run_dir
        self.journal_path = run_dir / "journal.jsonl"
        self.lock = threading.Lock()

    def append(self, event: str, **fields: object) -> None:
        record = {"at": time.time(), "event": event, **fields}
        encoded = json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n"
        with self.lock:
            self.journal_path.parent.mkdir(parents=True, exist_ok=True)
            with self.journal_path.open("a", encoding="utf-8") as handle:
                handle.write(encoded)
                handle.flush()
                os.fsync(handle.fileno())


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_usage_summary(run_dir: Path) -> dict[str, object]:
    totals = {
        "input_tokens": 0,
        "cached_input_tokens": 0,
        "output_tokens": 0,
        "reasoning_output_tokens": 0,
        "total_tokens": 0,
    }
    calls = 0
    jobs: set[str] = set()
    for path in sorted((run_dir / "attempts").glob("*/attempt-*.usage.json")):
        try:
            value = read_json(path)
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(value, dict) or value.get("contract") != "codex-usage/1":
            continue
        parsed: dict[str, int] = {}
        for key in totals:
            number = value.get(key)
            if not isinstance(number, int) or isinstance(number, bool) or number < 0:
                break
            parsed[key] = number
        else:
            model_calls = value.get("model_calls", 1)
            if (
                not isinstance(model_calls, int)
                or isinstance(model_calls, bool)
                or model_calls < 1
            ):
                continue
            calls += model_calls
            for key, number in parsed.items():
                totals[key] += number
            job_id = value.get("job_id")
            if isinstance(job_id, str):
                jobs.add(job_id)
    summary: dict[str, object] = {
        "calls_recorded": calls,
        "contract": "review-usage/1",
        "jobs_with_usage": len(jobs),
        "totals": totals,
    }
    dump_atomic(run_dir / "usage.json", summary)
    return summary


def parked_jobs(run_dir: Path) -> dict[str, dict[str, object]]:
    path = run_dir / "parked.json"
    if not path.exists():
        return {}
    value = read_json(path)
    if not isinstance(value, dict) or not isinstance(value.get("jobs"), list):
        raise OSError("parked.json has an invalid shape")
    return {
        item["job_id"]: item
        for item in value["jobs"]
        if isinstance(item, dict) and isinstance(item.get("job_id"), str)
    }


def write_parked(run_dir: Path, jobs: dict[str, dict[str, object]]) -> None:
    dump_atomic(run_dir / "parked.json", {"jobs": [jobs[key] for key in sorted(jobs)]})


def pid_alive(pid: object) -> bool:
    if not isinstance(pid, int) or pid < 1:
        return False
    try:
        os.kill(pid, 0)
    except (OSError, ProcessLookupError):
        return False
    return True


def lease_value(run_dir: Path) -> dict[str, object] | None:
    path = run_dir / "runner.lease.json"
    if not path.exists():
        return None
    value = read_json(path)
    return value if isinstance(value, dict) else None


def write_lease(run_dir: Path, pid: int, status: str) -> None:
    dump_atomic(
        run_dir / "runner.lease.json",
        {"heartbeat": time.time(), "pid": pid, "status": status},
    )


def meta_files(run_dir: Path, job_id: str) -> list[Path]:
    return sorted((run_dir / "attempts" / job_id).glob("attempt-*.meta.json"))


def attempt_counts(run_dir: Path, job_id: str) -> tuple[int, int, int]:
    judgment = transport = maximum = 0
    for path in meta_files(run_dir, job_id):
        try:
            value = read_json(path)
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(value, dict):
            maximum = max(maximum, int(value.get("attempt", 0)))
            if value.get("kind") == "rejected":
                judgment += 1
            elif value.get("kind") == "transport-failed":
                transport += 1
    return judgment, transport, maximum


def next_attempt(run_dir: Path, job_id: str) -> int:
    directory = run_dir / "attempts" / job_id
    directory.mkdir(parents=True, exist_ok=True)
    numbers = []
    for path in directory.glob("attempt-*"):
        tail = path.name.removeprefix("attempt-").split(".", 1)[0]
        if tail.isdigit():
            numbers.append(int(tail))
    return max(numbers, default=0) + 1


def latest_rejection_codes(run_dir: Path, job_id: str) -> tuple[str, ...]:
    for path in reversed(meta_files(run_dir, job_id)):
        try:
            value = read_json(path)
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(value, dict) or value.get("kind") != "rejected":
            continue
        codes = value.get("codes")
        if isinstance(codes, list) and all(isinstance(code, str) for code in codes):
            return tuple(codes)
    return ()


def kill_process_group(process: subprocess.Popen[str]) -> None:
    try:
        os.killpg(process.pid, signal.SIGTERM)
        process.wait(timeout=2)
    except (ProcessLookupError, subprocess.TimeoutExpired):
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass


def run_command(
    command: list[str], timeout: float, input_text: str | None = None
) -> subprocess.CompletedProcess[str]:
    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE if input_text is not None else None,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        start_new_session=True,
    )
    try:
        stdout, stderr = process.communicate(input=input_text, timeout=timeout)
    except subprocess.TimeoutExpired:
        kill_process_group(process)
        return subprocess.CompletedProcess(command, 124, "", "transport-timeout")
    return subprocess.CompletedProcess(command, process.returncode, stdout, stderr)


def config_signature(stderr: str) -> str | None:
    lowered = stderr.lower()
    if any(marker in lowered for marker in PERMANENT_CONFIG_MARKERS):
        return hashlib.sha256(lowered.strip().encode()).hexdigest()[:16]
    return None


def backoff_seconds(job_id: str, failure_count: int, base: float, cap: float) -> float:
    raw = min(cap, base * (2 ** max(0, failure_count - 1)))
    seed = int(hashlib.sha256(f"{job_id}:{failure_count}".encode()).hexdigest()[:2], 16)
    return raw * (0.9 + (seed / 255) * 0.2)


def execute_job(
    assignment_path: Path,
    run_dir: Path,
    room_root: Path,
    worker_cmd: str,
    timeout: float,
    state: RunState,
) -> Outcome:
    assignment = read_json(assignment_path)
    if not isinstance(assignment, dict) or not isinstance(
        assignment.get("job_id"), str
    ):
        return Outcome(
            assignment_path.stem, "environment-error", ("assignment-invalid",)
        )
    job_id = assignment["job_id"]
    attempt = next_attempt(run_dir, job_id)
    attempt_dir = run_dir / "attempts" / job_id
    raw_path = attempt_dir / f"attempt-{attempt}.json"
    meta_path = attempt_dir / f"attempt-{attempt}.meta.json"
    usage_path = attempt_dir / f"attempt-{attempt}.usage.json"
    workdir = attempt_dir / f"work-{attempt}"
    workdir.mkdir(parents=True, exist_ok=True)
    try:
        rendered = worker_cmd.format(
            assignment=assignment_path.as_posix(),
            output=raw_path.as_posix(),
            usage=usage_path.as_posix(),
            workdir=workdir.as_posix(),
        )
        command = shlex.split(rendered)
    except (KeyError, ValueError) as error:
        return Outcome(job_id, "environment-error", (f"worker-template:{error}",))
    state.append("dispatched", attempt=attempt, job_id=job_id)
    prompt_path = (
        Path(__file__).parents[2] / "references/shared/finding-worker-prompt.md"
    )
    worker_input = (
        prompt_path.read_text(encoding="utf-8")
        + "\n\n# Assignment\n\n```json\n"
        + assignment_path.read_text(encoding="utf-8")
        + "```\n"
    )
    retry_codes = latest_rejection_codes(run_dir, job_id)
    if retry_codes:
        worker_input += (
            "\n\n# Validator feedback for this retry\n\n"
            "The previous output was rejected by deterministic admission checks. "
            "Correct every listed code while preserving the assignment identifiers "
            "and issue order exactly:\n\n```json\n"
            + json.dumps(list(retry_codes), indent=2)
            + "\n```\n"
        )
    completed = run_command(command, timeout, worker_input)
    if (
        completed.returncode != 0
        or not raw_path.exists()
        or raw_path.stat().st_size == 0
    ):
        code = (
            "transport-timeout"
            if completed.returncode == 124
            else "transport-nonzero-exit"
            if completed.returncode != 0
            else "transport-missing-output"
        )
        signature = config_signature(completed.stderr)
        dump_atomic(
            meta_path,
            {
                "attempt": attempt,
                "code": code,
                "exit_code": completed.returncode,
                "kind": "transport-failed",
                "stderr": completed.stderr[-4000:],
            },
        )
        state.append(
            "transport-failed",
            attempt=attempt,
            code=code,
            job_id=job_id,
            signature=signature,
        )
        return Outcome(job_id, "transport-failed", (code,), signature)
    raw_hash = sha256(raw_path)
    state.append("raw-received", attempt=attempt, job_id=job_id, raw_sha256=raw_hash)
    checkpoint = run_dir / "maker-results" / f"{job_id}.json"
    receipt = run_dir / "receipts" / f"{job_id}.json"
    admitter = Path(__file__).with_name("admit_finding_result.py")
    admitted = run_command(
        [
            sys.executable,
            str(admitter),
            "--assignment",
            str(assignment_path),
            "--raw",
            str(raw_path),
            "--room-root",
            str(room_root),
            "--out",
            str(checkpoint),
            "--receipt",
            str(receipt),
        ],
        timeout,
    )
    if admitted.returncode == 0:
        dump_atomic(
            meta_path,
            {
                "admission": "admitted",
                "attempt": attempt,
                "kind": "admitted",
                "raw_sha256": raw_hash,
            },
        )
        state.append("admitted", attempt=attempt, job_id=job_id, raw_sha256=raw_hash)
        return Outcome(job_id, "admitted")
    try:
        payload = json.loads(admitted.stdout)
        codes = tuple(sorted(payload.get("codes", ["raw-unparseable"])))
    except (json.JSONDecodeError, AttributeError):
        codes = ("raw-unparseable",)
    dump_atomic(
        meta_path,
        {
            "admission": "rejected",
            "attempt": attempt,
            "codes": list(codes),
            "kind": "rejected",
            "raw_sha256": raw_hash,
        },
    )
    state.append("rejected", attempt=attempt, codes=list(codes), job_id=job_id)
    return Outcome(job_id, "rejected", codes)


def write_progress(run_dir: Path, total: int, in_flight: int = 0) -> dict[str, int]:
    admitted = len(list((run_dir / "maker-results").glob("*.json")))
    parked = len(parked_jobs(run_dir))
    progress = {
        "admitted": admitted,
        "in_flight": in_flight,
        "parked": parked,
        "pending": max(0, total - admitted - parked - in_flight),
        "total": total,
    }
    dump_atomic(run_dir / "progress.json", progress)
    return progress


def run_jobs(args: argparse.Namespace) -> int:
    run_dir = Path(args.run_dir)
    room_root = Path(args.room_root)
    inputs = sorted((run_dir / "inputs").glob("*.json"))
    if not inputs:
        print("run_review_jobs: no assignments found", file=sys.stderr)
        return 2
    workers = args.workers
    if workers < MIN_WORKERS or workers > MAX_WORKERS:
        print(
            f"run_review_jobs: --workers must be {MIN_WORKERS}..{MAX_WORKERS}",
            file=sys.stderr,
        )
        return 2
    run_dir.mkdir(parents=True, exist_ok=True)
    lease = lease_value(run_dir)
    if (
        lease
        and lease.get("status") == "running"
        and lease.get("pid") != os.getpid()
        and pid_alive(lease.get("pid"))
    ):
        print(
            f"run_review_jobs: runner {lease['pid']} already holds the lease",
            file=sys.stderr,
        )
        return 2
    write_lease(run_dir, os.getpid(), "running")
    (run_dir / "maker-results").mkdir(exist_ok=True)
    (run_dir / "receipts").mkdir(exist_ok=True)
    state = RunState(run_dir)
    parked = parked_jobs(run_dir)
    pending = deque(
        path
        for path in inputs
        if not (run_dir / "maker-results" / f"{path.stem}.json").exists()
        and path.stem not in parked
    )
    state.append(
        "run-started",
        disclosure=DISCLOSURE,
        estimated_invocations=len(pending),
        job_count=len(inputs),
        model=args.model,
        reasoning_effort=args.effort,
        worker_source="flag" if args.workers_explicit else "default",
        workers=workers,
    )
    print(f"Review run: {len(inputs)} jobs, {workers} workers. {DISCLOSURE}")
    write_progress(run_dir, len(inputs))
    write_usage_summary(run_dir)
    config_failures: list[str] = []
    consecutive_transport_failures = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        futures: dict[concurrent.futures.Future[Outcome], Path] = {}
        while pending or futures:
            while pending and len(futures) < workers:
                path = pending.popleft()
                future = pool.submit(
                    execute_job,
                    path,
                    run_dir,
                    room_root,
                    args.worker_cmd,
                    args.timeout,
                    state,
                )
                futures[future] = path
                if args.throttle_ms:
                    time.sleep(args.throttle_ms / 1000)
            write_progress(run_dir, len(inputs), len(futures))
            write_lease(run_dir, os.getpid(), "running")
            done, _ = concurrent.futures.wait(
                futures, return_when=concurrent.futures.FIRST_COMPLETED
            )
            for future in done:
                path = futures.pop(future)
                outcome = future.result()
                write_usage_summary(run_dir)
                judgment, transport, _ = attempt_counts(run_dir, outcome.job_id)
                if outcome.kind == "transport-failed":
                    consecutive_transport_failures += 1
                else:
                    consecutive_transport_failures = 0
                if outcome.kind == "rejected" and judgment < args.max_attempts:
                    pending.append(path)
                elif (
                    outcome.kind == "transport-failed"
                    and transport < args.transport_attempts
                ):
                    if outcome.signature:
                        config_failures.append(outcome.signature)
                        if config_failures[-2:] == [
                            outcome.signature,
                            outcome.signature,
                        ]:
                            for queued in list(pending) + list(futures.values()):
                                parked[queued.stem] = {
                                    "job_id": queued.stem,
                                    "reason": "config-error",
                                }
                            pending.clear()
                            write_parked(run_dir, parked)
                            state.append("run-stopped", reason="config-error")
                            write_lease(run_dir, os.getpid(), "stopped")
                            return 2
                    if consecutive_transport_failures >= 3:
                        state.append(
                            "transport-circuit-open",
                            consecutive_failures=consecutive_transport_failures,
                            seconds=args.circuit_breaker_seconds,
                        )
                        time.sleep(args.circuit_breaker_seconds)
                        consecutive_transport_failures = 0
                    delay = backoff_seconds(
                        outcome.job_id,
                        transport,
                        args.backoff_base,
                        args.backoff_cap,
                    )
                    state.append(
                        "transport-backoff",
                        job_id=outcome.job_id,
                        seconds=delay,
                    )
                    time.sleep(delay)
                    pending.append(path)
                elif outcome.kind != "admitted":
                    reason = (
                        "retry-cap-exhausted"
                        if outcome.kind == "rejected"
                        else "transport-budget-exhausted"
                    )
                    parked[outcome.job_id] = {
                        "job_id": outcome.job_id,
                        "reason": reason,
                    }
                    write_parked(run_dir, parked)
                    state.append("parked", job_id=outcome.job_id, reason=reason)
    progress = write_progress(run_dir, len(inputs))
    usage = write_usage_summary(run_dir)
    state.append("run-stopped", progress=progress, reason="complete", usage=usage)
    write_lease(run_dir, os.getpid(), "stopped")
    return 0


def status(args: argparse.Namespace) -> int:
    run_dir = Path(args.run_dir)
    inputs = list((run_dir / "inputs").glob("*.json"))
    progress_path = run_dir / "progress.json"
    progress = None
    if progress_path.exists():
        try:
            candidate = read_json(progress_path)
        except (OSError, json.JSONDecodeError):
            candidate = None
        required = {"admitted", "in_flight", "parked", "pending", "total"}
        if (
            isinstance(candidate, dict)
            and required <= candidate.keys()
            and all(isinstance(candidate[key], int) for key in required)
            and candidate["total"] == len(inputs)
        ):
            progress = {key: candidate[key] for key in sorted(required)}
    if progress is None:
        admitted = len(list((run_dir / "maker-results").glob("*.json")))
        parked = len(parked_jobs(run_dir))
        progress = {
            "admitted": admitted,
            "in_flight": 0,
            "parked": parked,
            "pending": max(0, len(inputs) - admitted - parked),
            "total": len(inputs),
        }
    print(json.dumps(progress, indent=2, sort_keys=True))
    return 0


def park(args: argparse.Namespace) -> int:
    run_dir = Path(args.run_dir)
    jobs = parked_jobs(run_dir)
    jobs[args.job_id] = {"job_id": args.job_id, "reason": args.reason}
    write_parked(run_dir, jobs)
    RunState(run_dir).append("parked", job_id=args.job_id, reason=args.reason)
    return 0


def unpark(args: argparse.Namespace) -> int:
    run_dir = Path(args.run_dir)
    jobs = parked_jobs(run_dir)
    if args.job_id not in jobs:
        print("run_review_jobs: job is not parked", file=sys.stderr)
        return 2
    del jobs[args.job_id]
    write_parked(run_dir, jobs)
    RunState(run_dir).append(
        "unparked", by=args.by, job_id=args.job_id, reason=args.reason
    )
    return 0


def stop(args: argparse.Namespace) -> int:
    run_dir = Path(args.run_dir)
    lease = lease_value(run_dir)
    if not lease or lease.get("status") != "running" or not pid_alive(lease.get("pid")):
        print("run_review_jobs: no live runner", file=sys.stderr)
        return 2
    pid = lease["pid"]
    assert isinstance(pid, int)
    os.kill(pid, signal.SIGTERM)
    RunState(run_dir).append("stop-requested", by=args.by, pid=pid, reason=args.reason)
    write_lease(run_dir, pid, "stop-requested")
    return 0


def detach(args: argparse.Namespace) -> int:
    run_dir = Path(args.run_dir)
    run_dir.mkdir(parents=True, exist_ok=True)
    lease = lease_value(run_dir)
    if lease and lease.get("status") == "running" and pid_alive(lease.get("pid")):
        print(
            f"run_review_jobs: runner {lease['pid']} already holds the lease",
            file=sys.stderr,
        )
        return 2
    child_args = [argument for argument in sys.argv[1:] if argument != "--detach"]
    log_path = run_dir / "runner.log"
    with log_path.open("a", encoding="utf-8") as log:
        process = subprocess.Popen(
            [sys.executable, str(Path(__file__).resolve()), *child_args],
            stdin=subprocess.DEVNULL,
            stdout=log,
            stderr=log,
            start_new_session=True,
        )
    write_lease(run_dir, process.pid, "running")
    print(f"Detached review runner pid={process.pid}; log={log_path}")
    return 0


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    commands = root.add_subparsers(dest="command", required=True)
    run = commands.add_parser("run")
    run.add_argument("--run-dir", required=True)
    run.add_argument("--room-root", required=True)
    run.add_argument("--worker-cmd", required=True)
    run.add_argument("--workers", type=int, default=DEFAULT_WORKERS)
    run.add_argument("--timeout", type=float, default=1800)
    run.add_argument("--throttle-ms", type=int, default=0)
    run.add_argument("--max-attempts", type=int, default=DEFAULT_JUDGMENT_ATTEMPTS)
    run.add_argument(
        "--transport-attempts", type=int, default=DEFAULT_TRANSPORT_ATTEMPTS
    )
    run.add_argument("--backoff-base", type=float, default=DEFAULT_BACKOFF_BASE)
    run.add_argument("--backoff-cap", type=float, default=DEFAULT_BACKOFF_CAP)
    run.add_argument(
        "--circuit-breaker-seconds", type=float, default=DEFAULT_CIRCUIT_BREAKER
    )
    run.add_argument("--model", default=None)
    run.add_argument("--effort", default=None)
    run.add_argument("--detach", action="store_true")
    status_command = commands.add_parser("status")
    status_command.add_argument("--run-dir", required=True)
    park_command = commands.add_parser("park")
    park_command.add_argument("--run-dir", required=True)
    park_command.add_argument("--job-id", required=True)
    park_command.add_argument("--reason", required=True)
    unpark_command = commands.add_parser("unpark")
    unpark_command.add_argument("--run-dir", required=True)
    unpark_command.add_argument("--job-id", required=True)
    unpark_command.add_argument("--by", required=True)
    unpark_command.add_argument("--reason", required=True)
    stop_command = commands.add_parser("stop")
    stop_command.add_argument("--run-dir", required=True)
    stop_command.add_argument("--by", required=True)
    stop_command.add_argument("--reason", required=True)
    return root


def main() -> int:
    root = parser()
    args = root.parse_args()
    if args.command == "run":
        args.workers_explicit = "--workers" in sys.argv
        if args.detach:
            return detach(args)
        return run_jobs(args)
    if args.command == "status":
        return status(args)
    if args.command == "park":
        return park(args)
    if args.command == "unpark":
        return unpark(args)
    if args.command == "stop":
        return stop(args)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
