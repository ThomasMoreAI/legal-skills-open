---
name: complaint-breach-of-contract
title: Complaint for Breach of Contract
description: Drafts a U.S. plaintiff-side breach of contract complaint with caption, jurisdiction/venue, four-element cause of action, and prayer for relief. Trigger when user needs to draft a breach of contract complaint for state or federal court filing.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/complaint-breach-of-contract
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [drafting, pleading]
---

# Complaint for Breach of Contract

Generates a litigation-ready plaintiff-side complaint structured around the four breach-of-contract elements with jurisdiction-appropriate procedural compliance.

## Prerequisites

Collect before drafting:

1. **Governing contract** — executed agreement with amendments, exhibits, attachments
2. **Correspondence** — emails, letters, cure/notice communications (chronological)
3. **Performance evidence** — invoices, delivery records, payment confirmations
4. **Breach evidence** — documentation of defendant's failure, cure notices, responses
5. **Damage calculation** — itemized losses with supporting documentation
6. **Filing court** — jurisdiction, division, and applicable local rules

## Quick Start

1. Identify filing court and confirm jurisdiction (federal diversity/question vs. state general)
2. Extract party details, contract terms, and breach facts from uploaded documents
3. Draft complaint sections in order: caption, jurisdiction/venue, parties, facts, cause of action, relief
4. Verify procedural requirements (jury demand, verification, Rule 11) against local rules

## Complaint Sections

### 1. Caption

- Full court name with division/department
- Case number (if pre-assigned)
- Complete legal names and capacities of all parties
- Jurisdiction-specific formatting per local rules

### 2. Jurisdiction & Venue

| Element | Federal | State |
|---|---|---|
| Subject matter | Diversity: 28 U.S.C. § 1332 (complete diversity + AIC > $75K) or federal question: § 1331 | Statutory/constitutional general jurisdiction |
| Venue | 28 U.S.C. § 1391: defendant residence, contract performance, or breach location | Defendant residence, place of business, or performance/breach location |

State amount in controversy when jurisdictionally required.

### 3. Party Identification

- **Individuals**: legal name, address, contractual role
- **Entities**: legal form, state of organization, principal place of business, registered agent
- **Representative parties**: capacity and source of authority

### 4. Factual Background

Chronological narrative covering:

- **Formation** — date, place, consideration, essential terms
- **Plaintiff's performance** — dates, amounts, deliverables
- **Defendant's breach** — obligations unperformed, breach date, cure notice status
- **Defendant's response** — acknowledgment, dispute, or silence
- **Resulting harm** — causal link from breach to damages

Ground all allegations in uploaded documents with specific dates, amounts, and quoted contract language.

### 5. Cause of Action

Allege each element with dedicated factual paragraphs:

1. **Valid enforceable contract** — parties, subject matter, consideration, mutual assent; address statute of frauds if applicable
2. **Plaintiff's performance** — conditions precedent satisfied or excused/waived
3. **Defendant's material breach** — provisions violated, manner, date
4. **Resulting damages** — causal link to quantified harm

Incorporate contract-specific provisions: notice requirements, cure periods, liquidated damages, attorney's fees clauses. [VERIFY jurisdiction-specific element variations beyond standard four elements]

### 6. Prayer for Relief

- Compensatory damages (itemized where calculable)
- Consequential/special damages (allege foreseeability at contracting)
- Specific performance or injunctive relief (where legally available)
- Pre-judgment and post-judgment interest (cite applicable rate/statute)
- Costs of suit
- Attorney's fees (if contract or statute authorizes)
- Punitive damages (only if jurisdiction permits and facts support bad faith)
- General relief catch-all

### 7. Procedural Requirements

- **Jury demand** — include in body or file separately per local rules
- **Rule 11 certification** — good faith factual and legal basis for all allegations
- **Verification** — sworn verification if required by state court
- **Signature block** — attorney name, bar number, firm, address, phone, email

## Pitfalls & Checks

- Number all paragraphs consecutively for cross-reference in motions
- Keep factual, objective tone — no inflammatory language; reserve argument for briefs
- Ensure factual narrative preemptively addresses likely affirmative defenses: statute of frauds, waiver, impossibility, accord and satisfaction
- All allegations must be supportable by documents in counsel's possession at filing
- Verify local rules for page limits, margins, font, and spacing before finalizing
