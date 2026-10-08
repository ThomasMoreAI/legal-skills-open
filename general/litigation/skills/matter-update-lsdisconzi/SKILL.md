---
name: matter-update-lsdisconzi
title: Matter Update
description: Append a dated event to the matter's history and refresh its row in matters/_log.yaml — captures new developments, status and stage changes, risk re-assessments, deadline shifts, evidence developments, and co-counsel changes. Use when the user wants to log an update, note a development, or record a status change on the matter.
author: lsdisconzi
author_url: https://github.com/lsdisconzi/craudio-para-adevogados/tree/main/skills/matter-update
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Matter Update

The matter ledger is only useful if it stays current. This skill makes logging an update cheap — a few minutes of structured capture, no freeform drift — and keeps `_log.yaml` and `history.md` in sync. This plugin tracks one matter; there is no slug to disambiguate.

## Running this skill

1. **Load configuration.** Read the configured practice profile at `~/.claude/plugins/config/craudio-p-advogados/<plugin>/CLAUDE.md` and the firm profile at `~/.claude/plugins/config/craudio-p-advogados/company-profile.md`. If either file is missing, or a critical field still shows `[PLACEHOLDER]`, STOP — tell the attorney: "This plugin needs setup. Run the `cold-start-interview` skill."
2. **Apply the frame.** The Plugin Operating Rules, Shared Guardrails, Decision posture, Jurisdiction recognition, and Ontology Governance sections of CLAUDE.md govern this skill. The skill workflow below is a FLOOR, not a ceiling (see "Scaffolding, not blinders").
3. **Resolve vault paths.** Every `{vault root}` reference below resolves against `## Vault location` in CLAUDE.md. Never hard-code an absolute path.
4. **Apply the work-product header** from CLAUDE.md `## Outputs` to every internal deliverable; suppress it on externally-facing output per Quiet mode.
5. **Run the workflow below.**
6. **Close** with the `⚠️ Reviewer note` block and the next-steps decision tree from CLAUDE.md `## Outputs`.

---

## Load context

> **Matter paths.** Every `matters/…` path below resolves under the config matters directory — `~/.claude/plugins/config/craudio-p-advogados/<plugin>/matters/` — never the plugin repo. Matter slug: `<matter-slug>`. See CLAUDE.md `## Matter workspaces`.

- `matters/_log.yaml` — the single matter row; find `id: <matter-slug>`
- `matters/<matter-slug>/history.md` — the append target
- `matters/<matter-slug>/matter.md` — reference for current posture; do not rewrite it here

**Matter gate.** If `matters/_log.yaml` has no matter row, or `matters/<matter-slug>/` does not exist, refuse and route:

> "The matter hasn't been set up yet — there's no `_log.yaml` row or `history.md` to append to. Run `/craudio:matter-intake` first."

## Workflow

### 1. Event type

Offer categories — pick the closest, or freeform:

- **Procedural** — petition filed, decision issued, hearing held, deadline set, service effected
- **Evidence** — new evidence surfaced, hash completed, preservation confirmed, chain-of-custody gap, CCTV development
- **Substantive** — new facts, key transcript segment identified, violation analysis completed
- **Strategy** — forum decision, demand letter sent, settlement offer made or received, posture shift
- **Cross-jurisdiction** — service of process across BR/CL, carta rogatória progress, treaty-channel development
- **Co-counsel** — Chilean co-counsel engaged or changed, international specialist retained
- **Regulatory** — ANAC / DGAC development, transparency-law response
- **Administrative** — evidence indexed, translation completed, legal hold issued or refreshed

### 2. Date

Default today (2026-05-16 unless otherwise current). Accept an override for an event being captured after the fact.

### 3. Summary

One-paragraph narrative: what happened, what it means, the immediate implication for the case.

### 4. Log field changes

Walk only the fields plausibly affected by the event type:

- `status:` — has the stage shifted (e.g., `active` → `filed`)?
- `stage:` — free-text substage update
- `risk:` — does the development move the risk rating? (per CLAUDE.md risk calibration)
- `exposure_range:` — revise if new damages information
- `next_deadline:` — a new or shifted date
- `chilean_counsel:` — firm / lead / email / engagement status change
- `prescription:` — only if an interruption event resets a clock (see 4a)
- `violations_count` / `evidence_count` / `transcripts_count` — if the record grew

Only prompt for fields the event could touch. A procedural filing usually moves `stage` and `next_deadline`; a co-counsel engagement moves `chilean_counsel`.

### 4a. Prescription-interruption gate — explicit prompt

The matter carries hard prescription clocks (CACH/MC99 → 2026-07-05; LPDC → likely expired). Certain events interrupt or reset a clock. When the event is one of these, **always prompt — do not let the user move past it silently**:

| Event | Prompt |
|---|---|
| Demand letter sent / received | "A demand letter can interrupt prescription (BR: CC Art. 202). Which clock(s) does this touch? Should `prescription:` be updated? `[review]` — confirm the interruption rule for the forum." |
| Suit filed | "Filing interrupts prescription. Confirm which clock(s) stop and note the filing date." |
| Settlement negotiation opened | "Negotiation may or may not interrupt prescription depending on forum. Flag `[review]` — do not assume." |

Any change to a `prescription:` date is tagged `[review]` and `[direito estrangeiro — verificar com co-counsel]` if it concerns a Chilean or treaty clock — prescription interruption is jurisdiction-specific and the matter must not silently rely on it.

### 4b. Settlement-offer gate

If the Strategy update is a **settlement acceptance** (the client is accepting an offer or authorizing acceptance — not merely logging that an offer was made or received): do not log the acceptance or move `exposure_range` on that basis without confirming the settlement authority ladder (CLAUDE.md → Settlement Authority). An offer at or above R$100,000 / CLP $10,000,000 requires managing partner + client. State the ladder and confirm the right approver signed off before logging.

### 5. Seed doc prompt (optional)

If the update references a document — a filed petition, a decision, correspondence, a new evidence item — ask for a path to link. Not pushy.

## Writing

### Append to `matters/<matter-slug>/history.md`

Most recent at top, directly under the header:

```markdown
## [YYYY-MM-DD] — [Event type]: [short title]

[Paragraph summary.]

**Campos alterados / Fields changed:**
- [field]: [old → new]

**Verificação de prescrição / Prescription check:** [no change / clock X interrupted — [review]]
**Doc relacionado / Related doc:** [path, if provided]
```

Omit the "Fields changed" and "Prescription check" lines when not applicable.

### Update `matters/_log.yaml`

- Apply the confirmed field changes to the matter row.
- Set `last_updated:` to today (or the event date if the user overrode — the log records when the record was last touched).

## Confirm

Show the user the history entry and the `_log.yaml` diff before writing:

> Aqui está o que vou anexar e atualizar. Posso gravar? / Here's the entry and the log diff. Good to commit?

## What this skill does not do

- **Edit past history entries.** Corrections are new entries that reference and correct the prior one. `history.md` is append-only.
- **Silently change the log.** Every field change is shown before write.
- **Rewrite `matter.md`.** Evolving theory and posture notes go in `matter.md` directly; this skill reads it for reference only.
- **Decide a prescription clock was interrupted.** It surfaces the question and flags `[review]`; the attorney (and co-counsel for CL/INT clocks) decides.
