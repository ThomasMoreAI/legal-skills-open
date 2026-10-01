---
name: contract-administration-fdu-ins
title: Contract Administration Skill
description: 'Manage construction contract administration from the field perspective. Covers AIA contract forms (A101, A201, A401), bond types and requirements, mechanics lien law, insurance verification, indemnification, dispute resolution, and subcontractor default procedures. Provides practical field guidance for notice requirements, lien waiver processing, COI verification, and claims documentation. Integrates with pay-application (lien waivers), change-order-tracker (constructive changes), delay-tracker (notice provisions), sub-performance (default triggers), and cost-tracking (back-charges). Triggers: "contract", "contract admin", "AIA", "A201", "A101", "bond", "performance bond", "payment bond", "lien", "lien waiver", "mechanics lien", "insurance", "COI", "certificate of insurance", "OCIP", "CCIP", "indemnification", "dispute", "mediation", "arbitration", "notice", "cure notice", "default", "sub default", "termination for cause", "claims", "ConsensusDocs", "EJCDC".'
author: FDU-INS
author_url: https://github.com/FDU-INS/Insurance-Skills/tree/main/Skills/contract-administration
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: construction
language: en
sources:
- title: Aia Contract Forms Guide
  path: references/aia-contract-forms-guide.md
- title: Bonds And Insurance Guide
  path: references/bonds-and-insurance-guide.md
- title: Dispute Resolution Guide
  path: references/dispute-resolution-guide.md
- title: Lien Law Field Guide
  path: references/lien-law-field-guide.md
- title: Skill Detail
  path: references/skill-detail.md
---

# Contract Administration Skill

## Overview

The **contract-administration** skill provides construction superintendents with practical, field-level guidance on contract administration tasks that directly affect daily operations. This is not a law school course -- it is the working knowledge a superintendent needs to protect the project, keep subcontractors accountable, process pay applications correctly, and avoid the costly mistakes that happen when field personnel do not understand the contract documents sitting in the job trailer.

**Why superintendents need this:**
- You sign daily reports that become evidence in claims and disputes
- You accept or reject work that triggers payment obligations
- You direct subcontractors under contracts you may not have read cover-to-cover
- You are the first person to notice when a sub is failing, and the documentation you create (or fail to create) determines whether the project can terminate for cause or is stuck
- Your verbal directives can create constructive change orders worth hundreds of thousands of dollars
- Missing a notice deadline by even one day can waive the project's right to recover time or money

**What this skill covers:**
1. AIA contract forms that govern most commercial construction
2. How ConsensusDocs and EJCDC contracts differ (so you are not blindsided)
3. Bond types, requirements, and claims processes
4. Mechanics lien law and lien waiver processing
5. Insurance requirements and COI verification
6. Indemnification clauses and what they mean in the field
7. Dispute resolution procedures from notice through arbitration
8. Subcontractor default procedures from warning signs through replacement

**Critical principle:** In contract administration, **written notice is everything**. Verbal conversations do not preserve contractual rights. If it is not in writing, it did not happen.

---

## AIA Contract Forms Field Guide

The American Institute of Architects (AIA) publishes the most widely used standard contract forms in commercial construction. Three documents form the backbone of most projects.

### A101 -- Owner-Contractor Agreement

The A101 is the main agreement between the owner and general contractor. It establishes the deal: scope, price, time, and payment terms.

#### Key Clauses for Field Operations

| Article | Subject | What the Super Needs to Know |
|---------|---------|------------------------------|
| Art. 3 | Date of Commencement & Substantial Completion | Your schedule is contractually bound to these dates. Substantial Completion triggers retainage release, warranty periods, and liquidated damages cutoff. Know these dates cold. |
| Art. 4 | Contract Sum | The total price. Every dollar above this requires an approved change order. No verbal authorizations. |
| Art. 5 | Progress Payments | Pay application schedule (monthly, Net 30 per W Principles standard), retainage percentage (W Principles default: 10% flat), and conditions for payment. The architect certifies payment -- you provide the supporting documentation. |
| Art. 6 | Dispute Resolution | Specifies whether disputes go to mediation, arbitration, or litigation. Check this BEFORE you have a dispute. |
| Art. 7 | Termination or Suspension | Owner can suspend work for convenience; contractor can stop work if payment is 7+ days late (after 7-day written notice). |
| Art. 8 | Miscellaneous | Insurance requirements, key personnel, governing law. |

