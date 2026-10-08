"""Aggregate juriscan audit trail into latency + invocation metrics.

Phase 7 Step 7.1. Reads one or more `.juriscan/audit/<run_id>.jsonl` files
and produces:

  - per-subagent p50 / p95 / max latency (ms)
  - total invocations per subagent
  - error count
  - schema_valid rate
  - total invocations for the run (budget gate)
  - elapsed wall-clock (first → last timestamp)

Budget gate (enforced when --enforce is given):

  - p95 latency per run <= --max-p95-ms   (default 600000 = 10 minutes)
  - total invocations per run <= --max-invocations  (default 30)

Exit code non-zero when gate fails. Intended to be called from CI on
completed golden-suite runs.

Usage
-----
    python3 scripts/report_metrics.py --run-id <uuid> [--root .juriscan/audit]
    python3 scripts/report_metrics.py --all-runs
    python3 scripts/report_metrics.py --run-id <uuid> --enforce
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Iterable


DEFAULT_ROOT = Path(".juriscan/audit")
DEFAULT_MAX_P95_MS = 10 * 60 * 1000   # 10 minutes
DEFAULT_MAX_INVOCATIONS = 30


def _percentile(values: list[float], p: float) -> float:
    if not values:
        return 0.0
    xs = sorted(values)
    k = (len(xs) - 1) * p
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return xs[int(k)]
    return xs[f] + (xs[c] - xs[f]) * (k - f)


def _load_run(path: Path) -> list[dict]:
    entries: list[dict] = []
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return entries


def summarize_run(entries: list[dict]) -> dict:
    """Return a structured summary of one audit run."""
    by_agent: dict[str, list[dict]] = defaultdict(list)
    ts_first: datetime | None = None
    ts_last: datetime | None = None
    error_count = 0
    schema_invalid_count = 0
    total_real_invocations = 0

    for e in entries:
        agent = e.get("agent") or "unknown"
        if agent == "__meta__":
            # Meta entries (run start/end) don't count as invocations.
            ts_raw = e.get("timestamp")
            if ts_raw:
                t = datetime.fromisoformat(ts_raw.replace("Z", "+00:00"))
                ts_first = t if ts_first is None or t < ts_first else ts_first
                ts_last = t if ts_last is None or t > ts_last else ts_last
            continue
        total_real_invocations += 1
        by_agent[agent].append(e)
        if e.get("error"):
            error_count += 1
        if e.get("schema_valid") is False:
            schema_invalid_count += 1
        ts_raw = e.get("timestamp")
        if ts_raw:
            t = datetime.fromisoformat(ts_raw.replace("Z", "+00:00"))
            ts_first = t if ts_first is None or t < ts_first else ts_first
            ts_last = t if ts_last is None or t > ts_last else ts_last

    per_agent: dict[str, dict] = {}
    all_latencies: list[float] = []
    for agent, group in by_agent.items():
        latencies = [
            float(e["latency_ms"]) for e in group
            if isinstance(e.get("latency_ms"), (int, float))
        ]
        all_latencies.extend(latencies)
        per_agent[agent] = {
            "invocations": len(group),
            "latency_p50_ms": round(_percentile(latencies, 0.50), 1) if latencies else None,
            "latency_p95_ms": round(_percentile(latencies, 0.95), 1) if latencies else None,
            "latency_max_ms": round(max(latencies), 1) if latencies else None,
            "errors": sum(1 for e in group if e.get("error")),
        }

    elapsed_ms: float | None = None
    if ts_first and ts_last:
        elapsed_ms = (ts_last - ts_first).total_seconds() * 1000.0

    return {
        "total_invocations": total_real_invocations,
        "unique_agents": len(per_agent),
        "error_count": error_count,
        "schema_invalid_count": schema_invalid_count,
        "latency_p50_ms": round(_percentile(all_latencies, 0.50), 1) if all_latencies else None,
        "latency_p95_ms": round(_percentile(all_latencies, 0.95), 1) if all_latencies else None,
        "latency_max_ms": round(max(all_latencies), 1) if all_latencies else None,
        "elapsed_wall_ms": round(elapsed_ms, 1) if elapsed_ms is not None else None,
        "per_agent": per_agent,
    }


def enforce_budget(
    summary: dict,
    *,
    max_p95_ms: int,
    max_invocations: int,
) -> list[str]:
    """Return a list of budget violations (empty if all ok)."""
    violations: list[str] = []
    p95 = summary.get("latency_p95_ms")
    if p95 is not None and p95 > max_p95_ms:
        violations.append(
            f"latency p95 {p95:.0f}ms > limit {max_p95_ms}ms "
            f"({p95 / 1000:.1f}s > {max_p95_ms / 1000:.1f}s)"
        )
    total = summary.get("total_invocations", 0)
    if total > max_invocations:
        violations.append(
            f"total invocations {total} > limit {max_invocations}"
        )
    return violations


def format_summary(summary: dict, run_id: str) -> str:
    lines = [
        f"=== run {run_id} ===",
        f"total invocations : {summary['total_invocations']}",
        f"unique agents     : {summary['unique_agents']}",
        f"errors            : {summary['error_count']}",
        f"schema_invalid    : {summary['schema_invalid_count']}",
        f"latency p50       : {summary['latency_p50_ms']} ms",
        f"latency p95       : {summary['latency_p95_ms']} ms",
        f"latency max       : {summary['latency_max_ms']} ms",
        f"elapsed wall      : {summary['elapsed_wall_ms']} ms",
        "",
        "per agent:",
    ]
    for agent, stats in sorted(summary["per_agent"].items()):
        lines.append(
            f"  {agent:28} n={stats['invocations']:>3} "
            f"p50={stats['latency_p50_ms']} "
            f"p95={stats['latency_p95_ms']} "
            f"max={stats['latency_max_ms']} "
            f"errors={stats['errors']}"
        )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Juriscan audit trail metrics")
    parser.add_argument("--root", default=str(DEFAULT_ROOT),
                        help="Audit trail directory (default: .juriscan/audit)")
    parser.add_argument("--run-id", default=None, help="Specific run to report")
    parser.add_argument("--all-runs", action="store_true",
                        help="Report every *.jsonl file under --root")
    parser.add_argument("--json", action="store_true",
                        help="Emit machine-readable JSON on stdout")
    parser.add_argument("--enforce", action="store_true",
                        help="Exit non-zero if budget gates are violated")
    parser.add_argument("--max-p95-ms", type=int, default=DEFAULT_MAX_P95_MS)
    parser.add_argument("--max-invocations", type=int, default=DEFAULT_MAX_INVOCATIONS)
    args = parser.parse_args(argv)

    root = Path(args.root)
    if not root.exists():
        print(f"audit root not found: {root}", file=sys.stderr)
        return 2

    runs: list[Path]
    if args.run_id:
        runs = [root / f"{args.run_id}.jsonl"]
    elif args.all_runs:
        runs = sorted(root.glob("*.jsonl"))
    else:
        print("must pass --run-id or --all-runs", file=sys.stderr)
        return 2

    results: dict[str, dict] = {}
    exit_code = 0

    for run_path in runs:
        if not run_path.exists():
            print(f"missing: {run_path}", file=sys.stderr)
            exit_code = max(exit_code, 2)
            continue
        entries = _load_run(run_path)
        summary = summarize_run(entries)
        run_id = run_path.stem
        results[run_id] = summary
        if not args.json:
            print(format_summary(summary, run_id))
            print()
        if args.enforce:
            violations = enforce_budget(
                summary,
                max_p95_ms=args.max_p95_ms,
                max_invocations=args.max_invocations,
            )
            if violations:
                exit_code = 1
                print(f"[BUDGET FAIL] run {run_id}:", file=sys.stderr)
                for v in violations:
                    print(f"  - {v}", file=sys.stderr)

    if args.json:
        json.dump(results, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
