---
name: ga-deadlines-codearranger
title: Georgia Case Deadlines
description: Use when the user asks about timing or deadlines in a Georgia civil case. Triggers include "when is my answer due in Georgia", "how many days to respond in Georgia", "30 days to respond", "compute a deadline", "Georgia statute of limitations credit card", "what's the SOL on a contract in Georgia", "Georgia court holidays", "court-day vs calendar-day in Georgia", "discovery response deadline Georgia", "motion response deadline", "default deadline Georgia", "notice of appeal 30 days Georgia", "dispossessory answer deadline", "is my debt too old to sue on in Georgia". Computes calendar-day and court-day deadlines under O.C.G.A. § 1-3-1(d)(3) (incorporated into the Civil Practice Act by O.C.G.A. § 9-11-6(a)), excludes Georgia legal holidays under O.C.G.A. § 1-4-1, applies the Saturday / Sunday / holiday roll-forward and the sub-7-day exclusion of intermediate weekends and holidays, and maps named civil rules and statutes of limitation to days plus authority via the bundled calendar
  script.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-deadlines
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Georgia Case Deadlines

> **NOT LEGAL ADVICE.** This skill computes deadlines. Always
> independently verify in the cited rule or statute and confirm the
> court's actual holiday closures and the assigned judge's standing
> orders before treating any computed date as final.

Use this skill to compute deadlines under Georgia's time-computation
rule (O.C.G.A. § 1-3-1(d)(3), incorporated into the Civil Practice Act
by O.C.G.A. § 9-11-6(a)), the Georgia legal-holiday list (O.C.G.A.
§ 1-4-1), and the named civil-procedure and statute-of-limitation rules
encoded in `scripts/case-calendar.py`.

## Time computation — O.C.G.A. § 1-3-1(d)(3) / § 9-11-6(a)

Georgia counts time intervals stated in its statutes and rules as
follows:

1. **Exclude** the first day — the day of the triggering event (e.g.,
   the day of service).
2. **Count** every intermediate calendar day for periods of **7 days
   or more**, then adjust only the last day.
3. **Count** the **last** day, **unless** it falls on a **Saturday,
   Sunday, or O.C.G.A. § 1-4-1 legal holiday** — in which case the
   period runs through the **next business day**.
4. For a prescribed period of **fewer than 7 days**, **exclude**
   intermediate Saturdays, Sundays, and legal holidays from the count
   (effectively count only business days).

The roll-forward at the end can only extend a deadline; it never
shortens one. A "minus" period (e.g., a notice that must be served a
minimum number of days *before* an event) counts backward under the
same rule.

### The +3-days-for-mail/e-mail rule — O.C.G.A. § 9-11-6(e)

When a party must act within a prescribed period **after service of a
paper** and that paper was served **by mail or by e-mail**, **three
days are added to the prescribed period** (the three days extend the
period before the end-of-period weekend/holiday roll-forward). Two
limits to flag:

- It applies only to **post-complaint papers** — **not to service of
  the original summons and complaint** (so the 30-day answer period is
  not extended by mailing the complaint).
- It is irrelevant to **statutes of limitation**.

`scripts/case-calendar.py --mail-service` applies the +3 days to a
forward response period (e.g., a discovery response served by mail:
`--rule rfp-response --mail-service`).

## Georgia legal holidays — O.C.G.A. § 1-4-1

Georgia sets **exactly thirteen state-holiday days each year** by
gubernatorial proclamation. O.C.G.A. § 1-4-1(a) adopts the federal
public holidays as they existed on **January 1, 2022**, plus the days
the Governor proclaims; the statute also requires the Governor to
include one of **January 19 / April 26 / June 3** among the
proclaimed days (the formerly named anchors, now published unlabeled
as "State Holiday").

### Predictable-rule holidays (auto-computed by the script)

| Holiday | Date |
|---|---|
| New Year's Day | January 1 |
| Martin Luther King, Jr. Day | 3rd Monday in January |
| Memorial Day | Last Monday in May |
| Juneteenth | June 19 (observed in Georgia) |
| Independence Day | July 4 |
| Labor Day | 1st Monday in September |
| Columbus Day | 2nd Monday in October (observed; not renamed) |
| Veterans Day | November 11 |
| Thanksgiving Day | 4th Thursday in November |
| Day after Thanksgiving | Friday after Thanksgiving (published "State Holiday") |
| Christmas Day | December 25 |

Fixed-date holidays follow federal observance: a Saturday holiday
shifts to the preceding Friday; a Sunday holiday shifts to the
following Monday.

### Floating "State Holiday" days (NOT auto-computed — verify each year)

These are proclamation-driven and vary year to year, so the script
does **not** include them:

