---
name: representation-agreement
title: Representation Agreement (Litigation)
description: 'Drafts a U.S. litigation representation agreement covering scope, fees, costs, duties, conflicts, and termination. Use when preparing an engagement letter, fee agreement, retainer, or attorney-client representation agreement at intake or pre-filing. Trigger: representation agreement, engagement letter, retainer, contingency fee, personal injury, litigation.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/representation-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Representation Agreement (Litigation)

Generates a matter-specific engagement agreement between attorney/firm and client for U.S. litigation, with personal-injury-oriented fee structures.

## Prerequisites

Collect before drafting:

1. **Client identity** — legal name, entity type, authorized signer, contact info
2. **Matter summary** — dispute description, opposing parties, venue/jurisdiction, case caption if filed
3. **Fee model** — hourly, flat, contingency, or hybrid; rates; retainer; trust handling
4. **Conflicts check** — completed; waivers identified
5. **Cost policy** — advance vs. direct pay; approval thresholds; lien rights
6. **Jurisdictional rules** — state bar written-fee-agreement and disclosure requirements
7. **Key dates** — effective date, imminent deadlines

## Quick Start

1. Populate the intake table below with all known values
2. Select the applicable fee model (Section 3) and delete the others
3. Assemble agreement sections 1–15 in order
4. Attach rate table or contingency addendum as applicable
5. Verify against jurisdiction-specific rules (see Pitfalls)

## Intake Variables

| Field | Value |
|---|---|
| Firm legal name | |
| Attorney(s) & bar numbers | |
| Firm address / phone / email | |
| Client legal name | |
| Client address / phone / email | |
| Entity representative & title | |
| Matter description | |
| Court / venue / case no. | |
| Effective date | |
| Fee model | |
| Retainer amount & trust treatment | |
| Billing cadence & payment due | |
| Cost approval threshold | |
| Communication preferences | |
| File retention period | |
| Governing law / venue | |

## Agreement Sections

Assemble in this order:

1. **Parties and Effective Date** — full legal names; signer authority for entities
2. **Scope of Representation** — covered matter and services (investigation, pleadings, discovery, motions, ADR, trial); excluded services (appeals, collection, unrelated claims); expansion by written amendment only
3. **Fee Arrangement** — select one:
   - *Hourly* — rates table by timekeeper, billing increment, rate-change notice
   - *Flat Fee* — amount, covered tasks, treatment of unused portion
   - *Contingency* — percentage(s) by phase, definition of "recovery," cost-deduction order, jurisdictional client acknowledgments
   - *Hybrid* — hourly + contingency or flat + success fee
4. **Retainer / Advance Deposit** — amount, trust account treatment, replenishment threshold, non-replenishment consequences
5. **Costs and Expenses** — itemized categories (filing fees, service, transcripts, experts, travel, research, copying); advance vs. client-direct; approval required above $[X]
6. **Billing and Payment** — frequency, payment terms, interest/late charges if permitted, attorney lien rights
7. **Client Responsibilities** — candor, evidence preservation, litigation hold compliance, attendance, no direct opposing-party contact
8. **Attorney Responsibilities** — competent/diligent representation, communication cadence, independent professional judgment
9. **Confidentiality and Privilege** — duty of confidentiality, privilege ownership, permitted/required disclosure exceptions
10. **Conflicts of Interest** — check completed, waivers disclosed/attached, future unrelated representations
11. **Termination and Withdrawal** — client termination right, withdrawal grounds per rules, file transfer, final accounting, unearned-fund refund
12. **File Retention** — retention period, destruction policy after notice
13. **Dispute Resolution** — fee dispute program / mandatory arbitration; optional mediation
14. **Governing Law and Miscellaneous** — governing law, venue, entire agreement, amendments in writing, severability, notices, client-name use only with consent
15. **Signatures and Acknowledgments** — signature blocks for firm and client; acknowledgments for fee terms, scope, arbitration rights

## Fee-Model Addenda

### Rate Table (hourly or hybrid)

| Timekeeper | Role | Hourly Rate |
|---|---|---|
| | | |

### Contingency Fee Schedule

| Phase | % Fee |
|---|---|
| Pre-suit resolution | |
| Post-filing, pre-trial | |
| Trial | |
| Appeal | |

- State whether costs deducted before or after fee calculation
- Include statutory/rule-mandated disclosures
- Provide illustrative fee-calculation example

## Pitfalls

- **Jurisdiction compliance** — match the state's written-fee-agreement and contingency-disclosure rules; insert required consumer notices
- **No outcome promises** — never guarantee recovery
- **Scope creep** — exclude appeals and collection unless expressly included
- **Retainer clarity** — specify whether any portion is earned on receipt
- **Personal injury specifics** — verify state contingency limits, medical-lien disclosures, and settlement-authority requirements
- **Conflicts waivers** — attach as a separate informed-consent document
- **Plain language** — use consistent defined terms throughout
