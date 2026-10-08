---
name: ga-pro-se-codearranger
title: Pro Se Drafting for Georgia
description: This skill should be used when drafting Georgia court documents for a self-represented (pro se) litigant. Triggers include "represent myself in Georgia", "pro se Georgia court", "I can't afford a lawyer", "fee waiver Georgia", "file without a lawyer in Georgia", "pauper's affidavit Georgia", "I got served and have no attorney". Covers the rights and limits of self-representation in Georgia, how to read the summons and tell whether the case is in Superior, State, or Magistrate Court, the 30-day answer clock, the pauper's affidavit for fee waiver under O.C.G.A. § 9-15-2, where to find Georgia self-help resources, the pro se signature block under O.C.G.A. § 9-11-11, and courtroom etiquette and candor. Pro se litigants are held to the same procedural rules as licensed attorneys.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-pro-se
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Pro Se Drafting for Georgia

> **NOT LEGAL ADVICE.** This skill is a drafting aid for
> self-represented litigants, not legal advice and not a substitute
> for counsel. For complex matters, or matters with substantial sums
> at stake, consider consulting a licensed Georgia attorney. Verify
> every rule, deadline, and citation against current law before
> filing.

Use this skill in addition to `ga-statewide-format` whenever the filer
is unrepresented. Georgia uses the terms "pro se" and
"self-represented" interchangeably.

## The right to self-represent — and its limits

A natural person may appear and act in their own behalf in any Georgia
court. But two structural limits matter at the outset:

1. **Held to the same rules.** A pro se litigant is bound by the same
   procedural rules — the Civil Practice Act (O.C.G.A. Title 9,
   Chapter 11), the Uniform Superior Court Rules (USCR), and the
   applicable evidence rules — as a licensed attorney. Courts do not
   relax deadlines, pleading requirements, or service rules because a
   party has no lawyer. Missing the answer deadline, failing to
   respond to requests for admission, or skipping the certificate of
   service produces the same consequences for a pro se party as for an
   attorney.

2. **Cannot represent others or an entity.** Self-representation
   covers the individual only. A corporation, LLC, or other artificial
   entity generally must appear through a licensed attorney — except in
   Magistrate Court, where an officer or authorized employee may
   represent the entity under the informal-procedure rules (O.C.G.A.
   §§ 15-10-40 through 15-10-53). One spouse cannot file for the other;
   a parent cannot file pro se on behalf of an adult child.

The practical takeaway: a pro se filing must clearly **name the relief
sought**, **cite the rule or statute** under which that relief is
available, **state facts** supporting each element, and **conclude
with a signature** (and, where the action requires it, a
verification).

## Reading the summons — which court are you in?

The single most important first step is identifying the court and the
deadline. Read the caption of the **summons** and the **complaint**:

- **Court name** appears at the top: "IN THE SUPERIOR COURT OF
  ________ COUNTY", "IN THE STATE COURT OF ________ COUNTY", or "IN
  THE MAGISTRATE COURT OF ________ COUNTY."
- **County** fixes venue and the clerk's office where you file.
- **File number** is the case number you must put on every paper.

Georgia's trial courts split by **subject matter**, not by dollar
amount above the Magistrate cap:

| Court | What it hears | Answer clock |
|---|---|---|
| **Superior Court** (O.C.G.A. § 15-6-8) | General jurisdiction; **exclusive** over divorce, equity, title to land, and felonies | 30 days (CPA) |
| **State Court** (O.C.G.A. § 15-7-4) | Civil actions of **any amount** except the Superior-exclusive subjects; most debt-collection and tort suits land here in counties that have a State Court | 30 days (CPA) |
| **Magistrate Court** (O.C.G.A. § 15-10-2) | Civil claims up to **$15,000** (§ 15-10-2(5)); dispossessory (no cap on dispossessory money judgments); garnishment within the cap | Per the magistrate summons (informal procedure) |

Because most counties with high filing volume (Fulton, Cobb, Gwinnett)
have all three trial courts, do not assume a debt or tort case is in
Superior Court just because the amount is large — it is usually in
State Court. See `ga-state-court`, `ga-magistrate`, and the venue
skills.

## The 30-day answer clock

Under O.C.G.A. § 9-11-12(a), the defendant must serve an **answer
within 30 days** after service of the summons and complaint (except as
otherwise provided). Count carefully — see `ga-deadlines` for time
computation and Georgia legal holidays.

Two safety valves if the deadline is missed:

- **Open default as of right.** Under O.C.G.A. § 9-11-55(a), a default
  may be opened **as a matter of right within 15 days** of the default
  by filing the answer and paying costs.
- **Open default by motion.** After the 15-day window, the court may
  open a default under O.C.G.A. § 9-11-55(b) on a showing of
  providential cause, excusable neglect, or a proper case, on the four
  statutory conditions.

Do not rely on these as a substitute for answering on time.

## Pauper's affidavit — fee waiver under O.C.G.A. § 9-15-2

