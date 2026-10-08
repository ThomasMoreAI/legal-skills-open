---
name: prompt-pack-outside-counsel-guidelines-sboghossian
title: Outside Counsel Guidelines
description: Use when drafting outside counsel guidelines (OCGs) for a company's legal department governing how external law firms bill, staff, manage, and report on legal matters. Covers billing requirements, approved rate structures, staffing and supervision standards, invoice submission, e-billing, diversity requirements, and performance metrics. Applicable to any in-house legal department managing external counsel spend.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-outside-counsel-guidelines
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Outside Counsel Guidelines

## When to use this

Use this skill to draft or update a company's outside counsel guidelines — the formal policy document issued by the in-house legal department to all retained external law firms, setting out the requirements for billing, staffing, matter management, and performance. OCGs are typically incorporated by reference into engagement letters and govern the entire law-firm relationship.

Triggers:
- "Draft outside counsel guidelines for our legal department."
- "We need to update our OCGs to include e-billing and diversity requirements."
- "Write billing guidelines to send to our law firms."

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Company name | Names the document | Ask user |
| Applicable regions / countries | OCGs may need jurisdiction-specific sections for MENA, EU, UK | Ask user |
| E-billing platform (if any) | Determines invoice submission format requirements | Specify or state "paper/email invoice" |
| Rate approval process | How rates are approved annually | Annual approval in January |
| Diversity policy (if any) | Whether to include outside counsel diversity requirements | Optional — ask user |

## Optional inputs

- Preferred law firm panel (if OCGs are panel-specific)
- Matter budget requirement threshold (above what dollar amount must firms submit a budget)
- Pre-authorization requirements for expenses
- Insurance requirements

## OCG structure

---

**[COMPANY NAME] OUTSIDE COUNSEL GUIDELINES**
**Effective Date: [Date]**
**Issued by: Office of the General Counsel**

---

### Section 1: Introduction and Application

1.1 These Outside Counsel Guidelines ("Guidelines") apply to all law firms and individual counsel ("Outside Counsel") retained by [Company Name] ("Company") for legal services, unless a specific written engagement letter expressly modifies a provision of these Guidelines.

1.2 By accepting an engagement from the Company, Outside Counsel agrees to comply with these Guidelines. Any material deviation from these Guidelines must be agreed in writing with the General Counsel or Deputy General Counsel before work commences.

1.3 These Guidelines supplement (and do not replace) any applicable engagement letter, statement of work, or separate billing agreement.

---

### Section 2: Matter Engagement and Authorization

2.1 **Prior authorization required**: Outside Counsel shall not commence work on any new matter until receiving written authorization from the Company's Legal Department specifying the matter name, matter number, and scope of engagement.

2.2 **Engagement letter**: A written engagement letter must be executed before or promptly after commencement of work on any new matter. Verbal or email authorizations do not substitute for a written engagement letter for matters expected to exceed [USD 10,000] in total fees.

2.3 **Matter number**: All invoices and communications must reference the Company's assigned matter number. Outside Counsel must obtain a matter number from the Legal Department before commencing work.

2.4 **Sub-contracting**: Outside Counsel shall not sub-contract or refer any portion of a Company matter to another law firm without prior written approval. Any approved sub-contractor is subject to these Guidelines.

---

### Section 3: Staffing

3.1 **Right people on the matter**: Outside Counsel should staff matters with the most cost-effective mix of timekeepers appropriate to the complexity and nature of the work. Partners should focus on strategy, advocacy, and high-complexity work; associates and paralegals should handle research, drafting, and routine tasks.

3.2 **Rate approvals**: The billing rates of all timekeepers working on Company matters must be pre-approved by the Company's Legal Department. Rate schedules are reviewed and approved annually. Approved rates are set out in the Rate Approval Schedule appended to the engagement letter.

3.3 **No rate increases without approval**: Outside Counsel shall not increase rates during the calendar year. Proposed increases for the following year must be submitted to the Legal Department no later than November 1. Rate increases that are not approved in writing are not payable.

3.4 **Key personnel**: The lead partner/attorney identified in the engagement letter shall not be changed without the Company's prior written consent.

