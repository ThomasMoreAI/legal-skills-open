# Rates, tiers, and the two rest-day regimes

Read this before computing any figure. Every rate here is the statutory floor. A collective
agreement or an extension order can be more generous, never less, so where the user's workplace has
one, it governs and this file is the fallback.

## 1. The bounds

| Bound | Value | Source |
|---|---|---|
| Working day | **8 hours** | `סעיף 2(א)` |
| Working day, night work / eve of weekly rest / eve of a holiday not worked | **7 hours** | `סעיף 2(ב)` |
| Working week, **statutory** | **45 hours** | `סעיף 3` |
| Working week, **operative in the economy since 2018** | **42 hours** | 2018 extension order |
| Working week, public bodies in the later framework agreement | 40 hours | framework agreement, ask whether it applies |
| Weekly rest | at least **36 continuous hours** | `סעיף 7` |
| Minimum gap between working days | **8 hours** | `סעיף 21` |

The 2018 order shortened the week by removing **one hour on a single defined and fixed day**, the
`יום מקוצר`, rather than trimming every day. **It did not change the daily maximum**, which is why
`סעיף 2` still reads 8 hours. An agent that "spreads" the reduction across the week will compute the
daily overtime threshold wrongly on four days out of five.

Say which weekly basis you are applying and for which period. A user reconciling a payslip from
before April 2018 needs the basis that applied then, not today's.

## 2. The premium tiers

| Bucket | Rate | Source |
|---|---|---|
| Ordinary hours | 100 percent | |
| First **two** overtime hours **of that day** | **125 percent** | `סעיף 16(א)` |
| Each overtime hour after them, same day | **150 percent** | `סעיף 16(א)` |
| Hours in the weekly rest | **150 percent** | `סעיף 17(א)(1)` |

The statute renders these as the mixed fractions `1 1/4` and `1 1/2`. A transcription that drops the
leading `1` produces 25 percent and 50 percent, understating by a factor of five. If you ever see a
quoted snippet reading `לא פחות מ־1/4 מהשכר הרגיל`, it has been mis-transcribed.

### Three rules that decide the answer

1. **The two-hour tier resets daily.** `שבאותו יום` is in the text. It is not a monthly allowance.
2. **Daily first, then weekly.** Overtime is defined against the daily bound and the weekly bound as
   two independent limbs (`סעיף 1`). Count each day's excess first; then take the remaining ordinary
   hours and count what exceeds the weekly bound. Never start from a monthly total. A worker can be
   owed overtime in a week that totals exactly the standard hours.
3. **The base includes supplements.** `סעיף 18`: for sections 16 and 17, `שכר רגיל` includes **all
   the supplements the employer pays the employee**. Computing the premium off bare base salary is
   the most common way a shortfall is manufactured on a payslip that otherwise looks compliant.

## 3. The rest day, which splits by pay basis

Same hours, two different owed figures. Get the pay basis before answering.

| | Monthly salaried | Hourly or daily paid |
|---|---|---|
| The day itself | Already covered by the monthly salary | Not otherwise paid |
| Marginal entitlement for hours in the weekly rest | The **premium element on top** of the salary already covering the day | The **full 150 percent** of the regular hourly wage |
| Compensating rest | Given. Treated as **paid** in practice (not deducted from salary or leave) | Given. Treated as **unpaid** unless an agreement provides otherwise |

**Sourcing caution on that last row.** `סעיף 17(א)(2)` requires compensating rest but is **silent on
whether it is paid**. The paid-for-monthly / unpaid-for-hourly split is settled labour-court practice
rather than statutory text, and it is NOT in this skill's evidence file. State it as practice, not as
a provision, and do not quote a section number for it.

`סעיף 17(ב)` separately lets an employer of a monthly-or-longer-salaried employee give **an hour and
a half of rest** for each rest-day hour worked, in place of the money. Compensating rest cannot be
commuted to cash and is not redeemable on termination.

## 4. Overtime inside the weekly rest

Where overtime hours fall **within** the weekly rest, the entitlements are **cumulative**, not
multiplicative: the rest-day element and the overtime element are added. Do not multiply 150 percent
by 125 percent. A multiplicative reading circulates and is wrong; the national labour court has
reaffirmed the cumulative method.

Because the exact combined figures depend on the pay basis and on whether an extension order applies,
state the components rather than asserting a single combined percentage, and show the arithmetic so
the user can check it against their own payslip.

For orientation only: Kol Zchut reports that in ע"ע (ארצי) 38313-03-18 the national labour court put
the first two overtime hours on the weekly rest at 175 percent (50 + 125) and later hours at 200
percent (50 + 150). This skill has NOT verified that against the judgment itself, and neither the
script nor the calculator prices it. Treat it as a pointer, say the computed rest-day figure is a
floor, and do not present 175 or 200 percent as settled.

