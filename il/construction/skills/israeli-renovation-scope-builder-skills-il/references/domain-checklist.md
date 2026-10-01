# Domain Coverage Checklist, israeli-renovation-scope-builder

Generated: 2026-08-10, revised 2026-08-11 after the pre-push expert review. Research on he.wikisource.org for every statutory row (חוק חוזה קבלנות; חוק התכנון והבניה; תקנות הפטור מהיתר; תקנות למניעת מפגעים; תקנות רישום קבלנים היקף כספי וסיווג; תקנות החשמל רשיונות; חוק החשמל; חוק המקרקעין; חוק ההתיישנות; תקנות ביטול עסקה; חוק מוסר תשלומים; חוק לצמצום השימוש במזומן; חוק בתי המשפט; חוק מס ערך מוסף; חוק הגז; תקנות הבטיחות בעבודה), the Nevo consolidated text plus a browser read for the current contractor thresholds, and the official רשומות PDF for the 2025 notice.

Every statutory row was verified against the source's own text layer. Aggregator pages were used for taxonomy discovery only and are NOT cited for any rule: kolzchut proved unreachable to both curl and a headless browser, which is precisely why no rule in this skill rests on it.

Every statutory row below was verified against the raw text layer of the source, not against a WebFetch summary and not against a renovation guide. Several widely repeated guide figures are wrong (see "Known bad figures").

## The framing that must survive into the skill

A homeowner renovation is a **חוזה קבלנות** under חוק חוזה קבלנות התשל"ד-1974. That statute is **dispositive**: it supplies default rules only where the contract is silent. It is NOT חוק המכר (דירות) and it carries **no בדק/אחריות schedule at all**. Importing the developer בדק periods (2/3/4/5/7 years) into a renovation is a wrong-law answer and is the single most likely failure mode of this skill, because those periods dominate Israeli search results for home defects.

## Must cover (core)

### Legal basis and the shape of the instrument

- [ ] Legal basis is חוק חוזה קבלנות התשל"ד-1974, not חוק המכר (דירות). A renovation is a contract "לעשיית מלאכה או למתן שירות בשכר" where the contractor is not the customer's employee (סעיף 1), source: https://he.wikisource.org/wiki/חוק_חוזה_קבלנות, why core: prevents the wrong-law answer described above.
- [ ] The statute is dispositive, so the contract governs. סעיף 8 applies the law only where no other legislation applies and where no contrary intention appears from the agreement, source: same, why core: this is precisely why a written scope plus terms is the operative instrument. Silence is what triggers the weak defaults.
- [ ] There is NO statutory warranty schedule for renovation work. Every בדק or אחריות period in the document is a number the parties choose, source: same (absence is the finding), why core: the skill must say this plainly rather than supply invented periods with a false statutory air.

### Defects: notice, cure, remedies

- [ ] פגם, notice and cure (סעיף 3). The statute's own term is **פגם**, NOT אי-התאמה (which belongs to חוק המכר); using the wrong term signals the wrong statute. Where the work is not as agreed, the customer must notify within a **reasonable time** after discovering (or after he should have discovered) the defect, and must give the contractor a **reasonable opportunity to cure**. Failure forfeits reliance on the defect unless the contractor knew of it, source: https://he.wikisource.org/wiki/חוק_חוזה_קבלנות, why core: there is no fixed statutory day count, so the contract must convert "זמן סביר" into a concrete number. Homeowners routinely lose claims by hiring a replacement before offering the cure opportunity.
- [ ] Remedies if the contractor does not cure (סעיף 4). The customer may fix it himself and recover reasonable costs, or deduct from the price the reduction in value, source: same, why core: this is the legal force behind a retention and deduction clause.
- [ ] Contractor's lien, זכות עכבון (סעיף 5). The contractor has a lien over the customer's property delivered to him for sums owed, source: same, why core: matters when a tradesperson holds appliances or materials. The contract should address it explicitly, and it is one of the few provisions that protects the tradesperson.
- [ ] Acceptance and passage of risk (סעיף 6). The customer must accept the work at the agreed time or within a reasonable time. Until acceptance the contractor carries responsibility as a שומר שכר, source: same, why core: defines when the handover checklist and the warranty clock start and who carries the works in the meantime.
- [ ] Other contract remedies are preserved (סעיף 7). Nothing derogates from חוק החוזים (תרופות), so delay damages, cancellation, and פיצוי מוסכם live there, source: same, why core: the delay-compensation clause is grounded here, not in חוזה קבלנות.

