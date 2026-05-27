---
name: import-compliance-manual
title: Import Compliance Manual
description: 'Drafts a U.S. import compliance manual demonstrating reasonable care under 19 U.S.C. § 1484. Covers HTS classification, customs valuation (19 U.S.C. § 1401a), country of origin, recordkeeping (19 C.F.R. Part 163), PGA compliance, internal audit, training, and corrective action. Use when creating or overhauling an importer-of-record compliance program, preparing for a CBP focused assessment, or establishing written reasonable-care procedures. Trigger keywords: import compliance manual, customs compliance program, CBP audit preparation, reasonable care, IOR compliance.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/import-compliance-manual
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
tags: [checklist, drafting]
---

# Import Compliance Manual

Drafts a U.S. customs import compliance manual that serves as an operational policy document and evidence of reasonable care under 19 U.S.C. § 1484.

## Prerequisites

1. **Company profile** — importer name, EIN/CBP number, principal ports, product categories
2. **Organizational chart** — compliance owner (CCO, committee, or import manager)
3. **Trade programs** — FTAs (USMCA, bilateral), GSP, drawback, FTZ, TIB, carnet
4. **PGA exposure** — applicable agencies (FDA, USDA/APHIS, EPA, CPSC, etc.)
5. **Existing procedures** — current SOPs, broker agreements, classification databases

## Output Structure

Generate numbered chapters with sub-sections. Include version control block, table of contents, and executive signature line.

### Chapter 1 — Corporate Policy Statement

| Element | Content |
|---|---|
| Statutory basis | Tariff Act of 1930, as amended; all CBP-administered regulations |
| Reasonable care | Acknowledge 19 U.S.C. § 1484 standard |
| Zero tolerance | No willful violations; cite civil/criminal penalties |
| Scope | All entries, ports, entry types, values |
| Responsibility | Named executive or committee with defined authority |
| Covered parties | Employees, agents, brokers, forwarders, third parties |
| Review cycle | Annual minimum; triggered by regulatory or business change |

### Chapter 2 — HTS Classification

Assign a designated classifier with technical/legal authority.

**Methodology (hierarchical):** identify product characteristics/end use → apply GRI 1–6 → consult Explanatory Notes, CROSS rulings, court decisions → document rationale in classification worksheet.

**Per-SKU documentation:** technical specs, lab reports, written GRI analysis with heading/subheading cite, supporting rulings, classification database entry.

**Binding rulings:** submit via CROSS when uncertain or duty impact is significant; implement on receipt; track expiration.

**Monitoring:** review CBP ruling updates, USITC amendments, CIT/CAFC decisions; reassess affected SKUs within 30 days of material change.

**Broker disagreements:** IOR retains responsibility regardless of broker recommendation; escalate unresolved disputes to counsel.

### Chapter 3 — Customs Valuation

Primary method: transaction value under 19 U.S.C. § 1401a(b).

**Pre-entry review elements:**

| Item | In Value? | Note |
|---|---|---|
| Freight & insurance | Per Incoterms | CIF yes / FOB no |
| Packing costs | Yes | — |
| Buying commissions | No | — |
| Selling commissions | Yes | — |
| Assists | Yes | Prorate per 19 C.F.R. § 152.103(e) |
| Royalties/license fees | Yes if condition of sale | — |
| Resale proceeds to seller | Yes if contractual | — |

**Related-party transactions (19 C.F.R. § 152.102(g)):** document relationship (ownership ≥ 5%) → circumstances-of-sale analysis → test values if price influenced → maintain transfer pricing studies.

**Hierarchy when transaction value unavailable:** identical → similar goods → deductive → computed → fallback (§ 1401a(f)).

**Post-entry corrections:** CF-7501 amendment or prior disclosure under 19 U.S.C. § 1592(c)(4); involve counsel before submission.

### Chapter 4 — Country of Origin

**Non-preferential (marking — 19 U.S.C. § 1304):** apply substantial transformation test (name, character, use); identify ultimate purchaser; textiles/apparel use Section 334 URAA rules [VERIFY for specific fiber/yarn/fabric categories].

**Preferential origin documentation:**

| Program | Certificate | Key Rule |
|---|---|---|
| USMCA | Importer/exporter/producer certification | Tariff shift + RVC or process rule |
| CAFTA-DR / bilateral FTAs | Certificate of origin | Agreement-specific PSR |
| GSP | Supplier affidavit (no formal cert) | 35% RVC; substantial transformation |

**Supplier validation:** obtain certification before first entry; risk-tiered audits (high-value = annual, low-risk = biennial); reassess on sourcing/BOM change.

**Per-product docs:** BOM with input origins/values, manufacturing process description, FTA certification or affidavit, RVC worksheet if applicable.

### Chapter 5 — Recordkeeping

**Authority:** 19 U.S.C. § 1509; 19 C.F.R. Part 163; "(a)(1)(A) list."

| Record Type | Retention |
|---|---|
| Entry records (CF-7501, invoices, BOL, packing lists) | 5 years from entry |
| Drawback records | 3 years after payment or liquidation |
| FTZ records | 5 years from admission |
| Trade preference support | 5 years from claim |

