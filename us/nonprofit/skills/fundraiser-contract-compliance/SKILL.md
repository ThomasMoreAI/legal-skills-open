---
name: fundraiser-contract-compliance
title: Professional Fundraiser Contract Compliance Check
description: Audits professional solicitor, fundraising counsel, and commercial co-venturer contracts for state charitable solicitation compliance. Classifies relationships, verifies vendor registration, extracts compensation and custody-of-funds terms, checks state-mandated clauses, and produces disclosure narratives, gap logs, and evidence packages. Use when reviewing fundraiser agreements, onboarding fundraising vendors, preparing state charity filings (CHAR007, CT-2CF, Schedule G), or auditing charitable solicitation compliance.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/fundraiser-contract-compliance
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: nonprofit
language: en
tags: [analysis, corporate, drafting]
---

# Professional Fundraiser Contract Compliance Check

Produces a structured compliance audit that classifies each fundraising relationship, verifies registrations, extracts disclosure data, and maps contract clauses against state-mandated requirements.

## Prerequisites

1. **States in scope** — where the charity is registered and/or solicits
2. **Contract documents** — executed agreements, amendments, SOWs, exhibits, fee schedules
3. **Filing target(s)** — annual report/renewal, campaign notice, co-venturer filing
4. **Operational artifacts** — donation flow diagrams, processor agreements, bank deposit controls (if available)
5. **Registration IDs** — fundraiser/solicitor/co-venturer and charity registration numbers per state (if known)
6. **Solicitation start date** — needed for Notice of Intent / contract filing deadlines

If inputs are missing, apply defaults: all registered states; annual report/renewal target; highest-risk classification until clarified. Mark gaps in "Open Items / Needed Inputs."

## Output Structure

### 1. Classify Relationship and Verify Registration

| Type | Key Markers | Regulatory Burden |
|---|---|---|
| **Professional Solicitor** | Directly solicits donations; may handle funds, donor data, scripts | Highest — registration, contract filing, campaign reporting, point-of-solicitation disclosures |
| **Fundraising Counsel** | Advises/manages campaigns; does NOT solicit or take custody of funds | Moderate — reclassified as solicitor if counsel solicits or takes custody |
| **Commercial Co-Venturer** | Ties purchase/use of goods to charitable benefit ("$1 per sale goes to X") | Advertising disclosures (benefit amount, duration, charity ID) and accounting |
| **Platform / Processor / Vendor** | Donation platform, payment processor, influencer/affiliate | May become solicitor or co-venturer depending on marketing claims and solicitation control |

> If classification is ambiguous, treat as highest-risk category until clarified by counsel.

**Registration verification** — for each vendor × state, extract and verify against state registry:

| Data Point | Verification Source |
|---|---|
| Legal name, DBA, address | State registry |
| Entity type, state of formation | Secretary of State DB |
| Registration No. (per state) | State DB (e.g., NY FR-No, CA CT-No) |
| Bond posted (if required) | State bond registry |
| Charity's own registration | State DB |

### 2. Extract Contract Data

Complete one row per **vendor × campaign × contract/SOW**:

| Category | Fields to Extract |
|---|---|
| **Parties** | Legal names, addresses, entity types |
| **Classification** | Solicitor / counsel / co-venturer / other |
| **Campaign** | Name/ID, dates, services, whether "solicitation" occurs |
| **Compensation** | Type (%, flat, retainer, per-call, CPM); percentage + base (gross vs. net); minimums/guarantees; expense allocations |
| **Custody of Funds** | Who receives funds first; deposit method; deposit/remittance timing; segregation; deductions before remittance |
| **Other Terms** | Charity name/logo use; donor data ownership; records/inspection rights; script approval; filing responsibilities; cancellation rights; subcontractors |

**Funds flow** — document for each arrangement: donor payment methods, intake entity, processor merchant of record, deposit account owner/type, deposit and remittance timing, deductions, reconciliation controls.

Funds-flow red flags:
- Vendor receives checks payable to vendor (not charity)
- Commingled accounts or no segregation of charitable funds
- Remittance timing unstated
- Charity lacks bank-view or reconciliation rights

### 3. Mandated-Clause Compliance Audit

Check each contract against this baseline. **Verify exact requirements per state statute.**

**A. Parties, Scope & Campaign**
- [ ] Charity and vendor identified (legal names, addresses)
- [ ] Services defined; whether vendor will solicit contributions
- [ ] Campaign(s) and geographic scope specified

**B. Compensation**
- [ ] Compensation stated clearly (%, fees, calculation base)
- [ ] "Gross receipts" vs. "net proceeds" defined
- [ ] Expenses and cost allocations defined
- [ ] Possible to compute % of gross contributions charity retains

**C. Custody of Funds**
- [ ] Who has custody/control at each step
- [ ] If vendor receives funds: segregation, deposit/remittance timing stated
- [ ] Cash/check handling, endorsements, payable-to instructions addressed
- [ ] Refunds/chargebacks and processor fees addressed

**D. Term & Cancellation**
- [ ] Term and renewal provisions clear
- [ ] Charity termination rights included
- [ ] Statutorily required cancellation right present (commonly 10–15 days) [VERIFY per state]

