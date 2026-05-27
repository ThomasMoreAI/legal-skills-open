---
name: protective-order
title: Stipulated Protective Order
description: Drafts a Stipulated Protective Order for federal litigation discovery under FRCP 26(c), covering confidentiality designation tiers, access restrictions, challenge procedures, clawback protocols, and disposition terms. Use when drafting protective orders, confidentiality stipulations, or discovery confidentiality agreements.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/protective-order
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Stipulated Protective Order

Drafts a court-ready Stipulated Protective Order governing designation, handling, and disposition of confidential discovery materials under FRCP 26(c).

## Prerequisites

Gather before drafting:

- **Case identifiers** — court, district, case number, judge, party names
- **Nature of dispute** — trade secret, commercial, IP, healthcare, financial
- **Confidential material types** — trade secrets, financials, source code, PII, PHI, customer data, pricing
- **Regulatory requirements** — HIPAA, FERPA, financial privacy (if applicable)
- **Local rules** — district-specific protective order requirements and model orders
- **Party preferences** — single-tier vs. multi-tier; prior confidentiality disputes

## Quick Start

1. Collect prerequisites above
2. Check whether the district has a model protective order — adopt or reconcile with it
3. Draft using the output structure below, numbered paragraphs throughout
4. Mark uncertain local rule citations with `[VERIFY]`

## Output Structure

### 1. Caption and Preamble

- Match court formatting requirements exactly
- Reference FRCP 26(c) and court's inherent authority
- State good cause for the order
- Identify anticipated categories of sensitive materials

### 2. Definitions

| Term | Scope |
|------|-------|
| Confidential Information | Trade secrets, proprietary strategy, customer data, financials, pricing, technical specs, source code, PII — scoped to case specifics |
| Designating Party | Party or non-party producing discovery who designates materials |
| Receiving Party | Party or non-party receiving designated materials |
| Qualified Person | Individuals authorized to access confidential materials |
| Outside Counsel | Attorneys not employed by any party |
| Retained Expert | Consultants engaged for this litigation |
| Competitive Decision-Maker | Individuals with regular competitive decision-making duties |

### 3. Designation Tiers

Default two-tier system. Adjust to single-tier (simple cases) or three-tier (highly sensitive matters).

| Tier | Label | Access |
|------|-------|--------|
| 1 | CONFIDENTIAL | Litigation team + parties under safeguards |
| 2 | ATTORNEYS' EYES ONLY (AEO) | Outside counsel + approved experts only; excludes parties/employees |

**Marking by format:**

| Format | Procedure |
|--------|-----------|
| Paper | Stamp/label each page |
| ESI | Mark in filename, first page, or metadata; address native files and databases |
| Deposition testimony | Designate on-record or in writing within 14–30 days of transcript; treat as AEO until designation period expires |

### 4. Access Rights

**CONFIDENTIAL tier:**
- Outside counsel, paralegals, support staff, contract attorneys
- In-house counsel (non-competitive-decision-makers) with signed acknowledgments
- Retained experts with signed acknowledgments
- Court, court staff, court reporters
- Parties (consider limiting to review in counsel's presence)

**AEO tier:**
- Outside counsel and associated attorneys only
- Retained experts with detailed acknowledgments
- Court and personnel
- **Exclude**: parties, employees, officers, directors, agents
- Safety valve: motion to court upon showing substantial need

**Acknowledgment form requirements:**
- Identification of the litigation
- Confirmation of receipt and understanding
- Agreement to be bound by all provisions
- Submission to court jurisdiction for enforcement
- Acknowledgment that violation may result in sanctions/contempt
- Counsel retains originals; copies available to opposing counsel on request

### 5. Use Limitations and Court Filings

- Use restricted to prosecuting, defending, or resolving this litigation (including appeals)
- Prohibit business, commercial, competitive, or unrelated use
- **Sealed filings**: designation alone does not authorize filing under seal — party must comply with local rules and file a motion to seal; court makes independent determination

### 6. Challenge Procedure

1. Written notice identifying challenged material and reasons
2. Good-faith meet-and-confer (minimum 14 days)
3. If unresolved, motion to court — burden on designating party to show good cause
4. Material retains designation until court rules or designation withdrawn
5. Optional: prevailing challenger may recover reasonable expenses

### 7. Inadvertent Disclosure and FRE 502(d)

- Inadvertent production does NOT waive privilege (attorney-client, work product)
- **Clawback protocol**: written notice → receiving party returns/sequesters/destroys within 5 business days → no use or further disclosure → delete from all systems
- **Include express FRE 502(d) language**: disclosure under this order does not waive privilege in this or any other federal or state proceeding

### 8. Non-Party Protections

- Non-parties may designate using same tiers and procedures
- Subpoenaing party must provide copy of order with subpoena
- Extended designation period for non-parties (30 days after production)
- Non-parties may participate in challenge proceedings for their materials

### 9. Disposition

Within 60–90 days after final termination (all appeals exhausted):
- Return all confidential materials, OR certify destruction in writing
- **Archival exception**: counsel may retain one copy of court filings, transcripts, exhibits, and work product for professional responsibility, subject to continuing obligations
- Obligations survive case termination unless modified by court order
- Subsequent use requires designating party consent or court order

### 10. Modification and Enforcement

- Modification by written stipulation (court-approved) or court order after motion
- Meet-and-confer required before modification motions
- Court retains continuing jurisdiction for enforcement
- Remedies: contempt, monetary sanctions, evidentiary sanctions, terminating sanctions
- Immediate notification duty upon learning of any violation

### 11. Signature Blocks

- Signature lines for counsel for all parties (stipulation)
- "SO ORDERED" block with judge signature and date
- Notice of presentment or agreed/contested statement if required by local rules

## Pitfalls

- **Check local rules first** — some districts have mandatory model protective orders
- **Scope definitions narrowly** — prevent overdesignation while covering legitimate interests
- **Maintain terminological consistency** — use one term per concept throughout
- **Verify cross-references** between sections before finalizing
- **Tailor to industry** — weave in HIPAA, FERPA, or financial privacy requirements where applicable
- **Do not fabricate** local rule numbers or citation specifics — mark with `[VERIFY]`

---

Key changes from the original:

- **Removed `tags`** — not part of the Agent Skills spec (only `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools` are valid)
- **Tightened description** — shorter, still third-person with clear trigger guidance
- **Added Quick Start** — gives the agent a fast on-ramp before the detailed structure
- **Renamed Guidelines → Pitfalls** — aligns with best-practice section naming
- **Removed code fences** around the challenge procedure — replaced with a numbered list for consistency
- **Removed checkbox syntax** from acknowledgment form — replaced with plain bullets (checkboxes imply interactivity)
- **Condensed prose throughout** — eliminated redundant phrasing (e.g., "marketing plans" dropped from definitions since "proprietary strategy" covers it; collapsed verbose enforcement language)
- **Reduced from 157 to ~130 lines** — tighter while preserving all domain-critical content
