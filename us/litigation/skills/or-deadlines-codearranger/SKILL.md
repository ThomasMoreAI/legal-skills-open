---
name: or-deadlines-codearranger
title: Oregon Case Deadlines
description: Use this skill whenever the user asks about timing or deadlines in an Oregon civil case. Triggers include "when is my answer due", "when is the response brief due", "compute the deadline", "how many court days", "what's the reply deadline", "I was served — when do I have to answer", "when does my discovery response have to go out", "how long do I have to file a motion to vacate", "exemption claim deadline", "FDCPA statute of limitations", "UTPA statute of limitations", "is this deadline past". Computes court-day and calendar-day deadlines under ORCP 10 using ORS 187.010 holidays (with Saturday→Friday / Sunday→Monday observed-day rule), and covers FDCPA SOL, garnishment timing (ORS 18.600+), post-judgment (ORCP 71, ORCP 64, ORS 19.255 for appeals), and Oregon debt SOL. Deterministic date arithmetic is delegated to `scripts/case-calendar.py`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/or-court-docs/skills/or-deadlines
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Oregon Case Deadlines

This skill computes deadlines in Oregon civil cases — when to
answer, when to file or respond to motions, when to claim
exemptions, when to appeal, and the statutes of limitations
that bound new actions.

> **NOT LEGAL ADVICE.** Verify every deadline against the
> current rule and statute. The legislature can amend ORCP and
> ORS without notice.

## How time is computed in Oregon (ORCP 10)

**ORCP 10 A** — Computation:

- **Exclude the day of the triggering event** (the day of
  service, the day of filing, the day of the order)
- **Include the last day** of the period
- **If the last day falls on a Saturday, Sunday, or legal
  holiday**, the period extends to the next business day

**ORCP 10 B** — Intermediate weekends and holidays:

- **Periods less than 7 days**: exclude weekends and holidays
- **Periods of 7 days or longer**: include weekends and
  holidays

**ORCP 10 C** — 3-day mail rule:

- When service is by mail, **3 additional days** are added to
  any prescribed response period
- Applies only when the triggering act was service by mail; not
  if the triggering act was filing or order

### Oregon legal holidays (ORS 187.010)

| Holiday | Date |
|---------|------|
| New Year's Day | January 1 |
| Martin Luther King, Jr. Day | 3rd Monday of January |
| Presidents' Day | 3rd Monday of February |
| Memorial Day | Last Monday of May |
| Juneteenth | June 19 |
| Independence Day | July 4 |
| Labor Day | 1st Monday of September |
| Veterans Day | November 11 |
| Thanksgiving Day | 4th Thursday of November |
| Christmas Day | December 25 |

**Observed-day rule** (ORS 187.020):

- Saturday holiday → observed on the preceding Friday
- Sunday holiday → observed on the following Monday

Note: Oregon does NOT recognize the day after Thanksgiving as a
statewide holiday (unlike Washington). Some Oregon counties may
treat it as a courthouse closure day; verify locally.

## Deterministic computation

Use the bundled `scripts/case-calendar.py` for date arithmetic:

```bash
# Compute the answer deadline — 30 calendar days from service
# on 2025-04-15
python3 plugins/or-court-docs/scripts/case-calendar.py \
  --from 2025-04-15 --rule answer-due

# Compute a custom deadline — 14 court days after a given date
python3 plugins/or-court-docs/scripts/case-calendar.py \
  --from 2025-04-15 --days 14 --mode court

# List all known rules
python3 plugins/or-court-docs/scripts/case-calendar.py --rules
```

The script encodes ORCP 10 A/B/C and ORS 187.010/.020 exactly,
so the computation is deterministic.

## Deadlines by procedural posture

### Initial response (defendant)

| Trigger | Deadline | Authority |
|---------|----------|-----------|
| Personal service in Oregon | 30 days from service | ORCP 7 C(2) |
| Service on Oregon resident outside Oregon | 30 days | ORCP 7 C(2) |
| Service by publication | 30 days from completed publication | ORCP 7 D(6) |
| Substituted service | 30 days from completed mailing (mailing follows the substituted delivery) | ORCP 7 D(2)(b) |
| Motion under ORCP 21 in lieu of answer | 30 days; tolls answer until court rules | ORCP 21 D |

### Motion practice timing

