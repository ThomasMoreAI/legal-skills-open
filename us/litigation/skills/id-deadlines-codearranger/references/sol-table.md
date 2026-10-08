# Idaho Statutes of Limitation — by Claim Type

> **NOT LEGAL ADVICE.** Limitations periods run on the **calendar
> (anniversary) date** and turn on accrual, tolling, and revival, all of
> which are fact-dependent. Verify the current period and accrual rule for
> the specific claim before relying on this chart.

Idaho's civil limitations periods live in **Idaho Code Title 5, Chapter
2**. Pull the verbatim statute text from:
`../../id-law-references/references/id-statutes-debt/Title5-limitations.md`.

## Limitations chart

| Claim family | Period | Authority |
|---|---|---|
| Written contract / instrument in writing | 5 years | Idaho Code § 5-216 |
| Oral / unwritten contract | 4 years | Idaho Code § 5-217 |
| Open account / account not in writing | 4 years | Idaho Code § 5-217; accrual § 5-222 |
| Personal injury | 2 years | Idaho Code § 5-219 |
| Fraud (from discovery) | 3 years | Idaho Code § 5-218(4) |
| Action upon a judgment | 11 years | Idaho Code § 5-215 |

## Notes on accrual and revival

- **Open / running accounts.** Idaho Code **§ 5-222** governs when a
  cause of action on a mutual, open, and current account accrues — the
  limitations clock generally runs from the **last item** on the account.
  Confirm the section's exact treatment in the corpus.
- **Fraud.** The 3-year period under § 5-218(4) runs from **discovery** of
  the facts constituting the fraud — not necessarily from the wrongful act.
- **Judgments.** The 11-year period under § 5-215 governs an action **upon
  a judgment**; renewal / revival of the judgment itself is a separate
  question — check current law.
- **Accrual, tolling, and any revival** (e.g., by written acknowledgment or
  part-payment) are fact-dependent and can move the bar date. Do not treat
  a computed anniversary date as final without checking these.

## Computing the date with the script

`scripts/case-calendar.py` carries `sol-*` rule keys that approximate the
anniversary by day count for a rough estimate. Treat that output as a
**screening aid only** — the controlling bar date is the calendar
anniversary of accrual under the cited Idaho Code section. See
`named-rules.md` for the full list of `sol-*` keys.

## Federal overlay (consumer matters)

For consumer-debt matters, federal limitations periods may also apply
(e.g., FDCPA, FCRA, TILA). Those are computed separately under the federal
statutes — see `id-consumer-debt` and the federal corpus. The Idaho Code
periods in this chart govern the state-law claims and defenses.
