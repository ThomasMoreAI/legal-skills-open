# Codex runner contract for document review

This is an optional local execution adapter. The shared review method remains
complete with native workers or sequential processing when `codex exec` is
unavailable or not authorized for matter material.

## Before dispatch

Confirm that the lawyer or firm has authorized the local Codex route. Run a
synthetic canary before sending matter content; executable presence alone does
not establish usable credentials or permission. Fix one model and reasoning
effort for the run. The runner journals both values and concurrency before the
first job.

The default concurrency is five. Change it per run with `--workers N` when the
machine or provider needs a lower bound or can safely sustain a higher one.
The supported range is 1–12. This skill does not read or write
`config.toml`; users may tune their own Codex defaults independently.

## Worker command

The runner sends the worker prompt and one assignment on standard input. A
typical command template is:

```text
python3 <skill>/scripts/shared/run_codex_finding_worker.py --assignment {assignment} --output {output} --usage-out {usage} --require-usage --schema <skill>/references/shared/finding-worker.schema.json --room-root <production> --review-copies <run>/review-copies.json --model <model> --effort <effort> --issue-batch-size 12
```

The adapter verifies each attached review-copy image against its sidecar hash,
maps attachments to document ordinals and pages, and launches an ephemeral,
read-only context. It makes a separate model call for each bounded request
batch, never more than 12 issues, validates the local issue order, then restores
the approved full-lens order in one canonical raw result. Set a lower batch
size for long or dense units. Its isolation flags prevent unrelated user
configuration, exec rules, MCP startup, and persisted session state from
entering each fresh review context. Pass one fixed higher-capability model and
reasoning effort of medium or above for the substantive run. Low effort is
refused unless the user explicitly overrides the quality gate and the command
adds `--allow-low-effort`.

Pass the template as the value of `--worker-cmd`. The runner replaces
`{output}` with the immutable attempt path and `{usage}` with its token-usage
receipt path. `{assignment}` and `{workdir}` are also available for adapters
that require file arguments. Each invocation gets one unit/lens assignment and
each bounded request batch gets a fresh model context. The adapter reads Codex
JSONL usage events; the runner aggregates every model call across request
batches, rejected attempts, and retries in `usage.json`.

Use the normal local sandbox for read-only review. Grant access only to the
production root and run directory. The runner itself uses no network and no
model SDK; it launches the already-authorized headless CLI as a subprocess.

## Durable execution

Use `run_review_jobs.py run --detach` for a long batch. The detached process
writes `runner.log`, a lease and heartbeat, `journal.jsonl`, immutable raw
attempts, deterministic admission receipts, `progress.json`, and
`parked.json`. A second runner refuses a live lease. Use `stop --by ...
--reason ...` to request termination and `unpark --by ... --reason ...` only
after the lawyer authorizes another judgment attempt.

Transport failures never consume the judgment retry cap. Malformed or
evidence-invalid model output does. Repeated permanent schema/configuration
errors stop the run instead of repeating the same failure across every job.