3.5 **New timekeepers**: Timekeepers not on the approved rate schedule may not bill to the matter without prior written approval. Outside Counsel must submit a new timekeeper approval request before any new timekeeper works on a Company matter.

3.6 **No first-year associate billing**: The Company does not pay for time billed by first-year associates on matters requiring substantive legal analysis. First-year associates may assist under appropriate supervision but their time is not billable to the Company.

---

### Section 4: Billing Practices

4.1 **Time recording**: Time must be recorded contemporaneously (same day or within one business day). Reconstructed time entries are not acceptable.

4.2 **Billing increments**: Time must be billed in increments of no more than 0.1 hour (6 minutes). Minimum billing increments of 0.25 hour (15 minutes) are not accepted.

4.3 **Detailed narrative**: Each time entry must contain a sufficiently detailed description of the work performed to allow the Company to assess its reasonableness and necessity. Entries such as "Legal research," "Review documents," or "Conference" without further specification are not acceptable.

4.4 **Block billing**: Block billing — recording multiple distinct tasks as a single time entry — is prohibited. Each task must be separately described and timed.

4.5 **Administrative tasks**: Time spent on administrative tasks (filing, docketing, scheduling, form completion) is not billable to the Company at attorney rates. If billable at all, such tasks should be at paralegal or administrative rates.

4.6 **Intra-firm conferences**: Routine intra-firm conferences and team check-ins involving more than [2] timekeepers require justification. The Company reserves the right to question and reduce charges for conferences that appear excessive relative to the matter complexity.

4.7 **Legal research**: Excessive research on basic or well-established points of law is not billable. Outside Counsel is expected to apply its existing knowledge base; research should be billed only for genuinely novel or jurisdiction-specific issues.

4.8 **Rounding and padding**: Time entries that appear to be rounded up or padded to a "round" number without a detailed narrative justification will be flagged and may be reduced.

---

### Section 5: Expenses and Disbursements

5.1 **Reimbursable expenses**: The Company will reimburse documented out-of-pocket expenses that are reasonable and necessary for the matter, subject to the restrictions below.

5.2 **Pre-authorization for major expenses**: Expenses exceeding [USD 500] in a single invoice line item require prior written approval from the responsible attorney at the Company.

5.3 **Travel**:
- Air travel: economy class for flights under [6 hours]; business class permitted only with prior approval for longer flights
- Hotel: up to [USD 300 / USD 400] per night in [tier 1 / tier 2 cities]; receipts required
- Meals: up to [USD 75] per person per day; no alcohol charged to the Company
- Ground transport: economy ride-share or standard rental car; no first-class car service without approval

5.4 **Photocopying and printing**: The Company does not pay for internal printing, photocopying, or scanning at per-page rates. If document production for court or regulatory purposes requires significant physical reproduction, submit a separate estimate for approval.

5.5 **Online legal research**: The Company does not pay separately for online legal research (Westlaw, LexisNexis, regional equivalents) — these costs are included in the blended hourly rate or are a firm overhead cost.

5.6 **No mark-ups**: The Company does not pay mark-ups on pass-through expenses. All expenses must be charged at actual cost.

5.7 **Courier / overnight delivery**: Reasonable courier costs are reimbursable where urgency is documented. Standard mail is not reimbursable.

---

### Section 6: Invoicing Requirements

6.1 **Invoice format**: Invoices must comply with [LEDES 1998B / LEDES 2000 / PDF with itemized detail — specify]. Invoices in a non-compliant format will be returned for correction.

6.2 **Invoice frequency**: Outside Counsel should invoice monthly. Invoices older than [6 months] from the date services were rendered will not be accepted for payment without prior written approval.

6.3 **Invoice content**: Each invoice must include: Company name; matter name and Company matter number; invoice number and date; billing period; itemized time entries (timekeeper, date, description, hours, rate, amount); itemized disbursements (description, amount); total amount due; currency; remittance details.

6.4 **E-billing submission**: Invoices must be submitted through [e-billing platform name, e.g., Legal Tracker / eBillingHub / Mitratech] at [portal URL]. Paper invoices are not accepted unless the matter predates the Company's e-billing system adoption.

