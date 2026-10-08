---
name: ny-city-courts-codearranger
title: Upstate City Courts (UCCA / 22 NYCRR Part 210)
description: Use when drafting or filing in an upstate City Court — the limited-jurisdiction civil layer outside New York City under the **Uniform City Court Act (UCCA)** with procedural rules at **22 NYCRR Part 210**. Triggers include 'Buffalo City Court', 'Rochester City Court', 'Syracuse City Court', 'Albany City Court', 'Yonkers City Court', 'White Plains City Court', 'Schenectady City Court', 'Utica City Court', 'Troy City Court', 'UCCA', 'Uniform City Court Act', '22 NYCRR Part 210', 'upstate City Court'. Covers the ~60 City Courts' civil and small-claims jurisdiction, Housing Parts where they exist, and the variable NYSCEF e-filing rollout. NOT for NYC Civil Court (see `ny-nyc-civil-court`); not for Town & Village Justice Courts (UJCA — see `ny-justice-courts`); not for Long Island District Courts (UDCA — see `ny-nassau-dc` and `ny-suffolk-dc`).
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-city-courts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Upstate City Courts (UCCA / 22 NYCRR Part 210)

> **NOT LEGAL ADVICE.** Verify the specific City Court's
> local rules, dollar caps, and e-filing rollout before
> every filing.

## At a glance

- **Court system**: City Courts established under the
  **Uniform City Court Act (UCCA)** of 1965 with procedural
  rules at **22 NYCRR Part 210**. Each city of population
  > 10,000 outside NYC operates a City Court.
- **Civil jurisdiction**: up to **$15,000** (UCCA § 202)
- **Small claims**: up to **$5,000** in most cities; **$3,000**
  in the smaller City Courts (UCCA § 1801); check the local
  court rules
- **Commercial claims**: up to $5,000 in cities where the
  Commercial Claims Part has been established (UCCA
  § 1801-A)
- **L&T (summary proceedings)**: where the City Court has a
  Housing Part, RPAPL Article 7 summary proceedings; in
  smaller cities without a Housing Part, L&T goes to the
  Civil Part with RPAPL Article 7 procedure
- **E-filing**: **NYSCEF mandatory or available in Buffalo,
  Rochester, Syracuse, Albany, Yonkers, White Plains, and
  expanding**; many smaller City Courts still rely on paper
  filings

## ~60 City Courts statewide

The major ones (by civil filing volume):

| City Court | County | Notes |
|---|---|---|
| **Buffalo City Court** | Erie | Largest upstate; Housing Part; NYSCEF mandatory |
| **Rochester City Court** | Monroe | Housing Part; NYSCEF expanding |
| **Syracuse City Court** | Onondaga | Housing Part; NYSCEF available |
| **Albany City Court** | Albany | Civil + Criminal Parts; NYSCEF |
| **Yonkers City Court** | Westchester | Largest in Westchester; NYSCEF |
| **White Plains City Court** | Westchester | NYSCEF |
| **New Rochelle City Court** | Westchester | NYSCEF |
| **Mount Vernon City Court** | Westchester | NYSCEF |
| **Niagara Falls City Court** | Niagara | NYSCEF |
| **Schenectady City Court** | Schenectady | NYSCEF |
| **Utica City Court** | Oneida | |
| **Troy City Court** | Rensselaer | |
| **Binghamton City Court** | Broome | |
| **Auburn City Court** | Cayuga | |
| **Watertown City Court** | Jefferson | |
| **Glen Cove City Court** | Nassau | Functions like a District Court Sixth District for civil |
| **Long Beach City Court** | Nassau | Functions like a District Court Fifth District for civil |
| **Newburgh City Court** | Orange | |
| **Poughkeepsie City Court** | Dutchess | |
| **Beacon City Court** | Dutchess | |

Note: Long Beach City Court and Glen Cove City Court
overlap with the Nassau District Court's Fifth and Sixth
Districts — confirm which court the summons names before
filing a response.

## Distinctives

### UCCA is parallel to the UDCA

The Uniform City Court Act tracks the Uniform District
Court Act closely. 22 NYCRR Part 210 mirrors 22 NYCRR Part
212 with City Court-specific terminology. A practitioner
who has handled a Nassau District Court matter (`ny-nassau-dc`)
will find the City Court procedural framework familiar.

### CCFA applies in full

