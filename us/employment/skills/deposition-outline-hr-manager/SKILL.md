---
name: deposition-outline-hr-manager
title: Deposition Outline — HR Manager
description: Creates strategically organized deposition outlines for examining HR managers in employment litigation. Covers hiring practices, personnel files, complaint investigations, termination procedures, comparative treatment, policy compliance, and impeachment preparation. Use when deposing an employer's HR representative or preparing for HR manager examination.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/deposition-outline-hr-manager
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
---

# Deposition Outline — HR Manager

Generates a structured deposition outline for examining the defendant employer's HR manager in contested employment matters.

## Quick Start

Gather before drafting:

- Operative pleadings — claims, defenses, disputed issues
- Personnel file — applications, evaluations, disciplinary records, termination docs
- HR policies — handbook, anti-discrimination policy, complaint procedures, progressive discipline
- Communications — emails, texts, investigation notes involving the HR manager
- Prior testimony — declarations, interrogatory responses, prior depositions
- Comparator data — similarly situated employees, treatment, outcomes
- Investigation files — complaint reports, investigation summaries

## Outline Sections

### I. Background and Foundation

- Name, title, reporting structure, tenure
- HR education, certifications (PHR/SPHR)
- Role in hiring, discipline, termination decisions
- **Lock in**: "You're the person most knowledgeable about HR policies at [Company]?"

### II. Policies and Procedures

- Authenticate handbook version in effect
- Anti-discrimination, anti-harassment, complaint, progressive discipline policies
- Termination approval process
- **Pin down deviations**: "Was this policy followed in [plaintiff]'s case?"

### III. Plaintiff's Employment History

- Hiring decision (who, why, qualifications)
- Duties, performance expectations, evaluations, trajectory
- Commendations, raises, promotions, prior discipline
- **Establish competence baseline** before adverse events

### IV. Triggering Events

- When and how HR became involved
- Protected activity timeline (complaint, leave request, whistleblowing)
- HR's response and communications with decision-makers
- **Temporal proximity**: timeline between protected activity and adverse action

### V. Investigation

- Investigator, methodology, timeline, witnesses, documents reviewed
- Findings, conclusions, credibility assessments
- **Probe thoroughness**: compare investigation of plaintiff vs. others

### VI. Termination Decision

- Decider identity — HR as decider or advisor?
- Stated reasons — lock in precisely
- Supporting documents; decision date vs. communication date
- Alternatives considered (PIP, transfer, demotion)?
- **Shifting explanations**: compare to interrogatories, position statements, prior testimony

### VII. Comparative Treatment

- Similarly situated employees outside protected class
- Same supervisor, position, time period; comparable conduct
- Different outcomes — document systematically:

| Employee | Protected Class | Conduct | Outcome | Decision-Maker |
|---|---|---|---|---|
| Plaintiff | [class] | [conduct] | Terminated | [name] |
| Comparator A | [class] | [comparable] | [outcome] | [name] |

### VIII. Pattern and Practice

- Prior discrimination/retaliation complaints in the department
- HR's handling of prior complaints
- EEOC charges or lawsuits involving same decision-makers
- Anti-discrimination training records (when, content, attendance)

### IX. Document Authentication

Mark and authenticate: personnel file, investigation files, emails, policy documents, termination approval docs.

### X. Impeachment Preparation

- Compare testimony to: interrogatory responses, EEOC position statement, personnel file documents, plaintiff's version
- Note inconsistencies for trial impeachment

## Examination Techniques

- **Open-ended first**: "Tell me everything you know about…" — lock in the narrative
- **Then narrow**: specific questions with document references
- **Commit-credit-confront**: get commitment, show favorable document, confront with inconsistency
- **Exhaust "I don't recall"**: use specific documents to refresh recollection

## Pitfalls and Checks

- Lock in stated termination reason early — before showing contradictory evidence
- Track which documents were in the file at termination vs. added later
- Note documents missing from file that should be there
- Time allocation: ~60% termination decision and comparators, ~20% policies/investigation, ~20% background/authentication

---

Key changes from original:

- **Removed `tags`** — not part of the Agent Skills spec (only `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools` are valid)
- **Restructured to best-practice layout**: Quick Start → Core Workflow → Pitfalls and Checks
- **Renamed "Prerequisites"** → "Quick Start" with tighter formatting
- **Renamed "Guidelines"** → "Pitfalls and Checks" for clarity
- **Removed the "Silence" examination technique** — general deposition knowledge Claude already has
- **Compressed verbose sections** — Investigation, Document Authentication, and Pattern/Practice sections tightened significantly
- **Removed redundant overview sentence** that repeated the description
- **Cut ~30% token count** while preserving all domain-specific legal content

I wasn't able to write to the file due to permissions. Please grant write access and I'll save it, or you can copy the content above directly.
