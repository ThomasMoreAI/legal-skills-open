# Policy Topics

This reference defines the 10 standard topics covered in the structured-summary section of the report. For each topic, the reference describes: what to look for in the policy, what "standard" treatment looks like, and what variations matter.

The structured summary covers all 10 topics in order. Topics where the policy is silent are reported explicitly ("Not addressed.") rather than omitted — silence is itself a finding for some topics (see `red_flags.md` for which silences rise to red flags).

## 1. Data collected

**What to look for:** what categories of data the vendor collects; the sources of that data (directly from the user, automatically via cookies/SDKs/tracking, from third parties); whether sensitive categories are included.

**Categories typically disclosed:**
- **Identity:** name, email, phone, account credentials.
- **Profile:** demographics, preferences, interests.
- **Transactional:** purchase history, billing information, transaction data.
- **Behavioral / usage:** clicks, page views, time-on-page, feature engagement.
- **Device and technical:** IP address, browser type, OS, device IDs.
- **Location:** precise (GPS) or coarse (city/region from IP).
- **Communications:** support tickets, chat logs, email content.
- **Sensitive (under various regimes):** government IDs, financial accounts, health data, biometrics, racial/ethnic origin, religious beliefs, sexual orientation, children's data.

**Sources:**
- Direct collection (user-provided).
- Automatic collection (cookies, web beacons, SDKs, server logs).
- Third-party sources (data brokers, social media integrations, advertising partners).

**What "standard" looks like:** clear enumeration of categories collected; clear identification of sources; explicit treatment of sensitive categories (either confirming non-collection or describing handling).

**What's worth noting:**
- Catch-all language ("any information you provide") without enumeration is a transparency concern.
- Categories collected from third-party sources without specific identification.
- Sensitive categories collected without specific consent or legal-basis discussion.
- Inferred-data categories (data derived from raw collection — e.g., interest profiles, demographic predictions) often missing.

## 2. Use of data

**What to look for:** what purposes the vendor uses data for; under GDPR-applicable contexts, the legal basis for each purpose; whether secondary uses (uses beyond the primary service purpose) are disclosed.

**Common purposes:**
- **Service provision:** delivering the product or service.
- **Security and fraud prevention:** detecting and preventing abuse.
- **Customer support:** responding to inquiries.
- **Service improvement:** analyzing usage to improve features.
- **Communications:** transactional emails, service announcements.
- **Marketing:** product marketing, often with opt-out.
- **Legal compliance:** responding to regulatory or legal obligations.
- **AI / ML training:** training models on customer data (the dominant 2025-2026 issue; see `red_flags.md`).
- **Aggregated analytics:** anonymized or aggregated analysis for the vendor's business or for sharing with third parties.

**Legal bases (GDPR contexts):**
- Consent.
- Contract performance.
- Legal obligation.
- Vital interests.
- Public interest.
- Legitimate interests (with balancing test).

**What "standard" looks like:** purposes enumerated with sufficient specificity to allow user to assess whether each purpose is acceptable; legal basis identified for each purpose under GDPR.

**What's worth noting:**
- Open-ended uses ("any purpose related to our business") that swallow the limitation.
- Secondary uses (marketing, analytics, AI training) bundled with primary uses without distinction or opt-out.
- Legitimate-interests legal basis without balancing-test disclosure.
- Use for "research and development" — sometimes a euphemism for ML training.

## 3. Sharing

**What to look for:** categories of third parties data is shared with; whether the vendor "sells" or "shares" personal information under CCPA's broad definitions; sub-processor arrangements.

**Common recipient categories:**
- **Service providers / processors:** parties that process data on behalf of the vendor (cloud hosting, payment processors, customer support tools, analytics services).
- **Affiliates / corporate family:** related entities of the vendor.
- **Advertising partners:** ad networks, ad measurement, retargeting.
- **Business partners:** referral partners, integration partners.
- **Buyers in M&A or asset sale:** typical disclosure for corporate transactions.
- **Government and law enforcement:** in response to legal process or under specified circumstances.
- **At user direction:** sharing initiated by the user (e.g., social sharing, integrations).

