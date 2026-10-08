# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Forensic legal analysis skill for Claude Code — the definitive tool for Brazilian judicial proceedings (processos judiciais). Extracts text from PDF court filings, chunks them by legal piece (peça processual), analyzes each piece structurally, detects contradictions, tracks arguments across judicial instances, calculates CPC-compliant deadlines, scores litigation risk, and exports to Obsidian vaults or structured JSON.

This repository IS the skill directory. Clone it to `~/.claude/skills/juriscan` and it works immediately.

## Commands

```bash
# Install (one time)
./install.sh

# Run all tests
pip install -r requirements.txt
python -m pytest tests/ -v

# Scripts (legacy pipeline — default)
python3 scripts/extract_and_chunk.py --input <pdf> --output <dir>
python3 scripts/integrity_check.py --input <dir>
python3 scripts/analyzed_init.py --index <dir>/index.json --output <dir>/analyzed.json
python3 scripts/merge_chunk_analysis.py --analyzed <dir>/analyzed.json --chunks-dir <dir>/chunks/ --output <dir>/analyzed.json
python3 scripts/schema_validator.py --input <analyzed.json>
python3 scripts/content_quality_check.py --input <analyzed.json> --strict --per-chunk-retry-plan
python3 scripts/prazo_calculator.py --date 2025-03-15 --tipo contestação --state SP
python3 scripts/instance_tracker.py --analysis <analyzed.json> --output <instances.json>
python3 scripts/legacy/contradiction_report.py --analysis <analyzed.json> --output <contradictions.json>
python3 scripts/legacy/risk_scorer.py --analysis <analyzed.json> --output <risk.json>
python3 scripts/finalize_legacy.py --input <analyzed.json> --inplace
python3 scripts/obsidian_export.py --analysis <analyzed.json> --output <vault_dir>
python3 scripts/agent_io.py validate --agent recommendations --input <recommendations.json>
python3 scripts/generate_report.py --analyzed <analyzed.json> --contradictions <c.json> --prazos <p.json> --risk <r.json> --recommendations <rec.json> --output REPORT.md

# Agents pipeline (opt-in during transition; see docs/architecture.md)
python3 scripts/agent_io.py new-run
python3 scripts/agent_io.py validate --agent <role> --input <output.json>
python3 scripts/persist_chunks.py --segmenter-output <seg.json> --raw-text <raw.txt> --output-dir <out>
python3 scripts/enrich_deterministic.py --input <pieces.json> --output <enriched.json>
python3 scripts/confidence_rules.py --synthesis <s.json> --auditor <a.json> --output <final.json>
python3 scripts/finalize.py --input <analyzed.json> --output <final.json>
python3 scripts/report_metrics.py --all-runs --enforce
python3 scripts/migrate_v2_to_v3.py --input <v2.json> --output <v3.json>
```

## Architecture

**Principle: Claude = semantic analysis engine. Python = deterministic data wrangling.**

### Two pipelines (during transition)

1. **Legacy** (`--pipeline=legacy`, current default — validated, v3.1.2) —
   per-chunk file pattern: `analyzed_init.py` creates skeleton, Claude writes
   one `chunks/NN.analysis.json` per chunk, `merge_chunk_analysis.py`
   consolidates with schema validation. Pipeline then runs contradiction
   detection, instance tracking, prazo calculation, risk scoring, Lei
   14.905 recalculation, Obsidian export, and finally `generate_report.py`
   which produces `REPORT.md` — the literal final response to the user.
2. **Agents** (`--pipeline=agents`, opt-in) — hybrid pipeline where semantic
   reasoning is delegated to native Claude Code subagents in `.claude/agents/`
   orchestrated by SKILL.md via the Task tool. Python still owns every
   deterministic computation (dates, BRL, CNJ, prazos CPC, schema, export).
   See `docs/architecture.md` for the full flow and `docs/subagents.md` for
   per-subagent contracts.

### Legacy Pipeline (v3.1.2 — per-chunk file pattern)

```
PDF → [1] Extraction → [2] Integrity Check
→ [3a] analyzed_init.py  (skeleton from index.json)
→ [3b] Per-chunk analysis  (Claude Writes chunks/NN.analysis.json — one per chunk, no helper scripts)
→ [3c] merge_chunk_analysis.py  (consolidates, renumbers split-semantic to integer indices)
→ [4] Schema Validation + content_quality_check.py --strict --per-chunk-retry-plan
→ [5] Cross-Synthesis (contradiction_report, instance_tracker)
→ [6] Prazo Calculation
→ [7] Risk Scoring
→ [8] Consolidate
→ [8.5] finalize_legacy.py  (Lei 14.905/2024 monetary recalculation)
→ [9] Obsidian Export
→ [9a] Strategic Recommendations (recommendations.json — evidence_quote obrigatória)
→ [9b] generate_report.py  (REPORT.md — executive markdown consolidado)
→ [10] Present REPORT.md literally as final response (zero paraphrase, zero additions)
```

### Agents Pipeline (see SKILL.md § Agents Pipeline)

```
PDF → extract_pdf → juriscan-segmenter → persist_chunks → juriscan-parser (parallel)
    → enrich_deterministic → [juriscan-advogado-autor × juriscan-advogado-reu × juriscan-auditor-processual] (parallel)
    → juriscan-verificador → juriscan-sintetizador → confidence_rules → finalize → obsidian_export
```

The agents pipeline uses **zero** `ANTHROPIC_API_KEY` — it runs on the user's
Claude Code subscription. Every subagent output is JSON-schema-validated by
`scripts/agent_io.py validate` and logged to an append-only audit trail at
`.juriscan/audit/<run_id>.jsonl`. See `docs/operations.md` for troubleshooting.

### Script Responsibilities