**E. Recordkeeping & Audit**
- [ ] Vendor must maintain campaign records (commonly 3–7 years)
- [ ] Charity access/inspection rights included
- [ ] Periodic accountings required (frequency and content defined)
- [ ] Written financial report required after campaign end (commonly 90 days) [VERIFY per state]

**F. Solicitation Materials & Disclosures**
- [ ] Charity approval of scripts/materials required before use
- [ ] Point-of-solicitation disclosures addressed (solicitor name, charity name, % retained)
- [ ] Co-venture ads include: benefit amount/%, duration, charity identity [VERIFY per state]

**G. Registration & Filings**
- [ ] Vendor represents current registration/licensing
- [ ] Registration numbers and renewal evidence required
- [ ] Responsibility for state filings/notices allocated
- [ ] Pre-solicitation filing deadlines referenced (commonly 10–20 days before start)

**H. Subcontractors**
- [ ] Subcontracting requires charity consent
- [ ] Subs meet same registration/recordkeeping requirements

**I. Data & Privacy**
- [ ] Donor data ownership and permitted use addressed
- [ ] Unauthorized sale/rental of donor lists prohibited
- [ ] Security measures and breach notification included

**State-specific matrix** — populate per state in scope:

| State | Statute [VERIFY] | Cancellation Right | Financial Report Deadline | Required Filings |
|---|---|---|---|---|
| CA | Bus. & Prof. Code §§ 17510+ | | | CT-1/CT-2 series |
| NY | Exec. Law Art. 7-A; 13 NYCRR Part 91 | | | CHAR007 |
| FL | Ch. 496, Fla. Stat. | | | |
| IL | 225 ILCS 460/ | | | |

### 4. Produce Outputs

**Gap / Issue Log**

| Issue ID | Contract / Vendor | Finding | Risk | Recommended Fix | Owner | Deadline |
|---|---|---|---|---|---|---|

**Disclosure narrative — Professional Solicitor/Fundraiser:**

> "During [start] to [end], the organization engaged **[Vendor]** ([address]; reg. no.: [state: ID]) as a **[professional solicitor / fundraising counsel]** for **[campaign]**. Compensation: **[X% of gross contributions / $X flat fee]** plus **[expenses]**. Gross contributions: $[amount]; fees paid: $[amount]; net to organization: $[amount] ([Y]% of gross). Contributions were **[received directly by organization / received by vendor and remitted within [X] days]**."

**Disclosure narrative — Commercial Co-Venturer:**

> "During the reporting period, **[Company]** conducted a commercial co-venture: **[promotion]**, [start] to [end]. Benefit to organization: **[$X per sale / X% of sales]**, subject to **[cap/floor]**. Total received: $[amount]. Funds transferred **[timing/method]**. Registration: **[state: ID/filing date]**."

**State reporting data map:**

| Item | Extracted Data | Form 990 Sch. G | CA CT-2CF | NY CHAR007 |
|---|---|---|---|---|
| Solicitor/CCV name | | Part I, Line 2a | Part II, Line 1 | Part B |
| Compensation % or amount | | Part I, Line 2c | Part II, Line 3 | Part B |
| Gross receipts | | Part I, Line 2b | | Part B |
| Net retained by charity | | | | Part B |
| Custody of funds (Y/N) | | Part I, Line 2b | | |
| Campaign dates | | | | |
| Vendor registration no. | | | | |

**Evidence binder checklist:**

- [ ] Executed contract + amendments/SOWs/exhibits
- [ ] Vendor registration proof per state
- [ ] Charity registration proof per state
- [ ] Notice of Intent / contract filing confirmations
- [ ] Campaign materials: scripts, mailers, landing pages, disclosures
- [ ] Funds flow proof: processor statements, bank deposits, remittance confirmations
- [ ] Campaign accounting: gross receipts, expenses, net to charity, refunds
- [ ] Vendor's written financial report of campaign
- [ ] Internal approvals (board/management)
- [ ] Annual report disclosure worksheet tied to source documents

## Guidelines

- Charitable solicitation regulation is **state-based** — requirements differ significantly by state and classification. Always verify current statutes; these laws are frequently amended.
- If classification is unclear or mixed, default to highest-risk category.
- If only a master agreement is available, treat missing SOWs/amendments as compliance risks.
- Confirm exact form field names per state (CA RRF-1/CT-2CF, NY CHAR500/CHAR007, Form 990 Schedule G).
- Pre-solicitation filing deadlines (Notices of Intent, contract filings) are commonly 10–20 days before campaign start — check per state.
- Every classification must be supported by contract language and operational evidence.
- Compensation base (gross vs. net) must be clearly identified and consistently applied.
- Disclosure narratives must match extracted data and be internally consistent.
- Mark all uncertain citations or requirements with [VERIFY].
- After delivering the audit, confirm: (1) classification matches the user's understanding of each vendor's role, (2) no additional contracts/amendments are outstanding, (3) whether additional state narratives are needed, (4) whether funds-flow concerns require escalation.
- This workflow supports legal and compliance review — it is not legal advice.

**Required disclaimer on every output:**

> THIS COMPLIANCE AUDIT REQUIRES INDEPENDENT ATTORNEY VERIFICATION OF ALL STATUTORY REQUIREMENTS, CLASSIFICATION DETERMINATIONS, AND FILING OBLIGATIONS, AND DOES NOT CONSTITUTE LEGAL ADVICE.
