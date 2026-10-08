"""Append-only audit trail for juriscan subagent invocations.

Writes one JSONL line per subagent invocation to .juriscan/audit/{run_id}.jsonl.
Used by scripts/agent_io.py (invoked from SKILL.md) to record every Task call
so the whole run is reproducible and inspectable.
"""

from __future__ import annotations

import hashlib
import json
import os
import time
import uuid
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_AUDIT_ROOT = Path(".juriscan/audit")


@dataclass
class AuditEntry:
    timestamp: str
    run_id: str
    agent: str
    subagent_name: str
    model_hint: str | None
    input_hash: str | None
    output_path: str | None
    latency_ms: int | None
    schema_valid: bool | None
    error: str | None = None
    extra: dict = field(default_factory=dict)


class AuditLogger:
    """Append-only JSONL logger keyed by run_id.

    The file is opened in append mode on every write (rather than kept open)
    so that concurrent processes invoked by SKILL.md don't stomp each other's
    writes. Each line is a complete JSON object (JSONL).
    """

    def __init__(self, run_id: str, root: Path | str = DEFAULT_AUDIT_ROOT):
        self.run_id = run_id
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.path = self.root / f"{run_id}.jsonl"

    def log_invocation(
        self,
        agent: str,
        subagent_name: str,
        *,
        model_hint: str | None = None,
        input_hash: str | None = None,
        output_path: str | Path | None = None,
        latency_ms: int | None = None,
        schema_valid: bool | None = None,
        error: str | None = None,
        extra: dict | None = None,
    ) -> AuditEntry:
        entry = AuditEntry(
            timestamp=datetime.now(timezone.utc).isoformat(),
            run_id=self.run_id,
            agent=agent,
            subagent_name=subagent_name,
            model_hint=model_hint,
            input_hash=input_hash,
            output_path=str(output_path) if output_path is not None else None,
            latency_ms=latency_ms,
            schema_valid=schema_valid,
            error=error,
            extra=extra or {},
        )
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(asdict(entry), ensure_ascii=False))
            fh.write("\n")
        return entry

    def read_all(self) -> list[dict]:
        if not self.path.exists():
            return []
        out = []
        with self.path.open("r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    out.append(json.loads(line))
        return out


def new_run_id() -> str:
    return str(uuid.uuid4())


def hash_input(data: str | bytes) -> str:
    if isinstance(data, str):
        data = data.encode("utf-8")
    return hashlib.sha256(data).hexdigest()[:16]


def _cli():
    import argparse

    parser = argparse.ArgumentParser(description="Juriscan audit trail utilities")
    sub = parser.add_subparsers(dest="cmd", required=True)

    new = sub.add_parser("new-run", help="Create a new run id and return it on stdout")
    new.add_argument("--root", default=str(DEFAULT_AUDIT_ROOT))

    log = sub.add_parser("log", help="Append one entry to an audit file")
    log.add_argument("--run-id", required=True)
    log.add_argument("--agent", required=True)
    log.add_argument("--subagent-name", required=True)
    log.add_argument("--model-hint", default=None)
    log.add_argument("--input-hash", default=None)
    log.add_argument("--output-path", default=None)
    log.add_argument("--latency-ms", type=int, default=None)
    log.add_argument("--schema-valid", choices=["true", "false"], default=None)
    log.add_argument("--error", default=None)
    log.add_argument("--root", default=str(DEFAULT_AUDIT_ROOT))

    args = parser.parse_args()

    if args.cmd == "new-run":
        run_id = new_run_id()
        logger = AuditLogger(run_id, root=args.root)
        logger.log_invocation(
            agent="__meta__",
            subagent_name="__run_start__",
            extra={"created_at": datetime.now(timezone.utc).isoformat()},
        )
        print(run_id)
        return 0

    if args.cmd == "log":
        logger = AuditLogger(args.run_id, root=args.root)
        schema_valid = None
        if args.schema_valid is not None:
            schema_valid = args.schema_valid == "true"
        logger.log_invocation(
            agent=args.agent,
            subagent_name=args.subagent_name,
            model_hint=args.model_hint,
            input_hash=args.input_hash,
            output_path=args.output_path,
            latency_ms=args.latency_ms,
            schema_valid=schema_valid,
            error=args.error,
        )
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(_cli())
