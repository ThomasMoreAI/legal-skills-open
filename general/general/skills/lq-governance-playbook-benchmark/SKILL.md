---
name: lq-governance-playbook-benchmark
title: LQ Governance Playbook Benchmark Protocol
description: Use when benchmarking a board-level governance document against the LQ Governance Playbook — a Delegation of Authority policy, committee charter, related party transaction framework, or board terms of reference. Produces a classification table (Match / Partial Match / Below Fallback / Red Flag / Omitted) with specific gaps and tracked changes.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/lq-governance-playbook-benchmark
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
tags: [governance, board-documents, delegation-of-authority, benchmark, playbook, compliance, redlines]
---

# LQ Governance Playbook Benchmark Protocol

You are benchmarking a target governance document against the LQ Governance Playbook. The Playbook is a reference document produced by LegalQuants encoding their preferred positions on recurring board-level clauses.

## Inputs Required

1. **Target document** — the currently open Word document under review
2. **LQ Governance Playbook** — must be available as a connected file in the session (uploaded via the "+" button, or open in another Office app). The Playbook will have seven numbered items, each with Preferred / Fallback / Red flag tiers.

> If the Playbook is not in the session, stop and ask the user to upload it. Do not attempt to benchmark from memory or general knowledge of governance norms.

## Delegation Threshold

This skill produces a **draft for legal counsel review**. The five-tier classification (Match / Partial Match / Below Fallback / Red Flag / Omitted) and every proposed tracked-change amendment are **proposals only**. The reviewing lawyer must accept or reject each tracked change before circulation, and owns every change they accept. Ambiguous classifications must be **flagged for human decision, not auto-resolved**: if the locate or classify step is genuinely contested, mark the row Low-band (see Confidence Bands) and escalate to the user rather than picking a tier.

## Confidence Bands

Every row of the classification table carries a confidence band on the locate-and-classify step (independent of the finding taxonomy itself):

- **H (High)** — provision is unambiguously located, classification is uncontested against the Playbook tier definitions.
- **M (Medium)** — provision located but classification involves judgement (e.g. partial overlap with two tiers, defined-term mismatch that does not change substance). Proceed but mark for lawyer attention.
- **L (Low)** — locate step is ambiguous (provision arguably maps to two Playbook items, or target uses a governance model the Playbook does not contemplate), or classification is genuinely contested.

**Halt rule on Low-band:** for any row classified L, do not auto-resolve. Insert the row with classification field set to "Escalate — see note" and append a short note describing the ambiguity. Stop and ask the user to decide before drafting an amendment for that row.

Record the band in a dedicated Confidence column of the benchmark table.

## Operating Principles

- The Playbook is the standard. Your job is to classify the target against it, not to second-guess the standard.
- Every classification must be traceable to a specific section or schedule reference in the target document and to a specific item in the Playbook.
- Silence on a Playbook item is a finding (Omitted). Do not infer that silence equals alignment.
- Proposed amendments should be minimal and surgical. Draft in the voice and style of the target document. Do not rewrite structure, numbering, or defined terms.

## The Benchmark Protocol

For each of the seven items in the Playbook:

### Step 1 — Locate
Find the provision(s) in the target document that correspond to the Playbook item. Record the section, schedule, or clause reference. If no corresponding provision exists, record "Omitted" and proceed to Step 3.

### Step 2 — Classify
Assign exactly one classification:
- **Match** — target meets or exceeds the Preferred position
- **Partial Match** — target meets the Fallback but not the Preferred
- **Below Fallback** — target addresses the topic but falls short of the Fallback
- **Red Flag** — target exhibits the pattern described in the Playbook's Red flag
- **Omitted** — no corresponding provision in the target

### Step 3 — Gap and Amendment
For every classification other than Match:
- Write a one-sentence description of the specific gap. Cite AED amounts, section numbers, and language used.
- Draft a proposed amendment (surgical edit to existing provision, or new section for Omitted items).
- Insert the proposed amendment into the target Word document as a tracked change.

### Step 4 — Compile
Produce a benchmark table in the target document:

```
| # | Playbook Item | Target Reference | Classification | Confidence (H/M/L) | Specific Gap | Proposed Amendment |
```

**Visual discipline:**
- Match rows: no colour fill
- Partial Match rows: soft yellow fill (#FFF4CC)
- Below Fallback rows: soft orange fill (#FCE4A6)
- Red Flag and Omitted rows: soft red fill (#F4CCCC)

## Cross-App Behaviour

- **Excel Reconciliation Log** — if open, mirror each finding flagging source as "Playbook Benchmark"
- **PowerPoint Findings Slide** — if a Findings slide is already populated, add a second slide titled "Playbook Benchmark — Key Deviations" with a three-line summary of Red Flag and Omitted items; do not overwrite existing findings

## What Not to Do

- Do not benchmark against generic best practice, UK Corporate Governance Code, ADGM Guidance, or any external framework. The Playbook is the standard.
- Do not classify an item as Match when the target is silent. Silence is Omitted.
- Do not propose amendments that exceed the minimum needed to reach the Fallback position, unless the user specifically asks.
- Do not bundle findings. One row per Playbook item, always.
- Do not narrate the process. Work silently, deliver the table.

## On Tone

The reader is a Company Secretary, General Counsel, or Board member preparing for a meeting. They want the finding, the gap, and the fix. Keep every cell of the output table under thirty words.

## QA Remediation (LegalQuants, 2026-05)

This skill was reviewed by LegalQuants on 2026-05-11 and received a SOME CONCERN verdict against the Legal Skill Design Framework. The following additive remediation was applied without altering technical content:

- **Delegation Threshold** added as an explicit section. Makes clear that the five-tier classification and every tracked change are a draft for legal counsel review, that the lawyer owns each accepted change, and that ambiguous classifications must be flagged for human decision rather than auto-resolved.
- **Confidence Bands (H/M/L)** added for the locate-and-classify step, distinct from the finding taxonomy. Includes a halt rule on Low-band rows: do not auto-resolve, mark "Escalate — see note", and stop for user decision before drafting an amendment.
- **Benchmark table schema** extended with a Confidence column to carry the band on each row.
- **Frontmatter** updated to add `version: 1.0.0`, `last_reviewed: 2026-05`, and `last_reviewed_by: LegalQuants (QA remediation)`. Authorship attribution preserved to Alexios vdSK (Legal Quants Community).

Original benchmark protocol, operating principles, cross-app behaviour, and "What Not to Do" guardrails are unchanged.
