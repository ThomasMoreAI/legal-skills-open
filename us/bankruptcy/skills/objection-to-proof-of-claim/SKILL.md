---
name: objection-to-proof-of-claim
title: Objection to Proof of Claim
description: Drafts Objections to Proof of Claim for U.S. bankruptcy courts under 11 U.S.C. § 502. Extracts case facts, identifies evidentiary deficiencies, and articulates grounds for disallowance or reduction. Use when a debtor, trustee, or party in interest challenges a creditor's proof of claim, claim classification, or insufficient documentation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/objection-to-proof-of-claim
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: bankruptcy
language: en
tags: [drafting, litigation, motion]
---

# Objection to Proof of Claim

Draft a litigation-ready objection challenging a creditor's proof of claim in U.S. bankruptcy court, targeting disallowance or reduction under 11 U.S.C. § 502.

## Prerequisites

Collect before drafting:

1. **Bankruptcy petition** — debtor name, case number, chapter, petition date
2. **Proof of claim (POC)** — claim number, filing date, creditor name, amount, stated basis, attachments
3. **Underlying documents** — contracts, invoices, payment history, correspondence
4. **Schedules and SOFA** — debtor's characterization and any discrepancies with POC
5. **Local rules** — formatting, page limits, verification requirements
6. **Bar date order** — claims deadline and timeliness of filing

## Output Structure

### 1. Caption

Format per local rules. Include: court name with district, case number, debtor name (as on petition), chapter, and centered title "OBJECTION TO PROOF OF CLAIM NO. [X]".

### 2. Introduction

- State objector's standing under § 502(a) (debtor, trustee, or party in interest)
- Identify claim number, creditor name, and asserted amount
- Preview objection grounds in one to two sentences — do not argue

### 3. Factual Background

Chronological narrative covering:

- Origin of alleged debt (contract, date, terms)
- Pre-petition payment history and disputes
- Petition date, bar date, and POC filing date relative to bar date
- Discrepancies between schedules and POC
- Documentation attached or missing from POC

Present facts neutrally. Distinguish disputed from undisputed. Every assertion must trace to a producible source document.

### 4. Grounds for Objection

Identify all applicable grounds:

| Ground | Authority | Showing Required |
|---|---|---|
| Insufficient documentation | FRBP 3001(f); § 502(b) | Missing contracts, invoices, or statements |
| Calculation errors | § 502(b)(1) | Incorrect interest, unauthorized fees, principal errors |
| Statute of limitations | § 502(b)(1) + state law | Claim accrued outside limitations period |
| Improper priority | § 503(b), § 507(a)(8), § 506 | Fails statutory priority requirements |
| Improper secured status | § 506(a) | No valid, perfected security interest |
| Lack of standing | § 502(a) | Not real party in interest; deficient assignment chain |
| Duplicative claim | § 502(b)(1) | Duplicates another filed claim |
| Post-petition debt | § 502(b) | Arose post-petition without administrative expense basis |

For each ground: cite statute/rule, state the legal standard, apply facts showing how claim fails.

### 5. Legal Argument

For each argument:

1. State governing standard (statute + controlling case law)
2. Apply burden framework — FRBP 3001(f) prima facie validity shifts to creditor on colorable challenge
3. Connect specific facts to legal standard
4. Anticipate creditor counterarguments

Cite controlling Circuit and BAP authority. Bluebook format with pinpoint cites. Mark unverified citations with [VERIFY].

### 6. Prayer for Relief

In order of preference:

1. Disallow claim in entirety
2. Reduce to $[amount] with basis
3. Reclassify from [current] to [requested] status (if applicable)
4. Fees/costs if statutory or contractual basis exists (cite authority)
5. General relief clause

### 7. Signature Block

Per FRBP 9011: name, bar number, firm, address, phone, email. Include verification under penalty of perjury if required by local rules.

## Checks

- **Tone**: Professional, measured — no inflammatory language
- **Format**: 12pt serif, double-spaced body, single-spaced caption/signature/block quotes, 1-inch margins, page numbers, case footer
- **Citations**: Bluebook with pinpoint cites throughout
- **Evidence**: Every fact must be traceable to an admissible source document
- **Fresh start**: For individual debtors, frame within bankruptcy's rehabilitative purpose where applicable
- **Never** assume secured status, priority, or standing — require creditor to prove each element
- **Never** concede facts favorable to the objector when characterizing disputed matters
