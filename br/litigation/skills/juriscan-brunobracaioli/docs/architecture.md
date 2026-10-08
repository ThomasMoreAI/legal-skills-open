# Juriscan — Architecture

> **v3.1.x note:** the legacy pipeline was significantly upgraded in
> v3.1.0-legacy / v3.1.1 / v3.1.2 with a per-chunk file pattern
> (`analyzed_init.py` + `merge_chunk_analysis.py`), an executive report
> generator (`generate_report.py`), strategic recommendations with
> verbatim evidence, and Lei 14.905/2024 monetary recalculation. See
> `CHANGELOG.md` and the updated legacy pipeline flow in `CLAUDE.md`.
> This document describes primarily the agents pipeline architecture,
> which remains the long-term target but has not been validated end-to-end
> against real PDFs yet.

## TL;DR

Juriscan is a Claude Code skill that analyzes Brazilian legal proceedings.
It has two pipelines during the v2→v3 transition, and the agents pipeline
is the long-term target.

- **Python owns every deterministic computation.** Dates, BRL normalization,
  CNJ parsing, CPC deadline math, schema validation, Decimal money arithmetic,
  Obsidian export.
- **Native Claude Code subagents own every semantic judgment.** Segmentation,
  parsing, adversarial dialectic (advogado-autor × advogado-reu × auditor),
  jurisprudence verification, synthesis.
- **Zero ANTHROPIC_API_KEY.** The skill uses the user's Claude Code
  subscription; subagents are invoked via the `Task` tool from `SKILL.md`.
- **Every LLM output is JSON-schema-validated and logged** before any
  Python script consumes it.

## Pipeline overview

```
                           ┌─────────────────────┐
                           │        PDF          │
                           └─────────┬───────────┘
                                     │
                          ┌──────────▼──────────┐
                          │ scripts/extract_pdf │  (legacy reuses extract_and_chunk.py)
                          └──────────┬──────────┘
                                     │ raw_text.txt + page_map.json
                                     │
                          ┌──────────▼──────────┐
                          │ juriscan-segmenter  │  [Task, model=haiku]
                          └──────────┬──────────┘
                                     │ /tmp/<run_id>-segmenter.json
                                     │     ▲ agent_io.py validate + log
                                     │
                          ┌──────────▼──────────┐
                          │ persist_chunks.py   │  — writes chunks/*.txt + index.json
                          └──────────┬──────────┘   with integrity gate
                                     │
                   ┌─────────────────┴─────────────────┐
                   │   Task × N (parallel, one message)│
                   │    juriscan-parser per chunk      │
                   └─────────────────┬─────────────────┘
                                     │
                          ┌──────────▼──────────┐
                          │ enrich_deterministic│  — utils.dates, utils.monetary, utils.cnj
                          └──────────┬──────────┘   raises if mismatch rate > 10%
                                     │
          ┌──────────────────────────┼──────────────────────────┐
          │           Task × 3 (parallel, one message)          │
          │  advogado-autor    advogado-reu   auditor-processual │
          │  (sonnet)          (sonnet)       (sonnet)           │
          └──────────────────────────┬──────────────────────────┘
                                     │
                          ┌──────────▼──────────┐
                          │ juriscan-verificador │  [Task + WebFetch, whitelist]
                          └──────────┬──────────┘
                                     │
                          ┌──────────▼──────────┐
                          │ juriscan-sintetizador│  (sonnet)
                          └──────────┬──────────┘
                                     │
                          ┌──────────▼──────────┐
                          │ confidence_rules.py │  — preservation invariant
                          └──────────┬──────────┘     + verification downgrade
                                     │
                          ┌──────────▼──────────┐
                          │   finalize.py       │  — Lei 14.905 split, honorarios
                          └──────────┬──────────┘     (Decimal arithmetic)
                                     │
                          ┌──────────▼──────────┐
                          │ obsidian_export.py  │  — _AUDITORIA, _VERIFICAÇÕES,
                          └─────────────────────┘     _PERSPECTIVAS added in v3
```

## Hard invariants

1. **Chunks in analyzed.json have 1:1 correspondence with files on disk.**
   Enforced by `scripts/integrity_gate.py` and called from both
   `schema_validator.py` and `persist_chunks.py`.
