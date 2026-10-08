---
name: or-post-judgment-codearranger
title: Oregon Post-Judgment Procedure
description: Navigate post-judgment procedures in Oregon — motions to vacate under ORCP 71, garnishment under ORS 18.600 et seq., supplemental proceedings (debtor exam), exemption claims under ORS 18.345–18.385, and satisfaction of judgment. Use when the user asks about vacating a default judgment, responding to a wage garnishment or bank levy, exempting property from collection, answering supplemental interrogatories, or filing a satisfaction of judgment.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/or-court-docs/skills/or-post-judgment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Exemptions
  path: references/exemptions.md
- title: Garnishment Response
  path: references/garnishment-response.md
- title: Motion To Vacate
  path: references/motion-to-vacate.md
- title: Satisfaction Of Judgment
  path: references/satisfaction-of-judgment.md
- title: Supplemental Proceedings
  path: references/supplemental-proceedings.md
---

# Oregon Post-Judgment Procedure

When a judgment has been entered — against the defendant or for
the defendant — a separate body of rules governs what happens
next. Pro se defendants most often face post-judgment procedure
in two situations:

1. **A default judgment was entered against them** and they want
   to vacate it under ORCP 71
2. **A judgment creditor is collecting** — garnishment, bank
   levy, supplemental proceedings — and the debtor needs to know
   their rights and exemptions

This skill covers both angles.

> **NOT LEGAL ADVICE.** Post-judgment timing is unforgiving.
> Verify each deadline and consult a licensed attorney where the
> stakes are significant.

## Core principles

1. **Vacation is about cause plus diligence** — ORCP 71 requires
   a specific ground (mistake, excusable neglect, void
   judgment, etc.) AND that the motion be brought within a
   "reasonable time" (and no more than 1 year for grounds (1)–
   (3))
2. **Exemptions are claimed promptly or lost** — most exemptions
   under ORS 18.345–18.385 must be claimed within 30 days of
   the garnishment notice
3. **Debtor exam responses are mandatory** — a writ of debtor
   exam (supplemental proceedings) is a court order; failure
   to respond can lead to contempt
4. **A judgment lives 10 years** (ORS 18.182) and can be
   renewed for another 10. The judgment is collectible
   throughout this period.

## Motion to vacate under ORCP 71

### When applicable

A defendant against whom default judgment was entered, who
believes the entry was wrongful or excusable. Grounds under
ORCP 71 B:

1. **Mistake, inadvertence, surprise, or excusable neglect** —
   most common ground; classic example: defendant did not see
   the summons because it was served while they were
   hospitalized
2. **Newly discovered evidence** — that, with reasonable
   diligence, could not have been discovered before the
   judgment
3. **Fraud, misrepresentation, or other misconduct of an
   adverse party** — including service fraud (false return of
   service)
4. **Judgment is void** — e.g., no personal jurisdiction,
   defective service
5. **Judgment satisfied, released, or discharged** — or no
   longer equitable
6. **Any other reason justifying relief**

### Deadline

- Grounds (1)–(3): "reasonable time", and not more than **1
  year** after entry of judgment
- Grounds (4)–(6): "reasonable time" — no fixed cap

The 1-year cap is **hard** for grounds (1)–(3). Beyond 1 year,
only the open-ended grounds (4)–(6) are available, and they're
harder to win.

### What the motion must show

The motion must establish:

1. **A specific ground** under ORCP 71 B
2. **Diligence** — the defendant moved promptly upon learning
   of the judgment
3. **A meritorious defense** — if the judgment is vacated, the
   defendant has a real defense to advance (not just a wish to
   re-litigate)
4. **Lack of prejudice to the plaintiff** — vacating the
   judgment doesn't unfairly harm plaintiff

See *Wagar v. Prudential Ins. Co. of America*, 276 Or 827, 556
P2d 658 (1976), and the recent ORCP 71 line of cases.

### Procedural mechanics

