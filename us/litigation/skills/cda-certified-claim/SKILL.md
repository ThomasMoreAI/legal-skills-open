---
name: cda-certified-claim
title: CDA Certified Claim
description: Drafts U.S. Contract Disputes Act (CDA) certified claims for federal government contracts, covering FAR Part 33 compliance, entitlement/quantum sections, certification language, and final-decision demand. Use when preparing a CDA claim, certified claim, or submission to a contracting officer under the Contract Disputes Act.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/cda-certified-claim
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# CDA Certified Claim

Produces a CDA-compliant claim package that preserves appeal rights and supports entitlement and quantum under 41 U.S.C. §§ 7101–7109.

## Prerequisites

Gather before drafting:

1. Executed contract and all modifications (including disputes/changes clauses)
2. Contracting officer name, title, office address, submission method
3. Chronology of events with source documents
4. Damages data with source records (cost reports, invoices, payroll, schedules)
5. Authorized company official for certification (if claim > $100,000)

## Quick Start

Structure the claim package using the sections below in order. Replace all bracketed fields with case-specific facts.

## Claim Structure

### 1. Header

- Claimant: full legal name and address (as in contract)
- Contracting Officer: name, title, agency, office address
- Contract Number (including mods), Award Date, Submission Date
- Subject: "Certified Claim under the Contract Disputes Act (CDA)"

### 2. Executive Summary (5–10 lines)

- Contract purpose, type, period of performance
- Claim type: change / differing site conditions / delay / breach
- Relief requested: definite sum and/or time extension
- Request for final decision

### 3. Contract Background

| Field | Detail |
|---|---|
| Contract type | [FFP / CPFF / T&M] |
| Scope | [brief scope] |
| POP | [start–end] |
| Value | [base + options] |
| Key clauses | [clause numbers/titles] |

### 4. Statement of Claim (Definite Relief)

- Monetary: `$[exact amount]` — no ranges or estimates
- Time extension: `[exact days]` calendar/work days (if applicable)
- Identify claim theory and triggering government act/omission

### 5. Factual Narrative

Chronological table with exhibit cites:

| Date | Event | Personnel | Exhibit |
|---|---|---|---|
| [YYYY-MM-DD] | [event] | [names/titles] | [Ex. #] |

### 6. Entitlement

Map claim theory elements to facts and authority:

| Theory | Elements | Authority | Facts Satisfied |
|---|---|---|---|
| Change | [elements] | FAR 52.243-1 / 52.243-2 | [facts] |
| Differing Site Conditions | [Type I/II] | FAR 52.236-2 | [facts] |
| Delay/Suspension | [elements] | [clause] | [facts] |

Required authority anchors:

- 41 U.S.C. §§ 7101–7109 (CDA)
- FAR Part 33; FAR 33.211 (final decision requirements) [VERIFY]
- Case law: include full name, citation, one-sentence holding

### 7. Quantum

| Cost Category | Basis | Amount | Source |
|---|---|---|---|
| Direct labor | [hours × rate] | $ | [Ex. #] |
| Materials | [qty × unit] | $ | [Ex. #] |
| Equipment | [rental/owned] | $ | [Ex. #] |
| Subcontracts | [COs/invoices] | $ | [Ex. #] |
| Indirects | [rate × base] | $ | [Ex. #] |
| Delay/overhead | [method] | $ | [Ex. #] |
| Productivity loss | [method] | $ | [Ex. #] |
| CDA interest | [rate + period] | $ | [Ex. #] |
| **Total** | | **$[total]** | |

- Delay/home-office overhead: specify method (e.g., Eichleay) and inputs
- Interest: cite 41 U.S.C. § 7109

### 8. Certification

**Required if claim > $100,000.** Insert exact statutory text without modification:

> "I certify that the claim is made in good faith; that the supporting data are accurate and complete to the best of my knowledge and belief; that the amount requested accurately reflects the contract adjustment for which the contractor believes the Government is liable; and that I am duly authorized to certify the claim on behalf of the contractor."

Signature block: Name, Title, Company, Date.

For claims ≤ $100,000: omit certification but still request a final decision.

### 9. Demand for Final Decision

State: "This is a claim under the CDA and requests a final decision by the Contracting Officer."

Include appeal preservation language per 41 U.S.C. § 7104 [VERIFY].

### 10. Exhibits

| Exhibit | Description | Date | Relevance |
|---|---|---|---|

Every factual assertion and quantum line item must cite an exhibit.

### 11. Delivery

State delivery method. Attach proof of receipt. Retain a complete copy.

## Pitfalls

- **No definite sum** — never use ranges, estimates, or "TBD"
- **Missing exhibit links** — every fact and cost must map to an exhibit
- **Wrong contracting officer** — verify addressee before submission
- **Unverified case law** — confirm jurisdiction (ASBCA, CBCA, COFC, Fed. Cir.)
- **Certification omitted** — required for claims > $100,000; omission may waive appeal rights
- **Uncertain citations** — mark with `[VERIFY]`
- **Argumentative tone** — keep factual and objective throughout
