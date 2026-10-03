# Cal. Code Civ. Proc. §§ 12-13 — Time Computation

- Citation: Cal. Code Civ. Proc., §§ 12-13
- Code: Code of Civil Procedure
- Subject: Computation of time periods in civil practice
- Source: https://leginfo.legislature.ca.gov/faces/codes_displayexpandedbranch.xhtml?tocCode=CCP
- Last verified: 2026-05-13

> Authored from canonical California statutory sources; verify
> against leginfo.legislature.ca.gov before relying.

## Overview

CCP §§ 12, 12a, 12b, and 12c provide California's general
time-computation framework. § 12 sets the basic rule (exclude
first day, include last); § 12a extends the period when the
last day falls on a judicial holiday; § 12c defines what
"court day" means.

These rules govern unless a specific statute or rule of court
provides otherwise.

## § 12 — Computation of time; general rule

The time in which any act provided by law is to be done is
computed by excluding the first day, and including the last,
**unless the last day is a holiday, and then it is also
excluded**.

### Practical application

- Day 0 = the triggering event (service of complaint, ruling,
  etc.)
- Day 1 = the first day after the triggering event
- Day N = the final day of the period
- If Day N is a weekend or judicial holiday → extend to next
  court day (§ 12a)

### Worked example — answer due

Service on Wednesday, April 15:

- Day 1 = Thursday, April 16
- Day 30 = Friday, May 15
- May 15, 2026 falls on a Friday (a court day) → answer due
  May 15

Service on Wednesday, December 11:

- Day 30 = Friday, January 10
- January 10 falls on a court day → answer due January 10

Service on Friday, December 15:

- Day 30 = Sunday, January 14
- January 14 is a weekend → extend to Monday, January 15

## § 12a — Holidays; computation

**(a)** If the last day for the performance of any act provided
or required by law to be performed within a specified period of
time is a holiday, then such period is hereby extended to and
including the next day which is not a holiday.

**(b)** "Holiday" as used in this section includes all day on
Saturdays, all holidays specified in Government Code Section
6700, and the day after Thanksgiving as specified in Government
Code Section 6700.

### California judicial holidays (CCP § 135 + Govt. Code § 6700)

The full list of California judicial holidays is:

| Holiday | Date | Govt. Code citation |
|---|---|---|
| New Year's Day | January 1 | § 6700(a)(1) |
| Martin Luther King Jr. Day | 3rd Monday of January | § 6700(a)(2) |
| Lincoln's Birthday | February 12 | § 6700(a)(3) |
| Presidents' Day | 3rd Monday of February | § 6700(a)(4) |
| Cesar Chavez Day | March 31 | § 6700(a)(13) |
| Memorial Day | Last Monday of May | § 6700(a)(6) |
| Juneteenth | June 19 | § 6700(a)(15) (added 2022) |
| Independence Day | July 4 | § 6700(a)(7) |
| Labor Day | 1st Monday of September | § 6700(a)(9) |
| Veterans Day | November 11 | § 6700(a)(11) |
| Thanksgiving | 4th Thursday of November | § 6700(a)(12) |
| Day after Thanksgiving | 4th Friday of November | § 6700(a)(14) |
| Christmas | December 25 | (per § 6700) |

**California-distinctive**: California recognizes the day after
Thanksgiving as a state holiday under Govt. Code § 6700(a)(14)
— Oregon does NOT, and many other states do not. California
also retains Lincoln's Birthday (Feb 12) and added Juneteenth
in 2022.

### Observed-day rule (weekend shift)

When a fixed-date holiday (New Year's, July 4, etc.) falls on
a weekend, the observed holiday shifts:

- Saturday → preceding Friday
- Sunday → following Monday

For court-day purposes, the OBSERVED day is the holiday.

## § 12b — Half-holidays

Generally treats half-holidays as full holidays for purposes of
filing deadlines.

## § 12c — "Court day" definition

**(a)** "Court day" means any day other than a Saturday, Sunday,
or other judicial holiday.

### Court days vs. calendar days

This is the foundational distinction in California time
computation:

- **Calendar day**: every day on the calendar.
- **Court day**: any day except Saturday, Sunday, or judicial
  holiday.

| Period stated as "X days" | Treat as |
|---|---|
| Without modifier (statute / rule says only "X days") | Usually calendar days |
| "X court days" | Court days |
| "X calendar days" | Calendar days |
| CCP § 1005(b) ("at least 16 court days before") | Court days |
| CCP § 437c(a)(2) ("at least 75 days before") | Calendar days |

## § 13 — Single-day computation

The time in which any act provided by law is to be done is
computed exclusive of the first day and inclusive of the last,
unless the last day is a holiday, and in that case it is also
excluded.

## Computation examples (using `scripts/case-calendar.py`)

### Motion notice (16 court days)

```
$ python3 scripts/case-calendar.py --from 2026-05-13 \
       --rule motion-notice-min
Minimum notice period for motions: 16 court days before the hearing (CCP § 1005(b))
Deadline: Tuesday, April 21, 2026
  From: Wednesday, May 13, 2026
  16 court days before
  Authority: Code Civ. Proc., § 1005(b)
```

If the hearing is May 13, the motion must be served and filed
by April 21 (counting back 16 court days, with no holidays in
that window).

### Answer due (30 calendar days)

```
$ python3 scripts/case-calendar.py --from 2026-04-15 \
       --rule answer-due
Answer due after personal service in California
Deadline: Friday, May 15, 2026
  From: Wednesday, April 15, 2026
  30 calendar days after
  Authority: Code Civ. Proc., § 412.20(a)(3)
```

## Common pitfalls

### Pitfall 1: Forgetting that motion deadlines use court days

CCP § 1005(b) requires "at least 16 court days" notice. Forgetting
to use court days (vs. calendar days) shaves several days off
the actual deadline.

### Pitfall 2: Forgetting day-after-Thanksgiving in CA

Many states do NOT recognize the day after Thanksgiving as a
judicial holiday. California DOES (Govt. Code § 6700(a)(14)).
A deadline that would otherwise fall on the Friday after
Thanksgiving extends to the following Monday.

### Pitfall 3: Forgetting Cesar Chavez Day (March 31)

CA-specific holiday (Govt. Code § 6700(a)(13)). Many federal
and out-of-state practitioners miss this.

### Pitfall 4: Forgetting Lincoln's Birthday (Feb 12)

Still observed by California for state-employee and judicial
holiday purposes. Even though many federal jurisdictions have
folded Lincoln's Birthday into Presidents' Day, California
retains both.

### Pitfall 5: SJ motion 75 days is CALENDAR days

CCP § 437c(a)(2) requires 75 days notice, which is calendar
days — NOT court days. Don't conflate with § 1005(b)'s 16
court days.

## Cross-references

- `CCP-Motions-1005-to-1020.md` — § 1005(b) court-day framework
- `CCP-Pleadings.md` — § 437c summary judgment 75-day notice
  (calendar days)
- `../../../ca-deadlines/SKILL.md` — workflow that uses these
  rules
- `../../../../scripts/case-calendar.py` — computational helper
  with all named CA rules and the Govt. Code § 6700 holiday
  calendar
