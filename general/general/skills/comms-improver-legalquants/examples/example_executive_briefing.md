# Worked Example — Executive Briefing

This example demonstrates Comms Improver translating a contract review summary into executive-briefing format. The source text is a detailed in-house counsel summary; the target is a one-paragraph readout for the CEO and CFO.

## Input

**Audience:** "Executive briefing for CEO and CFO; one-paragraph version. They need to understand the issue and make an approval decision; they're not going to read the underlying contract."

**Purpose:** "Decision input — they need to decide whether to approve negotiation terms before we sign the deal."

**Length constraint:** "One paragraph."

**Tone:** "Crisp businesslike; confident in the recommendation."

**Preserve specific terms:** not specified.

**Original text:**

> "Following Legal's review of the proposed Master Services Agreement with Vendor X (the 'Agreement'), we have identified six provisions that warrant negotiation prior to execution. The most consequential is Section 9.2, which provides Vendor with a license to use Customer Data for 'internal business purposes including without limitation product improvement, training of artificial intelligence and machine learning models, security analytics, and benchmarking,' without a customer opt-out. This is materially inconsistent with the Company's data governance posture, which prohibits ML training on Company data absent specific business case approval. Additionally, the limitation of liability provision (Section 8.1) caps Vendor's aggregate liability at the fees paid in the prior six (6)-month period, which is approximately half of the market-standard 12-month cap for an enterprise SaaS engagement of this size and is below the 12-month minimum that the Company's contract review standards specify for vendors processing Company personal information. The remaining four provisions involve issues of moderate severity that are appropriate for resolution through standard negotiation. Legal recommends that the Company proceed to negotiation with Vendor X but condition execution of the Agreement on resolution of the §9.2 ML training issue and the §8.1 liability cap issue. If Vendor X is unable to address either of these issues, Legal recommends that the Company decline to proceed with the engagement. Our negotiation timeline targets execution within four (4) weeks; if material progress is not achieved within two (2) weeks, we will reassess timing and counterparty fit."

## Output

# Comms Improver: Vendor X MSA Review for Executive Approval

**Audience:** Executive briefing for CEO and CFO; one-paragraph version
**Purpose:** Decision input
**Length constraint:** One paragraph
**Tone:** Crisp businesslike, confident

## Rewritten text

> Vendor X's proposed contract has two issues we need resolved before signing. First, their standard terms let them use our data to train AI models with no opt-out — that conflicts with our data governance policy, which doesn't allow this without specific approval. Second, their liability cap is half of market for a deal this size and below our internal minimum for vendors handling our data. Four other issues are moderate and resolvable in normal negotiation. Recommendation: proceed to negotiation, sign only if both critical issues are resolved, decline if Vendor X won't address either. We're targeting execution in four weeks; we'll reassess at the two-week mark.

## What was changed

- **Led with the bottom line:** the CEO/CFO sees the substance ("two issues we need resolved") in the first sentence, not after process narration.
- **Compressed legal substance:** "Section 9.2 provides Vendor with a license to use Customer Data for 'internal business purposes including without limitation...'" → "their standard terms let them use our data to train AI models with no opt-out." The detailed clause language was unnecessary at executive level.
- **Quantified the liability cap concern in business terms:** "approximately half of the market-standard 12-month cap" became "half of market for a deal this size." The market-standard reference is preserved; the precise duration figures are dropped.
- **Removed legal citations:** "Section 9.2," "Section 8.1," "Master Services Agreement (the 'Agreement')" — all eliminated. The CEO/CFO does not need clause references.
- **Decision framing in active voice:** "Legal recommends that the Company proceed to negotiation" → "Recommendation: proceed to negotiation." Crisp and direct.
- **Maintained the conditional structure on negotiation:** "sign only if both critical issues are resolved, decline if Vendor X won't address either" preserves the binary path Legal proposed.

## Terms simplified or preserved

- **"Customer Data"** (defined contract term) → "our data." Simplification appropriate for executive audience that won't see the contract.
- **"Limitation of liability"** → "liability cap." Common shorthand; preserves meaning.
- **"Master Services Agreement"** → "contract." Appropriate for executive audience.
- **"Material" / "materially inconsistent"** → "conflicts." Simplification appropriate; "material" is a legal term but at executive level the substantive point is the conflict, not the legal characterization.

If the user wants to preserve specific terms (e.g., for contract reference), the rewrite would have included them. The current rewrite trades term-preservation for executive accessibility, consistent with the audience.

## Preservation-of-meaning concerns

- **Compression of "ML training rights" to "use our data to train AI models with no opt-out":** the original specified the broader uses (product improvement, security analytics, benchmarking) before getting to ML training. The rewrite focuses on ML training as the headline because ML training is the dominant 2025-2026 issue and likely the executive concern. The other uses are not explicitly called out. If the executive is going to act on this rewrite, the user should verify that ML training is in fact the headline issue rather than the other uses.
- **"Below our internal minimum"** is a paraphrase of "below the 12-month minimum that the Company's contract review standards specify." The rewrite assumes the executives know about the internal contract review standards or will accept the reference. If executives don't know about the standards, this language could prompt a follow-up question.

## Suggested follow-ups

- **If the executives ask "what specifically would we negotiate?":** Legal can provide the specific language asks (require explicit no-training language; raise cap to 12 months).
- **If the executives ask about the four "moderate" issues:** Legal can provide a short list with one-line descriptions.
- **If the executives push back on the recommendation to walk if issues aren't resolved:** be ready with the cost-benefit framing for proceeding without resolution (deal value vs. data governance breach risk vs. liability exposure).
- **If a shorter version is needed (single sentence):** "Vendor X's contract has two issues — ML training on our data and a too-low liability cap — that need negotiation; we recommend proceeding only if both are resolved."

---

## What this example demonstrates

- **Length transformation is dramatic for executive audiences.** Original: 290 words. Rewrite: 100 words. The executive gets the same substance in one-third the length.
- **Legal scaffolding is removed for executive audience.** Section references, formal contract names, "Legal recommends that the Company proceed" — all eliminated. The executive doesn't need to know which clauses; they need to know what the issues are and what to do.
- **Quantification preserved where it matters.** "Half of market" preserves the substance of the liability cap concern; "below our internal minimum" preserves the policy violation. Specific dollar amounts or duration figures aren't needed at executive level.
- **The recommendation is preserved structurally.** "Proceed if resolved, decline if not" is the same conditional Legal proposed in the original. The executive can act on the same conditional logic.
- **Preservation-of-meaning concerns are surfaced.** The compression of "ML training plus other uses" to just "ML training" is flagged so the user can verify the headline framing matches their intent.
- **Suggested follow-ups anticipate executive reactions.** What if they ask about specific negotiation positions, what if they ask about the moderate issues, what if they push back on walking — the user is prepared with extension content rather than caught flat-footed.
- **A shorter alternative is offered.** Some executive audiences want even more compression; the suggested follow-up provides a single-sentence version.
