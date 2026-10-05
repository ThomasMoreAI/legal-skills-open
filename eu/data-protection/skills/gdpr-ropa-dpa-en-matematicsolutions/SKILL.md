---
name: gdpr-ropa-dpa-en-matematicsolutions
title: GDPR RoPA + DPA EN - records of processing (Art. 30) and processor contracts (Art. 28)
description: 'Records of processing (RoPA, GDPR Art. 30) and data processing agreement (DPA, Art. 28) review assistant. Part 1 - RoPA: builds and validates the controller register (Art. 30(1)) and processor register (Art. 30(2)), enforcing the required fields (purposes, categories of data subjects and data, recipients, transfers, erasure timelines, security measures). Part 2 - DPA: checks a processor contract against the mandatory Art. 28(3)(a)-(h) clauses (controller''s instructions, confidentiality, security, sub-processing, assistance with data-subject rights, assistance with Art. 32-36, deletion/return, audits) + Chapter V transfers. Produces a draft register and a contract redline - it does NOT sign (a human act). Adds no connectors and makes no outbound calls of its own; the contract text you paste still goes to the model you have configured. Use when: "records of processing", "RoPA Art. 30", "data processing agreement", "DPA Art. 28", "processor contract review", "GDPR register".'
author: matematicsolutions
author_url: https://github.com/matematicsolutions/awesome-matematic-skills-en/tree/main/data-protection/skills/gdpr-ropa-dpa-en
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
---

# GDPR RoPA + DPA EN - records of processing (Art. 30) and processor contracts (Art. 28)

## Philosophy

A RoPA is a living accountability document and a processor contract is a list of mandatory clauses -
both can be checked mechanically against the article. The skill drafts/redlines; signing and filing
are human acts.

## Part 1 - Records of processing (Art. 30)

**Controller (Art. 30(1))** - mandatory fields per activity:
- name and contact details of controller / joint controller / DPO,
- purposes of the processing,
- categories of data subjects and categories of personal data,
- categories of recipients (incl. in third countries),
- transfers to third countries + safeguards (Chapter V),
- envisaged erasure time limits per category,
- general description of technical and organisational security measures (Art. 32).

**Processor (Art. 30(2))** - mandatory fields per Art. 30(2)(a)-(d): name and contact details of the
processor(s) **and of each controller** on whose behalf it acts (plus, where applicable, representatives
and the DPO), categories of processing per controller, transfers + safeguards, description of measures.
Naming controllers and sub-processors alone is NOT a complete register - contact details, representatives
and DPO are statutory fields.

The skill validates completeness (a missing field is a gap, not a guess) and flags activities needing a
DPIA => [[gdpr-dpia-en]]. The Art. 30(5) exemption (<250 persons) is narrow - and unavailable regardless
of headcount where processing is likely to result in a risk, is not occasional, includes Art. 9(1)
special categories **or Art. 10 criminal-convictions data** (each a separate disqualifier). Rarely
applies in practice.

## Part 2 - Processor contract review (Art. 28(3))

The contract MUST bind the processor to:
- **(a)** process **only on the controller's documented instructions** (incl. transfers),
- **(b)** ensure **confidentiality** of authorised persons,
- **(c)** apply **security** measures (Art. 32),
- **(d)** respect the conditions for engaging **sub-processors** (authorisation + flow-down),
- **(e)** **assist** the controller in fulfilling data-subject rights (Chapter III),
- **(f)** **assist** with Art. 32-36 compliance (security, breaches, DPIA),
- **(g)** **delete or return** the data at the end,
- **(h)** make available information and allow **audits/inspections**.

Plus: subject-matter, duration, nature and purpose, type of data, categories of data subjects
(Art. 28(3) sentence 1) and Chapter V transfers (SCCs/adequacy). The skill produces a **redline** of
missing/defective clauses (via [[clause-checklist-en]]).

## Tool - Art. 28 clause check (deterministic, offline)

Find the gaps in a processor contract with the script - pass the clauses present, get the missing ones (zero dependencies, offline):

```bash
python scripts/dpa_clause_check.py --present a,b,c,g
```

Returns `missing` (e.g. d, e, f, h) = the exact redline target. `complete` when all eight (a-h) are present.

## Governance boundary

Skill: builds/validates the register, redlines the contract, maps gaps to articles. Human: approves
content, negotiates, **signs** the contract, owns the register. Signing is never automatic.

## Companion

Clause library/redline: [[clause-checklist-en]]. DPIA: [[gdpr-dpia-en]]. Polish parity: `rodo-ropa-dpa-pl`.
