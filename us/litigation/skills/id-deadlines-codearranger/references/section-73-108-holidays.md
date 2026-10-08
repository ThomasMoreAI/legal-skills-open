# Idaho Legal Holidays — Idaho Code § 73-108

> **NOT LEGAL ADVICE.** This file lists the holidays that trigger the
> I.R.C.P. 2.2 roll-forward. Confirm the operative set in the corpus and
> in `scripts/case-calendar.py` before relying on a date.

The legal holidays that cause a deadline to roll forward under I.R.C.P.
2.2 are fixed by **Idaho Code § 73-108**. Verbatim statute text:
`../../id-law-references/references/id-statutes-debt/holidays-Title73.md`.

## The § 73-108 holiday list

| Holiday | Date rule |
|---|---|
| New Year's Day | January 1 (fixed) |
| Martin Luther King, Jr. — Idaho Human Rights Day | 3rd Monday in January |
| Washington's Birthday | 3rd Monday in February |
| Memorial Day | Last Monday in May |
| Independence Day | July 4 (fixed) |
| Labor Day | 1st Monday in September |
| Columbus Day | 2nd Monday in October |
| Veterans Day | November 11 (fixed) |
| Thanksgiving Day | 4th Thursday in November |
| Christmas Day | December 25 (fixed) |

## Idaho specifics to flag

- **Columbus Day IS a state legal holiday** in Idaho (2nd Monday in
  October) — roll deadlines forward off it.
- **Juneteenth is NOT a § 73-108 state legal holiday.** Do not roll a
  deadline forward off June 19 unless the corpus says otherwise.
- The **day after Thanksgiving** is **not** a § 73-108 state legal
  holiday.
- The January observance is named **"Martin Luther King, Jr. — Idaho
  Human Rights Day."**

## Observed-day shift

When a § 73-108 holiday falls on a weekend, it is observed on an adjacent
weekday, and that **observed** day is the one that triggers the
roll-forward:

- A holiday that falls on a **Saturday** is observed the **preceding
  Friday**.
- A holiday (other than Sunday itself) that falls on a **Sunday** is
  observed the **following Monday**.

`scripts/case-calendar.py` computes the year-by-year holiday set,
including this observed-day shift, for any year. Treat the script and the
corpus statute text as authoritative over this summary table.
