# Tier 1 — Hard false-positive triggers

Tier 1 runs after Tier 0's parse record is complete. Tier 1 uses only what's already in the alert and the parse — no web access.

**At Tier 1, only FP rules can fire.** True-positive determinations are never reached at Tier 1, regardless of how strong the apparent match looks. A 100% upstream match score does not produce a TP at this tier. The reasoning: an upstream match score is a probability, and the skill is deterministic. Strong matches still need Tier 2's structured corroboration before a TP can be called.

A rule fires only when **all** of its preconditions are satisfied. If a precondition fails, the rule is marked `not_applicable` and the next rule is evaluated. Conservative posture: silence over weak inferences.

## FP-1 — Type mismatch

**Preconditions:**
- `listed_party_type` is one of {individual, entity, vessel, aircraft} (not "unknown")
- `screened_party_type` is one of {individual, entity, vessel, aircraft} (not "unknown")
- `screened_party_type_source` is `provided` or `user_confirmed` (not `inferred`)
- The list entry contains no eponymous cross-reference between types (e.g., the listed individual doesn't have a known company named after them that's also on the list with the same name structure)

**Fires when:**
- `listed_party_type` ≠ `screened_party_type`

**Outcome:** FP, cleared

**Audit:** Record both types, both type sources, confirmation that the cross-reference check ran and what it returned.

**Why this rule exists:** A common screening failure is matching a corporate name against an individual on the list (or vice versa) because the name strings happen to overlap. A vessel named "MARIA" matched against an individual named "Maria" on the SDN list is structural noise.

**Why the cross-reference check matters:** Some sanctioned individuals have eponymous entities. If "John Smith" is on the list as an individual AND "John Smith Holdings LLC" is on the list as an entity, then a screened entity called "John Smith Holdings" might be matching the wrong listed entry but is still genuinely sanctioned. Look at the list entry before clearing on type alone.

## FP-2 — Name-role mismatch

**Preconditions:**
- Both names have `parse_confidence: high` in the Tier 0 parse
- Both names map to the same naming convention, or to compatible conventions (e.g., Hispanic and Western-default share enough structure to compare)
- The screened name has been checked against every parsed alias of the listed party (not just the primary listed name)

**Fires when:**
- The overlap between screened name and listed name (or any of its parsed aliases) occurs **only** on non-anchor components
- AND there is no overlap at all on anchor components

**Outcome:** FP, cleared

**Audit:** Record the structural parse of both names, which components overlapped, which didn't, the convention applied, and the alias check confirmation.

**Examples that fire:**
- Screened "Jose Andrea" matched against listed "Jose Andrea Coronado" (Hispanic). Anchor of listed party is "Coronado"; screened name has no "Coronado" component. Overlap is only on given names. FP-2 fires.
- Screened "Wei Zhang" matched against listed "Wei Liu" (East Asian, family-name-first). Anchor of screened is "Wei", anchor of listed is "Wei" — wait, this needs care. In East Asian convention "Wei" is the family name if it appears first, but here both names start with "Wei" so the question is whether Wei is family or given in each. Look at the structural parse. If listed is parsed as family="Liu", given="Wei", and screened is parsed as family="Wei", given="Zhang", the anchors are different (Wei vs Liu). FP-2 fires.

**Examples that do NOT fire:**
- Screened "Maria Garcia Lopez" matched against listed "Maria Garcia Hernandez" (both Hispanic). Anchor of screened is "Garcia", anchor of listed is "Garcia". Anchors match; second surnames differ. This is NOT an FP-2 case — there's anchor overlap. Pass to Tier 2.
- Screened "Jose Andrea" matched against listed "Jose Andrea Coronado", but the listed entry has a documented alias "Jose Andrea" (no surname). The alias check finds the match against the alias, not against the primary listed name. FP-2 does NOT fire because the screened name matches a parsed alias.

**When parse confidence is low:** FP-2 does not fire. Pass silently. The case is escalation-eligible at the end of the pipeline unless a different rule clears it.

## FP-3 — Hard DOB contradiction

**Preconditions:**
- Both parties have a full DOB (day, month, year all present)
- The listed party's DOB inventory has been fully enumerated (some list entries have 5+ alternate DOBs)

**Fires when:**
- The difference between the screened DOB and **every** listed DOB exceeds 2 years
- AND the same-day-and-month carve-out does not apply: the rule does NOT fire if the screened DOB has the same day-and-month as any listed DOB (this preserves the "born on the same day, different year" coincidence pattern, which surfaces in registry-collision cases)

**Outcome:** FP, cleared

**Audit:** Record screened DOB, every listed DOB checked, the exact delta for each, and confirmation that the day-month carve-out was checked.

**Why "every listed DOB":** Sanctioned parties often have multiple DOBs on file because they use false identity documents. A 5-DOB list entry needs to be cleared against all 5 — a match against any one preserves the possibility of TP. The rule fires only when none of the listed DOBs is within range.

**Why the day-month carve-out:** Two people sharing day-and-month-of-birth across years is statistically common in registry collisions and synthetic identities. Treating "same day, different year" as a hard FP would clear real matches. Conservative posture: when day and month match, escalate, don't clear.

**What FP-3 does NOT do:**
- It does not fire on partial DOB mismatch. If the listed party has only a year, or a year range, FP-3 is `not_applicable`. The partial mismatch becomes a soft signal at Tier 2.
- It does not fire on a single mismatched DOB when alternates exist that would match. Always check all listed DOBs.

## Soft signals at Tier 1

Even though no Tier 1 rule fires on them, the following can be observed at this stage:

- **Gender inference mismatch** — when the listed party's name implies a gender and the screened party's name implies a different one. Gender from name is unreliable for unisex names, cross-cultural names, and transliterations.
- **Geographic-footprint mismatch** — when the listed party has a documented narrow geographic footprint and the screened party has no plausible nexus to it.
- **Nationality match or mismatch** — when both sides have nationality. Dual nationals and multi-jurisdiction footprints make this unreliable on its own.

**When a Tier 1 rule fires, soft signals are not surfaced in the output.** They are noise once the case is cleanly disposed of, and including them in the narrative dilutes the disposition. The JSON evidence record does not include soft signal entries when a hard rule fires either — the disposition is complete and the soft signal would only confuse a future reviewer.

Soft signals are surfaced only on escalations, where the analyst needs the full context to decide. In escalation cases, log them in the JSON `soft_signals_logged` field and include them in the narrative's escalation section.

## Exit from Tier 1

- **A Tier 1 rule fired** → output FP determination, stop, produce audit record
- **No Tier 1 rule fired** → proceed to Tier 2

Carry forward into Tier 2: the full parse record, the alert input, every Tier 1 rule's evaluation result (fired / not_applicable / did_not_fire), and any soft signals captured.