**CCPA categorizations:**
- **Sale:** sharing for "monetary or other valuable consideration." Defined broadly under CCPA — a vendor that shares with advertising partners may be "selling."
- **Sharing:** for cross-context behavioral advertising (CPRA-added category, distinct from sale).
- **Service provider** treatment: vendors that process on behalf of the user without "sale" or "sharing" risk.

**What "standard" looks like:** clear enumeration of recipient categories; explicit statement of whether the vendor "sells" or "shares" under CCPA; opt-out mechanism if vendor sells/shares.

**What's worth noting:**
- "We may share with our partners" without specifying the partners' role or category.
- Sale/sharing without opt-out mechanism.
- Affiliate-sharing with no scope limitation (in large corporate families, "affiliates" may include hundreds of entities).
- "We share aggregated information" — verify the aggregation standard.

## 4. Cross-border transfers

**What to look for:** whether the vendor transfers data across borders; the mechanisms used (SCCs, adequacy decisions, BCRs, derogations); recipient countries if disclosed.

**Mechanisms:**
- **EU-US Data Privacy Framework (DPF):** for transfers from EU to DPF-certified US entities.
- **EU SCCs:** Commission Implementing Decision 2021/914 standard contractual clauses.
- **UK IDTA / UK SCC Addendum:** for UK transfers.
- **Adequacy decisions:** EU has decisions for UK, Switzerland, Japan, South Korea, Canada (commercial), Israel, others.
- **Binding Corporate Rules (BCRs):** intragroup transfer mechanism.
- **Derogations under Article 49:** narrow circumstances.

**What "standard" looks like:** disclosure that transfers occur; identification of mechanism (typically SCCs); reference to recipient countries or regions.

**What's worth noting:**
- "We may transfer data internationally" without identifying mechanism.
- Mechanism reference that is stale (e.g., reference to Privacy Shield, which was invalidated by Schrems II in 2020 and replaced by DPF in 2023).
- No reference to mechanism in policies that clearly involve transfers (e.g., US-based vendor with EU customers).

## 5. Retention

**What to look for:** how long the vendor retains data; whether retention is based on purpose-fulfillment or fixed periods; any disclosed retention schedules.

**Common patterns:**
- **Purpose-based retention:** "We retain data for as long as necessary to fulfill the purposes described." Vague but acceptable.
- **Specific retention periods:** "Account data retained for 7 years after account closure for tax and legal purposes."
- **Indefinite retention:** explicit or implicit; usually problematic.
- **Tiered retention:** different periods for different data categories.

**What "standard" looks like:** retention periods or methodology; deletion mechanisms; explanation of retention beyond service necessity (typically legal-obligation-based retention for finance/tax/litigation).

**What's worth noting:**
- "We retain data as long as we need it" without further detail.
- "Indefinitely" or "permanently."
- Retention beyond service termination without clear basis.
- No mention of deletion at user request (under GDPR/CCPA right of erasure / right to delete).

## 6. User rights and exercise mechanisms

**What to look for:** what rights the policy says users have, and how to exercise them.

**Rights typically enumerated:**
- **Access:** right to obtain a copy of personal data held.
- **Correction:** right to correct inaccuracies.
- **Deletion / erasure:** right to delete (with limits for legal-obligation retention).
- **Portability:** right to receive data in machine-readable format.
- **Objection:** right to object to certain processing.
- **Restriction:** right to restrict processing.
- **Opt-out of sale/sharing (CCPA):** right to opt out of sale/sharing.
- **Limit use of sensitive PI (CCPA):** right to limit use of sensitive personal information.
- **Withdraw consent:** right to withdraw consent for consent-based processing.
- **Automated-decision-making:** rights related to automated decision-making (GDPR Art. 22) and profiling.
- **Non-discrimination:** right not to be discriminated against for exercising rights (CCPA).

**What "standard" looks like:** rights enumerated; exercise mechanism specified (email address, web form, account portal); response timeline (typically 30 days for GDPR, 45 days for CCPA).

**What's worth noting:**
- Rights enumerated but no exercise mechanism.
- Exercise mechanism that requires identity verification beyond reasonable.
- Charges for rights requests (CCPA prohibits charges for routine requests; GDPR allows charges only for manifestly unfounded or excessive requests).
- "Sole and exclusive remedy" language for rights requests (legally questionable).
- No timeline commitment.