**Field Impact:** The A101 sets the financial and time boundaries. When someone on site says "the owner told us to go ahead with the extra work," your response is: "Show me the signed change order or written authorization per Article 4."

#### Common Pitfalls
1. **Starting work before Notice to Proceed (NTP)** -- Work performed before NTP may not be compensable
2. **Missing Substantial Completion criteria** -- Review the definition; it is not "we think it is done" but rather "the owner can use it for its intended purpose"
3. **Retainage math errors** -- Track retainage held vs. retainage due on every pay application
4. **Liquidated damages ignorance** -- Know the daily LD rate; it starts accumulating the day after Substantial Completion deadline

### A201 -- General Conditions of the Contract for Construction

The A201 is the most important document for daily field operations. It contains the rules of engagement for how the project is built, administered, and disputes are resolved. Every superintendent should read Articles 3, 4, 7, 8, 9, 12, 14, and 15.

#### Article 1 -- General Provisions

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 1.1.1 | Contract Documents defined | Drawings, specs, A101, A201, addenda, modifications. All carry equal weight -- specs do not override drawings or vice versa. |
| 1.2 | Correlation of Documents | If something is shown on drawings but not in specs (or vice versa), contractor must provide it. This prevents "I did not see it in the specs" arguments. |
| 1.5 | Ownership of Documents | Drawings belong to the architect. You can use them for this project only. |

#### Article 2 -- Owner Responsibilities

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 2.2 | Evidence of Financial Arrangements | Contractor can request proof that the owner can pay. Use this if you suspect owner financial trouble. |
| 2.3 | Information and Services | Owner must provide surveys, legal descriptions, utility locations. If owner data is wrong and it causes delay or extra cost, that is an owner-caused issue. |

#### Article 3 -- Contractor Responsibilities

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 3.1.1 | General duty | Contractor shall perform work "consistent with the Contract Documents and reasonably inferable therefrom." The word "reasonably inferable" means you cannot claim ignorance of something obvious even if it is not explicitly shown. |
| 3.2 | Review of Documents | Contractor must review documents and report errors or inconsistencies. Failure to report a noticed error can shift responsibility to contractor. |
| 3.3 | Supervision and Construction Procedures | Contractor is solely responsible for means, methods, techniques, sequences, and procedures. The architect cannot tell you HOW to build -- only WHAT to build. |
| 3.4 | Labor and Materials | Contractor furnishes all labor, materials, equipment. Unless the contract says "Owner furnished," you provide it. |
| 3.5 | Warranty | Contractor warrants materials and workmanship free from defects and conforming to contract documents. This is not a time-limited warranty -- it covers the entire construction period. |
| 3.7 | Permits, Fees, Notices | Contractor obtains and pays for permits (unless contract says otherwise). You must comply with all codes regardless of what the drawings show. If code conflicts with drawings, notify the architect. |
| 3.9 | Superintendent | Contractor shall employ a competent superintendent who shall be present on site at all times work is being performed. The super represents the contractor in the field and is authorized to receive communications. |
| 3.10 | Contractor's Schedules | Must submit schedule promptly after contract execution and update regularly. Schedule must conform to contract time limits. |
| 3.12 | Shop Drawings and Submittals | Contractor reviews submittals for compliance before sending to architect. Architect review does not relieve contractor of responsibility for errors in submittals. |
| 3.18 | Indemnification | Contractor indemnifies owner and architect for claims arising from contractor's negligent acts or omissions. This is the key liability clause -- see Indemnification section below. |

