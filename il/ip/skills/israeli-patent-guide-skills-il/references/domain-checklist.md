# Domain Coverage Checklist: Israeli Patent Practice

This file is the explicit coverage contract for `israeli-patent-guide`. Every row is either covered by the skill, deliberately out of scope with a stated reason, or logged as a known gap. Re-litigate the "Out of scope" rows on every update cycle: a row that an ordinary user would plausibly ask for, or that has become capturable since the last cycle, must be reopened.

Last reviewed: 2026-09-13 (skill version 1.5.0)


## Covered

| Topic | Where | Notes |
|---|---|---|
| Service inventions, ownership and compensation (ss.132-135) | SKILL.md "Who Owns the Invention" | Added 1.3.0. Includes the Compensation and Royalties Committee. |
| National application requirements, Form P/1, specification structure | SKILL.md "Application Requirements" | |
| Filing languages and translation deadline | SKILL.md "Language" | |
| Address for service for foreign applicants | SKILL.md "Address in Israel" | |
| Continuing duty of disclosure (s.18) | SKILL.md "IDS Duty" and Gotcha 1 | Runs to Notice of Acceptance. |
| Automatic examination queue, no EPO-style request | SKILL.md "Examination is Queued Automatically" and Gotcha 2 | |
| Section 18 Notice prior to Examination, response deadline on the notice, NIS 240/month extensions, deferral | SKILL.md "The Section 18 Notice" | Extension fee NIS 240/month added 1.3.0. |
| Office Action response practice | SKILL.md "Office Action Response Deadlines" | Deliberately does not state a fixed period. |
| Examination backlog statistics | SKILL.md "Current Examination Backlog" | Sourced to ILPO 2024 Annual Report. Check for the 2025 report. |
| Prior art search, ILPO database and international databases | SKILL.md "Prior Art Search" | |
| Absolute novelty, no grace period today | SKILL.md Gotcha 0 | Added 1.3.0. Notes the designs-law asymmetry. |
| Defence-related inventions, secrecy orders, foreign filing permission (ss.94-113) | SKILL.md "Before Filing Abroad" | Added 1.3.0. |
| PCT filing via RO/IL, ISA options | SKILL.md "PCT International Filing from Israel" | |
| PCT national phase entry, 30 months from earliest priority | SKILL.md and references/pct-israel-checklist.md | Israel is 30 months, not 31. |
| PCT Article 19 amendment deadline | scripts/patent-deadlines.py | Fixed 1.5.0 to Rule 46.1 (later of ISR transmittal + 2 months or priority + 16 months). |
| PCT Rule 49.6 reinstatement | SKILL.md Troubleshooting | Sourced 1.5.0: due care, 240 ILS (WIPO IL chapter, 1 Aug 2026). |
| Paris Convention 12-month priority year | SKILL.md and scripts/patent-deadlines.py | |
| Divisional applications | SKILL.md "Divisional Applications" | |
| Accelerated examination, grounds and both fee routes | SKILL.md and references/ilpo-fee-schedule.md | Third-party s.19a(c) route added 1.3.0. |
| Absence of a domestic provisional application | SKILL.md "No True Provisional Application" | |
| Full 2026 official fee schedule | references/ilpo-fee-schedule.md | Every row transcribed from the official notice. |
| The reduction: eligibility, first-application condition, the two fees it covers | SKILL.md, references, and pct-israel-checklist.md | Corrected 1.3.0. |
| Renewal schedule and due dates | SKILL.md, references, scripts | Corrected 1.3.0 to years 6/10/14/18. |
| All-inclusive renewal option (NIS 14,410) | SKILL.md and references | Added 1.3.0. |
| Restoration of a lapsed patent (s.59) | references/ilpo-fee-schedule.md | Fee NIS 841. |
| 3-month opposition period from publication of acceptance (s.30) | SKILL.md "Objection Period" | Anchor corrected 1.5.0 from notice date to publication date. |
| Patent term, 20 years from filing | SKILL.md and scripts | |
| Pharmaceutical PTE: 90-day window, recognized-country linkage, shortest-extension rule, Israel-only route, 5-year and 14-year caps | SKILL.md, references/pte.md | Rewritten 1.5.0 against ss.64A-64Q; the old EU-5 description was wrong. |
| Pending Amendment No. 15 | SKILL.md dedicated section | 13 Sep 2026: tabled for first reading, no committee (Knesset OData). |


## Out of scope (explicit) - re-litigate every cycle

| Topic | Reason | Verdict 2026-08-01 |
|---|---|---|
| Utility models | Israel has no utility model system. Nothing to describe. | **Keep out.** Structurally correct, not a coverage choice. |
| Copyright | No registration system in Israel; copyright arises automatically. Different statute, different advice shape. | **Keep out.** Would not change a filing decision. |
| Trademark registration and prosecution | Different statute (the Trade Marks Ordinance) and different practice. | **REOPEN as routing only.** Same authority, same fee notice, and a founder asking how to protect a new product usually needs a brand mark too. Logged as a gap, not yet implemented. |
| Industrial design registration | Different statute (Designs Law 5777-2017, plus the old Designs Ordinance for pre-2018 registrations). | **REOPEN as routing only.** Designs carry a 12-month grace period where patents do not, so a founder who has already disclosed publicly may still have the design route open. This is a decision the skill currently cannot make for them. Logged as a gap. |
| Plant Breeders' Rights | Administered by a separate authority, not ILPO. | **Keep out.** Genuinely a different body. |
| Integrated Circuits (Protection) Law 5760-1999 | Rarely invoked; no registration procedure at ILPO. | **Keep out** for now, but note it exists if a hardware founder asks about mask works. |
| Litigation, infringement and enforcement strategy | Court practice, not prosecution. Requires litigation counsel. | **Keep out.** Correctly scoped. |
| Patent valuation, licensing and commercial terms | Commercial advice, not procedure. | **Keep out.** |
| Foreign national prosecution outside Israel | Jurisdiction-specific; unbounded scope. | **Keep out**, but the Israel-to-abroad routing decision is a logged gap. |


## Known gaps (logged, not yet implemented)

See `optimization-log.json` for the current cycle's carry list. In summary:

1. Israeli software / business-method examination practice (ss.3-5 and 7 criteria added 1.5.0).
2. A protection-route chooser covering patent, registered design, trademark and trade secret.
3. The Israel-versus-abroad filing strategy decision (direct Paris route versus PCT, cost deferral, what PCT is not).
4. Calculator flags for the Section 18 Notice response deadline and the PCT Chapter II demand deadline.
5. Budapest Treaty biological deposits, relevant given the skill's biotech emphasis.


## Verification anchors

When re-checking this skill, these are the sources to fetch:

- Official fee notice PDF: https://www.gov.il/BlobFolder/news/ilpo-fees/ar/news_fees-2026.pdf (gov.il HTML pages return 403 to automated fetchers; the PDF downloads cleanly and has a text layer)
- Patents Law 5727-1967: https://www.wipo.int/wipolex/en/text/495413 (Hebrew consolidated text: https://www.nevo.co.il/law_html/law01/p187_002.htm)
- WIPO PCT Applicant's Guide, Israel chapter: https://pctlegal.wipo.int/eGuide/view-doc.xhtml?doc-code=IL
- ILPO portal: https://www.gov.il/en/departments/ilpo
