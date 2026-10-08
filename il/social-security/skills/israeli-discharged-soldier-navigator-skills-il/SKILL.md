---
name: israeli-discharged-soldier-navigator-skills-il
title: Israeli Discharged Soldier Navigator
description: Navigate post-discharge benefits for IDF, MAGAV, Police, SHABAS, and SLE members via the MoD Department for Discharged Soldiers (hachvana.mod.gov.il). Computes Pikadon by service tier (lochem, tomech lechima, acher), explains the 14-day deposit vs 60-day manak shichrur timelines, validates withdrawals against the 6 statutory pre-5y purposes (academic studies, vocational training, driving lessons, business, marriage, apartment purchase, rental NOT included), walks Section 39a nekudot zikui via Tofes 101 and Tofes 135 retroactive refund, and covers Iron Swords benefits for combat veterans discharged October 2023+. Use when a hayal meshuchrar, parent, or SLE completer asks about pikadon, manak shichrur, post-army benefits, nekudot zikui chayal meshuchrar, or free university for combat veterans. Do NOT use for miluim (israeli-miluim-manager), lone soldiers (israeli-lone-soldier-rights), scholarships beyond Mimadim (israeli-academic-scholarships), or mortgages (israeli-mortgage-comparator).
author: skills-il
author_url: https://github.com/skills-il/government-services/tree/master/israeli-discharged-soldier-navigator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: social-security
language: he
sources:
- title: Adjacent Benefits
  path: references/adjacent-benefits.md
- title: Domain Checklist
  path: references/domain-checklist.md
- title: Mimadim Scholarship
  path: references/mimadim-scholarship.md
- title: Nekudot Zikui Tables
  path: references/nekudot-zikui-tables.md
- title: Six Purposes Deep Dive
  path: references/six-purposes-deep-dive.md
---

# Israeli Discharged Soldier Navigator

## Legal notice

This is a free information tool operated by an AI model. It explains the rules and calculates from the figures you enter, but it does not examine your full circumstances and does not constitute advice. All of its outputs are produced automatically, with no involvement, review, or approval by an authorised representative of any of the bodies named below, and an AI model may err, omit data, or present a wrong conclusion. Eligibility, the amount, and the service classification are determined solely by the paying authority: the MoD Department and Fund for Discharged Soldiers for the Pikadon, the grant and Mimadim; the Tax Authority for credit points; the National Insurance Institute for the required-work grant and unemployment benefit. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person, and all use of its output is the user's sole responsibility.


## Problem

A 21-year-old who just finished sherut chova has a Pikadon, a separate discharge grant, three years of tax credit points, a right to return to their pre-draft employer, and, for combat veterans, full university tuition. The information is scattered across hachvana, Kol Zchut, the Income Tax Ordinance and the Mimadim page, and almost every entitlement has its own deadline running from the discharge date. Most discharged soldiers miss benefits outright (retroactive nekudot zikui above all), try to spend the Pikadon on non-permitted purposes (rental is the classic), or let a window close. This skill walks eligibility, the per-tier rates, the 6 permitted purposes, the Tofes 101 flow, the Mimadim terms and the deadlines, with the right form numbers and portal paths.

## Instructions

### Step 1: Establish Eligibility

The Pikadon and discharge grant are governed by **Chok Klitat Chayalim Meshuchrarim, 5754-1994** (חוק קליטת חיילים משוחררים). The eligibility table:

| Service type | Minimum service | Pikadon? | Grant? |
|---|---|---|---|
| IDF mandatory (sherut chova) | 12 months | Yes | Yes |
| MAGAV (Border Police) | 12 months | Yes | Yes |
| Israel Police | 12 months | Yes | Yes |
| SHABAS (Prison Service) | 12 months | Yes | Yes |
| Sherut Leumi-Ezrachi (SLE) | 12 months | Yes (acher tier) | Yes |
| Any of the above, < 12 months, health discharge or injury in training / operational activity | Minimum waived, but the accrual rule is not: Pikadon is **pro-rata** (months served x tier rate) | Pro-rata | Pro-rata |
| Any of the above, < 12 months, voluntary exit | None | None |

