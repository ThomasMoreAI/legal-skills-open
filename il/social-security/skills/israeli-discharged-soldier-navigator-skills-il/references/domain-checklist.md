# Domain Coverage Checklist, israeli-discharged-soldier-navigator

Generated: 2026-05-18. Last re-litigated: 2026-08-27 (v1.5.0), against hachvana.mod.gov.il, the Kol Zchut discharged-soldier rights index, and the consolidated statute on nevo.co.il.

## Must cover (core)

- [x] **Pikadon eligibility rules**, IDF / MAGAV / Police / SHABAS / SLE, minimum 12 months (less if medical / training injury), source: kolzchut Pikadon page, why core: most common first question; SLE / under-12-months edge cases mislead users
- [x] **Pikadon monthly amount per service type (May 2026)**, lochem 990.63, tomech lechima 825.52, orfi 660.42, SLE 660.42, intermediate civilian track 495.38, split civilian track 330.25 NIS/month, AND the training reclassification (a combat soldier's first 4 training months accrue at the combat-support rate; a combat-support soldier's first 2 accrue at the "other" rate). Grant rates per month: 684.99 / 570.42 / 455.84 / 342.50 / 227.92, source: hachvana DepositUpTo5 page, why core: the "kama magia li?" answer; tier multipliers needed for sanity-check; instruct user to verify via official calculator since rates change monthly with index
- [x] **Pikadon 14-day availability rule (IDF) vs 30-day (SLE)**, source: kolzchut Pikadon page + hachvana, why core: distinct from 60-day grant timeline; users confuse the windows
- [x] **6 permitted pre-5y withdrawal purposes (exact Hebrew list)**, לימודים אקדמיים, הכשרה מקצועית, לימודי נהיגה, פתיחת/השקעה בעסק, נישואין, רכישת דירה/בית/קרקע. **Rental NOT included.**, source: hachvana GrantAndDeposit + DepositUpTo5, why core: most common user mistake is assuming rent qualifies; closed statutory list per Chok Klitat Chayalim Meshuchrarim
- [x] **5-year auto-transfer rule**, at end of 5 years remaining balance auto-transfers to bank for any purpose, source: kolzchut Pikadon page, why core: the "I forgot about my Pikadon" recovery flow
- [x] **Discharge grant (manak shichrur)**, separate from Pikadon, 20-60 days from end of service, unrestricted use, source: hachvana GrantAndDeposit + kolzchut grant page, why core: users confuse this with Pikadon; the grant is separate and unrestricted
- [x] **Tax exemption (Pikadon and grant)**, Section 9(27) Pkudat Mas Hachnasa, source: kolzchut, why core: prevents users panicking about tax on withdrawal
- [x] **Tax credit points (nekudot zikui), Section 39a, NOT 11**, 36 months from month after discharge, 2 points/year at >=23 months (male), >=22 (female), >=24 (SLE); otherwise 1 point/year from 12 months. State as thresholds, not ranges: the source table is inconsistent about the boundary month. An early medical discharge under 12 months is deemed to have completed 12. 2026 value: 242 NIS/month per point. Total benefit: ₪8,712 or ₪17,424, source: kolzchut nekudot zikui page, why core: single largest year-1 tax saving; service-length table routinely misquoted
- [x] **How to claim nekudot zikui (Tofes 101 + Tofes 135 retroactive)**, source: kolzchut nekudot zikui page, why core: unclaimed benefit = lost money
- [x] **Iron Swords full-tuition combat-soldier law**, Knesset legislation passed late 2023 covering 100% annual tuition for combat soldiers discharged from Oct 2023 onward, usable up to 5 years post-discharge, source: Times of Israel + hachvana IronSwords page, why core: most valuable post-discharge benefit for a typical 21-year-old planning university
- [x] **MY VISIT app / personal area at hachvana.mod.gov.il**, single login for balance, withdrawals, bank account updates, career-counselor scheduling, source: hachvana, why core: no manual/paper flow for most actions
- [x] **Required documents**, Teudat Shichrur, Teudat Zehut, Israeli bank account; purpose-specific evidence for withdrawals, source: hachvana, why core: missing Teudat Shichrur blocks every benefit
- [x] **Service-type cap: 32 months male / 24 months female**, source: hilan Chapter ג summary, why core: extra unpaid service does not accrue Pikadon
- [x] **Pikadon non-transferable / non-pledgeable / non-seizable**, source: hilan Chapter ג, why core: cannot be used as loan collateral

