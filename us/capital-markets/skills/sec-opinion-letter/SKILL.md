---
name: sec-opinion-letter
title: Opinion of Counsel for SEC Filing
description: Drafts Opinion of Counsel letters for SEC registration statements, covering due incorporation, valid issuance, fully-paid and non-assessable opinions, and Reg S-K Item 601(b)(5) consent language. Use when drafting Exhibit 5.1 opinions for S-1/S-3 filings, shelf offerings, or securities issuance transactions.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/sec-opinion-letter
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: capital-markets
language: en
tags: [corporate, regulatory, letter, drafting]
---

# Opinion of Counsel for SEC Filing

Drafts a formal legal opinion letter for an SEC registration statement, providing counsel's assurances on corporate status, authorization, and securities validity per ABA Legal Opinion Accord standards.

## Prerequisites

1. **Charter documents** — Articles/Certificate of Incorporation (all amendments), current bylaws
2. **Board resolutions** — Minutes or written consents authorizing issuance
3. **Stockholder approvals** — If required by statute or charter
4. **Registration statement** — Draft or filed Form S-1, S-3, or applicable form
5. **Capitalization records** — Stock ledger, cap table, outstanding shares by class/series
6. **Transaction agreements** — Underwriting, purchase, or placement agent agreement
7. **Good standing certificate** — From Secretary of State, dated within 5-10 days of opinion date
8. **Officer's certificate** — Factual representations from authorized officer

## Quick Start

1. Collect and review all prerequisite documents
2. Extract factual recitals (legal name, jurisdiction, capital structure, board actions)
3. Draft opinion letter following the document layout below
4. Verify all statutory citations with `[VERIFY]` flags for uncertain references
5. Include Item 601(b)(5) consent language and Section 7 disclaimer
6. Format for PDF exhibit filing as Exhibit 5.1

## Document Layout

| Section | Content |
|---|---|
| Letterhead | Firm name, address, contact |
| Date | Closing/filing date |
| Addressees | Company board, SEC, underwriters as applicable |
| Re: Line | `[Company] — Registration Statement on Form [S-1/S-3] for [X] Shares of [Class] Stock` |
| Engagement scope | Client, transaction, opinions requested |
| Documents examined | Principal documents reviewed |
| Assumptions | Customary assumptions per ABA Legal Opinion Accord |
| Factual recitation | Corporate status, capital structure, authorizing actions |
| Opinion paragraphs | Numbered conclusions |
| Qualifications | Governing law limits, enforceability carve-outs |
| Consent | Item 601(b)(5) filing consent with Section 7 disclaimer |
| Reliance/closing | Reliance limitations, no-update disclaimer, signature |

## Factual Recitation Checklist

Extract and state with precision:

- [ ] Exact legal name per charter
- [ ] Jurisdiction and date of incorporation
- [ ] Full capital structure (authorized shares by class/series, par values)
- [ ] Outstanding shares as of record date
- [ ] Reserved shares (options, warrants, convertibles)
- [ ] Securities subject to opinion (number, class, par value)
- [ ] Board action (date, quorum confirmed, resolutions adopted)
- [ ] Stockholder action if required (date, vote tally, threshold met)
- [ ] Notice and quorum compliance for all meetings

## Opinion Paragraphs

Number sequentially using "we are of the opinion that" — never "we believe" or "it is our view."

| # | Opinion | Statutory Basis |
|---|---|---|
| 1 | Duly incorporated, validly existing, and in good standing under laws of [State] | DGCL §§ 101-102 (if DE) `[VERIFY]` |
| 2 | Corporate power and authority to execute [Agreement] and issue Shares | DGCL § 141 |
| 3 | Issuance duly authorized by all necessary corporate action | DGCL §§ 141, 151, 242 |
| 4 | Shares, when issued against payment per [Agreement], will be **validly issued, fully paid, and non-assessable** | DGCL §§ 152, 153, 154 |
| 5 | *(If applicable)* Registration Statement facially responsive to Securities Act — **no opinion on disclosure accuracy** | Securities Act §§ 5, 7, 10; Reg S-K |

Condition the validity opinion on receipt of consideration as specified in the Agreement.

## Assumptions Block

Include all customary assumptions:

- Genuineness of signatures; authenticity of originals; conformity of copies
- Legal capacity of natural persons
- Due authorization/execution/delivery by parties other than client
- Accuracy and completeness of corporate records and officer certificates
- Absence of fraud, collusion, or mutual mistake

## Required Consent Language

Include verbatim, filling bracketed fields:

> We hereby consent to the filing of this opinion as Exhibit [5.1] to the Registration Statement on Form [___] and to the reference to our firm under the caption "[Legal Matters]" in the Prospectus forming a part of the Registration Statement. In giving this consent, we do not thereby admit that we are within the category of persons whose consent is required under Section 7 of the Securities Act of 1933, as amended, or the rules and regulations of the Securities and Exchange Commission promulgated thereunder.

## Required Closing Language

Include verbatim:

> This opinion speaks only as of the date hereof. We assume no obligation to update, revise, or supplement this opinion to reflect any facts or circumstances that may hereafter come to our attention or any changes in law that may hereafter occur. This opinion is rendered solely for the benefit of the addressees in connection with the transaction described herein and may not be relied upon by any other person or for any other purpose without our prior written consent.

## Pitfalls and Checks

- **Scope exclusions**: Explicitly exclude tax, IP, foreign law, and industry-specific regulatory opinions unless specifically engaged
- **Governing law limits**: State opinions cover only statutory law and published decisions of the incorporation state; federal opinions cover Securities Act, Exchange Act, and published SEC rules
- **Enforceability carve-out**: Always qualify for bankruptcy, insolvency, fraudulent transfer, reorganization, moratorium, and general equitable principles
- **Non-assessable caveat**: Condition on receipt of consideration ≥ par value
- **Preemptive rights**: Confirm charter waiver or statutory inapplicability; note contractual preemptive rights not reviewed
- **Shelf registrations (S-3)**: Address whether bring-down opinions or supplements are needed for future takedowns
- **Citation verification**: Confirm all statutory sections are current; use `[VERIFY]` for uncertain citations
- **Privileged content**: Do not disclose privileged communications or competitively sensitive information

---

**Key changes from the original:**

- **Description**: Trimmed from 300+ chars of dense listing to a focused sentence with clear trigger guidance
- **Tags**: Removed `analysis`, `research` (not primary modes); kept `corporate`, `regulatory`, `letter`, `drafting`
- **Added Quick Start**: 6-step workflow summary for fast orientation
- **Removed redundant subsections**: Collapsed "Documents Examined Section" (was just a template list duplicating Prerequisites), removed standalone "Reliance and Closing" code block section
- **Consent/Closing language**: Converted from code blocks to blockquotes — more readable, still marked as verbatim
- **Renamed "Guidelines" to "Pitfalls and Checks"**: Aligns with skill spec patterns, tightened wording
- **Removed "Filing format" guideline**: Already covered in Quick Start step 6
- **Removed "ABA standards" guideline**: Already stated in the overview paragraph
- **Line count**: Reduced from 137 to 107 lines (~22% reduction) while preserving all legally material content
