---
name: tax-clearance-request
title: Request for Tax Clearance Certificate
description: Drafts formal request letters for Tax Clearance Certificates from state tax authorities on behalf of corporate entities. Triggers on tax clearance requests, pre-dissolution tax letters, business sale tax certification, merger tax compliance, asset transfer clearance, or license renewal tax documentation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/tax-clearance-request
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: tax
language: en
tags: [corporate, drafting, letter, regulatory]
---

# Request for Tax Clearance Certificate

Draft a submission-ready letter requesting a Tax Clearance Certificate from the appropriate state tax authority, confirming all corporate tax obligations are satisfied.

## Required Inputs

1. **Formation documents** — Articles/Certificate with exact legal name as registered with SOS
2. **Tax IDs** — FEIN and all state tax account numbers (income, sales/use, withholding, unemployment)
3. **Filed returns** — all periods within clearance scope, with filing confirmations
4. **Payment records** — EFT confirmations, cancelled checks, or bank statements for all remittances
5. **Transaction documents** — purchase agreement, merger docs, dissolution resolution, or license renewal notice (establishes purpose and deadline)
6. **Prior correspondence** — existing clearances, audits, assessments, payment plans

## Workflow

1. **Collect and verify** — Gather all inputs above; flag any gaps to the user before drafting
2. **Confirm jurisdiction requirements** — Some states mandate official forms (not letters), notarization, or corporate seal; verify before proceeding
3. **Identify clearance type** — Tax clearance certificate vs. certificate of good standing are distinct; confirm which is needed
4. **Draft letter** — Follow the output structure and template below
5. **Cross-reference** — Validate legal name against SOS records; verify all tax IDs against source documents
6. **Proactive disclosures** — Surface pending audits, disputed assessments, payment plans, or recent large payments (within 30 days) with confirmation numbers

## Output Structure

Formal business letter on corporate letterhead. 1–2 pages. Single-spaced, double between paragraphs.

### Required Sections

| Section | Content |
|---|---|
| **Header** | Letterhead (legal name, address, phone, email), date, recipient agency clearance division |
| **Subject Line** | "Request for Tax Clearance Certificate — [Entity Legal Name] — [Primary Tax ID]" |
| **Purpose Statement** | What is requested, by whom, why (transaction type + closing date or statutory basis) |
| **Entity Identification** | Legal name (per SOS), FEIN, state tax IDs by category, addresses, formation date, prior names with effective dates |
| **Tax Account Inventory** | All accounts by type (income, sales/use, withholding, unemployment, excise, special). Note closed/transferred accounts with dates |
| **Clearance Scope** | Comprehensive vs. limited; tax types covered; time period; validity period needed |
| **Timeline & Expediting** | Transaction deadline; expedited request if needed; willingness to pay expedited fees |
| **Enclosures** | Numbered list: filed returns, payment proofs, formation docs, good standing certificate, prior clearances, assessment correspondence |
| **Proactive Disclosures** | Pending audits, disputed assessments, payment plans, recent large payments (dates, amounts, confirmation numbers) |
| **Closing & Contact** | Primary contact (name, title, phone, email); counsel/CPA contact with authorization scope; authorized officer signature block |

### Template

```
[ENTITY LETTERHEAD]

[Date]

[State Tax Authority]
[Clearance Division]
[Address]

Re: Request for Tax Clearance Certificate
    [Entity Legal Name] | FEIN: [XX-XXXXXXX] | State Tax ID: [XXXXXXX]

Dear [Title/Division]:

[Entity Legal Name] ("Company") respectfully requests issuance of a Tax
Clearance Certificate confirming that all state tax obligations have been
satisfied. This clearance is required in connection with [transaction type],
with an anticipated completion date of [date].

ENTITY INFORMATION
  Legal Name:        [as registered with Secretary of State]
  FEIN:              [XX-XXXXXXX]
  State Tax IDs:     [list by category]
  Principal Address: [address]
  Formation Date:    [date]
  Prior Names:       [if any, with effective dates]

TAX ACCOUNTS
  [Category]         [Account Number]    [Status]
  ...

SCOPE OF REQUEST
  Tax Types:    [All / specific categories]
  Period:       [Start date] through [end date]
  Validity:     Certificate valid through [date] requested

[If expedited: The Company requests expedited processing to accommodate
the [date] transaction deadline and will remit any applicable expedited
processing fees upon invoice.]

[Proactive disclosures paragraph if applicable]

The following documents are enclosed in support of this request:
  1. [Document list]
  ...

Please direct any questions to [contact name], [title], at [phone] or
[email]. [If represented: [Firm/CPA name] is authorized to communicate
with your office regarding this request; contact [name] at [phone/email].]

Thank you for your prompt attention to this matter.

Respectfully,

[Name]
[Title]
[Entity Legal Name]

Enclosures: [count]
```

## Pitfalls and Checks

- **Legal name mismatch** — Mismatches against SOS records cause automatic rejection
- **Never estimate tax IDs** — Cross-reference every account number against source documents
- **Multi-state nexus** — Flag if clearances are needed from multiple jurisdictions
- **Multi-agency clearance** — Some states require separate Department of Labor clearance (unemployment/workers' comp) in addition to tax authority
- **Recent payments** — Payments within 30 days may not have posted; request posting verification before clearance determination
- **Validity windows** — Typically 30/60/90 days; ensure certificate remains valid through closing
- **Processing times** — Range from days to weeks by jurisdiction; factor into transaction timeline
- **FRE 408 inapplicable** — This is administrative correspondence, not settlement negotiation
- **Missing information** — If critical data is unavailable, identify gaps explicitly and request from user before finalizing

---
