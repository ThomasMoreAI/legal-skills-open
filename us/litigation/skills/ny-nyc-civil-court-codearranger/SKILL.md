---
name: ny-nyc-civil-court-codearranger
title: Civil Court of the City of New York
description: Use when drafting or filing in the Civil Court of the City of New York — the separate trial court (Civil Court Act, NYC Charter § 2300 et seq.) handling civil actions up to $50,000 and small claims up to $10,000 across five borough branches. Triggers include 'NYC Civil Court', 'Civil Court of the City of New York', 'Civil Court small claims', 'CCEF', 'UCMS NYC', 'Consumer Credit Part', '$50,000 civil', '22 NYCRR § 208', '22 NYCRR § 202.27-a'. Covers five borough branches' filing protocols; Consumer Credit Part procedures (highest-volume debt-collection forum in state, ~150,000+ filings pre-CCFA); 22 NYCRR Part 208 / § 208.6-a default-scrutiny rule; UCMS / CCEF electronic-filing system (distinct from NYSCEF); and borough-specific scheduling. NOT a substitute for Supreme Court (separate jurisdictional ceiling + filing system).
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-nyc-civil-court
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Civil Court of the City of New York

> **NOT LEGAL ADVICE.** Verify the specific borough branch's
> local procedures + the assigned Judge's Part Rules before
> every filing.

## At a glance

- **Court**: Civil Court of the City of New York —
  established by the **NYC Civil Court Act** (Civil Court Act
  / NYC Charter § 2300 et seq.), procedural rules at
  **22 NYCRR Part 208**, separate trial court from Supreme
  Court
- **Civil jurisdiction**: claims up to **$50,000**
  (Civil Court Act § 202; CPLR 325(d) transfer back from
  Supreme Court if removed from CivCt)
- **Small Claims jurisdiction**: up to **$10,000** in
  informal proceedings (Civil Court Act § 1801)
- **Commercial Claims Part**: up to **$10,000** for entities
  that can't file in Small Claims (Civil Court Act § 1801-A)
- **Housing Part**: covered separately in `ny-nyc-housing-court`
  (RPAPL Article 7 summary proceedings, the largest L&T
  forum in the country)
- **E-filing**: **UCMS** (Universal Case Management System) /
  **CCEF** (Civil Court Electronic Filing) — **distinct from
  NYSCEF** used in Supreme Court / County Court. Mandatory
  for most consumer-credit matters in NY County and Bronx;
  expanding elsewhere.

## Five borough branches

Each branch operates independently with its own clerk's
office, calendar, and judge assignments. Filings route to
the borough where the cause of action arose or where the
defendant resides (Civil Court Act § 213).

| Borough | Courthouse | Address |
|---|---|---|
| **New York County** | NY County Civil Court | **111 Centre Street, NY NY 10013** |
| **Kings County** | Kings Civil Courthouse | **141 Livingston Street, Brooklyn NY 11201** |
| **Bronx County** | Bronx Civil Court | **851 Grand Concourse, Bronx NY 10451** |
| **Queens County** | Queens Civil Court | **89-17 Sutphin Boulevard, Jamaica NY 11435** |
| **Richmond County** | Richmond Civil Court | **927 Castleton Avenue, Staten Island NY 10310** |

> The Bronx and Queens Civil Court buildings physically share
> facilities with their respective Supreme Court Civil Term
> houses (851 Grand Concourse and 88-11 Sutphin Blvd) — the
> courts are still legally distinct.

## Parts division

NYC Civil Court runs a deep Parts structure. The principal
ones for civil practice:

- **Consumer Credit Part** (each borough) — the dedicated
  Part for consumer-debt collection actions; the
  highest-volume civil-litigation forum in the country.
  Calendar calls are routine; pro se debtors appear nearly
  exclusively pro se. Post-**2022 CCFA** the Part enforces:
  - **CPLR 3015(e)** heightened pleading
  - **22 NYCRR § 208.6-a** default-judgment scrutiny (the
    NYC Civil Court companion to § 202.27-a in Supreme
    Court)
  - **3-year SOL** under CPLR 214-i for consumer-credit
    actions
  - Mandatory notification-of-action mailing under CPLR
    308(six)
- **Civil Part** — general civil litigation up to $50,000;
  contract, tort, replevin, statutory claims
- **Small Claims Part** — informal proceedings; up to
  $10,000; no formal pleadings; the trial is by an
  arbitrator (with right to a "trial-de-novo" jury trial on
  request) and decided within a few weeks
- **Commercial Claims Part** — entity equivalent of small
  claims, up to $10,000
- **Housing Part** — RPAPL Article 7 summary proceedings;
  covered in `ny-nyc-housing-court`

## Distinctives

### NYC Civil Court is the primary consumer-debt forum in the state

