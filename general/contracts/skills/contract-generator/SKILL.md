---
name: contract-generator
title: Freelance Contract Generator
description: Generate professional freelance contracts, SOWs, and NDAs for client projects. Use when creating contracts, scope of work documents, or legal agreements for freelance engagements.
author: xinlingfeiwu
author_url: https://github.com/xinlingfeiwu/openclaw/tree/main/skills/contract-generator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Freelance Contract Generator

Generate professional contracts, statements of work (SOW), and NDAs for freelance engagements. Covers scope, payment, IP, revisions, and termination — the essentials for protecting both parties.

**DISCLAIMER**: These contracts are templates for common freelance arrangements. They are NOT legal advice. Users should have contracts reviewed by a qualified attorney for their jurisdiction before use.

## How to Use

```
/contract-generator service "Website redesign for Acme Corp, $5,000 fixed, 6 weeks, 2 revision rounds"
/contract-generator sow "Mobile app development, Phase 1: MVP, React Native, $15,000"
/contract-generator nda "Mutual NDA with TechStartup Inc for potential consulting engagement"
/contract-generator retainer "Monthly SEO services for LocalBiz, $1,500/mo, 3 month minimum"
```

- `$ARGUMENTS[0]` = Contract type: `service`, `sow`, `nda`, `retainer`, `hourly`
- `$ARGUMENTS[1]` = Project description with key terms

## Contract Types

### `service` — Fixed-Price Service Agreement

For one-time projects with a defined scope and fixed price.

```markdown
# FREELANCE SERVICE AGREEMENT

**Agreement Date**: [Date]
**Agreement Number**: [SA-YYYY-NNN]

## PARTIES

**Service Provider** ("Contractor"):
[Name/Business Name]
[Address]
[Email]

**Client**:
[Client Name/Business]
[Address]
[Email]

## 1. SCOPE OF WORK

### 1.1 Project Description

[Detailed description of what will be delivered]

### 1.2 Deliverables

| #   | Deliverable | Description   | Due Date |
| --- | ----------- | ------------- | -------- |
| 1   | [Item]      | [Description] | [Date]   |
| 2   | [Item]      | [Description] | [Date]   |
| 3   | [Item]      | [Description] | [Date]   |

### 1.3 Out of Scope

The following are explicitly NOT included in this agreement:

- [Item not included]
- [Item not included]
- [Common assumption to clarify]

Any work outside the defined scope requires a separate agreement
or written amendment to this contract with adjusted compensation.

## 2. TIMELINE

- **Project Start**: [Date]
- **Milestone 1**: [Description] — [Date]
- **Milestone 2**: [Description] — [Date]
- **Final Delivery**: [Date]

Timeline assumes timely feedback from Client. Delays in Client
feedback extend the timeline by an equal number of business days.

## 3. COMPENSATION

### 3.1 Total Fee

$[Amount] USD for the complete scope of work defined in Section 1.

### 3.2 Payment Schedule

| Payment   | Amount     | Due              |
| --------- | ---------- | ---------------- |
| Deposit   | $[X] (50%) | Upon signing     |
| Milestone | $[X] (25%) | Upon [milestone] |
| Final     | $[X] (25%) | Upon delivery    |

### 3.3 Payment Terms

- Payment due within 14 days of invoice date
- Accepted methods: [Bank transfer / PayPal / Wise / Stripe]
- Late payments accrue interest at 1.5% per month
- Work may be paused if payment is more than 14 days overdue

## 4. REVISIONS

- [x] rounds of revisions are included in the project fee
- Each revision round includes feedback on all deliverables
  submitted to date
- Additional revision rounds are billed at $[X]/hour
- A "revision" is a change to approved work within the original
  scope. New features or scope changes are not revisions.

## 5. INTELLECTUAL PROPERTY

### 5.1 Ownership Transfer

Upon receipt of full payment, all deliverables and associated
intellectual property rights transfer to the Client.

### 5.2 Prior to Full Payment

Contractor retains all rights to the work until final payment
is received in full.

### 5.3 Contractor Tools

Contractor retains rights to any pre-existing tools, frameworks,
libraries, or methodologies used in the project. Client receives
a perpetual, non-exclusive license to use these as part of the
deliverables.

### 5.4 Portfolio Rights

Contractor may display the completed work in their portfolio
and marketing materials unless Client requests otherwise in
writing.

## 6. CONFIDENTIALITY

Both parties agree to keep confidential any proprietary
information shared during this engagement, including but not
limited to business strategies, customer data, technical
specifications, and financial information. This obligation
survives termination of this agreement for a period of 2 years.

## 7. TERMINATION

### 7.1 By Client

Client may terminate this agreement with 7 days written notice.
Client will pay for all work completed to date plus any
non-refundable expenses incurred.

### 7.2 By Contractor

Contractor may terminate with 14 days written notice if Client
fails to provide required feedback, materials, or payment
within the agreed timeframes.

### 7.3 Kill Fee

If Client terminates after work has begun, the deposit is
non-refundable. Additional compensation is due for work
completed beyond the deposit amount.

## 8. WARRANTIES AND LIABILITY

### 8.1 Contractor Warranties

Contractor warrants that:

- The work will be original and not infringe third-party rights
- The work will substantially conform to the agreed specifications
- Contractor has the right to enter this agreement

### 8.2 Limitation of Liability

Contractor's total liability under this agreement shall not
exceed the total fees paid by Client under this agreement.

### 8.3 No Consequential Damages

Neither party shall be liable for indirect, incidental, or
consequential damages.

## 9. GENERAL PROVISIONS

### 9.1 Independent Contractor

Contractor is an independent contractor, not an employee.

### 9.2 Governing Law

This agreement is governed by the laws of [State/Country].

### 9.3 Entire Agreement

This document constitutes the entire agreement. Amendments
must be in writing and signed by both parties.

### 9.4 Force Majeure

Neither party is liable for delays caused by events beyond
reasonable control.

---

**AGREED AND ACCEPTED:**

Contractor: ****\*\*\*\*****\_****\*\*\*\***** Date: \***\*\_\_\_\_\*\***

Client: ****\*\*\*\*****\_****\*\*\*\***** Date: \***\*\_\_\_\_\*\***
```