### Payment

- [ ] חוק מוסר תשלומים לספקים התשע"ז-2017 does NOT apply where the payer is a private individual. It binds state bodies, local authorities, budgeted bodies, and an "עסק" (מוסד כספי, עוסק מורשה, עוסק פטור), source: https://he.wikisource.org/wiki/חוק_מוסר_תשלומים_לספקים, why core: a very common wrong answer tells a שיפוצניק he is entitled to שוטף פלוס 45 from a homeowner. He is not. Only the contract creates his payment date.
- [ ] The same law DOES apply when the commissioning party is a business. Business payer default is not later than 45 days from month end of invoice submission (סעיף 3(ז)). Public bodies: 45 days from submission or 30 days from month end (סעיף 3(א)). For עבודות הנדסה בנאיות a longer track of up to 85 days from submission or 70 days from month end (סעיף 3(ב)), source: same, why core: the skill serves both sides, and a company, עמותה, or landlord commissioning a renovation flips the whole payment regime.
- [ ] Milestone payments tied to verified completion, with a retention held past handover, source: statutory hook is סעיף 4 (deduct or self-cure) plus סעיף 6 (acceptance) at https://he.wikisource.org/wiki/חוק_חוזה_קבלנות, why core: this is the skill's core commercial output and must be anchored in the cure-and-deduct mechanism rather than asserted as custom.
- [ ] Price must state כולל מע"מ or בתוספת מע"מ explicitly, why core: after schedule, an unexpected VAT line is the most frequent renovation dispute.
- [ ] Only an עוסק מורשה may issue a חשבונית מס (סעיף 47(א)); every עוסק must issue a חשבונית עסקה (סעיף 46). An עוסק פטור therefore issues a חשבונית עסקה and a קבלה, never a חשבונית מס. עוסק מורשה charges מע"מ and issues a חשבונית מס. The turnover ceiling is deliberately NOT stated in this skill: it re-indexes annually, it is not needed to draft a scope document, and carrying it would add a drift surface for no benefit. why core: a homeowner who is himself a business gets no מס תשומות from an עוסק פטור receipt, which changes the real price.

### Permits

