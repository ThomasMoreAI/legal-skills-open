# Changelog

## 1.1.0 (2026-08-26)

Correctness release. First review since publication; four statements of law were wrong.

- Schedule item (4) פיתוח חצר was transcribed without its שקיעת מרצפות limb, so sunken floor tiles on the ground floor, in parking, on pavements and on paths were routed to item (2) at two years instead of item (4) at three. The skill also asserted that `floor_ground` exists only in the pre-2011 table, which is the opposite of the statute. Both tables, the script and the checklist corrected; the script now accepts `floor_ground`, `floor_outdoor` and `damp` under the current Schedule and redirects them.
- s.4א(ב) was missing. A hidden אי-התאמה יסודית has its own notice limb with no one-year cut-off, so the skill could tell a claimant with a live 20-year claim that they had missed the deadline. Added to the notice table, the instructions and the script's output.
- The claim that a written demand is a mandatory precondition for a complaint to the Registrar of Contractors was removed from all six places it appeared. The Ministry imposes no such condition; the demand letter is the statutory opportunity to repair under s.4ב(א) and the evidence base, and is still sent first.
- The claim that an individual owner's common-property complaint "will not be accepted" was removed. The Ministry states that any citizen may file and that the house-committee route is recommended, not required.
- Added s.4(א)(1): deviation from the מפרט, an official standard or the building regulations is an independent breach that does not depend on a Schedule row or period.
- Step 0 no longer suspends the notice clock: it now instructs a short dated written notice while an engineer is engaged.
- Added the practical middle of a claim: conduct at the contractor's repair visit, re-inspection, when an engineer's opinion earns its cost, the small-claims track, מומחה מטעם בית המשפט, and עוגמת נפש.
- Limitation (התיישנות) surfaced as a third clock wherever a window end-date is reported.
- Schedule item (7) restored "לרבות גגות קלים עם סיכוך"; noted that s.4(א)(5) says only הקונה, and that s.7א(ב)'s late-delivery limb reaches contracts from 07.07.2022.
- `defect_window.py`: friendly errors for malformed dates instead of a traceback, and a guard against a discovery date earlier than handover.

## 1.0.0 (2026-08-10)

Initial release.

- Room-by-room handover walkthrough checklist and a dated defect log format.
- Both statutory schedules of bedek periods, current and pre-06.04.2011, with the split rule.
- Burden-of-proof analysis across the bedek and warranty periods, and the separate 20-year regime for load-bearing defects (routing only, never classified by the skill).
- The one-year notice duty for defects visible at handover, treated as a clock independent of the defect period.
- Hebrew repair-demand letter template that preserves the statutory opportunity to repair.
- Escalation map covering the Registrar of Contractors route and its limits.
- `scripts/defect_window.py`, a pure-local deterministic window and burden calculator.