> Source quote (kolzchut): "מי שהשתחררו משירות חובה בצה\"ל, במג\"ב, במשטרת ישראל, בשב\"ס, או סיימו שירות לאומי-אזרחי ששירתו לפחות 12 חודשים"

### Step 2: Compute the Pikadon Amount (2026 indexed rates)

The Pikadon accrues per month of paid service at a rate set by service type. Current rates from hachvana:

| Service type | English | NIS/month (May 2026) |
|---|---|---|
| לוחמים | Combat | 990.63 |
| תומכי לחימה | Combat support | 825.52 |
| עורפי | Rear / other | 660.42 |
| שירות לאומי-אזרחי | National-civic service (SLE) | 660.42 |
| מסלול אזרחי ביניים | Intermediate civilian track | 495.38 |
| מסלול אזרחי מפוצל | Split civilian track | 330.25 |

**Training months are reclassified DOWN, and this is the single most common over-estimate.** The MoD states it explicitly: a combat soldier's first **4** training months are credited as combat support, and a combat-support soldier's first **2** are credited as other. So 32 combat months accrue 4 x 825.52 + 28 x 990.63, not 32 x 990.63. Only the first four downgrade: training beyond four months counts as combat.

**Caps and indexing:** hachvana publishes the operative caps as **32 months of paid service for a man and 24 for a woman** ("עד 32 חודשים לחייל ו-24 חודשים לחיילת"), and service beyond the cap adds nothing. **Flag the female figure rather than asserting it flatly:** s.11(a) as amended by Amendment 16 of 2014 reads "32 חודשים לחייל ו-28 חודשים לחיילת", and the commencement of the female figure is tied to regulations under s.16א(ד). Use 24, since that is what the paying authority publishes, but tell a woman who served more than 24 months to confirm her own cap with the Department before planning around it. The balance is re-indexed to the CPI at the start of each month, and it is personal, non-transferable, non-pledgeable, and non-seizable.

> Source quote (Chok Klitat Chayalim Meshuchrarim, Chapter ג): "הפקדון הוא אישי ואינו ניתן להעברה, לשעבוד או לעיקול בכל דרך שהיא"

**Always send the user to the official calculator for the personal total** at https://www.hachvana.mod.gov.il/GrantAndDeposit/DepositUpTo5/Pages/default.aspx. Give an order-of-magnitude estimate only when they supply service type and months served (capped at 32/24). These are the MoD's May 2026 figures and are re-indexed monthly; re-read hachvana before quoting them for a later period.

### Step 3: The Discharge Grant (Manak Shichrur)

The discharge grant is **separate** from the Pikadon. Key facts:

| Question | Answer |
|---|---|
| When, and to where | 20 to 60 days from end of service, to the account that received salary during service |
| Restrictions | None, "לכל מטרה בה תבחרו". Exempt from tax, same statute as the Pikadon |
| Per-month amounts (May 2026) | Combat 684.99, combat support 570.42, **other including SLE** 455.84, intermediate civilian 342.50, split civilian 227.92. Note this is **five** tiers, not six: the grant merges orfi and SLE into one row. The training reclassification applies here too |
| Eligibility | 12 months, or less on health grounds. Lone soldiers get an advance within 14 days |

> Source quote (hachvana GrantAndDeposit): "מענק שחרור, אשר יועבר לחשבונכם תוך 60 יום ממועד השחרור ובו תוכלו להשתמש לכל מטרה בה תבחרו"

### Step 4: Pikadon Availability and Withdrawal Window

