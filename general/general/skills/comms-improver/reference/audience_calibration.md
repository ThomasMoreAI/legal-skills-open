# Audience Calibration

Audience is the most consequential input for transformation. The same legal text rewritten for an executive briefing reads differently than the same text rewritten for the engineering team or for a customer-facing surface. This reference catalogs how to calibrate.

## Executive audiences (CEO, CFO, board)

**What they want:** the bottom line and what to do about it.

**Length:** typically a single paragraph; sometimes a single sentence with a follow-up paragraph if requested.

**Tone:** crisp, businesslike, decision-oriented. Confidence in the conclusion (where warranted) without legal hedging.

**Detail level:** minimum necessary. Save details for follow-up if asked.

**Example transformation:**

*Original:* "Following the Company's review of the proposed Master Services Agreement with Vendor X, we have identified several provisions that warrant negotiation prior to execution. Specifically, the limitation of liability provision (Section 8.1) caps Vendor's liability at the fees paid in the prior six (6) months, which is materially below market for a multi-year enterprise SaaS engagement of this size. Additionally, the customer data license in Section 9.2 contemplates the use of Customer Data for ML training without customer opt-out, which presents data protection concerns and is inconsistent with the Company's data governance posture."

*Plain (executive):* "The proposed contract with Vendor X has two issues that need negotiation before we sign: (1) the liability cap is too low — half of market for a deal of this size; (2) the vendor's standard terms allow them to use our data to train AI models without our opt-out, which conflicts with our data governance approach. We're working with Vendor X to address both. Recommend approving negotiations to proceed and signing only after these items are resolved."

**What changed:** moved from passive bureaucratic ("the Company's review... has identified") to active and concrete ("two issues that need negotiation"); led with the substance, not the process; framed for decision (recommendation at end).

## Operational audiences (sales, engineering, support, marketing)

**What they want:** what they can and can't do; where the boundaries are; what to escalate.

**Length:** typically a few paragraphs; usually with bullet structure for the boundary conditions.

**Tone:** practical and conversational. Direct verbs ("yes you can do X; no you can't do Y").

**Detail level:** enough specifics to act on without ambiguity. Operational owners ask follow-up questions if the rewrite is too high-level.

**Example transformation:**

*Original:* "Pursuant to Section 6 of the customer agreement and applicable data protection laws, Customer Data may be used solely for the purpose of providing the Service and may not be utilized for marketing or advertising purposes without the express prior consent of the Customer."

*Plain (sales):* "Two things you can't do with customer data:

- Use it for marketing campaigns to that customer without their explicit opt-in.
- Share it with our marketing or ad partners.

What you *can* do: use it to deliver the service and support the customer. If you're not sure whether a specific use is on the right side of the line, ask Legal — that's better than guessing."

