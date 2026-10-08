# Domain checklist: israeli-consumer-claim-kit

Research date: 2026-10-07. Primary text: the consolidated Consumer Protection Law 1981 on Hebrew Wikisource (bot-maintained from the Knesset National Legislation Database, last revision 2026-09-30 "כניסה לתוקף"), the two sets of regulations on Wikisource, and the Knesset Reshumot PDF for the 2024 aggravated-violator law. Kol Zchut, gov.il and consumers.org.il were read through a real browser (they return 403 to curl because of Cloudflare, but load with HTTP 200 in a browser). Every number below has a verbatim snippet in `evidence.json` unless marked UNVERIFIED.

Abbreviations: CPL = חוק הגנת הצרכן, התשמ"א-1981. Cancellation Regs = תקנות הגנת הצרכן (ביטול עסקה), התשע"א-2010. Warranty Regs = תקנות הגנת הצרכן (אחריות ושירות לאחר מכירה), התשס"ו-2006.

## Must cover (core)

### A. Technician / delivery lateness ("חוק הטכנאים", CPL s.18א(ג) to (ו))
- [ ] Who is covered | a "service provider" obliged to serve: (a) warranty obligations incl. extended warranty, (b) a service contract conditional on goods at the consumer (cable/satellite converter, router), (c) installation or removal of goods sold, rented or lent, (d) periodic home gas-installation inspections, (e) delivery of goods the dealer sold, (f) paid continuing repair contracts | source: https://he.wikisource.org/wiki/חוק_הגנת_הצרכן (s.18א(ג)(1)) | why core: decides whether the letter can cite the statute at all.
- [ ] Coordinated visit, 2-hour window | the provider must coordinate date and hour; waiting may not exceed 2 hours past the coordinated time; a "wait for a phone call" alternative is allowed only if the consumer was told they may refuse it, and waiting at home still may not exceed 2 hours | source: s.18א(ג)(1)-(2) | why core: the factual trigger.
- [ ] Visiting hours | for categories (a) to (d) only: 8:00 to 19:00 weekdays, 8:00 to 13:00 Fridays and holiday eves (exemption regs 2017 for outdoor electrical/gas/height work in darkness); deliveries and paid repair contracts are not bound to these hours | source: s.18א(ג)(1א) | why core: a visit scheduled outside hours is itself a breach.
- [ ] Postponement | provider may postpone by notice no later than 20:00 the evening before, provided the service is not pushed past the legal repair deadline | source: s.18א(ג)(3) | why core: a valid postponement (with a new agreed date and hour) moves the count to the NEW time but does not defeat the claim; a notice after 20:00, or one that pushes the service past its legal deadline, leaves the original time standing.
- [ ] Amounts | NIS 300 when 2 hours have passed BEYOND the 2-hour waiting window (i.e. 4 hours after the coordinated time); NIS 600 when 3 hours have passed beyond the window (5 hours after); NIS 300 for breaching the phone-call alternative rules | source: s.18א(ד) | why core: the headline number, widely misstated (see Known bad figures).
- [ ] No proof of damage, consumer need not prove loss | "לפיצוי בלא הוכחת נזק" | source: s.18א(ד) | why core: letter wording.
- [ ] Compensation in kind | only if the provider told the consumer they may choose cash and the consumer agreed; burden of proof on the provider | source: s.18א(ה) | why core: rebuts "we gave you a voucher".
- [ ] Exception | no statutory compensation if the delay arose from circumstances the provider did not know of and should not have known of when the time was set, or could not have foreseen, AND could not prevent | source: s.18א(ו) | why core: the standard defence; letter should pre-empt it.
- [ ] How it is paid | the statute grants an entitlement but sets no payment mechanism or deadline and no duty to request first; in practice: written demand, then small claims | source: s.18א(ד); Kol Zchut https://www.kolzchut.org.il/he/פיצוי_בגין_איחור_טכנאי_או_איש_שירות | why core: sets user expectations. Note: 18א is NOT in the s.31א list, so the s.31א(ב) written-request precondition does not formally apply, but a written demand is still the recommended first step.
- [ ] Temporal | amounts are fixed shekel figures in the section; no index-linkage or update clause appears in s.18א (confidence: medium, based on reading the section text; s.13ד1 by contrast has an explicit CPI clause). Section amended תש"ס, תשס"ח, תשע"א, תשע"ד, תשע"ח; the exact commencement of the current 300/600 wording was not extracted.