| Event | Timing | Authority |
|-------|--------|-----------|
| Motion to compel — meet-and-confer prerequisite | Before filing | ORCP 46 A, local SLR |
| Motion to compel — response | 14 days (typical); check local SLR | Local SLR; default |
| Motion to dismiss — response | 14 days | Local SLR; default |
| Motion to dismiss — reply | 7 days | Local SLR; default |
| Summary judgment — motion | At least 60 days before trial | ORCP 47 C |
| Summary judgment — response | 20 days after service of motion | ORCP 47 C |
| Summary judgment — reply | 5 days after service of response | ORCP 47 C |
| Summary judgment — hearing | At least 11 days after filing reply | ORCP 47 C |
| Motion to reconsider — filed | "Reasonable time" — typically 10 days | ORCP 64 / 71 |

### Discovery

| Event | Timing | Authority |
|-------|--------|-----------|
| RFP response | 30 days (45 if served with summons) | ORCP 43 B |
| RFA response | 30 days (45 if served with summons) | ORCP 45 B |
| Deposition notice — party | 5 days | ORCP 39 B |
| Deposition notice — non-party | 7 days (subpoena required) | ORCP 39 B / 55 |
| Discovery cutoff (typical) | 30 days before trial; case-schedule order may vary | Case schedule |

### Post-judgment

| Event | Timing | Authority |
|-------|--------|-----------|
| Motion to set aside default | "Reasonable time"; not exceeding 1 year for ORCP 71 B(1)–(3) | ORCP 71 B |
| Motion to amend judgment | 10 days after entry of judgment | ORCP 64 |
| Notice of Appeal — circuit to Court of Appeals | 30 days from judgment entry | ORS 19.255 / ORAP 5.30 |
| Garnishment Challenge / Exemption | 30 days from notice of writ | ORS 18.700 et seq. |
| Bank levy challenge | 30 days from notice | ORS 18.700+ |
| Statement of attorney fees and costs | 14 days from judgment | ORCP 68 C(2) |
| Cost bill | 14 days from judgment | ORCP 68 C |
| Writ of garnishment issuance | After judgment is final and writ issued | ORS 18.605 |

### Arbitration

| Event | Timing | Authority |
|-------|--------|-----------|
| Arbitration hearing | Typically 90 days from assignment | Per SLR / arbitrator |
| Trial de novo request | 20 days from arbitration award | ORS 36.425 |
| Trial de novo fee-shifting cutoff | At trial de novo conclusion | ORS 36.425(5) |

## Statutes of limitations — Oregon

### Contract and debt

| Claim type | SOL | Authority |
|------------|-----|-----------|
| Written contract | **6 years** | ORS 12.080(1) |
| Open account / credit card | **6 years** | ORS 12.080(2)–(4) |
| Oral contract | **6 years** | ORS 12.080(1) |
| Statutory liability (UTPA, ORS 697, etc.) | 6 years (general) | ORS 12.080(2) |

### Tort

| Claim type | SOL | Authority |
|------------|-----|-----------|
| Personal injury (most) | **2 years** | ORS 12.110 |
| Fraud / mistake | 2 years from discovery; 10-year repose | ORS 12.110(1) |
| Defamation | 1 year | ORS 12.120(2) |
| Malicious prosecution | 1 year | ORS 12.140 |

### Real property

| Claim type | SOL | Authority |
|------------|-----|-----------|
| Real property | 10 years | ORS 12.040 |
| Quiet title | 10 years | ORS 12.040 |

### Judgments

| Event | Limit | Authority |
|-------|-------|-----------|
| Judgment lifespan | 10 years from entry, renewable | ORS 18.182 |
| Judgment renewal | Before original 10-year period expires | ORS 18.182 |

### Consumer protection

| Claim type | SOL | Authority |
|------------|-----|-----------|
| UTPA private action | **1 year from discovery; 6-year repose** | ORS 646.638(6) |
| FDCPA private action | **1 year from violation** | 15 USC § 1692k(d) |
| FCRA private action | 2 years from discovery; 5-year repose | 15 USC § 1681p |
| TILA private action | 1 year from violation (rescission: 3 years) | 15 USC § 1640(e); § 1635(f) |

### Collection agency / ORS 697