**What changed:** legal authority citation removed (sales doesn't care about Section 6 references); specific don'ts and dos enumerated; escalation path provided; tone is direct without being preachy.

## Customer-facing audiences

**What they want:** clarity about what affects them. Not legal protection theater.

**Length:** as brief as accuracy allows. Customer-facing text is read by people who didn't ask to read it.

**Tone:** direct, second person ("you can request your data; we'll respond within 30 days"). Avoid "we may" hedge language unless legally required.

**Detail level:** enough to inform; not enough to overwhelm.

**Example transformation:**

*Original:* "In accordance with applicable law, Customer may exercise certain rights with respect to Customer's Personal Information, including without limitation the right of access, the right to deletion, the right to correction, and the right to portability. Such rights may be exercised by submitting a request to our designated privacy contact at privacy@[company]. Requests will be responded to within the timeframes required by applicable law."

*Plain (customer-facing):* "You can request your data, ask us to delete it, correct mistakes, or get a copy in a portable format. To exercise any of these rights, email privacy@[company]. We respond within 30 days for most requests; up to 45 days for complex ones."

**What changed:** "in accordance with applicable law" eliminated (the customer doesn't need to know it's a law-compliance disclosure; they need to know what they can do); rights enumerated as user actions, not abstract categories; specific timelines instead of "applicable timeframes"; "may exercise" → "can." The legal substance is preserved.

**Edge case:** sometimes regulators require specific language in customer-facing notices. The skill flags any language that may need preservation for regulatory compliance ("Notice at Collection" under CCPA; specific GDPR Article 13 disclosures) and the user verifies.

## Deal-team audiences (commercial counsel, product, sales engineers)

**What they want:** the substance of the legal point, in efficient prose. They will see the contract; they need to map the explanation to clauses.

**Length:** matched to the original's substance, not necessarily the original's length. If the original was bloated legal prose, the rewrite is shorter; if the original was already efficient, the rewrite is similar length.

**Tone:** professional but conversational. Less compression than executive briefing; less detail than full legal analysis.

**Detail level:** preserve the legal substance and the structure. Deal-team audiences benefit from understanding the legal scaffolding because it informs negotiation strategy.

**Example transformation:**

*Original:* "Section 7.1 provides that Vendor shall defend, indemnify, and hold harmless Customer against third-party claims that Customer's authorized use of the Service infringes patents, copyrights, or trade secrets. The indemnity is subject to standard exceptions for modification, combination, customer-furnished specifications, and use in violation of the Agreement, and is procedurally conditioned on prompt notice, control of defense, and reasonable cooperation."

*Plain (deal-team):* "The vendor's IP indemnity (Section 7.1) covers third-party claims that the Service infringes patents, copyrights, or trade secrets. Standard exceptions apply: vendor isn't on the hook if customer modified the Service, combined it with non-vendor products, used customer-furnished specs, or used the Service in breach of the agreement. Procedure: customer must give prompt notice, let vendor control the defense, and cooperate. Trademark infringement is not covered — confirm whether that's an issue for our use case."

**What changed:** legal language slightly compressed but the structure and citations preserved; concrete examples for the exceptions ("customer modified the Service"); proactive flag at the end about a gap (no trademark coverage). The deal team can now ask substantive questions about whether the gap matters.

## Engineering audiences

**What they want:** what they need to do (or not do) at the system or feature level; what the technical boundary is.

**Length:** typically focused on the specific feature or system implication, with bullet points for actionable items.

**Tone:** technical-conversational. Engineers respond well to concrete specifications and badly to legal hedging.

**Detail level:** enough to inform technical decisions. Engineers may need to escalate edge cases to Legal; the rewrite should make clear what counts as an edge case.

**Example transformation:**

*Original:* "Pursuant to Article 28(3)(g) of the GDPR and the corresponding provisions of the Data Processing Agreement, Vendor is required to delete or return Customer Personal Data at the conclusion of the engagement. Such deletion shall include all copies of the Personal Data, including those held in backup systems, although deletion from backup systems may occur on a deferred basis consistent with standard backup retention practices, provided that confidentiality obligations continue to apply to such backup-resident data until deletion."

*Plain (engineering):* "When a customer leaves, we delete their data. This includes:

- Active production systems: delete on customer request or within 30 days of termination, whichever is sooner.
- Backups: backup data follows our standard rotation cycle (typically 90 days). Customer data in backups remains protected by the same access controls and confidentiality protections until the rotation completes.
- Audit logs: retained per our standard logging policy (typically 1 year for security audit purposes).

If the customer wants their data returned (rather than deleted), we provide a structured export. Format and delivery method per the export specifications.

Edge cases that need legal review: customer requests for accelerated backup deletion; customer requests for legal-hold-style preservation post-termination; customer disputes about what 'their data' includes."

**What changed:** GDPR / DPA citation removed (engineering doesn't need the legal authority citation); requirements operationalized into specific systems and timelines; edge cases flagged for escalation. Engineering can now build to these requirements.

## Vendor / counterparty audiences

**What they want:** to understand the user's position so they can respond. May not be a lawyer.

**Length:** matched to the substance; usually a paragraph or two.

**Tone:** professional, neutral, businesslike. Not adversarial unless the situation is adversarial.

**Detail level:** enough to communicate the position; not so much that it reads as overstating. Counterparties read between the lines; saying less can sometimes communicate more.

**Edge case:** if the audience is opposing counsel or an adversary, plain-language rewrite is risky — simplification can lose protective hedging. The skill flags this and recommends user verification before sending.

## When the audience is mixed

Sometimes a single rewrite will be read by multiple audiences (an email cc'd to executive plus operational stakeholders). Choices:

- **Default to the highest-level audience.** Executive will get what they need; others can ask for follow-up detail.
- **Provide multiple variants.** Some users want the same content in two forms — one-paragraph for the exec, full version for operations.
- **Layer the content.** Lead with the bottom line; follow with the operational detail. Executive reads the lead and stops; operations continues.

The skill defaults to a single rewrite for the audience the user specified. If the user provides multiple audiences or a layered audience, the skill produces variants.