2. **`likely_range.min ≤ likely_range.max`** in all risk outputs.
   Enforced by `scripts/legacy/risk_scorer.py` via sorted() + assert.
3. **Legitimate appellate reforms are not contradictions.**
   `scripts/legacy/contradiction_report.py` emits `REFORMA_PARCIAL` notes
   in `instance_tracking` when sentença→acórdão values differ.
4. **Sintetizador cannot drop auditor findings.**
   `scripts/confidence_rules.py` raises `ConfidenceRuleError` if violated.
5. **Every Task call is logged to the audit trail.** Even failures
   (with `error=...` and `schema_valid=false`).
6. **Web lookup only in the whitelist.** `scripts/agent_io.py` rejects
   verificador outputs whose `source_url` host is not in
   `references/whitelist_fontes.json`, as a post-hoc hard gate.
7. **Monetary mismatch rate >10% aborts the pipeline** at the
   `enrich_deterministic.py` step. The dialectic layer never runs on
   unreliable parser output.
8. **Budget gate:** p95 latency per run ≤ 10 minutes and total Task
   invocations ≤ 30 for a 15-piece process. Enforced by
   `scripts/report_metrics.py --enforce` in CI.

## Schema versions

- **v2** — `references/output_schema_v2.json`. Output of the legacy
  pipeline. `schema_version` field absent or `"2.0"`.
- **v3** — `references/output_schema_v3.json`. Superset with
  `run_id`, `pipeline_mode`, `process_state`, `perspectives`,
  `auditor_findings`, `verifications`, `verification_summary`,
  `monetary_recalculations`, `dissensos`, `resumo_executivo`,
  `audit_trail_uri`. `schema_version == "3.0"`.

`scripts/schema_validator.py` auto-dispatches by the `schema_version`
field. `scripts/migrate_v2_to_v3.py` performs additive-only migration
(keys in the input are never overwritten).

## Directory map

```
.claude/agents/           7 subagent markdown files — juriscan-*
references/               schemas, taxonomies, whitelists, binding precedents
  agent_schemas/          8 JSON schemas for subagent outputs
  output_schema_v2.json   legacy schema (preserved)
  output_schema_v3.json   new schema, superset of v2
  whitelist_fontes.json   authoritative hosts for verificador
scripts/
  agent_io.py             glue CLI: new-run / validate / log / extract-field
  audit.py                append-only JSONL logger
  persist_chunks.py       writes chunks to disk from segmenter output
  enrich_deterministic.py normalizes dates/money/CNJ, makes dialectic digests
  confidence_rules.py     preservation invariant + verification downgrade
  finalize.py             Lei 14.905 + honorarios post-reform (Decimal)
  report_metrics.py       audit trail aggregation + budget gate
  migrate_v2_to_v3.py     v2 → v3 migration
  schema_validator.py     dispatches by schema_version
  integrity_gate.py       1:1 chunk-file ↔ JSON check
  prazo_calculator.py     CPC deadlines, state-aware
  obsidian_export.py      Obsidian vault with v3 views
  legacy/                 retired scripts still consumed by --pipeline=legacy
tests/                    435+ pytest unit/integration tests (v3.1.2)
docs/                     architecture.md, subagents.md, operations.md
```

## How the two pipelines coexist

During Phases 2–5 the agents pipeline is **opt-in** via `/juriscan --pipeline=agents`.
The legacy pipeline remains the default. Flip is the subject of Phase 6
Step 6.4 — requires the agents suite to pass the golden regression three
times in a row, then `SKILL.md` changes the default and the legacy mode
becomes `--pipeline=legacy` explicit for three more releases before removal.

Schema v2 never dies silently. `migrate_v2_to_v3.py` converts any v2
artifact into v3 additively, preserving the v2 value set unchanged.

## Prompt caching

System prompts for each subagent live in the body of
`.claude/agents/juriscan-*.md` and are stable across invocations — Claude
Code's automatic prompt cache retains them. Dynamic inputs come only
via the `prompt` parameter of each `Task` call, so the stable portion
stays at the beginning of the context window and cache hits are
maximized.

The `enrich_deterministic.make_dialectic_summary()` helper produces
compact digests of the parsed pieces for the dialectic layer, so the
three parallel advogados/auditor subagents receive structured facts
instead of raw chunk text — further reducing token count and
improving cache stability across their parallel invocations.
