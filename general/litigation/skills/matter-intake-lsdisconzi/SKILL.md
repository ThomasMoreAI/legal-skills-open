---
name: matter-intake-lsdisconzi
title: Matter Intake
description: Create the formal matter file. Writes matter.md with case identification, parties, jurisdiction, and initial strategy. Appends to the firm's matter log.
author: lsdisconzi
author_url: https://github.com/lsdisconzi/craudio-para-adevogados/tree/main/skills/matter-intake
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Matter Intake

Creates and maintains the formal matter file for the case. This is the canonical case record that all other skills reference.

## Running this skill

1. **Load configuration.** Read the configured practice profile at `~/.claude/plugins/config/craudio-p-advogados/<plugin>/CLAUDE.md` and the firm profile at `~/.claude/plugins/config/craudio-p-advogados/company-profile.md`. If either file is missing, or a critical field still shows `[PLACEHOLDER]`, STOP — tell the attorney: "This plugin needs setup. Run the `cold-start-interview` skill."
2. **Apply the frame.** The Plugin Operating Rules, Shared Guardrails, Decision posture, Jurisdiction recognition, Retrieved-content trust, and Ontology Governance sections of CLAUDE.md govern this skill. The skill workflow below is a FLOOR, not a ceiling (see "Scaffolding, not blinders").
3. **Resolve vault paths.** Every `{vault root}` reference below resolves against `## Vault location` in CLAUDE.md. Never hard-code an absolute path.
4. **Apply the work-product header** from CLAUDE.md `## Outputs` to every internal deliverable; suppress it on externally-facing output per Quiet mode.
5. **Run the workflow below.**
6. **Close** with the `⚠️ Reviewer note` block and the next-steps decision tree from CLAUDE.md `## Outputs`.

---

## Workflow

> **Matter paths.** The matter slug is determined at intake — derived from the client and opponent names (e.g., `client-vs-opponent-YYYY`). The matter folder and ledger live under the config directory — `~/.claude/plugins/config/craudio-p-advogados/<plugin>/matters/` — never the plugin repo, which ships only an empty template ledger. See CLAUDE.md `## Matter workspaces`.

### 1. Create Matter File
Write the matter file to `~/.claude/plugins/config/craudio-p-advogados/<plugin>/matters/<matter-slug>/matter.md`:

```markdown
# Matter: [CLIENT] vs [OPPONENT(S)]

## Matter Identification
- **Matter ID:** [MATTER-ID — e.g., CLIENT-YYYY-001]
- **Matter slug:** [client-vs-opponent-YYYY]
- **Date opened:** [TODAY]
- **Status:** ACTIVE — PRE-LITIGATION
- **Practice area:** [FILL — from CLAUDE.md case type]
- **Lead counsel:** [NAME], [FIRM]
- **Co-counsel:** [FILL — from CLAUDE.md]
- **Client:** [CLIENT NAME]

## Case Summary
[One-paragraph case summary from CLAUDE.md]

## Parties
[Table of all parties and roles from CLAUDE.md Parties & Defendants section]

## Jurisdiction
- **Lead forum:** [FILL — from CLAUDE.md]
- **Parallel forum(s):** [FILL — from CLAUDE.md]
- **Reserve forum(s):** [FILL — from CLAUDE.md]

## Incidents
[For each incident from CLAUDE.md: ID, date, location, brief summary]

## Claims Summary
[Table of all causes of action x jurisdiction x estimated damages]

## Critical Deadlines
[Prescription table from CLAUDE.md]

## Evidence Registry
- **Violations:** [count] at {vault root}/01-violations/
- **Evidence items:** [count] at {vault root}/03-evidence/
- **Transcripts:** [count] at {vault root}/02-transcripts/
- **Audio:** {vault root}/awareness/shared/audio_segmented/

## Current Status
- **Phase:** Pre-litigation — evidence analysis and demand drafting
- **Next action:** [CURRENT NEXT STEP]
- **Last updated:** [TODAY]
```

### 2. Create the history log
Create `~/.claude/plugins/config/craudio-p-advogados/<plugin>/matters/<matter-slug>/history.md` — the append-only event log every other matter skill (`matter-update`, `matter-close`, `legal-hold`, `oc-status`) appends to:
```
# Matter History — [CLIENT] vs [OPPONENT(S)]

[DATE] Matter opened — [CLIENT] vs [OPPONENT(S)].
[DATE] Initial evidence inventory complete — [N] items indexed.
[DATE] Violation sweep complete — [N] violations across [jurisdictions].
```

### 3. Write the ledger row
Write or update the matter's entry in `~/.claude/plugins/config/craudio-p-advogados/<plugin>/matters/_log.yaml`, following the schema documented at the top of that file. The row `id` is the matter slug and `path` is `matters/<matter-slug>/`. If a row already exists (matter previously created), `--update` refreshes it in place — never create a second row; this plugin tracks one matter.

### 4. Set Active Matter
This plugin tracks one matter; once intake completes, every subsequent skill run uses it as context.

### 5. Initial Status Assessment
Generate:
- **Risk matrix:** Severity × Likelihood for each claim category
- **Timeline to file:** Days remaining on each prescription clock
- **Resource estimate:** Anticipated legal work breakdown
- **Dashboard:** Matter status dashboard with deadlines, claims, and actions

## Guardrails
- `matter.md` is the canonical record — update it after every material action
- `history.md` is append-only — never delete or rewrite entries; the `_log.yaml` row is updated in place
- Cross-matter context off by default (single-client case)
- Privilege markings on matter file per practice profile
- **Ontology compliance:** outputs must satisfy the litigation-relevant error codes in `core/ontology/error-catalog.md`. If an invariant violation is detected, flag with `[ONT-ERROR: <code>]` and do not produce confident output. I-1 is absolute: no conclusory language.
