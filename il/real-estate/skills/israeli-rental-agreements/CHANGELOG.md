# Changelog

## [2.0.0] - 2026-08-30

Second pass on the same skill, from an expert legal review that followed the v1.4.0 release. v1.4.0
carried the four reported defects plus three found while verifying them; this release adds the
remaining findings. Restructured so SKILL.md stays within its size limit: the section-by-section
statutory text now lives in `references/statutory-provisions.md`.

### Fixed
- Habitability: replaced an invented list of amenities with the closed six-item First Schedule, including the partition between the toilet and the apartment, the lockable main entrance door and the safety/health catch-all. Added 25ו(ב) (delivering an unfit apartment is a BREACH) and 25יד(1) (25ו cannot be varied at all).
- Section 25ט was reduced to the broker fee. Added the closed 25ט(א) list and all three 25ט(ב) prohibitions, notably the bars on charging the tenant for buying or upgrading fixed installations and for building insurance, the two commonest overcharges in the market.
- Eviction: removed "landlord needs the property for personal use", which belongs to protected tenancies and is not a ground for an unprotected residential lease. Named the תביעה לפינוי מושכר track instead of the small claims court, and added an explicit warning that self-help eviction (changing locks, removing belongings, cutting utilities) is unlawful.
- Section 25יד is now stated as the operative list of which provisions may be varied and in which direction, rather than a general assertion that the rules cannot be contracted around.
- Entry and privacy: there is no statutory notice period for landlord entry. The previous "24 hours" figure was presented as a rule.
- Corrected שטר הון to שטר חוב throughout, and removed the non-existent "rent tribunal" (ועדת שכירות) from the dispute-resolution options.

### Added
- Sections 25ד (gap-filling by the model lease), 25ז(ג) (handover instructions), 25יא (written notice before the apartment is handed to a buyer), 25יב (the 90-day landlord and 60-day tenant option deadlines) and 25טו(ג) (sub-letting duties stay with the head landlord), all previously absent.
- Section 25יג(א): a clause letting only the landlord cancel without breach is VOID unless the tenant has an equivalent right. 25יג(ב) fixes the 90/60 minimum notice by statute, previously described as "the standard model".
- Guarantee Law 5727-1967: s.21(ב) releases an ערב יחיד entirely where the deed states no fixed sum, and s.27 bars action against an ערב מוגן before execution against the tenant is exhausted.
- `references/statutory-provisions.md`, a section-by-section reference for 25א-25טו, both Schedules and the guarantor rules.
- An explicit note that on a lease with an option it is unsettled whether "one third of תקופת השכירות" means the initial or the extended term, rather than quoting one ceiling with false confidence.

## [1.4.0] - 2026-08-29

Corrections from a public report (four items, all verified against the consolidated statute), plus
three defects found while verifying them. A larger remediation covering further findings from an
expert legal review is prepared but held pending an independent review pass.

### Fixed
- Section 25י(ב)'s ceiling is scoped to guarantees "involving a monetary outlay by the tenant" (cash, bank guarantee). A promissory note and personal guarantors are not counted in it. The reference file previously said "the total of all guarantees".
- Sections 25י(ג), (ד) and (ה) bind EVERY guarantee, including those outside the ceiling: realisation only on the four closed grounds, advance notice and a chance to cure before realising, and return within 60 days including the guarantee's fruits. Realisation grounds replace the previous loose "damages beyond normal wear" description.
- The 20,000 NIS exclusion threshold in section 25טו(4) is updated every 1 January by the CPI and rounded to the nearest 10 NIS. Both language files previously stated it was not index-linked.
- The landlord's pre-contract disclosure duty is item 7 of the Second Schedule, mandated by section 25ג. It was attributed to section 25ב, which governs the written form of the contract only.
- The repair remedy: section 25ח(ג) applies s.9(א), giving reimbursement of reasonable expenses or a PROPORTIONAL rent reduction. The skill said the tenant may deduct the repair cost from the rent, advice that puts a tenant in arrears and hands the landlord a 25י(ג)(1) realisation ground and an eviction claim.
- Family leases are NOT excluded from the chapter. Section 25טו(ב) disapplies only 25יד(2) for a קרוב, so relatives may contract out but every protection otherwise applies. They were listed alongside hotels and dormitories as excluded.
- The bundled calculator's CPI table was invented data understating 2022-2025 inflation by roughly a third while emitting a shekel figure. Replaced with the official CBS series 120010, chain-linked across the 2020/2022/2024 base changes and extended to 2026-07.
- Replaced the Knesset legislation portal reference link, which returns 401.
- Corrected the 10-year exclusion (it requires that the landlord have no earlier cancellation right) and the 3-month exclusion (no extension option).

### Added
- The 2026 amendment (Sefer HaChukkim 3510, 31.3.2026) adding a "notenn aruvah acher" guarantee to section 25י, in force 30.9.2026.
- A note that where guarantors are used, an ערב יחיד is released entirely if the deed states no fixed sum (Guarantee Law 5727-1967, s.21(ב)).
- Reference links to the consolidated law text and the official Sefer HaChukkim publication.

### Changed
- Evidence entries for the deposit cap, the exclusion threshold, the disclosure duty, the written-form rule and the repair remedy now cite the statute directly instead of a secondary summary.

All notable changes to this skill are documented here.

## [1.3.0] - 2026-08-09

### Added

- נוסף פרק "הבהרה משפטית" בראש SKILL.md ו-SKILL_HE.md, המפרט מה הכלי עושה, מה הוא אינו, ולאיזה בעל מקצוע מוסמך יש לפנות.

### Changed

- התיאור נפתח כעת בהבהרה קצרה, כך שהיא נראית גם בכרטיס ובתוצאות החיפוש.
