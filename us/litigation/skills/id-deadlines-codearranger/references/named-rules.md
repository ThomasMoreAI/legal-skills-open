# Named Rules — `case-calendar.py` Keys with Authority

> **NOT LEGAL ADVICE.** Day counts can change by rule amendment. Confirm
> each count against the verbatim rule text in the corpus, and re-check
> this table against `scripts/case-calendar.py` after any corpus refresh.

These are the rule keys recognized by `scripts/case-calendar.py`. Run
`python3 scripts/case-calendar.py --rules` to print the live list. A
**negative** day count is counted **backward** from the supplied date
(e.g., backward from a hearing date). Verbatim rule text:
`../../id-law-references/references/court-rules/IRCP-civil-procedure.md`
(I.R.C.P.) and `IAR-appellate.md` (I.A.R.).

## Initial response

| Key | Days | Authority |
|---|---|---|
| `answer-due` | +21 | I.R.C.P. 12(a)(1)(A) |
| `response-amended` | +14 | I.R.C.P. 15(a)(3) |
| `summons-service` | +182 | I.R.C.P. 4(b)(2) |

## Discovery (30-day response window)

| Key | Days | Authority |
|---|---|---|
| `interrogatory-response` | +30 | I.R.C.P. 33(a)(1), 33(b)(2) (40-cap, incl. subparts) |
| `rfp-response` | +30 | I.R.C.P. 34(b)(2) |
| `rfa-response` | +30 | I.R.C.P. 36(a)(3) (failure deems admitted) |

## Summary judgment (counted BACKWARD from the hearing)

| Key | Days | Authority |
|---|---|---|
| `sj-motion-before-hearing` | −28 | I.R.C.P. 56(b) |
| `sj-response-before-hearing` | −14 | I.R.C.P. 56(b) |

(Separately, the SJ motion must be filed at least **90 days before trial**
— I.R.C.P. 56(b); that cutoff is keyed to the trial date, not in the
script.)

## Motion practice

| Key | Days | Authority |
|---|---|---|
| `motion-notice` | +14 | I.R.C.P. 7(b)(3) (Notice of Hearing) |

## Post-judgment

| Key | Days | Authority |
|---|---|---|
| `new-trial-motion` | +14 | I.R.C.P. 59(b), 59(e) |
| `reconsideration` | +14 | I.R.C.P. 11.2(b) |
| `relief-judgment-outer` | +180 | I.R.C.P. 60(c)(1) (Rule 60(b)(1)-(3) outer 6-month) |
| `memorandum-costs` | +14 | I.R.C.P. 54(d) |
| `appeal` | +42 | I.A.R. 14(a) (cross-appeal: I.A.R. 15) |

## Statutes of limitation (anniversary-date approximations)

These keys approximate the SOL by day count for screening only; the
controlling bar date is the **calendar anniversary** under the cited Idaho
Code section. See `sol-table.md`.

| Key | Period | Authority |
|---|---|---|
| `sol-written-contract` | 5 years | Idaho Code § 5-216 |
| `sol-oral-contract` | 4 years | Idaho Code § 5-217 |
| `sol-open-account` | 4 years | Idaho Code § 5-217; accrual § 5-222 |
| `sol-personal-injury` | 2 years | Idaho Code § 5-219 |
| `sol-fraud-discovery` | 3 years | Idaho Code § 5-218(4) |
| `sol-judgment` | 11 years | Idaho Code § 5-215 |

## Federal SOLs and validation window (consumer matters)

| Key | Period | Authority |
|---|---|---|
| `sol-fdcpa` | 1 year | 15 U.S.C. § 1692k(d) |
| `sol-fcra-discovery` | 2 years (5-yr repose) | 15 U.S.C. § 1681p |
| `sol-tila` | 1 year | 15 U.S.C. § 1640(e) |
| `fdcpa-validation-period` | +30 | 15 U.S.C. § 1692g; 12 CFR § 1006.34 |

For a period that runs from **service by mail**, add the **3-day**
I.R.C.P. 2.2 mail add-on after the underlying count (see
`rule-2.2-time-computation.md`).