#### Article 4 -- Architect's Role

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 4.2.1 | Administration | Architect administers the contract, visits site, keeps owner informed. Architect does NOT supervise construction -- that is the contractor's job. |
| 4.2.6 | Rejection of Work | Architect can reject work that does not conform to contract documents. This can happen at any time, even after you think the work is accepted. |
| 4.2.7 | Submittals | Architect reviews submittals for "limited purpose of checking for conformance with information given and the design concept." This is not a comprehensive check -- contractor retains responsibility. |
| 4.2.11-14 | Initial Decision Maker | Architect serves as the Initial Decision Maker (IDM) for claims and disputes. Claims must go through the architect before mediation or arbitration. |

#### Article 7 -- Changes in the Work

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 7.1 | General | Changes only by Change Order (signed by owner, contractor, architect), Construction Change Directive (CCD, signed by owner and architect), or minor change order (architect alone for changes not affecting cost or time). |
| 7.2 | Change Orders | Must be signed by all three parties. No verbal change orders. Period. |
| 7.3 | Construction Change Directives | Owner and architect can direct changes even without contractor agreement on cost/time. Contractor must proceed with the work. Cost determined later by: mutual agreement, unit prices, cost-plus, or architect's determination. |
| 7.4 | Minor Changes | Architect can order minor changes consistent with intent of contract documents, not involving cost or time adjustment. If you think a "minor change" actually affects cost or time, object in writing immediately. |

**FIELD CRITICAL:** If someone verbally directs you to do something different from the drawings, respond:
1. Acknowledge the request
2. State that it requires a written change directive or change order
3. Send written confirmation of what was requested (email is acceptable)
4. Do NOT proceed until you have written authorization unless the CCD process applies

#### Article 8 -- Time

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 8.1.1 | Time definitions | "Date of Commencement" starts the clock. Know this date. |
| 8.2.1 | Progress and Completion | Time limits are "of the essence." This legal phrase means deadlines are strict -- missing them is a material breach. |
| 8.3 | Delays and Extensions | If contractor is delayed by owner, architect, or separate contractor, contractor is entitled to time extension. BUT: contractor must submit a claim per Article 15 -- the extension is not automatic. |

#### Article 9 -- Payments and Completion

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 9.2 | Schedule of Values | Submit SOV before first pay application. Break it down enough to track progress meaningfully. Front-loading the SOV (overvaluing early work) is a common dispute trigger. |
| 9.3 | Applications for Payment | Monthly, per contract schedule. Include: SOV progress, stored materials, change orders. Architect certifies within 7 days. |
| 9.4 | Certificates for Payment | Architect certifies payment to owner. Certificate is NOT acceptance of the work. |
| 9.5 | Decisions to Withhold | Architect can withhold certification for: defective work, third-party claims, failure to pay subs, damage to owner or another contractor, reasonable evidence work cannot be completed for unpaid balance, persistent failure to carry out work. |
| 9.6 | Payment to Subcontractors | Contractor must pay subs within 7 days of receiving payment from owner. **This is a field issue** -- sub performance problems and payment disputes are directly connected. |
| 9.8 | Substantial Completion | Architect inspects and issues Certificate of Substantial Completion (AIA G704). This document: lists incomplete items (punch list), establishes responsibilities for maintenance/utilities/insurance, fixes time for completing punch list, triggers retainage release timeline. |
| 9.9 | Partial Occupancy | Owner can occupy part of the project before Substantial Completion with mutual consent. Triggers insurance and warranty questions -- get these in writing. |
| 9.10 | Final Completion and Payment | After punch list complete, contractor submits final pay application. Owner must pay within 30 days of architect's final certificate. |

