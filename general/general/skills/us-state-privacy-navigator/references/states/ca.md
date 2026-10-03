# California — CCPA / CPRA

**Citation form**: California Consumer Privacy Act of 2018, as amended by the California Privacy Rights Act of 2020. Codified at Cal. Civ. Code §§ 1798.100 et seq. Implementing regulations at Cal. Code Regs. tit. 11, §§ 7000 et seq. ("CCPA Regs"). Enforced by the California Privacy Protection Agency (CPPA) and the California Attorney General.

> **Drafting note.** When citing in a memo, prefer Cal. Civ. Code §§ 1798.100 et seq. over "CCPA" or "CPRA." California courts and the CPPA refer to the consolidated act, not the original 2018 act and 2020 amendment as separate statutes.

## Applicability

A "business" is subject if it is a for-profit entity that does business in California, alone or jointly determines the purposes and means of processing PI of California consumers, AND meets ANY of the following thresholds (Cal. Civ. Code § 1798.140(d)):

1. Had annual gross revenues in excess of **$25 million** in the preceding calendar year (adjusted to $26.625M effective Jan 2025; confirm current adjustment); OR
2. Annually buys, sells, or shares PI of **100,000 or more consumers or households**; OR
3. Derives **50% or more of its annual revenues from selling or sharing** consumers' PI.

Also covers entities that control, are controlled by, or are joint venturers (≥40% common ownership) with a covered business and process CA PI under shared branding (Cal. Civ. Code § 1798.140(d)(2)–(3)).

**Distinct CA features:**
- Covers **employee, applicant, contractor, and B2B contact** PI. (Other states exclude these.)
- Excludes data covered by HIPAA, GLBA, FCRA, DPPA narrowly (data-level for most categories).
- Non-profits are generally not covered (subject to amendment activity; verify current state).

## Status terminology

- **Business** ≈ controller.
- **Service provider**: processes PI on behalf of the business pursuant to a written contract that limits processing to the business purposes. Most prescriptive contractual constraints (CCPA Regs § 7051).
- **Contractor**: similar to service provider but receives PI from the business for a business purpose; same contractual constraints.
- **Third party**: any entity that is not the business, a service provider, or a contractor. Disclosing PI to a third party for valuable consideration or for cross-context behavioral advertising triggers sale or sharing.

The distinction between service provider/contractor and third party is what determines whether a transfer of PI is a "sale" or "sharing." This is the most consequential drafting decision in any CA-targeted program.

## Consumer rights

| Right | Code section | Notes |
|---|---|---|
| Right to know | § 1798.110 | Categories and specific pieces; verifiable consumer request |
| Right to delete | § 1798.105 | Subject to enumerated exceptions (transactional, legal, security, etc.) |
| Right to correct | § 1798.106 | Added by CPRA (2023) |
| Right to opt out of sale or sharing | § 1798.120 | Includes cross-context behavioral advertising |
| Right to limit use of sensitive PI | § 1798.121 | CA-unique; not opt-in / consent |
| Right to data portability | § 1798.130 | Tied to right to know |
| Right of non-discrimination | § 1798.125 | Limited financial-incentive exception |
| Right re: automated decision-making | § 1798.185(a)(16); CPPA regs | Phased; risk assessments + ADMT regulations finalized 2025 |

Verification standard: "reasonably calculated" to ensure the requester is the consumer about whom the PI relates (CCPA Regs § 7060 et seq.). For sensitive requests (specific pieces, deletion of high-risk data), reasonableness skews toward stricter verification.

## Sensitive personal information

