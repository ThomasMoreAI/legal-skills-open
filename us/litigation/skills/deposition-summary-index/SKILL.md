---
name: deposition-summary-index
title: Deposition Summary with Key Document Index
description: Creates topic-based deposition summaries with exhibit-to-transcript citation mapping for U.S. commercial litigation. Use when a user provides a deposition transcript and requests a witness summary, deposition digest, exhibit index, cross-examination prep, or discovery-analysis packet.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/deposition-summary-index
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Deposition Summary with Key Document Index

Produces a neutral, topic-segmented deposition summary linked to exhibit IDs and page:line citations for fast litigation review.

## Prerequisites

Before starting, confirm you have:

- Complete transcript with stable page/line numbers
- Exhibit register with IDs, filenames, and privilege/redaction labels
- Witness name and reporter conventions (Q/A labels, speaker names)
- Jurisdiction, procedural rules, and target format (DOCX/PDF)
- Redaction scope and confidentiality instructions

Stop and escalate if privilege logs, sealing orders, or confidentiality controls are missing.

## Quick Start

1. Collect transcript + exhibit register
2. Normalize exhibit IDs to one consistent form
3. Segment testimony into topic blocks
4. Build topic summary table and document index table
5. Run completion checks and export

## Core Workflow

### 1. Validate and Normalize

- Canonicalize exhibit IDs (`Exh. 1`, `DEF. EXH. 2`, `PX-3` → single format)
- Extract transcript boundaries, witness name, counsel speakers, objections
- Resolve informal references ("the invoice") to formal exhibit IDs

### 2. Segment into Topics

- Split at explicit question shifts or sustained thematic changes
- Use plain, specific topic labels
- Draft 2–3 neutral sentences per topic: facts, dates, actions, uncertainties

### 3. Build Topic Summary Table

```
| Topic | Transcript Span | Summary (2–3 sentences) | Linked Exhibits |
|---|---|---|---|
| Contract negotiation | 12:1–14:22 | ... | [Exh. 3], [12:18–12:30] |
| Billing disputes | 31:4–38:10 | ... | [Exh. 8], [33:14–33:40] |
```

### 4. Build Key Document Index

Include every referenced exhibit with transcript cites, witness characterization, and risk flags.

```
| Exhibit ID | Transcript Mentions | Witness Characterization | Substance | Risk Notes |
|---|---|---|---|---|
| Exh. 3 | 12:10, 12:19–12:24 | "Contract signed by [witness] on [date]." | Formation details | [VERIFY] date ambiguity |
```

Flag: authentication gaps, hearsay concerns, missing metadata, contradictions.

### 5. Export

- Produce identical DOCX and PDF deliverables
- Preserve clickable anchors for exhibits and page:line citations
- Use professional heading hierarchy and consistent spacing

## Completion Checks

- [ ] Every transcript exhibit reference appears in the index
- [ ] No index entry references an exhibit absent from the transcript
- [ ] All page:line spans are accurate
- [ ] Privileged/sealed content removed or isolated per instruction

## Pitfalls

- **Neutrality**: No legal conclusions, argument, or advocacy language. Do not infer intent or motive unless explicitly on the record.
- **Ambiguity**: Mark unclear source text with `[VERIFY]`—never over-interpret.
- **Faithfulness**: Paraphrase testimony accurately; do not combine unrelated statements or use rhetorical language.
- **Citation style**: Follow counsel preferences for US filing conventions unless told otherwise.

---

**Key changes made:**

- **Frontmatter**: Removed non-spec `tags` field. Tightened `description` to focus on what it does and when to trigger, dropping the "trigger terms" list in favor of natural keyword coverage.
- **Structure**: Reorganized from a flat numbered process into Quick Start → Core Workflow → Completion Checks → Pitfalls for progressive disclosure.
- **Token efficiency**: Cut ~30% of tokens by eliminating redundant prose ("Use a two-column source mapping approach"), collapsing the Guidelines section into a compact Pitfalls list, and converting Prerequisites from numbered sentences to a bullet checklist.
- **Escalation guardrail** promoted to Prerequisites section (visible before any work starts) instead of buried at the end in Guidelines.
- **Templates preserved** with identical column structure but lighter surrounding text.
