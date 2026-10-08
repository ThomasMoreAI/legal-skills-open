---
name: prompt-pack-engagement-letter-sboghossian
title: Engagement Letter
description: Use when drafting an engagement letter from a law firm to a client confirming the scope of representation, fee structure, billing practices, staffing, conflicts check status, and file retention policy. Applicable across MENA (UAE, KSA, LB, EG, DIFC, ADGM) and internationally. Engagement letters are mandatory risk management tools — they define the scope of representation and limit malpractice exposure. Trigger when a law firm is taking on a new client matter or when an existing engagement's scope changes significantly.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-engagement-letter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Engagement Letter

## When to use this

Use this skill when a law firm needs to prepare the engagement letter that governs the professional relationship with a new or existing client for a specific matter. An engagement letter is the law firm's primary risk management document: it defines the scope of representation, sets out the fee arrangement, and allocates responsibilities.

Engagement letters are mandatory under bar rules and professional conduct codes in most jurisdictions (UAE Bar Association, DIFC Practitioners Rules, SRA Code in the UK, ABA Model Rules in the US). Failure to issue one exposes the firm to fee disputes, scope disputes, and malpractice claims.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Law firm name | Issuing party | Ask |
| Client name and address | Addressee; party being represented | Ask |
| Matter description | Defines the scope of representation | Ask in detail |
| Fee structure (hourly, fixed, retainer, success fee) | The commercial terms of the engagement | Ask |
| Lead partner and team | Identifies who is responsible | Ask |
| Conflicts check status | Must be cleared before engagement | Ask; must be confirmed before sending |

## Optional inputs

- Estimated total fees or budget
- Billing currency and bank details for payment
- Upfront retainer amount
- Specific matters excluded from the engagement scope
- Client-specific billing guidelines (invoice formats, e-billing systems)
- Whether a formal retainer / power of attorney is required alongside the engagement letter

## Document structure

### 1. Header and date

- Law firm letterhead
- Date
- Client name and address
- Subject: "Engagement Letter — [Matter Description]"

### 2. Introduction and scope of representation

Define clearly what the firm is engaged to do:
- Specific matter: "You have asked us to represent you in connection with [describe matter precisely]"
- What is in scope: specific transactions, negotiations, court proceedings, regulatory filings
- What is explicitly out of scope: "This engagement does not cover [tax advice / employment matters / registration in other jurisdictions] unless separately agreed in writing."

The scope definition is the single most important risk management element. Ambiguity in scope creates claims that the firm was responsible for work it did not intend to cover.

### 3. Conflicts of interest

- Confirm that a conflicts check has been conducted and no material conflict was identified (or describe the conflict waiver procedure if applicable)
- Note any related party positions: "We act for [related party] on unrelated matters and have obtained the necessary consents."
- State ongoing obligation: if a conflict arises during the engagement, the firm will notify the client and take appropriate steps

### 4. Team and responsibility

- Supervising partner name and contact
- Other team members and their seniority
- Client's primary contact within the firm
- Note that the firm may use support staff, paralegals, or specialist counsel and their time will be billed (if applicable)

### 5. Fee structure

Specify the basis of fees with precision:

**Hourly rates**:
- Rates by seniority level: partner, senior associate, associate, paralegal
- Currency of billing
- Billing increments (typically 6 or 15 minutes)
- Rates are reviewed annually; current rates effective until [date]

**Fixed fee**:
- Amount for the entire engagement or specific deliverables
- What is included in the fixed fee
- Out-of-scope work will be billed additionally at hourly rates with prior written consent

**Retainer**:
- Monthly retainer amount
- What services are covered within the retainer (number of hours, categories of work)
- Work beyond the retainer scope billed additionally

**Success / conditional fee**:
- Base fee plus success uplift (if permitted under applicable bar rules)
- Definition of the success event
- Applicable in some MENA jurisdictions with limitations; not all bar regulations permit contingency fees — confirm

**MENA note**: Contingency fees are prohibited or restricted in several MENA jurisdictions. UAE Federal Decree-Law on the Legal Profession generally prohibits agreements to share in the outcome; DIFC Practitioners Rules are more flexible. Confirm applicable bar rules before including a success fee arrangement.

### 6. Disbursements and expenses

