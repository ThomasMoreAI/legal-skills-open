# Changelog

All notable changes to this skill are documented here.

## [1.4.0] - 2026-08-09

### Added

- נוסף פרק "הבהרה משפטית" בראש SKILL.md ו-SKILL_HE.md, המפרט מה הכלי עושה, מה הוא אינו, ולאיזה בעל מקצוע מוסמך יש לפנות.

### Changed

- התיאור נפתח כעת בהבהרה קצרה, כך שהיא נראית גם בכרטיס ובתוצאות החיפוש.

## 1.5.0 (2026-08-27)

### Fixed (critical)
- **The 10-year window is not the Pikadon window.** v1.3.0 told active reservists their Pikadon
  purposes stayed open for ten years and dated the rule to Iron Swords. Section 19(a1)(1) attaches
  that window to the Section 7(a) and 7A study funds, for active reservists AND lone soldiers, and
  it came from Amendment 19 (12.07.2017) re-enacted by Amendment 24 (2022). The Pikadon's
  restricted-purpose window is five years for everyone. This also resolves a contradiction with
  `israeli-lone-soldier-rights`, which had it right.
- **The legal notice named the wrong authority**, the National Insurance Institute, for a skill
  whose paying authority is the MoD Department and Fund for Discharged Soldiers. Rewritten in both
  languages and in both descriptions to name the right body per benefit.
- **An approved request is not cash.** Sections 15(a) and 17(b) have the Fund pay the institution
  and the seller directly. The skill described all six purposes as a withdrawal to the user, and
  Example 4 told a Mimadim recipient to draw the Pikadon for costs it cannot legally pay.
- **Keva was unhandled.** Every Pikadon clock runs from the end of sherut chova, so a three-year
  keva leaver is already past the window. Credit points also run during keva with the 36 months
  starting after chova, leaving roughly 13 months on discharge from keva rather than 36.
- **Hesder and SHLAT.** Unpaid service does not accrue Pikadon but does count toward the
  credit-point threshold, measured on total service from enlistment.
- **Fabricated appeal channel.** Service-classification appeals were routed to a "Mador Iturim"
  that appears in no source. The route is the IDF public-enquiries officer, 1111 extension 5.

### Added
- Section 19(b) to (d): the 60-day transfer, the 120-day redemption where the bank account cannot
  be located, forfeiture to the Additional Assistance Fund at 5.5 years, the 4.5-year reclaim, the
  50 NIS residue, and the 3-year early release for a keva lochem.
- Step 8.6, Chok Chayalim Meshuchrarim (Hachzara LaAvoda): the 45-day request window, the 6-month
  employer obligation, the employer's burden of proof, the one-year fallback placement, and
  ועדת תעסוקה as the statutory forum.
- Section 12 funds bagrut completion, a mechina and psychometric preparation in their own right.
- Section 18א: the six purposes are the current Schedule, not a permanently closed list.
- Mimadim figures: the 12,017 NIS ceiling, 85% (10,214.45) with the 15% (1,802.5) released in the
  final year, three or four study years, the Charvot Barzel ordering rule, and the 31.10.26
  תשפ"ו deadline, which must be read off the Mimadim page and not the stale Iron Swords page.
- Real numbers and deadlines on the adjacent benefits: the 11,461 NIS required-work grant with its
  42-month claim deadline, the 60-day Rav-Kav profile deadline, the arnona owner-or-renter rule,
  the 688 NIS income ceiling on the BL exemption, the mortgage supplement, Pikadon 2000, and free
  Ministry of Justice legal aid.
- `references/adjacent-benefits.md` and `references/mimadim-scholarship.md`.
- Tofes 116 restored with a real citation; the female accrual cap now flagged as contested
  (hachvana publishes 24, s.11(a) reads 28 with a conditional commencement).

### Changed
- Credit-point table restated as thresholds rather than ranges, since the source is inconsistent
  about the boundary month.
- `pikadon-calculator.py`: added `--medical-discharge` and `--hesder-total-months` (credit-point
  threshold only), stopped applying the sherut-sadir gender cap to the national-service and
  civilian tracks, and corrected the docstring from Feb to May 2026 rates.