### B. Cancellation of transactions
- [ ] Distance sale (מכר מרחוק), goods | cancel from the transaction until 14 days from receipt of goods or of the written disclosure document, whichever later | source: CPL s.14ג(ג)(1) | why core: most common claim.
- [ ] Distance sale, services | 14 days from transaction or disclosure document, whichever later; continuing service: even after it started; one-off service: at least 2 non-rest days before the service | source: s.14ג(ג)(2) | why core.
- [ ] Distance-sale exclusions | perishable goods; lodging/travel/vacation/leisure if cancelling within 7 non-rest days before the service; computer "information"; goods made specially for the consumer; recordable/copyable goods whose original packaging was opened | source: s.14ג(ד) | why core: the letter must not demand what the law excludes.
- [ ] Door-to-door (עסקה ברוכלות) | goods: until 14 days from delivery or receipt of required details, whichever later; services similar; installation charge cap NIS 100 | source: s.14 | why core.
- [ ] Extended right for vulnerable groups | person with a disability (per Equal Rights for Persons with Disabilities Law 1998), senior = aged 65, new immigrant = less than 5 years since oleh/eligibility certificate | source: s.14ג1(א) | why core.
- [ ] 4 months, peddling | from transaction, delivery or receipt of details, whichever later | source: s.14ג1(ב) | why core.
- [ ] 4 months, distance sale ONLY if there was a conversation | the transaction must have included a conversation between dealer and consumer, incl. electronic (chat counts per Kol Zchut); a pure click-through web purchase gets only the regular 14 days | source: s.14ג1(ג) | why core: most misreported condition.
- [ ] Proof of status | dealer may ask for one certificate (senior certificate, oleh certificate, disability certificate over 6 months, or Fifth Schedule item) and may not ask for more | source: s.14ג1(ד) | why core: letter should attach it.
- [ ] No in-store extension for these groups | s.14ג1 covers peddling and distance sales only; no 4-month in-store right found in the Cancellation Regs | source: s.14ג1, Cancellation Regs | why core: prevents over-claiming.
- [ ] Refund and fee after distance/timeshare cancellation | no-reason cancellation: refund within 14 days of notice, fee capped at 5% or NIS 100, whichever LOWER; cancellation for defect, non-conformity, late/non-delivery or other breach: refund within 14 days and NO cancellation fee; consumer returns goods where delivered (breach case) or to the dealer's place of business (no-reason case) | source: s.14ה(א)-(ב) | why core.
- [ ] Installation fee | up to NIS 100 where goods were installed for a service | source: s.14ה(ב2) | why core.
- [ ] Ways to cancel | oral (phone or in person), registered mail, email, fax if the dealer has one, internet (dedicated link on the home page); notice states name and ID number | source: s.14ט | why core: the letter itself is a cancellation notice.
- [ ] Continuing transaction (s.13ד) | ends within 3 business days of a cancellation notice, 6 business days if by registered mail, unless the consumer named a later date; no charges after that | source: s.13ד(ג) | why core.
- [ ] In-store cancellation (Cancellation Regs) | applies to goods priced above NIS 50; 14 days from receipt for furniture, home and garden equipment, electrical/electronic devices incl. terminal equipment, unopened goods, ordered-not-supplied goods, water purifiers, watches (opening packaging is not use for most; connecting to power/gas/water is use); clothing and footwear and jewelry up to NIS 3,000: until 2 non-rest days after purchase (clothing: price tag not removed); certain services 14 days (see regs schedule items 8 to 20); new car from importer 14 days if not yet registered | source: https://he.wikisource.org/wiki/תקנות_הגנת_הצרכן_%28ביטול_עסקה%29 regs 1-2 and schedule | why core.
- [ ] In-store refund mechanics | refund at cancellation or ASAP, no later than 7 business days, same payment method; credit card: dealer cancels the charge or notifies the card company, which credits immediately (continuing deals: at the next billing date) | source: Cancellation Regs reg.4 | why core.
- [ ] In-store fee | 5% or NIS 100, whichever lower, plus clearing fee if the dealer proves it was charged | source: Cancellation Regs reg.5 | why core.
- [ ] In-store exclusions | furniture assembled in the consumer's home, made-to-measure goods, food, medicines and supplements, perishables, information, opened copyable goods, underwear and swimwear, gas, jewelry above NIS 3,000 (except watches), travel services fully abroad (if disclosed), gift cards/vouchers as payment, delivery requested more than 6 months later | source: Cancellation Regs reg.6 | why core.
- [ ] Return-policy notice (s.4ג) | a shop must post its non-defect return policy; if it posts none, the presumption is that returns are allowed; if it breaches its own posted policy, the consumer may return within 7 days of refusal for full refund in the original payment method | source: CPL s.4ג | why core: often the strongest in-store lever.