Defined at Cal. Civ. Code § 1798.140(ae). Includes:
- Government identifiers (SSN, driver's license, passport).
- Account login + access credentials.
- Precise geolocation.
- Racial/ethnic origin, religious or philosophical beliefs, union membership.
- Contents of mail, email, text messages (unless the business is the intended recipient).
- Genetic data.
- Biometric data processed for unique ID.
- Health, sex life, or sexual orientation data.
- Citizenship/immigration status.

**Right to limit, not opt-in.** A consumer may direct the business to limit use of sensitive PI to that necessary to perform the services or provide the goods reasonably expected (CCPA Regs § 7027). Covered uses outside the limit require either a notice or fall within enumerated exceptions (security, fraud, legal). The business must provide a "Limit the Use of My Sensitive Personal Information" link on the homepage.

## Sale and sharing

- **Sale**: § 1798.140(ad). Selling, renting, releasing, disclosing, etc., PI for monetary or other valuable consideration to a third party.
- **Sharing**: § 1798.140(ah). Disclosing PI to a third party for cross-context behavioral advertising, whether or not for consideration.

A controller doing third-party retargeting via Meta/Google/TikTok pixels is virtually certain to be sharing PI within § 1798.140(ah). Many such transfers also satisfy "sale" under the "valuable consideration" prong; conservative posture treats them as both.

Required disclosures:
- Privacy policy: categories sold/shared in the past 12 months; categories of third parties; opt-out method.
- Notice-at-collection: that PI may be sold or shared and right to opt out.
- Homepage link: "Do Not Sell or Share My Personal Information."
- Recognition of opt-out preference signals (GPC) per CCPA Regs § 7025.

## Notice-at-collection

CA-unique duty (CCPA Regs § 7012). Must be provided at or before the point of collection, in plain language, accessible from the page where collection occurs. Minimum content:
- Categories of PI to be collected.
- Purposes for which each category will be used.
- Whether PI is sold or shared.
- Retention period for each category, or criteria for determining retention.
- Link to the full privacy policy.
- For sensitive PI: notice of the right to limit and link to the limit-use page.

## Opt-out preference signal (GPC)

Mandatory recognition. Per CCPA Regs § 7025:
- The business shall process the signal as a valid opt-out request without requiring further interaction.
- If the consumer is logged in, apply the opt-out to the consumer's known account, not just the device.
- Where the controller treats the signal as unknown (frequency, ambiguity), apply the opt-out and notify the consumer of the option to revoke.

GPC implementation is a frequent enforcement target. Sephora (2022) was the first major CCPA enforcement action; subsequent CPPA actions have continued to focus on signal recognition gaps. See `references/enforcement.md`.

## Service-provider / contractor contracts

CCPA Regs § 7051. Required terms include:
- Specifying the limited and specified business purposes for which PI is disclosed.
- Prohibiting retention, use, or disclosure of PI outside the direct business relationship.
- Prohibiting combining the business's PI with PI from another source (with narrow exceptions for cross-context behavioral advertising done for the business).
- Requiring the service provider to notify the business if it can no longer comply, and granting the business the right to take steps to remediate.
- Requiring flow-down to subcontractors via written contract with equivalent terms.
- Granting the business audit rights (annual + on-suspicion).
- Requiring deletion or return of PI on termination.

A "service provider" agreement that does not include these terms is at risk of being recharacterized as a "third party" relationship — which makes the disclosure a sale or sharing.

## Risk assessments and automated decision-making (ADMT)

The CPPA finalized regulations in 2025 governing risk assessments, automated decision-making technology (ADMT), and cybersecurity audits. Phased applicability, with full compliance phased through 2027.

Triggering activities include sale/share, processing of sensitive PI, profiling for legal/significant decisions, and use of ADMT in employment, housing, insurance, healthcare, and education contexts.

Required assessment elements: purpose; necessity and proportionality; potential negative impacts; safeguards; consumer expectations; benefits to consumer/business/public.

Practical posture: the CPPA's risk-assessment template is the most prescriptive in the country. Programs covering CA must adopt this depth or risk significant enforcement exposure. Verify current effective dates against CPPA-issued guidance, as the rulemaking has moved.

## Enforcement

- **CPPA** (administrative): may assess civil penalties of up to $2,500 per violation or $7,500 per intentional violation or violation involving a minor's PI. No private right of action for ordinary violations.
- **California AG**: parallel authority.
- **Private right of action** (limited): Cal. Civ. Code § 1798.150 — only for unauthorized access and exfiltration, theft, or disclosure of certain non-encrypted/non-redacted PI as a result of a business's failure to implement reasonable security. Statutory damages $100–$750 per consumer per incident or actual damages, whichever is greater.

**No general cure right post-CPRA.** The 30-day cure right under the original CCPA was removed by CPRA effective Jan 2023. The CPPA may consider good-faith effort in determining penalties.

## Annual disclosures (large-volume businesses)

A business that buys, sells, or shares the PI of 10 million or more consumers in a calendar year must compile and disclose annually metrics about consumer rights requests and processing times (CCPA Regs § 7102).

## Data Broker Registration and DELETE Act

Separate regime. Registration with the CPPA annually, fee-based. The DELETE Act (Senate Bill 362) requires the CPPA to establish an accessible deletion mechanism by January 1, 2026. Brokers must process deletion requests received via that mechanism. Confirm current rollout against CPPA guidance.

## CA-specific drafting considerations

1. **Notice-at-collection** must be distinct from the privacy policy. Many controllers err by linking only to the policy.
2. **Limit-use link** for sensitive PI must be on the homepage. Several enforcement actions have focused on missing links.
3. **GPC handling** must be tested across browsers (Brave, DuckDuckGo, Firefox extensions). A controller relying on a banner CMP without GPC ingestion is non-compliant.
4. **Service-provider language** in vendor MSAs must be updated to reflect CCPA Regs § 7051. Many pre-2023 contracts use legacy CCPA language that no longer satisfies CPRA.
5. **Sensitive PI scope** is broader than under GDPR; include credentials and government IDs.
6. **Employee and B2B notices** are required even though many entities don't think of those constituencies as "consumers" in the colloquial sense.
