# Tier 2 — Structured identifier corroboration

Tier 2 is the first tier where true-positive determinations are reachable. It uses identifiers and structured fields already present in the alert and listed entry — no web access.

A rule fires only when **all** of its preconditions are met. Conservative posture: silence over weak inferences.

## TP-1 — Unique government identifier match

**Preconditions:**
- The same identifier type exists on both sides (passport, national ID, tax ID, registration number for entities, IMO number for vessels)
- The anchor-component name match is satisfied — i.e., the anchors in the parsed names overlap (this prevents a TP-1 firing on a clerical identifier collision between two unrelated people)
- The identifier values have been normalized (trim whitespace, uppercase, remove separators like dashes and slashes) on both sides

**Fires when:**
- The normalized identifier values match exactly

**Outcome:** TP, confirmed

**Audit:** Record the identifier type, both raw and normalized values, the anchor match confirmation, and which listed party identifier (primary or alternate) matched.

**Strictness note:** This rule does not fire on documented format variants (e.g., legacy 7-digit Iranian passports that were re-issued as 9-digit). Strict exact-after-normalization only. Format variants fall to Tier 3 if they're going to be resolved at all.

## TP-2 — Full identity triangulation

**Preconditions:**
- Full DOB present on both sides (day, month, year)
- Place of birth present on both sides with city-level granularity (city + country, not country alone)
- Full anchor-name match per Tier 0 parse — every anchor component on the screened side has a matching component on the listed side (and vice versa for cases where the screened side has a single anchor and the listed side has more, this is still a valid match if the screened anchor appears in the listed anchors)

**Fires when:**
- DOB matches exactly against any listed DOB
- POB city matches (exact city-name match, OR documented equivalent name per `place-name-equivalences.md` — e.g., "Leningrad" on one side and "St. Petersburg" on the other count as a city match because the equivalence is documented; political-entity differences like USSR vs. Russia are context, not a different place)
- Anchor names match

**Outcome:** TP, confirmed

**Audit:** Record each of the three components: DOB match (which listed DOB matched, exact comparison), POB match (city and country, equivalence applied if relevant), anchor name match (the parsed components on each side).

## Escalate-2 — Partial triangulation, anchor name intact

**Preconditions:**
- Full DOB match on at least one listed DOB
- Full anchor-name match
- POB available on both sides but only at **country level** on at least one side (city missing from one or both)

**Fires when:**
- Anchor names match AND DOB matches AND POB country matches, but city-level POB confirmation is not available

**Outcome:** Escalate (this is not a TP and not an FP — it's a strong signal that the case warrants human attention)

**Audit:** Record what matched, and explicitly note that country-only POB was the gating reason for escalation rather than TP.

**Why this rule exists:** Country-of-birth among populations of 80M+ people isn't unique enough to support TP deterministically. But anchor name + full DOB + country POB is too strong to dismiss. Escalation is the right call.

## FP-5 — Identifier mismatch on a unique field

**Preconditions:**
- The same identifier type exists on both sides (passport, national ID, tax ID)
- The listed party has fewer than 3 alternate identifiers of that type (3+ alternates indicates an evasion-pattern target where mismatch on any single one doesn't exonerate)
- The identifier has been normalized on both sides

**Fires when:**
- The screened party's normalized identifier value matches **none** of the listed party's normalized identifier values of that type

**Outcome:** FP, cleared

**Audit:** Identifier type, screened value (normalized), all listed values (normalized) checked, confirmation of no match, count of listed alternates.

**Why the 3+ alternate threshold:** Major SDN evasion targets often carry 4–8 passport entries from different identities. A screened passport that matches none of 4 listed passports is weak FP evidence — the target might be using a 5th. But against an ordinary list entry with one or two identifiers, a clean mismatch is strong FP evidence.

## FP-6 — Anchor failure despite DOB match

**Preconditions:**
- Full DOB on both sides
- DOB matches exactly against some listed DOB
- Both names have `parse_confidence: high` in Tier 0
- The non-matching anchor component on either side is unambiguously different — not a transliteration variant (Mohammed vs. Muhammad doesn't count as different) and not a documented alias of the listed party

**Fires when:**
- Name overlap is on a single component only (a given name OR an anchor component, not both)
- AND the other anchor component is clearly a different name (Garcia vs. Hernandez, Smith vs. Jones)

**Outcome:** FP, cleared

**Audit:** The parse trail (which component matched, which didn't), confirmation that the differing component isn't a transliteration variant or alias, the matched DOB, and the explicit names being compared.

**Why this rule exists:** Same-DOB coincidence is common — within any cohort of a few thousand people, multiple share a birthday by year. DOB-plus-half-a-name is not sufficient for TP and, when the other half is unambiguously a different name, it's strong evidence of FP. The rule is narrowly drawn (high-confidence parses both sides, no transliteration ambiguity, no alias coverage) so it doesn't sweep up real matches.

**What FP-6 does NOT do:**
- Does not fire when the differing component might be a transliteration of the same source name (covered in `transliteration-variants.md`).
- Does not fire when the differing component is a documented alias of the listed party.
- Does not fire when parse confidence is low on either name.

## Soft signals at Tier 2

The following may be observed at Tier 2 but never drive determinations:

- **Gender inference mismatch** — same as Tier 1.
- **Geographic-footprint mismatch** — same as Tier 1.
- **Partial DOB mismatch** — when one or both DOBs are partial (year-only, year-range, "circa") and the visible portions differ. FP-3 doesn't fire on partial; the mismatch becomes a soft signal here.
- **Nationality match or mismatch** — both directions possible. Dual nationals and corporate multi-jurisdiction footprints make this unreliable.
- **Occupation/role mismatch** — when both sides have documented occupation or role incompatible at the time of the alert.

**Surface soft signals only on escalation.** When a Tier 2 rule fires cleanly (TP-1, TP-2, FP-5, FP-6), soft signals are not included in the narrative or the JSON `soft_signals_logged` field. The disposition is complete; soft signals are noise.

The Escalate-2 outcome is itself an escalation — soft signals collected during Tier 2 evaluation are included in the output record because the case is being handed off.

## Exit from Tier 2

- **A TP rule fired (TP-1 or TP-2)** → output TP determination, stop, produce audit record
- **An FP rule fired (FP-5 or FP-6)** → output FP determination, stop, produce audit record
- **Escalate-2 fired** → output escalation record, stop (do not proceed to Tier 3 — Escalate-2 explicitly says human attention is warranted)
- **No rule fired AND Tier 3 gating is satisfied** → proceed to Tier 3
- **No rule fired AND Tier 3 gating is not satisfied** → output escalation record, stop

The Tier 3 gating criteria are in `tier-3-research.md`. The decision whether to enter Tier 3 happens at the boundary between Tier 2 and Tier 3, not inside Tier 2.

Carry forward into Tier 3 (if entered): the full parse record, the alert input, every Tier 1 and Tier 2 rule's evaluation result, and all soft signals captured.
