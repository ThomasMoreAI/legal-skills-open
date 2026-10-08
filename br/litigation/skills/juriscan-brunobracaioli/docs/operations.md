# Juriscan — Operations

Troubleshooting, recovery, and routine tasks for the juriscan skill.

## Quick health check

In a fresh Claude Code session, from a project directory:

```
/juriscan --selftest
```

Expected: `"Selftest OK — subagent echo respondeu e foi validado. run_id=<uuid>"`.
Failure usually means one of:

1. `./install.sh` was not run, or was run from the wrong directory →
   `.claude/agents/juriscan-*.md` not symlinked into `~/.claude/agents/`.
2. `jsonschema` not installed → `pip install -r requirements.txt`.
3. `references/agent_schemas/echo_output.json` edited incorrectly →
   `git status` + revert.

## Running a real analysis

```
/juriscan --pipeline=legacy   /abs/path/to/processo.pdf   # default while agents pipeline is in beta
/juriscan --pipeline=agents   /abs/path/to/processo.pdf   # new hybrid pipeline
/juriscan                      /abs/path/to/processo.pdf   # same as --pipeline=legacy (flip pending)
```

Output is written to `<pdf_dir>/juriscan-output/`:

```
juriscan-output/
├── manifest.json         run_id, pipeline_mode, timestamps
├── raw_text.txt
├── index.json            chunk catalog
├── chunks/               physical chunk files (legacy or via persist_chunks.py)
├── analyzed.json         final structured analysis (v2 or v3)
├── contradictions.json   (legacy only)
├── risk.json             (legacy only)
├── prazos.json
├── obsidian/             Obsidian vault with views
└── .juriscan/audit/<run_id>.jsonl    (agents only)
```

## Audit trail

Every Task invocation in the agents pipeline is logged:

```
python3 scripts/report_metrics.py --run-id <uuid> --root juriscan-output/.juriscan/audit
python3 scripts/report_metrics.py --all-runs --root juriscan-output/.juriscan/audit
python3 scripts/report_metrics.py --run-id <uuid> --json | jq
```

Sample human-readable output:

```
=== run 9c96db50-... ===
total invocations : 18
unique agents     : 6
errors            : 0
schema_invalid    : 0
latency p50       : 3200 ms
latency p95       : 18500 ms
latency max       : 22400 ms
elapsed wall      : 142000 ms
per agent:
  segmenter     n=  1  p50=12400 p95=12400 max=12400 errors=0
  parser        n=  6  p50=2800  p95=4200  max=4800  errors=0
  advogado_autor n=1   p50=18500 p95=18500 max=18500 errors=0
  ...
```

**Budget gate** (CI-friendly):

```
python3 scripts/report_metrics.py --run-id <uuid> --enforce \
    --max-p95-ms 600000 --max-invocations 30
```

Exit code 1 if p95 latency > 10 min or total invocations > 30.

## Audit trail retention

Stale audit logs (> 90 days) can be removed:

```
python3 scripts/cleanup_audit.py --root juriscan-output/.juriscan/audit --dry-run
python3 scripts/cleanup_audit.py --root juriscan-output/.juriscan/audit --days 90
```

## Migrating an existing v2 analyzed.json to v3

```
python3 scripts/migrate_v2_to_v3.py --input analyzed.json --output analyzed_v3.json
# or in place:
python3 scripts/migrate_v2_to_v3.py --input analyzed.json --in-place
# or preview:
python3 scripts/migrate_v2_to_v3.py --input analyzed.json --dry-run
```

Migration is additive-only — v2 fields are never modified. Keys introduced
by v3 (`perspectives`, `auditor_findings`, `verifications`, etc.) are
added with empty defaults for legacy documents. The migrated document
validates against `references/output_schema_v3.json`.

## Re-running a single pipeline step

When a subagent fails mid-pipeline, the audit trail records the failed
invocation with `schema_valid=false` and `error=<msg>`. To re-run just
that step in a new Claude Code session:

1. `grep '"agent": "<role>"' juriscan-output/.juriscan/audit/<run_id>.jsonl`
   to find the failing call and the output path.
2. Re-invoke the subagent manually via the Task tool with the same
   `prompt` + the previous error message appended as `feedback`.
3. Re-run `agent_io.py validate --agent <role> --input <path>` + log.
4. Resume from the next pipeline step.

The pipeline is idempotent by design: downstream steps only read the
validated JSON files on disk, not session state.

## Common issues

### `persist_chunks.py` fails with "gap/overlap between chunk ..."

The segmenter produced `end_char[i-1] != start_char[i]`. SKILL.md should
have re-invoked it once already — if the second attempt also failed,
inspect the segmenter output in `/tmp/<run_id>-segmenter.json` and the
raw text to diagnose. Usually the prompt needs more few-shot examples of
the specific document layout.

### `enrich_deterministic.py` raises `monetary mismatch rate X% exceeds threshold 10%`

The parser is hallucinating monetary values. Inspect
`pieces[i]._enriched.mismatches` in the pre-abort output. If the parser
output says `R$ 27.000.000` but the chunk text says `R$ 27.000,00`, the
parser prompt needs a tighter few-shot for BRL format.

### `confidence_rules.py` raises `preservation invariant violated`

The sintetizador dropped auditor findings. Re-invoke it with a feedback
message that includes the full list of auditor findings and the rule:
"You may organize but not remove; minimum `len(auditor_findings)` is N".

### Verificador output is rejected with `source_url host ... is NOT in references/whitelist_fontes.json`

The subagent tried to fetch a non-authoritative source. Either:
- The citation can only be verified on a non-whitelisted site → mark
  `NAO_ENCONTRADO` instead of inventing a URL.
- The whitelist needs a new entry → propose a PR editing
  `references/whitelist_fontes.json`, justified in the commit message.

### Golden suite fails the art. 942 gate

The auditor failed to produce a finding for the fixture
`processo_02_sintetico_art942`. Check
`auditor_findings[i].descricao` for the literal tokens `ampliação`,
`colegiado`, `maioria`. If any token is missing, the gate still fires
even if the logic is correct — the wording must be explicit.

## Install / update

```
git pull
./install.sh
```

The installer symlinks `~/.claude/skills/juriscan` to the repo and
symlinks each `.claude/agents/juriscan-*.md` file into
`~/.claude/agents/`. Run `/juriscan --selftest` in a fresh session to
confirm.

## Directory cleanup between runs

Agents pipeline intentionally wipes `chunks/*.txt` at the start of
`persist_chunks.py` to prevent orphan files from previous runs. The
integrity gate would catch stale orphans otherwise. `index.json`,
`analyzed.json`, and `obsidian/` are overwritten in place.

Audit trails accumulate across runs — use `cleanup_audit.py` or
manual `rm` if disk space matters.

## Rolling back

- `git revert <commit>` always works — no migrations are destructive.
- Schema v2 outputs continue to validate against `output_schema_v2.json`
  indefinitely.
- `scripts/legacy/` stays in place for 3 releases after the Phase 6.4
  default flip.
- To force legacy mode after the flip: `/juriscan --pipeline=legacy <pdf>`.
