---
name: customs-protest-form19
title: CBP Form 19 — Protest of Customs Decision
description: Drafts CBP Form 19 protests under 19 U.S.C. § 1514 and 19 C.F.R. Part 174 challenging tariff classification, valuation, origin, and trade preference decisions. Use when drafting customs protests, contesting liquidation decisions, or preparing Form 19 filings within the 180-day jurisdictional deadline.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/customs-protest-form19
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: trade
language: en
tags: [drafting, pleading]
---

# CBP Form 19 — Protest of Customs Decision

Draft a filing-ready protest preserving administrative and Court of International Trade review rights under 19 U.S.C. § 1514.

## Prerequisites

Gather before drafting:

1. **Entry docs** — CF-7501 summaries, invoices, bills of lading (entry numbers, port codes, dates)
2. **CBP decision docs** — CF-29 notices, liquidation notices, ruling letters with exact dates
3. **Merchandise specs** — technical data sheets, material composition, HTS classifications (assigned and claimed)
4. **Deadline check** — confirm within 180 days of liquidation/decision per § 1514(c)(3)
5. **Standing proof** — importer of record status, consignee designation, or POA for agents/brokers

## Quick Start

1. Extract entry data and CBP decision details from uploaded documents
2. Verify 180-day deadline — flag any timeliness risk before proceeding
3. Identify dispute type (classification, valuation, origin, preference, AD/CVD)
4. Draft each Form 19 section per the output structure below
5. Attach evidentiary exhibits with descriptions
6. Mark unverified citations with [VERIFY]

## Document Extraction

Search uploads for:

| Data Point | Source |
|---|---|
| 11-digit entry number(s) | CF-7501, CBP correspondence |
| Port code (3-digit) + name | Entry documents |
| Entry date, liquidation date | CF-29, liquidation notice |
| CBP-assigned HTSUS classification | CBP ruling/notice |
| Declared vs. assessed value | Entry summary, CF-29 |
| CBP-determined country of origin | CBP decision |
| Verbatim CBP decision language | Decision letters, CF-29 |

## Output Structure

### 1. Protestant Identification

- Full legal name (including DBA), address with 9-digit ZIP
- Entity type + state of formation
- Standing basis: importer of record / consignee / owner / authorized agent
- If agent: POA reference, broker license number

### 2. Entry Identification

Per contested entry:
- 11-digit entry number, port code + name
- Date of entry (MM/DD/YYYY), date of liquidation/reliquidation
- All CBP correspondence by document type, date, reference number

For consolidated protests (19 C.F.R. § 174.33): define scope of entries covered.

### 3. Contested Decision

Specify the exact determination challenged:

| Dispute Type | Required Detail |
|---|---|
| **Classification** | CBP-assigned HTSUS (chapter/heading/subheading/suffix) + duty rate |
| **Valuation** | Declared value, CBP value, adjustments, valuation method |
| **Country of origin** | CBP-determined origin, rules of origin framework |
| **Trade preference** | Program (USMCA, GSP, etc.), denial basis |
| **AD/CVD** | Order number, assessment rate, scope determination |

State when/how CBP communicated the decision to establish timeliness.

### 4. Claim for Relief

Frame as affirmative legal assertion:

- **Classification**: Correct HTSUS (8-digit subheading + 10-digit statistical) + duty rate
- **Valuation**: Correct method per § 1401a hierarchy, value with calculations
- **Origin**: Correct country + governing rule (substantial transformation / tariff shift / RVC)
- **Preference**: Program + qualification basis

### 5. Legal and Factual Argument

**Merchandise description** — material composition (percentages), manufacturing method, physical characteristics, functional capabilities, end use, industry standards.

**Classification disputes:**
1. Apply GRI in sequence
2. Analyze HS Explanatory Notes (persuasive, not binding)
3. Cite HQ/NY ruling letters — distinguish adverse rulings on facts
4. Cite CIT and Federal Circuit precedent with pinpoint citations

**Valuation disputes:**
1. Establish transaction value eligibility (sale for exportation, no related-party influence, no indeterminate conditions)
2. Address each § 1401a(b)(1) addition (packing, commissions, assists, royalties, resale proceeds)
3. If alternative method: explain transaction value failure, demonstrate next statutory method

**All disputes:**
- Distinguish CBP's cited authority
- Reference documentary evidence (technical literature, expert opinions, lab results, manufacturing docs)

### 6. Evidentiary Exhibits

List each with description: data sheets, expert reports/affidavits, prior CBP rulings on identical/similar merchandise, CIT decisions, industry publications, manufacturing documentation.

### 7. Signature Block

Include name, title, entity, date, contact info. If representative: identify principal, broker license or bar admission. Add 18 U.S.C. § 1001 certification statement.

## Critical Checks

- **180-day deadline is jurisdictional** — verify before drafting; flag risk prominently
- File at entry port or designated protest processing center
- Comply with 19 C.F.R. § 174.13 content requirements
- Preserve all arguments for CIT review — do not concede unnecessarily
- For related-party transactions, address § 1401a(b)(2)(B) relationship test proactively
- Protest denial triggers 180-day CIT action window under 28 U.S.C. § 2636(a)
- Use 19 C.F.R. § 174.14 for further review if initial protest denied
- Mark any unverified legal citation with [VERIFY]
