# Domain Coverage Checklist, israeli-attendance-wage-checker

Generated: 2026-08-11. Revised 2026-08-25 (v2): the payslip route was promoted from a reference-only
topic into a first-class entry point (Step 1b), because most users arrive holding a payslip and no
timesheet. Every statutory row was verified against the source's own text layer on
he.wikisource.org, sliced directly from the rendered page so each quoted snippet is contiguous.
Aggregator pages were used for taxonomy discovery only and are not cited for any rule.

## The framing that must survive into the skill

This skill starts from HOURS and stops at GROSS OWED. It is not a payroll calculator and must never
drift into tax, National Insurance, or net pay. Its distinctive value is threefold: the daily-then-
weekly ordering, the fact that the premium base includes all supplements, and the procedural burden
shift when the employer kept no ledger.

## Must cover (core)

- [ ] The applicability gate, `סעיף 30`, all six exclusion classes enumerated, asked BEFORE any
      arithmetic. If it applies, no premium is owed at all and every figure is meaningless.
- [ ] Definition of working hours, `סעיף 1`: at the employer's disposal, including short agreed
      breaks and toilet breaks, excluding the `סעיף 20` meal break.
- [ ] Definition of overtime, `סעיף 1`: two INDEPENDENT limbs, daily and weekly.
- [ ] Night work, `סעיף 1`: at least two hours between 22:00 and 06:00.
- [ ] Daily maximum 8 hours, `סעיף 2(א)`; 7 hours on night work, eve of weekly rest, eve of a holiday
      not worked, `סעיף 2(ב)`. NOT changed by the 2018 order.
- [ ] Statutory week 45 hours, `סעיף 3`, kept distinct from the operative 42.
- [ ] Operative week 42 hours since the 2018 extension order, implemented by shortening ONE defined
      day, not by trimming every day. Some public bodies at 40.
- [ ] Overtime rates, `סעיף 16(א)`: 125 percent for the first two overtime hours OF THAT DAY, 150
      percent thereafter. The two-hour tier resets daily.
- [ ] Weekly-rest premium, `סעיף 17(א)(1)`: 150 percent, plus compensating rest per the permit.
- [ ] The rest-day split by pay basis: monthly salaried get the premium element on top plus PAID
      compensating rest; hourly or daily get the full 150 percent with UNPAID compensating rest.
- [ ] Regular wage base, `סעיף 18`: includes ALL supplements the employer pays.
- [ ] Weekly rest is at least 36 continuous hours, `סעיף 7`.
- [ ] Breaks, `סעיף 20`: three quarters of an hour on a day of six hours or more, including one
      continuous half hour; half an hour on the eve of the weekly rest or a holiday.
- [ ] Paid-break rule, `סעיף 20`: a break of half an hour or more counts as working time where the
      employee's presence was necessary and the employer required him to stay.
- [ ] Eight hours between working days, `סעיף 21`, reported as a compliance flag not an entitlement.
- [ ] Employer's ledger duty, `סעיף 25`, kept on an ongoing basis with hours actually worked.
- [ ] Burden of proof, `סעיף 26ב(א)` of חוק הגנת השכר, WITH both limits: the 15 weekly / 60 monthly
      cap in `סעיף 26ב(ב)`, and the employee's own minimal factual version.
- [ ] Inclusive wage treated as regular wage only, `סעיף 5` of חוק הגנת השכר.
- [ ] Payslip fields, the Schedule via `סעיף 24`: hours actually worked, value of a regular hour, and
      itemised overtime and rest-day premium with units and amounts. IN BODY at Step 1b since v1.2.0.
- [ ] Presumption from a missing or incomplete payslip, `סעיף 26ב(ג)`, WITH all three qualifiers: it
      is rebuttable, it attaches only to the enumerated causes, and leave/recuperation/travel appear
      as triggers rather than as entitlements this skill prices. IN BODY at Step 1b since v1.2.0.
- [ ] Payslip internal-consistency checks that need no timesheet: hours times hourly value against
      the regular-wage line; premium total divided by premium units against 125 and 150 percent;
      hours line against the daily and weekly bounds.
- [ ] Wage due date, `סעיף 9`, and delayed-wage compensation, `סעיף 17`, as the HIGHER of the two
      formulas.
- [ ] The halana clock, `סעיף 17א`: one year, or 60 days from receipt, WHICHEVER IS EARLIER,
      extendable to 90 days, and distinct from the wage claim itself.
- [ ] Court discretion to reduce or cancel halana, so the figure is a claim ceiling not an award.
- [ ] Minimum-wage floor (added v1.3.0): a dated BTL table in `rates-and-tiers.md` section 8, the
      182 versus 186 divisor rule, the narrower `סעיף 3(ב)` base of חוק שכר מינימום (NOT the `סעיף 18`
      premium base), and proration for part-time (`סעיף 2(ב)`) and absence (`סעיף 2(ג)`).
- [ ] Absence months (added v1.3.0): reserve-duty, sick, leave and holiday days are not hours worked;
      the reserve-duty payment is its own Schedule line, computed by BTL from the 3 prior months, and is
      a lawful residual in check 1. `records-and-remedies.md` section 8.
- [ ] Breaks deducted only when actually given; automatic deductions, rounding and planned-versus-
      punched hours are questions about the record (added v1.3.0).

## Should cover (advanced / edge cases)

- [ ] Overtime inside the weekly rest is CUMULATIVE, not multiplicative.
- [ ] Overtime caps from the general permit, and that hours beyond them are still owed their premium.
- [ ] Night-shift weekly ceiling.
- [ ] Rest in lieu of pay, `סעיף 16(ב)` and `סעיף 17(ב)`, monthly-salaried only, not commutable.
- [ ] Piece-rate variants of both `סעיף 16` and `סעיף 17`.
- [ ] Global overtime (`גמול גלובלי`), its cumulative conditions, and that excess actual overtime is
      still owed. Flag, do not validate.