### C. Warranty and repair (Warranty Regs 2006)
- [ ] Scope | new electrical, electronic and gas products incl. mechanisms in furniture, priced above NIS 150 | source: https://he.wikisource.org/wiki/תקנות_הגנת_הצרכן_%28אחריות_ושירות_לאחר_מכירה%29 reg.1 | why core.
- [ ] Minimum warranty | 1 year from delivery (or from end of mandatory installation) | reg.1, reg.5 | why core.
- [ ] Free repair by manufacturer/importer | any fault in the warranty period, free, incl. part replacement; written repair report | reg.2, reg.18 (importer = manufacturer) | why core.
- [ ] Repair deadlines | 1 week from the call, or 10 days from delivery to a service station, or 2 weeks if left at the point of sale; specific items in the Second Schedule have shorter deadlines when the fault prevents main use; Sabbaths and holidays excluded; a dealer liable under reg.19 has 3 weeks | reg.10 | why core.
- [ ] Failed repair | if the repair does not restore the goods with original new parts, the manufacturer must supply new equivalent goods or refund, AT THE MANUFACTURER'S CHOICE | reg.6(ג) | why core: there is no consumer-elected "3 failures = replacement" rule in these regs.
- [ ] Technician lateness under warranty | max 2 hours wait; technician late more than twice in a row within the repair period = manufacturer in breach | reg.11 | why core.
- [ ] Spare parts | through the warranty period; goods above NIS 300: one more year; listed major appliances: 7 years | reg.3 | why core.
- [ ] Dealer liability when manufacturer cannot be located | goods above NIS 400 | reg.19 | why core.
- [ ] Charges allowed only if proven before repair | force majeure after delivery, consumer malice/negligence, unauthorised repair | reg.8 | why core: rebuts "you broke it".
- [ ] Warranty certificate in Hebrew (Arabic on request), dealer must hand it over; no waiver of rights; transfer to a new owner | regs 12-14, 17, 21 | why core.

### D. Exemplary damages (CPL s.31א)
- [ ] Amount | up to NIS 10,000 per breach without proof of damage; up to NIS 50,000 for a repeat, continuing or aggravated breach | source: s.31א(א), (ג) | why core.
- [ ] Only listed breaches qualify | incl. return-policy breaches (4ג), delivery-place deception, fixed-term charging after end, continuing charging after a 13ד cancellation notice, overcharge refund (13ד1), peddling refund, distance-sale/timeshare refund or charge cancellation (14ה), medical continuing-deal refund, foreign-travel cancellation-policy refund, shelf price vs till price (17ב(ד)), foreign-currency price, warranty certificate/sticker, warranty repair and spare parts | source: s.31א(א) | why core: technician lateness (18א(ג)-(ד)) is NOT on the list; it has its own fixed 300/600.
- [ ] Precondition | no exemplary-damages suit before the consumer sent a written request (email counts); for continuing-deal cancellation a non-oral s.14ט cancellation notice suffices; for distance-sale cancellation the cancellation itself suffices | source: s.31א(ב) | why core: the demand letter IS this precondition, so it must be in writing and kept.
- [ ] Who may claim | a consumer in a transaction with a dealer (s.31א(א)); court considers deterrence, consumer encouragement, severity, transaction value, dealer size, criminal fine; not the damage amount | s.31א(ה) | why core.
- [ ] Temporal | no index-linkage clause in s.31א (medium); the 10,000 figure is a fixed amount in the current text.

### E. Complaint channels and court
- [ ] Consumer Protection and Fair Trade Authority | online public-inquiries form, ; information is used for investigation, supervision and enforcement; it is an enforcement body and does not obtain individual compensation (Kol Zchut describes it as an independent enforcement arm) | source: https://www.gov.il/he/service/filing_a_complaint_to_fair_trade_authority | why core: set expectations.
- [ ] Israel Consumer Council (statutory consumer organisation) | complaint lobby with online, accessible and Word forms; handles a complaint only after the consumer approached the business in writing | source: https://www.consumers.org.il/category/complaint-form ; https://www.kolzchut.org.il/he/פנייה_למועצה_הישראלית_לצרכנות | why core: a second reason to send a written demand first.
- [ ] Small claims | ceiling NIS 30,000 base indexed, NIS 39,900 in 2026 (Courts Law s.60(1) annotation; Kol Zchut: "נכון לינואר 2026"); individuals only (not companies); no lawyer as a rule | source: https://he.wikisource.org/wiki/חוק_בתי_המשפט ; https://www.kolzchut.org.il/he/הגשת_תביעה_קטנה | why core: escalation path in every letter.
- [ ] Pre-suit demand letter | no general legal requirement for a demand letter before a small-claims suit (no such rule found); BUT (1) s.31א(ב) requires a prior written request for exemplary damages, (2) the Consumer Council requires a prior written approach, (3) cancellations must be notified via a s.14ט channel | why core: frames the letter as both evidence and statutory precondition.