#### Article 10 -- Protection of Persons and Property

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 10.1 | Safety Precautions | Contractor responsible for safety. This is non-delegable. Even if a sub causes the unsafe condition, you are responsible for site safety. |
| 10.2 | Safety of Persons and Property | Contractor must protect: workers, the public, adjacent property, existing structures. Includes providing barricades, signage, flagging. |
| 10.3 | Hazardous Materials | If contractor encounters hazardous materials not addressed in contract documents, STOP WORK in the affected area and immediately notify owner and architect in writing. |

#### Article 11 -- Insurance and Bonds

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 11.1 | Contractor's Insurance | Contractor carries CGL, auto, workers comp, umbrella. Limits as specified. Owner and architect listed as additional insured. |
| 11.2 | Owner's Insurance | Owner carries property insurance (Builder's Risk) covering full insurable value. This is typically replacement cost, all-risk coverage. |
| 11.3 | Waivers of Subrogation | Both parties waive subrogation rights against each other to the extent covered by insurance. This prevents the insurance company from suing the other party after paying a claim. |
| 11.4 | Bonds | If required, contractor furnishes performance and payment bonds per AIA A312. |

#### Article 12 -- Uncovering and Correction of Work

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 12.1 | Uncovering of Work | If work is covered contrary to architect's request, contractor uncovers at own cost. If architect did not specifically request to observe and work is found compliant, owner pays cost of uncovering and restoration. If non-compliant, contractor pays. |
| 12.2 | Correction of Work | Contractor corrects defective work at no cost to owner. Correction period is 1 year after Substantial Completion (not 1 year after Final Completion). |

#### Article 14 -- Termination or Suspension

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 14.1 | Termination by Contractor | Contractor can terminate if: work stopped for 30+ consecutive days due to court order, government act, or architect's failure to certify payment (not contractor's fault); or if owner fails to pay for 60+ days after due date. Requires 7-day written notice. |
| 14.2 | Termination by Owner for Cause | Owner can terminate if contractor: persistently fails to supply enough workers or materials, fails to pay subs, persistently disregards laws or contract requirements, or is otherwise guilty of substantial breach. Requires 7-day written notice and opportunity to cure. |
| 14.3 | Suspension by Owner | Owner can suspend work without cause upon 7-day written notice. Contractor entitled to extension and cost adjustment. |
| 14.4 | Termination by Owner for Convenience | Owner can terminate for any reason upon 7-day written notice. Contractor receives payment for work completed plus reasonable overhead and profit on work not performed. |

#### Article 15 -- Claims and Disputes

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 15.1.1 | Definition | A Claim is a demand seeking adjustment of the contract sum, contract time, or other relief. Written. With supporting documentation. |
| 15.1.3 | Notice of Claims | **CRITICAL**: Claims must be initiated within 21 days after occurrence of the event giving rise to the claim. Missing this deadline can waive the claim entirely. |
| 15.1.4 | Continuing Contract Performance | Pending final resolution, contractor must continue performing work. You cannot stop work because of a pending claim. |
| 15.2 | Initial Decision | Claims go to the Initial Decision Maker (architect). IDM must render decision within 10 days. If IDM fails to act within 30 days, claim proceeds to mediation. |
| 15.3 | Mediation | Mandatory before arbitration or litigation. Per AAA Construction Industry Mediation Procedures (or other agreed rules). Mediation is non-binding -- a settlement attempt, not a decision. |
| 15.4 | Arbitration | If A101 selects arbitration, disputes resolved per AAA Construction Industry Arbitration Rules. Arbitration is binding and final. Arbitration must be demanded within the applicable statute of limitations. |

**THE 21-DAY RULE:** This is the single most important deadline in the A201 for field personnel. When something happens on your project that could be a claim (delay, extra work, differing site conditions, design error), you have 21 days to submit written notice. Mark it on your calendar. Set a reminder. Do not let this deadline pass.

### A401 -- Contractor-Subcontractor Agreement

The A401 governs the relationship between the general contractor and each subcontractor. It incorporates the A201 by reference, meaning subs are bound by the same rules.

#### Key Clauses for Field Operations

