# Changelog

All notable changes to this skill are documented here.

## 1.4.0 - 2026-08-19

Regulatory-reform pass. The EU AI Act timeline moved from proposal to enacted law inside the review window, and Bank of Israel Directive 364 came into force.

### Corrected
- **The Digital Omnibus on AI is adopted, not pending.** Regulation (EU) 2026/1744 of 8 July 2026 was published in OJ L 2026/1744 on 24 July 2026 and entered into force on 27 July 2026. Every passage describing it as a provisional political agreement awaiting formal adoption has been replaced with the enacted text, and the Reference Links now cite EUR-Lex rather than the Council press release.
- **Added the trap the postponement creates.** Only the high-risk dates moved. The general date of application stayed at 2 August 2026, which has now passed, so Article 50 transparency applies to systems placed on the EU market since. A customer document reading "the AI Act was postponed to 2027" as covering everything is wrong.
- **ISO/IEC 42001 is not an EU AI Act conformity route.** The previous text said its controls "map cleanly to EU AI Act high-risk obligations". The European Commission states that 42001's goals and definitions are not aligned with the quality management system the AI Act requires, and that it has commissioned a separate standard.
- **Bank of Israel Directive 364 came into force on 18/05/2026** (or earlier on adoption by the bank), repealing Directives 357, 361 and 363 on that date. The skill previously gave only the 18/11/2024 publication date, which left the repeal undated. The Reference Links now point at kamakama.gov.il, which mirrors the Supervisor of Banks pages that boi.org.il serves only to browsers.
- Refreshed "as of May 2026" currency statements to August 2026 across SKILL.md, SKILL_HE.md and references/.

### Added
- The two NEW prohibitions inserted by the Omnibus (Article 5(1) first subparagraph points (ba) and (bb), and Article 5(1a) and (1b)), applying from 2 December 2026.
- Articles 102 to 110 applying from 27 July 2026, per the new Article 113(3)(d).
- The new Article 111(4) legacy grace period: providers of synthetic-content systems placed on the market before 2 August 2026 have until 2 December 2026 to comply with Article 50(2).
- The amended Article 111(2) deadline of 2 August 2030 for high-risk systems intended for use by public authorities.
- The Commission's stated rationale for the postponement (delayed standards, common specifications and guidance, and delayed establishment of national competent authorities).

### Corrected (sourcing)
- **The six Ministry of Innovation regulatory principles were wrong.** Three of the six listed ("whole-of-government approach", "balanced and proportionate intervention", "regular review and evolution") do not appear in the policy, and two real ones were missing. Both lists are now quoted from the PDF: empowering sector-specific regulators, international interoperability of frameworks, risk-based approach, incremental development and regulatory experimentation, soft regulation, multistakeholder cooperation. The ethical principles were re-listed the same way, including the growth principle that was absent and the accountability wording.
- **The policy title and date were wrong.** It is "Responsible Innovation: Israel's Policy on Artificial Intelligence Regulation and Ethics", published December 2023. The document carries no day-level date, so the previously asserted "December 14, 2023" was removed everywhere.
- Removed unsourced dates: the 31 October 2025 DPO grace-period expiry, "April 2025" as the PPA draft guidance publication month, the NIST critical-infrastructure concept-note day, and the "1 August 2025 via adequacy decisions" framing of the GPAI Code endorsement, which the Commission page does not support.
- Removed an invented "Risk Management Toolbox" and "National AI Ethics Committee" attributed to the AI Policy Coordination Center.
- Removed the ISO/IEC 42001 control count, which rests on a source that is Cloudflare-gated and could not be read.
- The February 2026 PPA consent opinion is now hedged consistently as reported by secondary analysis rather than primary-verified, in prose, checklist and gotchas, in both languages.

### Fixed (scripts)
- `classify_eu_ai_act_risk.py` evaluated Article 5 prohibitions BEFORE the Article 2 scope test, so an Israel-only system was told it was "Prohibited" under a regulation that does not reach it. Scope is now tested first, and an out-of-scope system that matches a prohibited practice gets that flagged as a design signal rather than as an AI Act finding.
- Its Article 5 screen narrowed social scoring to public authorities, which the statute does not, and omitted Article 5(1)(a) and 5(1)(g). All eight limbs are now present with their article references, and the caveat now says plainly that this is a screen and not a clearance.
- `--input` mode defaulted every absent or misspelled key to false, so a partially filled or typo'd JSON returned a confident classification. It now rejects unknown keys and refuses to classify with missing answers.
- Every in-scope result now prints the amended Article 113 applicability dates and a role-determination caveat.

### Added
- Role determination (provider, deployer, importer, distributor) as the first step of the EU AI Act analysis, with the Article 25 rule that a deployer branding or substantially modifying a high-risk system is treated as its provider.
- The Article 6(3) derogation for Annex III systems, in the risk-tier table and the decision framework.
- The EU AI Act risk-tier obligations table to SKILL_HE.md, which had been carrying the timeline without it.

### Evidence
- Every EU AI Act citation now points at a EUR-Lex CELEX URL read in a real browser with the location asserted, rather than an ELI permalink that returns an empty 202 body to any non-interactive fetch.

## [1.3.0] - 2026-08-09

### Added

- נוסף פרק "הבהרה משפטית" בראש SKILL.md ו-SKILL_HE.md, המפרט מה הכלי עושה, מה הוא אינו, ולאיזה בעל מקצוע מוסמך יש לפנות.

### Changed

- התיאור נפתח כעת בהבהרה קצרה, כך שהיא נראית גם בכרטיס ובתוצאות החיפוש.