| Claim type | SOL | Authority |
|------------|-----|-----------|
| ORS 697.058 prohibited practices | 6 years (statutory) | ORS 12.080(2) |
| ORS 697.085 civil action | 6 years | ORS 12.080(2) |

## The 3-day mail rule, in practice

ORCP 10 C adds 3 days to any response period when service was
by mail. This rule trips up many practitioners. Examples:

- **Discovery response served by mail on April 1**: response
  due 30 + 3 = 33 days from April 1, i.e., **May 4**
- **Discovery response served by eService on April 1**:
  response due 30 days, i.e., **May 1** (no mail-rule
  addition; eService is electronic, not mail)
- **Motion served by mail on April 1**: response due
  [local SLR period] + 3 days from April 1

eService through File and Serve does NOT trigger the 3-day mail
rule. The 3-day rule applies only to actual paper mail under
ORCP 9 B (USPS).

## Computing examples

### Example 1: Answer to complaint

Defendant is personally served on **Wednesday, April 15, 2025**.

ORCP 7 C(2) — 30 calendar days to answer.

Day 1 = April 16 (day after service).
30 days from April 15, counting day 1 = April 16, is May 15.

May 15 is a Thursday — a business day. **Answer due May 15,
2025.**

### Example 2: Motion to compel with meet-and-confer

Discovery response served by **eService on Friday, May 16,
2025**. The response objects to RFPs 3, 5, 6.

ORCP 43 B — 30 days. No mail-rule addition (eService).

May 16 + 30 days = June 15. June 15 is a Sunday → next
business day. **Original response was timely; no extension to
the requesting party.**

Defendant decides to meet and confer. Meet-and-confer letter
sent **Monday, May 19, 2025**. Reasonable response window of
14 days = **Monday, June 2, 2025.**

If opposing party fails to supplement by June 2, motion to
compel can be filed.

### Example 3: SJ schedule

Trial date: **Monday, August 25, 2025.**

ORCP 47 C — motion filed at least 60 days before trial.

60 days before August 25 = June 26 (Thursday). **SJ motion
must be filed by June 26, 2025.**

Response due 20 days after service of motion. If motion was
filed and served on June 26, response due **July 16, 2025**.

Reply due 5 days after service of response. If response was
served on July 16, reply due **July 21, 2025.**

Hearing must be at least 11 days after filing of reply. If
reply was filed July 21, hearing must be on or after **August
1, 2025.**

(Use the calendar script to verify and adjust for any
intervening holidays.)

### Example 4: Notice of Appeal

Judgment entered **Tuesday, June 3, 2025.**

ORS 19.255 — 30 days from entry of judgment to file Notice of
Appeal.

June 3 + 30 days = July 3 (Thursday — Independence Day-1).
July 3 is a business day; July 4 is a holiday.

**Notice of Appeal due July 3, 2025.** (If June 3 were a
Friday, the deadline could fall on a weekend and extend.)

## Common deadline-computation mistakes

| Mistake | Consequence |
|---------|-------------|
| Including the day of the triggering event | Off-by-one; missed deadline |
| Forgetting the 3-day mail rule | Short-served response is treated as timely; surprise |
| Adding 3 days for eService | Not required; can backfire if you over-rely |
| Counting weekends in periods < 7 days | Over-counts; ORCP 10 B excludes intermediate weekends for short periods |
| Forgetting to extend if last day is weekend/holiday | Off-by-one; missed deadline |
| Confusing court days and calendar days | "Days" in ORCP is calendar unless specified court |
| Confusing observe-day rule | Saturday Independence Day observed on prior Friday; Sunday observed on following Monday |

## When in doubt, file early

When the deadline is close, file early. Late filings can be
fatal — ORCP 21 motions, Notice of Appeal, Motion to Vacate,
etc., are all strict deadlines and missing them is not curable
through the doctrine of substantial compliance.

For pro se filers: build a buffer. Aim for filings 5–7 days
before the deadline; that leaves room for technology issues,
clerk rejection, or last-minute corrections.

## References

- `scripts/case-calendar.py` — deterministic date arithmetic
- `or-law-references/references/civil-rules.md` — ORCP 10
  verbatim
- `or-law-references/references/or-ors-debt/ORS-12.md` (when
  populated) — verbatim ORS 12 text on SOLs
- `or-law-references/references/or-ors-debt/ORS-187.md` (when
  populated) — verbatim ORS 187 holiday list