- Filing fees, court fees, notarization fees: billed at cost
- Travel (where applicable): economy class unless prior approval for business class
- Third-party expert fees (translators, process servers): pre-approved or billed at cost
- Internal photocopying, printing: note policy

### 7. Billing and payment

- Invoice frequency: monthly, per milestone, or at completion
- Payment terms: due within [30] days of invoice
- Consequences of late payment: interest at [rate] per month on overdue amounts; right to suspend work
- Upfront retainer: if requested, the amount and whether it is applied against final invoice or held as security
- Electronic billing / client billing system requirements (if applicable)

### 8. Client obligations

- Client to provide accurate and complete information promptly
- Client to give timely instructions when required
- Client to notify firm immediately of any change in instructions, contact details, or circumstances
- Client accepts responsibility for decisions made based on the firm's advice

### 9. Confidentiality and privilege

- All communications between the client and the firm are confidential and subject to legal professional privilege
- The firm will not disclose confidential information to third parties except as required by law or with client consent
- Note any disclosure obligations: mandatory reporting under AML/CFT laws (UAE AML Law, FATF obligations); the firm may be required to file STRs without notifying the client (tipping-off prohibition)

### 10. File retention and storage

- The firm will retain the file for [5–7] years following closure of the matter
- Original documents supplied by the client will be returned on request or at file closure
- After the retention period, files will be destroyed unless the client requests otherwise

### 11. Termination of engagement

- Client may terminate the engagement at any time on written notice; fees for work completed to that date are payable
- The firm may terminate on reasonable notice for good cause (including non-payment, client instructions that conflict with professional obligations, or breakdown of the working relationship)
- On termination, the firm will return the file; it may retain a lien over the file for unpaid fees (where permitted by applicable bar rules)

### 12. Limitation of liability

- Many jurisdictions permit firms to cap their liability to clients; confirm bar rules in the applicable jurisdiction
- In DIFC and UK, liability caps are common practice; in some MENA civil-law jurisdictions, professional liability cannot be excluded by contract
- Any cap should not apply to fraud, wilful misconduct, or gross negligence

### 13. Complaints procedure

- State the firm's internal complaints process
- In UAE, DIFC, and UK, there are regulatory complaints bodies that clients can approach if they are not satisfied with the firm's response

### 14. Governing law and dispute resolution

- Governing law: the law of the jurisdiction where the firm is licensed
- Disputes about the engagement letter: arbitration or litigation as appropriate; note that professional conduct disputes may involve bar authority oversight regardless

### 15. Acceptance

- Client signature (and date); return to law firm
- Confirm that work commences on receipt of signed letter

## Jurisdictional notes

| Jurisdiction | Bar requirement | Key specific terms |
|---|---|---|
| **UAE (DBA / ABA)** | Engagement letter recommended; ABA and DBA guidelines on legal fees | Contingency fees generally prohibited; fees in AED or agreed currency |
| **KSA (Saudi Bar)** | Written fee agreement required | Fees must be in SAR unless otherwise agreed; stamp of Saudi lawyer required |
| **DIFC (DFSA Licensed Practitioners)** | DFSA Practitioners Rules require client agreements | Conditional fees permitted with prior disclosure; mandatory disclosure of conflicts |
| **UK (SRA)** | SRA Code of Conduct requires client care letter and costs information | Costs estimate must be regularly updated; formal complaints procedure required |
| **France (Barreau)** | Convention d'honoraires required | Hourly rates or fixed fees; success fees limited to 10–15% of outcome by some bars |

## Common mistakes

- **Over-broad scope**: "Represent client in all matters related to the transaction" without limitation creates an open-ended engagement that is hard to manage and bill.
- **No out-of-scope list**: Without specifying what is not covered, clients will later argue that everything is covered; explicit exclusions save disputes.
- **No conflicts disclosure**: Conflicts of interest not addressed in the engagement letter can torpedo the engagement later if they become relevant.
- **Fee cap without client approval**: If there is a billing cap, both parties must agree; a firm cannot impose a cap unilaterally after commencement of work.
- **Missing tipping-off notice**: In AML-sensitive jurisdictions, the letter must note that the firm has AML reporting obligations and may be unable to notify the client if it files an STR.

## Related skills

- [[prompt-pack-full-contract-risk-review]]
- [[prompt-pack-due-diligence-report]]
- [[prompt-pack-employment-offer-letter]]
- [[prompt-pack-disclosure-letter]]
