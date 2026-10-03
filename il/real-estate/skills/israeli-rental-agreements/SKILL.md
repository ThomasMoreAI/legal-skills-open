---
name: israeli-rental-agreements
title: Israeli Rental Agreements
description: Guide users through Israeli rental agreements, tenant and landlord rights, and lease negotiation. Use when user asks about rental contracts (chozeh schirut), tenant rights, landlord obligations, deposits (arancia), rent increases, index-linked rent (hatzmada la'madad), the Fair Rental Law 2017, eviction procedures, or common red flags in Israeli leases. Covers essential contract elements, guarantees, dispute resolution, and the Tenant Protection Law. Do NOT use for commercial leases, property purchase transactions, or mortgage advice.
author: skills-il
author_url: https://github.com/skills-il/legal-tech/tree/master/israeli-rental-agreements
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: real-estate
language: en
sources:
- title: Contract checklist
  path: references/contract-checklist.md
- title: Fair rental law summary
  path: references/fair-rental-law-summary.md
- title: Statutory provisions
  path: references/statutory-provisions.md
---

# Israeli Rental Agreements

## Legal notice

This is a free information tool operated by an AI model. It explains the law and the procedure and helps you organise your own documents. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate. The output is not legal advice and not a legal opinion, but a general explanation and a template only: it does not read the full file of your matter, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

Any text this tool drafts is an automatic draft for your personal preparation only. It is not a document prepared by an advocate and must not be relied on as evidence. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person. Before starting proceedings, signing a document, or filing with an authority or a court, consult an advocate. All use of its output is the user's sole responsibility.


## Instructions

### Step 1: Israeli Rental Law Framework
Israel's residential rental market is governed by several key laws:

| Law | Hebrew | Year | Key Provisions |
|-----|--------|------|----------------|
| Rental and Borrowing Law | חוק השכירות והשאילה | 5731-1971 | The governing statute. The 2017 "fair rental" rules are an amendment to it, sections 25א-25טו, not a separate law |
| Guarantee Law | חוק הערבות | 5727-1967 | Governs guarantors (arevim). Protects an ערב יחיד / ערב מוגן, see Step 3 |
| Tenant Protection Law | חוק הגנת הדייר | 1972 | Pre-1968 protected tenancies only (rare today) |
| Standard Contracts Law | חוק החוזים האחידים | 5743-1982 | Route to strike an unfair clause in a lease that section 25טו EXCLUDES from the chapter |

**On naming**: "Fair Rental Law 2017" (חוק שכירות הוגנת) is not a standalone statute. It is the 2017 amendment inserting sections 25א-25טו (chapter 1, siman vav) into the Rental and Borrowing Law.

**Fair-rental provisions, key points.** Section 25ד (gap-filling), 25ז (delivery), 25יא (sale), 25יב (options) and 25יג (cancellation) are covered in Steps 5-6; full statutory text and the closed lists are in `references/statutory-provisions.md`. Cite section numbers from there rather than paraphrasing.

- **Fit for habitation (25ו + First Schedule).** Unfitness is defined ONLY by a closed six-item list: no drainage/sewage; no electricity or lighting; no ventilation and natural-light openings with doors and windows to close them, including a lockable main entrance door; no drinking water; NO PARTITION BETWEEN THE TOILET AND THE APARTMENT; unreasonable risk to safety or health. Delivering an unfit apartment is a BREACH (25ו(ב)). 25ו is the only provision that cannot be varied at all (25יד(1)). Do not substitute a plausible list of amenities: a water heater is not in the Schedule, the toilet partition is.
- **Suitable for living (25ה)** is a separate, weaker duty with אי-התאמה remedies. Do not conflate it with 25ו.
- **Repairs (25ח).** The landlord fixes any non-minor defect not caused by the tenant's unreasonable use within 30 days of the request, or 3 days if the defect makes reasonable habitation impossible. Miss that and 25ח(ג) applies s.9(א): reimbursement of reasonable expenses, or a PROPORTIONAL rent reduction reflecting lost value. Neither is deducting the invoice from the rent. The tenant is liable only for defects from UNREASONABLE use (25ח(א)), which is not the same test as "normal wear and tear".
- **Guarantee ceiling (25י(ב))** covers only guarantees costing the tenant money, capped at the lower of 3 months' rent or one-third of the lease value. The rest of 25י binds every guarantee: see Step 3.
- **Written form (25ב)** requires writing and signatures, and says expressly that non-compliance does NOT affect validity. An oral residential lease is a valid contract.
- **Contents (25ג + Second Schedule)** makes eight particulars mandatory, including item 7, the landlord's disclosure of known non-minor defects and known material nuisances.
- **Contracting out (25יד).** 25ו cannot be varied at all. Sections 6, 8-10, 15, 21(ב)-(ג), 23-25ה, 25ח(א)(1),(ב),(ג) and 25ט-25יג may be varied ONLY in the tenant's favour, so a clause moving a burden ONTO the tenant is void. 25ח(א)(2) is deliberately outside that list.

**Important:** the fair-rental provisions apply to residential rentals only. There is no statutory cap on rent amounts in Israel.

**Note on scope:** the 90/60 notice periods, the deposit cap, and the repair duties are all part of the 25א-25טו chapter and are subject to the section 25טו(א) exclusions below. A lease with a family member is NOT an exclusion: see the 25טו(ב) row.

**When the chapter does NOT apply (section 25טו(א) exclusions):**

| Exclusion | Details |
|-----------|---------|
| High rent | Monthly rent EXCEEDING 20,000 NIS. Section 25טו(4) updates this figure on 1 January each year by the change in the Consumer Price Index, rounded to the nearest 10 NIS, and the Minister publishes the updated amount in רשומות. Check the current-year figure rather than treating 20,000 as fixed |
| Long lease | A lease longer than 10 years AND under which the landlord has no right to cancel earlier. Both limbs are required |
| Very short lease | A lease of 3 months or less where the parties have no option to extend it |
| Hotels / vacation | Hotel rooms and any apartment let for vacation use |
| Assisted living | Sheltered / assisted-living housing (diyur mugan) |
| Dormitories | Student, pupil, or worker dormitories |
| Protected tenancy | Units under the Tenant Protection Law |
| Family lease is NOT an exclusion (25טו(ב)) | A lease with a `קרוב` stays fully inside the chapter. 25טו(ב) disapplies ONE provision, 25יד(2), so relatives MAY agree otherwise. Absent such agreement every protection applies |
| Sub-letting (25טו(ג)) | Where a head tenant on a lease of 10 years or less sublets, the 25ח(ב),(ג) repair duties and the 25ט(ב) prohibitions rest on the HEAD LANDLORD, not the head tenant |

Do NOT over-apply the deposit cap or the repair duties to a lease that is genuinely excluded. Do NOT under-apply them to a family lease, which is the commoner error.

**Payments the tenant bears (25ט).** 25ט(א) is a closed list: rent; occupier taxes including arnona; consumption of water, electricity, gas and heating; ONGOING house-committee maintenance; and classes prescribed by the Minister. 25ט(ב) bars charging the tenant anything else and names three in particular: buying or upgrading fixed systems or installations serving the apartment (a replacement boiler, air-conditioner or solar system is the landlord's, unless the tenant asked for the adaptation); BUILDING insurance premiums, ביטוח מבנה, as distinct from the tenant's own contents cover; and the landlord's debts to third parties, including a broker's fee where the broker acted for the landlord. A capital-renovation levy is not "ongoing maintenance", so it is not the tenant's. Because 25ט may be varied only in the tenant's favour, a clause shifting any of these onto the tenant is void.

### Step 2: Essential Contract Elements
The lease's required contents are not a matter of good practice: section 25ג makes the eight Second Schedule particulars mandatory (listed in Step 1 and set out in full in `references/statutory-provisions.md`). Verify each is present and specific:

| Element | Hebrew | What to Verify |
|---------|--------|---------------|
| Parties | משכיר / שוכר | Full names, Teudat Zehut numbers, addresses and contact details for both |
| Property | כתובת ותיאור הנכס | Exact address, apartment number and floor; rooms, fixtures, furniture, parking, storage, and any shared-property parts let with it |
| Term and options | תקופת השכירות ואופציה | Start and end dates; whether an option to extend exists and on what terms; any right to cancel and its conditions |
| Rent | דמי שכירות | Amount, payment date, method, and any index-linkage clause (check for a floor clause) |
| Additional payments | תשלומים נוספים | Any non-rent payment the tenant bears and its amount. Cross-check against 25ט(ב), which bars some outright |
| Guarantee | ערובה | Type, amount, realisation conditions and return timeline, consistent with 25י |
| Known defects | פגמים ידועים | Second Schedule item 7. Its ABSENCE is the point: a lease silent on defects is a lease the landlord has declared clean |

**Standard lease term patterns:** 12 months fixed is the most common; 12 + 12 with an option is very common; 3-6 months for sublets and temporary housing; 2-5 years is less common. Note that a lease of 3 months or less with no extension option, and one over 10 years where the landlord cannot cancel earlier, both fall outside the chapter entirely.

### Step 3: Deposits and Guarantees
A guarantee (ערובה) is the most critical financial element of a lease. Full text of section 25י and of the Guarantee Law is in `references/statutory-provisions.md`.

| Guarantee Type | Hebrew | Description | Risk Level for Tenant |
|---------------|--------|-------------|----------------------|
| Bank Guarantee | ערבות בנקאית | Bank issues a guarantee letter, funds frozen in your account | Low (controlled release) |
| Post-Dated Cheques | המחאות דחויות | Blank or post-dated cheques held by the landlord | Medium (can be cashed) |
| Cash Deposit | פיקדון מזומן | Cash or transfer held by the landlord | Medium (risk of non-return) |
| Promissory Note | שטר חוב | Note for a set amount, enforceable through the Execution Office without a full hearing | High |
| Personal Guarantors | ערבים | Third parties guarantee the tenant's obligations | Varies (personal liability) |

**The 25י(ב) ceiling is scoped; the rest of 25י is not.** This distinction decides most real questions:

| Rule | Details |
|------|---------|
| What the ceiling covers (25י(ב)) | Guarantees "involving a monetary outlay by the tenant" (הכרוכה בהוצאה כספית לשוכר), expressly cash and a bank guarantee. Their COMBINED total may not exceed the LOWER of 3 months' rent or one-third of the lease value. A 12-month lease caps at 3 months; a 6-month lease caps at 2 |
| Lease WITH an option | 25י(ב)(1) measures against "one third of תקופת השכירות", and 25יב uses a separate term for an extension (תקופת ההארכה). The safer reading is the term currently contracted for, not the term plus an unexercised option, but this is not settled: say so rather than quoting one ceiling with confidence |
| What it does not cover | A promissory note, a security cheque and a guarantors' deed cost the tenant nothing up front, so they do not count toward that total. A security cheque is arguable rather than settled: say so instead of assuring a tenant it is uncapped |
| What still binds every guarantee | 25י(א) defines ערובה with NO outlay qualifier, so 25י(ג),(ד),(ה) apply to ALL of them, promissory notes and guarantors included |
| Realisation grounds (25י(ג)) | A CLOSED list, each capped: unpaid rent (plus contractual linkage and interest); defects the tenant was liable to repair under 25ח(א), up to repair cost; unpaid 25ט(א)(2)-(5) charges; failure to vacate at term end, per the contract. "Damage beyond normal wear" is NOT a ground; the ground is unreasonable use |
| Notice and cure (25י(ד)) | The landlord must give reasonable advance notice of an intention to realise AND allow a reasonable period to put things right. A landlord who simply cashes a cheque has skipped a statutory step |
| Return (25י(ה)) | Within 60 days of the apartment being returned, or when debts under (ג) are settled, whichever is later, INCLUDING the guarantee's fruits |
| From 30.9.2026 | ס"ח 3510 of 31.3.2026 adds a guarantee from a "נותן ערבות אחר" (licensed credit provider, deposit-and-credit services licensee, stablecoin payment-services licensee, or insurer) alongside the bank guarantee, inside the same ceiling |

**If the lease uses personal guarantors**, the Guarantee Law 5727-1967 applies and is more protective than most parties assume: an ערב יחיד guarantees only the sum STATED in the guarantee contract, and if no fixed sum is stated they are released from it entirely (s.21). A residential-lease guarantee is normally small enough that the guarantor is an ערב מוגן, and under s.27 no action may be brought against them until judgment has been given against the tenant AND the Execution Registrar has certified that all reasonable execution steps against the tenant were taken.

**What to insist on:**
- A signed receipt (kabala) for any deposit paid
- Dated photographs of the whole apartment at move-in and move-out
- Pre-existing damage documented in writing and annexed to the contract (nispach l'chozeh)
- Return conditions and timeline stated explicitly, consistent with 25י(ה)
- For a bank guarantee, terms that match the contract terms
- A fixed sum stated in any guarantors' deed, and legal advice before signing a promissory note

### Step 4: Rent Increases and Index Linking
Understanding how rent changes work in Israel:

| Mechanism | Hebrew | Description |
|-----------|--------|-------------|
| Index-linked rent (Hatzmada La'Madad) | הצמדה למדד | Rent adjusts based on Consumer Price Index (CPI) changes |
| Fixed increase clause | סעיף העלאה קבוע | Predetermined increase percentage at renewal |
| Market adjustment | התאמה לשוק | Renegotiation at lease renewal based on market rates |
| No increase (during lease term) | ללא העלאה בתקופת החוזה | Landlord cannot raise rent during active lease unless contract allows |

**Index-linking (Hatzmada) details:**

| Aspect | Details |
|--------|---------|
| What is indexed | Rent adjusts to reflect changes in the CPI (Madad HaMechirim LaTzarchan) |
| Published by | Central Bureau of Statistics (Lishkat HaStatistika HaMerkazit) |
| Frequency | Usually calculated annually or at lease renewal |
| Direction | Can go up or down (deflation reduces rent) |
| Typical clause | "Rent will be adjusted according to the change in the CPI from [base month] to [adjustment month]" |
| Base index | The CPI value at the contract start date |

**Key rules on rent increases:**

| Scenario | Rule |
|----------|------|
| During active lease | Landlord CANNOT increase rent unless the contract explicitly permits it |
| At lease renewal (with option) | If option clause specifies terms, those terms apply |
| Between lease terms (new contract) | No legal cap; landlord can set any market rate |
| With index-linking clause | Automatic adjustment per CPI; no separate negotiation needed |
| Without index-linking | Rent stays fixed for the lease term |

### Step 5: Tenant Rights and Landlord Obligations
The statutory allocation is in Step 1; this is the operational summary. Where a duty is statutory, cite the section rather than calling it standard practice.

| Party | Duty | Basis |
|---|---|---|
| Landlord | Deliver the apartment fit for habitation, on the agreed date, free of persons and objects | 25ו, 25ז. Delivering an unfit apartment is a breach, and 25ו cannot be contracted out of |
| Landlord | Supply maintenance and use instructions for the apartment and its installations, no later than handover | 25ז(ג) |
| Landlord | Repair any non-minor defect not caused by the tenant's unreasonable use: 30 days, or 3 days if urgent | 25ח(ב) |
| Landlord | Disclose known non-minor defects and known material nuisances, in the contract | 25ג + Second Schedule item 7 |
| Landlord | Notify the tenant in writing before handing the apartment to a buyer | 25יא |
| Landlord | Return the guarantee within 60 days, including its fruits | 25י(ה) |
| Landlord | Report rental income to Mas Hachnasa. Residential rent has an exemption threshold and reduced-rate routes; verify the current figures | Income Tax Ordinance; a landlord matter, verify current figures |
| Tenant | Pay the rent on time | 25ט(א)(1) |
| Tenant | Pay occupier taxes including arnona, and consumption of water, electricity, gas and heating | 25ט(א)(2)-(3). A clause moving MORE onto the tenant is void; one moving these OFF the tenant is valid |
| Tenant | Pay ongoing house-committee maintenance, but not a capital levy | 25ט(א)(4) |
| Tenant | Repair defects caused by their own unreasonable use | 25ח(א) |
| Tenant | Notify the landlord of defects needing repair, which starts the 30/3-day clock | 25ח(ב) |

On **entry and privacy**: there is no statutory notice period for landlord entry. Whatever the contract says governs, so a tenant should negotiate one in rather than assume 24 hours. On **subletting**, the contract governs whether it is permitted, but where it is, 25טו(ג) keeps the repair duties and the 25ט(ב) prohibitions on the head landlord.

### Step 6: Termination, Eviction, and Dispute Resolution

| Termination Type | Hebrew | Process |
|-----------------|--------|---------|
| Natural expiry | סיום תקופה | Lease ends on the end date. Watch the 25יב option deadlines: 90 days for a landlord's option, 60 for a tenant's |
| Mutual agreement | הסכמה הדדית | Both parties agree to end it early |
| Under a cancellation clause | תניה לביטול | Only if the clause is valid: 25יג(א) voids a landlord-only right unless the tenant has an equivalent one. Minimum notice 90 days landlord / 60 tenant |
| Breach | הפרת חוזה | Non-payment, damage from unreasonable use, illegal use, material breach |

**Eviction.** For an unprotected residential tenancy there is no "the landlord needs it for personal use" ground: that belongs to protected tenancies under the Tenant Protection Law and does not apply here. The landlord's route is a valid cancellation clause or breach. Proceedings run as a תביעה לפינוי מושכר under תקנות סדר הדין האזרחי, התשע"ט-2018, a fast-track possession claim, not through the small claims court.

**Self-help eviction is unlawful.** A landlord may not change the locks, remove the tenant's belongings, or cut off water or electricity, whatever the tenant has done and whatever the contract says (חוק המקרקעין ss.18-19). A tenant facing it should document it and get urgent advice; it is among the most damaging illegal acts in this area.

**Dispute resolution:**

| Method | Hebrew | Best For | Cost |
|--------|--------|----------|------|
| Direct negotiation | משא ומתן ישיר | Minor disputes | Free |
| Mediation | גישור | Moderate disputes, preserving the relationship | Low-moderate |
| Small Claims Court | תביעות קטנות | Money claims up to the current ceiling (NIS 39,900), e.g. a withheld guarantee. Not for possession | Filing fee about 1% of the claim |
| Magistrate Court | בית משפט שלום | Larger claims and possession claims (פינוי מושכר) | Court fees |

There is no rental tribunal for ordinary tenancies. Where a lease is EXCLUDED from the chapter by 25טו(א), the route for attacking an unfair clause is חוק החוזים האחידים, התשמ"ג-1982, not the fair-rental provisions.

### Step 7: Common Red Flags in Rental Contracts
The full red-flag table, with the Hebrew term and the statutory basis for each, is in `references/contract-checklist.md`. The five that are VOID or unenforceable rather than merely unfavourable, and so are worth raising first:

- A landlord-only right to cancel without breach (VOID under 25יג(א) unless the tenant has an equivalent right)
- A guarantee above the 25י(ב) ceiling (void as to the excess)
- A guarantors' deed with no fixed sum (releases an ערב יחיד entirely, s.21(ב) Guarantee Law)
- Charging the tenant for fixed installations or building insurance (void, 25ט(ב)(1)-(2))
- Charging the tenant the landlord's broker fee (void, 25ט(ב)(3))

**Before signing:** have the contract reviewed; photograph the apartment and annex a condition report; verify ownership via a Tabu extract; check the Arnona classification with the municipality; confirm the va'ad bayit fee is ongoing maintenance rather than a capital levy.

## Examples

### Example 1: Reviewing a Lease Before Signing
**Input:** "I got a rental contract, what should I check before signing?"
**Output:** Verify landlord identity and ownership (Tabu extract). Check the eight Second Schedule particulars are present and specific (Step 2), especially item 7, since a lease silent on defects is one where the landlord has declared the apartment clean. Then check for the clauses that are VOID rather than merely bad (Step 7): a landlord-only cancellation right, a guarantee above the 25י(ב) ceiling, a guarantors' deed with no fixed sum, charges for fixed installations or building insurance, the landlord's broker fee, and any clause making the tenant responsible for all repairs. Confirm the guarantee type and amount, the index-linkage clause and whether it has a floor, and the option deadlines. Photograph the apartment and annex a condition report.

### Example 2: Deposit Dispute at Lease End
**Input:** "My landlord won't return my deposit, claims there's damage I didn't cause."
**Output:** Under 25י(ה) the guarantee, including its fruits, is returned within 60 days of handing back the apartment or of settling debts under 25י(ג), whichever is later. Realisation is limited to the four closed 25י(ג) grounds, and "damage beyond normal wear" is not one of them: the ground is a defect the tenant was liable to repair under 25ח(א), meaning damage from UNREASONABLE use, capped at the repair cost. Before realising, 25י(ד) requires the landlord to give reasonable advance notice and a reasonable chance to put things right, so a landlord who simply cashed a cheque skipped a statutory step. Ask what ground is claimed, whether notice and a cure period were given, and compare against the move-in condition report. A money claim for the withheld sum goes to small claims.

### Example 3: Rent Increase During Lease
**Input:** "My landlord wants to raise my rent in the middle of the lease, can they do that?"
**Output:** Not unless the contract contains an express mechanism, normally a CPI-linkage clause. Absent one, the rent is fixed for the term. Where there is a linkage clause, apply it as written and check for a floor clause preventing the rent falling; `scripts/rent-index-calculator.py` computes the adjustment from the CBS index. At renewal, or between terms, the landlord may propose a new figure and the tenant may negotiate or decline to renew. If an option was exercised, the extension terms are those fixed in the contract in advance (25יב(ב)).

### Example 4: Early Termination by Tenant
**Input:** "I need to break my lease early, what are my options?"
**Output:** Start with the contract's cancellation clause. If it lets only the LANDLORD cancel without breach, 25יג(א) makes it void unless the tenant has an equivalent right, which sometimes means the tenant has more room than the document suggests. Where a valid clause exists, the tenant's statutory minimum notice is 60 days (25יג(ב)). Otherwise the usual routes are agreement with the landlord, often by presenting a replacement tenant, or accepting the contractual consequences of leaving early. A penalty clause may be enforceable but is negotiable, and the guarantee may only be realised on a 25י(ג) ground.

## Bundled Resources

### References
- `references/statutory-provisions.md` -- Section-by-section text of 25א-25טו, both Schedules, and the Guarantee Law rules on guarantors. Consult before citing any section number.
- `references/contract-checklist.md` -- Detailed checklist of every clause to verify in an Israeli rental contract, organized by section (parties, property, lease term, rent, deposits, maintenance, utilities, termination). Includes Hebrew terms, common pitfalls, and red flags. Consult when a user is reviewing or negotiating a rental contract.
- `references/fair-rental-law-summary.md` -- Summary of the 2017 fair-rental amendment to the Rental and Borrowing Law, 5731-1971 (sections 25א to 25טו, commonly called Chok Schirut Hogenet) including minimum habitation standards, landlord and tenant obligations, the deposit cap, repair deadlines, termination rules, and enforcement options. Consult when a user asks about tenant rights, landlord obligations, or what the fair-rental provisions cover.

### Scripts
- `scripts/rent-index-calculator.py` -- Calculates rent adjustment based on CPI index linking (hatzmada la'madad). Given original rent, start date, and current date, calculates the adjusted rent using historical CPI data. Run: `python scripts/rent-index-calculator.py --help`

## Gotchas

- The 2017 fair-rental rules are sections 25א-25טו of the Rental and Borrowing Law, not a standalone "Fair Rental Law". Agents cite a statute that does not exist.
- The deposit cap is NOT a flat 3 months. It is the LOWER of 3 months' rent or one-third of the lease value, so a short lease caps lower. And it reaches only guarantees that cost the tenant money: agents apply it to a promissory note or guarantors, where it does not bite, while missing that 25י(ג),(ד),(ה) DO bind those instruments.
- Agents say the tenant can "deduct the repair cost from the rent". Section 25ח(ג) applies s.9(א), which gives reimbursement of reasonable expenses or a PROPORTIONAL rent reduction reflecting lost value, rarely the invoice figure. Paying less rent on the strength of an invoice puts the tenant in arrears and hands the landlord a 25י(ג)(1) realisation ground and an eviction claim.
- Agents treat a family lease as excluded from the chapter. 25טו(ב) disapplies only 25יד(2), so relatives may contract out; absent that, every protection applies. The genuine 25טו(א) exclusions are listed in Step 1, and two of them carry qualifiers agents drop: the 10-year exclusion needs the landlord to have no earlier cancellation right, and the 3-month one needs no extension option.
- Agents invent a habitability standard from plausible amenities. It is the closed six-item First Schedule, which includes a partition between the toilet and the apartment and a lockable main entrance door, and does not include a water heater.
- Agents reduce 25ט to the broker fee. It also bars charging the tenant for buying or upgrading fixed installations, and for building insurance, the two commonest overcharges in the market.
- Index-linked rent tracks the CPI both ways, but Israeli leases routinely add a floor clause preventing the rent falling below the base. Check for one before telling a tenant deflation will help them.
- A shtar chov (promissory note, NOT shtar hon) is enforceable through the Execution Office without a full hearing, which is why it is riskier for a tenant than a bank guarantee. Where personal guarantors are used, the Guarantee Law matters: an unstated sum releases an ערב יחיד entirely, and a protected guarantor cannot be pursued before the tenant has been.
- The small claims limit (currently NIS 39,900) and the 25טו(4) rent threshold both move. Verify the current figures rather than quoting these.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Gov.il: Rental and Borrowing Law amendment | https://www.gov.il/he/pages/rent_law | Official page on the 2017 fair-rental amendment, sample contract |
| Rental and Borrowing Law, consolidated text | https://he.wikisource.org/wiki/%D7%97%D7%95%D7%A7_%D7%94%D7%A9%D7%9B%D7%99%D7%A8%D7%95%D7%AA_%D7%95%D7%94%D7%A9%D7%90%D7%99%D7%9C%D7%94 | Full current text of the law, including chapter 25א-25טו and the Second Schedule |
| Sefer HaChukkim 3510 (31.3.2026) | https://fs.knesset.gov.il/25/law/25_lsr_12846788.pdf | The 2026 amendment adding a "notenn aruvah acher" guarantee to section 25י, in force 30.9.2026 |
| Kol Zchut: Apartment renters | https://www.kolzchut.org.il/he/%D7%A9%D7%95%D7%9B%D7%A8%D7%99_%D7%93%D7%99%D7%A8%D7%95%D7%AA | Tenant rights, the deposit cap, repair of defects, eviction procedures |
| Ministry of Construction & Housing | https://www.gov.il/en/departments/ministry_of_construction_and_housing | Housing policy, rent-controlled units |
| CBS Rent Index | https://www.cbs.gov.il/en/Pages/default.aspx | Consumer price index used for rent indexation |

## Recommended MCP Servers

These Model Context Protocol servers, available in the skills-il directory, pair well with this skill:

- **israel-law**: programmatic access to Israeli primary legislation. Use it to pull the current text of the Rental and Borrowing Law, 5731-1971, including the 2017 fair-rental amendment (sections 25א to 25טו), when you need to confirm an exact provision such as the deposit cap or the repair deadlines.
- **kolzchut**: access to Kol Zchut, Israel's plain-language rights portal. Use it to retrieve up-to-date practical guidance on tenant and landlord rights, deposit limits, defect repairs, and dispute procedures.

Always confirm load-bearing numbers (deposit cap, repair deadlines, small claims jurisdiction limit) against the primary source, since amounts and thresholds change.

## Troubleshooting

### Error: "Landlord refuses to provide a written contract"
Cause: informal arrangements, often to avoid reporting the rental income.
Solution: 25ב requires the lease to be in writing and signed, but expressly provides that non-compliance does NOT affect the contract's validity. So do not tell a tenant in an oral lease that they have no contract: they have one, and the chapter's protections still apply. The practical problem is proof. Document everything in writing (messages, transfers, a dated condition report), request a written contract, and note that where 25ב is not complied with, 25ד reads in the Minister's model lease if one is prescribed.

### Error: "Landlord enters the apartment without notice"
Cause: the belief that ownership carries unlimited access.
Solution: there is NO statutory notice period for landlord entry, so the honest answer is that the contract governs and a tenant who wants 24 hours' notice must negotiate it in. That said, the landlord cannot interfere with the tenant's use of the apartment, and repeated entry against the tenant's wishes may be trespass (הסגת גבול) and a breach of contract. Write to the landlord setting out the expectation, keep a log, and escalate on the contract terms.

### Error: "Contract requires a shtar chov (promissory note) as guarantee"
Cause: a promissory note can be submitted to the Execution Office and enforced without a full hearing, so landlords prefer it. (The instrument is a shtar CHOV; "shtar hon" is a different thing.)
Solution: it is the highest-risk instrument for a tenant, and the 25י(ב) ceiling does not limit its amount. But 25י(ג) and (ד) still do apply: it may be realised only on the four closed grounds, and only after reasonable notice and a chance to cure. Negotiate for a bank guarantee, cap the note's amount in the contract, and state expressly when it may be used. Take legal advice before signing. If guarantors are asked for instead, ensure the deed states a fixed sum, since an unstated sum releases an ערב יחיד entirely under s.21(ב) of the Guarantee Law.
