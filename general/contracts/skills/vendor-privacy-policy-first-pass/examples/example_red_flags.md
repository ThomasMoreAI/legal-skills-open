# Worked Example — Privacy Policy with Red Flags

This example demonstrates Vendor Privacy Policy First Pass handling a vendor privacy policy with multiple problematic provisions. The report is longer; the recommendation is to escalate to deeper privacy review and pause vendor onboarding pending substantive changes.

## Input

**Document:** AI-powered customer support platform's published privacy policy (effective date 22 months ago)
**Vendor context:** "AI customer support tool that ingests our customer support tickets, chat transcripts, and CRM data to provide automated responses and analytics."
**Applicable regimes:** "GDPR (EU users), CCPA/CPRA (California consumers)"
**Data to share:** "Customer support tickets and chat transcripts containing customer PII (names, emails, account details), account-level usage data, CRM contact records."

**Document (excerpts — actual policy is 8 pages):**

> **Effective Date:** [22 months ago]
>
> **§1 Information We Collect.** When you use our Service, we may collect any information you provide to us, information about your use of the Service, and information from third parties. This includes account information, usage information, customer interaction data, and any other information necessary to provide and improve our Service.
>
> **§2 Use of Information.** We use information for any purpose related to our business, including without limitation: providing and improving the Service; research and development, including training of artificial intelligence and machine learning models; analytics and benchmarking; marketing and advertising of our products and services; and any other purpose disclosed at the time of collection or with your consent.
>
> **§3 Sharing.** We may share information with our affiliates, service providers, business partners, advertising partners, and other third parties as necessary to provide and improve our Service or as we otherwise determine appropriate. We may also share aggregated and anonymized information for any purpose.
>
> Our Service may transfer information to third parties for valuable consideration, including in connection with cross-context behavioral advertising. California consumers may opt out of such sale or sharing by contacting privacy@[vendor].
>
> **§4 International Transfers.** Information may be transferred to and processed in any country where we or our service providers maintain operations. We rely on appropriate transfer mechanisms in compliance with applicable law, including the EU-US Privacy Shield Framework and Standard Contractual Clauses where applicable.
>
> **§5 Retention.** We retain information for as long as we deem necessary to provide our Service and for our legitimate business interests.
>
> **§6 Your Rights.** Depending on your jurisdiction, you may have certain rights regarding your personal information, including rights of access, correction, and deletion. We will respond to verifiable requests in accordance with applicable law and in our sole discretion regarding the appropriate response. Requests may be subject to a reasonable processing fee.
>
> **§7 Security.** We implement industry-standard security measures designed to protect your information. However, no method of transmission or storage is completely secure, and we cannot guarantee the absolute security of your information.
>
> **§8 Children's Data.** [no section in document]
>
> **§9 Contact.** For privacy questions, contact us at support@[vendor].
>
> **§10 AI Features.** Our Service includes artificial intelligence features that learn from interactions to provide better responses over time. By using the Service, you acknowledge that your data and interactions may be used to train and improve our AI systems. For more information, see our AI Usage Policy at [URL].

## Output

# Vendor Privacy Policy First Pass: [Vendor] Privacy Policy

**Vendor context:** AI customer support platform; user shares customer support tickets, chat transcripts, CRM data containing customer PII.
**Applicable regimes considered:** GDPR, CCPA/CPRA
**Data the user expects to share:** Customer support tickets and chat transcripts with customer PII; account usage data; CRM contact records.
**Policy effective date:** 22 months ago

## Bottom line

