# Red Flags

This reference drives the red-flag identification in the report. These are issues to flag whenever they appear, calibrated to triage stakes — the question is "does this warrant escalation, negotiation, or pause?" not "is this technically perfect?"

Severity uses the same Critical / Material / Minor structure as MSA Review for consistency, but tier-down for triage:

- **Critical** — the user should escalate to deeper privacy review or pause vendor onboarding pending vendor changes. Not a deal-breaker per se, but warrants stopping the standard procurement flow.
- **Material** — the user should address in the DPA negotiation or as a specific contractual carve-out. Acceptable to proceed with awareness.
- **Minor** — the user should be aware but the issue does not warrant action at the first-pass level.

A clean privacy policy first-pass review surfaces zero or one red flag at material severity. A typical commercial vendor's privacy policy surfaces 2-4 material flags and 0-1 critical. A problematic policy surfaces multiple critical flags.

## Data collection and use

### Catch-all data collection language

Policy collects "any information you provide" or "information about your use" without enumeration of categories.

**Why it's a red flag:** transparency is a baseline privacy principle. A policy that doesn't enumerate categories is not allowing the user to make an informed decision.

**Severity:** material in most contexts; critical in regulated-data contexts (PHI, financial, children's data).

**User action:** request specific category enumeration; verify in DPA that data categories are defined.

### Sensitive data collection without explicit treatment

Policy collects sensitive categories (government IDs, financial accounts, health data, biometrics) without specific consent disclosure or legal-basis discussion.

**Why it's a red flag:** sensitive data has heightened regulatory protections under GDPR, CCPA/CPRA, and other regimes. Bundled treatment with general personal data may not satisfy regulatory requirements.

**Severity:** critical when sensitive data is in scope and not specifically addressed.

**User action:** verify in DPA that sensitive data is handled per applicable regime; request specific consent mechanism if vendor's processing is consent-based.

### Open-ended use rights

Policy uses data for "any purpose related to our business," "internal business purposes," or similar broad language.

**Why it's a red flag:** swallows purpose limitation. Vendor can use data for any purpose the vendor chooses, regardless of what user expected.

**Severity:** material; critical when combined with broad sharing rights or AI/ML training rights.

**User action:** in DPA, narrow vendor's use rights to specific purposes related to the service. Refuse "internal business purposes" language.

### Use for "research and development" without further specification

Policy uses data for "research and development" or "service improvement."

**Why it's a red flag:** may include AI/ML training on customer data. Common drafting move to obscure training practices.

**Severity:** material; critical if vendor's products are AI/ML-powered.

**User action:** ask vendor explicitly whether "research and development" includes ML training; request specific carve-out in DPA.

## Sharing and recipients

### Broad affiliate-sharing without scope limitation

Policy shares with "affiliates" without identifying which affiliates or limiting scope.

**Why it's a red flag:** in large corporate families, affiliates can include hundreds of entities operating under different business models. Sharing with affiliates may include sharing with marketing arms, advertising arms, or affiliate companies with completely different data practices.

**Severity:** material; critical in deals involving sensitive data.

**User action:** request affiliate identification or scope limitation in DPA.

### "Selling" or "sharing" under CCPA without opt-out mechanism

Policy describes practices that constitute "sale" or "sharing" under CCPA's broad definitions, without clear opt-out mechanism.

**Why it's a red flag:** CCPA-applicable vendors must offer opt-out for sale/sharing. Policy that describes sale-like practices without opt-out suggests non-compliance.

**Severity:** critical for vendors with California consumers in scope.

**User action:** verify CCPA compliance posture; if vendor disputes that practices constitute sale/sharing, get the position in writing; consider escalation to privacy counsel if vendor's position seems untenable.

### Sharing with advertising partners

Policy shares with advertising partners, ad networks, or for "personalized advertising."

**Why it's a red flag:** depending on the user's deal with the vendor, this may exceed expected scope. Customer-data sharing with advertising partners often constitutes "sale" under CCPA.

**Severity:** material; can be critical when customer expects vendor to be a service-provider-only relationship.

**User action:** verify with vendor whether advertising-partner sharing is in scope for the user's account; verify CCPA categorization; address in DPA.

### Sale to third parties for monetary consideration

Policy explicitly states data is sold or licensed to third parties.

**Why it's a red flag:** rare in B2B vendor contexts; if present, suggests vendor's business model includes data monetization.

**Severity:** critical in most B2B contexts.

**User action:** clarify with vendor whether sale practices apply to user's account; if yes, escalate.

## AI and ML training (the dominant 2025-2026 issue)

### Vendor uses customer data for ML training without opt-out

Policy explicitly states vendor uses customer data to train AI/ML models, with no opt-out or with impractical opt-out.

**Why it's a red flag:** customer data used for ML training can produce model behavior reflecting customer-specific information; even with anonymization, model weights may encode customer patterns. For B2B vendors, this is increasingly viewed as exceeding the service-provider scope expected by customers.

**Severity:** critical in any context involving non-public customer data; material if data is clearly public-facing.

**User action:** request explicit no-training language in DPA; if vendor's product depends on training, negotiate narrow opt-in with specific scope and IP indemnity for outputs.

### Vendor uses "aggregated and anonymized" data for ML training

Policy reserves rights to use aggregated and anonymized data for ML training "or other purposes."

**Why it's a red flag:** anonymization standards vary. The CCPA's "deidentification" standard is much weaker than GDPR's anonymization standard. Aggregation does not always prevent re-identification.

**Severity:** material; critical if user's data is sensitive or distinctive (e.g., low-volume but highly specific data).

**User action:** verify anonymization standard in DPA; require GDPR-grade anonymization if applicable; consider whether the "or other purposes" language is acceptable.

### AI/ML practices disclosed in a separate "AI Usage Policy"

Privacy policy references but does not contain the AI/ML disclosure; says "see our AI Usage Policy" or similar.

**Why it's a red flag:** the separate document may contain expansive training rights not visible in the privacy policy review. The structure may also indicate vendor's discomfort with disclosing the practices in the main policy.

**Severity:** material until the separate policy is reviewed; severity reassessed after review.

**User action:** request the AI Usage Policy and run this skill on it separately; verify that DPA addresses ML training explicitly.

### Generative AI features described in training rather than inference terms

Policy describes generative AI features (chatbots, content generation, summarization) in language suggesting training on customer prompts and outputs rather than inference-time use only.

**Why it's a red flag:** generative AI use that involves training-time exposure of customer data creates broader risk than inference-time use. Inference-time data is processed and discarded; training-time data is potentially encoded in model weights.

**Severity:** material; critical when customer data is sensitive.

**User action:** clarify with vendor whether AI features involve training-time use of customer data; address in DPA with specific commitments on training vs. inference.

## Retention

### Indefinite retention

Policy retains data indefinitely or "as long as we have a relationship with you."

**Why it's a red flag:** retention without limit accumulates data exposure over time. Most regulatory regimes (GDPR storage limitation principle; CCPA retention disclosure requirements) expect purpose-bounded retention.

**Severity:** material; critical when sensitive data is involved.

**User action:** require specific retention periods in DPA; require deletion mechanism on user request.

### Retention beyond service necessity without clear basis

Policy retains data beyond the service relationship without identifying the basis.

**Why it's a red flag:** retention without basis is not legally sustainable under most regimes. Common legitimate bases (legal-obligation retention for tax/finance; litigation hold; statutory retention) should be identified.

**Severity:** material.

**User action:** clarify retention basis; address in DPA.

### Vague retention language

"We retain data as long as necessary" without further specification.

**Why it's a red flag:** acceptable as a high-level statement but not transparent enough at first pass. Without methodology or periods, user cannot assess.

**Severity:** minor at first pass; material if combined with other retention concerns.

**User action:** request retention schedule in DPA negotiation.

## Cross-border transfers

### Transfers occur but mechanism not disclosed

Policy says data may be transferred internationally but does not identify the transfer mechanism.

**Why it's a red flag:** GDPR requires transfer mechanism (SCCs, adequacy, BCRs, derogations). Policy that doesn't identify mechanism may not be GDPR-compliant.

**Severity:** critical for vendors with EU users.

**User action:** request mechanism identification; verify in DPA that SCCs (or appropriate mechanism) are executed.

### Reference to invalidated transfer mechanism

Policy references Privacy Shield (invalidated July 2020 by Schrems II) or 2010 SCCs (replaced by 2021 SCCs effective December 2022).

**Why it's a red flag:** indicates policy is stale and may not have been updated for current regulatory landscape.

**Severity:** material; critical if no current mechanism is also referenced.

**User action:** confirm with vendor that current mechanisms are in place; verify policy has been updated; flag staleness as broader concern.

### No reference to TIA (Transfer Impact Assessment) for non-adequacy transfers

Policy describes transfers from EU to non-adequacy countries without TIA reference.

**Why it's a red flag:** Schrems II requires supplementary measures supported by TIA for transfers to non-adequacy countries. Absence of TIA reference in vendor's documentation suggests vendor may not have conducted one.

**Severity:** material; critical for transfers to high-risk jurisdictions (e.g., transfers to countries with extensive government access laws).

**User action:** request TIA from vendor; verify supplementary measures are in place; consider whether to require specific contractual protections in DPA.

## User rights

### Rights enumerated without exercise mechanism

Policy lists user rights (access, deletion, etc.) but provides no clear mechanism to exercise them.

**Why it's a red flag:** rights without mechanisms are aspirational. GDPR and CCPA both require functional exercise mechanisms.

**Severity:** material.

**User action:** request exercise mechanism in DPA; verify response-timeline commitment.

### Charges for rights requests

Policy charges for routine rights requests (access, deletion).

**Why it's a red flag:** CCPA prohibits charges for routine requests. GDPR allows charges only for manifestly unfounded or excessive requests.

**Severity:** material; critical in jurisdictions where charges are not permitted.

**User action:** clarify charging policy; ensure DPA prohibits charges for routine requests.

### Vendor reserves discretion on rights requests

Policy says vendor will respond to rights requests "in our sole discretion" or "to the extent we determine appropriate."

**Why it's a red flag:** discretion-based rights responses are inconsistent with the rights themselves. Vendor cannot validly condition statutory rights on its own discretion.

**Severity:** material; critical if combined with broad data uses.

**User action:** require specific commitment in DPA to honor rights consistent with applicable law.

### No timeline for rights responses

Policy enumerates rights without committing to a response timeline.

**Why it's a red flag:** GDPR requires response within one month (extendable to three for complex requests); CCPA requires within 45 days. Vendor without timeline commitment cannot meaningfully meet user's regulatory obligations.

**Severity:** material.

**User action:** require timeline commitment in DPA matching user's regulatory obligations.

## Vague or boilerplate disclosures

### Privacy policy is generic and doesn't reflect the actual service

Policy reads as if it could apply to any service; doesn't reference vendor's specific data practices.

**Why it's a red flag:** suggests vendor used a template without customization; may not accurately describe vendor's practices.

**Severity:** material.

**User action:** ask vendor to describe specific data practices; verify against the policy; consider whether DPA should be more specific.

### Policy uses pronouns and structure inconsistent with B2B context

Policy uses "you" referring to consumer-style relationships when the actual deal is B2B.

**Why it's a red flag:** the policy may not be the right one for the actual relationship. Vendors often have separate policies for end consumers and B2B customers.

**Severity:** minor; material if no B2B-specific policy exists.

**User action:** ask vendor whether a B2B-specific policy exists; if so, request and review.

## Stale or inconsistent policy

### Policy last updated long ago

Policy effective date is more than 18 months old.

**Why it's a red flag:** privacy law has been evolving rapidly; a 2-year-old policy likely doesn't reflect CPRA, EU AI Act, or recent regulatory developments.

**Severity:** material; critical in conjunction with other concerns or in regulated-data contexts.

**User action:** ask vendor when policy was last reviewed; if substantial time has passed, request updated policy or written confirmation that practices reflect current law.

### Inconsistencies with vendor's marketing materials

Policy says one thing about data practices; vendor's marketing materials, sales discussions, or DPA say another.

**Why it's a red flag:** indicates internal inconsistency. Vendor may not have clear practices, or vendor's various functions may not be aligned.

**Severity:** material.

**User action:** raise inconsistency with vendor; obtain alignment or determine which document controls.

### Policy and DPA are inconsistent

Privacy policy describes practices that conflict with the vendor's standard DPA terms.

**Why it's a red flag:** in DPA negotiation, the DPA controls. But the inconsistency suggests the policy is misleading or the DPA is non-standard for the vendor.

**Severity:** material; critical if user is relying on policy representations.

**User action:** identify the inconsistency; ensure the DPA captures the user-favorable terms; consider whether policy needs updating.

## Missing standard sections

### No privacy contact

Policy has no privacy contact information or only a generic support email.

**Why it's a red flag:** baseline transparency expectation; GDPR requires DPO contact in applicable contexts.

**Severity:** material.

**User action:** obtain privacy contact in DPA negotiation.

### No supervisory-authority disclosure (GDPR)

Policy applies to EU users but does not disclose right to complain to supervisory authority.

**Why it's a red flag:** required by GDPR Article 13/14.

**Severity:** material for vendors with EU users.

**User action:** address in DPA; flag broader compliance posture concern.

### No children's data treatment in services that may attract minors

Policy is silent on children's data in services that could plausibly be used by minors.

**Why it's a red flag:** COPPA and similar regimes require specific disclosures for services directed at or knowingly used by children.

**Severity:** material if minors are likely users; minor otherwise.

**User action:** clarify with vendor whether service is directed at or knowingly used by minors; address in DPA.
