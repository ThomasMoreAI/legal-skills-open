# Worked Example — Clean Privacy Policy

This example demonstrates Vendor Privacy Policy First Pass handling a well-drafted vendor privacy policy. Most provisions are clear and within standard practice; the report is correspondingly short, with a "proceed to DPA" recommendation.

## Input

**Document:** SaaS analytics vendor's published privacy policy (effective date 4 months ago)
**Vendor context:** "Web analytics platform; we'd share visitor IP addresses, page-view data, and referrer information for analytics processing."
**Applicable regimes:** "GDPR (we have EU users); CCPA (we have California consumers)"
**Data to share:** "Web analytics data — visitor identifiers (IP, fingerprint), page-view events, referrer data, device/browser metadata. No account-level PII."

**Document (excerpts — actual policy is 12 pages):**

> **Effective Date:** [4 months ago]
>
> **§1 Information We Collect.** We collect the following categories of information:
> - **Account Information** (provided by our customers): name, email address, company, role, billing information.
> - **Visitor Data** (received from our customers' end users via our analytics SDK): IP address, browser type and version, device type, operating system, referring URL, page views, click events, session duration, custom event data as configured by our customers.
> - **Cookies and similar technologies** for our own website (separate from analytics SDK behavior on customer sites): session cookies, authentication cookies, preference cookies. See our Cookie Notice for details.
>
> **§2 How We Use Information.** We use the information we collect for the following specific purposes:
> - **Provide the Service:** to deliver analytics insights to our customers as contracted.
> - **Customer Support:** to respond to support inquiries from our customers' authorized users.
> - **Service Operations:** to maintain, secure, and improve our infrastructure (operational telemetry, debugging, capacity planning).
> - **Legal Compliance:** to comply with applicable law and respond to lawful requests.
>
> We do not use Visitor Data for marketing, advertising, or AI/ML model training. We do not use Visitor Data for our own business purposes beyond providing the Service. Operational telemetry uses anonymized and aggregated data only.
>
> **§3 Sharing of Information.** We share information only with:
> - **Sub-processors** that support our infrastructure (cloud hosting provider, payment processor, email delivery for transactional notices). A current list of sub-processors is maintained at [URL].
> - **Affiliates within our corporate family** in accordance with this policy.
> - **Service providers** acting on our instructions for limited purposes.
> - **Legal authorities** in response to valid legal process.
> - **In connection with corporate transactions** (M&A) with notice to customers.
>
> We do not sell or share personal information for cross-context behavioral advertising or other monetary or valuable consideration. For purposes of CCPA/CPRA, we operate as a Service Provider with respect to Visitor Data.
>
> **§4 International Transfers.** Information may be processed in the United States and the European Union. For transfers from the EEA, UK, or Switzerland to the United States, we rely on the EU-US Data Privacy Framework (DPF) and, where DPF does not apply, the European Commission Standard Contractual Clauses adopted by Implementing Decision (EU) 2021/914, executed with our customers and our sub-processors. We have conducted a Transfer Impact Assessment supporting these transfers; supplementary measures including encryption in transit and at rest are described in our Trust Center.
>
> **§5 Retention.** We retain Account Information for the duration of the customer relationship plus seven (7) years for tax and audit purposes. We retain Visitor Data for the period configured by our customers (default twenty-four (24) months); customers may shorten the retention period at any time. Operational telemetry is retained for ninety (90) days in identifiable form, then aggregated indefinitely.
>
> **§6 Your Rights.** Depending on applicable law, individuals have the following rights with respect to their personal information:
> - Access, correction, deletion, portability.
> - Opt-out of sale or sharing (for U.S. consumers under applicable state law); given that we do not sell or share, this right is moot but available.
> - Object to processing, restrict processing, withdraw consent (where consent is the legal basis).
> - Limit use of sensitive personal information; we do not collect sensitive personal information in connection with our Service.
> - Lodge a complaint with the supervisory authority in your jurisdiction.
>
> Visitor Data: visitors should typically direct rights requests to the customer (the website operator) who controls the data. We will support our customers' responses to such requests.
>
> Account Information: account users should email privacy@[vendor]. We respond within 30 days for GDPR requests, 45 days for CCPA requests; complex requests may extend by an additional 30 days with notice.
>
> **§7 Security.** We maintain a security program described in our Trust Center, including SOC 2 Type II certification, ISO 27001 certification, encryption in transit (TLS 1.3) and at rest (AES-256), access controls including MFA for all staff, and regular penetration testing.
>
> **§8 Children's Data.** Our Service is not directed at children under 16. Customers are responsible for compliance with COPPA and similar laws if they configure our Service in contexts where children's data may be collected.
>
> **§9 Contact.** Privacy questions: privacy@[vendor]. Data Protection Officer: dpo@[vendor]. EU representative: [name and contact]. Supervisory authority complaints: contact your local supervisory authority; a list is maintained at [URL].
>
> **§10 AI and Machine Learning.** We do not use Visitor Data, Account Information, or any data received from our customers for training, fine-tuning, or improving any AI or machine learning model. Our Service does not use AI/ML in a manner that processes individual visitor data; aggregated insights are computed using deterministic statistical methods.

## Output

# Vendor Privacy Policy First Pass: [Vendor] Privacy Policy

**Vendor context:** Web analytics platform; user shares visitor identifiers, page-view events, referrer data, device/browser metadata. No account-level PII.
**Applicable regimes considered:** GDPR, CCPA/CPRA
**Data the user expects to share:** Web analytics data; no sensitive PI; no PII beyond visitor identifiers
**Policy effective date:** [4 months ago]

## Bottom line

**Clean privacy policy with no red flags identified at the first-pass level. Proceed to DPA negotiation.** The policy demonstrates strong privacy posture: explicit no-ML-training language, narrow purpose limitation, current transfer mechanisms (DPF + 2021 SCCs), CCPA service-provider categorization, robust user-rights framework with operational specifics, and clear privacy contacts including DPO and EU representative. The policy is recently updated (4 months ago) and reflects current law. No issues identified that would warrant pausing vendor onboarding or escalating to deeper privacy review.

## Structured summary

### Data collected

Three distinct categories with clear sourcing: Account Information from customers (name, email, company, billing), Visitor Data from customers' end users via analytics SDK (IP, browser, page views, custom events), and own-website cookies. Sensitive categories explicitly not collected. [§1]

### Use of data

Four specific purposes enumerated: service provision, customer support, service operations (operational telemetry only), and legal compliance. Explicit statement that Visitor Data is not used for marketing, advertising, or AI/ML training. Operational telemetry uses anonymized and aggregated data only. [§2]

### Sharing

Five recipient categories: sub-processors (with current list at URL), affiliates within corporate family, service providers, legal authorities for lawful process, M&A transactions with notice. Explicit statement of no sale/sharing under CCPA. Vendor self-categorizes as Service Provider for Visitor Data under CCPA/CPRA. [§3]

### Cross-border transfers

Transfers between US and EU disclosed. Mechanisms: EU-US Data Privacy Framework (DPF) where applicable; otherwise 2021 EU Standard Contractual Clauses, executed with customers and sub-processors. Transfer Impact Assessment conducted; supplementary measures (encryption in transit and at rest) described in Trust Center. [§4]

### Retention

Specific periods: Account Information for customer-relationship duration plus 7 years (tax/audit basis); Visitor Data for customer-configured period (default 24 months, customer-adjustable); operational telemetry 90 days identifiable then aggregated indefinitely. [§5]

### User rights and exercise mechanisms

Rights enumerated comprehensively for both visitors and account users. Visitor rights routed through customers (website operators) per the controller-processor model; vendor commits to support customer responses. Account user rights direct to privacy@[vendor]; response timelines 30 days (GDPR), 45 days (CCPA), with up to 30-day extension for complex requests. [§6]

### Security

SOC 2 Type II, ISO 27001 certifications. TLS 1.3 in transit, AES-256 at rest. MFA for all staff, regular penetration testing. Detailed security program documented in Trust Center. [§7]

### Children's data

Service not directed at children under 16. Customer responsibility for COPPA compliance where applicable. [§8]

### Contact and complaints

Privacy email, DPO contact, EU representative all disclosed. Supervisory authority complaint right disclosed with reference URL. [§9]

### AI / ML use of data

**Explicit no-training commitment.** Vendor does not use any customer data for training, fine-tuning, or improving AI/ML models. Service uses deterministic statistical methods rather than ML processing of individual visitor data. [§10]

## Red flags

No red flags identified at the first-pass level.

## Items the policy doesn't address (gaps)

No material gaps for an analytics-vendor policy in this scope. The policy could go further on:

- **Sub-processor change-notification mechanics** — current sub-processor list is maintained at URL, but the policy doesn't describe how customers are notified of sub-processor changes. This is typically a DPA-level concern, not a privacy policy concern.
- **Specific data-residency commitments** — policy mentions US and EU processing but doesn't commit to data residency in a specific region. Not a privacy-policy expectation; would be addressed in DPA if customer requires.

These are not red flags but items the user may want to address in DPA negotiation if they matter for the user's deployment.

## Recommended next steps

1. **Proceed to DPA negotiation.** The privacy policy is adequate; the operative commitments will live in the DPA.
2. **Run DPA Checklist Review** when the vendor's DPA is presented. The DPA should mirror the privacy policy's commitments and add specific contractual obligations (sub-processor change notification, breach notification timing, audit rights).
3. **Verify Trust Center contents** — the policy references SOC 2 Type II, ISO 27001, and security details. Obtain actual reports/certifications during security review.
4. **Verify TIA** — the policy references a TIA for international transfers. Request the TIA or its summary as part of the privacy review file.
5. **Confirm sub-processor list is current** — the URL referenced in §3 should match the operative list; verify and align with DPA.

## Out of scope for this first pass

This first pass did not constitute: a full privacy assessment (which would include review of the DPA, security exhibit, sub-processor agreements, breach response history, regulatory inquiries, and operational practices); a CCPA or GDPR compliance certification (which requires legal opinion based on full facts); a security architecture review (which requires SOC 2 reports, penetration test summaries, and security questionnaires); or an enforceability opinion on the policy's commitments. The user should not rely on this first pass for those purposes.

---

## What this example demonstrates

- **Clean policies produce short reports.** No red flags identified; report is roughly two pages. The skill does not pad clean reviews to look thorough.
- **Structured summary covers all 10 topics regardless of policy length.** Even when the policy is clean, the user gets a quick reference for what the policy says on each topic.
- **The "no red flags" finding is stated explicitly.** Rather than omitting the section, the report explicitly notes that no red flags were identified — which is itself a meaningful finding for the user.
- **AI/ML use of data is treated as a distinct topic.** The vendor's explicit no-training commitment is highlighted in the structured summary because it's the dominant 2025-2026 issue. A vendor with this commitment is meaningfully different from a vendor without one.
- **Recommended next steps are operational and proportional.** Five steps, all routine vendor-onboarding actions; no escalation, no negotiation rounds. Appropriate to a clean policy.
- **Out-of-scope reminder closes the report.** Even with a clean policy, the skill explicitly tells the user what was not done — a clean privacy policy is not a security review, a DPA review, or a compliance certification.
- **"Proceed to DPA" is the explicit recommendation.** The skill recognizes that the privacy policy is one input to vendor onboarding, not the complete picture; the user should continue the standard procurement flow.
