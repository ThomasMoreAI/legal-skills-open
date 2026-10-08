---
name: wa-wawd-pro-se-codearranger
title: W.D. Washington Federal Court — Pro Se (WAWD)
description: 'Use this skill when a self-represented litigant is filing or litigating a civil case in FEDERAL court in western Washington — the U.S. District Court for the Western District of Washington (W.D. Wash. / WAWD). Triggers include "file in federal court", "WAWD", "U.S. District Court Seattle/Tacoma", "sue a federal agency", "civil rights lawsuit", "Social Security appeal", "diversity jurisdiction", "federal complaint", "CM/ECF pro se", "FRCP 4 service", "appeal to the Ninth Circuit". CRITICAL: this is a DIFFERENT rule universe — the FRCP + W.D. Wash. Local Civil Rules govern, NOT state CR/CRLJ or GR 14. Covers jurisdiction triage, opening a case, service, CM/ECF registration, the LCR 7(d) noting-date system, sealed documents, and Ninth Circuit appeal basics.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-wawd-pro-se
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Wawd Forms And Resources
  path: references/wawd-forms-and-resources.md
- title: Wawd Pro Se Guide
  path: references/wawd-pro-se-guide.md
---

# W.D. Washington Federal Court — Pro Se (WAWD)

> **NOT LEGAL ADVICE.** This skill produces drafting aids and procedural information from the
> court's own public guidance. It is not legal advice and does not create an attorney-client
> relationship. The court will hold a pro se litigant to the same rules as an attorney. Verify
> every rule, deadline, and fee against the current FRCP, the current W.D. Wash. Local Civil
> Rules, and the court's website before filing.

## This is federal court — different rules than the rest of this plugin

Everything else in `wa-court-docs` is Washington **state** practice (CR/CRLJ, GR 14, RCW).
This skill covers the **U.S. District Court for the Western District of Washington**, where the
**Federal Rules of Civil Procedure (FRCP)** and the court's **Local Civil Rules (LCR)** govern
instead. Do not apply GR 14 or the state civil rules to a WAWD filing, and do not apply this
skill to a state-court matter. Assigned judges may also have **individual chambers
requirements** — check the judge's page at `wawd.uscourts.gov/judges` after assignment.

Canonical sources (mirrored in [`references/wawd-pro-se-guide.md`](references/wawd-pro-se-guide.md)
and [`references/wawd-forms-and-resources.md`](references/wawd-forms-and-resources.md)):

- Representing Yourself (Pro Se): `https://www.wawd.uscourts.gov/representing-yourself-pro-se`
- Pro Se Guide to Filing Your Lawsuit in Federal Court (Rev. Jul-24, PDF)
- Forms: `https://www.wawd.uscourts.gov/court-forms` (Self-Representation + Civil sections)
- Local Rules: `https://www.wawd.uscourts.gov/local-rules-and-orders` · FRCP: `law.cornell.edu/rules/frcp`

## Step 0 — Is federal court even the right forum?

Federal courts are courts of **limited jurisdiction**. Triage before drafting anything:

| Case | Forum |
|---|---|
| Federal law / U.S. Constitution claim (civil rights, FDCPA, FCRA, FLSA, etc.) | Federal — likely correct |
| United States or a federal agency is a party (Social Security, VA, IRS, USPS) | Federal — likely correct |
| Parties in different states AND more than $75,000 in controversy ("diversity") | Federal — possible |
| Divorce, custody, adoption, name change, landlord-tenant, wills | **State court** — route to `wa-pro-se` / `wa-family-law` / `wa-landlord-tenant` |

Also screen: **statute of limitations** (filing in the wrong court can blow the deadline);
**FRCP 11(b)** sanctions for frivolous/harassing suits; and the cost risk that a **losing party
commonly pays the winner's costs** (depositions, witness fees, copies) and sometimes fees.

## Seattle or Tacoma?

File where the claim arose or where the defendant(s) reside (LCR 3):

- **Seattle** (700 Stewart St., Suite 2310, Seattle, WA 98101 · 206-370-8400): Island, King,
  San Juan, Skagit, Snohomish, Whatcom counties.
- **Tacoma** (1717 Pacific Ave., Room 3100, Tacoma, WA 98402 · 253-882-3800): Clallam, Clark,
  Cowlitz, Grays Harbor, Jefferson, Kitsap, Lewis, Mason, Pacific, Pierce, Skamania, Thurston,
  Wahkiakum counties.
- **Social Security appeals** are randomly assigned Seattle or Tacoma regardless of residence.

## Opening a case

Required to open: **(1) Complaint**, **(2) Civil Cover Sheet (JS-44)**, **(3) the filing fee
($405 per the Rev. Jul-24 guide — verify current) or an IFP application**. Use the court's
pro se complaint templates (12 cause-of-action variants — civil rights, employment
discrimination, FLSA, breach of contract, negligence, etc.) from the forms page; the
references file catalogs them. Optional at opening: **Summons** for each defendant (issued
immediately if the fee is paid; held until IFP is granted otherwise) and an **Application for
Court-Appointed Counsel** (civil-rights or employment-discrimination form; no right to
counsel in civil cases — the judge weighs finances, effort to hire counsel, ability to
self-present, and case complexity).

**How to file a NEW case**: in person (clerk window 9am–4pm M–F, or the lobby drop box),
by mail to the proper courthouse, or **by email — new cases only** —
`newcases.seattle@wawd.uscourts.gov` / `newcases.tacoma@wawd.uscourts.gov`. After
assignment, email filing is no longer allowed: paper or CM/ECF only.