## 7. Security

**What to look for:** the vendor's stated security commitments. Note: the privacy policy is not a security statement; expect high-level commitments only.

**Common patterns:**
- "We implement industry-standard security measures."
- Reference to specific certifications (SOC 2, ISO 27001).
- Reference to specific safeguards (encryption in transit and at rest; access controls).
- Reference to a separate security exhibit or trust center.

**What "standard" looks like:** brief statement of security commitments; reference to operational security program; ideally, reference to compliance certifications.

**What's worth noting:**
- No security commitments at all.
- Disclaimers like "we cannot guarantee security" without offsetting commitments.
- Vague commitments without specifics or certifications.
- The policy goes into detailed security architecture (privacy policy is not the right place — flag for cross-reference with security exhibit).

## 8. Children's data

**What to look for:** whether the service is directed at children; COPPA disclosures (US, under 13); GDPR-K disclosures (EU, under 16, varies by member state).

**Common patterns:**
- "Our service is not directed at children under 13."
- Specific COPPA compliance disclosures for services directed at children.
- Parental consent mechanisms.
- Different processing for children's data.

**What "standard" looks like:** explicit statement about children's data; if not directed at children, statement to that effect with deletion mechanism for inadvertent collection; if directed at children, specific COPPA/GDPR-K compliance.

**What's worth noting:**
- Silence on children's data in services that may attract minor users.
- Inadequate COPPA compliance for services directed at children.
- No mechanism for parents to request deletion of children's data.

## 9. Contact and complaints

**What to look for:** how to contact the vendor about privacy issues; complaint mechanisms; supervisory-authority disclosure for GDPR.

**Common patterns:**
- Privacy email address.
- DPO (Data Protection Officer) contact for GDPR-applicable contexts.
- EU representative for non-EU vendors with EU users.
- Supervisory authority disclosure (typically with a "you may complain to your local supervisory authority").

**What "standard" looks like:** privacy contact (email or web form); for GDPR-applicable, DPO and EU representative contact; supervisory-authority complaint right.

**What's worth noting:**
- No privacy contact at all.
- General support email as the only privacy contact (privacy contacts should be distinct).
- Missing DPO contact in GDPR-applicable contexts.
- Missing supervisory-authority disclosure.

## 10. AI / ML use of data

**What to look for:** whether the vendor uses customer data for AI/ML model training; how; whether opt-outs exist.

**This is the dominant 2025-2026 issue in privacy policy review.** Vendor practices vary widely:

- **No ML training on customer data.** Increasingly the customer-favored position.
- **ML training on aggregated/anonymized data only.** Common; verify the anonymization standard.
- **ML training on customer data with opt-out.** Acceptable depending on opt-out mechanism quality.
- **ML training on customer data without opt-out.** Critical red flag for non-public data.
- **ML training disclosed in a separate AI usage policy.** Increasingly common; flag and recommend reviewing the separate policy.

**What "standard" looks like:** explicit treatment — either confirmation that customer data is not used for ML training, or disclosure of training practices with opt-out mechanism.

**What's worth noting:**
- Silence on AI/ML use (often means data is being used for training; the policy is just not disclosing).
- Broad "service improvement" or "research and development" language that may include ML training.
- ML training disclosed but no opt-out mechanism.
- ML training opt-out mechanism that is impractical (requires separate request through obscure channel).
- Generative AI features that are described as "training" rather than "inference" (training using customer prompts and outputs creates exposure beyond inference-time use).

## How to write the structured summary

For each topic:

- **2-4 sentences** in the structured summary subsection — this is triage, not deep analysis.
- **Citation** to the specific section/clause of the policy.
- **Plain language** — translate legal/technical language into what it means in practice.
- **Note silence explicitly** — "Not addressed in the policy" is a valid finding for some topics.

If the policy treats a topic comprehensively but in a problematic way, the topic gets a brief structured-summary entry plus a more detailed treatment in the red-flags section. The structured summary describes what the policy says; the red-flags section identifies what's wrong with it.
