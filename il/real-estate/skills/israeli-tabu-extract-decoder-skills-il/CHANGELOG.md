# Changelog

## 1.2.0 (2026-09-19)

- Added how to order an extract (the registry's `מקרקעין ברשת` site), the three extract types (full, historical, consolidated), the rule that the online extract is an original only in digital form, and the 2026 fees: 18 NIS electronic, 88 NIS certified paper, 154 NIS paper consolidated, indexed every 1 January. The service page and the fee schedule were read first-hand this cycle, which reverses the 1.0.0 decision to state no fee.
- Inheritance entries: a completed ירושה or צוואה transfer line (heirs already registered) is now distinguished from a deceased owner still registered while the seller holds only a court order, where the inheritance must be registered first (s.7).
- Caveats: read who the beneficiary is, and how a caveat comes off (s.132(a): court order, or the Registrar satisfied of consent or a lapsed ground).
- Statute corrections: the consent note blocks under s.131, not s.128; the s.127(b) carve-out is limited to bankruptcy or winding-up avoidance; s.125(a) "conclusive" is subject to ss.93-97 of the Settlement Ordinance; the hundredths rule in s.57(a) is statutory, not practice; balconies and external walls are excluded from the floor area (s.57(b)). Capacity (s.129) and court-order (s.130) notes are now named.
- The "printout official?" troubleshooting row now answers from the registry's own rule.

## 1.1.0 (2026-08-11)

- Added Step 0a: order your own extract, re-check before every payment, and register a הערת אזהרה in your own favour early. Flags a caveat already registered for a DIFFERENT buyer as the clearest double-sale signal on the page.
- Added Step 6b: what the extract does NOT contain, and where that risk actually lives (רשם המשכונות, רשם החברות, תיק בניין, and the שבח / ארנונה / היטל השבחה / ועד clearances that gate registration), plus the מכתב כוונות mechanism for a mortgage discharged at closing.
- Added a protective stop-language carve-out to Step 6. Refusing a verdict on title does not mean refusing to say "stop before moving money", which is a caution about sequence.
- Added an evidence claim for `סעיף 55(ג)` and the never-attachable common-property list.
- The `הערת אזהרה` table row now keeps the operative condition (protection runs while the caveat stands unerased), and `הצמדה` is re-attributed to `סעיף 55(ג)` with the requirement to check the bay against the תשריט in the צו רישום בית משותף.
- The domain checklist no longer calls the property-activity alert service free or ranks it against other precautions; neither could be verified first-hand.

## 1.0.1 (2026-08-11)

- Added the missing `SKILL_HE.md`. The initial release shipped without it, so the sync pipeline fell back to the English body for `content_he` and the entire Hebrew page, including the legal notice, rendered in English. The Hebrew companion is now a full translation with the notice under `## הבהרה משפטית` immediately after the H1, which is what the site's legal-notice component looks for.

## 1.0.0 (2026-08-11)

Initial release.

- Line-by-line decoding of a land registry extract, with every entry type given its category meaning: ownership shares, long leases, ranked mortgages, attachments, caveats, consent-required notes, easements, and attachments of common property.
- The evidential question first: an extract is conclusive evidence for settled land and only prima facie evidence otherwise, so the same document does not prove the same thing everywhere.
- The caveat explained precisely, including the blocking effect, the shield against later attachment and insolvency, the avoidance carve-out most summaries drop, and the fact that it is not ownership.
- The mortgage-rank trap: a redeemed rank can be refilled by a later mortgage, so a discharge does not by itself free rank one.
- Condominium shares computed as a floor-area ratio in hundredths, and registered bylaws binding later owners, so a promised parking space belongs to the unit only if the register says so.
- The registration regimes treated as a core output rather than an edge case, because a large share of Israeli homes are not registered in the owner's name and the user's real question is often which document they should be holding instead.
- A hard refusal boundary: the skill lists what is recorded and what to ask about, and never concludes that title is good or that it is safe to sign.
- Deliberately states no extract fee and no ordering procedure. The government service pages carrying those details could not be read first-hand, and repeating unverified figures in a domain full of stale ones was judged worse than routing the user to the registry.
