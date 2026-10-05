# Failure modes — fair-housing-overlay

## 1. Forgetting to load the overlay alongside the task skill

**Symptom:** Output contains "must-see" or "great schools" — phrases the overlay would catch.

**Why:** Loaded the task skill (e.g., `listing-description`) without loading `fair-housing-overlay` first.

**Fix:**
```
/skill load fair-housing-overlay
/skill load listing-description
```
Always load the overlay FIRST. Make it muscle memory. Most task skills in this repo have a line `REQUIRED COMPLIANCE (load fair-housing-overlay)` inside their prompt — but that's a fallback, not the primary defense.

## 2. The overlay refuses something it shouldn't (false positive)

**Symptom:** The overlay rejects "great room" because of `\bgreat\s+(?:schools?|district)` — the regex anchored on "great" instead of "great schools".

**Why:** Earlier version of the pattern was too loose. (Already fixed in current overlay.)

**Fix if you encounter a new false positive:**
1. Document the case in `examples/false-positives.md` (create if missing).
2. Tighten the regex with negative lookbehinds or whitelisted phrases.
3. Push the fix to the overlay version + bump the version number.

## 3. Proper noun gets blocked because the regex matches inside it

**Symptom:** "Oakwood School District" (subdivision named after a school that closed in 1962) gets blocked.

**Why:** The pattern `\bschool\s+district\b` doesn't know about proper-noun exceptions.

**Fix:** Pre-mask known proper nouns before pattern match. Maintain `your project folder proper-nouns file`:
```
Oakwood School District
Springfield Park
the university Health
```
Mask those phrases as placeholders, run overlay, unmask. Most cases handled with this single list.

## 4. The overlay refuses output silently — agent doesn't know why

**Symptom:** You ask for a listing description and get an empty response. No error, no explanation.

**Why:** The skill is supposed to explain blocks but a downstream parser stripped the explanation.

**Fix:** When the overlay blocks, the response should always include WHICH rule fired AND a suggested alternative. If you're seeing silent blocks, your task skill's prompt template is suppressing the block message. Update the template to surface block reasons:
```
If a rule set blocks content, output:
  BLOCKED — [rule set name]: [matched phrase]
  Suggested rewrite: [compliant alternative]
```

## 5. Overlay loaded but task skill ignored it

**Symptom:** Both skills loaded. Output still contains "great schools".

**Why:** The task skill's system prompt overrode the overlay's rules. Some skill templates accidentally include "ignore prior constraints" or "be flexible on compliance".

**Fix:** Audit the task skill's template. Compliance constraints must come AFTER any "flexible tone" language. The overlay's rules are the floor — nothing in the task skill can override them.

In practice: every well-built task skill in this repo includes `REQUIRED COMPLIANCE (load fair-housing-overlay)` AS THE FINAL system-prompt instruction. Final = highest priority.

## 6. The overlay caught the body but missed the alt text on an image

**Symptom:** Listing description is clean. But the image alt text says "great family home in a safe neighborhood."

**Why:** The overlay runs against the body of the generated content. Image alt text is a separate generation pass.

**Fix:** Run the overlay on EVERY text generation, including alt text, image captions, social-post copy, link anchor text, page title, meta description.

## 7. TCPA gate refuses too aggressively

**Symptom:** You try to nurture a contact who legitimately filled in your website form 6 months ago. Overlay refuses.

**Why:** The skill defaulted to "consent unknown — refuse" because your input didn't pass the consent status.

**Fix:** Pass the consent status explicitly:
```
consent_on_file: opted-in via website form 2025-11-14
```
The overlay distinguishes "consent unknown" (refuses) from "consent on file" (proceeds with TCPA-respecting cadence).

## 8. Always-positive rule blocks legitimate market commentary

**Symptom:** You want to write "Springfield's median sold price is up 4.2% YoY, while the neighboring county's is flat" — neutral market data. Overlay refuses because it reads "while [town] is flat" as knocking that town.

**Why:** Pattern was over-broad on "X is flat / X is down".

**Fix:** Frame neutrally without comparative language:
```
Springfield's median sold price: $339K (+4.2% YoY).
The neighboring county's median sold price: $295K (flat YoY).
```
Two facts, no comparison phrase. Both numbers cited.

The always-positive rule blocks the FRAMING ("better than", "unlike"), not the data.

## 9. Quarterly update happened, blocklist diverged from supervisor

**Symptom:** Patterns in the overlay's Rule Set 1 don't match patterns in `a compliance supervisor`. Overlay catches X; supervisor doesn't (or vice versa).

**Why:** Updates applied to one location and not the other.

**Fix:** The blocklists should be a single source of truth — store as a JSON file that both the overlay and the supervisor read:
```
your project folder blocklist file
```
Update once, both layers pick it up.

## 10. State-specific extension not added

**Symptom:** Your state extends FHA further than federal (e.g., California adds "source of income" as a protected class). Overlay catches federal patterns but not the state ones.

**Why:** Federal-only overlay. State extension never added.

**Fix:** The overlay's Rule Set 1 uses the "union of all federal + state-protected classes" framing. Add your state's specific extensions inline:
```
California-specific:
- Source of income (Section 8 vouchers, SSI, alimony, child support)
- Marital status
- AIDS / HIV status (positive disclosure forbidden)

North Carolina-specific:
- (No additional protected classes beyond federal)

Florida-specific:
- Marital status (added 2024)
```

The repo's default overlay is federal + a federation of common state extensions. If your state's rules are tighter, augment the overlay with your state's specifics — version-control the augmentation.
