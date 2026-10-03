# Status Determination — Controller / Processor / Third Party

**Purpose.** Status (controller vs. processor vs. third party) drives every downstream obligation under US state privacy law. The same entity may be a controller for one data flow and a processor for another. Misclassification is one of the most consequential errors in privacy work product because it cascades through every conclusion that follows. This workflow runs the determination per data flow with citations and decision-tree logic.

> **Why this exists as a dedicated workflow.** In the original SKILL.md, status determination was a single table in the memo template. That treatment is inadequate. Real engagements involve dual-status entities (a SaaS controller-of-its-marketing-data and processor-of-customer-end-user-data), tri-status arrangements (advertising platforms that may be controller, processor, or third party for the same data depending on configuration), and edge cases where the boundary line itself is genuinely contested. Each requires deliberate analysis.

## Terminology by state

| Term | CA (CCPA/CPRA) | Other 19 states |
|---|---|---|
| Determines purposes and means | **Business** | **Controller** |
| Processes on behalf of | **Service Provider** (closer relationship; written contract w/ § 7051 terms) or **Contractor** (non-affiliate processor; can include vendors and subprocessors) | **Processor** |
| Receives data outside the SP/Contractor relationship | **Third Party** | **Third Party** |
| Joint determination of purposes and means | (Implicit — both are businesses; CCPA does not have a formal "joint controller" concept) | (Implicit — both are controllers; no formal "joint controller" concept analogous to GDPR Art. 26) |

> **CA/Other gap.** California's "Service Provider" / "Contractor" / "Third Party" trichotomy is more elaborate than the simple "Processor" / "Third Party" structure in other states. The California categories also have specific contractual content requirements (CCPA Regs §§ 7051–7053) — without those terms, the relationship defaults to "Third Party" regardless of intent.

## Foundational rule — determines purposes and means

The threshold question for every data flow is: **who determined the purposes and means of processing for this data?**

- **Sole determination by Entity A** → A is the controller (business); any other entity is a processor or third party depending on the relationship and contract.
- **Determination by both Entity A and Entity B for the same flow** → both are controllers (in CA, both are businesses) — i.e., they are not in a controller-processor relationship, they are independent or joint controllers. CA does not have a "joint controller" formal regime; both are simply businesses with their own obligations.
- **Determination by Entity B alone, with A merely receiving and acting on instructions** → A is the processor; B is the controller.

"Purposes" means *why* the data is processed. "Means" means *how* — what data, what tools, what retention. A vendor that decides the means (because it deploys its own platform) but operates strictly within the customer's purposes is generally still a processor.

## Decision tree

For each data flow, walk the tree:

```
Q1: Did the entity determine the purposes for processing this data?
    ├── YES → Q2: Did the entity determine the means?
    │            ├── YES → CONTROLLER (CA: Business)
    │            └── PARTIALLY (e.g., chose vendor that controls technical means but
    │                          set the purposes within which the vendor operates)
    │                          → CONTROLLER (the vendor is the processor for those
    │                            specific purposes)
    └── NO  → Q3: Is the data being processed on behalf of another entity that
                  determines purposes AND there is a written contract meeting
                  state-specific requirements?
                  ├── YES + CCPA Regs § 7051 terms (CA) → SERVICE PROVIDER
                  ├── YES + state-specific terms (other states) → PROCESSOR
                  ├── YES + contract lacks required terms → THIRD PARTY
                  │                                          (the controller's
                  │                                          disclosure to the
                  │                                          recipient is a "sale"
                  │                                          or "share")
                  └── NO + receiving data without controller's instruction
                          → THIRD PARTY (and the controller's disclosure to the
                            recipient is a "sale" or "share")
```

Run the tree for each distinct data flow. For most controllers, you will need to run it 5–15 times to cover the typical operational footprint.

## Required contract terms (CA)

CCPA Regs § 7051 (Service Providers and Contractors) requires the contract to:

1. Prohibit the recipient from selling or sharing the personal information.
2. Prohibit the recipient from retaining, using, or disclosing the personal information for any purpose other than the business purposes specified in the contract, including retaining, using, or disclosing personal information for a commercial purpose other than the business purposes specified in the contract, or as otherwise permitted by the CCPA.
3. Prohibit the recipient from retaining, using, or disclosing the personal information outside of the direct business relationship.
4. Prohibit the recipient from combining personal information that the recipient receives from, or on behalf of, the business with personal information that it receives from, or on behalf of, another person, or collects from its own interaction with the consumer (with narrow exceptions).
5. Require the recipient to comply with applicable obligations under the CCPA, including providing the same level of privacy protection to the personal information as required of businesses by the CCPA.
6. Grant the business the right to take reasonable and appropriate steps to ensure that the recipient uses the personal information transferred in a manner consistent with the business's obligations under the CCPA.
7. Require the recipient to notify the business if it makes a determination that it can no longer meet its obligations under the CCPA.
8. Grant the business the right, upon notice, to take reasonable and appropriate steps to stop and remediate unauthorized use of personal information.
9. Require the recipient to comply with rights requests forwarded by the business.
10. Specify that the contract is entered into pursuant to the CCPA.