**LCR 5.2(a) redaction (mandatory)**: dates of birth → year only; minors → initials; SSNs,
taxpayer IDs, passport numbers, driver-license numbers → remove entirely; financial account
numbers → last four digits.

**Document format** (the federal counterpart to the state skills' GR 14 knowledge): 8½×11
white paper, **25 numbered lines in the left margin**, caption + case number on every
document, typed or neatly written in blue/black ink on one side only, dated and **originally
signed** (FRCP 11(a)), with the filer's name, address, and phone on every document.

## Service of process (FRCP 4)

- Serve **every named defendant within 90 days** of filing (FRCP 4(m)) or face dismissal.
- The plaintiff cannot serve their own papers — **any non-party over 18** may; the court may
  order U.S. Marshal service (FRCP 4(c)(3), common in granted-IFP cases).
- **Waiver of service** (FRCP 4(d), AO Forms 398/399) saves service costs; a waiving
  defendant gets 60 days to respond. The United States cannot waive.
- **Serving the United States / agencies / officers (FRCP 4(i))**: registered/certified mail to
  the civil-process clerk at the U.S. Attorney's office for the district AND to the U.S.
  Attorney General in Washington, D.C.; plus the agency/officer itself when it is the named
  defendant or its order is challenged.
- File the **proof of service** (page 2 of the summons) for each defendant (FRCP 4(l)).

## Motion practice — the LCR 7(d) noting-date system

Every motion must state a **noting date** (the date it's ready for decision) on its face,
directly under the title. Categories per the court's guide (verify against current LCR 7):

| Category | Earliest noting date | Response | Reply |
|---|---|---|---|
| Same-day (stipulated/agreed, over-length, reconsideration, default, default judgment vs. non-appearing party, ex parte, TRO, appoint mediator) | day filed | none unless ordered | none unless ordered |
| 14-day (relief from deadline, protective order, motion to seal) | 14 calendar days | 9 days after filing | by noting date |
| 21-day (other non-dispositive: amend, remand, compel discovery) | 21 calendar days | 15 days after filing | by noting date |
| 28-day (dispositive: dismiss, preliminary injunction, class cert, remand/transfer/compel arbitration) | 28 calendar days | 21 days after filing | by noting date |
| In limine | ≥21 days after filing, ≤6 days before pretrial conference | Monday before noting date | none unless ordered |

Request argument by writing **"Oral Argument Requested"** under the case number and title —
most motions are decided on the papers. **Sealed documents**: motion to seal + proposed order
+ supporting declaration; sealed material cannot be e-filed — deliver in a sealed envelope
marked "FILED UNDER SEAL" (LCR 5(g)). **Change of address/phone/email**: file written notice
within 10 days (LCR 10(f)).

## CM/ECF for pro se filers

E-filing is optional — paper by mail/in person always works. Requirements: an open case with
the fee paid or IFP granted, a **per-case registration form**, plus PACER "Case Search Only"
and "Non-Attorney Filer" registration at pacer.gov. Two tiers: **E-Service only** (receive
filings by email; still file on paper) or **E-Filer + E-Service** (file and receive
electronically — waives paper copies entirely). PDFs only; the NEF email gives one free look
(expires 14 days; PACER charges ~$0.10/page after). Support: 206-370-8440 option 2,
`cmecf@wawd.uscourts.gov`, M–F 8–5.

## After filing, judgment, and appeal

Random judge assignment (no judge-shopping); possible **magistrate-judge** referral or
consent (FRCP 73). No answer → move for default under FRCP 55 (same-day noting). Answer →
pretrial: FRCP 26(f) conference before discovery opens, then depositions / interrogatories /
RFPs / RFAs (FRCP 30/33/34/36 — compose with `wa-discovery` for mechanics, but apply FRCP
numbers and limits, not the state CRs), dispositive motions (FRCP 12/56, 28-day noting), and
bench or jury trial. Appeals go to the **Ninth Circuit**: Notice of Appeal in this court
(FRAP 4 deadlines — generally 30 days from judgment; 60 when the United States is a party —
verify), $605 appeal fee per the court's appeals page (the Rev. Jul-24 guide's $505 is
stale — verify current), district-court IFP status carries up subject to Ninth Circuit
review. Transcripts: order form + arrange payment directly with the court reporter.

## Free help

- **Federal Civil Rights Legal Clinic** (Federal Bar Association; free 30-minute sessions,
  appointment only; advice and referrals, not representation): Seattle 206-267-7070 (press 1)
  or `kcba.org/nlc`; Tacoma 253-368-6690 (lines M–Th 10–3). Schedules vary — confirm when
  booking. The Clerk's Office is not affiliated and cannot book appointments.
- **The Clerk can** explain procedure and supply forms; **cannot** give legal advice, predict
  rulings, interpret rules or orders, or relay messages to the judge.
- Statewide legal-aid directory (Northwest Justice Project, county volunteer-lawyer programs,
  WSBA referral): see [`references/wawd-forms-and-resources.md`](references/wawd-forms-and-resources.md).

## Composition

Routes state-court matters to `wa-pro-se` and the subject bundles. For federal case law
(W.D. Wash. = CourtListener court `wawd`; Ninth Circuit = `ca9`), compose with
`case-law-research` in `claude-legal-federal-laws` — never cite a case from memory. Subject
bundles (`wa-consumer-debt` FDCPA claims, `wa-employment` discrimination, etc.) supply the
substantive law for claims that belong in this forum; `wa-deadlines` does NOT apply (use
FRCP 6 + LCR computation). Drafting scaffolders may be reused for structure, but strip GR 14
assumptions and apply the format rules above.