- **Washington's Birthday** — statutorily a February federal holiday,
  but Georgia **defers** its observance to the **year-end cluster**
  (often **December 24**).
- **The spring "State Holiday"** — the date formerly published as
  Confederate Memorial Day, statutorily anchored near **April 26**.
- In some years a **second floating "State Holiday."**

> ⚠ **Verify late-April and late-December deadlines.** If a computed
> deadline lands on or near late April or late December, confirm the
> court's actual closure against the per-year schedule published at
> **georgia.gov** / the **Administrative Office of the Courts (AOC)**,
> because a floated holiday can push a rollover the script does not
> capture.

## Named civil rules — quick reference

Run `python3 scripts/case-calendar.py --rules` for the canonical list.
Most commonly invoked (the script holds the exact day counts):

| Rule key | What it computes | Authority |
|---|---|---|
| `answer-due` | Answer after service of summons & complaint | O.C.G.A. § 9-11-12(a) |
| `open-default-as-of-right` | Open the default as of right (pay costs) | O.C.G.A. § 9-11-55(a) |
| `amended-pleading-response` | Respond to an amended pleading | O.C.G.A. § 9-11-15(a) |
| `interrogatory-response` | Interrogatory answers due | O.C.G.A. § 9-11-33(a) |
| `interrogatory-response-with-summons` | Interrogatories served with summons | O.C.G.A. § 9-11-33(a) |
| `rfp-response` | Response to Request for Production | O.C.G.A. § 9-11-34(b) |
| `rfp-response-with-summons` | RFP served with summons | O.C.G.A. § 9-11-34(b) |
| `rfa-response` | Response to Request for Admission (else **deemed admitted**) | O.C.G.A. § 9-11-36(a) |
| `rfa-response-with-summons` | RFA served with summons (else **deemed admitted**) | O.C.G.A. § 9-11-36(a) |
| `sj-motion-before-hearing` | SJ motion must be served *before* hearing | O.C.G.A. § 9-11-56(c) |
| `motion-response` | Response to a motion (typical) | USCR 6.2 |
| `dispossessory-answer` | Answer a dispossessory (eviction) summons | O.C.G.A. § 44-7-51(b) |
| `dispossessory-writ` | Writ of possession effective after judgment | O.C.G.A. § 44-7-55(a) |
| `motion-new-trial` | Motion for new trial | O.C.G.A. § 5-5-40(a) |
| `motion-jnov` | Motion for JNOV | O.C.G.A. § 9-11-50(b) |
| `notice-of-appeal` | Notice of appeal | O.C.G.A. § 5-6-38(a) |
| `set-aside-judgment` | Motion to set aside (certain grounds) | O.C.G.A. § 9-11-60(f) |
| `judgment-dormancy` | Judgment becomes dormant | O.C.G.A. § 9-12-60 |
| `revive-dormant-judgment` | Revive a dormant judgment | O.C.G.A. § 9-12-61 |
| `fbpa-demand` | FBPA written demand *before* filing suit | O.C.G.A. § 10-1-399(b) |

Key qualitative points the day counts encode:

- **Answer**: due 30 days after service (O.C.G.A. § 9-11-12(a)).
- **Default**: a case in default may be opened **as of right** (on
  payment of costs) within 15 days after default (O.C.G.A.
  § 9-11-55(a)); after that, only on the statutory showing.
- **Discovery responses**: 30 days, but a defendant served *with the
  summons* gets **45 days** after service of the summons
  (O.C.G.A. §§ 9-11-33 / 9-11-34 / 9-11-36). **Unanswered requests
  for admission are deemed admitted** (O.C.G.A. § 9-11-36(a)).
- **Summary judgment**: the motion must be served **at least 30 days
  before the hearing** (O.C.G.A. § 9-11-56(c)).
- **Dispossessory**: the tenant has **7 days** from service to answer
  (O.C.G.A. § 44-7-51(b)) — a sub-7-day-adjacent window where weekend
  / holiday handling matters.
- **Post-judgment**: motion for new trial, JNOV, and notice of appeal
  are each **30 days** (O.C.G.A. §§ 5-5-40, 9-11-50(b), 5-6-38(a)).
- **Dormancy / revival**: a judgment goes **dormant after 7 years**
  (O.C.G.A. § 9-12-60) and may be revived within **3 years** of
  dormancy (O.C.G.A. § 9-12-61).
- **FBPA**: a written **demand for relief** must be delivered **at
  least 30 days before** filing suit (O.C.G.A. § 10-1-399(b)); it is
  a prerequisite and does **not** toll the SOL.

## Statute of limitations — quick map

The day counts for multi-year SOLs are approximate (~365.25/yr);
always confirm the exact calendar date and check tolling/revival.