## Should cover (advanced / edge cases)
- [ ] Aggravated-violator mechanism (Chapter ה'2, ss.22כז to 22לח, plus Payment Services Law s.18א and Execution Law s.78ב) | the Commissioner may declare a dealer an "aggravated violator" for a repeated pattern of deception, unfair influence, or refund breaches that targets persons with special characteristics (disability, senior, oleh, minor, helpless person, someone not knowing the transaction language), involves threats, or causes especially significant harm to many consumers; notices go to regulated payment-service providers (stop payments, return funds to payers, restrict contracting) and to the Execution Office (no new files, freeze/close existing ones) | source: https://he.wikisource.org/wiki/חוק_הגנת_הצרכן ; https://www.israelhayom.co.il/news/welfare/article/16238303 | why: lets the letter tell a vulnerable user to also file with the Authority. An individual consumer cannot trigger it directly; the only route is a complaint to the Authority.
- [ ] Return-in-kind credit notes | credit note valid at least 2 years; change in cash if remainder is up to 5% or NIS 100 | source: Kol Zchut in-store page | why: frequent shop response. (Not separately evidenced; regulation text not fetched.)
- [ ] Foreign-travel services sold at a distance (s.14ג2) | dealer may offer the foreign provider's cancellation policy instead of the statutory right, with prior disclosure; burden of proof on dealer | source: s.14ג2 | why.
- [ ] Continuing medical-services deals (ss.13ה to 13ז) | 30-day cancellation without fee per Kol Zchut | why: elder-care users.
- [ ] Overcharge in continuing deals (s.13ד1) | refund within 4 business days plus interest plus a fixed costs payment | source: s.13ד1 | why. (Not in evidence.json.)
- [ ] Telecom-specific lateness rules | the CPL rule already covers telecom where service depends on equipment at the consumer (s.18א(ג)(1)(ב)). A separate Communications Law technician regime was NOT researched or verified; treat as UNVERIFIED.
- [ ] Insurance-company home services | Kol Zchut says the technician law does not apply to services on behalf of insurers; not located in statute text (medium).
- [ ] Credit-card transaction cancellation mechanics | Cancellation Regs reg.4 (card company credits the consumer when it can recover from the dealer); timeshare deals have a 30-day issuer hold (CPL s.14ב). A general chargeback right under the Debit Cards Law was NOT researched.
- [ ] Administrative fines | per Kol Zchut, refusing an in-store cancellation exposes the dealer to NIS 25,350 (corporation) / 8,065 (individual) as of 2025; the s.22ג schedule amounts are CPI-updated every 1 January (s.22ט(ב)), so treat the figure as year-specific.

## Follow-up for the next update (raised by the 2026-10-07 expert review, not yet evidenced)
- Ministry of Communications public-complaints unit as an escalation route for telecom licensees (no primary reference recorded yet).
- Sale Law route for defects in goods outside the Warranty Regulations.
- Limitation periods.
- Warranty extras: furniture mechanisms, extended-warranty withdrawal, parallel importers, warranty certificate duties.
- Minors and the Legal Capacity Law.

## Out of scope (explicit, with rationale)
- Drafting court pleadings, filing on the user's behalf, or predicting outcomes | the skill drafts letters/complaints the user signs; litigation strategy is legal advice reserved to advocates (Chamber of Advocates Law), and must be framed as information only.
- Class actions (תובענות ייצוגיות) | different procedure, requires counsel.
- B2B and consumer-to-consumer deals | the CPL protects consumers against dealers only; the Authority has no remit (Kol Zchut).
- Purchases from foreign websites | Kol Zchut: Israeli cancellation rules apply to Israeli sites; foreign sites' terms govern.
- Flight delay/cancellation compensation (Aviation Services Law), banking/insurance/pension disputes (regulator-specific ombudsmen), rental disputes, real estate purchases | separate statutes and forums; route to existing skills.
- Statutory interest and costs computation | court-determined.

## Authoritative sources
- Consumer Protection Law, consolidated: https://he.wikisource.org/wiki/חוק_הגנת_הצרכן (Wikisource mirror of the Knesset database, revision 2026-09-30).
- Cancellation Regs 2010: https://he.wikisource.org/wiki/תקנות_הגנת_הצרכן_%28ביטול_עסקה%29
- Warranty Regs 2006: https://he.wikisource.org/wiki/תקנות_הגנת_הצרכן_%28אחריות_ושירות_לאחר_מכירה%29
- Courts Law s.60 (small claims): https://he.wikisource.org/wiki/חוק_בתי_המשפט
- Aggravated-violator law, Reshumot Sefer HaChukim 3235, 4 July 2024, p.1016 (Knesset Reshumot PDF) (s.4: commencement 3 months after publication; minister may postpone by order for up to 9 months in total).
- Authority complaint service: https://www.gov.il/he/service/filing_a_complaint_to_fair_trade_authority
- Consumer Council complaint lobby: https://www.consumers.org.il/category/complaint-form
- Kol Zchut aggregator pages used for taxonomy: פיצוי_בגין_איחור_טכנאי_או_איש_שירות, ביטול_עסקה_שנעשתה_באינטרנט_או_בטלפון, ביטול_רכישה_שנעשתה_בבית_העסק_והחזרת_המוצר, ביטול_עסקה_מתמשכת, ביטול_עסקה_ברוכלות, עסקה_צרכנית_שלא_ניתן_לבטל, דמי_ביטול, הגשת_תביעה_קטנה, פנייה_למועצה_הישראלית_לצרכנות, הרשות_להגנת_הצרכן_ולסחר_הוגן (all on Kol Zchut). Note: Kol Zchut has no page titled "ביטול_עסקה" (404).

## Known bad figures
1. "Technician more than 2 hours late = NIS 300." Wrong. The 2 hours is the permitted waiting window. NIS 300 applies only after 2 MORE hours beyond that window (4h after the coordinated time) and NIS 600 after 3 more hours (5h). s.18א(ד)(1).
2. "Technician-law compensation is part of the 10,000 exemplary damages." Wrong. s.18א(ד) sets fixed 300/600; 18א(ג) is not on the s.31א list.
3. "Seniors/olim/disabled get 4 months to cancel any purchase." Wrong. 4 months applies to peddling sales and to distance sales that included a conversation (incl. electronic); a pure online checkout gets 14 days; no in-store extension.
4. "Cancellation fee is 5% or NIS 100, whichever is HIGHER." Wrong. It is the LOWER. And no fee at all when cancelling for defect, non-conformity, late delivery or other dealer breach (distance sales, s.14ה(א)).
5. "Senior = 60/67" or "oleh = 10 years / 3 years". Statute: senior = 65; oleh = under 5 years from certificate.
6. "The law letting the Authority order card companies to stop clearing took effect 2026-10-04." Wrong year. The Law on Protecting Consumers from Dealers Committing Violations in Aggravated Circumstances (Legislative Amendments) 5784-2024 was published 4 July 2024 with commencement 3 months later; Israel Hayom (2024-08-11) reports 4 October, i.e. 4 October 2024. It is not named "law for the prevention of economic harm to the consumer" in the statute book; that was the private-bill title (Walla, March 2024). No postponement order was found in the Wikisource amendment list (medium confidence). Individual consumers cannot invoke it directly.
7. "Warranty: after 3 failed repairs you are entitled to a new product." Not in the Warranty Regs; reg.6(ג) gives new goods OR refund at the manufacturer's choice when a repair fails to restore the goods.
8. Older small-claims ceilings from previous years. Current: NIS 39,900 for 2026 (base 30,000, Aug 2008 index).
9. "The Consumer Protection Authority will get you your money back." It is an enforcement body; individual monetary recovery is via the dealer, the Consumer Council's mediation, or small claims.
10. "A demand letter is legally required before any small claim." No general rule found. It is required (in writing) only as a precondition to exemplary damages (s.31א(ב)) and by the Consumer Council's intake policy.

## Could not verify
- Exact commencement date of the current wording of s.18א(ג)-(ד) and whether earlier wording governs older events (not extracted).
- Any separate telecom technician regime under the Communications Law.
- Whether any order postponed the aggravated-violator law's commencement (none listed; medium).
- Kol Zchut's statement that insurer home services are excluded from the technician law (no statutory text located).
- Note on `evidence.json`: several raw_snippets are verbatim statute text and therefore contain the statute's own en dash character; they were not edited to keep them verbatim.
