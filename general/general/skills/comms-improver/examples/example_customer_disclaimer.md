# Worked Example — Customer-Facing Disclaimer

This example demonstrates Comms Improver translating a legal disclaimer into customer-facing plain language. The source is a dense liability disclaimer written by outside counsel; the target is the disclaimer's customer-facing version on the user's product page.

## Input

**Audience:** "Customer-facing — non-technical consumers viewing our product page. They are evaluating whether to purchase. Most will not read the disclaimer carefully but the few who do should not be alienated by legalese."

**Purpose:** "Risk warning — they need to understand that our product makes recommendations, not decisions, and that they're responsible for the underlying decisions."

**Length constraint:** "Short — single paragraph, ideally 3-4 sentences. Will sit at the bottom of the product page."

**Tone:** "Direct and confidence-inspiring. We don't want to scare them off, but we do need them to understand the boundary."

**Preserve specific terms:** not specified, though user notes that the original was drafted by outside counsel and the user wants to verify the rewrite preserves protective effect.

**Original text:**

> "DISCLAIMER. The information, recommendations, and analysis provided through the [Product] (the 'Service') are intended for informational and educational purposes only and do not constitute, and should not be construed as, professional financial, legal, tax, medical, or other advice. Any decisions made by users of the Service in reliance on the information, recommendations, or analysis provided are made at the user's sole discretion and risk, and the Company shall have no liability for any losses, damages, or other adverse consequences resulting from such decisions. Users are strongly encouraged to consult with qualified professionals before making any significant decisions based on information obtained through the Service. The Company makes no representations or warranties as to the accuracy, completeness, reliability, or suitability of the information provided, and the Service is provided on an 'as is' and 'as available' basis. The Company expressly disclaims all warranties, whether express or implied, including without limitation the implied warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the Company be liable for any direct, indirect, incidental, special, consequential, or punitive damages arising out of or in connection with the use of the Service, regardless of the legal theory under which such liability is asserted."

## Output

# Comms Improver: Product Page Disclaimer

**Audience:** Customer-facing — non-technical consumers
**Purpose:** Risk warning — clarify the recommendation/decision boundary
**Length constraint:** Single paragraph, 3-4 sentences
**Tone:** Direct, confidence-inspiring

## Rewritten text

> [Product] gives you recommendations and analysis to help you make better decisions, but the decisions themselves are yours. We don't replace professional advice — for important financial, legal, medical, or tax questions, you should also talk to a qualified professional. We work hard to keep our recommendations accurate and useful, but we can't guarantee them, and you use [Product] at your own risk.

## What was changed

- **Compressed dramatically.** Original: 218 words. Rewrite: 65 words. The customer can read it without giving up.
- **Led with what the product does.** Original led with "DISCLAIMER" in all-caps; rewrite leads with "[Product] gives you recommendations and analysis." The substance comes first; the limitation follows.
- **Translated legal categories to user-relevant categories.** "Professional financial, legal, tax, medical, or other advice" → "professional financial, legal, medical, or tax questions." Same coverage; user-relevant framing.
- **Removed multi-clause warranty disclaimer.** "Makes no representations or warranties as to the accuracy, completeness, reliability, or suitability... 'as is' and 'as available' basis... expressly disclaims all warranties... merchantability, fitness for a particular purpose, and non-infringement" → "we work hard to keep our recommendations accurate and useful, but we can't guarantee them." The "as is" disclaimer is preserved in spirit but expressed as "we can't guarantee them."
- **Removed damages-exclusion sentence entirely.** The "in no event shall the Company be liable for direct, indirect, incidental, special, consequential, or punitive damages" sentence does not appear in the rewrite. This is the most consequential change — see preservation-of-meaning concerns.
- **Tone shift.** Original sounded defensive; rewrite is collaborative ("to help you make better decisions"). Both versions communicate the same boundary, but the rewrite is more likely to retain customer engagement.

## Terms simplified or preserved

- **"Disclaimer" header eliminated.** A header isn't needed for a 65-word disclaimer; it created legal-document framing the rewrite avoided.
- **"Information, recommendations, and analysis"** → "recommendations and analysis." Triple-redundant in the original; "information" is implicit.
- **"At the user's sole discretion and risk"** → "the decisions themselves are yours" + "you use [Product] at your own risk." The two ideas separated for clarity.
- **"Professional financial, legal, tax, medical, or other advice"** → "professional financial, legal, medical, or tax questions." "Advice" became "questions" because customers know to ask professionals about questions, not about advice. The professional categories are preserved.
- **"As is and as available"** → "we can't guarantee them." Common consumer interpretation.
- **"Implied warranties of merchantability, fitness for a particular purpose, and non-infringement"** — eliminated. These are legal terms with specific UCC and common-law meanings; their absence from the rewrite is the preservation-of-meaning concern below.
- **"In no event shall the Company be liable for any direct, indirect, incidental, special, consequential, or punitive damages"** — eliminated. This is the most consequential omission; see preservation-of-meaning concerns.

