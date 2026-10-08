---
name: ny-justice-courts-codearranger
title: Town & Village Justice Courts (UJCA / 22 NYCRR Part 214)
description: Use when drafting or filing in a New York Town or Village Justice Court (~1,250 courts statewide) established under the Uniform Justice Court Act (UJCA) with procedural rules at 22 NYCRR Part 214. Triggers include 'Town Justice Court', 'Village Justice Court', 'UJCA', '$3,000 small claims', 'East Hampton Justice', 'Southampton Town', 'Riverhead Town', 'Shelter Island'. Covers civil jurisdiction up to $3,000 (UJCA § 202), small claims up to $3,000, and part-time-judge lay-bench dynamics. NOT for cities (use `ny-city-courts`), Long Island Districts (use `ny-nassau-dc` / `ny-suffolk-dc`), or NYC Civil Court (use `ny-nyc-civil-court`). Especially relevant for **eastern Suffolk County** (East Hampton, Southampton, Riverhead, Shelter Island, Southold), which routes to Town Justice Courts, not Suffolk District Court.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-justice-courts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Town & Village Justice Courts (UJCA / 22 NYCRR Part 214)

> **NOT LEGAL ADVICE.** Verify the specific Town or Village
> Justice Court's schedule, sitting judge, and clerk hours
> before every filing.

## At a glance

- **Court system**: Town and Village Justice Courts —
  ~1,250 courts across the state established under the
  **Uniform Justice Court Act (UJCA)** of 1966 with
  procedural rules at **22 NYCRR Part 214**
- **Civil jurisdiction**: up to **$3,000** (UJCA § 202)
- **Small claims**: up to **$3,000** in informal proceedings
  (UJCA § 1801)
- **Commercial claims**: up to **$3,000** for entities (UJCA
  § 1801-A)
- **L&T (summary proceedings)**: no monetary cap on rent
  arrears; RPAPL Article 7 procedure applies; very high
  volume in rural and exurban towns
- **Criminal**: Vehicle and Traffic Law violations; lower-
  level misdemeanors; arraignments
- **Filing fee**: **$20** for civil filings under UJCA
  § 1911

## How the court works in practice

A Justice Court is typically located in the **Town Hall** or
**Village Hall**. The Justice (judge) is elected; in many
small towns the position is part-time and the Justice has a
day job in private practice or another field. A single
clerk handles intake, filings, and calendaring. Court
sessions are commonly held one or two evenings per week.

### Lay-judge note

Under UJCA § 105, Town and Village Justices are **not
required to be attorneys** — many are non-lawyers. State
law requires a brief training program through the OCA
Justice Court Assistance Program (JCAP). The procedural
rules at 22 NYCRR Part 214 are streamlined to accommodate
lay-judge administration, but RPAPL Article 7 (for L&T)
and the CPLR (for civil) still apply.

### Multi-municipality assignments

Some judges sit in **multiple courts** — e.g., a Village
Justice may also serve as a Town Justice in a neighboring
town. Conflicts and recusals are common in small
communities. The OCA's Justice Court Assistance Program
manages staffing across the ~1,250 courts.

## When you end up in Justice Court

The four most common civil scenarios:

### 1. Small claims under $3,000

Pro se plaintiff vs. pro se defendant; informal proceedings;
no formal pleadings; arbitrator-style hearing within
14-30 days of filing.

### 2. Eastern Suffolk County civil disputes

The five eastern Suffolk towns — **East Hampton, Southampton,
Riverhead, Shelter Island, Southold** — are **excluded from
Suffolk District Court** coverage. Civil matters arising in
those towns route to the Town Justice Court for amounts up
to $3,000 and to **Suffolk Supreme Court** for higher
amounts. There is **no $15,000-cap middle tier** in eastern
Suffolk.

### 3. Town / Village L&T summary proceedings

RPAPL Article 7 nonpayment and holdover petitions filed in
the town or village where the rental property is located.
14-day rent demand (post-HSTPA § 711(2)) and 30/60/90-day
holdover notice (RPL § 226-c) apply. The Justice Court
hears the petition; the tenant has the same defenses
available in NYC Housing Court (warranty of habitability,
retaliatory eviction, etc.).

### 4. Code-enforcement Town Court referrals

Town and Village Justice Courts hear local code-enforcement
matters — zoning violations, junk-vehicle ordinances,
short-term-rental disputes — referred by the municipality.
This is a civil-but-enforcement-adjacent docket distinct
from the consumer civil matters above.

