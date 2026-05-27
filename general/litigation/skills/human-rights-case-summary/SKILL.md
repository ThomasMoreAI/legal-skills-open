---
name: human-rights-case-summary
title: Human Rights Case Summary
description: Produces structured, citation-ready summaries of human rights decisions. Trigger when the user requests a human rights case summary, tribunal decision summary, or analysis involving ICCPR, ICESCR, ICERD, CAT, CRC, ACHR, ECHR, African Charter, UN treaty body views, or regional human rights court rulings.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/human-rights-case-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
tags: [analysis, research, summarization]
---

# Human Rights Case Summary

Structured summary of a human rights decision covering identification, reasoning, remedies, compliance, and impact.

## Prerequisites

Before drafting, confirm you have:

1. Primary decision text (judgment, opinion, order, or treaty body views)
2. Procedural posture and outcome stage (trial, appeal, enforcement, compliance)
3. Parties, forum, decision date, and citation
4. Relevant human rights instruments or provisions

If any material is missing, list required sources before drafting.

## Quick Start

1. Gather primary decision and procedural context.
2. Fill each template section; keep entries concise.
3. Run quality checks.
4. Flag gaps with `[VERIFY]` or `Unknown — source needed`.

## Output Template

```text
Case Identification
- Case name:
- Forum/Court/Tribunal:
- Decision date (Month Day, Year):
- Citation:
- Jurisdiction(s):
- Parties and roles:
- Procedural posture:
- Instruments/provisions at issue:

Executive Summary (3–6 sentences)
- Outcome:
- Core holding:
- Key principle clarified or expanded:
- Practical consequence:

Facts
- Chronology of key events:
- Alleged violations and affected groups:
- Government/actor conduct:

Claims and Defenses
- Petitioner/applicant claims:
- Respondent defenses:
- Admissibility/jurisdiction issues:

Legal Issues
- Issue 1:
- Issue 2:
- Issue 3:

Holdings
- Holding per issue:

Reasoning
- Interpretive method (textual, purposive, proportionality, margin of appreciation):
- Precedent or comparative law:
- Evidence and burden of proof:
- Balancing of competing rights:

Separate Opinions
- Concurrences:
- Dissents:
- Key divergence points:

Remedies and Orders
- Relief ordered:
- Compliance deadlines:
- Monitoring/enforcement mechanism:

Implementation Status
- Government response:
- Compliance actions:
- Follow-on litigation:

Precedential Value
- Binding scope:
- Persuasive influence:
- Doctrinal shift or novelty:

Social and Policy Impact
- Effects on affected communities:
- Institutional or legislative changes:
- Unintended consequences:

Open Questions
- Doctrinal gaps:
- Unresolved issues:

Sources
- Primary decision:
- Key filings:
- Secondary sources:
```

## Quality Checks

Run before finalizing:

- All facts tied to a source or marked `Unknown — source needed`
- Instruments and provisions cited accurately; use `[VERIFY]` if unsure
- Holdings and reasoning not conflated
- Remedies distinct from compliance status
- Dates in Month Day, Year format

## Pitfalls

- **Blurring analysis and advocacy** — maintain neutral tone; separate legal reasoning from policy impact
- **Omitting admissibility thresholds** — always address jurisdiction and admissibility explicitly
- **Ignoring enforcement limits** — for international/regional forums, specify compliance mechanisms and enforcement constraints
- **Missing posture details** — for U.S.-jurisdictional cases, note federal/state posture and standard of review
- **Drafting without sources** — if information is missing, request sources before writing the affected section
