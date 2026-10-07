# Worked Example — Sales Team

This example demonstrates Comms Improver translating a regulatory compliance memo into operational guidance for a sales team. The source is a legal memo on FTC endorsement guidelines; the target is a sales-team Slack-friendly explanation of what reps can and can't say in customer outreach.

## Input

**Audience:** "Sales team — outbound SDRs and AEs who are doing customer outreach. They need to understand what they can and can't say about our customers and case studies. They are not lawyers."

**Purpose:** "Action prompt — they need to update their outreach scripts and stop using a specific case-study claim that we've identified as problematic."

**Length constraint:** "Slack-message length — should fit in a single message without scrolling."

**Tone:** "Practical and direct. They're going to roll their eyes if it sounds preachy or bureaucratic. Friendly but clear about the boundaries."

**Preserve specific terms:** not specified.

**Original text:**

> "TO: Sales Leadership
> FROM: Legal
> RE: FTC Endorsement Guidelines and Customer Testimonial Use
>
> The Federal Trade Commission's revised Endorsement Guidelines (16 CFR Part 255), as updated in 2023, require that any claims about consumer experiences in advertising and marketing communications must reflect the typical experience of consumers under similar circumstances, or otherwise must include a clear and conspicuous disclosure of the atypical nature of the testimonial.
>
> We have identified that certain outbound sales communications include the testimonial 'Customer X reported a 73% reduction in operational costs within 90 days of deployment.' While this testimonial reflects Customer X's actual experience, internal data indicates that this outcome is meaningfully better than typical customer outcomes (where typical results are in the 25-40% reduction range over a 6-12 month timeframe). Continued use of this testimonial without modification creates exposure under the Endorsement Guidelines, particularly given that the FTC has been increasingly active in enforcement.
>
> Sales communications must therefore be modified to either (a) replace the testimonial with one that reflects typical customer experience, or (b) include a disclosure adjacent to the testimonial in clear and conspicuous form indicating that the customer's results are not typical and that typical customer results are in the 25-40% range over 6-12 months. Pending compliance updates, the testimonial should be removed from outbound materials immediately.
>
> Please coordinate with the Marketing team to ensure all customer-facing materials are reviewed for similar issues. We are happy to discuss specific testimonial language."

## Output

# Comms Improver: FTC Endorsement Guidelines Update for Sales Team

**Audience:** Sales team (SDRs, AEs)
**Purpose:** Action prompt — update outreach scripts; stop using a specific claim
**Length constraint:** Slack-message length
**Tone:** Practical and direct, friendly

## Rewritten text

> **Heads up — please update your outreach scripts.**
>
> Stop using this line: *"Customer X reported a 73% reduction in operational costs within 90 days of deployment."* That's a real Customer X result, but it's much better than typical (most customers see 25-40% over 6-12 months). The FTC requires that customer testimonials reflect typical results — so using a best-case story without context can create legal exposure.
>
> What to do:
>
> - **Today:** remove that specific testimonial from your scripts and email templates.
> - **Going forward:** if you want to share customer results, use ranges or use a typical customer story. Examples: "*Customers typically see 25-40% cost reduction over 6-12 months*" or "*Customer Y saw a 35% reduction in 8 months — pretty representative of what we see across our base*."
> - **If you want to use a higher-impact testimonial:** flag it to Marketing and Legal — we can add the right disclosure language so you can use it.
>
> Quick rule of thumb: if a customer story sounds amazing, ask whether it's typical. If not, either find a typical story or check with us before using it.
>
> Questions: ping #legal-team-pls or me directly. Thanks for jumping on this.

## What was changed

- **Led with the action.** Original buried the action ("communications must therefore be modified") in the third paragraph. Rewrite leads with "Stop using this line."
- **Removed legal citations.** "FTC's revised Endorsement Guidelines (16 CFR Part 255)" → "The FTC requires." Sales doesn't need the regulation citation.
- **Translated "exposure" to plain language.** "Creates exposure under the Endorsement Guidelines" → "can create legal exposure." More relatable; preserves the substance.
- **Provided concrete alternatives.** Original told sales what to stop doing but didn't make it easy to figure out what to do instead. Rewrite includes example replacement language sales can use directly.
- **Provided escalation path.** Sales gets a clear "if you want X, do Y" path rather than a blanket prohibition.
- **Conversational structure.** Bold for emphasis, bullets for actions, italics for example quotes. The Slack-friendly format helps comprehension and reads as direct communication rather than corporate memo.
- **Preserved the rule of thumb.** The "if it sounds amazing, ask if it's typical" line gives sales a heuristic they can apply without needing legal review for every testimonial.