| Article | Subject | What the Super Needs to Know |
|---------|---------|------------------------------|
| Art. 2 | Mutual Rights and Responsibilities | Sub is bound by same obligations to contractor that contractor has to owner. This "flow-down" means every A201 requirement applies to subs. |
| Art. 4 | Contractor's Responsibilities | Contractor must provide sub with copies of contract documents relevant to sub's work. Sub should have all drawings and specs for their scope. |
| Art. 5 | Subcontractor's Responsibilities | Sub furnishes labor, materials, equipment for their scope. Sub coordinates with other subs. Sub is responsible for their own safety program. |
| Art. 6 | Changes | Changes to sub's work require Change Order or Construction Change Directive. Sub cannot perform changed work without written authorization. Sub must notify contractor of claims for additional cost or time within 21 days. |
| Art. 7 | Sub's Applications for Payment | Sub submits pay apps per schedule. Contractor pays sub within 7 days of receiving owner payment. Retainage per contract terms. |
| Art. 8 | Progress Schedule | Sub must prepare schedule and update regularly. Sub must coordinate with master schedule. |
| Art. 9 | Sub's Recourse | If contractor does not pay within 7 days of receiving owner payment (and not due to sub's fault), sub can demand written explanation. If not resolved, sub can stop work after 7-day notice. |
| Art. 11 | Disputes | Claims between contractor and sub follow same mediation/arbitration process as A201. |
| Art. 12 | Termination | Contractor can terminate sub for cause if sub: fails to supply adequate workforce, fails to make payments to their own subs/suppliers, disregards laws or codes, fails to prosecute work, or is otherwise guilty of substantial breach. Requires 7-day notice and 7-day cure period. |

**Field Impact of A401:** When you are managing subs on site, you are enforcing the A401. When a sub is underperforming, the documentation you create is the foundation for any cure notice or termination. Your daily reports, emails, photos, and meeting minutes are the record.

---

## Bond Types & Requirements

Bonds are three-party agreements: the **principal** (contractor or sub), the **obligee** (owner or GC), and the **surety** (bonding company). The surety guarantees that the principal will perform its obligations.

### Bond Type Comparison

| Bond Type | Typical Amount | Who Requires It | What It Protects | When It Applies |
|-----------|---------------|-----------------|------------------|-----------------|
| **Bid Bond** | 5-10% of bid amount | Owner | Owner against contractor withdrawing bid after submission | Pre-award only |
| **Performance Bond** | 100% of contract value | Owner (or GC for subs) | Completion of the work per contract documents | Duration of contract + warranty period |
| **Payment Bond** | 100% of contract value | Owner (or GC for subs) | Payment to subs, suppliers, and laborers | Duration of contract |
| **Maintenance Bond** | 10-25% of contract value | Owner | Correction of defective work during warranty period | Warranty period (typically 1-2 years) |
| **Supply Bond** | 100% of supply contract | Contractor or Owner | Material delivery per supply agreement | Duration of supply contract |
| **Subdivision Bond** | Varies by jurisdiction | Municipality | Completion of public improvements (roads, utilities, sidewalks) | Until municipal acceptance |

### Bid Bonds -- Pre-Award Protection

**What they protect:** If a contractor submits the low bid and then refuses to enter the contract, the bid bond covers the difference between the low bid and the next acceptable bid (up to the bond amount).

**Typical amount:** 5% to 10% of the bid price.

**Field relevance for superintendents:** Minimal -- bid bonds are a pre-construction issue. But understand that your company's bonding capacity is a finite resource. Every bonded project reduces available capacity.

**Bonding capacity basics:**
- Bonding companies look at: working capital, net worth, work on hand, experience, and track record
- Typical aggregate capacity: 10x net worth (rough rule of thumb)
- Single project limit: usually 1/3 to 1/2 of aggregate capacity
- Slow pay apps, cost overruns, and claims eat into bonding capacity

### Performance Bonds -- Completion Guarantee