- [x] **Section 19 end-of-window mechanics**, auto-transfer within 60 days at year 5; 120 days to redeem after the Fund makes contact where the bank account cannot be located; forfeiture to the Additional Assistance Fund at 5.5 years with 4.5 years to reclaim; residue of 50 NIS or less to the Treasury; and the s.19(b)(2) early release at 3 years for a lochem with 3 further keva years. Source: nevo consolidated text s.19. Why core: this is the only path by which a user LOSES the Pikadon outright, and a stale bank account (already the skill's most common failure) is what triggers it.
- [x] **The 10-year window belongs to s.7(a) and s.7A, NOT the Pikadon**, s.19(a1)(1), added by Amendment 19 of 12.07.2017 and re-enacted by Amendment 24 of 2022, for active reservists and lone discharged soldiers. Source: nevo s.19(a1), s.7(a), s.7A. Why core: the skill asserted the opposite through v1.4.0 and contradicted `israeli-lone-soldier-rights`, which had it right.
- [x] **Chok Chayalim Meshuchrarim (Hachzara LaAvoda), 5709-1949**, right to return to the pre-draft employer, 6 months of employer obligation, service counted as seniority, and a written request between 15 days before and 30 days after discharge. Source: Kol Zchut "חזרה לעבודה של חייל משוחרר". Why core: the shortest deadline in the domain, it lapses silently, and it is a named statute a user will hear about elsewhere.
- [x] **Service-classification appeals go to the IDF, not the Department**, קצין פניות הציבור, 1111 extension 5. Source: Kol Zchut Pikadon page, "ערעור". Why core: v1.4.0 routed users to a "Mador Iturim" that appears in no source.

- [x] **The Fund pays the provider, not the soldier**, s.15(a) for institutions under ss.12-14 and s.17(b) for the seller of a dwelling. Source: nevo. Why core: the skill described all six purposes as a "withdrawal" through v1.4.0, so users planned around cash that never arrives.
- [x] **s.12 funds bagrut completion, a mechina, and psychometric preparation in their own right**, not merely as a route into a degree. Source: nevo s.12. Why core: the no-bagrut cohort is large and was being routed away.
- [x] **The six purposes are the current Schedule, not a closed statutory list**, s.18א lets the Minister add to it, and marriage (2001) and driving lessons (2015) arrived that way. Source: nevo s.18א + the תוספת.
- [x] **Keva servers are discharged soldiers for 5 years from the end of CHOVA**, so every Pikadon clock is anchored there and a three-year keva leaver is already past the window. Source: Kol Zchut Pikadon, "מי זכאי". Why core: it decides every keva case and the skill was silent on it.
- [x] **Credit points run DURING keva and the 36 months start after chova**, so a keva leaver typically has 13 months left, not 36, and a serving keva soldier should file Tofes 101 now. Source: Kol Zchut nekudot zikui, worked example.
- [x] **Hesder / SHLAT counts total service from enlistment for the credit-point threshold**, even though unpaid service does not accrue Pikadon. Source: Kol Zchut nekudot zikui, worked example. Why core: thresholding on paid months halves the entitlement.
- [x] **The female accrual cap is contested**, hachvana publishes 24, s.11(a) after Amendment 16 reads 28, with commencement tied to s.16א(ד). Use 24 and flag it; never assert it flatly.
- [x] **Chok Chayalim Meshuchrarim (Hachzara LaAvoda)**, with the 45-day request window, the 6-month employer obligation, the employer's burden of proof, the one-year fallback placement, and ועדת תעסוקה as the statutory forum. Source: Kol Zchut חזרה לעבודה.
- [x] **Heirs are eligible for a death during service OR after discharge**, so only a death in service routes to Mador Mishpachot Shakulot. Source: Kol Zchut Pikadon, "מי זכאי".
- [x] **Tofes 116 (תיאום מס)** for a mid-year start or a second employer. Source: Kol Zchut nekudot zikui, "תיאום מס".

## Should cover (advanced / edge cases)

- [x] **SLE parity vs IDF**, same 12-month threshold, SLE gets the regular (acher) tier rate, 30-day rule (not 14), source: hachvana
- [x] **Service-type classification on Teudat Shichrur**, combat-support vs combat drives the multiplier; the appeal route is the IDF public-enquiries officer on 1111 extension 5 (corrected 2026-08-27 from "Mador Iturim", which no source supports)
- [x] **Pikadon for rishyon nehiga**, permitted; need driving school receipts
- [x] **Pikadon for opening a business**, needs Osek Patur/Murshe registration; defer to israeli-freelancer-ops for the Osek setup
- [x] **Pikadon for apartment purchase**, permitted for purchase only, NOT rental; flag mashkanta interaction (defer to israeli-mortgage-comparator)
- [x] **Pikadon for marriage**, evidence: Teudat Nisuin or wedding hall receipts
- [x] **Withdrawal for academic studies abroad**, **NOT eligible**. Corrected 2026-08-27: this row previously said the opposite. Two sources say verbatim that the Pikadon is realisable in Israel only, hachvana ("כספי הפיקדון האישי ניתנים למימוש בתחומי מדינת ישראל בלבד") and Kol Zchut ("כספי הפיקדון ניתנים למימוש רק במדינת ישראל"). Recognition of the foreign institution is irrelevant.
- [x] **Tofes 135 retroactive refund up to 6 years back**, if employer failed to apply credit points
- [x] **Pikadon inheritance on death in service**, refer to Mador Mishpachot Shakulot
- [x] **Wounded-soldier rate preservation**, a lochem or tomech lechima wounded during or as a result of training or operational activity who moves to another role keeps the higher amount for the WHOLE service period. Source: Kol Zchut Pikadon, "כדאי לדעת"
- [x] **Pikadon 2000 dormant balances**, service ended after 01.01.1995 or begun before 31.12.2000; check the personal area, then email the Fund
- [x] **Adjacent-benefit disqualifiers**, the conditions that decide the Step 8.5 rows rather than their headline amounts: the 42-month claim deadline and 11,461 NIS (2026) for the required-work grant, the 60-day Rav-Kav profile deadline, the arnona owner-or-renter requirement, the 688 NIS/month income ceiling on the BL exemption. Held in `references/adjacent-benefits.md`
- [x] **Mortgage supplement**, 1% per service month, joint cap 46% single / 65% couple. Mentioned and routed rather than computed, see the out-of-scope note below
- [x] **Free Ministry of Justice legal aid** on discharged-soldier rights
- [x] **Mimadim LiLimudim extended-window rules**, verified 2026-08-27: base 5 years, +1 for bagrut / mechina / psychometric, +2 for a continuous year or more of keva, +3 for both. Note the statute (s.7A1(d)) measures from the END of the discharge year and gates on starting studies, while the website measures from discharge and gates on the first application. Full terms in `references/mimadim-scholarship.md`.
- [x] **Adjacent benefits (mention-and-link)**: Bituach Leumi + health exemption window, free public transport window, arnona discount, year-1 dmei avtala for discharged soldiers, Bahatzda discount card. Exact durations and thresholds change, surface as routes to the specialist skills (`israeli-bituach-leumi`, `israeli-unemployment-benefits-navigator`) and to the relevant municipal/transit operator rather than asserting specific magnitudes here.

## Out of scope (explicit, with rationale)

Re-litigated 2026-08-27 against the two tests: would an ordinary user ask for this, and has it
become capturable since the row was written? Two rows changed as a result. The mortgage
supplement was reopened, because users DO ask "how much more mortgage do I get for my service"
and the answer (1% per service month, joint cap 46%/65%) is a published figure this skill can
state in one line rather than routing blind; it is now a mention-and-route row in Step 8.5 with
the number, while the mortgage itself stays out. The lone-soldier row was refreshed: that skill
now exists and is live, and it is the authority on the s.7(a)/7A 10-year window, so this skill
defers to it rather than restating it. The remaining rows survive both tests unchanged.

- Reservist (miluim) compensation → `israeli-miluim-manager`
- Lone soldier (chayal boded) post-discharge specific package → `israeli-lone-soldier-rights` (live). That skill owns the s.7(a) / s.7A 10-year window; do not restate it here beyond the Step 5 correction. Re-confirmed out of scope 2026-08-27.
- Academic scholarships beyond Mimadim (PEREACH, Adams, Rothschild, Rashi) → `israeli-academic-scholarships`
- Vocational course catalog matching → potential future skill
- PTSD / Aka 8944 disability recognition → `israeli-miluim-manager` + `israeli-mental-health-navigator`
- Mortgage benefits / Misrad HaShikun discount → `israeli-mortgage-comparator` + `israeli-real-estate`. **Partially reopened 2026-08-27**: the service-based supplement (1% per month, joint cap 46%/65%) is now stated in Step 8.5 because it is a one-line published figure users ask for. Everything downstream of it stays out of scope.
- General Bituach Leumi benefits → `israeli-bituach-leumi`
- Pension funds, keren hishtalmut → `israeli-pension-advisor`
- Voluntary tax refund flow for salaried employees (Tofes 135 broader use) → `israeli-employee-tax-refund`

## Authoritative sources

- https://www.hachvana.mod.gov.il/Pages/default.aspx, MoD Department for Discharged Soldiers homepage; verify channels and service map
- https://www.hachvana.mod.gov.il/GrantAndDeposit/Pages/default.aspx, Grant + Deposit hub; verify 6-purpose list and 60-day grant timeline
- https://www.hachvana.mod.gov.il/GrantAndDeposit/DepositUpTo5/Pages/default.aspx, Pikadon pre-5y page; verify current per-tier monthly NIS amounts (change monthly with CPI)
- https://www.hachvana.mod.gov.il/IronSwords/Pages/sword.aspx, Iron Swords wartime benefits hub; verify which expansions remain in force
- Kol Zchut: search "פיקדון אישי לחיילים משוחררים", Pikadon page (6-purpose canonical list, SLE 30-day rule, medical-early-discharge exception)
- Kol Zchut: search "נקודות זיכוי ממס הכנסה לחיילים משוחררים", nekudot zikui (36-month duration, service-length point table, Section 39a, Tofes 101 + Tofes 135 process)
- Kol Zchut: search "מענק שחרור לחיילים משוחררים", discharge grant (20-60 day window)
- https://www.nevo.co.il/law_html/law01/150_023.htm, Chok Klitat Chayalim Meshuchrarim full text; statutory base
- hilan.co.il legislation center "חוק קליטת חיילים משוחררים פרק ג פקדון ומענק", Chapter ג summary (sections 8-11); verify caps and non-transferable clause
- https://www.hachvana.mod.gov.il/MainEducation/HachvanaScholarship/Pages/UniformToStudies.aspx, MoD Department for Discharged Soldiers and Reservists, official Mimadim LiLimudim page: 100% tuition funding, gold-honour vs honour eligibility tracks, and the 5-year application window with its extensions
- https://www.kolzchut.org.il/he/החזר_מס_הכנסה, Kol Zchut Tofes 135 process for retroactive employee tax refunds (6-year window, 4% interest)