By volume, NYC Civil Court Consumer Credit Parts hear more
debt-collection cases than the rest of New York's courts
combined. The 2022 CCFA was drafted specifically to address
abuses in this forum:

- Debt-buyer plaintiffs (Midland, Cavalry SPV, Velocity,
  Unifin, LVNV, Cach LLC) historically filed in NYC Civil
  Court with sparse complaints, obtained default judgments
  through sewer service, and enforced against bank accounts
  under CPLR Article 52.
- The CCFA's CPLR 3015(e) heightened pleading, 22 NYCRR
  § 208.6-a default scrutiny, and CPLR 214-i 3-year SOL
  collectively flipped the burden onto plaintiffs to prove
  chain of title + itemization + last-activity-date before
  default judgment.
- The Consumer Credit Part judges now routinely deny default
  judgments sua sponte when the CCFA documentation is
  missing.

### UCMS / CCEF — distinct e-filing from NYSCEF

NYSCEF (used in Supreme + County Court) and UCMS / CCEF
(used in NYC Civil Court) are **completely separate
systems**. A pro se litigant who has used NYSCEF in a
Supreme Court matter will need to register separately at
[nycourts.gov/courts/nyc/civil/efiling.shtml] for UCMS
access. Document types, exhibit handling, and service
mechanics differ. Verify which system before assembling a
packet.

### Department system — not IAS

NYC Civil Court does **not** use the Individual Assignment
System (22 NYCRR § 202.3). Cases route to **Departments**
that handle case categories, and within each Department to
calendar parts and trial parts. A motion filed today may be
heard by one judge and the trial held before another. There
is no "Part Rules" lookup analogous to Supreme Court.

### Small Claims arbitrators are not judges

Small Claims trials are heard by **arbitrators** (volunteer
attorneys, judges *pro tem*) under Civil Court Act
§ 1804-A, not by sitting Civil Court judges. The pro se
litigant has the right to demand a trial-de-novo before a
sitting judge under § 1808, but must do so before the
arbitration begins. The hearing is informal; CPLR Article
45 evidence rules apply with reduced rigor.

### Self-Help Resource Centers in every borough

Each borough courthouse runs a **Self-Help Resource
Center** with paid attorneys available to answer
procedural questions for pro se litigants. Hours vary by
borough; usually 9 AM-4 PM weekdays. The Consumer Credit
Part scheduled calendar calls often coincide with the SHRC
hours.

## Filing checklist

1. **Summons + Complaint**: Civil Court Act § 401 — short-
   form summons + complaint with the **$45 filing fee**
   (Civil Court Act § 1911(1)) for actions up to $1,000;
   **$45 + $20** for actions over $1,000
2. **Service**: CPLR 308 / 312 within Civil Court Act § 403
   service period (typically 120 days under CPLR 306-b)
3. **CCFA notice** (if consumer-credit action): plaintiff
   must mail an additional notice under CPLR 308(six)
4. **Answer**: defendant has **20 days** from personal
   service or **30 days** from substituted service
   (CPLR 320(a))
5. **Calendar call**: Consumer Credit Parts run a weekly
   calendar; the case appears 30-60 days after Answer
6. **Trial**: 6-12 months from filing in most cases

> **Format compliance:** 22 NYCRR Part 208 governs filings.
> Use `ny-statewide-format` as the baseline; Part 208 mirrors
> Part 202 with Civil Court-specific adjustments (case
> caption uses "Civil Court of the City of New York" instead
> of "Supreme Court").

## Composition with other ny- skills

- `ny-statewide-format` — baseline 22 NYCRR Part 202 format
  with Part 208 Civil Court adjustments
- `ny-nyc-housing-court` — the Housing Part covered
  separately
- `ny-county-courts` — broader roll-up that this skill
  refines (NYC Civil Court is no longer in the roll-up's
  scope)
- `ny-discovery` — CPLR Article 31 mechanics (Civil Court
  uses discovery in modified form; demands are uncommon)
- `ny-first-30-days` — Answer / pre-answer motion triage
- `ny-consumer-debt` — CCFA pleading + default scrutiny
- `ny-pro-se` — pro se framework (Civil Court Consumer
  Credit Part is overwhelmingly pro se on defense)
- `ny-file-packet` — UCMS / CCEF assembly

## Pro-se resources

- **NYC Civil Court Self-Help Resource Centers** (one per
  borough; check `nycourts.gov/courts/nyc/civil/`)
- **CLARO clinics** (Civil Legal Advice and Resource Office)
  — pro se debt-defense clinics in each borough
- **NYLAG (New York Legal Assistance Group)** — Mobile
  Legal Help Center
- **Legal Aid Society Civil Practice** — direct legal aid
  for income-qualifying defendants
- **NYC Department of Consumer Worker Protection** —
  consumer complaint intake (collection-agency licensure
  enforcement under NYC Admin Code § 20-486 et seq.)
