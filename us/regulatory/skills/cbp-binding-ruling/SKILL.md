---
name: cbp-binding-ruling
title: CBP Binding Ruling Request (19 CFR Part 177)
description: Drafts U.S. Customs and Border Protection binding ruling requests under 19 CFR Part 177 for tariff classification, valuation, origin, and marking determinations. Trigger when input mentions "binding ruling," "CBP ruling request," "19 CFR Part 177," "classification request," "HTSUS analysis," "transaction value," "country of origin," or "marking for import."
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/cbp-binding-ruling
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
tags: [drafting, letter, research]
---

# CBP Binding Ruling Request (19 CFR Part 177)

Produces a complete, exhibit-backed binding ruling request package for pre-filing U.S. import treatment decisions on classification, valuation, origin, or marking.

## Prerequisites

1. Confirm the matter is a U.S. import treatment determination appropriate for 19 CFR Part 177.
2. Identify requesting party's role and authority (importer / prospective importer / foreign manufacturer / authorized representative).
3. Gather transaction evidence: supply chain docs, technical specs, invoices, contracts, prior entries, prior CBP communications.
4. Check for related-party pricing, royalty/assist/profit-sharing elements, or prior rulings on similar goods.
5. Secure signatory authority; confirm POA scope if acting through counsel/broker.
6. Identify any confidential business information requiring redaction.
7. Verify no pending protest/litigation or excluded-request conflict with Part 177 scope.

## Quick Start

1. Screen scope and jurisdiction → validate determination type against Part 177 authority.
2. Draft requester/standing section → collect merchandise record → document transaction chain.
3. Isolate legal questions (one per issue) → build authority-stack analysis.
4. Assemble exhibit index → add certification and confidentiality block.
5. Run quality gates → finalize output in template order.

## Workflow

### 1. Scope and Jurisdiction Screen

Validate request type; flag and reframe non-Part 177 matters to non-binding inquiry.

| Determination | Authority | Required Facts |
|---|---|---|
| Classification | 19 CFR Part 177, HTSUS + GRI 1–6 | Composition, function, process, alternatives rejected |
| Valuation | 19 USC 1401a, 19 CFR Part 152 | Related-party analysis, transfer pricing, royalties/assists/proceeds |
| Origin/Marking | 19 CFR Part 102 (or agreement appendices) | Manufacturing operations, tariff shift, criteria applied |
| Other | Related Part 177 authority | Issue isolation and requested relief [VERIFY] |

### 2. Requester and Standing

- Full legal name, principal business address, contact person
- Relationship to merchandise/importation
- Legal authority basis; POA summary if applicable
- Distinguish roles when requester ≠ importer of record

### 3. Merchandise Record

| Field | Detail |
|---|---|
| Product name | Commercial and technical designation |
| Composition | Material IDs and percentages by weight/volume |
| Process | Step-by-step transformation from origin materials to finished goods |
| Specs | Weight, dimensions, capacity, tolerances, performance |
| Use | End-user function, market segment, substitutability |
| Standards | ASTM/ISO/FDA/FCC references with citations |
| Samples | Photos/specimens plan with exhibit mapping |

For classification: state full 10-digit HTSUS with GRI sequencing, Explanatory Notes, and exclusionary analysis.

### 4. Transaction Structure and History

- Full supply chain: sourcing → processing → manufacturing → export → shipment → U.S. entry
- All parties and relationship mapping; flag related-party status under 19 CFR 152.102(g)
- Pricing: Incoterms, currency/terms, royalties, assists, proceeds of resale
- Prior import history if any: entry numbers, ports, dates, declared HTSUS/values, audit outcomes, prior rulings with factual changes explained

### 5. Legal Questions

One question per discrete issue. No compound questions or non-determinative hypotheticals. Sample forms (tailor to facts):

- Classification: "Whether merchandise is classifiable under subheading [____], HTSUS, as opposed to [alternative], based on [GRI path + facts]."
- Valuation: "Whether transaction value under 19 U.S.C. 1401a is acceptable where [relationship/royalties/assists] and whether [adjustment] is required under § 1401a(b)(1)(D)."
- Origin: "Whether country of origin for marking is [country] under 19 CFR Part 102 based on [tariff shift / substantial transformation]."

### 6. Legal Analysis

Build authority stack table:

| Issue | Controlling Authority | Support | Application |
|---|---|---|---|
| Classification | HTSUS, GRI 1–6 | HQ/NY rulings, ENs | Why heading is/is not met |
| Valuation | 19 USC 1401a; 19 CFR Part 152 | CBP rulings | Transaction value acceptability + adjustments |
| Origin/Marking | 19 CFR Part 102 | Rulings + technical evidence | Why origin rule is triggered |

Prior rulings: prioritize HQ over NY; distinguish adverse precedent with material differences; flag supersession/revocation before citing.

### 7. Exhibit Index

| Exhibit | Type | Relevance |
|---|---|---|
| Ex. 1 | Corporate authorization / POA | Standing and signatory authority |
| Ex. 2 | Technical specs / engineering data | Composition and manufacturing basis |
| Ex. 3 | Samples / photos | Physical characteristics |
| Ex. 4 | Commercial docs | Value and sale-structure support |
| Ex. 5 | Prior rulings / correspondence | Historical treatment |
| Ex. 6 | Expert / lab reports | Scientific support |

Include certifications for expert reports (identity, qualification, method, date).

### 8. Certification and Confidentiality

- Sworn certification: printed name, title, signature, date
- Confirm signer has authority and factual knowledge or reasonable basis
- 19 CFR 177.2(b)(7) confidentiality request: itemized identifiers, harm rationale, redaction plan for public version

### 9. Final Assembly

Template order:
1. Header and requester identification
2. Purpose and legal authority
3. Factual background
4. Transaction/merchandise description
5. Issues and questions presented
6. Applicable law and analysis
7. Requested determination
8. Attachments and index
9. Certification and signatures

## Quality Checks

- Every asserted fact has exhibit support; no unresolved references
- All citations current; revocation/supersession status verified
- Questions map one-to-one to requested determinations
- Routing to proper CBP office confirmed [VERIFY]
- Uncertain authority marked [VERIFY] before finalization

## Pitfalls

- **Scope creep**: never include penalty/reasonable-care advisories, litigation strategy, or non-customs policy questions.
- **Compound questions**: CBP may decline or partially answer; isolate each issue.
- **Stale rulings**: always check revocation/modification status before citing.
- **Unsupported claims**: no narrative assertions without source documents; separate facts from analysis.
- **Jurisdiction**: U.S. only; flag and adjust when trade-agreement or foreign-law layers apply.