- [ ] Baseline rule under סעיף 145(א)(2) חוק התכנון והבנייה: a permit is required for erecting, demolishing and re-erecting, adding to, and **any repair to** a building, except a שינוי פנימי בדירה, VERIFIED, source: https://he.wikisource.org/wiki/חוק_התכנון_והבניה, why core: this is the permit decision boundary for almost every renovation.
- [ ] The FIVE statutory negative conditions in the definition of שינוי פנימי, each enumerated separately: not touching the exterior of the building; not harming its חזית or מראה or **שלד**; not harming **רכוש משותף** or piping or other equipment also serving other dwellings; not harming others (אינו פוגע בזולת); not changing the dwelling's **שטח** (save a lawfully enclosed balcony) or the **number of יחידות דיור**. VERIFIED verbatim, source: https://he.wikisource.org/wiki/חוק_התכנון_והבניה, why core: these five are the actual decision boundary for the large majority of Israeli renovations, and this is exactly where an unqualified "internal work needs no permit" answer becomes dangerous.
- [ ] General preconditions attached to EVERY exemption (פרק א of the regulations): performed by a holder of a right in the land; structural stability and occupant safety assured; compliance with the applicable תכנית and הנחיות מרחביות; no harm to a שימור site or the coastal strip, source: https://he.wikisource.org/wiki/תקנות_התכנון_והבנייה_%28עבודות_ומבנים_הפטורים_מהיתר%29, why core: exempt work performed in breach of these is an unlicensed building offence, not permitted work.
- [ ] Reporting duty for exempt works (הודעה, via the מינהל התכנון online system), source: same, why core: homeowners routinely believe "exempt" means "nothing to file".
- [ ] Enumerated exemption categories relevant to renovation, each verified individually rather than summarised: גדר וקיר תומך; גגון or סוכך; מצללה (פרגולה); מזגן; החלפת רכיב ברכיב בעל מידות זהות (the correct home for window and pipe replacement, with "מידות זהות" as the limit); פרטי עזר such as cameras and lighting; שלט; ממ"ד in low-rise housing (exempt only with הג"א approval), source: same. Caps VERIFIED for סורגים (תקנה 17, ת"י 1635 plus an escape-opening bar in one window per dwelling, 45-day notice to the licensing authority AND the national fire authority), מצללה (תקנה 12, 50 sq m **or a quarter of the free ground or roof area, whichever is larger**, and the definition requires at least 40 percent evenly distributed gaps so a solid roof disqualifies), and מזגן (תקנה 19, 60,000 BTU, placement conditions, and **no** notice duty).

### The trades

- [ ] קבלן רשום threshold has TWO independent limbs, value and nature. Under תקנות רישום קבלנים לעבודות הנדסה בנאיות (היקף כספי ומהות מקצועית) התשמ"ד-1984, work at a single site must be performed by a registered contractor above **108,500 ש"ח per ענף עבודה** and **56,750 ש"ח per ענף משנה** (nevo text as of 24.5.2026). Separately, work touching the **שלד** requires a registered contractor **regardless of value**, source: https://www.nevo.co.il/law_html/law00/74262.htm, why core: the second limb means a cheap structural job still needs a registered contractor, which the value-only framing in every guide misses.
- [ ] Temporal rule for that threshold. The amounts are updated **every 1 January** by the rise in מדד תשומות הבנייה למגורים (October against the preceding October), rounded to the nearest 50 ש"ח, and the רשם publishes the updated figures in רשומות. The governing version is the one in force at the relevant time; there is no grandfathering, source: same, why core: any hardcoded figure is stale within twelve months, so the skill must carry the as-of date AND the update mechanism, and point at the current notice.
- [ ] Registration is per ענף. A contractor registered in one branch is not thereby permitted at the threshold in another, source: same, why core: sub-dimension of the threshold.
- [ ] How to verify registration: the פנקס הקבלנים maintained by רשם הקבלנים at משרד הבינוי והשיכון, searchable by registration number, ענף, and סיווג.
- [ ] חשמלאי בודק is a SEPARATE licence class, and a חשמלאי מוסמך may not sign his own inspection. בודק סוג 1 up to 3x80A; סוג 2 up to 3x250A; סוג 3 any installation, source: same, why core: a תעודת בודק issued by the same מוסמך who did the work is worthless. Enumerating the three בודק grades is the sub-dimension.
- [ ] Whether a תעודת בודק is STATUTORILY required after ordinary apartment rewiring: RESOLVED AS A NEGATIVE. No such duty on a private homeowner was located, and the commonly cited תקנות החשמל (בדיקת מיתקן חשמלי) does not appear to exist. The skill treats it as a **contractually required handover artifact**, which is defensible and useful, and must NOT assert a blanket statutory duty.

### Living in a building with other people

- [ ] Renovation noise, national floor. Noisy building and repair work is prohibited 20:00 to 07:00 on weekdays, and from 17:00 on the eve of a rest day until 07:00 the morning after, with a full-day prohibition on rest days. Basis is חוק למניעת מפגעים and its 1992 regulations, source: https://he.wikisource.org/wiki/תקנות_למניעת_מפגעים_%28מניעת_רעש%29, why core: the working-hours clause is the single most common neighbour dispute trigger.
- [ ] Municipal by-laws may be STRICTER and vary by city, often adding a midday rest break, source: same, why core: the skill must never state one national range as final. It must send the user to the local חוק עזר.
- [ ] Noise inside permitted hours can still be an actionable מטרד if unusual, prolonged, or materially harming quality of life, source: same, why core: a clause promising "only permitted hours" is not a complete defence.
- [ ] Damage to רכוש משותף and to neighbours is the homeowner's exposure, pushed to the tradesperson contractually, source: same, why core: drives the indemnity and third-party insurance clause.

### The document itself

- [ ] Written scope must enumerate quantities, finishes, brands or specs, and explicit EXCLUSIONS. No statutory source; this is the drafting core, why core: an unspecified finish is the mechanism by which תוספות inflate the price, and the כתב כמויות is the whole point of the skill.
- [ ] Delay compensation drafted as פיצוי מוסכם with a daily rate, a cap, and defined excusable delays, grounded in חוק החוזים (תרופות) as preserved by סעיף 7, why core: without a liquidated figure the homeowner must prove actual damage.
- [ ] Warranty split BY TRADE with separate periods (איטום, ריצוף, נגרות, חשמל, אינסטלציה, צבע), each with its own definition of defect against fair wear, why core: a single blanket "one year warranty" is what the parties default into, and it is worse for both.
- [ ] Handover artifacts checklist: as-built or marked routing of concealed plumbing and electrical lines, appliance warranties and manuals, tile and paint batch plus surplus stock, the electrician's certificate where obtained, איטום test evidence for wet rooms, waste removal confirmation, and the signed acceptance protocol that starts the warranty clock (סעיף 6), why core: the concealed-piping map is what makes the NEXT renovation safe.
- [ ] Who buys the materials, and the consequence. The statute's application provisions carve out a contract that is in substance a מכר where the contractor supplies materials, source: https://he.wikisource.org/wiki/חוק_חוזה_קבלנות, VERIFIED (סעיף 8(ב)): the carve-out targets a contract to supply an asset **that must be produced or manufactured** where the contractor supplies the main materials, which then falls under חוק המכר תשכ"ח-1968. why core: it does NOT reach renovating an existing apartment, so a renovation where the contractor buys the tiles stays a חוזה קבלנות. Guides that call any materials-inclusive job a sale are wrong.
- [ ] Insurance as a CONTRACTUAL precondition, not a statutory duty. ביטוח צד ג' with the homeowner as additional insured and an אישור קיום ביטוחים before the first day; ביטוח עבודות קבלניות once the work is structural or high value. NOT verified as legally mandatory for a private home renovation, and the skill must not say it is, why core: genuinely load-bearing in the contract, and mislabelling it as a legal requirement would be a fabricated claim.
- [ ] Cash payment: the rule is NOT a flat 6,000 ש"ח cap. סעיף 2 triggers on the TRANSACTION PRICE exceeding the Schedule amount, and the definition of "תשלום במזומן" in סעיף 1 carves out only the LOWER of ten percent of the price and the Schedule amount, source: https://he.wikisource.org/wiki/חוק_לצמצום_השימוש_במזומן, VERIFIED 2026-08-27. why core: the flat-cap reading is permissive in the dangerous direction, and סעיף 2(ג) binds the paying homeowner, so the skill's own emphasis would turn a wrong figure into an instruction to commit an offence.
- [ ] חוק החוזים האחידים where the tradesperson issues a standard form to many clients: סעיף 4(1) liability cap, 4(2) unreasonable suspension/cancellation right, 4(6א) agreed compensation unreasonably in the supplier's favour are all presumed מקפח; סעיף 5(א) (limiting access to the courts) and 5(ב) (bodily-injury exemption) are void outright, source: https://he.wikisource.org/wiki/חוק_החוזים_האחידים, VERIFIED 2026-08-27. why core: the skill actively drafts three of these clauses for the tradesperson side, and the homeowner side needs the same fact as a defence.
- [ ] The limits of סעיף 72(א): the מפקח's jurisdiction reaches disputes about rights or duties under the תקנון or under the sections it enumerates (58, 59, 59א-59ג, 59ה-59י) and three named statutes, and NOT a neighbour's tort claim for damage caused by the works, source: https://he.wikisource.org/wiki/חוק_המקרקעין, VERIFIED 2026-08-27. why core: an over-broad "small claims will dismiss you" costs a neighbour with a modest damage claim the cheapest forum available to him. סעיף 72(ב) is לפי בחירתו, an option and never compulsory.

## Should cover (advanced / edge cases)

- [ ] Safety regulations: a מבצע בניה must appoint a מנהל עבודה and notify the מפקח עבודה אזורי under תקנות הבטיחות בעבודה (עבודות בניה) התשמ"ח-1988, source: https://he.wikisource.org/wiki/תקנות_הבטיחות_בעבודה_%28עבודות_בניה%29. The threshold at which a private apartment renovation becomes "עבודות בניה" was NOT verified, so the skill should frame this as "ask who the מבצע בניה is" rather than assert a trigger.
- [ ] עבודה בגובה is separately regulated (scaffolding, facade, roof), source: https://he.wikisource.org/wiki/תקנות_הבטיחות_בעבודה_%28עבודה_בגובה%29.
- [ ] Consumer cancellation window: VERIFIED AS NOT APPLICABLE. The right attaches only to the 23 enumerated Schedule items and none covers building, renovation, or trade services; תקנה 6(א) separately excludes made-to-measure goods and furniture assembled in the home. The 14-day right asserted throughout renovation guides does not exist for this engagement. Distance-selling and door-to-door provisions of חוק הגנת הצרכן are a SEPARATE route, source: https://he.wikisource.org/wiki/תקנות_הגנת_הצרכן_%28ביטול_עסקה%29
- [ ] התיישנות VERIFIED: סעיף 5 gives seven years for a non-real-property claim and a renovation contract claim is contractual; סעיף 8 starts the clock on discovery; סעיף 9 restarts it on acknowledgment and treats **partial performance as an acknowledgment**, so a contractor's partial repair can restart it, why: bounds how long a contractual warranty is worth writing.
- [ ] Subcontractors: the terms should bar or condition subcontracting and keep the head contractor liable. No statutory source, why: the most common route by which a warranty becomes unenforceable against anyone.
- [ ] Change orders: extra work agreed in writing and priced BEFORE execution. No statutory source, why: converts the single largest source of renovation disputes into a documented decision.
- [ ] Dated photographic record before, during, and after, and treating WhatsApp exchanges as a written record.
- [ ] Neighbour notice and a pre-work condition survey of adjoining apartments, protecting against later cracking claims.
- [ ] Waste (פסולת בניין) removal, container permits, and site access, water and electricity consumption. Municipal rules vary; treat as a locally confirmed checklist item.
- [ ] The tradesperson's side: deposit, materials price escalation, delays caused by the homeowner's own access failures, and the עכבון fallback (סעיף 5), why: the skill serves both sides and must not read as a homeowner shield.

## Out of scope (explicit, with rationale)

- חוק המכר (דירות) בדק and אחריות schedule for a newly purchased apartment. Different legal basis entirely (statutory and mandatory, developer facing) from renovation (contractual and dispositive). Related skill: `israeli-home-defect-report` handles it.
- New-build private home construction on private land. Permit, שלד, engineer supervision, and construction-loan mechanics are a different pipeline. Related skill: `israeli-private-home-construction` handles it.
- Generic freelance or professional services agreements, with no כתב כמויות, no בדק, and no permit dimension. Related skill: `israeli-freelancer-service-agreement` handles it.
- Employer and employee contracts. A tradesperson who is an עובד falls outside סעיף 1 by definition, and misclassification is an employment-law topic. Related skills: `israeli-employment-contracts`, `israeli-workplace-rights-navigator`.
- תמ"א 38, פינוי-בינוי, and building-wide renovation projects. Building-scale developer transactions with their own statutory regime.
- Pricing, estimating, or validating whether a renovation quote is reasonable. The skill structures the engagement and never supplies or judges a price. This is the highest-risk invented-number surface in the domain.
- Suing a contractor, drafting pleadings, or assessing the merits of a claim. Related skill: `israeli-small-claims-court` within the jurisdiction limit, otherwise a licensed advocate.
- Structural or safety assessment of an existing element. That is a licensed engineer's call.
- Insurance product selection and pricing. The skill names policy types as contract preconditions only.

## Findings added by the pre-push expert review (2026-08-11)

The Phase 2.9 expert review, run as a practitioner answering a real user's question rather than as a
scope check, found gaps that this checklist itself had not anticipated. All were fixed before push.
Recorded here so a future update does not quietly drop them:

- Counterparty identity (`ת.ז.`/`ח.פ.`), a personal guarantee where the contractor is a company, and
  checking that a `פנקס הקבלנים` registration is CURRENT rather than merely existing.
- חוק לצמצום השימוש במזומן: the cash cap binds the paying homeowner too, not only the tradesperson.
- Post-dated cheques, which defeat the milestone schedule and the retention entirely.
- Naming WHO verifies a milestone, without which "verified completion" is not operable.
- A termination clause and a suspension-for-non-payment clause, absent from the first draft.
- An indemnity distinct from insurance, and employers' liability cover for the crew.
- A chronological pre-payment sequence, and the irreversible items: first-fix photography, the
  pre-tiling flood test, notifying the homeowner's own insurer, and baseline meter readings.
- The building's `תקנון` as a third layer over the noise floor and the by-law.
- Gas as a licensed trade, previously missing from the trade checklist entirely.
- TWO factual corrections: the הצמדה/הרחבה majority conflation, and the wrong dispute forum.

## Known bad figures (secondary sources that are wrong)

A note on stale figures generally: commercial renovation guides routinely republish threshold
amounts from an earlier indexation year without an as-of date. Treat ANY threshold figure that does
not carry the date it applies from as stale, including the ones in this skill.

- "חוק מוסר תשלומים gives the שיפוצניק שוטף פלוס 45 from the homeowner". Actually the law does not apply where the payer is a private individual, source: https://he.wikisource.org/wiki/חוק_מוסר_תשלומים_לספקים.
- "Renovation defects carry the חוק המכר (דירות) בדק periods". Actually there is no statutory בדק schedule for renovation. The periods are whatever the contract sets, backed by the סעיף 3 notice-and-cure mechanism, source: https://he.wikisource.org/wiki/חוק_חוזה_קבלנות.
- "חוק חוזה קבלנות sets a fixed number of days to report a defect". Actually סעיף 3 says only "זמן סביר" after discovery, plus a reasonable cure opportunity, source: same.
- "Any internal renovation is exempt from a permit". Actually the internal-change carve-out does not reach changes to area or unit count, to systems outside the apartment, or to load-bearing elements.
- "A חשמלאי מוסמך can issue the תעודת בודק for his own work". Actually inspection is a distinct licence class (בודק סוג 1, 2, 3), source: https://he.wikisource.org/wiki/תקנות_החשמל_%28רשיונות%29.
- "A renovation contract can be cancelled within 14 days." No such right exists for this engagement.
- "Expanding into or taking common property needs a three-quarters majority." That is `סעיף 71ב` and
  covers only building an extension. Attaching an existing common part needs EVERY owner, `סעיף 62(א)`.
- "A renovation dispute goes to small claims." Owner-versus-owner disputes in a בית משותף go to the
  `מפקח על רישום המקרקעין` (`סעיף 72(א)`), and small claims is individual-only and capped.
- "Renovation noise is allowed 07:00 to 20:00 everywhere in Israel". That is only the national floor. Municipal by-laws are frequently stricter, and in-hours noise can still be an actionable מטרד, source: https://he.wikisource.org/wiki/תקנות_למניעת_מפגעים_%28מניעת_רעש%29.

## Open items: RESOLVED 2026-08-10

All seven were closed against primary statute text in a second pass. Resolutions below; each has a
corresponding verbatim entry in `evidence.json`.

1. **סעיף 145(א)(2) CLOSED.** The permit rule is broad: "הקמתו של בנין, הריסתו והקמתו שנית, כולו או
   מקצתו, הוספה לבנין קיים **וכל תיקון בו**, למעט שינוי פנימי בדירה". Note "וכל תיקון בו", ANY repair
   needs a permit unless it lands in the carve-out or a separate exemption. The definition of
   "שינוי פנימי" is IN the statute, not in regulations, and is built from five negative conditions:
   not touching the exterior, not harming the facade, appearance, **שלד**, **רכוש משותף**, or piping
   or equipment also serving other dwellings, not harming others, and not changing the dwelling's
   **area** or the **number of dwelling units**.
2. **Exemption catalogue CLOSED.** סורגים IS enumerated (תקנה 17), conditioned on ת"י 1635 and on one
   window per dwelling carrying an escape-opening bar, with a 45-day notice to the licensing
   authority AND the national fire authority. מצללה is 50 sq m **or a quarter of the free ground or
   roof area, whichever is LARGER** (guides state a flat 50 and understate it), and a solid roof
   disqualifies it entirely since the definition requires at least 40 percent evenly distributed
   gaps. מזגן is 60,000 BTU with placement conditions and carries **no** notice duty. The 45-day
   notice is per-regulation, not general.
3. **תעודת בודק CLOSED as a NEGATIVE finding.** No statutory duty was located binding a private
   homeowner to obtain one after ordinary apartment electrical work, and the commonly cited
   "תקנות החשמל (בדיקת מיתקן חשמלי)" does not appear to exist as an instrument. The skill therefore
   requires the certificate **contractually** and must never claim the law requires it. What IS
   verified and load-bearing: inspection is a separate licence class, and a בודק may not inspect
   work he both designed and executed (תקנה 23), so the electrician cannot sign off his own job.
4. **התיישנות CLOSED.** סעיף 5: seven years for a non-real-property claim, and a renovation contract
   claim is contractual despite the works being on land. סעיף 8: the clock starts on discovery where
   the facts were unknown for reasons outside the plaintiff's control. סעיף 9: an acknowledgment
   restarts the clock, and **partial performance counts as an acknowledgment**, so a contractor who
   returns to do a partial repair may restart it.
5. **ביטול עסקה CLOSED, and the guides are wrong.** The cancellation right attaches only to the 23
   enumerated Schedule items, none of which covers building, renovation, or trade services. There is
   no 14-day right to cancel a renovation engagement. תקנה 6(א) separately excludes made-to-measure
   goods and furniture assembled in the home, which covers custom joinery. Distance-selling and
   door-to-door provisions of חוק הגנת הצרכן itself are a SEPARATE route and must not be conflated.
6. **סיווג caps CLOSED.** Group א (which contains sub-branch 131 שיפוצים) runs סוג ק up to 825
   thousand, then 1,927 / 3,854 / 7,708 / 15,416 thousand, then סוג 5 unlimited. Amounts are in
   THOUSANDS and re-index twice a year (1 April and 1 October). The instrument's real name is
   תקנות רישום קבלנים לעבודות הנדסה בנאיות (סיווג קבלנים רשומים); "תקנות סיווג קבלנים רשומים" is not
   a real title.
7. **עבודות בניה threshold NOT closed, and deliberately reframed.** No clean statutory trigger was
   found for when a private apartment renovation becomes "עבודות בניה" for the safety regulations.
   The skill therefore does NOT assert a threshold. It asks who the מבצע בניה is and flags that the
   answer determines who must appoint a מנהל עבודה, which is the actionable question either way.

## Authoritative sources

- https://he.wikisource.org/wiki/חוק_חוזה_קבלנות, the operative statute: סעיף 1 definition, סעיף 3 notice and cure, סעיף 4 remedies, סעיף 5 עכבון, סעיף 6 acceptance and risk, סעיף 7 preserved remedies, סעיף 8 dispositive application.
- https://he.wikisource.org/wiki/חוק_מוסר_תשלומים_לספקים, חוק מוסר תשלומים: the definitions that exclude a private individual, and the 45 / 45 plus 30 / 85 plus 70 payment tracks.
- https://www.nevo.co.il/law_html/law00/74262.htm, תקנות רישום קבלנים (היקף כספי ומהות מקצועית): the amounts, the שלד limb, and the 1 January indexation mechanism. Re-read every year.
- https://he.wikisource.org/wiki/תקנות_התכנון_והבנייה_%28עבודות_ומבנים_הפטורים_מהיתר%29, the exemption catalogue, the פרק א preconditions, and the reporting duty.
- https://he.wikisource.org/wiki/תקנות_החשמל_%28רשיונות%29, תקנות החשמל (רשיונות): execution grades and the בודק classes.
- https://he.wikisource.org/wiki/תקנות_למניעת_מפגעים_%28מניעת_רעש%29, noise floor and the municipal variation caveat.
- https://he.wikisource.org/wiki/חוק_המקרקעין, what counts as רכוש משותף and the consent rules.
- https://he.wikisource.org/wiki/חוק_מס_ערך_מוסף, the receipt against invoice rule and the turnover ceiling.
