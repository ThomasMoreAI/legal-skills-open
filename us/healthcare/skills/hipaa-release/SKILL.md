---
name: hipaa-release
title: HIPAA Release Authorization
description: Drafts a HIPAA Release Authorization form compliant with 45 CFR § 164.508 for authorizing disclosure of protected health information. Use when drafting HIPAA authorizations, PHI release forms, medical records releases, or healthcare privacy waivers alongside healthcare powers of attorney or advance directives.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/hipaa-release
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: healthcare
language: en
---

# HIPAA Release Authorization

Drafts a 45 CFR § 164.508-compliant authorization for disclosure of protected health information, typically executed alongside healthcare powers of attorney or advance directives. Output is a single execution-ready form with all client-specific fields marked in `[BRACKETS]`.

## Prerequisites

Gather before drafting:

1. **Patient info** — full legal name, DOB, address
2. **Healthcare agent(s)** — names and relationships (primary + successor)
3. **Cross-reference document** — Healthcare POA or Advance Directive
4. **Jurisdiction** — state witness/notary rules, sensitive-category consent requirements
5. **Scope instructions** — whether to include mental health, substance abuse, HIV/AIDS, genetic info

## Form Sections

Generate all sections in order:

| # | Section | Key Content |
|---|---------|-------------|
| 1 | Title | "Authorization for Release of Protected Health Information Pursuant to HIPAA" |
| 2 | Patient Identification | Full legal name, DOB, address; statement: "I authorize the use and disclosure of my PHI as described in this authorization." |
| 3 | Authorized Recipients | Each agent by name and role: `[Agent Name], designated as my Healthcare Agent`; include successors |
| 4 | Disclosing Parties | Broad: "Any health plan, physician, healthcare professional, hospital, clinic, laboratory, pharmacy, medical facility, or other covered entity that has provided payment, treatment, or services to me or possesses my PHI." |
| 5 | Scope of Information | Default comprehensive: complete medical record, mental health, substance abuse treatment, HIV/AIDS, genetic info. Flag state carve-outs needing separate consent. |
| 6 | Purpose | "To enable my designated healthcare agent(s) to make informed healthcare decisions on my behalf, communicate with my providers, and access all information necessary to execute their duties under my Healthcare POA or Advance Directive." |
| 7 | Duration & Expiration | Effective immediately; remains until written revocation or death. State whether authorization survives incapacity. |
| 8 | Revocation Rights | Required § 164.508 statements — see checklist below |
| 9 | Additional Statements | Right to refuse; treatment not conditioned on signing; right to copy |
| 10 | Execution Block | Patient signature, printed name, date; personal representative block (name, signature, relationship, authority); witness/notary lines per state law |

## § 164.508 Compliance Checklist

Every authorization must include all six statements:

- [ ] Right to revoke in writing at any time
- [ ] Revocation does not affect actions taken in reliance before receipt
- [ ] Disclosed information may be re-disclosed and no longer federally protected
- [ ] Right to refuse to sign
- [ ] Treatment/payment not conditioned on authorization (unless exception applies)
- [ ] Right to receive a copy of the signed authorization

## Sensitive Category Carve-Outs

Some categories require **separate consent** beyond the general HIPAA authorization:

| Category | Federal Rule | State Variation |
|----------|-------------|-----------------|
| Mental health / psychotherapy notes | Separate authorization required (§ 164.508(a)(2)) | Many states add restrictions |
| Substance abuse treatment | 42 CFR Part 2 requires separate consent | Stricter re-disclosure rules |
| HIV/AIDS | No federal carve-out beyond HIPAA | ~35 states require specific consent |
| Genetic information | GINA covers employment/insurance | State genetic privacy laws vary |

Flag applicable state rules and draft supplemental consent language where needed.

## Drafting Rules

- All placeholders use `[BRACKETS]` with descriptive labels
- Cross-reference named agents against the client's Healthcare POA
- Plain language with legal precision; use numbered/lettered sections
- Include personal representative authority documentation fields (court appointment, POA)
- Footer: "This is a legal document. Review by qualified legal counsel is recommended before execution."
- Do not include regulatory explanations in the form — keep it execution-ready
- If jurisdiction known, tailor witness/notary and sensitive-info requirements; if unknown, include optional blocks with guidance notes