## Distinctives

### Procedure is leaner than other civil courts

Justice Court civil procedure is **deliberately streamlined**.
22 NYCRR Part 214 mirrors Part 212 (Long Island District
Court) with further simplifications:

- Pleadings can be very short
- Discovery is rare and requires court permission
- Motion practice is limited; most disputes resolve at the
  first or second appearance
- Trial is usually a 1-2 hour bench trial

### Appeal goes to County Court, not Appellate Division

Appeals from Justice Court civil judgments go to the
**County Court** of the same county under UJCA § 1701, not
to the Appellate Division. (Some districts route appeals to
Appellate Term instead — verify per the Second
Department's coverage map.)

### Recording is local — not unified

Justice Court records are kept by the Town or Village —
**not by OCA**. Pulling a record requires contacting the
specific court clerk by phone (no central electronic
docket). Some larger Town Justice Courts have begun
publishing dockets online; most have not.

### Right to Counsel and Good Cause Eviction — opt-in

Local Law 136 universal Right to Counsel applies only in
NYC. Outside NYC, RTC is opt-in by municipality and is
**not** available in most Justice Courts. The 2024 Good
Cause Eviction Law is opt-in by municipality outside NYC —
verify whether the Town or Village has adopted before
drafting a Good Cause defense or holdover petition.

### Witness fees + costs are token

UJCA § 1903 caps witness fees at $5/day; subpoena fees at
$5/document. The court's general operating cost structure
is intentionally low.

## Filing checklist

1. **Summons + Complaint** — UJCA § 401; short form;
   $20 filing fee (UJCA § 1911); affidavit of service
   under CPLR 308 service rules
2. **Predicate notice** — for L&T, 14-day rent demand under
   RPAPL § 711(2) or 30/60/90-day holdover notice under
   RPL § 226-c
3. **Answer** — defendant has **20 days** from personal
   service or **30 days** from substituted service
4. **First appearance** — typically 14-30 days from issue
   joined
5. **Trial** — bench trial; 30-90 days from filing in most
   cases

> **Format compliance:** 22 NYCRR Part 214 governs Justice
> Court filings. Use `ny-statewide-format` as the baseline;
> Part 214 is the leanest of the trial-court format rule
> sets.

## Composition with other ny- skills

- `ny-statewide-format` — baseline 22 NYCRR Part 202 format
  with Part 214 Justice Court adjustments
- `ny-nyc-civil-court` — distinct court for matters inside
  NYC
- `ny-city-courts` — distinct court for matters inside a
  city's territorial reach
- `ny-suffolk-dc` — distinct court for the five western
  Suffolk towns + Brookhaven (eastern Suffolk towns route
  to Justice Court)
- `ny-county-courts` — appellate destination for Justice
  Court civil appeals
- `ny-consumer-debt` — CCFA applies in Justice Court Civil
  Part the same way it applies elsewhere
- `ny-landlord-tenant` — RPAPL Article 7 mechanics for
  Justice Court L&T docket
- `ny-pro-se` — pro se framework
- `ny-file-packet` — paper-filing assembly (Justice Courts
  are paper-only in most jurisdictions)

## Pro-se resources

- **NYS OCA Court Help** — `nycourts.gov/courthelp/` has
  Justice Court-specific forms
- **OCA Justice Court Assistance Program (JCAP)** — staff
  available for procedural questions
- **Regional legal aid offices** (LawNY, LSHV, Legal Aid
  Buffalo, Hiscock, Legal Aid Society of NE NY) cover most
  upstate counties for income-qualifying defendants in
  L&T and major-asset civil matters

## When to escalate out of Justice Court

If the dispute exceeds the $3,000 civil cap, the action
must be commenced in:

- **Supreme Court** — general jurisdiction; no monetary
  cap (use the appropriate `ny-nyco`, `ny-kings`,
  `ny-bronx`, `ny-nassau`, `ny-queens`, or `ny-county-courts`
  skill)
- **County Court** — civil jurisdiction up to $25,000 in
  counties outside NYC (rarely used as a civil forum since
  most counties prefer to route civil to Supreme Court)
- **District Court** — Nassau or Suffolk only; $15,000 cap

For L&T matters, even at low rent-arrears values, the
Justice Court remains the proper forum for the town /
village where the property is located.
