# I.R.C.P. 2.2 — Time Computation (Rule 6 is RESERVED)

> **NOT LEGAL ADVICE.** This file summarizes the time-computation method.
> Pull the verbatim rule text from the corpus and confirm every count
> before relying on a computed date.

Idaho computes time under **I.R.C.P. 2.2**. This is a defining quirk:
**I.R.C.P. 6 is "[Reserved]"** and carries no time-computation text. Do
**not** cite Rule 6 for counting days in an Idaho civil matter.

Verbatim rule text:
`../../id-law-references/references/court-rules/IRCP-civil-procedure.md`.

## The counting method

To count any period stated in **days** in the Idaho Rules of Civil
Procedure, a court order, or (unless otherwise provided) a statute:

1. **Exclude** the day of the act, event, or default that begins the
   period (e.g., the date the summons and complaint were served).
2. **Count every intervening day, including Saturdays, Sundays, and legal
   holidays.**
3. **Include** the last day of the period — **unless** it falls on a
   **Saturday, Sunday, or legal holiday**, in which case the period runs
   forward to the **end of the next day** that is none of those.

The legal holidays that trigger the roll-forward come from **Idaho Code
§ 73-108** — see `section-73-108-holidays.md`.

## The 3-day mail add-on

When a period runs from **service** of a paper and that service was made
by **mail**, I.R.C.P. 2.2 adds **3 days** to the period. Apply the add-on
**after** completing the underlying Rule 2.2 count of the base period.

> Confirm the current treatment of **electronic service** (iCourt /
> I.R.E.F.S.) under Rule 2.2 in the corpus — service-method add-ons are
> amended periodically and an e-service add-on may not be the same as the
> mail add-on.

## Worked example

Summons and complaint served by hand on a Friday; answer due in 21 days
(I.R.C.P. 12(a)(1)(A)):

- Exclude the day of service (Friday).
- Count 21 calendar days forward, including the intervening weekends.
- If day 21 lands on a Saturday, Sunday, or § 73-108 holiday, roll forward
  to the next day that is none of those.

If service had been **by mail**, add **3 days** to the 21 first, then
apply the weekend / holiday roll-forward to that later date.

## Forward vs. backward counts

Some periods are counted **backward** from a fixed event (e.g., a summary-
judgment motion must be served at least 28 days **before** the hearing —
I.R.C.P. 56(b)). The exclude-first / include-last logic and the weekend /
holiday roll still apply; `scripts/case-calendar.py` handles the direction
via a negative day count. See `named-rules.md`.
