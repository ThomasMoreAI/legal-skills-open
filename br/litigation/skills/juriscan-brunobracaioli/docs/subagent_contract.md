# Juriscan — Subagent Contract

This document describes the contract between `SKILL.md` (the orchestrator) and
the native Claude Code subagents that live at `.claude/agents/juriscan-*.md`.
It is the source of truth for Phase 0 Step 0.4 of the migration plan.

## Why this contract exists

Juriscan delegates semantic reasoning (segmentation, parsing, adversarial
analysis, verification, synthesis) to Claude Code subagents, while Python
scripts own every deterministic computation (dates, CNJ, BRL, prazos CPC,
schema, export). The contract below is the thin, strict interface that keeps
those two worlds honest: LLM output is never trusted until Python has
validated and logged it.

## Actors

| Actor | File | Role |
|---|---|---|
| Orchestrator | `SKILL.md` | Reads the user prompt, runs Python scripts, emits `Task` calls, enforces the contract |
| Subagent | `.claude/agents/juriscan-<role>.md` | One markdown file per role. Frontmatter defines name / tools / model hint; body is the system prompt |
| Schema | `references/agent_schemas/<role>_output.json` | JSON Schema (Draft-07) that the subagent output must satisfy |
| Glue CLI | `scripts/agent_io.py` | `new-run`, `validate`, `log`, `extract-field` |
| Audit trail | `.juriscan/audit/{run_id}.jsonl` | Append-only JSONL, one line per invocation |

## Lifecycle of one invocation

```
SKILL.md                                             subagent        agent_io.py / audit
   │                                                     │                   │
   ├── Task(subagent_type="juriscan-<role>", ...) ───────▶│                   │
   │                                                     │                   │
   │                                            writes JSON file             │
   │◀──────────────────── confirmation ──────────────────┤                   │
   │                                                     │                   │
   ├── python3 agent_io.py validate --agent <role> --input <path> ──────────▶│
   │◀─────────────────────────── exit 0 / exit 1 ───────────────────────────┤
   │                                                     │                   │
   │   exit 1 ─▶ retry once with error feedback          │                   │
   │   second exit 1 ─▶ abort pipeline, surface run_id   │                   │
   │                                                     │                   │
   ├── python3 agent_io.py log --run-id ... --agent <role> ... ─────────────▶│
   │                                                     │         appends JSONL entry
```

## Non-negotiable invariants

1. **No canonical writes from subagents.** Subagents write only to scratch JSON
   files (typically under `/tmp` or `<output>/agents/`). `analyzed.json` and
   everything else the user consumes is written exclusively by Python.
2. **No unlogged Task calls.** Every `Task(subagent_type=juriscan-*)` must be
   followed by an `agent_io.py log` entry, including failures. The audit trail
   is append-only and keyed by `run_id`.
3. **No schema-invalid outputs consumed.** Python downstream reads only files
   whose `validate` has already returned exit 0.
4. **Web lookup only via the verificador.** `juriscan-verificador` is the
   single subagent with `WebFetch` in its `tools:`. It is restricted to the
   whitelist in `references/whitelist_fontes.json` (Phase 4).
5. **One retry, then abort.** If `validate` fails, the orchestrator re-invokes
   the subagent once with the error message as feedback. A second failure
   aborts the pipeline and reports the `run_id` so the user can inspect the
   audit trail.
6. **Parallel invocations go in the same message.** When the pipeline fans out
   (parser × N chunks, advogado-autor + advogado-réu + auditor), SKILL.md
   emits the `Task` calls in a single assistant message so Claude Code runs
   them in parallel.

## Known agents (Phase 0)

| Agent | Schema | Status |
|---|---|---|
| `echo` | `echo_output.json` | Live — only subagent wired in Phase 0, used by `/juriscan --selftest` |
| `segmenter` | `segmenter_output.json` | Skeleton schema only — implemented in Phase 2 Step 2.2 |
| `parser` | `parser_output.json` | Skeleton schema only — Phase 2 Step 2.3 |
| `advogado_autor` / `advogado_reu` | `advogado_output.json` | Skeleton schema only — Phase 3 Steps 3.1/3.2 |
| `auditor` | `auditor_output.json` | Skeleton schema only — Phase 3 Step 3.3 (art. 942 gate) |
| `verificador` | `verificador_output.json` | Skeleton schema only — Phase 4 Step 4.2 |
| `sintetizador` | `sintetizador_output.json` | Skeleton schema only — Phase 3 Step 3.4 |

## Selftest

Run `/juriscan --selftest` in a fresh Claude Code session (after `./install.sh`)
to verify the plumbing. A successful run:

1. Creates `.juriscan/audit/<uuid>.jsonl` with one `__run_start__` entry.
2. Invokes `juriscan-echo` via Task tool.
3. Validates the echo output against `echo_output.json`.
4. Appends a second entry to the audit trail with `schema_valid=true`.
5. Prints `"Selftest OK — ..."` in the session.

If the Task tool responds that `juriscan-echo` is unknown, `install.sh` did not
symlink `.claude/agents/juriscan-*.md` into `~/.claude/agents/` — re-run the
installer.

## Extending the contract

To add a new subagent:

1. Write `.claude/agents/juriscan-<role>.md` with frontmatter (`name`,
   `description`, `tools`, `model`) and a body containing the system prompt.
2. Add `references/agent_schemas/<role>_output.json` with required fields.
3. Register the agent in `KNOWN_AGENTS` / `_SCHEMA_FILE_OVERRIDES` in
   `scripts/agent_io.py`.
4. Add fixtures + tests in `tests/test_agent_io.py` (at minimum: one valid,
   one invalid).
5. Reference the new role in the appropriate phase of `SKILL.md` (behind the
   `--pipeline=agents` flag until the flip in Phase 6).
