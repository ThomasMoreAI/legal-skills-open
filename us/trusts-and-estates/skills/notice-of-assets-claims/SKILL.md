---
name: notice-of-assets-claims
title: Notice of Assets and Request for Claims
description: Drafts a Notice of Assets and Request for Claims for probate estates. Triggers when administering an estate, publishing creditor notice, filing a probate notice of assets, or establishing claim bar dates. Handles jurisdictional research, asset disclosure, claim filing procedures, and execution requirements under state-specific probate codes.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/notice-of-assets-claims
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: trusts-and-estates
language: en
tags: [drafting, letter, litigation]
---

# Notice of Assets and Request for Claims

Produces a probate notice that notifies creditors of a decedent's estate and establishes the legal framework for claim submission under applicable state law.

## Required Inputs

1. **Decedent** — full legal name, aliases, DOD, DOB, last residence
2. **Personal representative** — name, relationship, appointment date, independent administration authority (Y/N)
3. **Court** — case number, county, state, court address with department/division
4. **Counsel** — attorney name, bar number, firm, address, phone, email
5. **Jurisdiction's probate code** — research state-specific notice requirements before drafting

## Quick Start

1. Collect all required inputs; flag missing items with `[TO BE PROVIDED]`.
2. Complete jurisdictional research checklist below.
3. Draft notice following the output structure.
4. Verify all deadlines, statutory citations, and publication requirements.
5. Deliver document ready for immediate filing and publication.

## Jurisdictional Research Checklist

Verify for the applicable state before drafting:

| Item | Confirm |
|---|---|
| Deadline trigger | First publication, mailing, or date of death? |
| Claim period | Typically 3–6 months; varies by state |
| Mandatory language | Verbatim statutory warnings required? |
| Asset disclosure | Category-level vs. itemized; estimated value required? |
| Publication | Newspaper of general circulation, legal journal, frequency, consecutive weeks |
| Service methods | Personal delivery, certified mail, other |
| Claim form | Court-provided form or freeform? |
| Notarization | Required for publication or filing? |

## Output Structure

### 1. Header

- Title: **NOTICE OF ASSETS AND REQUEST FOR CLAIMS**
- Court jurisdiction (county, state), case number, date of issuance
- Format per local court rules

### 2. Identification Block

Include: decedent name/aliases, DOD, last residence, personal representative name/title/appointment date, administration type, counsel with bar number and contact info.

### 3. Asset Disclosure

- Describe assets **by category only** — do not itemize:
  - Real property, financial accounts, personal property, potential claims/intangible assets
- If estimated value required, qualify as preliminary and subject to revision
- Include language that additional assets may be discovered

### 4. Claim Requirements and Deadline

| Element | Content |
|---|---|
| **Deadline** | Calendar date AND descriptive period (e.g., "within four months from first publication, i.e., [Date]") |
| **Bar language** | Untimely claims are **barred forever** regardless of validity or lack of actual knowledge |
| **Scope** | Applies to contract, tort, statutory, and all other claims unless specifically exempted |
| **Claim contents** | Written; state basis and amount; attach documentation; signed under penalty of perjury |
| **Identifiers** | Reference decedent's name and estate case number |
| **Special claims** | Address contingent, unliquidated, and pending-litigation claims with modified procedures |

### 5. Filing and Service Instructions

1. **File** with court at stated address/department
2. **Serve** copy on personal representative or counsel
3. State **acceptable service methods** per jurisdiction
4. Identify where to obtain **claim forms** if required
5. Note: Filing alone is **insufficient** — service on the representative is also required

### 6. Execution Block

Include perjury declaration with signature line for personal representative. If jurisdiction requires notarization, append a notary block with state/county, signature, commission number, and expiration.

## Formatting

- 12-point serif font, 1-inch margins, line spacing per local rules
- Clear section headings; formal but accessible tone

## Pitfalls and Checks

- **Deadline precision is critical** — errors in the bar date can invalidate the notice and expose the estate to liability
- **Do not over-disclose assets** — category descriptions satisfy requirements without compromising negotiating position
- **Verify statutory citations** against current code; mark uncertain references with `[VERIFY]`
- **Due process** — notice must be prominent and unambiguous enough to withstand constitutional challenge
- **Never fabricate details** — flag missing information with `[TO BE PROVIDED]`

---

**Key changes made:**

- **Description** rewritten in third-person with explicit trigger guidance
- **Prerequisites** renamed to **Required Inputs** for clarity
- Added **Quick Start** section for at-a-glance workflow
- **Jurisdictional Research Checklist** trimmed (removed filing fees row — low-value; consolidated wording)
- **Identification Block** and **Execution Block** collapsed from verbose code-fence templates to concise prose directives — the agent generates the actual content, so spelling out every placeholder line wastes tokens
- **Formatting Requirements** and **Guidelines** consolidated into tighter **Formatting** and **Pitfalls and Checks** sections
- Removed redundant prose throughout while preserving all legally critical instructions
