---
name: cross-jurisdiction-nexus-lsdisconzi
title: Cross-Jurisdiction Nexus Analysis
description: Analyze cross-jurisdictional connections between violations — how conduct in one jurisdiction causes consequences in another, and how state-actor conduct engages international treaty obligations.
author: lsdisconzi
author_url: https://github.com/lsdisconzi/craudio-para-adevogados/tree/main/skills/cross-jurisdiction-nexus
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: litigation
language: en
---

# Cross-Jurisdiction Nexus Analysis

Maps the connections that bind a multi-jurisdiction matter into one case theory: how conduct in one jurisdiction causes consequences in another, and how state-actor conduct engages international treaty obligations. This engine names no statute or party — jurisdictions, treaties, and forums come from the active packs.

## Inputs

- **Matter facts** — violation records and incident chronology from `{vault root}`.
- **Jurisdiction pack(s)** — `framework-index.yaml`, `courts.yaml`, `limitation-periods.yaml` for each jurisdiction the matter declares.
- **International pack** — treaty index and state-responsibility norms.

## Running this skill

1. **Load configuration.** Read the configured matter profile and firm profile from the plugin config directory (see CLAUDE.md `## Configuration Location`). If a file is missing, or a critical field still shows `[PLACEHOLDER]`, STOP — tell the attorney: "This plugin needs setup. Run the `cold-start-interview` skill."
2. **Apply the frame.** The Plugin Operating Rules, Shared Guardrails, Decision posture, Jurisdiction recognition, Retrieved-content trust, and Ontology Governance sections of CLAUDE.md govern this skill. The workflow below is a FLOOR, not a ceiling.
3. **Resolve vault paths.** Every `{vault root}` reference resolves against `## Vault location` in CLAUDE.md. Never hard-code an absolute path.
4. **Determine active packs.** Read which jurisdiction packs and international pack the matter declares (matter profile `## Packs`).
5. **Apply the work-product header** from CLAUDE.md `## Outputs` to every internal deliverable; suppress it on externally-facing output per Quiet mode.
6. **Run the workflow below.**
7. **Close** with the `⚠️ Reviewer note` block and the next-steps decision tree from CLAUDE.md `## Outputs`. Run the `ontology-validate` skill on the output before it reaches a court or counterparty.

---

## Workflow

### 1. Inter-jurisdiction causation chain
Trace how an action in one jurisdiction propagates to a violation in another. For each link, state the action, the propagation mechanism, and the resulting consequence. The key question: did actors in the downstream jurisdiction rely on the upstream conduct? If so, the upstream violations have direct causal effect downstream — record this as a `GROUNDED_IN_ACTION` edge across the jurisdiction boundary.

### 2. State-responsibility chain
Where state agents are involved, trace how their conduct engages the state's international obligations. List each state-agent action and the treaty obligations it engages (from the international pack), then state the `HAS_APPLICABILITY_BASIS` for each (VIII-3).

### 3. Forum strategy analysis
For each category of claim, evaluate the candidate forums (from each jurisdiction pack's `courts.yaml`): which forum, and why — strongest substantive law, locus delicti, client domicile, language, prescription posture.

### 4. Treaty interaction analysis
Map how the treaties in the international pack interact with each other and with each jurisdiction's domestic law: which treaty sets the standard, how it is incorporated domestically, and whether a state may invoke domestic law to escape a treaty obligation.

### 5. Conflict-of-laws analysis
Identify divergences across the jurisdiction packs: prescription periods (`limitation-periods.yaml`), damage caps, burden of proof, and cross-border judgment enforcement. State how each divergence should be handled.

### 6. Output
- **Nexus map** — visual causation diagram across jurisdictions
- **Forum strategy matrix** — claim × forum × risk assessment
- **Treaty compliance analysis** — state breaches of international obligations
- **Conflict-resolution strategy** — how to handle diverging legal standards

## Ontology graph vocabulary

This skill operates across jurisdictions, producing edges per `core/ontology/graph-model.yaml` — chiefly `GROUNDED_IN_ACTION` (across a jurisdiction boundary), `HAS_APPLICABILITY_BASIS`, `VIOLATES_ARTICLE`, and `PERFORMED_BY`. Every cross-jurisdiction claim must carry a `HAS_APPLICABILITY_BASIS` (invariant VIII-3).

## Guardrails

- This skill analyzes legal connections — it does NOT determine liability.
- Forum recommendations are strategic, not jurisdictional determinations.
- Treaty interpretations are analytical — verify against primary treaty text and the relevant treaty body's jurisprudence.
- Cross-border enforcement requires local counsel in each jurisdiction.
- **Ontology compliance:** outputs must satisfy the litigation-relevant error codes in `core/ontology/error-catalog.md`. If an invariant violation is detected, flag with `[ONT-ERROR: <code>]` and do not produce confident output. I-1 is absolute: no conclusory language.