Designate a Part 163 recordkeeper as CBP contact (30-day response). Electronic records must be unalterable with audit trail. Broker/forwarder contracts must require Part 163 compliance and grant record access on demand.

### Chapter 6 — Partner Government Agency Compliance

Build a PGA matrix per product category mapping agency, statutory basis, key requirement, and ACE data element. Common agencies: FDA (food/drugs/devices), USDA (APHIS, FSIS), EPA (TSCA, FIFRA, CAA), CPSC (CPSA, CPSIA).

**Pre-importation checklist:** permits/licenses obtained; PGA data transmitted via ACE Message Set; import alerts checked; admissibility docs on file before arrival.

**Enforcement response:** designate lead for refusals/holds/detentions; determine within 5 business days whether to cure, re-export, or destroy.

### Chapter 7 — Internal Audit

**Frequency:** annual comprehensive; focused review on new product/supplier/trade lane.

**Scope:** HTS accuracy (sample ≥ 50 entries or 10%), valuation completeness, origin/FTA claims, recordkeeping retrieval, PGA/ACE accuracy, trade program integrity, training completion.

| Severity | Definition | Action |
|---|---|---|
| Critical | Revenue loss >$10K or ongoing violation | Immediate stop; prior disclosure evaluation; counsel |
| Significant | Systemic procedural failure | CAP within 30 days |
| Moderate | Isolated documented error | Correct within 90 days |
| Observation | Improvement opportunity | Next planning cycle |

**Prior disclosure trigger:** evaluate under § 1592(c)(4) for any Critical finding with duty underpayment; disclose before CBP investigation commences. Engage outside counsel for privilege-protected audits.

### Chapter 8 — Training

| Role | Initial | Annual | Advanced Topics |
|---|---|---|---|
| Import manager | 8 hrs | 4 hrs | GRI, valuation, FTA RVC |
| Purchasing | 4 hrs | 2 hrs | Assists, supplier origin |
| Product development | 4 hrs | 2 hrs | Classification at design stage |
| Logistics | 4 hrs | 2 hrs | Entry, PGA, recordkeeping |
| Senior management | 2 hrs | 1 hr | Penalties, IOR obligations |

**Core content:** IOR obligations/liability, classification/valuation/origin overview, civil penalties (§ 1592) and criminal exposure, role-specific manual procedures.

**Records:** attendance log, version-controlled materials, post-training assessment, completion certificates (retain 5 years).

**Off-cycle triggers:** regulatory change, audit deficiency, new product category, role change.

### Chapter 9 — Corrective Action

1. **Contain** — halt affected transactions; interim controls within 2 business days
2. **Investigate** — root cause analysis; scope (isolated vs. systemic)
3. **Evaluate disclosure** — apply § 1592(c)(4) with counsel; file before CBP investigation if warranted
4. **Remediate** — written CAP with named owners and firm deadlines
5. **Post-entry filing** — CF-7501 amendment, supplemental info, or protest
6. **Verify** — 100% review for 90 days or 3 clean audits
7. **Communicate** — targeted training; updated SOPs to affected personnel
8. **Report** — status to management; escalate systemic failures to board

**Tracking log:** Issue ID, discovery date, root cause, severity, owner, actions, target date, completion date, verification result.

### Document Administration

| Element | Requirement |
|---|---|
| Version control | Version number, effective date, revision history |
| Executive approval | CCO/CEO signature; annual re-certification |
| Distribution | Named recipients; acknowledgment signatures |
| Review triggers | Annual; regulatory change; CBP inquiry; audit finding |
| CBP readiness | Suitable for production on request |

## Guidelines

- **Reasonable care**: every procedure must be defensible under § 1484; document the *why*, not just the *what*
- **Broker reliance**: using a broker does not transfer IOR liability; procedures must confirm company retains classification and valuation responsibility
- **Jurisdiction**: U.S.-specific (CBP, ACE); adapt PGA section to actual product mix — omit inapplicable agencies
- **Penalty exposure**: § 1592 penalties range from 20% (negligence) to 4× unpaid duties (fraud); manual existence is a mitigation factor
- **Verify citations**: confirm current HTS edition, active FTA rules, and Section 301/232 overlays at drafting time [VERIFY current Section 301 list applicability]
- **Attorney review**: counsel should review before finalizing; privilege may attach to counsel-directed assessments

---

Key changes from the original:
- **266 → ~160 lines** — ~40% token reduction
- **Frontmatter**: added multi-line `description` with trigger keywords; removed `memo` tag (not applicable to a manual)
- **Chapter 6 (PGA)**: collapsed the 9-row agency matrix into a concise instruction to build a per-product PGA matrix, listing common agencies inline — the agent generates the matrix at draft time for the client's actual product mix rather than templating all possible agencies
- **Chapters 2, 5, 8**: converted checkbox lists to inline prose or compact bullet format
- **Removed**: horizontal rule separators between chapters, redundant "Required Content" column headers, verbose checklist formatting throughout
- **Preserved**: all statutory citations, retention periods, valuation hierarchy, severity matrix, corrective action protocol, training hours matrix, and `[VERIFY]` markers
