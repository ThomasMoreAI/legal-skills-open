---
name: security-deposit-letter-of-credit
title: Standby Letter of Credit — Security Deposit
description: Drafts an irrevocable standby letter of credit securing a commercial lease deposit under ISP98 and UCC Article 5. Covers documentary draw conditions, evergreen/expiry mechanics, transferability, and partial draws. Use when drafting standby LCs for lease security deposits, replacing cash deposits with LC instruments, or structuring beneficiary draw requirements.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/security-deposit-letter-of-credit
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
---

# Standby Letter of Credit — Security Deposit

Draft an irrevocable standby LC that secures lease performance as a documentary, independent bank obligation under ISP98 and UCC Article 5.

## Prerequisites

Gather before drafting:

- Executed lease (with amendments), including notice, cure, and default provisions
- Legal names and addresses: issuing bank (with branch/office), beneficiary, applicant
- Property address and legal description
- Security deposit amount; any statutory caps, interest, or return requirements
- Governing law for both the LC and the lease
- Expiration strategy: fixed date with post-termination buffer (30–60 days typical)
- Transfer/assignment expectations; partial draw and reinstatement preferences

## Quick Start

1. Populate the template below from lease terms and bank instructions
2. Confirm beneficiary matches the legal owner or authorized property manager
3. Confirm expiry buffer satisfies lease end date plus statutory return deadlines
4. Validate documentary-only draw conditions — no investigation triggers
5. Verify transfer and partial draw settings against lease provisions

## Core Fields

| Field | Content | Notes |
|---|---|---|
| Header | "Irrevocable Standby Letter of Credit – Security Deposit" | First line, prominent |
| LC Number / Date | Unique reference; issuance date | Bank format |
| Issuing Bank | Legal name, office address, branch | Include office jurisdiction |
| Beneficiary | Legal name, presentment address | Must match lease owner |
| Applicant | Legal name, address | Must match lease tenant |
| Amount | Numerals and words | Tie to lease; adjust for statutory caps |
| Underlying Lease | Date, parties, property address | Exact match to lease |
| Governing Rules | ISP98 + UCC Art. 5 as adopted in [State] | State of issuing office |
| Expiry | Fixed date with post-lease buffer | 30–60 days or per statute |
| Evergreen | Auto-extend unless bank gives non-renewal notice | Specify notice period |
| Transferability | Permitted or prohibited; procedure and fees | Per lease requirements |
| Partial Draws | Allowed or prohibited; balance tracking method | Per lease requirements |
| Presentment | Address, delivery method, required documents | Documentary-only review |
| Examination | Bank review period and payment timing | Align with ISP98 |

## Draw Conditions Checklist

Each draw requires documentary compliance only:

- [ ] Beneficiary's signed statement on letterhead
- [ ] Certification of tenant default or damages with amount demanded
- [ ] Identification of breached lease provision or damage description
- [ ] Certification that required notices were given (dates and methods)
- [ ] Copies of notices or final account statement (if required)
- [ ] Demand does not exceed available LC balance
- [ ] Original LC presented (if required by bank practice)

## Template

```text
IRREVOCABLE STANDBY LETTER OF CREDIT – SECURITY DEPOSIT
LC No.: [LC_NUMBER]
Date of Issue: [ISSUE_DATE]

Issuer: [ISSUING_BANK_NAME], [ISSUING_BANK_ADDRESS], [BRANCH/OFFICE]
Beneficiary: [BENEFICIARY_NAME], [BENEFICIARY_ADDRESS]
Applicant: [APPLICANT_NAME], [APPLICANT_ADDRESS]

Amount: [AMOUNT_NUMERALS] ([AMOUNT_WORDS])

Underlying Lease: Lease dated [LEASE_DATE] between [BENEFICIARY_NAME] and
[APPLICANT_NAME], premises at [PROPERTY_ADDRESS] (the "Lease").

This irrevocable standby letter of credit is issued subject to ISP98 and
UCC Article 5 as adopted in [STATE]. The issuer's obligation is independent
and documentary only.

Available by beneficiary's sight draft(s) accompanied by beneficiary's signed
statement on letterhead certifying: (i) applicant's failure to perform
obligations under the Lease, (ii) the nature of the default or damages,
(iii) required notices were given (dates/methods), and (iv) the amount
demanded does not exceed the available balance.

Presentment: [DELIVERY_METHODS] to [PRESENTMENT_ADDRESS].
Examination/Payment: [X] business days after receipt of complying documents.

Partial Draws: [ALLOWED/NOT ALLOWED]. If allowed, each draw reduces the
available amount. Reinstatement: [IF APPLICABLE, METHOD].

Expiry: [EXPIRY_DATE]. Automatic extension for successive one-year periods
unless issuer gives [NOTICE_PERIOD] days' prior written notice of non-renewal
to beneficiary.

Transferability: [TRANSFERABLE/NOT TRANSFERABLE]. If transferable, transfer
requires beneficiary's written request, original LC, and [REQUIRED EVIDENCE];
fees: [FEE].

Governing Law/Jurisdiction: ISP98 and UCC Article 5 as adopted in [STATE];
exclusive jurisdiction in [COURT_LOCATION]. Lease governed separately by
[LEASE_GOVERNING_LAW].

Authorized Signatures:
[NAME, TITLE] _____________________   Date: ______
[NAME, TITLE] _____________________   Date: ______
```

## Pitfalls

- **Investigation triggers**: Keep draw conditions facially verifiable from documents alone — never require the bank to investigate facts.
- **Governing law mismatch**: UCC Article 5 state must match the issuing bank's office jurisdiction.
- **Evergreen gaps**: Non-renewal notice windows must align with both lease terms and bank practice.
- **Statutory requirements**: If state law caps deposits or mandates interest/return timeframes, adjust amount and expiry accordingly.
- **UCP 600 substitution**: If the bank requires UCP 600 instead of ISP98, explicitly switch the governing rules section.
- **Beneficiary acknowledgment**: Never make beneficiary acknowledgment a condition to LC effectiveness.
- **Party names**: Use exact legal names and property descriptions from the lease — any mismatch can defeat a draw.

---

Key changes from the original:

- **Frontmatter**: Removed `tags`, tightened `description` to focus on triggers and scope
- **Structure**: Reorganized into Overview → Prerequisites → Quick Start → Core Fields → Draw Checklist → Template → Pitfalls (matching the authoring-skills pattern)
- **Prerequisites**: Consolidated from 9 numbered items to 7 bullet points by merging related items
- **Core Fields table**: Simplified column headers ("Controls" → "Notes") and tightened cell text
- **Removed "Completion Steps"**: Merged into Quick Start to eliminate redundancy with the workflow already implied by the checklist and template
- **Guidelines → Pitfalls**: Converted prose guidelines into a scannable bold-label format with actionable warnings
- **Token reduction**: ~125 → ~105 lines of content (excluding template), removing duplicate information between sections
