---
name: ny-nassau-dc-codearranger
title: Nassau County District Court
description: Use when drafting or filing in Nassau County District Court — the Long Island District Court (Uniform District Court Act) that handles civil actions up to $15,000, summary proceedings (landlord-tenant), small claims, and misdemeanor and violation criminal matters. Triggers include 'Nassau District Court', 'Nassau County District Court', '99 Main Street Hempstead', 'First District Hempstead', 'Nassau Landlord Tenant Part', 'Nassau Small Claims Part', 'Nassau commercial claims', 'UDCA', 'Uniform District Court Act'. Covers Nassau District Court's six geographic districts, the Civil Part / Landlord-Tenant Part / Small Claims Part / Commercial Claims Part division of business, 22 NYCRR Part 212 format compliance, and the UDCA's $15,000 jurisdictional ceiling — the principal pro se debt- defense and L&T forum in Nassau County. NOT a substitute for Nassau Supreme Court (`ny-nassau`); the District Court is a separate court with its own filing system.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-nassau-dc
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Nassau County District Court

> **NOT LEGAL ADVICE.** Verify the specific District's local
> rules and the assigned Judge's Part Rules before every
> filing.

## At a glance

- **Court**: Nassau County District Court — established under
  the **Uniform District Court Act (UDCA)** and codified
  procedural rules at **22 NYCRR Part 212**
- **Civil jurisdiction**: claims up to **$15,000** (UDCA
  § 202)
- **Small claims**: up to **$5,000** in informal proceedings
  (UDCA § 1801)
- **Commercial claims**: up to **$5,000** in the Commercial
  Claims Part (UDCA § 1801-A; available to
  corporations / LLCs / partnerships that cannot use small
  claims)
- **L&T (summary proceedings)**: no monetary cap on rent
  arrears; RPAPL Article 7 procedure
- **Headquarters**: **99 Main Street, Hempstead, NY 11550**
  (First District / Main Courthouse)
- **E-filing**: **NYSCEF available** for civil matters in
  Nassau District Court (one of the first District Courts to
  expand NYSCEF coverage). L&T filings are case-by-case.

## Geographic districts

Nassau District Court is divided into six geographic
districts. Each has its own courthouse; choice of district
is determined by where the action arose or where the
defendant resides (UDCA § 213).

| District | Coverage area | Courthouse |
|---|---|---|
| **First District** | All of Nassau County (countywide civil and L&T) | 99 Main Street, Hempstead |
| **Second District** | North Hempstead Town | 435 Plandome Road, Manhasset |
| **Third District** | Oyster Bay Town | 99 Main Street, Hempstead (Third District Part) |
| **Fourth District** | Hempstead Town | 99 Main Street, Hempstead (Fourth District Part) |
| **Fifth District** | Long Beach + Atlantic Beach + Lido Beach | Long Beach City Court (shared facility) |
| **Sixth District** | City of Glen Cove | Glen Cove City Court (shared facility) |

> **Filing tip:** Most civil and L&T filings route to the
> First District unless the action is town-bound (e.g., a
> Hempstead Town code violation in the Fourth District). When
> in doubt, the **Nassau County Clerk's office routes filings
> to the correct District** based on the defendant's address.

## Parts division

The court operates several specialized **Parts**:

- **Civil Part** — debt-collection and contract actions up to
  $15,000; small-claims actions up to $5,000
- **Landlord-Tenant Part** — RPAPL Article 7 summary
  proceedings (nonpayment + holdover); the Long Island analog
  to NYC Housing Court
- **Small Claims Part** — informal proceedings for natural
  persons; no formal pleadings required; trial is in two
  weeks
- **Commercial Claims Part** — same as small claims but for
  entities; UDCA § 1801-A
- **Traffic and Parking Violations Agency (TPVA)** — TPVA
  (Hempstead) handles parking and certain traffic; criminal
  Parts handle DWI / misdemeanors

## Distinctives

### Pro se debt-defense is the norm

