---
name: israeli-aliyah-navigator-skills-il
title: Israeli Aliyah Navigator
description: Comprehensive guide for new immigrants (olim) to Israel covering the full aliyah journey from pre-arrival to settlement. Use when user asks about "aliyah to Israel", "sal klita", "absorption basket", "misrad haklita", "klitat aliyah", "teudat oleh", "ulpan enrollment", "oleh chadash rights", "tax benefits for olim", or "driver's license conversion in Israel". Covers Misrad HaKlita processes, sal klita tracking, Ulpan, housing, banking, Bituach Leumi, tax exemptions, license conversion, and professional recognition. Do NOT use for general Israeli bureaucracy unrelated to immigration (use israeli-gov-services instead) or tourist visa questions.
author: skills-il
author_url: https://github.com/skills-il/government-services/tree/master/israeli-aliyah-navigator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: immigration
language: he
sources:
- title: Aliyah Additional Procedures
  path: references/aliyah-additional-procedures.md
- title: Aliyah Timeline Guide
  path: references/aliyah-timeline-guide.md
- title: Alternate Aliyah Statuses
  path: references/alternate-aliyah-statuses.md
- title: Driver License Conversion
  path: references/driver-license-conversion.md
- title: Post Basket Entitlements
  path: references/post-basket-entitlements.md
- title: Pre Aliyah Documents
  path: references/pre-aliyah-documents.md
- title: Professional Recognition
  path: references/professional-recognition.md
- title: Sal Klita Rates
  path: references/sal-klita-rates.md
- title: Tax Benefits Olim
  path: references/tax-benefits-olim.md
- title: Troubleshooting
  path: references/troubleshooting.md
---

# Israeli Aliyah Navigator

## Legal notice

This is a free information tool operated by an AI model. It helps you organise and complete forms for government authorities. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate, tax adviser, or accountant. The output is not legal, tax, or other professional advice. An AI model may err, omit data, or present a wrong conclusion.

A form submitted to an authority is a document whose contents are your responsibility, and incorrect details in it can carry liability. Check every field before filing, and do not file a form whose contents you do not understand. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person, and all use of its output is the user's sole responsibility.


## Instructions

### Step 1: Assess the Oleh's Situation

Before advising, establish: **stage**, **family status** (drives the sal klita track), **country of origin** (drives document authentication and recognition), **profession**, **Hebrew level**, and **prior time spent in Israel** (the sal klita 24-month presence test in Step 4 turns on it). Then generate a checklist:

```bash
python scripts/aliyah-checklist.py --stage <stage> --family <status> --country <country> --profession <profession>
```

### Step 2: Pre-Arrival Checklist

Guide the user through pre-arrival requirements:

