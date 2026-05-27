---
name: appellee-response-brief
title: Appellee's Response Brief
description: Drafts appellee response briefs for federal and state appellate courts, exploiting standards of review and record evidence to defend trial court decisions. Trigger when the user needs to respond to an appellant's opening brief or defend a favorable lower court ruling on appeal.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/appellee-response-brief
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [brief, drafting]
---

# Appellee's Response Brief

Defends the trial court's decision by exploiting deference standards, grounding every argument in the record, and systematically dismantling appellant's challenges.

## Quick Start

Gather before drafting:

1. **Appellant's opening brief** — every issue raised, claimed standards of review, key arguments
2. **Lower court decision** — opinion, order, or judgment under review
3. **Trial record** — transcripts, exhibits, supporting documents
4. **Appellate rules** — FRAP 28/32 or state equivalent; local rules, word limits, deadlines

## Deference Standards

The appellee's core advantage is deference. Always argue for the most deferential applicable standard.

| Standard | Applies To | Appellee Advantage |
|---|---|---|
| Abuse of discretion | Evidentiary rulings, case management | Affirm unless irrational |
| Clearly erroneous | Factual findings (bench trial) | Affirm if any evidence supports |
| De novo | Pure legal questions | Argue alternative grounds |
| Plain error | Unpreserved issues | Appellant bears heavy burden |

## Core Workflow

### 1. Counter-Statement of the Case

- Present record facts supporting affirmance with extensive citations (transcript pages, exhibit numbers)
- Correct appellant's factual omissions and mischaracterizations
- Emphasize procedural posture triggering deference

### 2. Argue Each Issue

For every issue the appellant raises, apply this sequence:

1. **Preservation** — raised below? If not, argue waiver/forfeiture
2. **Standard of review** — frame to maximize deference
3. **Record support** — cite specific evidence backing the lower court
4. **Distinguish cases** — factual differences, procedural posture, jurisdiction
5. **Alternative grounds** — argue affirmance on grounds the lower court didn't reach
6. **Harmless error** — even if error occurred, show it didn't affect the outcome

Lead with your strongest ground for affirmance. Address issues in your best narrative order, not necessarily appellant's.

### 3. Assemble Brief

- **Front matter**: cover page (correct color per FRAP 32 [VERIFY]), TOC with argumentative headings, Table of Authorities with pin cites, jurisdictional statement (if required), Statement of Issues reframed for affirmance
- **Argument**: structured per Step 2
- **Conclusion**: concise request for affirmance; no new arguments
- **Certificates**: Certificate of Compliance (word count, typeface), Certificate of Service

## Pitfalls and Checks

- Don't chase every minor point — focus on arguments that could actually reverse
- Address preservation/waiver issues early when applicable
- The record is your strongest tool — cite it relentlessly
- Raise alternative grounds for affirmance even if the lower court didn't rely on them
- Verify all citations or mark `[VERIFY]`
- Maintain a professional, measured tone — project confidence in the judgment below
