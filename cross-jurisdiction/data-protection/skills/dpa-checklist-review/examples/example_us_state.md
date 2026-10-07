# Worked Example — US State Privacy DPA Review (Service Provider Perspective)

This example shows the skill applied to a Service Provider Addendum proposed by a customer (a business under CCPA/CPRA) to the user (a SaaS vendor / service provider). The user is on the processor side; the analysis flips accordingly.

## Input

**Regulatory regime:** us_state_privacy
**Party role:** processor (service provider / contractor)
**Data categories:** "California consumer end-user data — name, email, account profile data, transaction history. No sensitive personal information."
**Prior agreements:** "We have an MSA with this customer dated 2024-Q3; this Service Provider Addendum is being proposed as an addition."

**Document (excerpts):**

> **CALIFORNIA CONSUMER PRIVACY ACT SERVICE PROVIDER ADDENDUM**
>
> **1. Definitions.** Capitalized terms used herein and not defined have the meanings given in the California Consumer Privacy Act of 2018, as amended by the California Privacy Rights Act of 2020 ("CCPA"). "Business" means Customer; "Service Provider" means Vendor; "Personal Information" or "PI" has the meaning given in CCPA §1798.140(v).
>
> **2. Service Provider Status. The parties acknowledge that Service Provider is a "service provider" within the meaning of CCPA §1798.140(ag), and that Personal Information disclosed by Business to Service Provider is disclosed for the limited and specified purposes set forth in the underlying Master Services Agreement and any Statement of Work, including without limitation: providing the Services, customer support, security and integrity functions, and any other purposes that Business may direct from time to time.
>
> **3. Restrictions on Service Provider.** Service Provider shall not:
>
> (a) sell or share the Personal Information;
>
> (b) retain, use, or disclose the Personal Information for any purpose other than for the business purposes specified in the Agreement, including retaining, using, or disclosing the Personal Information for a commercial purpose other than providing the Services;
>
> (c) retain, use, or disclose the Personal Information outside of the direct business relationship between Service Provider and Business;
>
> (d) combine the Personal Information that Service Provider receives from or on behalf of Business with Personal Information that Service Provider receives from or on behalf of another person, or collects from its own interaction with the consumer, except as permitted by 11 CCR §7050(b) (or its successor regulation).
>
> **4. Subcontractors.** Service Provider may engage subcontractors to perform the Services, provided that Service Provider enters into a written agreement with each subcontractor that requires the subcontractor to comply with the obligations applicable to Service Provider under this Addendum. Service Provider shall maintain a list of subcontractors that process Personal Information and shall make this list available to Business upon written request.
>
> **5. Consumer Rights. Service Provider shall provide reasonable and appropriate cooperation to Business to enable Business to comply with verifiable consumer requests under CCPA, including requests for access, deletion, correction, opt-out of sale/sharing, and limit use of sensitive personal information. Service Provider shall respond to Business's requests for cooperation within ten (10) business days, or such other period as may be necessary for Business to respond to the consumer request within the timeframes required by law.
>
> **6. Security. Service Provider shall implement reasonable security procedures and practices appropriate to the nature of the Personal Information to protect the Personal Information from unauthorized or illegal access, destruction, use, modification, or disclosure. Service Provider's current security practices are described in Service Provider's Trust Center, available at [URL], and incorporated into this Addendum by reference.
>
> **7. Compliance Notification.** Service Provider shall notify Business promptly if Service Provider determines that it can no longer meet its obligations under CCPA or this Addendum.
>
> **8. Audit Rights. Business may, no more than once per twelve (12) month period and upon at least thirty (30) days' written notice, request and receive copies of Service Provider's then-current third-party audit reports (such as SOC 2 Type II) under reasonable confidentiality protections. Business may also, with reasonable cause and upon Service Provider's reasonable consent (not to be unreasonably withheld), conduct an on-site audit at Business's expense.
>
> **9. Deletion. Upon termination of the Services or upon Business's written request, Service Provider shall, at Business's option, return or delete Personal Information within sixty (60) days, except for Personal Information that Service Provider is required by law to retain or that is contained in routine system backups (which will be deleted in accordance with Service Provider's standard backup retention practices).
>
> **10. Sensitive Personal Information.** The parties acknowledge that processing of "sensitive personal information" as defined in CCPA §1798.140(ae) is not within scope of this Addendum. If processing of sensitive personal information becomes necessary, the parties will execute an amendment.

## Output

# DPA Checklist Review: California CCPA Service Provider Addendum

**Regulatory regime:** US State Privacy (CCPA/CPRA, with note on multi-state implications)
**Party role:** Processor / Service Provider
**Data categories:** California consumer end-user data — name, email, account profile, transaction history; no sensitive PI
**Prior agreements:** MSA dated 2024-Q3 (referenced; conflicts assessed below)

## Overall posture

**Compliant with minor gaps from a service provider perspective.** The Addendum is generally well-drafted and addresses the core CCPA/CPRA service provider requirements. From a service provider perspective (the user's role), the Addendum is signable with two minor adjustments. Two operational items warrant the user's attention: (a) the "purposes that Business may direct from time to time" clause in §2 creates open-ended scope expansion that the service provider should constrain; (b) the on-site audit provision in §8 should specify that audit costs include reasonable allocation of service-provider personnel time. Note that this is a CCPA/CPRA-only Addendum and does not address other state privacy laws that may apply to the same data flows; if California consumers are part of a broader US user base, a multi-state harmonized addendum may be more efficient.

## Compliance checklist

| # | Required term | Source | Status | Clause | Assessment |
|---|---|---|---|---|---|
| 1 | Purpose limitation | CCPA §1798.140(ag)(1) | Partial | §2 | Open-ended "purposes Business may direct from time to time" — broader than CCPA contemplates |
| 2 | Prohibition on sale and sharing | CCPA §1798.140(ag)(1)(A) | Present | §3(a) | Compliant |
| 3 | Prohibition on retention/use/disclosure outside business purposes | CCPA §1798.140(ag)(1)(B) | Present | §3(b)–(c) | Compliant |
| 4 | Prohibition on combining PI | CCPA §1798.140(ag)(1)(C) | Present | §3(d) | Compliant; properly cites 11 CCR §7050(b) carve-out |
| 5 | Subcontractor flow-down | CCPA §1798.140(ag)(1)(D) | Present | §4 | Compliant; subcontractor list available on request |
| 6 | Consumer rights cooperation | CCPA §1798.140(ag)(1)(E) | Present | §5 | Strong — 10-business-day response with adjustment for legal timeframes |
| 7 | Security safeguards | CCPA §1798.100(e), §1798.140(ag) | Present | §6 + Trust Center | Reasonable security with framework reference; verify Trust Center contents |
| 8 | Audit and inspection rights | CCPA §1798.140(ag)(1)(D)(ii) | Present | §8 | Reasonable parameters; clarify audit cost allocation |
| 9 | Notification of inability to comply | CCPA §1798.140(ag)(1)(D)(i)(III) | Present | §7 | Brief but compliant |
| 10 | Deletion / return at end | (Convergent state requirement) | Present | §9 | Compliant; controller choice; reasonable backup carve-out |
| 11 | Identification of consumer rights | (Some state requirement) | Partial | §5 | Listed in §5; minor — recital-level addition would strengthen |
| 12 | Sensitive PI handling | CCPA §1798.140(ae) | N/A — out of scope | §10 | Properly carved out via amendment mechanism |
| — | Multi-state coverage | (Other state laws) | **Missing** | — | Addendum is CCPA-only; other state laws (Virginia, Colorado, Connecticut, etc.) not addressed |

## Detailed findings

### 1. Purpose limitation — Partial

**Required by:** CCPA §1798.140(ag)(1).

**What's required:** The contract must specify the limited and specified purposes for which the service provider processes personal information. Open-ended purpose definitions undermine the service provider safe harbor; if the service provider can be directed to do anything, it functionally has no purpose limitation.

**What the document says:** §2 specifies "providing the Services, customer support, security and integrity functions, and any other purposes that Business may direct from time to time."

**Why this is a partial finding:** The first three purposes (Services, customer support, security) are appropriately scoped. The catch-all ("any other purposes that Business may direct from time to time") is not. From a service provider perspective, this creates two problems: (1) the service provider's permitted scope expands at the customer's unilateral direction, with no contractual gate; (2) if the customer directs a purpose that exceeds CCPA service-provider parameters, the service provider's safe harbor evaporates without notice.

**Recommended language:**
> "Service Provider shall process Personal Information only for the following business purposes: (a) providing the Services as described in the Master Services Agreement and any Statement of Work; (b) customer support relating to the Services; (c) security and integrity functions, including detection and prevention of fraud, security incidents, and unauthorized access; (d) any additional business purposes specified in writing by Business with Service Provider's written acknowledgment, provided such purposes are consistent with CCPA §1798.140(ag)."

This preserves the customer's flexibility (they can add purposes) while requiring service provider acknowledgment (the service provider can confirm the new purpose is within CCPA scope before agreeing).

### 8. Audit rights — Present (but cost allocation should be clarified)

**Required by:** CCPA §1798.140(ag)(1)(D)(ii).

**What's required:** The business must be able to take reasonable and appropriate steps to ensure that the service provider uses personal information consistent with the business's CCPA obligations.

**What the document says:** §8 provides report-review audit rights annually with 30-day notice; on-site audits permitted "with reasonable cause and upon Service Provider's reasonable consent (not to be unreasonably withheld)" at Business's expense.

**Why this is acceptable but worth refining:** The structure (report review for routine; on-site for cause) is industry standard and CCPA-compliant. The "Business's expense" language in the on-site provision typically refers only to direct audit costs (auditor fees, travel) — but on-site audits also consume service-provider personnel time, system access, and operational disruption. Industry practice is to specify that the auditing party reimburses the audited party for reasonable personnel time and out-of-pocket expenses incurred in supporting the audit.

**Recommended adjustment:**
Add to §8: "*Business shall reimburse Service Provider for reasonable personnel time, out-of-pocket expenses, and disruption costs incurred in supporting on-site audits, except where the audit reveals a material breach of this Addendum by Service Provider, in which case Service Provider shall bear all reasonable audit costs.*"

### Multi-state coverage — Missing

**Required by:** Other state privacy laws (Virginia VCDPA, Colorado CPA, Connecticut CTDPA, and others).

**What's required:** If California consumer data is being processed under this Addendum, it is highly likely that data of consumers from other US states is being processed in the same systems and by the same service provider — and several of those states (Virginia, Colorado, Connecticut, Texas, Oregon, and others) have their own DPA-equivalent contractual requirements that are similar but not identical to CCPA.

**Why this is a finding:** A CCPA-only Addendum does not provide the contractual basis for processing data of consumers from those other states. The customer (Business) bears the regulatory risk if other state laws apply and are not contractually addressed. The service provider also has an interest in clarity here — if the customer later asserts a Virginia VCDPA violation, the service provider's defense rests on what the contract actually requires.

**Recommended approach:**

1. Confirm with the customer whether the data flows under this engagement involve only California consumers, or include consumers from other US states.
2. If the latter, propose either (a) a multi-state harmonized addendum that addresses CCPA, VCDPA, CPA, CTDPA, and other applicable laws (recommended for efficiency), or (b) a state-specific addendum for each applicable state (less efficient but acceptable).
3. If the customer insists on CCPA-only scope, document the limitation clearly: the Addendum should state that the parties have considered other state privacy laws and have determined (with documented basis) that they do not apply to the data flows under this Agreement.

## Items requiring human judgment

- **Verify Trust Center security practices** are adequate for the data category. Trust Centers vary in detail; review actual contents before signing.
- **Confirm whether other state privacy laws apply** to the data flows in scope. The Addendum is CCPA-only by structure; other state laws may also apply if non-California consumers' data is processed.
- **Consider conflict with the existing MSA dated 2024-Q3.** Specifically: does the MSA contain general data-handling provisions that this Addendum modifies? Does the MSA's confidentiality clause overlap with this Addendum's §3? An integration clause should be added to clarify precedence.
- **Whether the catch-all "purposes Business may direct from time to time"** is acceptable as a business call. The Material finding on §2 reflects strict CCPA service-provider scoping; some service providers accept this language for trusted customers.

## Recommended next steps

1. **The Addendum is signable from a service provider perspective with the recommended adjustment to §8 (audit cost allocation) and consideration of the §2 partial finding.** Both are negotiable but the document as a whole is structurally sound.
2. **Address multi-state scope.** Confirm whether the data in scope includes non-California consumers; if so, recommend a multi-state harmonized addendum.
3. **Add an integration clause** clarifying the relationship between this Addendum and the existing MSA.
4. **Verify Trust Center contents** are current and adequate before signing.

---

## What this example demonstrates

- **Severity calibration to a clean document.** Most table rows are Present; only one Partial finding and one structural Missing finding. The detailed-findings section is short because there is little to detail.
- **Processor-perspective lens.** The Partial finding on §2 (open-ended purpose) and the Material finding on §8 (audit cost allocation) are framed from the service provider's interest. A controller-perspective review of the same Addendum would have different priorities — the controller might be satisfied with §2's open-endedness and contest the on-site audit consent gate.
- **Multi-state issue surfaced as a structural finding.** This is a category not present in the GDPR example because it doesn't apply to GDPR. The skill's regime-specific reference files surface regime-specific issues.
- **Prior agreements input does work in the report.** The "Items requiring human judgment" section flags MSA-conflict considerations because `prior_agreements` was provided.
- **The checklist format reflects the actual posture.** Most rows Present; the Addendum is genuinely well-drafted; the report is correspondingly short. A long report on a clean document would be padding.
- **Recommended next steps are prioritized and proportional.** First step is "signable with adjustments," not "negotiate everything." When a document is mostly fine, the report should reflect that.
