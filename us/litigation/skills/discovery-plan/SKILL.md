---
name: discovery-plan
title: Joint Discovery Plan & Proposed Scheduling Order
description: Drafts Joint Discovery Plans and Proposed Scheduling Orders under FRCP 26(f) or state equivalents. Analyzes pleadings, court requirements, and case complexity to produce discovery timelines, ESI protocols, privilege procedures, and scheduling deadlines. Use when preparing Rule 26(f) reports, proposed scheduling orders, case management plans, or discovery frameworks after meet-and-confer.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/discovery-plan
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [drafting, pleading]
---

# Joint Discovery Plan & Proposed Scheduling Order

Produces a court-ready Joint Discovery Plan and Proposed Scheduling Order reflecting FRCP 26(f) meet-and-confer results while protecting client interests.

## Required Inputs

1. **Complaint, answer, amended pleadings** — all claims, defenses, counterclaims
2. **Meet-and-confer details** — date, participating attorneys
3. **Court information** — court/division, case number, judge, local rules, standing orders
4. **Initial disclosures** — if exchanged
5. **Existing court orders** — CMC minutes, scheduling preferences, model templates

## Workflow

### 1. Analyze Discovery Scope

For each claim/defense, identify:
- Elements requiring proof and key disputed facts
- Document types, custodians, and witness categories
- Proportionality under Rule 26(b)(1): importance of issues, amount in controversy, relative access, party resources

### 2. Draft Document Sections

| Section | Contents |
|---|---|
| Caption & Introduction | Court/division, case number, parties, cite to FRCP 26(f) or state equivalent, meet-and-confer date and counsel |
| Discovery Subjects & Scope | Claim-by-claim discovery needs tied to legal elements and factual disputes |
| ESI Protocol | Production formats, metadata, search terms, TAR/predictive coding, preservation |
| Privilege Procedures | FRE 502(d) clawback, privilege log requirements, timing |
| Discovery Limitations | Depositions, interrogatories, RFAs, time/geographic/custodian limits |
| Phased Discovery | If warranted: threshold issues, liability/damages bifurcation, multi-defendant sequencing |
| Proposed Schedule | All milestone deadlines in tabular format |
| Signature Blocks & Certificate of Service | All counsel of record with bar numbers, firm, address, phone, email |

### 3. Set ESI Protocol

- **Format**: Native for spreadsheets/databases; searchable PDF or TIFF+load files for static documents
- **Metadata**: Author, recipient, dates created/modified, custodian, plus case-specific fields
- **Email**: Preserve threading and family relationships
- **Search**: Exchange proposed terms → validate against samples → refine precision/recall; specify TAR if used
- **Preservation**: Custodians, data sources (email, drives, cloud, mobile, social), time period, departing employee protocols
- **Cost allocation**: Burden-shifting for disproportionate costs, backup tapes, forensic imaging
- **Deduplication**: Global vs. custodian-level

### 4. Define Privilege Framework

| Element | Provision |
|---|---|
| Clawback order | FRE 502(d) — inadvertent production does not waive privilege |
| Clawback procedure | Written notice with specificity + privilege basis → return/destroy within 5–10 business days |
| Receiving party duty | Assert within 30 days or before use in deposition/filing |
| Privilege log fields | Date, author, recipients, document type, subject description |
| Log timing | 30 days after each production (or rolling) |
| Categorical exclusions | Consider post-litigation counsel-client and pure legal advice communications |
| Common interest/JDA | Address if applicable |

### 5. Set Discovery Limitations

| Type | Presumptive Limit | Rule |
|---|---|---|
| Depositions per side | 10 (adjust for complexity) | Rule 30(a)(2)(A)(i) |
| Deposition duration | 7 hours/deponent | Rule 30(d)(1) |
| Interrogatories | 25 including subparts | Rule 33(a)(1) |
| RFAs | 25–50 (stipulate) | Rule 36 |
| Contention interrogatories | Deferred until close of fact discovery | — |

Include format (in-person/remote), location protocols, and cost allocation for reporters/videographers.

### 6. Build Proposed Schedule

Work backward from anticipated trial date:

| Milestone | Guideline |
|---|---|
| Join parties | +90–120 days from order |
| Amend pleadings | +120–180 days |
| Fact discovery closes | +9–12 months (moderate complexity) |
| Plaintiff expert reports | +30–60 days after fact discovery |
| Defendant expert reports | +60–90 days after plaintiff reports |
| Rebuttal expert reports | +30–45 days after defendant reports |
| Expert depositions complete | +30–45 days after final reports |
| Dispositive motions | +30–45 days after expert discovery |
| Responses | +21–30 days |
| Replies | +14–21 days |
| Motions in limine / jury instructions | –30–45 days before trial |
| Final pretrial conference | –14–30 days before trial |
| Trial | ~18–24 months from order (moderate) |

Adjust for party count, document volume, expert count, jurisdictional constraints, court availability.

### 7. Add Modification Provisions

- Fact/expert extensions: by stipulation with court approval if they do not affect dispositive motion or trial dates
- Dispositive/trial changes: court approval, good cause required
- Meet-and-confer required before any modification request
- Optional status conferences at key intervals

### 8. Assess Phased Discovery

Consider phasing when:
- Jurisdictional or limitations issues are threshold
- Liability and damages are naturally bifurcated
- Multi-defendant cases have distinct factual tracks
- Sampling custodians can inform broader discovery scope

Specify clear phase triggers, transition procedures, and right to modify if phasing proves unworkable.

## Pitfalls & Checks

- Cite FRCP 26(f) or state equivalent in introduction; confirm local rule and standing order compliance
- Ground every discovery subject in specific pleading allegations — no generic categories
- Use court-adoptable format ("IT IS HEREBY ORDERED" or separate proposed order)
- Number all paragraphs for easy reference
- Verify all deadlines are internally consistent and comply with local rules
- Check for model plans or templates required by the specific court/judge
- Include certificate of service compliant with applicable rules
- Tone: cooperative where appropriate, protective of client interests where necessary