Nassau District Court is the **principal pro se debt-defense
forum** in Nassau County for debts under $15,000. Pro se
defendants routinely file Answers and appear at "consumer
credit calendar calls." The 2022 **Consumer Credit Fairness
Act (CCFA)** applies in full — the heightened pleading
requirements under CPLR 3015(e) (account statements,
itemization) and the default-judgment scrutiny under 22 NYCRR
§ 202.27-a are enforced at the District Court level the same
way they are in Civil Court of the City of New York and
Supreme Court. Note that the 3-year SOL on consumer-credit
actions (CPLR 214-i, added by the CCFA) shortens many
District Court debt cases.

### Long Island L&T forum

The **Landlord-Tenant Part** is the suburban analog to NYC
Housing Court. Filings under RPAPL Article 7 (nonpayment +
holdover) are the highest-volume case category after debt
collection. Procedure tracks NYC Housing Court's structure:
**14-day rent demand** notice as a precondition to nonpayment
proceedings (RPAPL § 711(2), 14-day rule from the 2019 HSTPA);
**30-day notice** to terminate for month-to-month tenancies
under 1 year (Real Property Law § 232-a / § 232-b, with the
2019 HSTPA expansion to 30 / 60 / 90 days based on tenancy
length); good-cause-eviction protection where adopted by the
municipality (2024 Good Cause Eviction Law applies to several
Nassau County municipalities by local option).

### Discovery is limited

CPLR Article 31 disclosure applies in name, but **District
Court Civil Part practice is faster + leaner**. Document
demands and interrogatories are uncommon outside the formal
pre-trial conference; the court expects most cases to resolve
at the first or second appearance.

### Notable: NYSCEF e-filing has expanded

Nassau District Court is one of the **first District Courts**
to fully roll out NYSCEF for civil filings. Confirm the case
type is e-fileable (most consumer-credit and contract actions
are; L&T and TPVA are not yet). When NYSCEF is unavailable,
filings go to the District Court Clerk in person or by mail
at 99 Main Street, Hempstead.

## Filing checklist

1. **Summons + Complaint**: UDCA § 401 / 402 — short-form
   summons + complaint with the **$45 filing fee** (UDCA
   § 1911(1))
2. **Service**: CPLR 308 / 312 within UDCA § 403 service
   period (typically 120 days)
3. **Answer**: defendant has **30 days** from service in the
   Civil Part (CPLR 320(a) / UDCA Article 4)
4. **Pre-trial conference**: routinely scheduled within
   60-90 days of issue being joined
5. **Trial date**: court tracks toward trial 6-12 months from
   filing in most cases

> **Format compliance:** 22 NYCRR Part 212 governs filings
> here. Margins, page size, caption format, and verification
> requirements mirror 22 NYCRR Part 202 with District Court-
> specific adjustments. Use `ny-statewide-format` as the
> baseline and verify Part 212 deviations before filing.

## Composition with other ny- skills

- `ny-statewide-format` — baseline format (22 NYCRR Part 202)
  with Part 212 adjustments
- `ny-county-courts` — the broader roll-up that this skill
  refines
- `ny-nassau` — Nassau Supreme Court (separate court; over
  $15,000)
- `ny-discovery` — CPLR Article 31 mechanics (District Court
  Civil Part uses these in modified form)
- `ny-first-30-days` — Answer / pre-answer motion triage
- `ny-consumer-debt` — CCFA pleading + default scrutiny
  applies in Civil Part
- `ny-landlord-tenant` — RPAPL Article 7 Long Island L&T Part
  procedure (cross-references this skill's L&T Part)
- `ny-pro-se` — pro se framework (Nassau District Court is
  high-volume pro se)
- `ny-file-packet` — assembling a District Court filing
  packet for NYSCEF or hand filing

## Pro-se resources

- **Nassau County Bar Association Lawyer Referral Service**:
  516-747-4070
- **Nassau / Suffolk Law Services (NSLS)** — civil legal aid
  for low-income tenants and consumers
- **Hofstra Law Family Court Litigation Clinic** — referrals
  for related Family Court matters
- **Court of Original Jurisdiction Self-Represented Office**
  at 99 Main Street, Hempstead
