---
name: gsa-schedule-contract
title: GSA Schedule Contract
description: 'Drafts FAR/GSAR-compliant GSA Schedule (MAS/FSS) contracts with clause matrices, SIN scope, pricing/PRC/EPA mechanics, IFF reporting, TAA, Section 508, cybersecurity, and subcontractor flow-downs. Use when drafting or reviewing GSA Schedule contracts, MAS solicitations, SIN crosswalks, price lists, or FAR/GSAR clause sets. Triggers: GSA Schedule, MAS, SIN, FAR 52.212, GSAR 552.238, IFF, PRC, EPA, TAA, Section 508, FedRAMP.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/gsa-schedule-contract
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
---

# GSA Schedule Contract

Draft an execution-ready GSA Schedule contract with verified FAR/GSAR clause set, pricing framework, and compliance obligations.

## Prerequisites

Collect before drafting:

- **Contractor identity**: SAM legal name, UEI, CAGE, DBA(s), address, authorized signatory
- **Solicitation**: current MAS solicitation version, clause list, class deviations
- **SINs**: awarded SINs with descriptions; legacy-to-MAS crosswalk if applicable
- **Pricing**: Commercial Sales Practices, Basis of Award, negotiated discounts, Authorized Price List
- **IFF**: current rate, reporting portal, cadence
- **TAA**: country of origin data, substantial transformation analyses
- **IT accessibility**: VPAT/ACR if IT in scope
- **Cybersecurity**: NIST, FedRAMP, CUI requirements if applicable
- **Reps/certs**: size, socioeconomic, FAR 52.204-24/25
- **Subcontractors**: list and required flow-down terms

## Contract Structure

Use this section order:

1. Cover Sheet / Contract Summary
2. Parties and Authority
3. Contract Period and Effective Dates
4. Schedule Designation and Scope
5. SINs and Scope Details
6. Ordering Procedures and Order-Level Terms
7. Pricing, Discounts, and Authorized Price List
8. Price Reductions (PRC) and Notifications
9. Economic Price Adjustment (EPA) — if applicable
10. Industrial Funding Fee (IFF) and Sales Reporting
11. Trade Agreements Act (TAA)
12. IT Accessibility (Section 508) — if applicable
13. Cybersecurity and Incident Reporting — if applicable
14. Subcontracting and Flow-Down Requirements
15. Contract Administration and Modifications
16. Audit Rights and Record Retention
17. Disputes and CDA Clause
18. Delivery, Performance, QA, and Warranties
19. Representations and Certifications
20. Attachments and Incorporated Documents

## Required Tables

**Cover Sheet** — contract number, contractor name/UEI/CAGE, schedule designation, awarded SINs, base/option periods, CO and contractor POC. Source each field (GSA, SAM, Solicitation, Award, Contractor).

**SIN Scope** — per SIN: current title (verbatim from solicitation), contractor offerings, scope limits, certifications.

**Legacy SIN Crosswalk** (if applicable) — legacy SIN → current MAS SIN with in/out-of-scope confirmation.

**Authorized Price List** (appendix) — per item: SIN, item/service, part/service ID, unit, GSA price, commercial price, discount %, MOQ, lead time.

**TAA Compliance** — per item: country of origin, TAA designated (Y/N), substantial transformation basis (CBP ruling/analysis).

**Section 508** (if IT scope) — per product: VPAT/ACR version, conformance level, exceptions.

**Cybersecurity** (if applicable) — CUI handling (NIST SP 800-171), FedRAMP auth level, incident reporting process.

**Clause Matrix** — all clauses incorporated by reference: clause number, title, date, applicability. Must include at minimum: FAR 52.212-4, FAR 52.212-5, GSAR 552.238-74, GSAR 552.238-81, GSAR 552.238-82.

**Subcontractor Flow-Downs** — per clause: flow-down required (Y/N), subcontract type (supply/service/IT).

## Pricing and IFF Blocks

Insert from current GSAR clause text — do not paraphrase:

**Pricing relationship**: Basis of Award customer/category, commercial discount to Basis of Award, negotiated GSA discount, pricing relationship rule.

**PRC** (GSAR 552.238-81): clause number/title/date, notification window in days, effective date rule.

**EPA** (if applicable): clause number/title/date, index name, cap (max %/period), required documentation, CO modification approval.

**IFF** (GSAR 552.238-74): rate (verify current), reporting portal name, cadence with due date rule, pass-through prohibition — IFF never separately charged to ordering agencies.

## Administrative Provisions

- Modifications only by CO-signed written mods
- Audit rights per applicable FAR/GSAR clauses
- Record retention per clause-specified duration
- Disputes: FAR 52.233-1 with CDA references

## Compliance Checks

- Verify all FAR/GSAR clause numbers, titles, and dates against official sources; mark `[VERIFY]` when uncertain.
- Never assume IFF rate, period lengths, or PRC notification windows — insert from current solicitation/GSAR.
- Use incorporation by reference unless solicitation requires full text.
- Use UEI only — DUNS is obsolete.
- TAA, Section 508, cybersecurity, and PRC must use current clause text verbatim; do not paraphrase.
- If solicitation or mass modification conflicts with legacy terms, flag the conflict and adopt the current requirement with citation.
- IFF must not appear as a separate line item to ordering agencies.