## Preservation-of-meaning concerns

**Significant — user must verify before publishing.** This rewrite preserves the substance of the disclaimer (we make recommendations, you make decisions, we don't guarantee accuracy, you use at your own risk) but does not include the standard legal language that maximizes protective effect:

1. **The implied warranty disclaimers** ("merchantability, fitness for a particular purpose, non-infringement") are absent from the rewrite. These disclaimers, when properly conspicuous and stated in writing, can be enforceable under UCC §2-316 to limit certain warranty claims. The rewrite's "we can't guarantee them" is a substantive equivalent but may not satisfy the formal "conspicuous" standard required for enforceable disclaimer of implied warranties.

2. **The damages-exclusion clause** ("In no event shall the Company be liable for any direct, indirect, incidental, special, consequential, or punitive damages") is absent from the rewrite. This clause typically operates to exclude broad damage categories that could otherwise be available; without it, the user may face damages claims the original would have foreclosed.

3. **"Strongly encouraged to consult with qualified professionals"** is softened to "you should also talk to a qualified professional." Both versions communicate the recommendation, but the original's "strongly encouraged" carries more weight for showing the user was warned.

**Recommendations for the user:**

- **Outside counsel review.** Since the original was drafted by outside counsel, the user should have the rewrite reviewed by counsel before publishing. Plain-language rewrite for consumer surfaces is a common request; counsel can verify whether the protective effect is preserved or recommend hybrid approaches.
- **Hybrid option.** Many customer-facing surfaces use a "summary" version (like the rewrite) plus a "full disclaimer" link to the original legal language. This gives consumers an accessible version while preserving the formal protective language. Recommend exploring this with counsel.
- **Don't publish without review.** Plain-language rewrites of legal disclaimers can change the legal effect even when they preserve the substantive meaning. The risk is asymmetric: if the rewrite turns out to be less protective, the cost is real; if the rewrite is over-protective, there's no harm.

## Suggested follow-ups

- **If counsel approves the rewrite as written:** publish it with confidence; the calibration is appropriate for the customer-facing context.
- **If counsel wants to add back the warranty disclaimer language:** consider a hybrid: the plain-language paragraph as currently written, plus a separate sentence (perhaps in slightly smaller text or a footnote) reading something like: "[Product] is provided 'as is' without warranty of merchantability, fitness for a particular purpose, or non-infringement, and we do not accept liability for indirect or consequential damages arising from your use."
- **If counsel wants to keep more of the original protective language:** ask which specific clauses are most important to preserve; rewrite again with those clauses intact while still simplifying the rest.
- **If the user wants alternative tones:** more reassuring ("We're confident in our recommendations and want to help you make great decisions, but...") or more direct ("These are recommendations, not advice. You decide. Talk to a pro for big questions.").

---

## What this example demonstrates

- **Customer-facing rewrites compress dramatically.** Original: 218 words. Rewrite: 65 words. The customer reads it; the original gets skipped.
- **Confidence-inspiring tone is achievable.** "Gives you recommendations and analysis to help you make better decisions" is the same substance as "intended for informational and educational purposes only" but reads as collaborative rather than defensive.
- **Preservation-of-meaning concerns are critical and prominently flagged.** The rewrite eliminates two clauses that have specific protective legal effect (implied warranty disclaimer; damages exclusion). This is the most consequential preservation issue we've encountered; the rewrite's "concerns" section is correspondingly long.
- **The user is told not to publish without review.** When the original was drafted by counsel and the rewrite changes potential legal effect, "user verifies" isn't enough — outside counsel review is recommended. The skill's role is to produce the candidate rewrite, not to authorize publication.
- **Hybrid options are surfaced.** Many customer-facing pages use a summary plus a "full disclaimer" link; the rewrite suggests this pattern as a path to combine accessibility with legal protection.
- **The rewrite is candid about its limitations.** Plain-language rewriting of consumer disclaimers is a common request and produces useful drafts, but it's not a substitute for counsel-reviewed protective language. The skill's output reflects this honest scope.
