---
name: military-law-summary
title: Military Law Summary
description: Generates structured summaries of military law matters including courts-martial, UCMJ disciplinary actions, administrative separations, and appellate decisions. Trigger when a user needs a reference summary of a military justice proceeding, CAAF/CCA opinion, Article 15 action, or service regulation issue for JAG officers, command staff, or military legal practitioners.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/military-law-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: criminal
language: en
tags: [analysis, litigation, summarization, summary]
---

# Military Law Summary

Produces a standalone structured summary of a military law matter — court-martial, disciplinary action, regulatory issue, or appellate decision — for JAG officers, command staff, and practitioners.

## Quick Start

1. Collect source materials: court-martial decisions, appellate opinions (CAAF, service CCAs), UCMJ provisions, MCM guidance, administrative records, or service regulations.
2. Identify matter details: service branch, rank/status, proceeding type (Article 15, summary/special/general court-martial, admin separation, appellate review).
3. Produce the summary using the output structure below.

## Output Structure

### 1. Header Block

| Field | Content |
|---|---|
| Matter | Case name or regulatory matter identifier |
| Service Branch | Army / Navy / Air Force / Marines / Coast Guard / Space Force |
| Personnel | Rank, status, role |
| Proceeding Type | Article 15 / Summary CM / Special CM / General CM / Admin separation / Appellate review / Regulatory |
| UCMJ Articles | Charged articles (e.g., Art. 120, Art. 134) |
| Disposition Date | Date of decision or action |
| Reviewing Authority | CAAF / Service CCA / Convening authority / Other |

### 2. Factual Background

- Core facts in chronological order
- Relevant military context (unit, deployment status, command relationship)
- Nature of alleged offenses or regulatory issues

### 3. Procedural History

- Charges preferred and referred; forum and plea
- Findings by article and specification
- Sentence imposed
- Post-trial convening authority action
- Appellate history (CCA, CAAF, Supreme Court if applicable)

### 4. Legal Analysis

Per significant issue:

- **Issue**: Framed as a question
- **Standard of review**: De novo, abuse of discretion, factual sufficiency, etc.
- **Controlling authority**: UCMJ article, MCM provision, binding precedent
- **Reasoning**: How authority was applied to facts
- **Holding**: Outcome
- **Dissents/concurrences**: Key reasoning if any

Note divergence from civilian criminal law where relevant.

### 5. Elements and Evidence (Offense Cases)

| Element | Evidence Presented | Sufficiency |
|---|---|---|
| {Element} | {Key evidence} | Met / Not met |

### 6. Administrative Matters (If Applicable)

- Applicable standard (characterization of service, fitness-for-duty, clearance adjudication)
- Deference afforded to military decision-makers
- Collateral consequences: benefits, veteran status, employment impact

### 7. Practical Implications

- Effect on future practice and command guidance
- Changes to established precedent
- Unresolved questions or anticipated developments
- Actionable takeaways for advisors and commanders

## Pitfalls and Checks

- **Citations**: Use standard military format — UCMJ articles (Art. 32, UCMJ), MCM rules (R.C.M. 1001), CAAF opinions (*United States v. Smith*, 80 M.J. 200 (C.A.A.F. 2020)). Mark unverified citations with `[VERIFY]`.
- **Do not conflate with civilian procedure**: Military justice is a distinct framework. Flag where military due process diverges (command influence, military judge authority, unlawful command influence).
- **Phase awareness**: Identify pre-trial, trial, post-trial/clemency, or appellate posture and tailor analysis accordingly.
- **Constitutional rights in military context**: Address Art. 31(b) vs. Miranda, search authorization vs. warrant (4th Amend.), First Amendment limits for service members.
- **Neutral posture**: Do not advocate; summarize analytically.
- **Standalone completeness**: Summary must be usable without the underlying source documents.
