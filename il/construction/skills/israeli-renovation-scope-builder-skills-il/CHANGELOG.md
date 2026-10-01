# Changelog

## 1.1.0 (2026-08-27)

Three corrections of law found by an independent expert review, each verified against the primary text before it was written, plus four coverage additions.

- **Cash payments were stated as a flat 6,000 ש"ח cap, and that is wrong in the permissive direction.** סעיף 2 of חוק לצמצום השימוש במזומן triggers on the TRANSACTION PRICE exceeding the Schedule amount, not on the size of the payment, and the definition of "תשלום במזומן" in סעיף 1 carves out only the LOWER of ten percent of the price and the Schedule amount. On an ordinary renovation the ten percent limb binds, so the lawful residue is materially less than 6,000. Because סעיף 2(ג) binds the paying homeowner, and because the skill rightly stresses that, the old flat figure turned the skill's own emphasis into an instruction to overpay in cash.
- **The dispute-forum table over-read סעיף 72(א).** It sent a neighbour's cracked-wall claim to the מפקח על רישום המקרקעין and warned that small claims would dismiss it for want of jurisdiction. סעיף 72(א) reaches disputes about rights or duties under the תקנון or under the sections it enumerates, and a tort claim for damage caused by the works is not among them: it goes to court, where small claims may well be open. סעיף 72(ב) is לפי בחירתו, an option and never a compulsory forum. The table now splits the two cases and the matching Gotcha was rewritten.
- **חוק החוזים האחידים was absent entirely**, although the skill drafts standard terms for a tradesperson to issue to clients and three of those clauses sit inside the סעיף 4 presumptions of קיפוח (4(1) liability cap, 4(2) unreasonable suspension right, 4(6א) agreed compensation in the supplier's favour), with סעיף 5(א) and 5(ב) void outright. Now stated to BOTH sides: a warning to the tradesperson, a defence for the homeowner.
- Added: ערבות ביצוע / ערבות בדק as an alternative to a cash retention, with the point that its term must outlast the longest per-trade warranty; naming the מבצע בניה and who appoints the מנהל עבודה; a parallel complaint route to רשם הקבלנים that neither replaces nor prejudices a money claim; and the פרק א general preconditions that make every exemption conditional, so "exempt" is never answered without the rider.

### Sourcing corrections

- Small claims ceiling: the 39,900 ש"ח figure was attributed to "the statute's own text" (`נוסח החוק`). It is not statutory text. The statute enacts 30,000 ש"ח index-linked, and 39,900 comes from the Justice Minister's annual notice under סעיף 2(ג) of צו בתי המשפט (שינוי סכום התביעה בתביעות קטנות), התשס"ח-2008, published in י"פ התשפ"ו עמ' 3641. The figure is correct and unchanged; the attribution now names the instrument that fixes it, and evidence.json carries the notice itself as a primary source.
- Construction-waste container: removed an uncited proposition that the fine for placing a `מכולה` on a public road without a permit falls on the property owner rather than on the contractor. Who bears it is a matter of the local `חוק עזר` and varies between authorities, so the skill now says that rather than allocating liability.

## 1.0.0 (2026-08-11)

Initial release.

- Scope-of-work builder (כתב כמויות פשוט) with a six-column line format and a mandatory Excluded column, plus a trade checklist so a scope cannot silently omit a trade.
- Milestone payment schedule tied to verified completion rather than to dates, with a retention anchored in the deduct-and-self-cure remedy of סעיף 4 to make it collectable.
- The correct legal frame: a renovation is a חוזה קבלנות, a dispositive statute carrying NO warranty schedule of its own. The בדק periods that dominate Hebrew search results come from חוק המכר (דירות) and govern a new apartment from a developer, not a renovation.
- Permit gate built on סעיף 145(א)(2), which requires a permit for "וכל תיקון בו", with all five statutory conditions of the שינוי פנימי carve-out enumerated separately so a job can be tested against each.
- Exempt-work conditions read from the regulations rather than summarised: סורגים (ת"י 1635 plus an escape-opening bar, notice to the licensing authority AND the fire authority), מצללה (50 sq m or a quarter of the free area, whichever is larger, and a 40 percent gap definition that disqualifies a solid roof), מזגן (60,000 BTU, and no notice duty).
- Both limbs of the קבלן רשום rule: the indexed monetary threshold with its as-of date and the 1 January indexation mechanism, and the separate limb making any work touching the שלד require a registered contractor at any value.
- Two distinct noise cut-offs, 20:00 for renovation work under תקנה 4 and 19:00 for machinery under תקנה 5, both binding whoever permits the work, so the homeowner is exposed and not only the tradesperson.
- Electrical licensing grades, and the rule that a בודק may not inspect work he both designed and executed, so the certificate is required contractually rather than on a claimed statutory duty that could not be located.
- Payment-regime branch on who is paying: חוק מוסר תשלומים לספקים does not reach a private homeowner, but does reach a business payer.
- Drafted from both sides, with the tradesperson's legitimate protections (mobilisation, price escalation, access relief, the סעיף 5 lien) written in rather than omitted.
- Optional `scripts/payment_schedule.py`, pure local arithmetic with no default split, that checks the schedule closes at one hundred percent and that the retention survives handover. Every check it performs is also stated inline for agents that cannot run scripts.
- Correction carried in the skill because renovation guides assert the opposite: there is no 14-day consumer right to cancel a renovation engagement.
- Counterparty identification (ת.ז. / ח.פ.), a personal guarantee where the contractor is a company, and checking that a פנקס הקבלנים registration is current rather than merely present.
- The cash-payment cap under חוק לצמצום השימוש במזומן, which binds the paying homeowner and not only the tradesperson, and the post-dated-cheque trap that otherwise defeats the retention.
- A named milestone verifier, a termination clause, a suspension-for-non-payment clause, and an indemnity distinct from insurance.
- A chronological pre-payment sequence naming the four irreversible moments, including first-fix photography and the flood test that must be witnessed before tiling rather than requested at handover.
- Correct dispute routing: owner-versus-owner disputes in a בית משותף go to the מפקח על רישום המקרקעין under סעיף 72(א), not to small claims, which is individual-only and capped.
- The two distinct common-property majorities kept apart: unanimity for הצמדה under סעיף 62(א), three quarters and two thirds for הרחבה building under סעיף 71ב.
- Gas added to the trade checklist as licensed work under חוק הגז.
