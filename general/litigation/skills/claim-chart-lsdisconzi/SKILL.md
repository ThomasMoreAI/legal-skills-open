---
name: claim-chart-lsdisconzi
title: Claim Chart Builder
description: Construct element-by-element claim charts for each cause of action across all jurisdictions. Maps statutory elements to specific facts with evidence anchors. Patent-style element chart for civil causes of action.
author: lsdisconzi
author_url: https://github.com/lsdisconzi/craudio-para-adevogados/tree/main/skills/claim-chart
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
sources:
- title: Element Templates
  path: references/element-templates.md
---

# Claim Chart Builder

Builds element-by-element claim charts in the style of patent claim charts — each legal element of each cause of action mapped to specific facts with evidence citations. This engine names no statute or party: the cause-of-action library and its elements come from packs.

## Inputs

- **Matter facts** — violation records, actions, evidence from `{vault root}`.
- **Domain pack(s)** — `packs/domain/<id>/norm-templates.yaml` supplies each cause of action as a norm template with its `required_elements`.
- **Jurisdiction pack(s)** — `packs/jurisdiction/<id>/framework-index.yaml` resolves each norm template to concrete statutory articles; `citation-format.yaml` governs citation form.

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

### 1. Select cause of action
Build the claim-chart library from the active packs: each entry in a domain pack's `norm-templates.yaml` is a cause of action; its `required_elements` are the chart rows; the jurisdiction pack's `framework-index.yaml` resolves it to the governing statutory article. Choose the cause(s) of action relevant to the violation(s) under analysis.

### 2. Element mapping
For each element, identify:
- **Factual anchor:** specific event with date, time, location, actor
- **Evidence citation:** transcript segment, document, or testimony
- **Legal reasoning:** why this fact satisfies this element
- **Counter-arguments:** anticipated defenses and responses

### 3. Chart format

```
CLAIM: <cause of action> — <statutory article from jurisdiction pack> (<jurisdiction>)

Element 1: <element name from norm-template required_elements>
├── Fact: <specific event from the matter>
├── Evidence: <evidence-id / transcript-key seg-N>
├── Key Quote: "<verbatim text>" (<evidence anchor>)
└── Law: <statutory article and why it is satisfied>

Element 2: ...
```

### 4. Cross-jurisdictional charts
When the same facts ground claims in multiple jurisdictions, chart the fact once and list each jurisdiction's matching norm template + article beneath it:

```
FACT: <fact statement> (<incident, date>)
├── <jurisdiction A>: <norm template> — <article>
├── <jurisdiction B>: <norm template> — <article>
└── <international>: <norm template> — <article>
```

### 5. Output
- **Per-claim chart** — element-by-element with evidence
- **Master claim matrix** — all claims × elements × evidence grid
- **Evidence sufficiency assessment** — which elements are fully proven vs. need discovery
- **Dashboard** — color-coded claim chart with evidence links

## Integration
- Run after `violation-analysis` for the facts-and-norms foundation.
- Run after `chronology` for temporal alignment.
- Feed into `demand-draft` and `brief-section-drafter`.

## Guardrails
- Claim charts are analytical tools — not filed pleadings.
- Every element must cite evidence — no unsupported claims.
- The counter-arguments column is mandatory — it demonstrates good faith.
- Per Ontology Invariant I-1: all allegations, not adjudicated facts.
- **Ontology compliance:** outputs must satisfy the litigation-relevant error codes in `core/ontology/error-catalog.md`. If an invariant violation is detected, flag with `[ONT-ERROR: <code>]` and do not produce confident output. I-1 is absolute: no conclusory language.