The 2022 Consumer Credit Fairness Act applies in City Courts
the same way it applies in NYC Civil Court and the Long
Island District Courts. CPLR 3015(e) heightened pleading,
22 NYCRR § 202.27-a default-judgment scrutiny (applied
through the parallel Part 210 rule), and CPLR 214-i 3-year
SOL all apply.

### Housing Parts vary

Buffalo, Rochester, Syracuse, and Yonkers operate dedicated
Housing Parts modeled on NYC Housing Court. Other cities
hear L&T summary proceedings in the Civil Part. RPAPL
Article 7 procedure (14-day rent demand under § 711(2),
30/60/90-day holdover notice under RPL § 226-c) applies
statewide regardless of forum.

### 2024 Good Cause Eviction — opt-in outside NYC

NYS Good Cause Eviction (RPL Article 6-A) applies in NYC
by default. Outside NYC, the law is **opt-in by
municipality**. Cities that have opted in (as of mid-2025):

- **Albany** — opted in 2024
- **Newburgh** — opted in 2024
- **Kingston** — opted in 2024
- **Poughkeepsie** — opted in 2024
- **Hudson** — opted in 2024
- **Beacon** — opted in 2024
- **Syracuse** — opted in 2024

Buffalo, Rochester, Schenectady, and several others
debated opt-in but had not adopted as of early 2026. Verify
the specific municipality's status when drafting a Good
Cause defense.

### Right to Counsel — limited but expanding

NYC's universal Right to Counsel (Local Law 136 of 2017)
is being modeled in upstate jurisdictions. Albany, Newburgh,
and Rochester have piloted RTC programs for income-qualifying
tenants. Most upstate cities still operate without
universal RTC; legal aid organizations are the principal
source of representation:

- **Legal Aid Buffalo** — Erie / Niagara
- **Legal Assistance of Western New York (LawNY)** —
  Rochester / Western NY
- **Hiscock Legal Aid Society** — Syracuse / CNY
- **Legal Aid Society of Northeastern New York** — Albany /
  North Country
- **Legal Services of the Hudson Valley** — Westchester /
  Putnam / Dutchess / Rockland / Ulster / Orange / Sullivan
- **Mid-Hudson Legal Services** — Dutchess

### Trial-de-novo in Small Claims

City Court Small Claims Part trials are conducted by
arbitrators (volunteer attorneys) under UCCA § 1804-A. The
losing party has the right to a trial-de-novo before a
sitting City Court judge under UCCA § 1808 — but the demand
must be served before the arbitration begins.

## Filing checklist

1. **Summons + Complaint** — UCCA § 401, **$45 filing fee**
   (UCCA § 1911); affidavit of service per CPLR 308
2. **Answer** — defendant has **20 days** from personal
   service or **30 days** from substituted service (CPLR
   320(a))
3. **Pre-trial conference** — most City Courts schedule
   within 60-90 days
4. **Trial** — bench trial typically 6-9 months from filing
   for Civil Part actions

> **Format compliance:** 22 NYCRR Part 210 governs filings
> here. Use `ny-statewide-format` as the baseline; Part 210
> mirrors Part 202 with City Court-specific adjustments
> (caption uses "[City] City Court" instead of "Supreme
> Court").

## Composition with other ny- skills

- `ny-statewide-format` — baseline 22 NYCRR Part 202 format
  with Part 210 City Court adjustments
- `ny-nyc-civil-court` — distinct court for cases inside NYC
- `ny-justice-courts` — Town & Village Justice Courts for
  cases outside any city's territorial reach
- `ny-discovery` — CPLR Article 31 mechanics (City Court
  Civil Part typically light on discovery)
- `ny-first-30-days` — Answer / pre-answer motion triage
- `ny-consumer-debt` — CCFA pleading + default scrutiny
- `ny-landlord-tenant` — RPAPL Article 7 mechanics for
  Housing Parts and Civil Parts handling L&T
- `ny-pro-se` — pro se framework
- `ny-file-packet` — NYSCEF (where mandatory) or paper-
  filing assembly

## Pro-se resources

- **LawNY** (rochester / WNY)
- **Legal Aid Buffalo** (erie / niagara)
- **Hiscock Legal Aid Society** (CNY)
- **Legal Aid Society of Northeastern New York** (capital region)
- **Legal Services of the Hudson Valley** (LSHV)
- **NYS Office of Court Administration Pro Se forms** —
  `nycourts.gov/courthelp/`
- **Each City Court** runs a Pro Se Help Desk during clerk's
  hours