## Terms simplified or preserved

- **"FTC Endorsement Guidelines"** → "The FTC." Simplification appropriate; the technical name isn't needed for action.
- **"Clear and conspicuous disclosure"** → "the right disclosure language." Simplification at the cost of legal precision; appropriate for sales audience because Legal will handle the actual disclosure if a higher-impact testimonial is requested.
- **"Atypical"** → "much better than typical." Plain-language equivalent; preserves meaning.
- **"Continued use... creates exposure"** → "can create legal exposure." Plain-language equivalent; preserves meaning.

## Preservation-of-meaning concerns

- **The "quick rule of thumb"** is a heuristic, not a precise statement of FTC standards. The actual FTC standard requires testimonials to reflect typical experience or to include adequate disclosure of atypical results — the heuristic captures this but in a simplified form. For routine sales decisions this is appropriate; for borderline cases, the rewrite directs sales to escalate, which is the right backstop.
- **"Better than typical (most customers see 25-40% over 6-12 months)"** is the user's data. The rewrite assumes this is correct and that the user has internal data supporting it. If the user is uncertain about typical-customer ranges, the rewrite should be revised to use language closer to the original ("internal data indicates...") rather than presenting the range as established fact.
- **"Going forward" examples** ("typically see 25-40%"; "Customer Y saw 35%") use rough ranges without explicit disclosure of variability. For high-stakes claims, even ranges may need disclosures. The rewrite is calibrated for general sales outreach, not for advertising or formal marketing claims; if these examples will appear in advertising, Marketing/Legal review of the specific claim is recommended.

## Suggested follow-ups

- **If sales asks "but Customer X really did get 73% — why can't we use it?":** explain that the FTC's standard isn't whether the claim is true, it's whether it represents typical results. Best-case stories require disclosure, not removal.
- **If sales pushes for a list of "approved" testimonials:** Marketing/Legal can produce a short list of pre-cleared customer quotes for outreach use.
- **If sales asks how to handle prospects who specifically ask about Customer X:** factual response is fine in conversation ("Customer X did see those results — that's outstanding for our category, and most customers see somewhere in the 25-40% range over 6-12 months"). The compliance issue is *advertising* / *outreach claims*, not factual responses to specific questions.
- **For Marketing coordination:** the original memo asked for review of all customer-facing materials. Marketing should run their own review using the same standard; this rewrite covers sales but not marketing materials.

---

## What this example demonstrates

- **Slack-friendly format is achievable for substantive content.** The rewrite is structured for the medium (bold, bullets, examples) without losing substance.
- **Action-orientation is the dominant transformation for operational audiences.** The original's "modifications must be made" became "Stop using this line. Today: remove. Going forward: use ranges. If you want exception: flag." Sales can act without further interpretation.
- **Examples replace abstractions.** "Replace with one that reflects typical customer experience" is abstract. "*Customers typically see 25-40% cost reduction over 6-12 months*" is a usable script line. Sales can copy-paste.
- **Escalation path is operational.** "If you want a higher-impact testimonial, flag it to Marketing and Legal" gives sales a path that doesn't shut down their ability to use compelling stories — it just routes them through review.
- **The rule-of-thumb gives sales decision-making capacity without legal review for every case.** "If it sounds amazing, ask if it's typical" is a memorable heuristic that empowers sales to self-screen.
- **Preservation-of-meaning concerns flag the limits.** The heuristic isn't a substitute for the actual standard; the example numbers depend on user's internal data; advertising claims may need additional review. The user can verify these before sending.
- **Suggested follow-ups address the "what about" questions.** Sales will ask "but really, why?" and "what about prospects who ask?" — preparing for those conversations protects the rewrite's authority.
