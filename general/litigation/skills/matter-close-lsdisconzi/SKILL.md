---
name: matter-close-lsdisconzi
title: Matter Close
description: Close the matter — capture the outcome across all jurisdictions, record final damages recovered vs. estimated, lessons, and write the final state to matters/_log.yaml without deleting the record. Use when the user wants to close the matter, says "the case is done", or needs to record a settlement, judgment, dismissal, or withdrawal outcome.
author: lsdisconzi
author_url: https://github.com/lsdisconzi/craudio-para-adevogados/tree/main/skills/matter-close
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Matter Close

Matters end. The outcome is the most valuable record the matter produces — it is what a future cross-jurisdictional case is calibrated against. Closing captures the outcome structurally so the record is useful, not just archived. The matter is **not deleted**: it stays in `_log.yaml` and on disk as the closed record.

## Running this skill

1. **Load configuration.** Read the configured practice profile at `~/.claude/plugins/config/craudio-p-advogados/<plugin>/CLAUDE.md` and the firm profile at `~/.claude/plugins/config/craudio-p-advogados/company-profile.md`. If either file is missing, or a critical field still shows `[PLACEHOLDER]`, STOP — tell the attorney: "This plugin needs setup. Run the `cold-start-interview` skill."
2. **Apply the frame.** The Plugin Operating Rules, Shared Guardrails, Decision posture, Jurisdiction recognition, and Ontology Governance sections of CLAUDE.md govern this skill. The skill workflow below is a FLOOR, not a ceiling (see "Scaffolding, not blinders").
3. **Resolve vault paths.** Every `{vault root}` reference below resolves against `## Vault location` in CLAUDE.md. Never hard-code an absolute path.
4. **Apply the work-product header** from CLAUDE.md `## Outputs` to every internal deliverable; suppress it on externally-facing output per Quiet mode.
5. **Run the workflow below.**
6. **Close** with the `⚠️ Reviewer note` block and the next-steps decision tree from CLAUDE.md `## Outputs`.

---

## Load context

> **Matter paths.** Every `matters/…` path below resolves under the config matters directory — `~/.claude/plugins/config/craudio-p-advogados/<plugin>/matters/` — never the plugin repo. The matter slug is determined at intake. See CLAUDE.md `## Matter workspaces`.

- `matters/_log.yaml` — the matter row
- `matters/<matter-slug>/matter.md` — reference for the intake theory and estimated exposure
- `matters/<matter-slug>/history.md` — the append target

**Matter gate.** If `matters/_log.yaml` has no matter row, refuse: "There's no matter to close — `_log.yaml` has no row. Either the matter was never set up, or it's already been removed. Run `/craudio:matter-intake` if it genuinely needs creating."

## Cross-jurisdiction note — one matter, multiple resolutions

A multi-jurisdictional matter can resolve in one forum while another remains live. **Do not record the matter as closed while any forum remains active.** Capture the resolution per forum; close only when all live tracks are resolved or formally abandoned.

## Workflow

### 1. Per-forum resolution

For each forum that was active, capture the resolution type:

- `settled` — counterparty, amount, structural terms (e.g., ban lifted, record corrected), confidentiality
- `judgment-for-client` — forum, stage, amount awarded, appeal exposure
- `judgment-against-client` — forum, stage, appeal status
- `dismissed` — with or without prejudice, mechanism
- `withdrawn` — by which party, circumstances
- `abandoned` — a track formally not pursued (e.g., IACHR petition window allowed to lapse)
- `other` — with explanation

If a forum is still live, the matter is not closeable — record the per-forum status and stop.

### 2. Resolution date

The date the last live track actually ended.

### 3. Final damages — recovered vs. estimated

- Actual recovery (total across fora: moral + material + costs)
- vs. the intake estimate in `matter.md` / `_log.yaml` `exposure_range` — did the estimate hold?
- Per jurisdiction: BR recovery (R$), CL recovery (CLP), INT outcome

### 4. Lessons

Two or three honest sentences. What did the case theory get right — the three-layer theory, the CCTV centrality, the cross-jurisdictional nexus? What was misjudged — a forum that underperformed, a prescription clock that nearly lapsed (LPDC), an evidence gap that was not closed in time? This is what a future cross-jurisdictional matter will reread.

### 5. Seed doc prompt

Settlement agreement, final judgment, dismissal order — path if available. Not required.

## Writing

**Before closing the matter (the consequential act — active tracking ends and any legal hold should be reviewed for release):** confirm with the attorney:

> Fechar a matéria encerra o acompanhamento ativo. Antes de gravar: (a) todas as instâncias (BR / CL / INT) estão resolvidas ou formalmente abandonadas? (b) há um *legal hold* ativo que deva ser liberado — rodar `/craudio:legal-hold --release` separadamente? (c) o prazo de petição à CIDH foi resolvido ou deixado expirar conscientemente? Confirmado?

Do not write the close fields or append the close entry without an explicit yes.

### Update `matters/_log.yaml`

```yaml
status: closed
closed: [YYYY-MM-DD]
outcome: [settled | dismissed | judgment-for-us | judgment-against-us | withdrawn | other]
outcome_by_forum:
  br: [resolution]
  cl: [resolution]
  int: [resolution]
final_recovery: "[total — e.g., R$XX.XXX + CLP $X.XXX.XXX]"
last_updated: [today]
```

Retain every existing field. Do not delete the row — a closed matter is the calibration record.

### Append the final entry to `matters/<matter-slug>/history.md`

```markdown
## [YYYY-MM-DD] — Matéria encerrada / Matter closed: [outcome]

**Resolução por foro / Resolution by forum:**
- BR (TJSP): [narrative]
- CL (Santiago): [narrative]
- INT (IACHR): [narrative or "não acionado"]

**Recuperação final / Final recovery:** [amount + structural terms]
**vs. estimativa de intake / vs. intake estimate:** [compare to matter.md range]

**Lições / Lessons:**
[2-3 honest sentences]

**Doc relacionado / Related doc:** [path, if provided]
```

### Touch `matters/<matter-slug>/matter.md`

Add a closing block at the end — do not modify the earlier sections, they are the historical intake:

```markdown
---

## Encerrada / Closed [YYYY-MM-DD]

[One-paragraph resolution summary. Pointer to the final history entry for detail.]
```

## Confirm

Show the user the full close entry, the `_log.yaml` changes, and the `matter.md` closing block before writing.

## What this skill does not do

- **Delete the matter.** The closed matter stays in `_log.yaml` and on disk.
- **Close a matter with a live forum.** If BR, CL, or INT remains active, the skill records per-forum status and stops.
- **Release the legal hold.** Closing flags the question; `/craudio:legal-hold --release` is a separate, deliberate step — premature release is a spoliation exposure.
- **Re-open.** If the case returns (appeal, related litigation, an IACHR petition after exhaustion), open a new matter row that references this closed one — do not reanimate the closed record.
- **Invent lessons.** If the user skips the lessons section, leave it empty rather than manufacture a retrospective.
- **Conclude on the merits.** Per Invariant I-1, the outcome is recorded as what the forum did (settled, dismissed, judgment) — not as a finding that the defendants were "liable" or the claims "proven".