- File the motion with a supporting **declaration** under
  ORCP 1 E
- Attach the **proposed answer** as an exhibit (showing the
  meritorious defense)
- File a **Notice of Hearing** (or follow local SLR for
  motion scheduling)
- The motion is typically set on the assigned judge's
  calendar; in Multnomah, contact the JA
- Be prepared for the judge to want oral argument — see
  `or-hearings`

### Stay of execution pending vacate motion

Filing the motion to vacate does NOT automatically stay
execution (garnishment, levy). To stop collection while the
motion is pending, file a **separate motion for stay** with a
showing of:

- Likely success on the vacate motion
- Irreparable harm without stay
- Balance of equities
- Public interest (if applicable)

See `references/motion-to-vacate.md` for the full template and
checklist.

## Garnishment response

### How Oregon garnishment works

Once a judgment is entered and the time for appeal has passed,
the judgment creditor can issue a **Writ of Garnishment**
(ORS 18.605):

- **Wage garnishment**: served on the debtor's employer; the
  employer withholds a portion of wages (typically 25% under
  ORS 18.385) and pays it to the court
- **Bank levy**: served on the debtor's bank; the bank
  freezes funds in the account and (after a waiting period)
  pays them to the court
- **Account-receivable garnishment**: served on any third party
  who owes money to the debtor

### Exemption claim procedure

Within **30 days** of being notified of the writ, the debtor
can file a **Challenge to Writ of Garnishment** (ORS 18.700+)
claiming exemptions:

- **Wage exemption** (ORS 18.385): only 25% of disposable
  earnings is garnishable; if disposable earnings are below
  the statutory minimum (around 40× federal minimum wage),
  garnishment is zero
- **Head of household / family support** (ORS 18.385): if the
  debtor supports a family, additional protection
- **Federal benefits** (Social Security, SSI, VA, federal
  retirement) — fully exempt under federal and state law
- **State benefits** (TANF, OHP, unemployment) — exempt under
  ORS 18.345+
- **Homestead exemption** (ORS 18.395+): up to $40,000 of
  equity ($50,000 for joint owners) in primary residence
- **Personal property exemptions** (ORS 18.345): tools of
  trade ($5,000), motor vehicle ($3,000), personal property
  ($3,000), etc.

### What to do on receipt of garnishment notice

1. **Calendar the 30-day deadline** for filing the Challenge
2. **Photograph the notice** and the postmarked envelope
3. **Identify what's being garnished** (wages vs. bank account)
4. **Compute exemptions** — which categories apply and how
   much
5. **File the Challenge** on the OJD form (Exemption Claim
   Form) via File and Serve
6. **Serve the creditor** under ORCP 9
7. **Attend the hearing** (typically held within 21 days of
   filing) — see `or-hearings`

See `references/garnishment-response.md` for the full
checklist and form templates.

## Supplemental proceedings (debtor exam)

After judgment, the creditor may serve a **Notice of Debtor's
Examination** (ORS 18.265+) requiring the debtor to appear and
answer questions about assets, income, and ability to pay.

### Mechanics

- **Service**: ORCP 7 or under ORS 18.265 — typically
  personal service
- **Location**: courthouse, before the judge or a court
  reporter
- **Topics**: any assets that could be subject to execution;
  the debtor must answer truthfully
- **Documents**: the creditor can subpoena financial records
  (bank statements, pay stubs, etc.)

### Exemptions during exam

The debtor can refuse to answer questions about exempt
property — but must affirmatively claim the exemption on the
record. Silent refusal is treated as evasion and risks
contempt.

### Pro se considerations

- **Bring documents requested in the subpoena** — failure to
  produce is sanctionable
- **Answer truthfully** — perjury is a felony
- **Claim exemptions on the record** — name the property and
  the statutory ground
- **Take notes** — what assets the creditor seems interested
  in; this informs future planning

See `references/supplemental-proceedings.md` for the full
guide.

