---
name: ny-deadlines-codearranger
title: New York Case Deadlines
description: Use when the user asks about timing or deadlines in a New York civil case. Triggers include 'when is my answer due in NY', 'CPLR 2103 service deadline', 'mail rule New York', '5 days for mail in NY', '5-day mail rule', 'CPLR 3133 interrogatory response', 'compute deadline NY Supreme Court', 'CPLR 2104 stipulation extension', 'CPLR 306-b 120 days for service', 'count weekends and holidays in NY filing', 'New York court holidays', 'NY Gen. Constr. Law § 24 holidays', 'when is a holiday for filing purposes in New York', 'Lincoln's Birthday court holiday'. Computes calendar-day and court-day deadlines using CPLR 2103 (service add-ons), CPLR 2103-a (electronic-service rules), NY Gen. Constr. Law § 24 + § 25-a holidays, and CPLR 2103(b)(2) 5-day mail rule — the most-mistaken rule for filers used to the 3-day federal mail rule.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-deadlines
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# New York Case Deadlines

> **NOT LEGAL ADVICE.** Missing a deadline can be fatal. Run
> the case-calendar script (`scripts/case-calendar.py`) for
> mechanical verification before relying on a hand-computed
> deadline.

## Core time-computation rules

### CPLR 2103 — Service of papers

| Mode | Add-on |
|------|---------|
| Personal delivery | None |
| Overnight delivery service (CPLR 2103(b)(6)) | **1 day** |
| Mail (CPLR 2103(b)(2)) | **5 days** |
| Facsimile (CPLR 2103(b)(5)) | None (counted on transmittal day) |
| Email (CPLR 2103(b)(7) and (8)) | None (counted on transmittal day) when authorized by consent or court order |
| Electronic filing through NYSCEF (22 NYCRR § 202.5-bb(b)(2)) | None — service occurs on the date the document is filed |

**The 5-day mail rule is the most-mistaken in NY.** Filers
used to FRCP 6(d) (3 days) over-count or under-count when
porting practice. Apply the **5-day add-on** when:

- Papers are served by mail
- The recipient's response deadline depends on the date of
  service
- The response is one for which the rule allows an add-on

The 5-day add-on is added **at the back end** of the
response period — i.e., the recipient has the normal CPLR-
specified response window *plus 5 days*.

### CPLR 2103-a — Email service

Added 2022. Allows email service if:

1. The recipient consented to email service (in writing,
   in a stipulation, in an NYSCEF appearance with email
   address provided)
2. Or the court ordered email service

Email service is **complete on transmission**; no add-on.

## NY court holidays (NY Gen. Constr. Law § 24)

| Holiday | Date |
|---------|------|
| New Year's Day | January 1 |
| Martin Luther King Jr. Day | 3rd Monday in January |
| Lincoln's Birthday | February 12 |
| Washington's Birthday (Presidents' Day) | 3rd Monday in February |
| Memorial Day | Last Monday in May |
| Flag Day | June 14 (not a court-closing day per CPLR; included in NY Gen. Constr. Law § 24) |
| Juneteenth | June 19 (added 2020 + 2024 amendments) |
| Independence Day | July 4 |
| Labor Day | 1st Monday in September |
| Columbus Day / Indigenous Peoples' Day | 2nd Monday in October |
| Election Day (general) | Tuesday after first Monday in November (every year) |
| Veterans Day | November 11 |
| Thanksgiving Day | 4th Thursday in November |
| Christmas Day | December 25 |
| Saturdays + Sundays | Excluded under CPLR 2103(c) |

**Distinctive NY court holidays**:

- **Lincoln's Birthday (Feb 12)** — NY-specific; not a
  federal court holiday
- **Election Day** — every year (federal courts open on
  off-year election days)
- **Flag Day (June 14)** — listed in NY Gen. Constr. Law
  but courts generally open

**Substitutes** (NY Gen. Constr. Law § 25-a):

- When a holiday falls on Saturday, the *Friday before* is
  the legal holiday for "public business"
- When a holiday falls on Sunday, the *Monday after* is the
  legal holiday

