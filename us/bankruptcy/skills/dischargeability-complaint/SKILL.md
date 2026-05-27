---
name: dischargeability-complaint
title: Dischargeability Complaint
description: Drafts a U.S. bankruptcy adversary complaint under 11 U.S.C. §523 to determine non-dischargeability of debt. Use when a creditor, assignee, or subrogee needs a complaint for Bankruptcy Court with §523 theories (fraud, fiduciary defalcation, willful/malicious injury). Trigger when inputs include debtor case data, petition/§341 dates, transaction facts, and target §523 subsections.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/dischargeability-complaint
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: bankruptcy
language: en
tags: [drafting, litigation, pleading]
---

# Dischargeability Complaint

Drafts a court-ready adversary complaint under 11 U.S.C. §523 for U.S. bankruptcy proceedings, with jurisdiction/venue allegations, evidence-anchored counts, and FRBP compliance.

## Quick Start

Collect before drafting:

- **Standing**: Plaintiff's enforcement right (original creditor, assignee, successor, subrogee)
- **Case data**: Court, case number, chapter, petition date, first §341 date, conversion status
- **Deadline posture**: FRBP 4007(c) timing — confirm filing window or extension basis
- **Evidence**: Contracts, account records, correspondence, payment history, admissions, fiduciary documents
- **§523 theories**: Map each subsection to its required elements under controlling circuit law
- **Damages**: Principal, contractual interest, statutory interest, fees, costs
- **Local rules**: Caption format, paragraph style, line numbering, font/margins, filing protocol

## Core Workflow

### 1. Build complaint scaffold

| Section | Content | Verify |
|---|---|---|
| Caption | Court name, bankruptcy case no., adversary caption, parties | District matches debtor case |
| Jurisdiction/Venue | 28 U.S.C. §§1334, 157(b)(2)(I), 1409; core proceeding | Explicitly alleged |
| Parties | Names, addresses, standing chain | Standing complete |
| Procedural posture | Petition date, §341 date, Rule 4007(c) timing | Within deadline or extension stated |
| Factual narrative | Chronological facts with dates and sources | Each allegation tied to exhibit |
| Counts | Per-theory allegations for each §523 subsection | All elements and remedies included |
| Prayer | Non-dischargeability, amount, interest, fees, costs | Amounts traceable to evidence |
| Verification | Perjury statement and signature block | Authorized signer confirmed |
| Service checklist | Filing-ready package | Complete |

### 2. Plead theory-specific elements

| Theory | Elements | Style |
|---|---|---|
| §523(a)(2)(A) | False representation, scienter, reliance, proximate causation, damages | Fact-dense: who/what/when/where/how |
| §523(a)(2)(B) | Materially untrue financial statement | Attach supporting financials, explain materiality |
| §523(a)(4) | Express fiduciary relationship, breach, fraud/defalcation | Distinguish express fiduciary duty from contractual/statutory |
| §523(a)(6) | Willful and malicious injury | Show intentional conduct + substantial certainty of harm |

### 3. Apply paragraph construction rules

- Number all paragraphs; keep short-to-medium length for readability.
- Fraud allegations must satisfy Rule 9(b): identify statement, communicator, medium, date, and falsity.
- Incorporate prior paragraphs by reference at each count's start.
- Use separate counts per theory — prevents collapse if one fails.
- Cross-reference facts; do not repeat full blocks.

### 4. Produce mandatory sections

1. Complaint heading and title
2. Jurisdiction and venue
3. Parties / standing
4. Factual background
5. Procedural timing
6. Count I: §523(a)(2)(A)
7. Count II: §523(a)(4) *(if applicable)*
8. Count III: §523(a)(6) *(if applicable)*
9. Prayer for relief
10. Verification
11. Signature block
12. Service/filing checklist

## Legal Constraints

- **FRBP 7001**: Adversary proceeding form governs structure.
- **FRBP 7009 / Rule 9(b)**: Heightened pleading for fraud allegations.
- **FRBP 7012 / Rule 12(b)(6)**: Frame for plausibility to resist dismissal.
- **FRCP 11**: Remove weak, conclusory, or unsupported allegations — sanctions exposure.

## Pitfalls and Checks

- Reconcile all damages figures against attached evidence.
- Confirm every element has at least one direct fact anchor.
- No allegation may rest on speculation — separate facts from legal inference.
- Do not mix circuit authority; use only jurisdiction-verified standards.
- Do not plead causes outside §523 scope.
- Keep tone objective — factual allegations only, no inflammatory language.
- Include `[VERIFY]` placeholders for unresolved legal standards or local-rule citations.
- Confirm attorney signature, bar status, and filing authorization before finalizing.
- Preserve exhibit organization and authentication trail.

---
