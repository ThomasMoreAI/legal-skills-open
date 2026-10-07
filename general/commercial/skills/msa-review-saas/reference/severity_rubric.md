# Severity Rubric

Every issue identified in the review gets one of three severity ratings: **Critical**, **Material**, or **Minor**. The rating drives where the issue appears in the report and how strongly the recommended next steps treat it.

The rubric is calibrated for in-house counsel making business-pragmatic judgments, not for purist drafting standards. An issue is critical because it would change the user's recommendation, not because it is technically imperfect.

## Critical

An issue is critical if any of these are true:

1. **Operationally impossible.** Compliance with the provision would be impossible or would require fundamental changes to how the user's organization operates. Example: suspension without notice in a business-critical service deployment.

2. **Significant unbargained-for risk.** The provision creates substantive risk beyond the deal's stated purpose. Examples: ML training rights on sensitive customer data without opt-out; broad customer indemnity that extends to claims beyond customer's actual conduct; acceleration on uncured material breach combined with broad breach definitions.

3. **Eliminates standard protections.** Examples: missing SLA in a service deal; missing data protection provisions for personal data; missing IP indemnity in a software deal; "AS IS" service warranty with no express commitments.

4. **Creates fundamental contractual instability.** Examples: unilateral right to modify all MSA terms on notice; force majeure that swallows the SLA; cross-references to documents not provided that contain material substantive terms.

5. **Materially asymmetric in a "mutual" provision.** A mutual cap, indemnity, or termination clause that is structurally one-sided is critical when the asymmetry has substantial financial consequences.

A critical issue, in the recommended next steps, typically warrants: do not sign as-is; negotiate or escalate.

## Material

An issue is material if any of these are true:

1. **Notable departure from standard.** The provision deviates from market-standard SaaS MSA practice in a way that creates real but not catastrophic exposure. Examples: 18-month auto-renewal opt-out window (standard is 30-60); cap on liability at 6 months of fees (standard is 12 months); renewal pricing without cap.

2. **Operational friction without operational impossibility.** Compliance is possible but creates burden the user should weigh. Examples: vendor's audit rights of customer with substantial fees; SLA credits with onerous reporting requirements; long cure periods that make termination-for-cause difficult.

3. **Unusual provisions warranting business judgment.** Provisions that are not inherently problematic but are unusual enough to warrant the user's deliberate decision. Examples: most-favored-nation clauses; broad customer-data license for "internal business purposes"; vendor's right to use anonymized customer data.

4. **Asymmetry of moderate magnitude.** Asymmetric provisions in a nominally-mutual MSA where the asymmetry is real but not severe.

5. **Conflicts with disclosed prior agreements.** Provisions that conflict with the user's prior agreements, where the conflict is identifiable but resolvable.

6. **Conflicts with the Order Form (when provided).** MSA terms that conflict with the Order Form — typically Order Form controls per the order-of-precedence provision, but conflicts should be flagged for awareness.

A material issue, in the recommended next steps, typically warrants: negotiate the redline or accept with explicit awareness of the trade-off.

## Minor

An issue is minor if any of these are true:

1. **Drafting cleanliness only.** The provision is acceptable substantively but could be drafted more clearly. Examples: ambiguous notice provisions; missing counterparts clause; minor inconsistencies between clauses.

2. **Departure from preference rather than from standard.** The provision is within the normal range but not the user's first preference. Examples: New York governing law where user prefers Delaware; 99.5% uptime where user prefers 99.9%; net 30 payment where user prefers net 45.

3. **Tier 3 issues** (notice mechanics, severability, waiver, counterparts) that are within standard parameters.

A minor issue, in the recommended next steps, typically warrants: no action required, or accept with awareness.

## How to apply the rubric

When in doubt between two ratings, apply this principle: **rate up to the higher-effort category if the user's reasonable response would be different.** If a "minor" rating would suggest acceptance and a "material" rating would suggest negotiation, and you genuinely think negotiation is the right call, rate material.

Conversely, **rate down to the lower-effort category if escalation is unwarranted.** Critical ratings drive escalation pressure; do not call something critical because it is technically wrong if a competent business judgment could accept it.

Calibration check for SaaS MSA review:

- A typical commercial SaaS MSA reviewed in good faith from the customer side will surface 1-3 critical issues, 3-6 material issues, and several minor issues.
- A typical SaaS MSA reviewed from the vendor side (where vendor drafted) will surface 0-1 critical issues (defects in vendor's own draft), 1-3 material issues (areas where vendor anticipates pushback), and several minor issues.
- A vendor-drafted MSA reviewed from the customer side typically surfaces more issues than a customer-drafted MSA reviewed from the vendor side, because most MSAs in the wild are vendor-favorable by default.

If your review surfaces no critical issues from the customer side on a vendor-drafted MSA, that is unusual but not impossible — some vendors (typically enterprise-focused ones with mature legal teams) draft MSAs that are within market on most issues. If unsure, double-check Tier 1 issues for missed problems.

If your review surfaces many critical issues, that is correct for problematic documents — do not soften severity to make the report comfortable.

## Severity is not certainty

A critical rating is a call to action, not a guarantee. The skill is making a probabilistic judgment based on patterns observed across many MSAs. Three implications:

1. **Cite specifically.** Every severity rating should be tied to a specific clause reference so the user can verify the call.

2. **Defer to user expertise on judgment calls.** When severity depends on facts the skill does not have (the user's risk appetite, the specific deal context, the user's history with this counterparty, the specific data sensitivity), say so. Surface the issue, propose a severity, and note what facts could change the rating.

3. **Calibrate to deal context where provided.** A critical issue in a high-stakes enterprise deal may be material in a small-dollar SMB deal. The `deal_context` input lets the user signal which calibration applies; use it.

The user is the decision-maker. The rubric exists to help them prioritize, not to make decisions for them.