A filer who cannot afford court costs may proceed without prepayment
by filing a **pauper's affidavit** (affidavit of indigence) under
**O.C.G.A. § 9-15-2**. Key points:

- The affidavit states, under oath, that because of indigence the
  party is **unable to pay the costs**. Filed with the initial paper,
  it lets the clerk docket the case without prepayment of filing fees.
- Any party at interest, or the clerk, may **contest the affidavit**;
  the court then holds a hearing and decides whether the affiant is in
  fact unable to pay. If the contest succeeds, the filer must pay
  costs or the matter does not proceed.
- A fee waiver covers court filing costs; it does not automatically
  pay for a private process server or other out-of-pocket litigation
  expenses — confirm scope with the clerk.

Submit the affidavit **with** the first filing rather than paying and
seeking a later refund.

## Signature block — "Pro Se", no Bar number

Georgia attorneys sign under their **State Bar of Georgia** number per
O.C.G.A. § 9-11-11. A pro se filer **omits the Bar number** and
replaces it with a clear self-represented designation:

```
Respectfully submitted, this ___ day of __________, 20__.

                                        ____________________________
                                        Jane Q. Doe
                                        [Street address]
                                        [City, GA ZIP]
                                        Phone: (###) ###-####
                                        Email: jane@example.com
                                        Defendant, Pro Se
```

Use **"Pro Se"** on the last line, tracking the filer's role
("Plaintiff, Pro Se"; "Defendant, Pro Se"; in divorce/family matters,
"Petitioner, Pro Se" or "Respondent, Pro Se"). Note that O.C.G.A.
§ 9-11-11 imposes no general verification requirement on ordinary
pleadings — verification is required only for specified actions (some
equitable and extraordinary proceedings).

## Service — the pro se filer's responsibility

A pro se plaintiff cannot personally serve their own defendant.

- **Service of process** (the summons + complaint) follows **O.C.G.A.
  § 9-11-4** — personal service, service on an agent, the statutory
  methods including publication under § 9-11-4(f), or acknowledgment/
  waiver under § 9-11-4.1. Use the **sheriff** or a court-appointed
  process server.
- **Service of subsequent papers** follows **O.C.G.A. § 9-11-5**, and
  every filed paper must carry a **certificate of service**. See
  `ga-statewide-format` for the certificate template.

## Georgia self-help resources

- **georgiacourts.gov** — the Judicial Council/Administrative Office
  of the Courts site, with statewide self-help materials and the
  e-filing court map (georgiacourts.gov/efile-court-records).
- **Georgia Legal Aid (georgialegalaid.org)** — plain-language guides,
  forms, and legal-aid referral by county.
- **County law libraries** — most populous counties operate a public
  law library at or near the courthouse with statutes, USCR, and
  form-books.
- **Georgia Child Support Commission calculator** — the official
  online Child Support Worksheet calculator for any case involving
  child support (see `ga-family-law`).
- **Court clerks and self-help kiosks** — clerks can explain
  procedure and accept filings but cannot give legal advice.

## Etiquette and candor

- **Candor to the tribunal.** Do not misstate facts or law. A pro se
  litigant who misrepresents the record risks sanctions and loss of
  credibility.
- **Courtroom conduct.** Address the judge as "Your Honor," stand when
  speaking, do not interrupt, and arrive early. See `ga-hearings` for
  oral-argument and courtroom protocol.
- **When to get counsel.** Divorce with contested custody or
  significant assets, suits with large exposure, and anything with a
  looming statute-of-limitations or default consequence warrant at
  least a consultation with a licensed Georgia attorney.

## Common pro se pitfalls in Georgia

1. **Filing in the wrong court** — putting a debt or tort case in
   Superior Court when the county's State Court is the right forum, or
   misjudging the $15,000 Magistrate cap.
2. **Missing the 30-day answer deadline** and not acting within the
   15-day open-default-as-of-right window under § 9-11-55(a).
3. **Ignoring requests for admission** — under O.C.G.A. § 9-11-36,
   unanswered requests are **deemed admitted**. See `ga-discovery`.
4. **Omitting the certificate of service** required by § 9-11-5.
5. **Paying fees the filer can't afford** instead of filing the
   § 9-15-2 pauper's affidavit with the first paper.

## Composition

- For statewide format: `ga-statewide-format`
- For the specific court: `ga-fulton`, `ga-cobb`, `ga-gwinnett`,
  `ga-state-court`, `ga-magistrate`, `ga-county-courts`
- For motion drafting: `ga-draft-motion`
- For deadline computation: `ga-deadlines`
- For citation verification: `ga-fact-check`
- For setting a hearing: `ga-schedule-hearing`

## References

- `references/pro-se-rights-and-limits.md` — self-representation
  rights, entity-representation limits, candor duties
- `references/pauper-affidavit.md` — O.C.G.A. § 9-15-2 fee-waiver
  mechanics and the contest procedure
- `references/self-help-resources.md` — georgiacourts.gov, Georgia
  Legal Aid, county law libraries, the Child Support calculator
