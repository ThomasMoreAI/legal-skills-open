---
name: hipaa-release-authorization
title: HIPAA Release Authorization
description: 'Drafts HIPAA-compliant PHI release authorizations for estate-planning workflows under 45 CFR §164.508. Use when drafting release forms, healthcare POA support documents, or record-access instruments. Triggers: HIPAA release, PHI authorization, healthcare agent access, advance directive support, medical record release.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/hipaa-release-authorization
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: trusts-and-estates
language: en
---

# HIPAA Release Authorization

Generates a 45 CFR §164.508-compliant authorization permitting designated recipients to access a patient's protected health information (PHI) from covered entities, typically in an estate-planning context.

## Quick Start

Gather before drafting:

1. **Jurisdiction** — state governs signature and witness/notary formalities
2. **Patient identity** — legal name, DOB, contact details
3. **Recipients** — healthcare agent, successor agent(s), other representatives
4. **Disclosing entities** — providers, hospitals, labs, pharmacies, health plans
5. **PHI scope** — all records or limited categories
6. **Purpose and duration** — expiration date, event, or condition
7. **Representative authority** (if applicable) — POA, guardianship order, court appointment
8. **Related documents** — healthcare proxy, advance directive for terminology alignment

## Required Sections

Every authorization must include these elements per §164.508:

| Section | Key requirement |
|---|---|
| Patient identification | Name, DOB, contact |
| Authorization statement | Voluntary, specific written consent |
| Authorized recipients | Agent names, roles, relationships — no ambiguity |
| Disclosing entities | Covered entities / record holders |
| PHI scope | Explicit categories; do not mix "all records" with narrow limits |
| Purpose | Specific estate-planning healthcare decision-making purpose |
| Expiration | Explicit end date, event, or condition |
| Required notices | Re-disclosure warning, treatment non-conditioning, right to refuse |
| Revocation | How and where written revocation is sent; prospective-only effect |
| Execution block | Patient signature first, then representative if applicable |
| Witness/notary | Only where state law requires [VERIFY] |

## Draft Workflow

1. **Confirm inputs** against the Quick Start checklist; flag any gaps.
2. **Select PHI scope** — if client wants full-record access, state it unambiguously; otherwise enumerate categories. Sensitive categories (substance use, mental health, genetic, HIV/AIDS) require explicit inclusion [VERIFY].
3. **Draft the form** using this structure:
   - Title citing 45 CFR §164.508
   - Patient identification block
   - Authorization statement
   - Disclosers list
   - Recipients list (match names/roles to healthcare POA document)
   - PHI scope with checkbox-style selection
   - Purpose statement tied to healthcare directives
   - Duration clause (date, revocation, or death — whichever first)
   - Patient rights / required statements (all six §164.508 notices)
   - Execution block (patient, then representative if signing on behalf)
   - Witness/notary block if state law applies
4. **Validate** — all placeholders visible, recipients consistent across sections, terminology aligns with governing POA/directive.
5. **Add state-specific addendum** only when confirmed for target jurisdiction.

## Pitfalls

- Never authorize broader disclosure than needed unless client explicitly requests full-record access.
- Never leave recipient or discloser fields unidentified.
- Never leave representative signature fields blank without authority documentation.
- Federal law is not exclusive — state mandates may impose additional form requirements [VERIFY].
- Estate-planning variants must match healthcare POA terminology in the core delegation document [VERIFY].
- Include attorney-review language in cover memo if template is client-facing.
