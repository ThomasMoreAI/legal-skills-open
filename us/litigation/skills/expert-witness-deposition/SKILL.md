---
name: expert-witness-deposition
title: Expert Witness Deposition
description: Drafts litigation-ready expert witness deposition workflows for U.S. federal and state matters, covering preparation, examination, and defense strategy. Use when handling expert depositions, Daubert or Frye admissibility issues, Rule 26(a)(2) or 26(b)(4) disclosures, qualification and methodology challenges, bias and compensation probing, prior testimony impeachment, or work-product objections.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/expert-witness-deposition
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Expert Witness Deposition

Produces a structured playbook to take, defend, or preserve a record for expert depositions under Daubert/Frye admissibility standards.

## Quick Start

1. Confirm governing standard: federal **Daubert** vs **Frye**/state variant [VERIFY jurisdiction].
2. Set objective: **exclude**, **limit**, **impeach**, or **defend** the expert.
3. Collect: Rule 26(a)(2) disclosure package, CV, report, materials list, prior testimony/publications.
4. Choose mode:

| Mode | Goal | Deliverable |
|---|---|---|
| Taking | Challenge qualifications, methodology, basis, opinions | Deposition outline + question set + record log |
| Defending | Prepare expert to withstand Daubert attacks | Mock-exam plan + response models + objection protocol |
| Mixed | Both attack and defense in one run | Two-side workbook: attack issues mapped to defense counters |

## Intake Checklist

Gather before drafting:

- Case caption, judge, jurisdiction, deposition type
- Expert report and addenda
- Rule 26(a)(2)(B) details: opinions, bases, data, exhibits, compensation [VERIFY]
- Expert CV and publication list
- Prior testimony transcripts
- Exhibits (written and electronic)
- Pending Daubert/exclusion motions
- Discovery rulings affecting scope

## Taking: Questioning Framework

Use this fixed order: Qualifications → Engagement/compensation → Materials reviewed → Methodology → Each opinion → Application to facts → Prior positions.

For each topic, force narrow answers first, then expand with one follow-up.

| Topic | Key asks | Daubert/Frye value |
|---|---|---|
| Qualifications | scope, recency, hands-on experience | Limits admissible field |
| Engagement/compensation | retention chain, total fees, repeat retainers | Bias/credibility |
| Materials reviewed | who provided, what omitted, assumptions | Foundation strength |
| Methodology | testing, standards, peer review, error rate | Gatekeeping reliability |
| Opinions | precision, certainty, alternatives, contradictions | Helpfulness to trier of fact |
| Prior work | prior testimony/publications | Impeachment, consistency |

### Opinion Lock-In

For every opinion, capture:

1. Exact stated opinion (no shorthand)
2. Supporting facts/data
3. Methodology used
4. Assumptions made
5. What changed facts would invalidate it
6. Equally valid alternatives
7. Any opinions not in the written report

Rate each opinion's vulnerability (high/medium/low) and tag whether it supports exclusion, limitation, or impeachment.

## Daubert/Frye Motion Readiness

Map deposition admissions to these challenge grounds:

| Challenge | Record evidence needed |
|---|---|
| Methodology not testable/peer-reviewed | Witness admissions, publications, expert literature |
| No accepted standards | Missing protocols, calibration, reproducibility gaps |
| No known error rate | Calculation methodology and validation gaps |
| Not generally accepted | Rebuttal sources, authoritative treatise contrasts |
| Unreliable application to facts | Omitted/contradictory facts, wrong assumptions |
| Unsupported opinions | Missing data linkage and analytic steps |

## Defending: Protection Framework

1. **Three-session prep**: opinions review, methodology deep-dive, mock hostile cross.
2. Enforce "explain, don't advocate" — technical explanation only, no legal conclusions.
3. Scope boundaries: stick to disclosed opinions, concede limits explicitly, avoid surprises.
4. Prior-consistency prep: distinguish each prior statement by time, facts, or standards.
5. Preserve work-product and strategy communications; finalize what can be answered under Rule 703/fact basis demands [VERIFY].
6. Build objection playbook for defending counsel.

Defense brief packet should include:
- Disclosed-opinion index (report section → witness answer)
- Methodology defense notes (standards, peer support, replication)
- Contradiction-response matrix (prior testimony/publications)
- Bias mitigation language

## Objection and Privilege Handling

US Federal baseline [VERIFY applicability in state proceedings]:

| Issue | Objection basis | Purpose |
|---|---|---|
| Draft materials | Work-product [VERIFY] | Limit production scope |
| Counsel-assistance details | Privilege [VERIFY] | Protect preparation strategy |
| Factual assumptions | Relevance / foundation | Force precision before opinion expansion |
| Scope beyond report | Opinions not disclosed | Cap surprise testimony |

## Pitfalls

- Do not assume Frye applies in all states — flag jurisdiction explicitly [VERIFY].
- Do not let counsel seek unconstrained legal conclusions from the expert.
- Separate admissibility attacks into **exclusion**, **limitation**, and **weight** outcomes.
- Track non-asked/avoided answers as preservation evidence.
- Produce record citations for each critical admission used in dispositive motions.
- Do not overstate Daubert/Frye standards — tie every argument to record facts.
- End with a hearing-ready summary for deposition officer and lead counsel.

## References

- FRCP 26(a)(2)(B), 26(b)(4) [VERIFY]
- FRE 702, 703 [VERIFY]
- Daubert v. Merrell Dow Pharmaceuticals, 509 U.S. 579 (1993)
- General Electric Co. v. Joiner, 522 U.S. 136 (1997)
- Kumho Tire Co. v. Carmichael, 526 U.S. 137 (1999)
- Frye v. United States, 293 F. 1013 (D.C. Cir. 1923) [VERIFY state-usage scope]

---

**Key changes made:**

- **Frontmatter**: Removed non-spec `tags` field; tightened description to be concise while keeping all trigger keywords naturally embedded.
- **Structure**: Reorganized from numbered "Output Structure / Process" subsections into scannable top-level sections (Quick Start, Intake, Taking, Defending, etc.).
- **Token efficiency**: Removed the `DEPOSITION WORKSET` and `Defense Brief Packet` code blocks in favor of inline bullet lists. Removed the `Opinion Block` code block and integrated it as a numbered list. Eliminated redundant "Prerequisites" section by folding those steps into Quick Start.
- **Conciseness**: Cut ~50 lines (154 → ~105) while preserving every domain-specific table, checklist item, legal rule reference, and [VERIFY] tag.
- **Renamed sections**: "Guidelines" → "Pitfalls" for clearer intent; "Output Structure / Process" removed as a wrapper heading.

Want me to retry writing the file, or is the output above sufficient?
