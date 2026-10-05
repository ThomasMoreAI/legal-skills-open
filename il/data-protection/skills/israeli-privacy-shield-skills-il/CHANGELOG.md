# Changelog

## 1.5.1 - 2026-08-13

Rebuilt the Amendment 13 enforcement section against the statute as published in Sefer HaChukim. Statutory damages are Section 15א capped at NIS 10,000, not 'Section 29A' at NIS 50,000-100,000. Administrative fines are per-violation statutory amounts (NIS 150,000 under s.23כו(a), doubled for databases of 1,000,000+ people; NIS 320,000 for specified data-security breaches), not a NIS 1,000-320,000 range doubling to 640,000. The NIS 3.2 million aggregate does not appear in the statute. The 5% of turnover figure is a reduction granted on request, not a headline cap. Both per-person schedules are now stated separately: NIS 50/100 per person approached with a NIS 30,000 floor, and NIS 2/4 per person in the database.

All notable changes to this skill are documented here.

## [1.6.0] - 2026-08-27

### Added

- עמדת הרשות להגנת הפרטיות לגבי משמעות "דיווח מיידי", מתוך העיצום על מאוחדת מיולי 2026: החובה קמה עם היוודע האירוע, המתנה להשלמת הבדיקות מרוקנת את דרישת המיידיות, והדיווח הנדרש הוא דיווח ראשוני שמשלימים אותו אחר כך.
- גילוי הדעת הסופי של הרשות על מינוי ממונה הגנת פרטיות (26 ביולי 2026), כולל התפקידים והכישורים המצטברים הנדרשים.
- שתי פעולות אכיפה חדשות: 256,000 ש"ח על מאוחדת ו-12,000 ש"ח בגין הפרת חובת היידוע לפי סעיף 11.

### Fixed

- `compliance_checker.py` דחה בשקט מפתחות JSON לא מוכרים והחזיר BASIC למאגר שדורש HIGH. הסקריפט דוחה עכשיו מפתח לא מוכר, דורש `record_count`, ובודק טיפוסים.
- SKILL.md חרג ממגבלת 5,000 המילים כבר לפני המחזור הזה; פרטי ממשל ה-AI, מבנה העיצומים ושיטת ה-DPIA הועברו לקובץ העזר.
- תאריך אישור תיקון 13 בכנסת סומן כשנוי במחלוקת ולא מאומת.

## [1.5.0] - 2026-08-09

### Added

- נוסף פרק "הבהרה משפטית" בראש SKILL.md ו-SKILL_HE.md, המפרט מה הכלי עושה, מה הוא אינו, ולאיזה בעל מקצוע מוסמך יש לפנות.

### Changed

- התיאור נפתח כעת בהבהרה קצרה, כך שהיא נראית גם בכרטיס ובתוצאות החיפוש.