## 5. What to flag as unlawful, separately from the money

Hours worked beyond the permitted caps are **still owed their premium**. The illegality is a separate
finding. Report it in its own section so the user does not read a compliance breach as an extra
entitlement, or an entitlement as permission.

Flag at least:

- A gap of less than 8 hours between one working day and the next (`סעיף 21`).
- A working day that, including overtime, exceeds the permitted ceiling.
- A working week exceeding the permitted overtime count.
- Night-shift patterns beyond what the permits allow.

The caps sit in a general permit rather than in the statute. Under the general permit of 14.03.2018,
as summarised by Kol Zchut, a working day including overtime may not exceed **12 hours**, a week may
not carry more than **16 overtime hours**, and a night-shift worker may not work more than **58 hours**
a week including overtime. Those caps have been varied by temporary permits during wartime periods,
including the war with Iran, for some employers and for limited periods. Do not presume a relaxation:
ask the period and the employer's sector, and if they fall inside a temporary permit, say the caps may
have been relaxed rather than flagging a breach you cannot substantiate.

## 6. Worked example, five-day week, 42-hour basis

Tuesday 08:00 to 19:30, 45-minute break.

```
span              11.50 h
less break         0.75 h
working hours     10.75 h
daily bound        8.00 h
overtime           2.75 h  ->  2.00 h @ 125%
                             0.75 h @ 150%
```

The Tuesday premium is owed whether or not the week reaches the weekly bound, because the daily limb
stands on its own. Then, separately, sum the week's **ordinary** hours (the 8 from Tuesday plus each
other day's ordinary hours) and tier anything above the weekly bound.

## 7. Categories this file does not cover, and where they go

- **Youth under 18**, part-timers on fixed days, piece-rate workers, and shift supplements folded
  into the base: each has its own rule. Name the rule and say it needs checking rather than applying
  the general tiers to them.
- **Holidays** interact with the rest-day rules and with holiday pay, and the combined figure differs
  again for hourly workers compelled to work. Treat as adjacent and flag.
- **Global overtime** (`גמול גלובלי`) is recognised by the labour courts on cumulative conditions,
  including informed consent, a genuine supplement rather than a relabelling of existing pay, respect
  for the statutory caps, a payslip that separates the component, and periodic reconciliation so the
  global is not systematically below the real hours. Where actual overtime exceeds what the global covers, the excess is
  owed. Flag it; do not validate a global arrangement as compliant.
- **Sector regimes** (guarding, hotels and restaurants, manpower contractors, foreign care workers)
  have their own extension orders. Say so and stop.

## 8. The minimum-wage floor, and why it uses a different base

The annual update takes effect on **1 April**, but increases have also come on other dates (the
1.12.2017 row), and the figure has not risen every year: the monthly 5,300.00 did not change between
December 2017 and April 2023. Use the dated row in force for the period being
audited, never a remembered figure, and re-verify on the Bituach Leumi table after each 1 April:
https://www.btl.gov.il/Mediniyut/GeneralData/Pages/שכר%20מינימום.aspx

Adult (18 and over), as published by Bituach Leumi. Each row applies until the next one:

| From | Monthly | Daily, 5-day week | Daily, 6-day week | Hourly, 182 basis | Hourly, 186 basis |
|---|---|---|---|---|---|
| 01.04.2026 | 6,443.85 | 297.4 | 257.75 | 35.4 | 34.64 |
| 01.04.2025 | 6,247.67 | 288.35 | 249.90 | 34.32 | 33.58 |
| 01.04.2024 | 5,880.02 | 271.38 | 235.20 | 32.30 | 31.61 |
| 01.04.2023 | 5,571.75 | 257.16 | 222.87 | 30.61 | 29.95 |
| 01.04.2018 | 5,300.00 | 244.62 | 212.00 | 29.12 | 28.49 |
| 01.12.2017 | 5,300.00 | 244.62 | 212.00 | (none) | 28.49 |

That covers the seven-year limitation window. For a period before 1.12.2017, take the row from the
Bituach Leumi page; do not extrapolate. Rows before April 2018 carry an hourly figure on the
186 basis only, because the 42-hour week did not yet exist; take them from the same page. Employees
under 18 have separate, lower rates that this file does not carry and that the Bituach Leumi page
above does not list. Say so, and ask the user for the rate from an official source rather than
applying the adult row to a minor.

### Which hourly divisor, 182 or 186

The statute still defines the hourly minimum as `החלק ה־186 של שכר המינימום` (חוק שכר מינימום,
`סעיף 1`). Since the 2018 extension order shortened the week to 42 hours, the steering committee's
decision and the Ministry of Labour's position are that the hourly figure is the monthly figure divided
by **182**, and that employers should pay that. The ministry has also said it will not take criminal or
administrative steps against an employer that keeps paying on 186. So:

