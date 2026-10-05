# Changelog

## 1.1.0 (2026-10-01)

First full audit since launch.

Corrections:

- The audit threshold. No s.19(ג) amount was gazetted for 2015 to 2025 (the 2014 notice gave
  1,172,933 NIS and the 2026 notice, 1,380,630 NIS, says it accounts for the 2014 to 2025 updates),
  and the statute does not settle which year's amount a year's turnover is measured against. The
  skill told the agent to "take that year's gazetted amount", which does not exist, and
  `band_check.py` returned CANNOT DETERMINE for every live cycle, including its own example. Both
  now report a zone for the 2024 and 2025 reports: audit required on every reading, on none, or
  unsettled with the conservative course stated. The script's comment also misdated the 2026
  notice; it is dated 12.2.2026 and was published on 11.3.2026.
- The bookkeeping band is measured on the previous year's receipts (the Second Schedule's
  "מחזור"), so the script now separates the books kept during the report year from the next
  year's.
- The reduced fee tier. Fee schedule item 2(ד) settles which year's turnover governs (the verbal
  report for the last year whose report fell due before the fee year), so the skill no longer says
  the test is unknowable. The script no longer decides the tier from the wrong year's turnover, and
  keys the fee on the year the application actually requires.
- Donor naming. The anonymity ceiling is 100,000 NIS a year (Forms Regulations reg. 7א(ב)); the
  20,000 NIS figure is the donor-register threshold. Added the 50,000 NIS and 20% must-name rule.
- A donation with a full name but no ID can now be attributed through a supplementary report.
- Two-year certificates exist (Registrar letter of 28.5.2024); the reference said none could be
  confirmed.
- The retracted "interim status" wording survived in a Gotcha and the domain checklist. Removed.
- Step 1 pointed to step 8 for the chalatz track; it is step 10.

Added:

- The 500,000 NIS financial-report filing exemption (reg. 7(ה)(2)), with the report still going
  to the audit committee and the assembly, and the Form 7א Annex 1 and 2 route for the s.36(ב)
  and s.36א statements.
- Statutory disqualifications on the board and audit committee (s.32 and every s.33(א) ground), board pay (s.26א) and
  the prohibited-distribution rule (s.34ג), and the Registrar's 14.6.2026 supervision drive on
  family ties (relatives at most 10% of staff or payroll).
- The s.38 two-week change notices, including lawsuits.
- The online gate requiring up to four earlier years of reports, and the separate certificate
  request.
- The majority-foreign-funding duty under s.5א of the Disclosure Duty Law.
- Working back from the accountant's quota date to the assembly and audit-committee dates.
- `references/donor-rules.md` and `references/refusal-path.md`, which take the donor-naming rules
  and the full refusal procedure out of the body to stay under the word cap.
- `band_check.py` always prints the quarterly foreign-donation duty, which has no turnover gate.

## 1.0.1 (2026-09-09)

Corrects the lesser-confirmation paragraph in the refusal step, which was published with three
errors found in post-publication expert review:

- The Registrar's own service page names it `אישור על קבלת מסמכים`. The skill said
  `אישור על הגשת מסמכים`, a form used only by a superseded page.
- Its documented population is a new amuta, or one that has not carried on continuous activity for
  two years, not an established amuta whose certificate was refused. The earlier text generalised
  an unverified rule that the skill's own checklist records under "do not invent".
- The claim that many funders accept it as an interim was unsourced, and state support decisions
  condition support on the proper management certificate itself.

Also hardens `scripts/band_check.py` against negative turnover and implausible certificate years.

## 1.0.0 (2026-09-09)

Initial release.
