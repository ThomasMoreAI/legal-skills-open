---
name: prejudice-quantification-lsdisconzi
title: Prejudice Quantification
description: Calculate moral damages and material damages across all jurisdictions in the matter. Damage heads, reference awards, and liability limits are loaded from packs.
author: lsdisconzi
author_url: https://github.com/lsdisconzi/craudio-para-adevogados/tree/main/skills/prejudice-quantification
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Prejudice Quantification

Calculates compensable damages under the law of each jurisdiction in the matter. Distinguishes moral damages, material damages, and punitive/social damages. This engine names no statute or currency: damage heads come from domain packs (`remedies.yaml`), reference awards and liability limits come from jurisdiction packs.

## Inputs

- **Matter facts** — violations, documented expenses, and incident records from `{vault root}`.
- **Domain pack(s)** — `packs/domain/<id>/remedies.yaml` supplies the compensable damage heads for the domain.
- **Jurisdiction pack(s)** — reference award ranges, currency, statutory damage bases (`framework-index.yaml`), and any treaty liability limits.

## Running this skill

1. **Load configuration.** Read the configured matter profile and firm profile from the plugin config directory (see CLAUDE.md `## Configuration Location`). If a file is missing, or a critical field still shows `[PLACEHOLDER]`, STOP — tell the attorney: "This plugin needs setup. Run the `cold-start-interview` skill."
2. **Apply the frame.** The Plugin Operating Rules, Shared Guardrails, Decision posture, Jurisdiction recognition, Retrieved-content trust, and Ontology Governance sections of CLAUDE.md govern this skill. The workflow below is a FLOOR, not a ceiling.
3. **Resolve vault paths.** Every `{vault root}` reference resolves against `## Vault location` in CLAUDE.md. Never hard-code an absolute path.
4. **Determine active packs.** Read which domain and jurisdiction packs the matter declares (matter profile `## Packs`).
5. **Apply the work-product header** from CLAUDE.md `## Outputs` to every internal deliverable; suppress it on externally-facing output per Quiet mode.
6. **Run the workflow below.**
7. **Close** with the `⚠️ Reviewer note` block and the next-steps decision tree from CLAUDE.md `## Outputs`. Run the `ontology-validate` skill on the output before it reaches a court or counterparty.

---

## Workflow

### 1. Moral damages — per jurisdiction
For each jurisdiction in the matter:
- Load the compensable damage heads from the domain pack `remedies.yaml`.
- For each head, identify the grounding violation(s) and supporting evidence.
- Estimate a range using the reference awards in the jurisdiction pack — cite each comparable award with its court, facts, and amount.
- State the statutory basis from the jurisdiction pack `framework-index.yaml`.

### 2. Material damages
Build a liquidation table of documented out-of-pocket losses from the matter: each item with amount, jurisdiction, and documentation reference. Flag any item lacking a receipt or booking record as `[undocumented — verify]`.

### 3. Punitive / social damages
Where the jurisdiction's law recognizes an enhancement (e.g. for intentional or knowing conduct, or institutional pattern), state the basis from the jurisdiction pack and the matter facts that support it.

### 4. Treaty liability limits
If the matter declares an international jurisdiction pack, apply any treaty liability limit it defines: state the limit, whether it applies to the damage type, and any exclusion (e.g. intentional misconduct) the matter facts support.

### 5. Output
- **Damages schedule** — per-head calculation with legal basis and supporting precedent
- **Liquidation table** — documented material damages with references
- **Treaty-limit analysis** — applicability and any exclusion argument
- **Total estimate** — combined damages range across all jurisdictions

## Guardrails

- All amounts are estimates for demand/discussion — not liquidated values.
- Reference awards are for guidance — each case is individual.
- Damages estimates for any jurisdiction require local-counsel confirmation.
- Treaty-limit analysis must be verified against the current limit value.
- Material damages require documented receipts — flag undocumented items.
- **Ontology compliance:** outputs must satisfy the litigation-relevant error codes in `core/ontology/error-catalog.md`. If an invariant violation is detected, flag with `[ONT-ERROR: <code>]` and do not produce confident output. I-1 is absolute: no conclusory language.