**Privacy policy contains seven red flags including five at critical severity. Do not proceed with vendor onboarding pending substantial vendor responses.** The policy presents structural and substantive privacy concerns that, in combination, suggest either (a) the vendor's privacy practices are inadequate for the data sensitivity in scope, or (b) the privacy policy substantially understates the vendor's actual privacy posture. The most consequential issues: (1) explicit AI/ML training on customer data without opt-out (§§2, 10); (2) explicit "sale" under CCPA in a context where the user expects service-provider treatment (§3); (3) reference to invalidated Privacy Shield as a transfer mechanism (§4); (4) catch-all data collection and broad use language (§§1, 2); (5) policy is 22 months old (not updated for CPRA, EU AI Act, or recent regulatory developments). Recommend escalation to privacy counsel before proceeding; if proceeding is desired, require substantive policy revision plus DPA terms that override the policy's worst provisions.

## Structured summary

### Data collected

Catch-all collection language: "any information you provide," "information about your use," and "information from third parties." No enumeration of categories. Sources include direct collection, automatic collection, and third-party sources, none specifically identified. [§1]

### Use of data

Open-ended use rights: "any purpose related to our business." Specific purposes enumerated include providing the Service, but also research and development with explicit ML training, analytics, benchmarking, marketing, and advertising. The "or any other purpose disclosed at the time of collection or with your consent" language allows further expansion. [§2]

### Sharing

Broad sharing with multiple recipient categories including advertising partners. Vendor explicitly transfers information for valuable consideration and discloses cross-context behavioral advertising — vendor self-categorizes as engaging in CCPA "sale" or "sharing." Aggregated and anonymized information shared for "any purpose." Sub-processor identification absent. [§3]

### Cross-border transfers

Generic statement that information may transfer to "any country where we or our service providers maintain operations." Mechanisms referenced: Privacy Shield Framework (invalidated July 2020 by Schrems II) and "Standard Contractual Clauses where applicable." No reference to current 2021 SCCs, DPF, or TIA. [§4]

### Retention

Vague: "as long as we deem necessary to provide our Service and for our legitimate business interests." No specific periods, no methodology, no deletion mechanism on user request. [§5]

### User rights and exercise mechanisms

Rights enumerated (access, correction, deletion). Exercise mechanism not specified beyond a single privacy contact. Vendor reserves "sole discretion regarding the appropriate response." Charges for rights requests permitted. No timeline commitment. [§6]

### Security

Generic "industry-standard security measures" with disclaimer ("we cannot guarantee absolute security"). No reference to certifications (SOC 2, ISO 27001), no specific safeguards (encryption, access controls), no Trust Center reference. [§7]

### Children's data

Not addressed in the policy.

### Contact and complaints

Single privacy contact (support@[vendor], a general support email rather than dedicated privacy contact). No DPO disclosure for GDPR-applicable contexts. No EU representative disclosure. No supervisory authority complaint right disclosed. [§9]

### AI / ML use of data

Vendor explicitly uses customer data and interactions to train and improve AI systems. Acknowledgment is deemed by use of the Service ("by using the Service, you acknowledge"). Further detail in a separate AI Usage Policy referenced but not included in this review. [§10]

## Red flags

### §§2, 10 — AI/ML training on customer data without opt-out (CRITICAL)

**What the policy says:** vendor uses customer data and interactions to train AI/ML models. User acknowledgment is deemed by use of the Service. No opt-out mechanism.

**Why it's critical:** customer support tickets and chat transcripts typically contain customer PII (names, account details, financial issues, complaints). Using this data to train AI models can produce model behavior that reflects customer-specific information; even with claimed anonymization, model weights may encode customer patterns. For the user's data flow (customer support data with PII), this is an unacceptable default. The "deemed acknowledgment by use" structure does not constitute meaningful consent under GDPR or affirmative authorization under most state privacy laws.

**User action:** require explicit no-training commitment in the DPA, or narrow opt-in mechanism. This is non-negotiable for the data sensitivity in scope.

### §3 — Explicit "sale" or "sharing" under CCPA (CRITICAL)

**What the policy says:** vendor transfers information for valuable consideration including for cross-context behavioral advertising. Vendor self-categorizes as engaging in CCPA "sale" or "sharing."