| Claim type | SOL | Authority | Rule key |
|---|---|---|---|
| Simple written contract | 6 years | O.C.G.A. § 9-3-24 | `sol-written-contract` |
| Credit-card debt (written cardmember agreement) | 6 years | O.C.G.A. § 9-3-24 | `sol-credit-card` |
| Open account / oral / implied | 4 years | O.C.G.A. § 9-3-25 | `sol-open-account` |
| Other contract (catch-all) | 4 years | O.C.G.A. § 9-3-26 | `sol-contract-catchall` |
| Personal injury | 2 years | O.C.G.A. § 9-3-33 | `sol-personal-injury` |
| Defamation / injury to reputation | 1 year | O.C.G.A. § 9-3-33 | `sol-defamation` |
| Trespass / damage to realty | 4 years | O.C.G.A. § 9-3-30 | `sol-realty` |
| Injury to / conversion / recovery of personalty | 4 years | O.C.G.A. §§ 9-3-31, 9-3-32 | `sol-personalty` |
| Fair Business Practices Act | 2 years | O.C.G.A. § 10-1-401 | `sol-fbpa` |
| FDCPA | 1 year | 15 U.S.C. § 1692k(d) | `sol-fdcpa` |
| FCRA | 2 years (from discovery; 5-yr repose) | 15 U.S.C. § 1681p | `sol-fcra-discovery` |
| TILA | 1 year | 15 U.S.C. § 1640(e) | `sol-tila` |

### Credit-card characterization — the live fight

A credit-card claim runs **6 years** as a *written contract* when the
plaintiff can produce the cardmember agreement and frame the card's
use as acceptance of those written terms (O.C.G.A. § 9-3-24). Where a
debt buyer **cannot** produce the written agreement and pleads the
claim as an **open account** or **account stated**, the **4-year** bar
of O.C.G.A. § 9-3-25 applies — often paired with a
proof / foundation defect. Identify which theory the complaint actually
pleads before computing the bar.

## Tolling and revival

- **Fraud**: O.C.G.A. § 9-3-96 tolls the period until the fraud is (or
  reasonably should have been) discovered.
- **New promise**: a new promise to pay a debt must be **in writing**
  to revive a barred claim (O.C.G.A. § 9-3-110).
- **Part payment**: a partial payment is treated as a new promise
  only when made on **written evidence** of the debt (O.C.G.A.
  § 9-3-112) — central in debt-buyer cases that rely on a recent
  payment to restart the clock.

## Examples

### "When is my answer due if I was served on Tuesday, April 15, 2025?"

```
$ python3 scripts/case-calendar.py --from 2025-04-15 --rule answer-due
Answer due — 30 days after service of summons and complaint
Deadline: ...
  From: Tuesday, April 15, 2025
  30 calendar days after
  Authority: O.C.G.A. § 9-11-12(a)
```

### "Is a credit-card debt that defaulted on March 15, 2019 time-barred?"

```
$ python3 scripts/case-calendar.py --from 2019-03-15 --rule sol-credit-card
SOL — credit-card debt on a written cardmember agreement ...
  From: Saturday, March 15, 2019
  ~6 years after
  Authority: O.C.G.A. § 9-3-24
```

If the plaintiff cannot produce the written agreement, also compute
the 4-year open-account bar:

```
$ python3 scripts/case-calendar.py --from 2019-03-15 --rule sol-open-account
```

### "List every named rule the calculator knows."

```
$ python3 scripts/case-calendar.py --rules
```

You can also compute an arbitrary interval:

```
$ python3 scripts/case-calendar.py --from 2025-04-15 --days 30 --mode calendar
$ python3 scripts/case-calendar.py --from 2025-04-15 --days 5 --mode court
```

## How `ga-deadlines` composes with the script

The skill body above is the reference. The arithmetic lives in
`scripts/case-calendar.py`, which:

- Encodes the predictable O.C.G.A. § 1-4-1 holidays and computes
  `ga_holidays(year)` for any year
- Implements the § 1-3-1(d)(3) roll-forward and the sub-7-day
  exclusion of intermediate weekends and holidays
- Provides `is_court_day(d)`, `add_calendar_days`, `add_court_days`
- Exposes a `RULES` dictionary mapping named keys to
  `(days, mode, description, authority)`

Use `--rules` for the canonical list and
`--from YYYY-MM-DD --rule <key>` for any specific computation.

## Composition

- For first-response timing (answer, default, defenses): `ga-first-30-days`
- For discovery-response and motion timing: `ga-discovery`
- For debt-claim SOL and credit-card characterization: `ga-consumer-debt`
- For dormancy, revival, and garnishment windows: `ga-post-judgment`
- For format of the resulting filing: `ga-statewide-format`
- For citation and date verification: `ga-fact-check`
