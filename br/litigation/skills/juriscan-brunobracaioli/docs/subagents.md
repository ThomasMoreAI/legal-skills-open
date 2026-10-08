# Juriscan — Subagents

All seven juriscan subagents live in `.claude/agents/juriscan-*.md` and are
symlinked into `~/.claude/agents/` by `install.sh`. Each has a strict
JSON Schema in `references/agent_schemas/<role>_output.json` and is
validated post-hoc by `scripts/agent_io.py validate --agent <role>`.

| Role | Model | Tools | Phase | Critical? |
|---|---|---|---|---|
| [`juriscan-echo`](#echo) | haiku | Read | 0 | Selftest only |
| [`juriscan-segmenter`](#segmenter) | haiku | Read, Bash | 2 | Yes — all downstream depends on coverage |
| [`juriscan-parser`](#parser) | haiku | Read, Bash | 2 | Load-bearing for `votos_divergentes` |
| [`juriscan-advogado-autor`](#advogado-autor) | sonnet | Read, Bash | 3 | Dialectic half #1 |
| [`juriscan-advogado-reu`](#advogado-reu) | sonnet | Read, Bash | 3 | Dialectic half #2 |
| [`juriscan-auditor-processual`](#auditor) | sonnet | Read, Bash | 3 | **MOST CRITICAL** — art. 942 gate |
| [`juriscan-verificador`](#verificador) | haiku | Read, WebFetch, Bash | 4 | Whitelist-restricted |
| [`juriscan-sintetizador`](#sintetizador) | sonnet | Read, Bash | 3 | Cannot drop findings |

## Contract (common to all)

1. SKILL.md invokes via `Task(subagent_type="juriscan-<role>", prompt=...)`.
2. The subagent writes its output JSON to the path passed in the prompt
   (never returns it as text).
3. SKILL.md runs `agent_io.py validate --agent <role> --input <path>`.
4. If exit 0 → log + consume. If exit ≠ 0 → retry once with the error
   message as feedback. Second failure → abort pipeline.
5. Every successful or failed invocation is logged to
   `.juriscan/audit/<run_id>.jsonl`.

## juriscan-echo

Trivial selftest agent. Writes `{"ok": true, "agent": "juriscan-echo", "input_echo": ...}`.
Used by `/juriscan --selftest` to verify the plumbing before any real
analysis runs.

## juriscan-segmenter

Identifies boundaries between legal pieces in the raw extracted text.
Output: `chunks[] = {id, start_char, end_char, tipo_provavel, confianca, evidencia?}`.
Must cover the entire raw text without gaps or overlap —
`scripts/persist_chunks.py` verifies and will re-invoke with feedback if
coverage is violated.

**Confidence calibration:** `0.90+` for explicit headers, `0.70-0.89`
for inferred, `<0.50` only with `tipo_provavel="DESCONHECIDO"`.

## juriscan-parser

Analyzes one chunk per invocation. SKILL.md fires N `Task` calls in a
single assistant message to parallelize across chunks. Output shape is
compatible with legacy v2 chunk objects for backwards compat during the
transition.

**Load-bearing:** when `tipo_peca == "ACÓRDÃO"`, must fill
`acordao_detail.votos_divergentes[]` completely. The auditor uses this
to detect art. 942 CPC triggers; missing it breaks the Phase 3 gate.

## juriscan-advogado-autor

Represents the pole ativo. Produces `forcas`, `fraquezas`,
`recursos_cabiveis`, and a `risk_score` from the perspective of the
author only. Every item must cite `peca_refs` — the schema rejects
arguments without sources. Must never downplay weaknesses when the
autor has lost at first instance.

## juriscan-advogado-reu

Symmetric to advogado-autor for the polo passivo. Shares the same JSON
schema (`advogado_output.json`). Must handle the case where the réu has
already been condemned: reform base attackable? quantum excessive?
nullity arguable?

## juriscan-auditor-processual

**The critical subagent.** Impartial — not advocating for either side.
Produces `auditor_findings[]` and a mandatory 6-item checklist
(`checklist_resultado`). Each checklist entry is `{value, justificativa}`
and cannot be null.

The six items:
1. `art_942_cpc_triggered` — 5 objective conditions for the mandatory
   panel-expansion technique. The golden fixture
   `tests/golden/processo_02_sintetico_art942/` blocks CI on this.
2. `lei_14905_2024_applicable` — straddling 2024-08-30 cutover?
3. `honorarios_post_reform_omission` — embargos de declaração cabíveis?
4. `tempestividade_all_pieces_ok` — any piece out of deadline?
5. `citacao_ok` — art. 246 CPC compliant?
6. `preclusao_detected` — any central argument precluded?

For art. 942 detections, the finding description **must** contain the
literal words `ampliação`, `colegiado`, `maioria`. The golden gate checks
for these tokens.

## juriscan-verificador

Verifies jurisprudence citations against authoritative sources via
`WebFetch`. Restricted to `references/whitelist_fontes.json` — any
`source_url` host outside the whitelist fails
`agent_io.py validate --agent verificador` (post-hoc hard gate in
`scripts/agent_io.py _check_verificador_whitelist`).

**Never** produces `CONFIRMADO` without an in-session `WebFetch`. When
CONFIRMADO or DIVERGENTE, must include a literal `trecho_oficial` from
the fetched page.

## juriscan-sintetizador

Consolidates autor + reu + auditor outputs into a final report.
**Cannot** drop `auditor_findings` — `scripts/confidence_rules.py`
enforces `len(output) >= len(input)` and raises
`ConfidenceRuleError` if violated. Produces `dissensos[]` (original
contribution) by comparing the two advocate outputs.

## Adding a new subagent

1. Write `.claude/agents/juriscan-<role>.md` with frontmatter
   (`name`, `description`, `tools`, `model`) and a prompt body.
2. Add `references/agent_schemas/<role>_output.json` with required fields.
3. Register the role in `KNOWN_AGENTS` and `_SCHEMA_FILE_OVERRIDES` in
   `scripts/agent_io.py`.
4. Add fixtures under `tests/fixtures/agent_io/` and tests in
   `tests/test_agent_io.py`.
5. Wire the new role into `SKILL.md`'s `## Agents Pipeline` section,
   initially marked `[PENDING]` until the acceptance criteria of its
   phase are met.