| Script | Purpose |
|---|---|
| `extract_and_chunk.py` | PDF extraction (pdftotext→pypdf→OCR), regex chunking by legal piece, OCR confidence, page mapping |
| `integrity_check.py` | OCR quality scoring, metadata anomaly detection, page gap detection |
| `analyzed_init.py` | **v3.1.0-legacy** — creates analyzed.json skeleton from index.json preserving technical fields |
| `merge_chunk_analysis.py` | **v3.1.0-legacy** — consolidates `chunks/NN.analysis.json` files with schema validation; renumbers split-semantic (v3.1.1) and inherits primary_date (v3.1.2) |
| `content_quality_check.py` | **v3.0.1** — non-blocking quality check with per-chunk retry plan (v3.1.0-legacy) and art. 942 grounding enforcement |
| `prazo_calculator.py` | CPC Art. 219-232 deadline calculation, feriados forenses, recesso forense, accent-insensitive |
| `instance_tracker.py` | Classify pieces by judicial instance (1ª inst→TJ→STJ→STF), argument evolution tracking |
| `legacy/contradiction_report.py` | Structural contradiction detection (values, dates, facts, jurisprudence) — no false positives on legitimate partial reform |
| `legacy/risk_scorer.py` | Procedural risk, merit indicators, monetary exposure scoring |
| `finalize_legacy.py` | **v3.1.0-legacy** — standalone Lei 14.905/2024 monetary recalculation (detects condenação crossing 2024-08-30) |
| `schema_validator.py` | Validates JSON output against `references/output_schema_v2.json` + integrity gate |
| `obsidian_export.py` | Generates Obsidian vault with 7 main views + piece notes + stub notes |
| `generate_report.py` | **v3.1.0-legacy centerpiece** — executive markdown report consolidating all pipeline outputs; chronological sort + word-safe truncate + dict factor handling |
| `agent_io.py` | Schema validation CLI for all agent outputs (segmenter, parser, advogados, auditor, verificador, sintetizador, **recommendations**) |

### Utils (`scripts/utils/`)

| Module | Purpose |
|---|---|
| `dates.py` | Brazilian date parsing (DD/MM/YYYY, written Portuguese, ISO), piece-type-aware primary date extraction |
| `monetary.py` | BRL value extraction/normalization (R$ format, written forms, multipliers) |
| `filenames.py` | Collision-safe filename generation with `FilenameRegistry` |
| `cnj.py` | CNJ process number parsing, check digit validation, court name resolution |

### Reference Data (`references/`)

| File | Purpose |
|---|---|
| `output_schema_v2.json` | JSON Schema v2 — full analyzed.json output specification (legacy default) |
| `output_schema_v3.json` | JSON Schema v3 — superset for agents pipeline (perspectives, auditor_findings, verifications) |
| `chunk_analysis_schema.json` | **v3.1.0-legacy** — schema for `chunks/NN.analysis.json` files (strict, `additionalProperties: false`); includes `primary_date` override for split-semantic (v3.1.2) |
| `agent_schemas/recommendations_output.json` | **v3.1.0-legacy** — schema for recommendations.json (evidence_quote required per item) |
| `prompt_templates.md` | All 8 prompt templates (7 original + strategic recommendations v3.1.0-legacy) |
| `piece_type_taxonomy.json` | 27 piece types with phase, polo, instance, expected fields |
| `cpc_prazos.json` | 14 standard CPC deadlines with exceptions (Fazenda, JEC, Defensoria) |
| `feriados_forenses.json` | National + mobile (Easter-based) + state court holidays (SP,RJ,MG,RS,PR,SC,BA,PE) |
| `brazilian_legal_entities.md` | Courts, electronic systems, legislation codes, citation regex patterns |
| `appellate_structure.md` | Instance hierarchy, detection patterns, piece classification rules |
| `binding_precedents.md` | Binding precedent types (SV, IRDR, IAC, RG, Rep.) with detection regex |
| `risk_scoring_rubric.md` | Risk scoring rubric: procedural, merit, monetary dimensions |

## Key Design Decisions

- **Chunk by legal piece, not by page** — core invariant. Brazilian filings contain multiple procedural pieces that are semantic units.
- **Deduplication threshold: 200 chars** — close regex matches within 200 chars are deduplicated.
- **Fragments under 50 chars skipped** — noise from headers.
- **ISO 8601 internally, DD/MM/YYYY for display** — eliminates DD/MM vs MM/DD ambiguity.
- **Piece-type-aware date extraction** — SENTENÇA uses "Publique-se" date, ACÓRDÃO uses session date, PETIÇÃO uses protocol date.
- **OCR confidence per chunk** — heuristic based on vowel ratios, legal term density, encoding quality.
- **Recesso forense Dec 20–Jan 20** — all prazo calculations suspend during this period (CPC Art. 220).
- **Fact divergence detection defers to Claude** — script flags structural contradictions, semantic comparison via prompt template.

## Domain Context

- All legal terminology and user-facing text in **Brazilian Portuguese**.
- Process numbers follow **CNJ format**: `NNNNNNN-DD.YYYY.J.TT.OOOO` (Res. 65/2008).
- Judicial instances: 1ª Instância (Varas) → TJ/TRF (Câmaras) → STJ (Turmas) → STF (Plenário/Turmas).
- Binding precedents: Súmula Vinculante, IRDR, IAC, Repercussão Geral, Recurso Repetitivo.

## Dependencies

- Python 3.10+ (uses `X | Y` union syntax)
- System: `poppler-utils` (pdftotext, pdfinfo, pdftoppm), `tesseract-ocr` + `tesseract-ocr-por`
- Python: `pip install -r requirements.txt` (pypdf, pytesseract, Pillow, jsonschema, pytest)