- [ ] No hour-for-hour netting of a short hour against an extra hour.
- [ ] Part-timers on fixed days: only the daily ceiling bites.
- [ ] Shift supplements folding into the overtime base.
- [ ] Youth under 18: separate daily and weekly ceilings and a night-work prohibition.
- [ ] Holiday interaction with holiday pay for hourly workers compelled to work.
- [ ] Sector regimes (guarding, hotels and restaurants, manpower contractors) flagged, not computed.
- [ ] Wartime temporary provisions relaxing the caps, so a reconciliation covering such a period does
      not report a breach that was permitted.

## Out of scope (explicit, with rationale)

- Gross-to-net: income tax, National Insurance, health tax, pension, `שווי רכב`. Owned by
  `israeli-payroll-calculator`.
- Severance, notice pay, and end-of-employment settlements.
- Annual leave, recuperation and travel as standalone entitlements. They appear only as
  `סעיף 26ב(ג)` presumption triggers.
- General employee rights and dismissal procedure: `israeli-workplace-rights-navigator`.
- Contract drafting: `israeli-employment-contracts`.
- Teacher payroll and foreign-caregiver payroll: dedicated skills exist; reference, do not
  reimplement.
- Filing a claim, pleadings, court fees, representation.

## Known bad figures (secondary sources that are wrong)

- "120 percent for the first two overtime hours." The statute says 125 percent (`1 1/4`). 120 is a
  branch-agreement figure and never the statutory floor.
- **A transcription reading `לא פחות מ־1/4 מהשכר הרגיל`.** The source renders the mixed fraction
  `1 1/4`. Dropping the leading `1` turns 125 percent into 25 percent, an error by a factor of five.
  This was caught during authoring in a research output and is the reason every rate snippet here was
  re-sliced from the rendered page rather than trusted second hand.
- "The work week is 43 hours" or "45 hours" as the operative basis. 45 is the statute and is still
  formally in force; 43 was the pre-2018 practical basis; 42 has been the basis since 2018.
- "Overtime is computed from the monthly hour total." It is daily first, then weekly. A worker can be
  owed overtime in a week totalling exactly the standard hours.
- "No records means the employee wins everything." `סעיף 26ב(ב)` caps the shifted burden at 15 weekly
  or 60 monthly overtime hours, and the employee must still give a minimal factual version.
- "187.5 percent / 225 percent for overtime on Shabbat" as a general rule. The cumulative method is
  the one the national labour court has reaffirmed; those figures belong to a different fact pattern
  involving a night-shift supplement folded into the base.

## Open items for the next update

1. The exact combined percentages for overtime falling inside the weekly rest, per pay basis, from a
   primary source rather than from a summary. The skill currently states the components and the
   cumulative principle rather than a single combined figure, which is the honest position until
   this is closed.
2. CLOSED 2026-10-01 for the routine caps (12 / 16 / 58, general permit of 14.03.2018, via Kol Zchut).
   Still open: the text and expiry of any 2026 wartime temporary permit, which was not located.
3. CLOSED 2026-10-01: the statute (`סעיף 1` of חוק שכר מינימום) still says 186; the 2018 steering
   committee and the Ministry of Labour say 182, with no enforcement against an employer paying on 186;
   BTL publishes both. The skill tests a full-time 42-hour hourly worker at 182, treats the band
   between the two as disputed, and compares a monthly employee against the monthly figure.
4. A monthly-salaried worker whose rest-day work was a sixth day ON TOP of a full week. Step 4, the
   Step 1b check 2 reading and the script all price the rest-day line at the 50 percent premium element,
   which assumes the salary already covers the day. Whether more is owed when it does not, and from what
   source, is unresolved. Raised by the 2026-10-01 expert review; resolve next cycle.
5. Overtime inside the weekly rest is cumulative (rates-and-tiers section 4). Since v1.3.1 the script and
   Step 6 FLAG it as not checked rather than pricing it; Kol Zchut cites ע"ע 38313-03-18 for 175 / 200 percent. Verify against the
   judgment and either implement or flag it in the script output.

## Out-of-scope re-litigation, 2026-10-01

- Gross-to-net: users ask constantly, but `israeli-payroll-calculator` owns it. Stays out.
- Severance, notice: different trigger and evidence. Stays out.
- Annual leave, recuperation, travel valuation: users do ask. Hand-off now named
  (`israeli-workplace-rights-navigator`), which closes the carry-forward item. Pricing stays out.
- Holiday pay (דמי חגים): an hourly worker's September payslip commonly lacks it. Now flagged in
  `records-and-remedies.md` section 8 as a possible gap; pricing stays out because it turns on
  qualifying conditions this skill does not collect.
- Reserve-duty pay: brought partly IN scope as absence handling. Pricing the payment stays out
  (`israeli-miluim-manager`, BTL calculator).
- Minimum wage figure: REOPENED and now carried (users ask it in the same breath as overtime).
- Contract drafting, teacher and caregiver payroll, claims and representation: stay out.

## Authoritative sources

- https://he.wikisource.org/wiki/חוק_שעות_עבודה_ומנוחה
- https://he.wikisource.org/wiki/חוק_הגנת_השכר
- https://www.gov.il/BlobFolder/dynamiccollectorresultitem/extention-order-short-week-2018/he/extention-order-short-week-2018.pdf (text layer mangles Hebrew RTL digits; trusted for the 42 only)