### `sow` — Statement of Work

Similar to service agreement but focused on detailed scope for larger projects. Includes:

- Detailed requirements broken into phases
- Acceptance criteria for each deliverable
- Change request process
- Communication plan (weekly meetings, tools, contacts)
- Assumptions and dependencies

### `nda` — Non-Disclosure Agreement

Standard mutual or one-way NDA. Includes:

- Definition of confidential information
- Obligations of receiving party
- Exclusions (public info, independently developed, etc.)
- Term (typically 2 years)
- Return/destruction of materials
- Remedies for breach

### `retainer` — Monthly Retainer Agreement

For ongoing work relationships. Includes:

- Monthly hours included (e.g., 20 hours/month)
- Rollover policy (unused hours expire or roll over 1 month)
- Overage rate (hourly rate for hours beyond retainer)
- Scope of services (types of work covered)
- Monthly reporting requirements
- Minimum commitment period
- Cancellation notice period (typically 30 days)
- Monthly invoicing schedule

### `hourly` — Hourly Rate Agreement

For time-and-materials engagements. Includes:

- Hourly rate
- Minimum billing increment (15 min or 30 min)
- Estimated hours (non-binding)
- Weekly/monthly hour caps
- Time tracking and reporting method
- Invoice frequency (weekly or bi-weekly)

## Output

Save to `output/contracts/`:

```
output/contracts/
  [contract-type]-[client-name]-[date].md    # Markdown version
  [contract-type]-[client-name]-[date].html  # Print-ready HTML
```

HTML version includes:

- Professional formatting suitable for printing
- Clear section numbering
- Signature lines
- Page break hints for clean printing
- Header with agreement number on each page

## Important Notes

1. These are TEMPLATES — always customize for the specific engagement
2. Include specific deliverables — vague scope is the #1 source of disputes
3. Always include an "Out of Scope" section — prevents scope creep
4. Payment milestones tied to deliverables protect both parties
5. The IP clause should match the engagement — some clients need work-for-hire language
6. Recommend both parties sign digitally (DocuSign, HelloSign) for convenience and records