> **Failure mode.** A contract that omits any of these terms — particularly the purpose limitation, the no-combine clause, or the assistance-with-rights clause — does not establish service-provider status. *In re Honda* (2024) settled this question with a $632,500 settlement plus structural remediation.

## Required contract terms (other states)

Most other states' acts mirror the GDPR / CCPA structure with these required terms in controller-processor contracts:

1. Purpose limitation (data processed only for purposes specified by the controller).
2. Confidentiality obligations on personnel.
3. Security measures (technical and organizational).
4. Subprocessor flowdown (subprocessors bound to equivalent terms).
5. Assistance with consumer rights requests.
6. Assistance with data protection assessments.
7. Deletion or return of data at end of services.
8. Audit / inspection rights.
9. Notification of inability to comply.

State-specific provisions: Va. Code § 59.1-579; Colo. Rev. Stat. § 6-1-1305(5); Conn. Gen. Stat. § 42-521; analogous in others.

## Common dual-status patterns

### B2B SaaS provider

- **Customer-end-user data** (e.g., users of customer's CRM): **Processor** for that data, controller is the customer.
- **Customer-account data** (e.g., the customer's billing contact, admin user logins): **Controller** for that data — the SaaS uses it for its own customer-management purposes.
- **Marketing data** (prospect leads, website visitors): **Controller**.
- **Aggregate / de-identified data** used to improve the service: depends on whether genuinely de-identified per the standard. If yes, outside the act. If not, controller status for any "improvement" use.

### Adtech / ad platform

- **Configuration matters profoundly.** The same platform (e.g., Meta) can be:
  - **Service Provider** — when contractually limited to processing data on behalf of the advertiser (e.g., custom audience uploads with no further use).
  - **Third Party** — when receiving data for its own commercial purposes (e.g., audience modeling, lookalike-audience generation, training of advertising algorithms).
  - **Independent Controller** — for data Meta collects through its own user accounts.
- The advertiser's status: **Controller** for the data flow it initiates; the line between "service provider" and "third party" treatment is the dominant compliance question.

### Analytics platform (Google Analytics, Adobe Analytics)

- Analytics platforms have evolved their offerings to support service-provider configurations.
- **Default GA4** with measurement-protocol enabled and ads-personalization signals on: **Third Party** (data is being shared for cross-context behavioral advertising).
- **GA4 with Restricted Data Processing** + ads-personalization disabled + appropriate DPA: **Processor / Service Provider**.
- The configuration determines status, not the platform name.

### Identity / authentication provider (Auth0, Okta)

- **Processor / Service Provider** — typically processes only authentication data for the customer's purposes.
- Provider's own use of aggregate operational metrics is typically excluded by contract.

### Customer support tooling (Zendesk, Intercom)

- **Processor / Service Provider** for the customer's end-user support tickets.
- **Controller** for the customer's own admin and account data.

### Customer-data platforms (Segment, mParticle)

- **Processor / Service Provider** when configured to forward data per the customer's instructions.
- The CDP's identity-resolution features may push the relationship toward independent controller for those features; require granular DPA review.

### Email service providers (SendGrid, Postmark, Mailchimp)

- **Processor / Service Provider** for transactional and marketing sends initiated by the customer.
- **Controller** for ESP's own product analytics and prospect outreach.

### Payment processors (Stripe, Adyen)

- **Independent controller** for fraud detection and risk modeling. This is consistent with Stripe's own Privacy Policy.
- **Processor** for the specific transaction processing on the merchant's behalf.
- **Note**: PCI-DSS-mandated practices interact with privacy law; payment data is also "sensitive" or "financial" in most state definitions.

### Email / chat-based AI assistants and AI vendors

- **High contention.** Default vendor TOS often reserves the right to use customer data for model training, which makes the vendor an independent controller for that data flow.
- **Service-provider configuration** requires explicit contractual prohibition on use for training and other purposes outside the customer's business purposes.
- For a customer using a generative-AI assistant against its own customer data, the AI vendor's status depends on the contract: with a strong DPA, processor; with default TOS, third party.

## Edge cases

### "Joint determination" of purposes — independent controllers

When two entities jointly determine the purposes of processing, neither is a processor of the other. Both are controllers. Under US state privacy law, there is no formal "joint controller" regime analogous to GDPR Article 26, but the operational reality is the same: each entity has its own controller obligations to the consumer, including separate notice, separate rights-fulfillment, and separate duties to honor opt-outs.

Example: Two co-marketing partners that share lead data for joint promotion. Each is a controller; each must independently provide notice and honor opt-outs.

### Reseller or distributor relationships

A reseller that takes title to customer data and resells access to it is a controller, not a processor — even if the original collector is upstream. The reseller's commercial purpose is its own.

### Drop-shipping / fulfillment

A fulfillment provider receiving order data only to fulfill orders is a processor. A fulfillment provider that uses order data for its own commercial purposes (e.g., retargeting, lookalike audiences) is a third party for those uses.

### Data brokers

A data broker is generally a controller for the data it sells. The downstream recipient of broker data is a controller for its own use of that data. Importantly, data brokers are typically subject to additional state-specific registration laws (CA, TX, OR, VT) regardless of their comprehensive privacy law applicability.

### Internal corporate affiliates

Sharing between corporate affiliates under common ownership may or may not be a "sale" depending on the state. CCPA § 1798.140(ad) excludes intentionally-disclosed transfers between business and a person that is part of the same group of entities under common ownership and control — provided the transfer is consistent with consumer expectations and the parties share a privacy notice. Other states have varying provisions.

### A processor that exceeds its instructions

A processor that processes data outside the scope of the controller's instructions becomes a controller for that out-of-scope processing — and may have liability as a controller for that data flow. The contract does not protect a processor that knowingly processes outside the contract.

## How to document status determination

For each engagement, produce a table per data flow:

| Data flow | Source of data | Recipient(s) | Determines purpose | Determines means | Status | Required contract terms in place? | Citation |
|---|---|---|---|---|---|---|---|

Run it for at least these flows in any controller of consequence:

- End-user account / login data
- End-user activity / behavioral data
- End-user transaction / billing data
- Marketing prospect / lead data
- Customer (B2B) account data
- Customer end-user data (for SaaS providers)
- Vendor / employee data (CA-only relevance for HR)
- Aggregate / de-identified data flows
- Adtech / advertising-related data
- Analytics platform data
- Customer support tooling data
- Payment processor data
- Specific sensitive-data flows (health, biometric, geolocation, child)

## Common errors in status determination

1. **Treating the vendor's marketing materials as authority.** A SaaS vendor that calls itself a "processor" in its sales deck is not a processor unless the contract reflects it. Read the contract.
2. **Assuming "joint controllers" is a US concept.** It is not. Two co-determining entities are both controllers under US state privacy law. Each has independent obligations.
3. **Failing to distinguish service provider from third party in CA.** The CCPA Regs § 7051 specificity matters. A contract that calls the vendor a "service provider" but lacks the required terms creates a third-party relationship — and a "sale."
4. **Treating processor-of-the-controller's-data as a complete pass-through.** Processors have direct obligations: confidentiality, security, subprocessor flowdown, deletion on directive. *In re Blackbaud* (2024 multistate, $49.5M) established that processors face direct AG enforcement.
5. **Forgetting status changes when a vendor's offering changes.** When Meta launched Custom Audiences with the Conversions API and additional data categories, the analysis of Meta's status as service provider vs. third party shifted. Stay current.
6. **Missing affiliate-disclosure scrutiny.** Transfers between corporate affiliates may or may not be sales depending on state. Don't assume "we're all one company" cures the issue.
7. **Treating de-identified data flows as out-of-scope without verifying de-identification rigor.** De-identification is a high bar; verify the data is genuinely de-identified before excluding the flow from analysis.

## When status is genuinely contested

Some flows present genuinely contested status. The conservative posture:

1. **Default to controller for the flow** unless the contract clearly establishes processor status with required terms.
2. **Address the flow as both controller and processor in parallel** in the privacy notice and operational practices — this is often achievable with modest additional disclosure and supports either eventual determination.
3. **Surface the contested status in the deliverable** with the analysis and recommendation. The user (or reviewing counsel) should make the final call.

A controller defending an enforcement action will be in a stronger position with documented analysis of the contested status than with a unilateral assumption that turned out to be wrong.