| Event | Window |
|---|---|
| Pikadon visible | Day 14 after IDF / MAGAV / Police / SHABAS, day **30** after SLE |
| Discharge grant landed | Day 20-60 after end of service, automatic |
| Pre-5y window | Years 0-5, restricted to the 6 purposes in Step 5 |
| Post-5y auto-transfer | To the account on file within 60 days of the 5-year mark, SMS then ~7 business days. Applies to service ending after 01.01.2014; earlier is the Pikadon 2000 path |
| Bank account not located | The Fund makes contact, then **120 days** to redeem (s.19(b)(1)) |
| Forfeiture | At **5.5 years** the balance goes to the Additional Assistance Fund (s.19(c)), reclaimable for a further **4.5 years** (s.19(c1)), so the outer deadline is 10 years. A residue of 50 NIS or less goes to the Treasury (s.19(d)) |
| Early release at 3 years | A lochem who served 3 more keva years as lochem or tomech lechima and committed to another may draw the balance at 3 years (s.19(b)(2)), on request within 2.5 years |

**Ask when sherut CHOVA ended, never when they left the army.** Every clock above runs from it: "משרתי קבע נחשבים חיילים משוחררים במשך 5 שנים מתום שירות החובה שלהם". Someone who signed three years of keva is at year six from chova, so the window has closed and the balance has transferred, or is in the forfeiture path if the account was stale.

Nothing in the account on day 1 is normal: the Pikadon needs 14 days (30 for SLE), the grant up to 60.

### Step 5: The Six Permitted Pre-5-Year Withdrawal Purposes

**The restricted-purpose Pikadon window is 5 years for EVERYONE** (s.19(a)). The well-known "10 years for active reservists and lone soldiers" rule is s.19(a1)(1), and it attaches to the **s.7(a) and s.7A benefits** (the Additional Assistance Fund for a mechina, a vocational institution and a living allowance; and the Higher-Education Encouragement Fund for study in priority areas), **not to the Pikadon**. It was added by Amendment 19 of 12.07.2017 and re-enacted by Amendment 24 of 2022, so it is not an Iron Swords measure. Never tell a reservist or lone soldier their Pikadon purposes stay open for 10 years.

> Source quote (Chok Klitat Chayalim Meshuchrarim, Section 19(a1)): "חייל מילואים פעיל וחייל משוחרר בודד יהיו רשאים לממש את הזכאויות לפי סעיפים 7(א) ו-7א בתקופת עשר השנים הראשונות שלאחר סיום השירות הסדיר"