- For a **monthly-salaried** employee, compare the monthly figure and avoid the divisor entirely.
- For a full-time **hourly** employee on a 42-hour week, test against the 182 figure. A rate between the
  two figures is a disputed point, not a settled shortfall. Say so.
- For deriving the value of a regular hour from a monthly salary generally (Step 1 item 6), the same
  extension order puts it at monthly salary divided by **182** for a full-time post, which is why 182 is
  the default divisor. The order does not apply where the full-time post was already 42 hours a week or
  less, or to an employee outside the Hours of Work and Rest Law.

### The base is NOT the overtime base

`סעיף 18` of the Hours law puts **every** supplement into the base for overtime and rest-day premium.
The minimum-wage test runs the other way. `סעיף 3(א)` of חוק שכר מינימום counts only the wage paid
for an ordinary working day, and `סעיף 3(ב)` lists what counts (base or combined wage, cost-of-living
supplement, a fixed supplement paid because of the work) and then excludes, in its own words:

> ואולם לא יובאו בחשבון תוספת משפחה, תוספת ותק, תוספת בשל עבודה במשמרות, פרמיה מדודה, מוסכמת,
> קבועה או קבוצתית, משכורת י״ג, מענקים על בסיס שנתי, והחזר הוצאות לרבות הוצאות כלכלה, אש״ל ונסיעות
> שמשלם המעסיק.

Overtime and rest-day premium are not wage for an ordinary working day either. So a base below the
minimum, topped up by a shift supplement, seniority pay, travel or premium pay, still fails the test.
Reusing the inflated `סעיף 18` rate for the minimum-wage check is the commonest way that failure is
missed. Two lines that DO count: a `השלמה לשכר מינימום` (minimum-wage completion) line, which exists
precisely to lift the ordinary-day wage to the floor, and a fixed supplement paid because of the work.
Where the pay is not built from a base or combined wage at all, `סעיף 3(ד)` uses the regular wage
without supplements.

### Proration

- **Part-time:** `סעיף 2(ב)`, a part-time employee is entitled to a minimum prorated to the position
  scope.
- **Absence:** `סעיף 2(ג)`, where the employee was absent the minimum is reduced in proportion to the
  absence, but where the employee is entitled to payment for the absence under law or an agreement,
  that arrangement governs. In a month with reserve duty, sick days or leave, compare the ordinary-day
  wage for the days actually worked against the prorated minimum; do not compare full gross, which may
  include the reserve-duty payment, against the full monthly figure. Sick pay in particular follows its
  own statute and is lawfully lower than full pay on the first days, so a reduced sick line is not a
  minimum-wage shortfall.
- **Partial month:** a month in which employment started or ended part-way is compared pro rata to the
  working days of employment in that month, not against the full monthly figure. That is the same
  proportional logic as `סעיף 2(ג)` rather than a separately quoted provision.
- **Rounding:** allow a few agorot; the published daily and hourly figures are themselves rounded.

### What follows from a shortfall

If the ordinary-day wage was below the minimum, the ordinary-day wage owed is the minimum, and the
supplements the employer pays are still owed **on top** of it, because they could not be counted
toward the floor. So rebuild the `סעיף 18` premium base as the lifted ordinary-day wage PLUS the
wage supplements that `סעיף 3(ב)` excluded from the test and that are paid for the work itself (shift,
seniority and family supplements, and a premium paid per hour or day), and price the premiums on that.
Whether a particular premium or a family supplement forms part of the regular wage is fact-specific;
treat a disputed one as a question, not a settled add-back.
Two kinds of item stay out of the add-back. A supplement that counted toward the floor (a fixed
supplement paid because of the work, a cost-of-living supplement, a `השלמה לשכר מינימום` line) is
already inside the lifted figure. And the rest of the `סעיף 3(ב)` list, expense refunds including
meals, אש״ל and travel, the 13th salary and annual grants, is not an hourly wage supplement at all.
Adding either back overstates the base. Never take the larger of the minimum and the payslip's
existing `סעיף 18` rate: that keeps the supplement doing double duty.

Example, 2026, full-time hourly worker: base 30.00 an hour plus a shift supplement of 6.00 an hour.
The payslip's `סעיף 18` rate is 36.00, which is above 35.4, but the minimum-wage test ignores the shift
supplement and the base of 30.00 fails it. The ordinary-day wage owed is 35.4, the premium base is
35.4 + 6.00 = 41.4, and the first two overtime hours of a day are owed at 1.25 x 41.4 = 51.75, not
1.25 x 36.00 = 45.00. Use the 182 figure for this and say the 186 figure is the disputed floor.

This is reasoning from the two statutes together rather than a quoted provision; present it as such.