## Exemption catalog (ORS 18.345–18.385)

### Real property

- **Homestead**: $40,000 single / $50,000 joint owners of
  principal residence (ORS 18.395+)
- Mobile home as principal residence: same

### Personal property

- **Motor vehicle**: $3,000 equity
- **Tools of trade**: $5,000
- **Books, musical instruments, family photos**: $600 each
- **Household goods, furnishings, appliances**: $3,000
  aggregate
- **Wearing apparel, jewelry, personal items**: $1,800 +
  $600 watch
- **Pets**: not specifically protected but courts won't
  generally seize

### Earnings

- **Wages**: 75% of disposable earnings exempt; lower limit at
  ~40× federal minimum wage
- **Pensions, retirement, IRAs**: exempt (ORS 18.358)
- **Federal benefits** (Social Security, SSI, VA, federal
  retirement): fully exempt under federal preemption

### Benefits

- **Unemployment compensation**: exempt
- **Workers' compensation**: exempt
- **Public assistance** (TANF, OHP): exempt
- **Tax refunds / EITC**: federal portion exempt; Oregon
  state EITC also exempt under recent decisions

### Bank account safe harbor

When wages or federal benefits are deposited directly into a
bank account, those funds retain their exempt character. Under
**31 CFR 212**, banks must protect 2 months of direct-deposited
federal benefits from garnishment. State law (ORS 18.345)
similarly protects identified federal benefits.

If garnished, the debtor files a Challenge identifying the
funds as exempt federal benefits with bank records showing the
deposits.

See `references/exemptions.md` for the full annotated list with
ORS citations.

## Satisfaction of judgment

When a judgment has been paid in full, the creditor must file a
**Satisfaction of Judgment** (ORS 18.235 / ORCP 67):

- Within **60 days** of full payment
- On the OJD form, identifying the case and the amount paid
- Filed with the court that entered the judgment

If the creditor fails to file a satisfaction, the debtor may
move the court for an order declaring the judgment satisfied
(ORS 18.235+ procedure).

See `references/satisfaction-of-judgment.md` for the full
mechanism and template.

## Judgment renewal

A judgment lives **10 years** from entry (ORS 18.182). The
creditor may renew once for another 10 years by filing a
**Motion to Renew Judgment** (ORS 18.182(2)) before the
original 10-year period expires.

For a debtor, the practical implication: a creditor cannot
collect after 20 years (10 original + 10 renewed) unless they
manage another renewal — which is procedurally hard. The 10-
year clock is a defense to long-stale judgments.

## Pro se post-judgment checklist

After receiving any post-judgment paper:

- [ ] **Identify the type** (garnishment notice, debtor exam
      notice, satisfaction request, etc.)
- [ ] **Photograph the paper and the envelope**
- [ ] **Calendar all deadlines** (30 days for exemption claim;
      30 days for vacate; debtor exam date; etc.)
- [ ] **Identify which skill applies** — vacate?
      garnishment? exam? satisfaction?
- [ ] **Pull the relevant exemption analysis** from
      references
- [ ] **Draft the response** using the corresponding
      reference template
- [ ] **eFile via File and Serve** with the correct UTCR
      2.110 code
- [ ] **Serve the creditor** under ORCP 9 / UTCR 21.100
- [ ] **Attend any scheduled hearing** — see `or-hearings`

## References

- `references/motion-to-vacate.md` — ORCP 71 motion to
  vacate, full template and checklist
- `references/garnishment-response.md` — Challenge to Writ
  of Garnishment under ORS 18.700+, exemption-claim form,
  hearing prep
- `references/exemptions.md` — full annotated exemption
  catalog (ORS 18.345–18.385)
- `references/supplemental-proceedings.md` — debtor exam
  preparation and conduct
- `references/satisfaction-of-judgment.md` — Satisfaction of
  Judgment under ORS 18.235; motion to compel satisfaction
  if creditor refuses