Before it closes, the Pikadon may be withdrawn for these and ONLY these (hachvana's wording):

> "לימודים אקדמיים, הכשרה מקצועית, נישואין, הקמת עסק, לימודי נהיגה ורכישת דירה, בית או קרקע לבניית בית"

Four sit in the statute (s.12 bagrut/mechina/psychometric, s.13 academic, s.14 vocational, s.18 business); marriage and driving lessons were added to the Schedule by order under s.18א, which lets the Minister add more. Treat it as the current Schedule, not a permanently closed list. Numbered as quoted:

| # | Purpose (Hebrew) | English |
|---|---|---|
| 1 | לימודים אקדמיים | Academic studies. **s.12 makes this wider than a degree**: bagrut completion, a pre-academic mechina, and psychometric preparation are each funded in their own right, so a user with no bagrut is told yes, not routed away |
| 2 | הכשרה מקצועית | Professional / vocational training |
| 3 | נישואין | Marriage |
| 4 | הקמת עסק | Starting or investing in a business |
| 5 | לימודי נהיגה | Driving lessons |
| 6 | רכישת דירה / בית / קרקע לבניית בית | Purchase of an apartment, house, or land to build on |

**The Fund pays the provider, not the soldier.** For studies, training and a mechina it "תשלם את סכומי ההשתתפות בשכר הלימוד במישרין למוסדות" (s.15(a)); for an apartment it "תעביר את סכום ההשתתפות ישירות למוכר דירת המגורים" (s.17(b)). An approved request settles a bill, it does not put cash in the user's account. Never describe purposes 1, 2 or 6 as money they will receive.

`references/six-purposes-deep-dive.md` has the evidence each purpose needs and the five refusals users argue with: rent (only purchase qualifies), the post-army trip, a degree abroad (Israel only, "כספי הפיקדון ניתנים למימוש רק במדינת ישראל", however recognised the institution), a parent withdrawing for them, and loan collateral.

### Step 6: Tax Credit Points (Nekudot Zikui) for Discharged Soldiers

The most-missed benefit. Awarded under **Pkudat Mas Hachnasa Section 39a** (not Section 11).

State these as thresholds, never as ranges: the source table is inconsistent about which band the boundary month falls in.

| Threshold reached | Points per year | Annual value (2026) | Total over 36 months |
|---|---|---|---|
| Male IDF/MAGAV/Police/SHABAS **≥ 23 months**; female **≥ 22**; SLE **≥ 24** | 2 | 5,808 NIS | **17,424 NIS** |
| Otherwise, **≥ 12 months** in any of those populations | 1 | 2,904 NIS | **8,712 NIS** |
| < 12 months | None, EXCEPT an early medical discharge, deemed to have completed 12 months | 1 | 8,712 NIS |

It is prorated across calendar years (so years 1 and 4 are partial) and stacks on the 2.25 base resident points.

**Three populations the month-count alone gets wrong, all set out in `references/nekudot-zikui-tables.md`, which you must read before answering any of them:** a **keva** soldier (the 36 months run from the end of CHOVA and the points are claimable while still serving, so a keva leaver typically has 13 months left, not 36); a **hesder / SHLAT** soldier (unpaid service does not accrue Pikadon but DOES count toward the credit-point threshold, measured over total service from enlistment); and an **early medical discharge** under 12 months (deemed to have completed 12).

**Mechanics:**

| Rule | Detail |
|---|---|
| Duration and value | 36 months from the month **after** discharge. 242 NIS per point per month in 2026, so 2 points is 484 NIS/month off income tax owed |
| Salaried claim | **Tofes 101** to the employer at the start of each calendar year with the Teudat Shichrur attached. It appears on the payslip under "נקודות זיכוי" |
| Self-employed claim | Fill the relevant fields with the discharge certificate when filing the ordinary annual return. Kol Zchut describes only this route; do not tell a self-employed user to file Tofes 135 |
| Retroactive (salaried) | **Tofes 135** via the Tax Authority online portal, up to 6 years back from the end of each tax year, one request per year. Refunds actual over-withholding plus indexation and 4% interest |
| Started work mid-year, or two employers | File **Tofes 116** ("בקשה להקלה ולתיאום בחישוב ניכויי המס"), or the credit is swallowed by over-withholding. The gov.il landing pages for it now 404, so cite the form, not a URL |

> Source quote (kolzchut): "חיילים 23 חודשים ומעלה 2 ... 36 חודשים לאחר השחרור, החל מהחודש שלאחר חודש השחרור"

A user who discharged 2 to 6 years ago, has been working, and never claimed goes straight to Tofes 135.

### Step 7: Tax Exemption of Pikadon and Grant

Pikadon withdrawals and the discharge grant are both exempt from income tax under **Pkudat Mas Hachnasa Section 9(27)** (not 9(7), which is severance).

> Source quote (kolzchut): "מכספי הפיקדון האישי לא מנוכה מס הכנסה (פקודת מס הכנסה, סעיף 9(27))"

So a user withdrawing the whole balance for studies receives all of it. Reassure anyone worried that a lump sum that size will attract mas hachnasa: it does not.

### Step 8: Mimadim LiLimudim, 100% Tuition

**Mimadim LiLimudim** funds **100% of the CHE university tuition**. **`references/mimadim-scholarship.md` carries the full terms; read it before answering on eligibility or amounts.** The essentials:

| Aspect | Detail |
|---|---|
| Who qualifies | Two tracks. (1) Combat soldiers with a **"shichrur bekavod-zahav"** certificate. (2) "Special populations" with a **"shichrur bekavod"** certificate: tashmash horim, parents who received family payments, lone soldiers, minorities, Arab / Druze / Circassian dischargees, olim. Combat support is not a track on its own but is not excluded either, so verify the cohort. |
| Coverage | 100% of CHE tuition, capped at that ceiling (**12,017 NIS, תשפ"ו**). Annual refund of up to 85% (10,214.45 at the ceiling), the accrued 15% (1,802.5) released in the final year. 3 study years, 4 for engineering, medicine (doctor) or architecture. Tuition only. |
| Window | 5 years from discharge, +1 for bagrut / mechina / psychometric, +2 for a year or more of continuous keva, +3 for both. Statute and website measure it differently, see the reference file. |
| Charvot Barzel | Someone eligible for both cannot realise them in the same academic year, and the ORDER changes the total. |
| Application | Education section of the personal area; confirm the bank details first. The תשפ"ו cycle closes **31.10.26**, read off the Mimadim page and NOT the Iron Swords page, which still shows an expired 2025 date. |

**Not in scope:** third-party scholarships (PEREACH, Adams, Rashi, Rothschild) route to `israeli-academic-scholarships`.

### Step 8.5: Other High-Value Benefits, Mention-and-Route

These are delivered by bodies other than the Department, so they sit outside this skill's core. Surface them, then route. **The full routing table, and the conditions that decide each one, are in `references/adjacent-benefits.md`. Read it before answering on any of them, because several disqualify the typical 21-year-old outright.** The headline facts and the trap on each:

- **מענק עבודה נדרשת**, 11,461 NIS (2026) for 6 full months in a defined sector within 24 months of discharge, on Tofes 1521 to Bituach Leumi. Largest non-Pikadon cash benefit, and taxable. Claim within **42 months**. → `israeli-bituach-leumi`
- **Dmei avtala**, max 70 days where the unemployment period starts in year 1. → `israeli-unemployment-benefits-navigator`
- **Arnona exemption**, up to 4 months. Not automatic, and not available while living in a parent's home, though the parents may qualify instead.
- **2-month BL and health-contribution exemption**, automatic, but only while not working and with non-work income at or below 688 NIS/month (2026).
- **Free public transport for a year**, forfeited unless the "discharged" Rav-Kav profile is loaded **within 60 days** of discharge.
- **תוספת משכנתא**, +1% of entitlement per service month, joint cap 46% single / 65% couple. → `israeli-mortgage-comparator`
- **פיקדון 2000**, dormant balances where service ended after 01.01.1995 or began before 31.12.2000.
- **Free Ministry of Justice legal aid** on discharged-soldier rights.
- **"Bahatzda" benefits card**, via hachvana.mod.gov.il.
- **Service-type appeal**, to the IDF public-enquiries officer on **1111 ext 5**. The Department cannot reclassify service; only the IDF can.
- **Pikadon inheritance**, for a death during service OR after discharge. Only a death in service goes to Mador Mishpachot Shakulot.


### Step 8.6: Right to Return to the Pre-Draft Employer (45-day window)

**Chok Chayalim Meshuchrarim (Hachzara LaAvoda), 5709-1949** gives a discharged soldier the right to go back to their pre-conscription employer. It carries the shortest deadline in the domain and is routinely missed, because it runs from the discharge date and not from when the user starts job-hunting.

It applies to a "permanent employee" there, or someone who worked **6 continuous months** before conscription, and who did **not** take severance on leaving. Service counts as accrued seniority, and the employer must re-employ them for **6 months** on the same job and terms, or the best available if that is impossible, with the burden of proving impossibility on the **employer**.

**The deadline is a written request between 15 days before discharge and 30 days after.** Miss that 45-day window and the right lapses. Name a start date within 30 days of the request and copy the employment bureau and the workers' committee. A workers' organisation may file it on the soldier's behalf.

A refusal on the named date is not the end: where the employer cannot take them that day they may be taken on "בתוך שנה מהיום שהגיש את הבקשה, במועד האפשרי המוקדם ביותר". Disputes go to a **ועדת תעסוקה**, the statutory forum; Ministry of Justice legal aid helps the user get there but is not the tribunal. Someone who resigned on conscription after 12 months there gets severance instead, and taking it ends this right.

### Step 9: The hachvana.mod.gov.il Personal Area

Everything above runs through the personal area (האזור האישי) at hachvana.mod.gov.il: balance, withdrawal requests and their evidence uploads, the bank account on file, counsellor scheduling, Mimadim, and the Teudat Shichrur. Do not assert a login method, the site does not publish one consistently. There is no manual fallback for withdrawals, so a user who cannot log in must call the Department.

### Step 10: Required Documents Checklist

Before any application: the **Teudat Shichrur** (from the personal area or the IDF), the **Teudat Zehut**, an **Israeli bank account in the user's own name** (the Pikadon will not pay a foreign or a parent's account), the purpose-specific evidence from Step 5 for a pre-5y withdrawal, and Tofes 101 plus the Teudat Shichrur for the employer.

## Examples

### Example 1: Just discharged combat, wants Pikadon for driving lessons

"I just finished as a lochem (32 months). Can I use my Pikadon for a driving course?"

1. Eligible: 32 months IDF lochem, at the male cap.
2. Estimate: 4 x 825.52 (training months, at the combat-support rate) plus 28 x 990.63. Send him to the official calculator for the live total.
3. Driving lessons are purpose #5, so yes. Evidence: driving-school receipts.
4. Pikadon visible day 14.
5. Apply in the personal area under Pikadon.

### Example 2: 3 years after discharge, wants Pikadon for a rental deposit

"I discharged 3 years ago and still have money in my Pikadon. Can I use it for the deposit on my first rental?"

1. No. Rental is not one of the six purposes; only purchase qualifies.
2. Options: wait for the year-5 auto-transfer, which is unrestricted; or, if enrolled in studies, use purpose #1 for tuition (paid to the institution) and free up other cash; or, if actually buying, purpose #6 with a signed agreement.
3. Two years to the auto-transfer. Tell him to check the bank account on file NOW: a stale one at year 5 starts the 120-day clock and then the 5.5-year forfeiture.

### Example 3: Sherut Leumi-Ezrachi completer, 18 months

"My daughter finished Sherut Leumi-Ezrachi 18 months ago. What is she entitled to?"

1. Eligible: over the 12-month minimum. Pikadon at the SLE rate of 660.42 x 18; official calculator for the live total.
2. Availability for SLE is **day 30**, not day 14. The grant should already have landed within 60 days; if not, the bank account on file is the usual cause.
3. Credit points: 18 months is under the SLE 24-month threshold, so 1 point/year for 36 months from the month after completion, if she has taxable income. Tofes 101 to her employer, Tofes 135 for any missed year.
4. Her restricted window closes about 3.5 years from now. Check the bank account on file today.

### Example 4: Combat veteran discharged 2024, asks about free university

"I'm a lochem who discharged March 2024. I heard the Knesset passed free university?"

1. Mimadim funds 100% of the CHE tuition if his certificate is "shichrur bekavod-zahav". Capped at 12,017 NIS (תשפ"ו), refunded at 85% annually with the 15% released in the final year.
2. Window: 5 years from discharge, so to roughly March 2029, with the extensions in `references/mimadim-scholarship.md`. The current cycle closes 31.10.26.
3. If he also qualifies for the Charvot Barzel scholarship, he cannot realise both in one academic year, and the order changes the total. Have him check first.
4. Do NOT tell him to draw the Pikadon for "what Mimadim doesn't cover": the study purpose is paid to the institution as a tuition contribution, and Mimadim already meets the tuition. It can fund a mechina, bagrut completion, or psychometric prep under s.12 instead.
5. A tomech-lechima asking the same question is not automatically excluded; send him to verify his cohort.

### Example 5: Discharged 4 years ago, never claimed credit points

"I've been working 4 years since discharge and my payslip never showed nekudot zikui. Did I lose them?"

1. Retroactive refunds run 6 years back from the end of each tax year, via **Tofes 135**, one request per year, with the Teudat Shichrur, that year's salary summary, and bank details.
2. Verify service length against the thresholds, and ask whether any of it was keva or SHLAT, which changes both the count and the clock.
3. Ceiling on the benefit: 17,424 NIS (2 points) or 8,712 NIS (1 point), realised only against tax actually owed.
4. Also file Tofes 101 with the current employer if any of the 36-month window is left.

## Recommended MCP Servers

No public MCP server exists for hachvana.mod.gov.il; the personal area has no public API, so withdrawals go through the user's authenticated browser session.

## Reference Links

| Source | URL | What to check |
|---|---|---|
| Department homepage | https://www.hachvana.mod.gov.il/Pages/default.aspx | Contact channels |
| Grant hub | https://www.hachvana.mod.gov.il/GrantAndDeposit/Pages/default.aspx | 6 purposes, 60-day grant timeline |
| Grant amounts | https://www.hachvana.mod.gov.il/GrantAndDeposit/Pages/Grant.aspx | Per-tier grant NIS rates |
| Pikadon pre-5y (with calculator) | https://www.hachvana.mod.gov.il/GrantAndDeposit/DepositUpTo5/Pages/default.aspx | Per-tier monthly rates (re-indexed monthly), 14-day rule |
| Chok Klitat Chayalim Meshuchrarim | https://www.nevo.co.il/law_html/law01/150_023.htm | Sections 7, 7A, 7A1, 19: windows, forfeiture, early release |
| Kol Zchut: Pikadon | https://www.kolzchut.org.il/he/פיקדון_אישי_לחיילים_משוחררים_ומסיימי_שירות_לאומי-אזרחי | 6 purposes, Israel-only rule, SLE day 30, appeal via 1111 ext 5 |
| Kol Zchut: Nekudot Zikui | https://www.kolzchut.org.il/he/נקודות_זיכוי_ממס_הכנסה_לחיילים_משוחררים_ומסיימי_שירות_לאומי-אזרחי | Section 39a thresholds, 2026 point value, Tofes 101 / 135 |
| Kol Zchut: return to work | https://www.kolzchut.org.il/he/חזרה_לעבודה_של_חייל_משוחרר | The 45-day request window, 6-month employer duty |
| Kol Zchut: rights index | https://www.kolzchut.org.il/he/זכויות_חיילים_משוחררים_ומסיימי_שירות_לאומי-אזרחי | The full entitlement taxonomy, to spot anything new |
| Mimadim LiLimudim | https://www.hachvana.mod.gov.il/MainEducation/HachvanaScholarship/Pages/UniformToStudies.aspx | Tuition ceiling, 85/15 split, window extensions, cycle deadline |
| Kol Zchut: tax refund + Form 135 | https://www.kolzchut.org.il/he/החזר_מס_הכנסה | 6-year window from end of tax year, indexation + 4% interest |

## Gotchas

- **The 10-year window is NOT the Pikadon window.** Section 19(a1) gives active reservists and lone soldiers ten years for the Section 7(a) and 7A study-fund benefits. The Pikadon's restricted-purpose window is five years for everyone, and the balance leaves the Fund at 5.5 years.
- **Ask when CHOVA ended, not when they left the army.** Every Pikadon clock runs from the end of compulsory service, so a keva leaver is usually already past the window.
- **An approved request is not cash.** For studies, training and an apartment the Fund pays the institution or the seller directly (ss.15(a), 17(b)). It settles a bill; it does not fund the user's plans around it.
- **A stale bank account can forfeit the Pikadon, not just delay it.** At year 5 the balance transfers to the account on file. If the Fund cannot locate it there are 120 days from its contact; at 5.5 years it goes to the Additional Assistance Fund with 4.5 years to reclaim.
- **Two citations agents get wrong.** Credit points are **Section 39a**, not Section 11. The Pikadon and grant exemption is **Section 9(27)**, not 9(7).
- **Rental is not a permitted purpose**, and the six purposes are the current Schedule, not a permanently closed list: s.18א lets the Minister add to it, which is how marriage and driving lessons got there.
- **Pikadon rates index monthly with CPI**, so any figure here (990.63 combat, May 2026) is an order-of-magnitude anchor. Send the user to the official calculator.
- **The caps are on PAID service, and the female figure is contested.** hachvana publishes 32 for a man and 24 for a woman; s.11(a) reads 28 for a woman with a conditional commencement. A woman past 24 months should confirm with the Department.
- **"Unpaid service does not accrue" is a Pikadon rule and does NOT carry across to credit points.** A hesder or SHLAT soldier is thresholded on total service from enlistment, so paid months alone can halve their entitlement.
- **Training months are reclassified DOWN, and only the first four.** A combat soldier's first 4 accrue at the combat-support rate (2 for a combat-support soldier, at "other"). Training beyond four counts as combat. Applies to the grant as well.
- **A wounded lochem or tomech lechima keeps the higher rate** for the WHOLE service period after transferring to another role.
- **Credit points start the month AFTER discharge**, stack on the 2.25 base resident points, and are claimable during keva service.
- **Forward credit cannot exceed monthly tax liability; the retroactive path can pay cash.** Tofes 101 reduces tax owed to zero and no further, so "I lost X shekels" is wrong for the forward case. Tofes 135 refunds real over-withholding plus indexation and 4% interest, 6 years back from the END of each tax year, one request per year.
- **The return-to-work request has a 45-day window**, from 15 days before discharge to 30 days after. Shortest deadline in the domain, and it lapses silently.
- **Mimadim is not lochem-only, and its deadlines are not on the Iron Swords page.** The special-populations track runs off a "shichrur bekavod" certificate. The Iron Swords page still shows an expired 2025 date; the live תשפ"ו cycle closes 31.10.26.
- **Pikadon is non-transferable, non-pledgeable, non-seizable.**

## Bundled Resources

### Scripts

- `scripts/pikadon-calculator.py`, estimates the Pikadon and grant from service type and months served at the May 2026 rates, with the training reclassification applied. `--medical-discharge` and `--hesder-total-months` move the credit-point threshold only; neither changes the Pikadon. Run: `python scripts/pikadon-calculator.py --service-type lochem --months 32 --gender male`

### References

- `references/adjacent-benefits.md`, the conditions behind every Step 8.5 row (required-work grant, avtala, arnona, BL exemption, Rav-Kav, mortgage supplement, Pikadon 2000, legal aid).
- `references/mimadim-scholarship.md`, full Mimadim terms: eligibility tracks, the 85/15 mechanics and ceiling, window extensions, the Charvot Barzel interaction.
- `references/six-purposes-deep-dive.md`, evidence required per permitted withdrawal purpose.
- `references/nekudot-zikui-tables.md`, credit-point thresholds and the Tofes 101 / 135 flow.
- `references/domain-checklist.md`, coverage list used by future update runs.

## Troubleshooting

### Error: "Pikadon not visible in the personal area 20 days after discharge"
Cause: likeliest is that the discharge date has not synced from IDF systems, or the login is the wrong identity. Not confirmed against a published Department notice, so hedge it. An SLE completer is not late until day 30, and a keva leaver may be years past the window rather than days early.
Solution: confirm they logged in with their own Teudat Zehut, and confirm when CHOVA ended. Then contact the Department; there is no manual workaround.

### Error: "Withdrawal request for apartment rental rejected"
Cause: rental is not one of the 6 permitted purposes, so the rejection is automatic and correct.
Solution: wait for the year-5 auto-transfer, which is unrestricted, or re-submit under purpose #6 only if they are genuinely purchasing (signed agreement, not a lease).

### Error: "Nekudot zikui not on the payslip even though Tofes 101 was submitted"
Cause: usually a one-month payroll lag or a missing Teudat Shichrur attachment.
Solution: check the next payslip; if still missing after two cycles, have payroll re-process Tofes 101 with the certificate and file Tofes 135 for the months already lost. The 36-month window does not pause.

### Error: "Discharge grant did not arrive after 60 days"
Cause: almost always the bank account on file, closed, frozen, or in the wrong name after the user left their service-era account.
Solution: update the bank account in the personal area. The same stale account is what triggers the Pikadon forfeiture clock at year 5, so fix it once and it fixes both.

### Error: "Mimadim scholarship rejected"
Cause: usually the certificate type. The gold-honour track is combat-only, and the special-populations basket attaches to a "shichrur bekavod" certificate.
Solution: check the cohort terms for that academic year. If the rejection turns on service classification, that is an IDF question, not a Department one: appeal on 1111 extension 5. If outside the basket entirely, route to `israeli-academic-scholarships` for alternative scholarships (PEREACH, Rashi, etc.).