**For CPLR purposes** (CPLR 2103(c)): "When a deadline falls
on a Saturday, Sunday or public holiday, the time is extended
to the next succeeding business day." So you generally
forward-roll (not back-roll) to the next business day.

## Named NY deadlines

| Event | Deadline | Authority |
|-------|---------|-----------|
| Answer (personal service in-state) | 20 days | CPLR 3012(a) |
| Answer (substituted / out-of-state / mail) | 30 days | CPLR 3012(c) |
| Service of summons under CPLR 306-b | 120 days from filing | CPLR 306-b |
| Notice of Motion service period | 8 days minimum / 16 days with cross-motion | CPLR 2214(b) |
| Notice of Motion service + 5-day mail add-on | 13 days (8+5) | CPLR 2214 + 2103(b)(2) |
| Cross-motion service | 7 days before return date | CPLR 2215 |
| Bill of Particulars demand response | 30 days | CPLR 3042(a) |
| Notice for Discovery and Inspection response | 20 days | CPLR 3120(2) |
| Interrogatories response | 20 days | CPLR 3133(a) |
| Notice to Admit response | 20 days | CPLR 3123(a) |
| Deposition (EBT) notice | 20 days | CPLR 3107 |
| Motion to vacate default | 1 year from notice of entry | CPLR 5015(a)(1) |
| Notice of Appeal (Appellate Division) | 30 days from notice of entry | CPLR 5513(a) |
| Motion for reargument | 30 days from notice of entry | CPLR 2221(d) |
| Restraining notice duration | 1 year | CPLR 5222(b) |
| Consumer-credit SOL (new CCFA) | **3 years** | CPLR 213(a) |
| General contract SOL | 6 years | CPLR 213(2) |
| Personal injury SOL | 3 years | CPLR 214(5) |
| Defamation SOL | 1 year | CPLR 215(3) |
| Money judgment enforcement | 20 years | CPLR 211(b) |
| Foreclosure (post-FAPA) | 6 years; no acceleration unilateral revival | CPLR 213(4) + L 2022, ch 821 |

## Pitfalls

1. **5-day mail rule vs. federal 3-day** — port practice
   correctly
2. **Lincoln's Birthday** — Feb 12 closure is NY-specific
3. **Election Day** — every year, not just presidential
4. **Saturday/Friday rollback** — NY Gen. Constr. Law §
   25-a rolls **back** for public business (Saturday →
   Friday) but CPLR 2103(c) rolls **forward** for
   deadlines (Saturday → Monday). Don't confuse them.
5. **NYSCEF filing as service** — under 22 NYCRR §
   202.5-bb(b)(2), filing through NYSCEF on a registered
   party counts as service on the filing date; no add-on.
   This is increasingly the default in NY Supreme Court.
6. **Substituted service "complete 10 days after filing
   affidavit"** — when computing the answer deadline from
   substituted service (CPLR 308(2)), service is complete
   *10 days after* the affidavit of service is filed, not
   when delivery was attempted.

## case-calendar.py

The `scripts/case-calendar.py` script encodes:

- CPLR 2103 add-ons (5 days mail, 1 day overnight)
- NY Gen. Constr. Law § 24 holidays
- CPLR 2103(c) Saturday/Sunday/holiday forward-roll
- Named-rule deadline computations (answer due, RFP due,
  appeal due, etc.)
- SOL calculations by claim type with CPLR 213/214/215

Invoke:

```bash
python3 plugins/ny-court-docs/scripts/case-calendar.py \
  --rule answer-substituted \
  --service-date 2025-06-15
python3 plugins/ny-court-docs/scripts/case-calendar.py \
  --rules    # list all named rules
```

## Composition with other ny- skills

- `ny-first-30-days` — answer-deadline triage
- `ny-discovery` — discovery-response deadline computation
- `ny-post-judgment` — CPLR 5015(a)(1) 1-year clock
- `ny-consumer-debt` — CPLR 213(a) 3-year SOL on consumer
  credit
- `ny-quality-check` — pre-filing deadline verification
