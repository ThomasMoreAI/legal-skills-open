# Domain Coverage Checklist, israeli-home-defect-report

Generated: 2026-08-10. Revised 2026-08-26 (v1.1.0) via research on: nevo.co.il (consolidated text of חוק המכר (דירות), תשל"ג-1973, version current to 18-09-2023 following תיקון 9), kolzchut.org.il (אחריות קבלן לליקויים בדירה חדשה, הגשת תלונה לרשם הקבלנים), govforms.gov.il.

Every statutory row below was verified against the RAW HTML text layer of the source, not against a WebFetch summary and not against a marketing blog. Several widely-repeated blog figures are wrong (see "Known bad figures" at the end).

## Must cover (core)

### The two Schedule tables, split by purchase date

The single most common way to get this skill wrong is to encode one table. There are two, and the split is by the date the sale contract was concluded.

- [ ] Split rule: current Schedule applies where the sale contract was concluded on or after 06.04.2011 AND construction did not finish before that date - source: https://www.kolzchut.org.il/he/אחריות_קבלן_לליקויים_בדירה_חדשה - why core: applying the current table to a pre-2011 apartment overstates the buyer's rights, and applying the old table to a new one understates them. Both are actionable errors.
- [ ] Pre-2011 apartments keep the old table even if resold later - source: same - why core: a sub-buyer (קונה משנה) of an older apartment inherits the older periods, which is counter-intuitive.

Current Schedule (contract on/after 06.04.2011), all TEN items enumerated separately. Source for all ten: https://www.nevo.co.il/law_html/law00/72490.htm

- [ ] (1) מסגרות ונגרות incl. aluminium and plastic, 2 years
- [ ] (2) ריצוף וחיפוי פנים incl. subsidence and wear, 2 years
- [ ] (3) מכונות ודוודים, function and durability failure, 3 years
- [ ] (4) פיתוח חצר, 3 years, EXPRESSLY including שקיעות "בין השאר של מרצפות בקומת קרקע, בחניות, במדרכות ובשבילים בשטח הבניין" and finish-material surfaces, plus water, sewage, drainage, electricity, lighting and communications systems. Do NOT route sunken floor tiles to item (2) at 2 years
- [ ] (5) בידוד תרמי components, function and durability failure, 3 years
- [ ] (6) צנרת incl. water, heating, gutters, waste and sewage, 4 years, where "כשל" expressly includes leaks
- [ ] (7) איטום המבנה incl. underground spaces, walls, ceilings and roofs, "לרבות גגות קלים עם סיכוך", 4 years
- [ ] (8) סדקים wider than 1.5 mm in NON-load-bearing elements, 5 years
- [ ] (9) חיפויי חוץ detachment, peeling or crumbling, 7 years
- [ ] (10) any other non-conformity that is not fundamental, 1 year

Pre-2011 Schedule, enumerated separately. Source: https://www.kolzchut.org.il/he/אחריות_קבלן_לליקויים_בדירה_חדשה

- [ ] צנרת incl. heating and gutters, 2 years (NOT 4)
- [ ] חדירת רטיבות in roof, walls and shelter, 3 years
- [ ] מכונות, מנועים ודוודים, 3 years
- [ ] קילוף חיפויים in stairwells, 3 years
- [ ] שקיעת מרצפות on the ground floor, 3 years
- [ ] שקיעת מרצפות in parking, pavements and paths, 3 years
- [ ] סדקים עוברים in walls and ceilings, 5 years
- [ ] קילופים ניכרים in exterior cladding, 7 years
- [ ] any other non-fundamental non-conformity, 1 year

### The route that bypasses the Schedule

- [ ] s.4(a)(1): the apartment differing from the מפרט, from an official standard, or from the building regulations is a breach in its own right, independent of any Schedule row, period or burden - source: nevo - why core: it is the live route when a Schedule window has closed, and the Registrar lists it as its own complaint category. Absent from v1.0.0 entirely.

### Period arithmetic and burden of proof

- [ ] תקופת בדק starts at העמדת הדירה לרשות הקונה (actual handover of possession), NOT at contract signature and NOT at the date the protocol is signed if that differs - source: nevo, definition in s.4(c) - why core: getting the clock start wrong shifts every downstream date.
- [ ] תקופת אחריות is 3 years starting at the END of that item's bedek period, so total protection per item equals its bedek period PLUS 3 - source: nevo, definition in s.4(c) - why core: users and blogs routinely read the warranty as running from handover, which understates protection by up to 7 years.
- [ ] During bedek, the SELLER must prove the buyer caused the defect (s.4(a)(2)) - source: nevo - why core: this is the buyer's single biggest advantage and drives the urgency of acting inside the window.
- [ ] During acharayut, the BUYER must prove origin in planning, workmanship or materials (s.4(a)(3)) - source: nevo - why core: this is normally the point at which a licensed expert opinion becomes practically necessary, which is a routing trigger.

### Fundamental non-conformity (load-bearing), routing row

- [ ] Definition: a non-conformity in the parts that carry and transfer loads to the ground and that concerns the building's stability and safety - source: nevo s.4(c) - why core: it defines the boundary of what this skill must refuse to assess.
- [ ] 20-year bedek period with the burden on the SELLER (s.4(a)(4)) - source: nevo - why core: a user with structural cracks at year 9 would otherwise be told they are out of time, which is badly wrong.
- [ ] Actionable even AFTER 20 years where the buyer proves origin (s.4(a)(5)) - source: nevo - why core: there is no absolute cut-off, and saying otherwise forecloses a real right.
- [ ] ROUTING row: the skill must NOT classify a defect as fundamental, assess structural integrity, or assess safety. On any indicator (cracks in load-bearing elements, sagging, movement, water reaching electrical systems) it must stop the workflow and route to a licensed מהנדס and, where there is an immediate hazard, to emergency services - why core: this is a reserved professional act and a safety-of-life issue.

### Notice duties

- [ ] Discoverable-at-handover defects: notice within ONE YEAR of handover (s.4a(a)(1)) - source: nevo - why core: missing it forfeits reliance on the defect regardless of remaining bedek period. This is the highest-consequence deadline in the skill.
- [ ] s.4a(b): a hidden FUNDAMENTAL non-conformity has its OWN notice limb, reasonable time after discovery, with no one-year cut-off - source: nevo - why core: s.4a has three limbs, not two. Applying the one-year bar to a load-bearing defect tells a claimant with a live 20-year claim that they missed the deadline. This is the most damaging output the skill can produce.
- [ ] Hidden defects: notice within a reasonable time after discovery, even if more than a year has passed (s.4a(a)(2)) - source: nevo, and Kol Zchut gives internal piping as the worked example - why core: users wrongly assume the one-year bar kills all late claims.
- [ ] The one-year notice duty and the bedek period are TWO SEPARATE clocks that both must be satisfied - why core: conflating them is the most common analytical error in this domain.

### Right to repair, and the demand letter

- [ ] s.4b(a): the buyer MUST give the seller a proper opportunity to repair, and the seller must repair within a reasonable time - source: nevo - why core: a buyer who repairs first and demands money after generally loses. This makes the demand letter a legal step, not a formality.
- [ ] s.4b(b): self-repair at the seller's expense only where the defect RECURRED after the seller repaired it once or more within two years of the notice, OR the repair is urgent and the seller did not repair in reasonable time - source: nevo - why core: these are the only two statutory gateways to self-help.

### Waiver and the handover protocol

- [ ] s.7A(a): no contracting out of the law except in the buyer's favour - source: nevo - why core: contract clauses shortening bedek periods are ineffective, and users assume their contract overrides the statute.
- [ ] s.7A(b): a waiver, including a written one, of defect or late-delivery rights that is made a CONDITION of handover, of repairs, or of transfer of rights, is VOID (בטל) - source: nevo - why core: this is exactly the pressure applied at the keys handover.
- [ ] A waiver is ineffective even where the buyer agreed freely, for example in exchange for a discount - source: Kol Zchut FAQ - why core: it is the buyer's most common self-inflicted worry and the answer is reassuring and correct.
- [ ] Correct framing of signing the protocol: signing cannot legally waive the contractor's liability, but a signed factual statement that the apartment is defect-free is an evidentiary admission that a court will weigh. The remedy is to record reservations in writing on the protocol rather than to refuse to sign - why core: the popular framing ("sign and you lose everything") is legally wrong but the practical advice attached to it is right, so the skill must separate the two.
- [ ] s.5(c): where the seller supplied no compliant מפרט, the burden of proving the item was of high quality rests on the SELLER - source: nevo - why core: a free extra argument most buyers never raise.
- [ ] s.4(a)(6): failure to deliver הוראות תחזוקה ושימוש is itself a breach - source: nevo - why core: commonly omitted by contractors and independently actionable.

### Remedies and forums

- [ ] Written demand to the contractor is the statutory opportunity to repair under s.4b(a) and the evidence every later route rests on. It is NOT a legal precondition for a Registrar complaint - source: nevo s.4b(a); https://www.gov.il/he/service/complaint-about-constractor - why core: it is the skill's primary output and its legal function must be stated accurately. v1.0.0 asserted a precondition that the regulator does not impose.
- [ ] Complaint to רשם הקבלנים at the Ministry of Construction and Housing, free, filed at https://govforms.gov.il/mw/forms/complaint-about-contractor@moch.gov.il - source: Kol Zchut - why core: the only free escalation, and most buyers have never heard of it.
- [ ] Registrar limits: disciplinary only, not arbitration, does not resolve the dispute, does not handle monetary disputes or matters already in court; contractor must be in the register. ANY citizen may file; the house-committee route for common property is RECOMMENDED, not required - source: https://www.gov.il/he/service/complaint-about-constractor - why core: setting the wrong expectation sends users down a route that cannot give them money, and a fabricated bar shuts them out of the only free one.
- [ ] Civil suit is available in parallel, and s.7 preserves all other rights under any law - source: nevo s.7, Kol Zchut - why core: the statute is a floor, not a ceiling.
- [ ] ROUTING row: a contested claim, quantification of damages, and any court filing require a licensed עורך דין, and the supporting חוות דעת הנדסית requires a licensed מהנדס - why core: reserved acts, and the honest limit of this skill.

## Should cover (advanced / edge cases)

- [ ] קונה משנה (sub-buyer) inherits the rights, and the clock still runs from the ORIGINAL handover, not from the resale - source: nevo, definitions and s.4 - why: common in second-hand purchases of nearly-new apartments.
- [ ] Common property (רכוש משותף): route through the elected house committee where one exists, which the Ministry recommends. An individual owner is NOT barred from filing - source: https://www.gov.il/he/service/complaint-about-constractor - why: a large share of real defects (roof sealing, exterior cladding, yard development) are in common property, and a fabricated bar shuts a user with no functioning committee out of the only free route.
- [ ] Distinguishing normal wear, user-caused damage and a genuine defect, so the log does not get discredited wholesale by one bad entry.
- [ ] Evidence hygiene for the log: date, room, photograph with scale reference, and whether the defect was visible at handover, since visibility is what selects the notice rule.
- [ ] Recurrence tracking, because s.4b(b) self-help depends on counting repairs within a two-year window, which nobody tracks unless told to.
- [ ] Interaction with התיישנות (general limitation) as a separate outer bound on suing, flagged as a lawyer question rather than answered. MUST be surfaced to the user whenever a window end-date is reported, since a cover period is not a filing deadline.
- [ ] What happens between the demand letter and a claim: conduct at the contractor's repair visit (attend, photograph, date, sign nothing accepting the repair), re-inspection, the licensed מהנדס opinion and when it becomes worth its cost, the small-claims track, מומחה מטעם בית המשפט, and עוגמת נפש as a distinct head of damage - why: this is the half of "what do I actually do" that v1.0.0 stopped short of, and repair-visit records are what the s.4b(b) gateway is counted from.

## Out of scope (explicit, with rationale)

- Structural and safety assessment, and any classification of a defect as אי-התאמה יסודית: reserved to a licensed מהנדס, and a wrong answer is a safety risk. The skill routes instead.
- Producing a חוות דעת הנדסית or anything presented as an expert opinion: reserved work product, and the thing courts actually rely on. The skill produces a buyer's own log, which is a different artifact.
- Costing or quantifying repair value in shekels: in practice this is שמאי or מהנדס territory and an invented number would anchor the user wrongly.
- Late-delivery compensation under s.5A: real and adjacent, but a distinct money claim with its own formula, not a defect matter. Named so the user knows it exists and is told it is separate.
- בטוחות / ערבות חוק מכר and the Sale Law Supervisor: protects payments against contractor insolvency, unrelated to defect liability. Named to prevent misrouting.
- Rental property defects: different statute entirely, handled by israeli-rental-agreements.
- Private home built by the owner on their own land: no קבלן-seller and no חוק המכר (דירות) relationship. israeli-private-home-construction owns that.
- Drafting court pleadings or representing the user: reserved to an advocate.

## Known bad figures circulating in secondary sources

Recorded so a future update does not "correct" the skill back to them:

- "plumbing 2 years": true only for pre-06.04.2011 apartments. Current Schedule is 4 years.
- "roof sealing 3 years": current Schedule item 7 is 4 years for איטום. The 3-year figure is the pre-2011 חדירת רטיבות row.
- "structure 7 years": there is no 7-year structural item. Item 9's 7 years is exterior CLADDING. Load-bearing structure is the 20-year fundamental regime.
- "warranty is 3 years from handover": it is 3 years from the END of the item's bedek period.
- "sunken floor tiles are ריצוף, 2 years": no. The statute expressly puts שקיעת מרצפות on the ground floor, in parking, on pavements and on paths inside item (4) פיתוח חצר at 3 years. v1.0.0 truncated the row and misrouted them.
- "a complaint to the Registrar requires a prior written demand": no such requirement on the Ministry's page.
- "an individual owner cannot complain about common property": the Ministry says any citizen may file and the committee route is only recommended.
- "a recent amendment changed the defect regime": the last substantive change is תיקון 5 (2011); תיקון 9 (2022) touched late delivery and waiver. Later amendments recorded against this law are indirect (a Knesset committee renaming) and do not touch defects.

## Authoritative sources

- https://www.nevo.co.il/law_html/law00/72490.htm - consolidated חוק המכר (דירות), תשל"ג-1973. Verify: the Schedule's ten items, s.4 burdens, s.4a notice, s.4b repair, s.7A waiver. Check the "נוסח עדכני נכון ליום" banner for a newer amendment.
- https://www.kolzchut.org.il/he/אחריות_קבלן_לליקויים_בדירה_חדשה - Verify: the two-table split at 06.04.2011, the pre-2011 table, the waiver FAQ.
- https://www.kolzchut.org.il/he/הגשת_תלונה_לרשם_הקבלנים_במשרד_הבינוי_והשיכון - Verify: registrar prerequisites, scope limits, who may file.
- https://www.gov.il/he/service/complaint-about-constractor - the Ministry's service page and the AUTHORITY on who may file, what to attach and the disciplinary scope limits. Note the official slug misspells "contractor". Cloudflare-protected: read it in a real browser, not with curl.
- https://govforms.gov.il/mw/forms/complaint-about-contractor@moch.gov.il - Verify: the complaint form is still live and at this address. Returns an empty JS shell to curl; confirm in a browser.
