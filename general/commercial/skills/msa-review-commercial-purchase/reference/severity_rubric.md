# Severity Rubric

This rubric is shared with MSA Review — SaaS for consistency across the contract-review skill family. The rubric structure is identical; the example calibrations below are tuned for purchase-MSA priorities. (See DE-080 in the project PRD for the planned hoisting of this rubric to shared infrastructure.)

Every issue identified in the review gets one of three severity ratings: **Critical**, **Material**, or **Minor**. The rating drives where the issue appears in the report and how strongly the recommended next steps treat it.

The rubric is calibrated for in-house counsel making business-pragmatic judgments, not for purist drafting standards. An issue is critical because it would change the user's recommendation, not because it is technically imperfect.

## Critical

An issue is critical if any of these are true:

1. **Operationally impossible.** Compliance with the provision would be impossible or would require fundamental changes to how the user's organization operates. Example for purchase MSAs: 24-hour acceptance period for goods that require destructive testing to evaluate; supplier obligation to provide spare parts indefinitely after end-of-production with no minimum order quantity.

2. **Significant unbargained-for risk.** The provision creates substantive risk beyond the deal's stated purpose. Examples: open-ended raw-material price-pass-through with no cap; broad supplier indemnity for buyer's own product-liability claims; buyer's right to revoke acceptance long after receipt without justification.

3. **Eliminates standard protections.** Examples: missing IP infringement indemnification in component-supply MSAs; missing express warranties beyond the UCC implied warranties (often paired with effective UCC §2-316 disclaimer of implied warranties, leaving buyer with no warranty); missing supply-continuity protections in single-source critical-supply deals.

4. **Creates fundamental contractual instability.** Examples: unilateral right to modify all MSA terms or specifications; force majeure that excuses supplier's delivery indefinitely with no termination right; cross-references to specifications, quality agreements, or industry standards not provided or incorporated by reference.

5. **Materially asymmetric in a "mutual" provision.** Mutual indemnity, force majeure, or termination clauses that are structurally one-sided and have substantial financial consequences.

A critical issue, in the recommended next steps, typically warrants: do not sign as-is; negotiate or escalate.

## Material

An issue is material if any of these are true:

1. **Notable departure from standard.** Examples for purchase MSAs: payment terms longer than 60 days net (in industries where 30-45 days is standard); warranty period shorter than 12 months for capital equipment; risk of loss passing to buyer at supplier's loading dock rather than buyer's receiving dock without compensating logistics arrangement.

2. **Operational friction without operational impossibility.** Compliance is possible but creates burden the user should weigh. Examples: short acceptance windows that require buyer to accelerate inspection processes; supplier's audit rights that require operationally significant cooperation; change-order processes that require formal documentation for minor modifications.

3. **Unusual provisions warranting business judgment.** Examples: most-favored-customer pricing; non-compete provisions in design-and-build relationships; raw-material indexed pricing with caps that may be triggered in unusual market conditions.

4. **Asymmetry of moderate magnitude.** Asymmetric provisions in a nominally-mutual MSA where the asymmetry is real but not severe.

5. **Conflicts with disclosed prior agreements.** Provisions that conflict with the user's prior agreements where the conflict is identifiable but resolvable.

6. **Conflicts with the PO / Order Form (when provided).** MSA terms that conflict with the PO — typically the MSA controls per the order-of-precedence provision (in contrast to SaaS MSAs where Order Form often controls), but conflicts should be flagged.

A material issue, in the recommended next steps, typically warrants: negotiate the redline or accept with explicit awareness of the trade-off.

## Minor

An issue is minor if any of these are true:

1. **Drafting cleanliness only.** The provision is acceptable substantively but could be drafted more clearly. Examples: ambiguous notice provisions; missing counterparts clause; minor inconsistencies between clauses.

2. **Departure from preference rather than from standard.** Examples: New York governing law where user prefers Delaware; specific venue selection within a jurisdiction; net 45 payment where user prefers net 30.

3. **Tier 3 issues** (notice mechanics, severability, waiver, counterparts) within standard parameters.

A minor issue, in the recommended next steps, typically warrants: no action required, or accept with awareness.

## How to apply the rubric

When in doubt between two ratings, apply this principle: **rate up to the higher-effort category if the user's reasonable response would be different.** If a "minor" rating would suggest acceptance and a "material" rating would suggest negotiation, and you genuinely think negotiation is the right call, rate material.

Conversely, **rate down to the lower-effort category if escalation is unwarranted.** Critical ratings drive escalation pressure; do not call something critical because it is technically wrong if a competent business judgment could accept it.

Calibration check for commercial purchase MSA review:

- A typical commercial purchase MSA reviewed in good faith from the buyer side will surface 1-3 critical issues (typically warranty / IP indemnity / supply continuity / payment terms), 3-6 material issues, and several minor issues.
- A typical purchase MSA reviewed from the supplier side (where supplier drafted) will surface 0-1 critical issues, 1-3 material issues, and several minor issues.
- Industry-specific overlays (medical device, automotive, aerospace, food/pharma) typically add 1-3 material issues if the MSA does not adequately address industry requirements.
- Single-source critical-supply deals warrant up-rating of supply-continuity findings (an issue that would be material in a multi-supplier commodity context becomes critical in a single-source critical-supply context).

If your review surfaces no critical issues from the buyer side on a supplier-drafted MSA, that is unusual but not impossible — some suppliers (typically those with mature commercial-counsel teams in regulated industries) draft MSAs that are within market on most issues. If unsure, double-check Tier 1 issues for missed problems.

If your review surfaces many critical issues, that is correct for problematic documents — do not soften severity to make the report comfortable.

## Severity is not certainty

A critical rating is a call to action, not a guarantee. The skill is making a probabilistic judgment based on patterns observed across many purchase MSAs. Three implications:

1. **Cite specifically.** Every severity rating should be tied to a specific clause reference so the user can verify the call.

2. **Defer to user expertise on judgment calls.** When severity depends on facts the skill does not have (the user's risk appetite, the supplier's actual operational track record, the strategic importance of the supply relationship, the specific regulatory context), say so.

3. **Calibrate to deal context where provided.** A critical issue in a single-source critical-supply deal may be material in a multi-supplier commodity purchase. The `deal_context` and `goods_or_services` inputs let the user signal which calibration applies; use them.

The user is the decision-maker. The rubric exists to help them prioritize, not to make decisions for them.