6.5 **Disputed invoices**: The Company reserves the right to adjust or reject any invoice that does not comply with these Guidelines. Disputed line items will be identified in writing; undisputed portions will be paid within the standard payment terms. Outside Counsel shall not suspend work due to a good-faith billing dispute.

---

### Section 7: Matter Budgets

7.1 **Budget requirement**: For any matter expected to exceed [USD 25,000] in total fees, Outside Counsel must submit a matter budget within [10] business days of engagement.

7.2 **Budget format**: Budgets must be broken down by phase and task and aligned with UTBMS billing codes.

7.3 **Budget updates**: Outside Counsel must notify the responsible Company attorney promptly when it anticipates that actual costs will exceed the approved budget by more than [15%]. No work beyond the budget may proceed without written approval of a revised budget.

7.4 **Budget compliance**: The Company tracks Outside Counsel's budget compliance as part of its performance metrics.

---

### Section 8: Outside Counsel Diversity

8.1 The Company values diversity and expects its law firm partners to reflect this commitment.

8.2 **Diverse staffing**: Outside Counsel is encouraged to staff Company matters with diverse teams. "Diverse" includes women, underrepresented ethnic and racial minorities, LGBTQ+ individuals, and persons with disabilities.

8.3 **Diverse fee earner data**: At the Company's request, Outside Counsel will provide data on the diversity composition of fee earners who worked on Company matters during the preceding year.

8.4 **Aspirational targets**: The Company is committed to directing [X]% of its outside counsel spend to firms with demonstrated diversity leadership.

---

### Section 9: Performance Evaluation

9.1 Outside Counsel performance is evaluated by the Company on an ongoing basis on the following criteria:
- Quality of legal work and advice
- Responsiveness and communication
- Budget compliance
- Invoice compliance with these Guidelines
- Matter outcome (where applicable)
- Diversity of staffing

9.2 Firms that consistently fail to meet these Guidelines may be removed from the Company's preferred panel.

---

### Section 10: Confidentiality

10.1 Outside Counsel must maintain the confidentiality of all Company information received in connection with any engagement. Outside Counsel must not disclose Company information to any third party without prior written consent.

10.2 Outside Counsel must comply with applicable data protection law in handling Company personal data. A data processing agreement may be required.

---

### Section 11: Conflicts of Interest

11.1 Outside Counsel must perform a conflict check before accepting any new matter. Any potential conflict must be disclosed immediately to the General Counsel.

11.2 Outside Counsel shall not represent any party adverse to the Company in any matter, whether directly related or unrelated to any current engagement, without the Company's written consent.

---

### Section 12: Amendment and Questions

12.1 These Guidelines may be amended by the Company on [30-day] written notice to Outside Counsel.

12.2 Questions about these Guidelines should be directed to: [Legal Operations Manager name, email, phone].

---

## MENA-specific adaptations

- **Arabic-language firms**: For MENA regional firms (UAE, KSA, Lebanon, Egypt), include a clause on invoice submission in English (or bilingual), since the Company's e-billing and review processes operate in English.
- **Local counsel panel**: Identify approved local counsel in each MENA market; specify which matters require local counsel vs can be handled by the Company's primary firm.
- **VAT compliance**: UAE (5% VAT) and KSA (15% VAT) invoices must include VAT registration numbers and comply with local e-invoicing requirements (KSA ZATCA Phase 2).
- **Legal hold coordination**: Firms handling litigation matters must coordinate with the Company's Legal Department on document preservation and legal hold management.

## Common mistakes

- **Not updating OCGs to reflect e-billing adoption**: sending OCGs that reference paper invoices after deploying an e-billing platform creates confusion.
- **No rate approval process**: without a formal annual rate approval workflow, firms increase rates without company sign-off.
- **Omitting the pre-authorization requirement**: the most common source of billing disputes is work performed before a formal engagement letter.
- **No diversity metrics**: OCGs without diversity requirements or metrics have no enforcement mechanism; include at least aspirational targets and reporting obligations.

## Related skills

- [[prompt-pack-legal-invoice-review-checklist]]
- [[prompt-pack-legal-budget-forecast]]
- [[prompt-pack-matter-budget-template]]
- [[prompt-pack-legal-department-kpi-dashboard]]
- [[prompt-pack-legal-technology-rfp]]
