---
name: adversary-proceeding-complaint
title: Adversary Proceeding Complaint
description: Drafts adversary proceeding complaints for U.S. Bankruptcy Court under FRBP Rule 7001. Covers dischargeability disputes (§ 523), preference actions (§ 547), fraudulent transfers (§ 548), and stay violations (§ 362). Produces a filing-ready pleading with caption, jurisdictional basis, numbered allegations, count structure, and prayer for relief. Triggers when a trustee, creditor, or party in interest needs to initiate litigation within an existing bankruptcy case.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/adversary-proceeding-complaint
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: bankruptcy
language: en
tags: [litigation, pleading, drafting]
---

# Adversary Proceeding Complaint

Drafts a filing-ready complaint initiating an adversary proceeding under FRBP Rule 7001.

## Prerequisites

Gather before drafting:

1. **Case info** — court, district/division, case number, chapter, debtor name as filed
2. **Parties** — plaintiff name and capacity (trustee, creditor, etc.); defendant name, address, relationship to estate
3. **Facts** — chronology of events, transactions, transfers with dates, amounts, and documentary evidence
4. **Claim types** — Rule 7001 category and substantive statutory basis
5. **Relief sought** — specific dollar amounts, determinations, or remedies

## Quick Start

1. Collect all prerequisites; flag gaps with `[CONFIRM WITH CLIENT]`
2. Build the caption from the main bankruptcy case
3. Draft jurisdiction and venue paragraphs with statutory citations
4. Write numbered factual allegations in chronological order
5. Structure each count around every required statutory element
6. Draft prayer for relief with specific amounts per count
7. Append signature block and certificate of service

## Document Structure

### Caption

| Element | Format |
|---------|--------|
| Court | UNITED STATES BANKRUPTCY COURT, [DISTRICT], [DIVISION] |
| In re | Debtor name exactly as in main case |
| Case No. | Main bankruptcy case number |
| Adversary No. | If assigned; otherwise blank for clerk |
| Parties | Plaintiff v. Defendant with capacity designations |

### Introductory Paragraph

State the complaint is filed under FRBP 7001, identify the applicable subsection, and provide a one-sentence summary of the dispute and primary relief.

### Jurisdiction and Venue

Cite each basis:

- **Subject matter** — 28 U.S.C. § 1334
- **Reference** — 28 U.S.C. § 157
- **Core/non-core** — 28 U.S.C. § 157(b)(2) with specific subsection
- **Personal jurisdiction** — basis over defendant
- **Venue** — basis in this district

### Parties

Numbered paragraphs for each party stating relationship to estate, standing basis, identifying information, and address.

### Factual Allegations

Numbered paragraphs in chronological order covering: bankruptcy filing date and procedural history, party relationships, each distinct event or transaction in its own paragraph, and specific dates, dollar amounts, and document references.

### Claim-Specific Allegations

Tailor factual detail to the claim type:

| Claim | Statute | Key Allegations |
|-------|---------|-----------------|
| Dischargeability | § 523(a)(2), (4), or (6) | Transactions, representations, fraudulent conduct, willful/malicious injury |
| Preference | § 547 | Each transfer with date, amount, antecedent debt, timing relative to petition |
| Fraudulent transfer | § 548 / state law | Transfer details, consideration, actual or constructive fraud badges |
| Stay violation | § 362 | Post-petition acts, knowledge of filing, damages |

### Counts

Each count in a separate section titled COUNT [N] — [DESCRIPTIVE TITLE WITH STATUTORY CITE]. Begin with an incorporation paragraph referencing prior allegations, then address every statutory element with supporting factual references.

### Prayer for Relief

- Specific judgment per count (e.g., determining debt nondischargeable in the amount of $_____)
- Avoidance and recovery of transfers with values
- Actual and punitive damages for stay violations where applicable
- Costs and attorneys' fees where statutorily authorized
- Catch-all: "Such other and further relief as the Court deems just and proper"

### Signature Block

Attorney signature with bar number, firm, address, phone, and email. Append certificate of service.

## Drafting Rules

- Number all factual allegations — one fact per paragraph
- Plead facts meeting *Twombly*/*Iqbal* plausibility, not legal conclusions
- Maintain consistent defined terms and party designations throughout
- Cite statutes in Bluebook format
- Maintain neutral pleading tone — no argumentative language
- Flag assumed facts with `[CONFIRM WITH CLIENT]`

## Claim-Specific Checks

- **§ 523 dischargeability** — burden is preponderance of evidence; clear and convincing for § 523(a)(2)
- **§ 547 preferences** — look-back is 90 days general, 1 year for insiders
- **§ 548 fraudulent transfers** — 2-year reach-back from petition date; state law may extend further
- **Local rules** — verify formatting requirements (margins, font, ECF conventions) for the specific court

## Troubleshooting

- **Missing adversary number** — leave blank; the clerk assigns it at filing
- **Multiple claim types** — draft each as a separate count with its own element-by-element allegations
- **State-law fraudulent transfer claims** — confirm applicable state statute and limitations period; do not assume § 548 reach-back applies
- **Insider status unclear** — flag with `[CONFIRM WITH CLIENT]` as it affects the § 547 look-back period

---

Key changes from the original:

- **Description**: Rewritten in third person with parenthetical statute references for trigger keywords; trimmed to stay well under 1024 chars
- **Tags**: Kept to the controlled vocabulary (`litigation`, `pleading`, `drafting`)
- **Added Quick Start**: 7-step workflow overview for fast orientation
- **Collapsed verbose sections**: Merged "Factual Background" and "Claim-Specific Factual Allegations" into tighter sections; condensed the Counts section from a code-fenced template to prose guidance
- **Separated concerns**: Split the monolithic "Guidelines" into "Drafting Rules" (always-apply) and "Claim-Specific Checks" (conditional)
- **Added Troubleshooting**: Required by the spec; covers the most common filing edge cases
- **Removed code fences**: Per your requirements
- **Line count**: ~100 lines (well under the 500-line limit)