**Jewish Agency and Consulate Process:**
1. Open a file with the Jewish Agency (Sochnut)
2. Book the consulate appointment
3. Choose the visa path: **Oleh visa** (immediate aliyah, full benefits) or **A1 temporary residence** (1-year renewable trial, no aliyah benefits, no military obligation, convertible later via Shinui Ma'amad, Step 2b). Comparison table: `references/aliyah-additional-procedures.md`.
4. Receive the **Ishur Chok HaShvut** (Confirmation of Eligibility), issued once the file passes review. Bring the original to the consulate and present it on arrival.
5. Gather required documents. The full list, with the authentication rules that trip people up, is in `references/pre-aliyah-documents.md`. The four that most often derail a file:
   - **Police clearance** from the country of birth, from every country lived in continuously over 1 year after age 14, and from every country of current citizenship. Shinui Ma'amad applicants (from Nov 2024) need one from every country they lived in for more than one year, with no age-14 qualifier.
   - **Marriage certificate** (from 30 Sept 2024) must show each spouse's PRE-marriage civil status, with apostilled divorce or death certificates for any prior marriage.
   - **Apostille** on every public-record document from the issuing country's Hague authority; non-Hague countries need consular legalisation instead.
   - **Converts (giyur):** four dated, ink-signed, stamped letters on top of the standard list. Reform and Conservative conversions are accepted by Misrad HaPnim for aliyah but NOT by the Rabbanut for marriage, divorce or burial; route marriage questions to ITIM (itim.org.il).

**Nefesh B'Nefesh** (nbn.org.il) gives olim from the USA, Canada and the UK free assistance, flight subsidies, group flights, employment guidance and airport reception.

**Before departure:** notify banks about international transfers, get certified translations, choose a kupat cholim, consider the tax-free container. Detail: `references/aliyah-timeline-guide.md`.

### Step 2b: Shinui Ma'amad (Aliyah from within Israel)

Someone already in Israel on another visa (A1, student, work) can convert to oleh status through Misrad HaPnim rather than leaving and returning. Two things drive most of the friction: from **November 2024** applicants must present background checks from every country they lived in for **more than one year** (broader than the standard rule only in dropping the "after age 14" qualifier, NOT in shortening the period to six months), and the sal klita first payment arrives as a bank deposit rather than an airport card. **Time already spent in Israel counts against the 24-month presence test in Step 4**, which is where this route most often fails. Full procedure, A1 comparison and document set: `references/aliyah-additional-procedures.md`.

### Step 3: Arrival and First-Week Essentials

**At Ben Gurion Airport:** the Misrad HaKlita desk at arrivals issues the Teudat Oleh (your identification until the Teudat Zehut), the first sal klita payment (a prepaid card, with a larger cash component during strikes, chagim and emergencies), and a starter SIM. NBN group flights are met by their own representatives.

**First week, in order.** Day 1-2: register at Misrad HaPnim with the Teudat Oleh, passport and photos, and the Teudat Zehut follows automatically. Day 1-3: open the bank account (JOINT, for a couple) and register with a kupat cholim. Day 1-7: Bituach Leumi, an Israeli SIM, and a MyGov account (which needs the Israeli SIM for SMS verification). Week 1-2: register for ulpan, and for children aged 3-18 enrol at the municipal education department, asking about the Misrad HaChinuch **Sela** absorption programme. Children under 3 go to Step 4b for the no-income-test daycare tier. Documents needed per step and the full month-by-month timeline: `references/aliyah-timeline-guide.md`.

**Refund of pre-aliyah fees:** some consular, apostille and passport fees paid before you held a Teudat Oleh are reimbursable against original receipts, filed at the absorbing branch within the first year (`references/aliyah-additional-procedures.md`).

### Step 4: Sal Klita (Absorption Basket)

The sal klita is a financial grant provided by Misrad HaKlita to help olim during their first months.

**Eligibility (there is a presence test the ministry states and most summaries omit):**
- Entering Israel for the first time on an "oleh" visa, with full oleh entitlement
- **No more than 24 months in Israel, consecutive or cumulative, in the 3 years before receiving oleh status.** Someone who spent two and a half of the last three years in Israel on a student or work visa is outside the basket even with a valid Teudat Oleh, so ask about prior stays before quoting a figure.
- Ezrach Oleh and Katin Chozer applicants who meet the same rules are also entitled
- Must register with Misrad HaKlita within the first year
- Paid in monthly installments to the oleh's Israeli bank account

**Payment schedule (2026).** Three parts, and **there is NO seventh payment** for anyone, couples and families included: month 7 is where the post-basket entitlements in Step 4b begin, not another instalment.

1. A **prepaid card at Ben Gurion** on arrival (a bank deposit instead, for those changing status inside Israel).
2. A one-time **bank top-up** (השלמה לחשבון בנק) into the Israeli account, a separate line from the instalments. A couple must open a **joint** account and give the ministry its details.
3. **Six** monthly instalments, paid as living costs (דמי מחיה) during the ulpan period.

| Track | Ben Gurion | Bank top-up | Each of the 6 instalments | Total |
|---|---|---|---|---|
| Single | 1,250 | 1,544 | 3,150 | **21,694** |
| Single parent | 2,300 | 1,631 | 5,190 | **35,071** |
| Couple | 2,500 | 4,023 | 5,806 | **41,359** |

Two more full tables are keyed to the **statutory retirement age** (67 for men, 62 to 65 for women by birth year), NOT to age 65: pre-pension (single 26,785 / single parent 41,196 / couple 50,888) and pensioner (22,779 / 28,086 / 34,263). **Children are supplements to the family basket, never a basket of their own** (0-4 adds 12,831; 4-18 adds 8,521; 18-21 adds 11,039), and a household of 6+ adds 5,918. Per-line tables: `references/sal-klita-rates.md`.

The basket is **not income-tested**. Register within one year of receiving oleh status. **Leaving the country stops the payments**; they resume only if you return within the first aliyah year.

```bash
python scripts/sal-klita-calculator.py --status couple --child-ages 3,9 --track standard
```

The ministry publishes its own eligibility calculator on the same page; prefer it to an estimate when the oleh needs a number to rely on. An overpayment is clawed back via a promissory note (הסדרת חוב) issued through the personal adviser. The governing instrument is **נוהל משרד העלייה והקליטה מס' 14.211**; quote it when disputing a stopped payment or a debt demand.

Source: `gov.il/he/pages/absorption_basket` (updated 27.07.2026). Re-read that page before quoting a figure for a later year; never index the 2026 numbers yourself.

**Tracking payments:** the personal area (ezor ishi) at klita.gov.il shows payment status. Do NOT change the bank account number in the first years, and report it immediately if you must. The basket is not taxable income and is not repayable, but a late-opened bank account delays it.

### Step 4b: What Comes AFTER the Six-Month Basket

The basket stops at month 6. Most agents stop there too, and that is where olim lose the most money. Four entitlements run on afterwards. Details, conditions and exclusions: `references/post-basket-entitlements.md`.

- **Rent assistance (קצבת שכר דירה)** is the big one, and it is paid by **משרד הבינוי והשיכון**, not Misrad HaKlita. It is **automatic** into the bank account: from month **7 to month 30** for anyone who made aliyah from 01.03.2024, and from month 8 to the end of year 5 (year 6 for single parents) for the earlier cohort. No time limit for olim living on Bituach Leumi benefits; up to 36 months around IDF or national service; from month 1 for נעל"ה graduates. Capped at 95% of the rent, declining with time in Israel. It is NOT automatic for someone who arrived past retirement age. Hotline \*2310.
- **Two different post-basket income supports, at two different agencies.** **הבטחת קיום** is paid by Misrad HaKlita in the second half of the first aliyah year in six separately-gated tracks (ill or hospitalised, caring for a sick relative, pregnant, under 65, single-parent family, disability or blindness). **הבטחת הכנסה** is the Bituach Leumi benefit the ministry's page points to at the end of month 6, and ulpan attendance can substitute for its employment-bureau condition. Do not send a pregnant oleh to the wrong counter.
- **An oleh who arrived past retirement age is NOT uninsured-and-therefore-unentitled.** They get the **special old-age pension** (גמלת זיקנה מיוחדת) at the basic single rate: 1,838 NIS to age 80, 1,941 from 80 (2026), with spouse and child additions and השלמת הכנסה where income is low.
- **Daycare subsidy with NO income test:** an oleh parent within 2 years of aliyah at the start of the school year gets tier 3 of the מעונות יום tuition table for every child, provided both parents are either in ulpan for 24+ hours a week or registered as job-seekers (or one of each).

### Step 5: Ulpan (Hebrew Language Program)

Four things are commonly stated wrongly, so state them correctly:

- Funding covers **420 to 450 hours** of Ulpan Aleph, for olim **aged 17 and over**. It is a range, not a round 500.
- **18 months is the entitlement PERIOD, not a start-by deadline.** It runs 18 months from the aliyah date, **24 months** for olim on havtachat hachnasa, and the branch extends it on request for pregnancy or childbirth, childcare, a move, family distress, or illness. Do not tell an oleh at month 17 that the door is closing.
- The **80%-attendance** rule belongs to the private-institution **voucher** route, not the public ulpan. That voucher reimburses actual cost up to **5,000 NIS** for a course of up to 6 months (8 by prior written approval) and releases its final 30% only against a completion certificate.
- Voucher eligibility runs while **10 years** since aliyah have not elapsed, and **15 years** for olim from Ethiopia, Yemen and Bnei Menashe.

Ulpan hours are also the gate for the no-income-test daycare tier in Step 4b, and the six sal klita instalments are formally the living costs (דמי מחיה) for this study period. Options, levels and registration: `references/aliyah-timeline-guide.md`.

### Step 6: Housing for Olim

Rentals run through Yad2 and city Facebook groups; agents charge about a month's rent; mercazei klita provide temporary housing. Expect arevut of roughly 3 months' rent, post-dated cheques, plus arnona and vaad bayit.

**The oleh housing benefits worth naming out loud:** an arnona discount of up to 90% on 100 sq m, given for **12 months out of the 24** that start on the day the oleh is registered in the population registry (so it need not be claimed in month one), with the percentage at the municipality's discretion, and up to 80% on the WHOLE apartment for olim on a long-term-care or dependency-based disability benefit. **Rent assistance is the larger benefit and it is covered in Step 4b**, because it mostly starts after the basket ends. Reduced mas rechisha applies on a first property (`references/tax-benefits-olim.md`), and a lawyer is required for every Israeli real-estate transaction. Rental mechanics, mercazei klita and buying detail: `references/aliyah-additional-procedures.md`.

### Step 7: Banking for Olim

Leumi, Hapoalim, Discount, Mizrahi-Tefahot and Mercantile all run oleh desks. Bring Teudat Zehut or Teudat Oleh, passport, proof of address, and proof of income if you have it. Open the account in the first days, because the sal klita bank top-up and instalments cannot be paid without an Israeli account, and a couple needs a JOINT one that both must attend the bank to open.

**Bringing money declaration:** the threshold DEPENDS ON THE CROSSING, not on one national figure: NIS 12,000 at the five land crossings (Nitzana, Erez, Jordan River, Yitzhak Rabin, Taba), 2,000 dinar (about NIS 10,000) at Allenby, and NIS 50,000 everywhere else including Ben Gurion. Someone entering overland can be far under 50,000 and still obliged to declare. "Funds" covers cash, bank and traveller cheques, negotiable securities and instruments, and immediate-debit cards. Transfer, cheque and horaat-keva practicalities: `references/aliyah-additional-procedures.md`.

### Step 8: Tax Benefits for Olim

Section 14 of the Income Tax Ordinance is the anchor. Full rules, brackets and conditions: `references/tax-benefits-olim.md`.

**10-year foreign-income exemption:** exempt from Israeli tax on foreign-source income (pensions, rent abroad, dividends, capital gains, foreign business income) for 10 years from the aliyah date, for olim chadashim and toshavim chozrim vatikim alike. **Branch on the aliyah date for REPORTING:** olim arriving from 1 January 2026 must report worldwide income and assets even where it is untaxed; those who arrived earlier keep both the tax and the reporting exemption. Saying "no reporting" to a 2026 oleh is the common error.

**Tax credit points (nekudot zikui):** the ladder was reformed in 2022, so **branch on the aliyah date** here too. An oleh who arrived **in 2022 or later** gets 8.5 points over **54 months**, not 42:

| Months since aliyah | Points per month | Monthly value (2026) |
|---|---|---|
| 1-12 | 1/12 of an annual point | 242 NIS |
| 13-30 | 1/4 | 726 NIS |
| 31-42 | 1/6 | 484 NIS |
| 43-54 | 1/12 | 242 NIS |

The first year is deliberately the LOWEST rung, because most olim are not yet earning. Anyone who arrived **before 2022** is on the legacy 42-month / 7.5-point ladder, which starts at the 1/4 rung. One point is worth **242 NIS a month / 2,904 a year (2026)**, so full use of the post-2022 ladder is about **24,700 NIS** of tax. These sit ON TOP of the resident points, which are 2.25 for a resident and **2.75 for a woman resident** (every woman gets half a point more), so never present 2.25 as the base for a female oleh. They apply automatically once the employer is told via Form 101, and reduce tax owed, not taxable income. **Regular IDF service and post-secondary study pause the clock rather than extend it** (automatic, not an election); otherwise it runs from the teudat oleh even in months with no income, and those months are lost.

**New-oleh Israeli-source income exemption (2026 incentive window):** residency established between **5 November 2025 and 31 December 2026** buys a tiered exemption on **earned** Israeli-source income (salary and self-employment only, never passive), on top of Section 14: 600,000 NIS in 2026, 1,000,000 in each of 2027 and 2028, 350,000 in 2029, 150,000 in 2030, capped at 140,000 a year for work for a related party. The anti-abuse clause has **two cumulative limbs joined by "and", not "or"**: it bites only on someone who BOTH ceases to be an Israeli resident during 2028 or 2029 AND spends fewer than 75 days in Israel in those years, so an oleh who merely travelled a lot keeps it. Outside that window only the standard Section 14 benefits apply.

**Olim DO have the Acclimatization Year election** (shnat histaglut). This is the opposite of what is usually assumed, and getting it backwards costs an oleh a year of deferral. The ministry's own service states that "new immigrants or returning residents (in accordance with the determination by the Tax Authority) can choose to have their first year considered as an acclimation and settling in year for the purpose of the directive of the income tax". It is filed online **within 90 days of receiving the status** and **only once**; during that year the person is not an Israeli tax resident, which pushes out both the Section 14 clock and the first reporting obligation; and it does not delay Misrad HaKlita assistance, which runs from the status date either way. It interacts with the 2026 window's residency-start date, so raise it and route the decision to a tax adviser. Toshav chozer cases go to `israeli-toshav-chozer-vatik-tax-planner`.

**Buying a car with olim benefits (3-year window):** reduced purchase tax within 3 years of oleh status. Three things people get wrong: the 4-year lock runs on USE of the car in Israel (months abroad beyond 12 must be made up before a tax-free sale); a couple gets ONE discounted car between them, and nobody outside the couple may drive it; and the window extends for IDF or national service and, exceptionally, via the Tax Authority's exceptions committee. Never tell an oleh who missed the window that the benefit is gone. Also: reduced customs on personal belongings, tax-free container shipment, VAT relief on some first purchases. Conditions: `references/aliyah-additional-procedures.md`.

**No asset or income test on sal klita.** The ministry states the entitlement does not depend on income ("הזכאות לסל קליטה אינה תלויה בגובה ההכנסה"), with no capital declaration and no asset ceiling. Do not tell an oleh that savings will cut their basket.

**BL / US-Social-Security coordination:** olim from the US still paying US Social Security may get a limited exemption from the matching BL contributions under the totalization arrangement. Scope has moved with recent BL/SSA amendments, so verify with Bituach Leumi (*6050) and the SSA international office rather than quoting historical specifics.

**Reporting:** Israeli-source income is reported from day one; file a doch shnati above the filing threshold or under the 2026-onwards rules. Complex foreign-asset cases go to a yo'etz mas.

### Step 9: Bituach Leumi (National Insurance)

**Registration:** every oleh registers with Bituach Leumi, at a branch or online, and that registration triggers health coverage through a kupat cholim.

**Benefits eligibility timeline:** health cover is immediate on kupat cholim registration, and child allowances are immediate for children under 18. A maternity grant needs a qualifying residency period and unemployment needs 12 months of employment. The contributory old-age pension turns on years of residency and contributions, **but an oleh who arrived past retirement age gets the special old-age pension instead (Step 4b), so never end that sentence at "they are not insured"**.

**Health insurance:** actively pick one of the four HMOs (Clalit, Maccabi, Meuhedet, Leumit). The basic basket is universal by law; switching is allowed in the transfer periods. Contributions come out of salary for employees, monthly for atzma'im, and an oleh not yet employed should check their status because cover depends on it.

**Child Savings Plan (Chisachon LeKol Yeled):** opened automatically for every child up to 18 once the child has a Teudat Zehut, with a monthly state deposit. Parents may double it and choose a bank account or a kupat gemel. Activate it in the personal area in the first month. See `references/aliyah-additional-procedures.md`.

### Step 10: Driver's License Conversion

Conversion turns on driving experience, not country of origin (that system ended in August 2017).

| Driving Experience | Process |
|---|---|
| 5+ years consecutive | Administrative conversion only (medical certificate + documents, no tests). BOTH conditions must hold: 5+ years on the foreign licence AND a target category of 1, A, A1, A2 or B. Any other category still needs the practical test |
| Under 5 years | A **full practical driving test** (test / מבחן נהיגה מעשי), not a short "control test". Two attempts are allowed. No theory up front; theory becomes required only after **failing twice**, followed by a further practical, and on that retest path the applicant is **exempt from the minimum-lessons requirement** |
| Under 2 years | The same practical test, plus classification as a **nahag chadash** with the restrictions that carries. Do not quote a lesson count |

**Conversion window:** the conversion must be done within the first 5 years in Israel. Separately, the foreign licence may be used to drive in Israel for **one year from the date of entry**. Those are two different clocks: an oleh past month 12 who has not converted may no longer drive on the foreign licence even though the conversion window is still open.

See `references/driver-license-conversion.md` for the full per-tier procedure, required documents, theory-test languages, and common rejection reasons.

### Step 11: Professional License Recognition

**Before quoting costs, say what the state pays for.** Misrad HaKlita funds preparatory courses for the state licensing exams in medicine, accountancy, pharmacy, law, veterinary medicine and dentistry, contributes to the **notarial translations** the process requires, and provides exam accommodations for olim. Separately, **המינהל לסטודנטים עולים** funds tuition for olim admitted to a recognized institution (degree, hendesai, and certificate tracks), on a clock of **36 months from receiving the status**, excluding military and national service. Confirm an institution is recognized BEFORE enrolling. See `references/post-basket-entitlements.md`.

Professional recognition (hakarat miktzoa) varies by field, but the shape is constant: apostille the academic documents, get certified Hebrew translations, submit to the recognizing body for that profession, sit any required exam or supplementary training, and receive the Israeli rishyon miktzoi. Per-field process, exams, recent reforms and common rejection causes: `references/professional-recognition.md`. Month-by-month first-year timeline: `references/aliyah-timeline-guide.md`.

### Step 11b: IDF Draft, Lone Soldier, Teudat Ma'avar

Men aged 18-22 and women aged 18-20 get a Tzav Rishon from IDF Meitav once Misrad HaPnim registration completes; deferrals exist for academic study, yeshiva, and new-oleh adjustment of up to a year. An oleh serving with no parents resident in Israel must **request Chayal Boded status explicitly at induction**: it carries a salary supplement, a paid month a year to visit family abroad with an IDF-covered flight, a housing subsidy, counselling at Mador HaBoded, an end-of-service grant, and it extends rent assistance (Step 4b). And an oleh does NOT get a full Darkon straight away, but a **Teudat Ma'avar**, a one-year travel document, which some countries will not accept, so plan travel around it. Deferral tracks, exemptions and travel-document specifics: `references/aliyah-additional-procedures.md`.

### Step 12: Alternate Aliyah Statuses (Route the User Correctly)

Not every aliyah is a standard Oleh Chadash. Identify which of these applies **before** quoting Sal Klita figures or document lists, because eligibility, documents and benefits all differ: **Ezrach Oleh** (born abroad to a parent who was an Israeli citizen at your birth), **Katin Chozer** (left Israel before age 14), **Aliyah BaShenit** (previously a citizen, renounced), **Aliyah BeNifrad** (family arriving at different times within a year, where the basket is per FAMILY unit and later arrivals get only the remainder), and **ARLI** (renouncing within 3 months, reversible inside the window). Conditions, document sets and the responsible authority for each: `references/alternate-aliyah-statuses.md`.

**Verify citizenship status before any change** (marriage, divorce, birth, foreign naturalization, ARLI) in the Misrad HaPnim "Citizenship Status" page in MyGov. Stale records cause Bituach Leumi suspensions and wrong IDF service-obligation calculations.

For Toshav Chozer, which is NOT a Law of Return status and does NOT get the oleh Sal Klita, route to `israeli-returning-resident-navigator`; for Section 14 mechanics, to `israeli-toshav-chozer-vatik-tax-planner`. A Toshav Chozer certificate is a returnee certificate, not an oleh one: reroute and stop quoting oleh figures.

## Examples

### Example 1: Pre-Arrival Planning for a Family from the USA

User says: "We're a family of 4 making aliyah from the US next month. What do we need to prepare?"

Actions:
1. `python scripts/aliyah-checklist.py --stage pre-arrival --family family --country usa --profession tech`, then the Step 2 document set
2. Ask how long they have spent in Israel in the last 3 years, because of the sal klita 24-month presence test
3. `python scripts/sal-klita-calculator.py --status couple --child-ages 5,12`, and say plainly that it covers six months
4. Walk them to Step 4b: rent assistance from month 7, and, if a child is under 3, the no-income-test daycare tier that both parents unlock by doing 24 ulpan hours a week
5. Nefesh B'Nefesh for US olim; morning ulpan for the non-working spouse, evening for the working one

Result: a plan that covers the whole first two and a half years, not only the basket.

### Example 2: Professional License Conversion for a Doctor

User says: "I'm a physician from France, how do I get my medical license recognized in Israel?"

Actions:
1. Medical, so Misrad HaBriut (Step 11); outline the credential review for EU-trained physicians, the Hebrew terminology exam and the stazh
2. **Say up front that the state funds the licensing-exam prep course AND contributes to the notarial translations**, before they pay for either
3. Point at `references/professional-recognition.md`, and at the Student Authority if they need further study

Result: a licensing path (typically 1-2 years) with the funded support named rather than discovered late.

### Example 3: Understanding Sal Klita Payments

User says: "I made aliyah 2 months ago and haven't received my second sal klita payment. What should I do?"

Actions:
1. Verify the user opened an Israeli bank account and shared details with Misrad HaKlita
2. Check expected payment schedule (Step 4)
3. Calculate expected amount: `python scripts/sal-klita-calculator.py --status single`
4. Check the personal area (ezor ishi) at klita.gov.il, then the local branch with Teudat Oleh and bank details
5. Usual causes: wrong bank details, incomplete registration, or a trip abroad that stopped the payments

Result: a concrete troubleshooting path for a delayed instalment.

### Example 4: Tax Planning for an Oleh with Foreign Assets

User says: "I have rental income from an apartment in London. Do I need to pay Israeli tax on it?"

Actions:
1. Explain the 10-year foreign-income exemption (Step 8); UK rental income is exempt foreign-source income
2. **Branch on the aliyah date before saying anything about reporting.** An oleh who arrived from 1 January 2026 must REPORT the income even though it stays untaxed; one who arrived earlier keeps both exemptions. Saying "no reporting" to a 2026 oleh is the common error here
3. Note that UK tax obligations continue regardless of Israeli residency, and raise the Acclimatization Year if they are inside the 90-day window
4. Send complex cases to a dual-qualified adviser; rules in `references/tax-benefits-olim.md`

Result: the income is exempt from Israeli tax for 10 years, with the reporting answer correctly branched on the arrival date.

## Bundled Resources

### Scripts
- `scripts/aliyah-checklist.py` -- prioritized checklist by stage, family, country, profession. `--help` for flags.
- `scripts/sal-klita-calculator.py` -- 2026 basket by track, status, child ages, household size. `--help` for flags.

### References
- `sal-klita-rates.md` -- the four full 2026 basket tables plus the rules that travel with them.
- `post-basket-entitlements.md` -- rent assistance, havtachat kiyum, the special old-age pension, daycare subsidy, Student Authority, funded licensing support.
- `tax-benefits-olim.md` -- Section 14, the credit-point ladders, the 2026 incentive window, mas rechisha, customs, reporting.
- `aliyah-timeline-guide.md` -- month-by-month first year, first-week actions, ulpan options.
- `aliyah-additional-procedures.md` -- A1 vs oleh visa, Shinui Ma'amad, housing, banking, MyGov, pre-aliyah refunds, buying a car.
- `alternate-aliyah-statuses.md` -- per-status conditions for the five alternate statuses.
- `pre-aliyah-documents.md` -- the full pre-arrival document set and its authentication rules.
- `driver-license-conversion.md` -- per-tier licence conversion procedure.
- `professional-recognition.md` -- per-field credential recognition and recognizing bodies.
- `troubleshooting.md` -- diagnosed failure modes, EN and HE.

## Recommended MCP Servers

| MCP | What It Adds |
|-----|-------------|
| [kolzchut](https://agentskills.co.il/he/mcp/kolzchut) | Live rights articles from Kol Zchut, the authoritative Israeli rights base. Use `kolzchut_search_rights` for "סל קליטה", "סיוע בשכר דירה לעולים", "הטבות מס לעולים" or "גמלת זיקנה מיוחדת" to get current-year figures and eligibility rules. Fall back to this skill's static guidance when it is not installed. |

## Gotchas
- Sal klita amounts change annually and differ by family size and age band. Agents routinely quote a previous year's figures.
- Agents treat the six-month basket as the whole entitlement and stop at month 6. Rent assistance, havtachat kiyum and the special old-age pension all start after it (Step 4b), and missing them costs an oleh far more than any figure in the basket table.
- Misrad HaKlita and the Jewish Agency handle different parts of the process, and agents send users to the wrong one.
- Oleh credit points run 54 months (2022 onward) or 42 (legacy), not permanently. Agents omit the expiry or quote the wrong ladder for the arrival year.
- Professional recognition takes months to years and differs per profession, and agents underestimate it.
- The Acclimatization Year (shnat histaglut) is NOT returning-resident-only. Olim have it too, on a 90-day filing deadline, and an agent that denies it costs the user a year of deferral.

## Reference Links

| Source | URL | What to Check |
|---|---|---|
| Misrad HaAliyah V'HaKlita | https://www.gov.il/en/departments/ministry_of_aliyah_and_integration | Sal Klita amounts, ulpan list, eligibility |
| Klita.gov.il personal area | https://www.klita.gov.il/ | Payment status, rights and forms |
| Kolzchut, olim and returning residents | https://www.kolzchut.org.il/he/עולים | Rights pages with statute citations and current-year amounts |
| Nefesh B'Nefesh | https://www.nbn.org.il/ | Flight subsidies, rights summaries, employment guidance |
| Jewish Agency (Sochnut) | https://www.jewishagency.org/aliyah/ | File opening, document upload, eligibility |
| Shivat Zion knowledge base | https://shivatzion-support.freshdesk.com/en/support/solutions/501000214842 | Apostille and background-check authorities by country, alternate-status overviews |
| Bituach Leumi | https://www.btl.gov.il/ | Registration and benefit eligibility timelines |
| Israel Tax Authority, olim | https://www.gov.il/en/departments/israel_tax_authority | Section 14 details, reporting obligations |

## Troubleshooting

See `references/troubleshooting.md`.