**Why it's critical:** for a customer support platform handling user's customer PII, "sale" of that data is fundamentally inconsistent with the service-provider relationship the user expects. The user is sharing customer data for the limited purpose of supporting the user's customers; vendor's monetization of that data is outside the expected scope. CCPA opt-out mechanism is required and disclosed, but the underlying business model is the issue, not just the opt-out availability.

**User action:** clarify with vendor whether sale/sharing applies to user's account specifically, or whether vendor offers a service-provider-only configuration; if vendor cannot provide service-provider-only treatment, escalate immediately.

### §4 — Reference to invalidated transfer mechanism (CRITICAL)

**What the policy says:** "EU-US Privacy Shield Framework" referenced as a transfer mechanism.

**Why it's critical:** Privacy Shield was invalidated by the CJEU's Schrems II decision in July 2020, nearly six years ago. Vendors operating under Privacy Shield were required to transition to alternative mechanisms; the EU-US Data Privacy Framework (DPF) became available for certified entities in July 2023. A policy still referencing Privacy Shield indicates either the policy has not been substantively updated since 2020 (a significant maintenance issue) or vendor is not aware of the regulatory landscape (a more concerning posture issue). Either way, transfers from EU to US under this policy may not have a valid mechanism, exposing user to GDPR transfer-mechanism non-compliance.

**User action:** require vendor to confirm in writing that current transfer mechanisms (DPF or 2021 SCCs) are in place; require updated privacy policy reflecting current mechanisms; verify TIA exists.

### §§1, 2 — Catch-all data collection and broad use language (CRITICAL)

**What the policy says:** "any information you provide" plus "any purpose related to our business." Effectively unlimited collection and use.

**Why it's critical:** the user has no way to assess what data is collected or how it's used. For data that includes customer support tickets with customer PII, this lack of transparency is unacceptable.

**User action:** require specific data-category enumeration and purpose enumeration in the DPA. Refuse the catch-all language.

### Effective date 22 months ago (CRITICAL given other findings)

**What the policy says:** effective date is 22 months old.

**Why it's critical:** in conjunction with the Privacy Shield reference (invalid for 6 years) and absence of CPRA-specific disclosures (CPRA fully effective March 2023), the policy is not maintained current with the regulatory landscape. EU AI Act provisions effective in 2024-2025 are also not reflected. The policy may not reflect vendor's actual current practices.

**User action:** request updated privacy policy reflecting current law before proceeding; if vendor cannot or will not produce updated policy, treat as a major posture concern.

### §6 — Rights exercise subject to vendor's "sole discretion" with charges (MATERIAL)

**What the policy says:** vendor responds to rights requests "in our sole discretion regarding the appropriate response" with potential processing fees.

**Why it's material:** discretion-based rights responses are inconsistent with GDPR and CCPA, which require specific responses to verified requests. CCPA prohibits charges for routine requests. The "sole discretion" language attempts to subordinate statutory rights to vendor's choices; this is not enforceable but suggests vendor is not in compliance posture.

**User action:** require specific commitment in DPA to honor rights consistent with applicable law; ensure no charges for routine requests; specify response timelines.

### §7 — Generic security with self-undermining disclaimer (MATERIAL)

**What the policy says:** "industry-standard security measures" with "we cannot guarantee the absolute security."

**Why it's material:** for a vendor handling customer PII, generic security commitments without specific safeguards or certifications are inadequate. The self-undermining disclaimer ("we cannot guarantee") is not by itself problematic but combined with no offsetting commitments leaves user with no meaningful security expectations.

**User action:** require specific security commitments in DPA; obtain SOC 2 Type II report or equivalent; conduct security review separately.

## Items the policy doesn't address (gaps)

Material absences beyond the red flags:

- **Sub-processor identification or list URL.** Vendor's sub-processors are not disclosed in the policy.
- **Specific retention periods or methodology.** §5 is vague.
- **DPO contact in GDPR-applicable contexts.** Not disclosed.
- **EU representative for non-EU vendor with EU users.** Not disclosed.
- **Supervisory authority complaint right.** Not disclosed.
- **Children's data treatment.** No section.
- **Specific transfer mechanism for current SCCs (post-Schrems II).** Reference to "Standard Contractual Clauses where applicable" without specifying the 2021 module.
- **TIA reference for non-adequacy transfers.** No mention.

Each of these gaps is material in a comprehensive privacy review; in this triage, they accumulate to suggest a vendor with substantially below-market privacy posture.

## Recommended next steps

1. **Pause vendor onboarding.** The combination of seven red flags including five critical and substantial gaps warrants stopping the standard procurement flow.
2. **Escalate to privacy counsel.** This first pass identifies issues that warrant expert review before proceeding. Privacy counsel can assess whether the policy reflects actual practices or is just poorly drafted, and can guide the negotiation strategy.
3. **Request vendor responses on critical issues:**
   - Confirm whether the vendor offers a service-provider-only configuration that excludes ML training and CCPA "sale."
   - Confirm current transfer mechanisms (DPF certification status, 2021 SCCs).
   - Request updated privacy policy reflecting current law.
   - Provide specific data-category and purpose enumeration.
4. **Request SOC 2 Type II report and security questionnaire.** The privacy policy's security section is too generic to allow assessment.
5. **Request the AI Usage Policy** (referenced in §10 but not included). Run this skill on it separately.
6. **Consider whether to proceed at all.** Even if vendor provides satisfactory responses, the policy's current state suggests vendor's privacy practices may require substantial vendor-side investment to bring into alignment with the user's expectations. If competing vendors have more mature privacy postures, the negotiation cost may exceed the value.
7. **If proceeding, require substantial DPA terms:**
   - Explicit no-training language overriding §§2, 10.
   - Service-provider-only processing under CCPA, overriding §3's sale/sharing posture.
   - Specific 2021 SCCs with TIA.
   - Specific data-category and purpose enumeration overriding §§1, 2 catch-all.
   - Specific retention periods overriding §5.
   - Specific rights commitments overriding §6's discretion language.

## Out of scope for this first pass

This first pass did not constitute: a full privacy assessment (full assessment requires DPA review, security exhibit, sub-processor review, breach response history); a CCPA or GDPR compliance opinion (compliance opinions require legal analysis based on full facts); or a security architecture review. Given the volume and severity of issues identified, all three deeper reviews are recommended before any onboarding decision.

---

## What this example demonstrates

- **Severity calibration to a problematic policy.** Five critical red flags identified; the report length reflects the document's posture, not skill padding.
- **The AI/ML training issue is treated as the headline.** Consistent with the dominant 2025-2026 issue framing; the user's customer-support data context elevates the severity.
- **CCPA "sale" disclosure is taken seriously.** Many vendors who explicitly disclose sale/sharing under CCPA have services that some customers expect to be service-provider-only; the conflict between the disclosure and the customer's expectation is the issue, not just the opt-out availability.
- **Stale policy is treated as a posture indicator, not just a maintenance issue.** Privacy Shield reference 6 years post-invalidation is more than carelessness — it suggests the vendor is not engaged with the regulatory landscape.
- **Recommended next steps are escalation-oriented.** First step is pause; second is privacy counsel escalation. This is the appropriate response to seven red flags including five critical.
- **The skill recognizes "decline to proceed" as a valid recommendation.** Step 6 contemplates that even with vendor responses, the deal may not be salvageable; the user is reminded that competing vendors may be a better path.
- **Out-of-scope reminder gains weight in problematic policies.** The user is explicitly told that this triage cannot substitute for the deeper reviews this situation warrants.
- **Items the policy doesn't address (gaps) section does work.** Distinct from red flags, the gaps section identifies what's missing rather than what's wrong with what's present. The cumulative effect is that the user sees both the problematic provisions and the absent ones.