**What they protect:** If the contractor defaults (fails to complete the work), the surety must either:
1. Complete the work themselves (hiring a completion contractor)
2. Pay the obligee the cost to complete (up to bond amount)
3. Tender a new contractor to complete the work
4. Arrange financing to help the contractor complete

**Key provisions:**
- Bond amount is typically 100% of the contract value
- Bond follows contract modifications (change orders increase bond obligation)
- Surety has right to investigate before acting -- they do not pay automatically
- Obligee must give surety written notice of default
- Surety typically has 30-60 days to respond after notice

**Performance bond claim process:**
1. Contractor fails to perform
2. Owner sends written notice to contractor (per contract cure provisions)
3. If contractor fails to cure, owner declares contractor in default
4. Owner sends written notice of default to surety (with copies of all default documentation)
5. Surety investigates (typically 30-45 days)
6. Surety elects remedy: complete, pay, tender, or finance
7. If surety denies claim, litigation may follow

**What the super needs to know:** Your documentation of contractor or sub performance failures is the evidence used in a bond claim. Daily reports, photos, emails, and meeting minutes documenting the default are critical. Without contemporaneous documentation, the surety will deny the claim.

### Payment Bonds -- Protecting the Payment Chain

**What they protect:** Payment to subcontractors, sub-subcontractors, suppliers, and laborers who are not paid by the contractor.

**Federal projects -- Miller Act (40 U.S.C. 3131-3134):**
- Required on ALL federal construction projects over $35,000
- Performance and payment bonds both required
- Payment bond covers subs, suppliers, and laborers
- First-tier subs can make claim directly
- Second-tier subs/suppliers must give 90-day written notice to the contractor
- Claim must be filed within 1 year of last furnishing labor/materials

**State projects -- Little Miller Acts:**
- Most states have versions of the Miller Act for state/local public projects
- Thresholds vary by state ($5,000 to $100,000+)
- Notice and filing deadlines vary -- check your state statute
- Some states extend to private projects when bonds are required

**Private projects:**
- Payment bonds not required by law on private projects
- Owner or lender may require as a condition of the contract
- Bond provides alternative to mechanics lien rights on private projects
- Many payment bonds exclude suppliers more than two tiers removed from the principal

**Payment bond claim process:**
1. Claimant (sub/supplier) is not paid
2. Claimant sends written notice to the surety (and principal)
3. First-tier claimants: no preliminary notice required (federal Miller Act)
4. Second-tier claimants: must send 90-day notice (federal) or per state requirements
5. Claimant files suit on bond within deadline (1 year federal, varies by state)
6. Surety investigates and pays valid claims or litigates

**What the super needs to know:**
- Track sub payment status at every pay application cycle
- If a sub's suppliers or workers complain about non-payment, this is a red flag for payment bond exposure
- Lien waivers from subs should flow through every pay cycle (see Mechanics Lien section)
- If you are on a public project, there are no mechanics lien rights -- the payment bond is the sole remedy for unpaid parties

### Practical Bond Scenarios for Field Personnel

**Scenario 1: Sub is failing to perform**
- Before considering a performance bond claim against the sub, you must first exhaust the cure notice process under the subcontract
- Document everything: staffing shortages, missed milestones, quality deficiencies, failed inspections
- Send written cure notice per A401 (7-day notice, 7-day cure period)
- If sub fails to cure, terminate for cause and notify surety

**Scenario 2: Sub's workers approach you about non-payment**
- This is an early warning of sub financial distress
- Document the complaint (date, who, what they said)
- Notify your PM and corporate office immediately
- Check the sub's payment bond information
- Increase oversight of sub's pay applications and lien waiver submissions

**Scenario 3: Owner is not paying the GC**
- Review the GC's performance bond provisions
- After appropriate notice periods, GC may have right to stop work or terminate
- Subs affected by non-payment can pursue claims against the GC's payment bond

---


---

> **Extended reference**: Detailed examples, templates, scoring rubrics, and best practices are in `references/skill-detail.md`.
