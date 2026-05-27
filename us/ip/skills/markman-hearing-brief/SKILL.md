---
name: markman-hearing-brief
title: Markman Hearing Brief
description: Drafts Markman Hearing Briefs for patent claim construction under the Phillips framework. Structures disputed-term analysis from intrinsic evidence (claims, specification, prosecution history) with local-rule-compliant formatting. Use when preparing claim construction briefs, Markman hearing submissions, or patent claim interpretation arguments in US federal court.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/markman-hearing-brief
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
tags: [brief, drafting, litigation]
---

# Markman Hearing Brief

Drafts a claim construction brief persuading the court to adopt the client's proposed constructions of disputed patent claim terms under the Phillips framework.

## Prerequisites

Gather before drafting:

- **Patent-in-suit** — claims, specification (column:line or ¶ cites), drawings
- **Prosecution history** — office actions, responses, amendments, examiner interviews
- **Disputed terms** — each term with client's and opposing party's proposed constructions
- **Party position** — plaintiff/defendant; opening/responsive brief
- **Local rules** — font, margins, page/word limits, caption format, CM/ECF requirements
- **Case management order** — briefing schedule, page limits, claim construction procedures

## Brief Structure

### 1. Caption & Title Page

Court name, parties, case number, and title per local rules. Title format: "[Party]'s Opening/Responsive Brief in Support of Claim Construction."

### 2. TOC / TOA

- **TOC**: all sections with page refs — generate after final draft
- **TOA**: cases (alphabetical, Bluebook), statutes/rules, treatises/dictionaries

### 3. Introduction

- Identify patent-in-suit, disputed terms, and proposed constructions
- Include claim construction summary table:

| Disputed Term | [Party]'s Construction | Opposing Construction |
|---|---|---|
| "[term]" | … | … |

- Roadmap arguments; write for a generalist judge

### 4. Factual & Procedural Background

- **The invention** — problem solved and how; plain language
- **Prosecution history** — amendments, arguments overcoming rejections, estoppel implications
- **Litigation posture** — accused products/processes, procedural history to Markman hearing
- Cite spec by column:line or ¶; prosecution history by date and document

### 5. Legal Standards

Present the Phillips v. AWH Corp., 415 F.3d 1303 (Fed. Cir. 2005) (en banc) framework:

| Principle | Rule |
|---|---|
| Ordinary meaning | POSITA meaning at time of invention |
| Intrinsic hierarchy | Claims → specification → prosecution history |
| Specification as context | Read claims in light of spec; do not import limitations unless clearly intended |
| Claim differentiation | Different terms presumed different meanings |
| Validity preservation | Construe to preserve validity; cannot override ordinary meaning |
| Prosecution history estoppel | Clear, unmistakable disavowals bind patentee |
| Extrinsic evidence | May inform but cannot contradict intrinsic record |

Cite analogous Federal Circuit cases with parentheticals.

### 6. Proposed Constructions — Per Disputed Term

For each term, follow this sub-structure:

**A. "[Claim Term]"**
- **Proposed construction:** [precise language]
- **Claim language** — usage in context; cross-claim differentiation analysis
- **Specification** — quoted passages showing usage/definition; operation description; purpose/advantages
- **Prosecution history** — applicant statements on meaning; narrowing amendments; prior-art distinctions
- **Extrinsic evidence** (if applicable) — dictionaries, expert declarations, treatises; must confirm, not contradict, intrinsic record
- **Rebuttal** — why opposing construction conflicts with intrinsic evidence, renders language superfluous, or fails under Phillips hierarchy

### 7. Conclusion

- Summary table restating each proposed construction
- Request court adopt constructions
- No new arguments or evidence

### 8. Certificate of Service

Date, parties served, method (CM/ECF), counsel signature. Comply with FRCP 5 and local rules.

## Critical Rules

- **Phillips framework governs** — organize every term through intrinsic evidence hierarchy
- **Never import spec limitations** unless patentee acted as own lexicographer or clearly disclaimed scope
- **Quote precisely** — spec by column:line or ¶; prosecution history by document and date
- **Anticipate opposition** — preemptively address strongest counterarguments per term
- **Consistency** — proposed constructions must work across all claims containing the term
- **Accessibility** — explain technical terms for a non-specialist judge
- **Tone** — professional, respectful, forceful; never dismissive of opposing positions

## Final QC Checklist

- [ ] All citations verified against source documents
- [ ] Cross-references correct
- [ ] Word/page count within local-rule limits
- [ ] TOC/TOA regenerated after final edits
- [ ] Local-rule formatting confirmed (font, margins, spacing, caption)
- [ ] Certificate of service complete
