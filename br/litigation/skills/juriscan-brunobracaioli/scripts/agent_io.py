"""Glue CLI between SKILL.md (orchestrator) and juriscan subagents.

SKILL.md invokes a subagent via the Task tool, receives a JSON output file,
then shells out to this script to (a) validate the JSON against the schema
for that agent and (b) log the invocation to the append-only audit trail.

Subcommands
-----------
  new-run
      Generate a fresh run_id (uuid4), create .juriscan/audit/{run_id}.jsonl,
      print the run_id to stdout. SKILL.md captures it and threads it through
      every subsequent log call.

  validate --agent NAME --input PATH
      Load references/agent_schemas/{agent}_output.json, validate the JSON at
      PATH. Exit 0 on success, 1 on failure. Error message to stderr.

  log --run-id ID --agent NAME [--subagent-name N] [--input PATH] \
      [--latency-ms N] [--schema-valid true|false] [--model-hint M] \
      [--error MSG]
      Append a single JSONL entry to the audit trail. If --input is given,
      its sha256 prefix is computed and stored as input_hash.

  extract-field --input PATH --jq EXPR
      Tiny jq-subset for SKILL.md to read a field from a validated JSON
      output without needing jq on the host. EXPR is a dot path such as
      ".chunks[0].id". Prints the value on stdout.

Design notes
------------
- No `anthropic` / SDK dependency. The script never talks to an LLM.
- Uses `jsonschema` (already in requirements.txt).
- Integrates with scripts/audit.py for logging.
- Whitelist enforcement for the verificador agent is layered on top of
  schema validation (Phase 4 Step 4.1) — a dedicated branch in validate().
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft7Validator
except ImportError:  # pragma: no cover - deps guaranteed in requirements.txt
    print("ERROR: jsonschema not installed. Run: pip install -r requirements.txt",
          file=sys.stderr)
    raise

# Import sibling audit module without requiring package install
_THIS_DIR = Path(__file__).resolve().parent
if str(_THIS_DIR) not in sys.path:
    sys.path.insert(0, str(_THIS_DIR))
from audit import AuditLogger, DEFAULT_AUDIT_ROOT, hash_input, new_run_id  # noqa: E402

REPO_ROOT = _THIS_DIR.parent
SCHEMAS_DIR = REPO_ROOT / "references" / "agent_schemas"
WHITELIST_PATH = REPO_ROOT / "references" / "whitelist_fontes.json"

KNOWN_AGENTS = {
    "echo",
    "segmenter",
    "parser",
    "advogado_autor",
    "advogado_reu",
    "auditor",
    "verificador",
    "sintetizador",
    "recommendations",
}

# Agents that share a schema file name != agent name.
_SCHEMA_FILE_OVERRIDES = {
    "advogado_autor": "advogado_output.json",
    "advogado_reu": "advogado_output.json",
    "auditor": "auditor_output.json",
    "echo": "echo_output.json",
    "segmenter": "segmenter_output.json",
    "parser": "parser_output.json",
    "verificador": "verificador_output.json",
    "sintetizador": "sintetizador_output.json",
    "recommendations": "recommendations_output.json",
}


def _schema_path(agent: str) -> Path:
    if agent not in KNOWN_AGENTS:
        raise SystemExit(
            f"unknown agent: {agent!r} (known: {sorted(KNOWN_AGENTS)})"
        )
    filename = _SCHEMA_FILE_OVERRIDES[agent]
    return SCHEMAS_DIR / filename


def _load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"input file not found: {path}")
    except json.JSONDecodeError as e:
        raise SystemExit(f"invalid JSON in {path}: {e}")


def _load_whitelist_hosts() -> set[str]:
    """Return the flat set of whitelisted hosts from references/whitelist_fontes.json."""
    if not WHITELIST_PATH.exists():
        return set()
    data = _load_json(WHITELIST_PATH)
    hosts: set[str] = set()
    for bucket in (data.get("categories") or {}).values():
        for host in bucket:
            hosts.add(host.strip().lower())
    return hosts


def _host_in_whitelist(host: str, whitelist: set[str]) -> bool:
    """True if host equals a whitelist entry OR is a subdomain of one."""
    host = host.strip().lower()
    if not host:
        return False
    # Reject bare IP addresses — hex-safe simple check.
    if host.replace(".", "").isdigit():
        return False
    if host in whitelist:
        return True
    for allowed in whitelist:
        if host.endswith("." + allowed):
            return True
    return False


def _check_verificador_whitelist(doc: dict) -> list[str]:
    """Post-hoc enforcement: every verification.source_url host must be whitelisted."""
    errors: list[str] = []
    verifications = doc.get("verifications") or []
    if not verifications:
        return errors
    whitelist = _load_whitelist_hosts()
    if not whitelist:
        errors.append(
            "whitelist file is missing or empty: references/whitelist_fontes.json"
        )
        return errors

    from urllib.parse import urlparse
    import datetime as _dt

    for i, v in enumerate(verifications):
        url = v.get("source_url") or ""
        try:
            parsed = urlparse(url)
        except Exception:
            errors.append(f"verifications[{i}]: unparseable source_url: {url!r}")
            continue
        if parsed.scheme not in ("http", "https"):
            errors.append(
                f"verifications[{i}]: source_url must be http(s): {url!r}"
            )
            continue
        host = parsed.hostname or ""
        if not _host_in_whitelist(host, whitelist):
            errors.append(
                f"verifications[{i}]: source_url host {host!r} is NOT in "
                f"references/whitelist_fontes.json (citation={v.get('citacao_original')!r})"
            )
        # Access date must parse and not be in the future.
        raw_date = v.get("access_date") or ""
        try:
            d = _dt.date.fromisoformat(raw_date)
        except Exception:
            errors.append(
                f"verifications[{i}]: access_date must be ISO YYYY-MM-DD, got {raw_date!r}"
            )
            continue
        if d > _dt.date.today():
            errors.append(
                f"verifications[{i}]: access_date is in the future: {raw_date}"
            )
        # CONFIRMADO / DIVERGENTE require a literal snippet.
        status = v.get("status")
        trecho = v.get("trecho_oficial")
        if status in ("CONFIRMADO", "DIVERGENTE") and not trecho:
            errors.append(
                f"verifications[{i}]: status={status} requires trecho_oficial "
                f"(literal snippet from the fetched page)"
            )
    return errors


def validate_agent_output(agent: str, json_path: Path) -> tuple[bool, list[str]]:
    """Validate JSON at json_path against the schema for agent.

    For agent=='verificador', also enforces the whitelist from
    references/whitelist_fontes.json as a post-hoc hard rule (schema valid
    is not enough — a schema-valid output with a source_url outside the
    whitelist still fails).

    Returns (ok, errors).
    """
    schema = _load_json(_schema_path(agent))
    doc = _load_json(json_path)
    validator = Draft7Validator(schema)
    errors = [
        f"{'/'.join(str(p) for p in err.absolute_path) or '<root>'}: {err.message}"
        for err in validator.iter_errors(doc)
    ]

    if agent == "verificador" and not errors:
        # Only run the post-hoc whitelist check if the schema validation passed —
        # otherwise we'd be checking garbage.
        errors.extend(_check_verificador_whitelist(doc))

    return (not errors), errors


def extract_field(json_path: Path, expr: str) -> object:
    """Tiny dot-path extractor. Supports '.a.b[0].c' form."""
    doc = _load_json(json_path)
    cur: object = doc
    if not expr or not expr.startswith("."):
        raise SystemExit(f"expression must start with '.': {expr!r}")
    token = ""
    i = 1
    while i <= len(expr):
        ch = expr[i] if i < len(expr) else ""
        if ch in (".", "[", ""):
            if token:
                if not isinstance(cur, dict):
                    raise SystemExit(f"cannot index non-object with {token!r}")
                if token not in cur:
                    raise SystemExit(f"key not found: {token!r}")
                cur = cur[token]
                token = ""
            if ch == "[":
                end = expr.find("]", i)
                if end == -1:
                    raise SystemExit(f"unterminated '[' in {expr!r}")
                try:
                    idx = int(expr[i + 1 : end])
                except ValueError:
                    raise SystemExit(f"non-integer index in {expr!r}")
                if not isinstance(cur, list):
                    raise SystemExit("cannot index non-array with [n]")
                if idx >= len(cur) or idx < -len(cur):
                    raise SystemExit(f"index out of range: {idx}")
                cur = cur[idx]
                i = end + 1
                continue
            i += 1
        else:
            token += ch
            i += 1
    return cur


def _cmd_new_run(args) -> int:
    run_id = new_run_id()
    logger = AuditLogger(run_id, root=args.root)
    logger.log_invocation(
        agent="__meta__",
        subagent_name="__run_start__",
        extra={"source": "agent_io.new-run"},
    )
    print(run_id)
    return 0


def _cmd_validate(args) -> int:
    ok, errors = validate_agent_output(args.agent, Path(args.input))
    if ok:
        if not args.quiet:
            print(f"[OK] {args.agent} output valid: {args.input}")
        return 0
    print(f"[FAIL] {args.agent} output invalid: {args.input}", file=sys.stderr)
    for e in errors:
        print(f"  - {e}", file=sys.stderr)
    return 1


def _cmd_log(args) -> int:
    logger = AuditLogger(args.run_id, root=args.root)
    input_hash = None
    if args.input:
        try:
            input_hash = hash_input(Path(args.input).read_bytes())
        except FileNotFoundError:
            input_hash = None
    schema_valid = None
    if args.schema_valid is not None:
        schema_valid = args.schema_valid == "true"
    logger.log_invocation(
        agent=args.agent,
        subagent_name=args.subagent_name or f"juriscan-{args.agent}",
        model_hint=args.model_hint,
        input_hash=input_hash,
        output_path=args.input,
        latency_ms=args.latency_ms,
        schema_valid=schema_valid,
        error=args.error,
    )
    return 0


def _cmd_extract_field(args) -> int:
    value = extract_field(Path(args.input), args.jq)
    if isinstance(value, (dict, list)):
        print(json.dumps(value, ensure_ascii=False))
    else:
        print(value)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="agent_io",
        description="Juriscan subagent I/O helper (validate / log / extract).",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    new = sub.add_parser("new-run", help="Generate run id and open audit file")
    new.add_argument("--root", default=str(DEFAULT_AUDIT_ROOT))
    new.set_defaults(func=_cmd_new_run)

    val = sub.add_parser("validate", help="Validate agent output JSON")
    val.add_argument("--agent", required=True, choices=sorted(KNOWN_AGENTS))
    val.add_argument("--input", required=True)
    val.add_argument("--quiet", action="store_true")
    val.set_defaults(func=_cmd_validate)

    log = sub.add_parser("log", help="Append one entry to audit trail")
    log.add_argument("--run-id", required=True)
    log.add_argument("--agent", required=True)
    log.add_argument("--subagent-name", default=None)
    log.add_argument("--input", default=None, help="Path to output JSON from subagent")
    log.add_argument("--latency-ms", type=int, default=None)
    log.add_argument("--schema-valid", choices=["true", "false"], default=None)
    log.add_argument("--model-hint", default=None)
    log.add_argument("--error", default=None)
    log.add_argument("--root", default=str(DEFAULT_AUDIT_ROOT))
    log.set_defaults(func=_cmd_log)

    ext = sub.add_parser("extract-field", help="Read a field from a JSON file")
    ext.add_argument("--input", required=True)
    ext.add_argument("--jq", required=True, help="Dot-path expression, e.g. .chunks[0].id")
    ext.set_defaults(func=_cmd_extract_field)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
