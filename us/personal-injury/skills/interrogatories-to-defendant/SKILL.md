---
name: interrogatories-to-defendant
title: Interrogatories to Defendant — Personal Injury
description: Drafts plaintiff's interrogatories to defendant in personal injury litigation with caption, definitions, instructions, and substantive questions. Triggers when user needs to draft interrogatories, written discovery requests to a defendant, or PI discovery sets. Enforces numerical limits, subpart counting, and contention interrogatory practices.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/interrogatories-to-defendant
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
tags: [drafting, litigation, pleading]
---

# Interrogatories to Defendant — Personal Injury

Drafts interrogatories that pin down defendant's factual contentions, identify witnesses and evidence, and build the foundation for depositions and trial.

## Required Inputs

1. **Caption details** — court, case number, party names
2. **Operative pleadings** — complaint (claims) and answer (affirmative defenses)
3. **Jurisdiction** — federal (FRCP 33) or state; confirm applicable rules
4. **Numerical limit** — FRCP 33 default is 25 including discrete subparts; state rules vary
5. **Set designation** — first, second, etc.
6. **Attorney info** — name, bar number, firm, address, phone, email

## Document Structure

### 1. Caption

Standard litigation caption. Title: "Plaintiff's [First/Second/etc.] Set of Interrogatories to Defendant."

### 2. Introduction

- Propound under governing rule (FRCP 33 or state equivalent)
- State response deadline (30 days unless local rule differs)
- Require separate, full, written answers under oath

### 3. Definitions

Define at minimum:

| Term | Scope |
|------|-------|
| IDENTIFY (person) | Name, address, phone, employer, relationship to parties |
| IDENTIFY (document) | Author, date, type, custodian, location, Bates number |
| IDENTIFY (communication) | Date, participants, medium, substance |
| PERSON | Natural persons and all entities |
| DOCUMENT | All tangible and ESI formats |
| COMMUNICATION | Every form of information exchange |
| INCIDENT | Specific event(s) giving rise to the lawsuit |
| YOU/YOUR | Defendant including agents, employees, representatives |

Draft broadly to prevent evasion; keep defensible.

### 4. Instructions

- Duty to supplement (FRCP 26(e) or state equivalent)
- Answer each interrogatory separately and fully
- Privilege claims require a privilege log
- Duty to investigate despite lack of personal knowledge
- Answer subparts separately
- Business-records option under FRCP 33(d) with specification

### 5. Substantive Interrogatories

Tailor to the specific facts, claims, and defenses. Organize by category:

**A. Witness Identification**
- All persons with knowledge of relevant facts (identity, substance of knowledge)
- Expected trial witnesses and testimony subjects
- Experts retained or consulted (identity, opinions, basis)

**B. Defendant's Version of Events**
- Factual account of the incident
- Acts or omissions attributed to plaintiff (contributory/comparative fault basis)

**C. Evidence Identification**
- Documents, photos, recordings, tangible evidence related to the incident
- Statements obtained from any person (written, recorded, oral summaries)
- Surveillance or investigation regarding plaintiff or incident

**D. Personal Injury–Specific**
- Defendant's knowledge of plaintiff's injuries
- Insurance coverage (carrier, policy number, limits)
- Prior similar incidents or claims involving defendant
- Mitigation-of-damages contentions with factual basis

**E. Contention Interrogatories**
For each affirmative defense: state every supporting fact, identify every supporting document, identify every knowledgeable person.

### 6. Signature Block & Certificate of Service

- Attorney signature, date, name, bar number, firm, address, phone, email
- Certificate of service: method, date, recipient counsel details

## Pitfalls & Checks

- **Count subparts rigorously** — discrete subparts count toward the cap; structure compound questions carefully
- **Tailor every set** — never submit generic form interrogatories without case-specific customization
- **Proportionality** — each interrogatory must satisfy FRCP 26(b)(1) relevance and proportionality
- **Avoid objection bait** — do not draft overbroad, unduly burdensome, or privilege-invading questions
- **Strategic sequencing** — front-load questions yielding deposition and settlement value
- **Check local rules** — some jurisdictions mandate pattern interrogatories (e.g., California DISC-001) or impose different limits
- **Contention timing** — some courts defer contention interrogatories to late discovery; flag for attorney review if served early
