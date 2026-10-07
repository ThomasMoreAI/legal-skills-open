# SaaS MSA Issue Checklist

This checklist drives Pass 2 of the review. Issues are organized into four tiers:

- **Tier 1** — Always reviewed in detail. Covered in both `comprehensive` and `quick_triage`.
- **Tier 2** — Reviewed in detail in `comprehensive` only. In `quick_triage`, surfaced only when materially deviant.
- **Tier 3** — Reviewed in detail in `comprehensive` only. Drafting cleanliness; rarely material on their own.
- **Tier 4** — SaaS-specific provisions; treated like Tier 2 (detailed in `comprehensive`, deviation-only in `quick_triage`).

For each item, classify: **Present and standard** / **Present but unusual** / **Missing** / **N/A**.

Items marked with † are particularly perspective-sensitive — the same clause language reads very differently depending on which side the user is on. See `perspective_lens.md` for how to flip the lens.

## Tier 1 — Always reviewed in detail

### 1.1 Limitation of Liability †

**What it is:** the clause capping each party's aggregate liability arising under the agreement.

**What "standard" looks like:**
- Mutual cap, typically expressed as fees paid in the prior 12 months. Some enterprise deals run higher (24 months, 2x annual fees) or use multipliers.
- Carve-outs from the cap for: confidentiality breach, indemnification obligations, gross negligence, willful misconduct, infringement, and the customer's payment obligations.
- Many MSAs include a "super-cap" for specific high-stakes categories — security incidents involving customer data, breaches of data protection obligations — typically 2x or 3x the base cap.
- Mutual exclusion of indirect, incidental, consequential, special, exemplary, and punitive damages, with carve-outs that mirror the cap carve-outs.

**What's unusual:**
- Cap below 12 months of fees (favors vendor; problematic for customer).
- Cap above 24 months without an enterprise-grade context (favors customer; unusual but not problematic).
- Missing standard carve-outs (gross negligence, willful misconduct, IP indemnification, customer payment obligations) — flag whichever side is disadvantaged.
- Asymmetric caps in a "mutual" cap clause.
- No super-cap for security incidents in deals where customer data is sensitive (problematic for customer in security-sensitive deals).
- Caps that include or exclude "amounts paid" inconsistently between sections.
- Limitation of liability provisions that appear to cap the customer's payment obligations (always a drafting error; flag).
- Liquidated damages provisions in addition to the cap structure (uncommon; flag).

### 1.2 Indemnification †

**What it is:** mutual or one-sided obligations to defend and pay damages for specified third-party claims.

Standard SaaS MSAs typically have three indemnification components:

- **Vendor's IP indemnity:** vendor indemnifies customer against third-party IP infringement claims arising from the service. Standard exceptions: customer's modification of the service, combination with third-party products, customer's use in violation of agreement, customer-provided content.
- **Customer's content/use indemnity:** customer indemnifies vendor against third-party claims arising from customer's data, customer's use of the service in violation of laws, or customer's misuse.
- **Mutual confidentiality indemnity:** sometimes present, sometimes folded into general damages claims.

**What "standard" looks like:**
- Vendor IP indemnity covering claims that the service infringes third-party patents, copyrights, trademarks, or trade secrets.
- Standard exceptions to vendor IP indemnity (modification, combination, customer content, etc.).
- Vendor's right and obligation to: defend the claim, control settlement, and either replace the infringing component, modify it to be non-infringing, obtain a license, or refund.
- Customer indemnity scoped to customer's content, customer's misuse, and customer's violations.
- Procedural mechanics: prompt notice, control of defense, cooperation, no settlement without consent.

**What's unusual:**
- No vendor IP indemnity at all — flag as critical for customer; standard for some vendors but problematic.
- Vendor IP indemnity excludes patents (sometimes structured as "no patent indemnity" in cost-sensitive deals; flag for customer).
- "Sole and exclusive remedy" language for IP infringement that would limit customer's other recourse — increasingly viewed as overreach; flag for customer.
- Customer indemnity scope that extends beyond customer's actual conduct (e.g., "any claim arising out of customer's use of the service" without limitation) — favors vendor.
- Indemnity capped at the LoL cap (which would make the indemnity nearly worthless for high-value claims) — flag whichever side is disadvantaged.
- No procedural protections (no notice requirement, no cooperation, no consent for settlement) — favors the indemnified party in some respects but creates uncertainty.

### 1.3 Intellectual Property and Customer Data Ownership †

**What it is:** allocation of IP rights between vendor's service IP and customer's data and content.

**What "standard" looks like:**
- Vendor owns all IP in the service, including the platform, software, documentation, and any improvements vendor makes (whether based on customer feedback or otherwise).
- Customer owns all IP in customer data — the data customer uploads to or generates within the service.
- Customer grants vendor a license to use customer data solely for purposes of providing the service (and, sometimes, narrow ancillary purposes — service improvement, anonymized analytics).
- Feedback provided by customer becomes vendor's property or licensable to vendor (depending on the drafting).
- Customer retains all rights not expressly granted.

**What's unusual:**
- Customer data licensed to vendor for vendor's "internal business purposes" beyond service operation — flag as material for customer.
- Customer data licensed to vendor for "service improvement" without customer opt-out — increasingly contested; flag as material for customer.
- Customer data licensed for "training of machine learning models" or "training of AI/ML systems" — flag as critical for customer in deals where customer data is sensitive or proprietary; this is the dominant new issue in 2025-2026 SaaS deals.
- "Aggregated and anonymized" data carve-outs that effectively allow vendor to monetize customer data — flag for customer; the anonymization standard is often weaker than the GDPR's.
- Feedback provisions that assign all customer feedback to vendor without limitation — flag as material for customer.
- Vendor IP grant to customer that is narrower than necessary to use the service (e.g., excludes customer's own service users in a multi-tier resale model) — flag for customer.
- Vendor's IP grants tied to specific deployment models that don't match the actual deployment — flag.

### 1.4 Data Protection (DPA Reference)

**What it is:** the MSA's incorporation of and reference to a Data Processing Agreement.

**What "standard" looks like:**
- Express incorporation of a DPA (either appended to the MSA as an exhibit or executed separately).
- Statement that the DPA controls data protection terms; the MSA does not duplicate substantive DPA terms.
- Reference to the applicable regulatory regimes (GDPR, US state privacy, HIPAA where applicable, etc.).
- The DPA itself is then reviewed by the DPA Checklist Review skill, not by this MSA review.

**What's unusual:**
- No DPA at all — flag as critical for customer if any personal data is being processed; flag as material for vendor (regulatory exposure).
- DPA "available on request" but not attached or pre-executed — flag as material; the operative DPA terms should be locked at MSA signing.
- DPA terms scattered through MSA without a structured DPA document — flag as material; the unbundled approach makes compliance assessment difficult.
- Reference to a DPA that is dated (e.g., "the parties' 2020 DPA") in a regime that has materially changed (CCPA→CPRA, GDPR transfer mechanism updates) — flag as material; DPA may be stale.

### 1.5 Warranties and Disclaimers †

**What it is:** vendor's affirmative warranties about the service and the disclaimer of other warranties.

**What "standard" looks like:**
- **Express warranties (vendor):** service will perform substantially in accordance with documentation; service will be provided in a workmanlike manner; vendor has the right to provide the service; service will not introduce malicious code; vendor maintains a security program (often by reference to a Trust Center or security exhibit).
- **Disclaimer:** of all other warranties, express or implied, including merchantability, fitness for a particular purpose, non-infringement (typically already covered by IP indemnity), accuracy, and uninterrupted operation.
- **Customer warranties:** customer has the right to provide its data; customer's data does not violate third-party rights; customer's use complies with applicable laws.

**What's unusual:**
- Missing the basic vendor express warranties (workmanlike performance, right to provide service) — flag as critical for customer.
- Disclaimer of warranties that haven't been disclaimed in the express warranties — internal inconsistency, flag.
- Disclaimer of vendor's data protection or security commitments — flag as critical for customer.
- "AS IS" service warranty without any express warranty — vendor-aggressive; flag as critical for customer.
- Customer warranty extending beyond customer's actual control (e.g., "customer warrants that customer's users will not violate AUP") — flag for customer; customer should warrant only its own conduct.

### 1.6 Term and Termination †

**What it is:** how long the agreement lasts, how it renews, and how it can be terminated.

**What "standard" looks like:**
- **Term:** initial term of one to three years, with auto-renewal unless either party gives notice of non-renewal (typically 30–90 days before end of term).
- **Termination for cause:** either party can terminate for material breach by the other, with notice and cure period (typically 30 days).
- **Termination for convenience:** sometimes — if present, typically allows the customer to terminate with refund of unused fees, often with a cap on refund or a notice period.
- **Termination for insolvency:** either party can terminate on the other party's bankruptcy, insolvency, or assignment for benefit of creditors.
- **Effect of termination:** customer pays all amounts owed; vendor stops providing service; data return/deletion per DPA; survival of confidentiality, indemnification, payment, limitation of liability, and other relevant provisions.

**What's unusual:**
- **Vendor-favorable patterns to flag:**
  - Long auto-renewal opt-out windows (60+ days) — favors vendor.
  - Unilateral price increases at renewal beyond a stated cap — flag for customer.
  - No customer termination for convenience — typical but worth noting in long-term deals.
  - Termination-for-cause notice/cure that effectively prevents customer's exit (excessively long cure periods, ambiguous breach definitions).
- **Customer-favorable patterns to flag:**
  - Customer termination for convenience without proportionate refund cap — favors customer.
  - Aggressive vendor termination liability (e.g., forfeiture of all prepaid amounts on vendor's termination for cause) — flag for vendor.
- **Both-side issues:**
  - No termination-for-insolvency provision — both parties should want this.
  - Auto-renewal mechanics with no notice obligation from vendor (customer must remember the deadline unilaterally) — flag for customer.
  - "Termination for change of control" provisions that aren't symmetric (e.g., vendor can terminate on customer's change of control but not vice versa) — flag.

### 1.7 Payment, Pricing, and Renewal Pricing †

**What it is:** the financial terms — what the customer pays, when, how, and how prices change at renewal.

**What "standard" looks like:**
- **Pricing:** specified in Order Form; MSA reserves Order Form precedence on pricing.
- **Invoicing:** typically annual in advance for SaaS subscriptions; payment net 30 from invoice.
- **Late fees:** typically 1.5% per month on overdue amounts (or the maximum permitted by law).
- **Suspension/acceleration:** vendor may suspend service for non-payment after notice and cure period (typically 10–15 days); some MSAs include acceleration of all remaining contract value on uncured breach.
- **Renewal pricing:** either fixed (uncommon) or capped (e.g., "no more than CPI + X%" or "no more than 5% per year"). Sometimes uncapped (vendor-favorable).
- **Tax:** customer pays applicable taxes; vendor responsible for its own income tax.

**What's unusual:**
- **No cap on renewal price increases** — flag as material for customer; multi-year renewals can balloon unpredictably.
- **Suspension rights without notice or cure period** — flag as critical for customer; vendor can take service offline without warning.
- **Acceleration clauses** that demand all remaining contract value on minor breach — flag as material; converts ordinary breach disputes into existential financial events.
- **Late fees beyond statutory maximum** — flag as minor (state usury law may make excess unenforceable).
- **Right to charge for usage above committed levels** without notice or cap — flag for customer.
- **Payment of "fees and any other charges as billed"** without itemization — flag for customer; transparency issue.

### 1.8 Service Level Agreement (SLA)

**What it is:** vendor's commitments on service availability, performance, and the customer's remedies for SLA breach.

**What "standard" looks like:**
- **Uptime commitment:** typically 99.5% to 99.99% for enterprise-grade SaaS.
- **Calculation methodology:** monthly basis; excluded periods (scheduled maintenance, force majeure, customer-caused issues).
- **Remedies:** SLA credits typically 5–10% of monthly fees per percentage point below commitment, with a cap (typically 25–50% of monthly fees).
- **Remedy as exclusive:** SLA credits typically stated as customer's "sole and exclusive remedy" for SLA misses; carve-outs sometimes for material/repeated breaches.
- **Reporting:** vendor provides uptime reports; customer must request credits within a stated period.

**What's unusual:**
- **No SLA at all** — flag as material for customer in any non-trivial deal; flag for vendor as missing customer expectation.
- **Uptime commitment below 99.5% in an enterprise context** — flag for customer.
- **Excessive exclusion list** that effectively eliminates the SLA (e.g., "scheduled maintenance" with no time bound or "force majeure" defined to include vendor's own infrastructure failures) — flag for customer.
- **SLA credits as truly exclusive remedy** even for repeated material failures — flag for customer; customers typically want exit rights for chronic SLA breach.
- **No customer right to terminate for chronic SLA breach** — flag for customer.
- **Asymmetric SLA reporting** (customer must report incidents within 24 hours but vendor reports monthly) — flag for customer.

## Tier 2 — Reviewed in detail in `comprehensive` only

### 2.1 Confidentiality

**What it is:** mutual confidentiality obligations covering information shared between the parties (distinct from customer data and DPA terms).

**Standard pattern:** mutual confidentiality with carve-outs (publicly available, prior knowledge, independent development, third-party receipt, compelled disclosure with notice). Term typically 3–5 years post-termination.

**Unusual:** missing entirely; one-sided when both parties share confidential information; perpetual obligations on broad categories.

### 2.2 Assignment

**Standard pattern:** mutual restriction with consent; carve-outs for change of control, M&A, internal reorganization. Either party retains right to assign to successor.

**Unusual:** unilateral right by one party; broad consent rights that block legitimate M&A; assignment to direct competitor of the other party (sometimes flagged in customer-favorable templates).

### 2.3 Governing Law and Venue

**Standard pattern:** specified state's law and forum (state or federal court in that state) or arbitration with specified rules. Delaware, New York, and California are the most common state choices.

**Unusual:** no governing law specified; vendor's home jurisdiction in a jurisdiction with no nexus to the deal; non-US jurisdiction in an otherwise-US deal; mandatory arbitration in a venue inconvenient to customer.

### 2.4 Dispute Resolution

**Standard pattern:** specifies how disputes are resolved — court litigation, arbitration (JAMS, AAA, ICC, CPR), or tiered (negotiation → mediation → arbitration). Arbitration choices specify the rules, the seat, and the language.

**Unusual:** mass arbitration prohibitions that block class actions; mandatory pre-suit mediation that delays equitable relief; arbitration with class waiver in jurisdictions where consumer-protection rules invalidate.

### 2.5 Force Majeure †

**Standard pattern:** mutual carve-out for events beyond reasonable control. Typically excuses non-performance other than payment obligations. Includes notice, mitigation, and termination right if FM continues beyond X days.

**Unusual:**
- FM defined to include vendor's own infrastructure failures or cloud-provider outages — flag for customer; this swallows the SLA.
- Asymmetric — excuses vendor's service failure but not customer's payment obligation (typical and acceptable; flag if extreme).
- No termination right after extended FM — flag.

### 2.6 Change-of-Terms Mechanics †

**What it is:** vendor's right to modify the MSA, AUP, or service over time.

**Standard pattern:** vendor may modify the AUP and operational policies on notice; material changes to MSA terms require customer consent or trigger customer's right to terminate without penalty.

**Unusual:**
- Unilateral right to modify all MSA terms on notice — flag as critical for customer.
- "Continued use constitutes acceptance" of modified terms without customer's express opt-in or termination right — flag as critical for customer.
- AUP modifications without notice — flag as material.

### 2.7 Suspension and Acceleration

Already covered in §1.7 above.

### 2.8 Professional Services Scope

If the MSA includes professional services (implementation, configuration, integration, training):

**Standard pattern:** PS scope governed by SOW; deliverables specified in SOW; PS-specific warranties (workmanlike performance, IP rights in deliverables); customer ownership of PS deliverables (with vendor retaining IP in pre-existing tools).

**Unusual:** PS terms scattered without clear SOW reference; vendor IP ownership of PS deliverables (typical for vendor-favorable templates; flag for customer); broad customer indemnity for PS-related claims; PS warranty disclaimers that swallow the warranty.

### 2.9 Third-Party Components

**What it is:** disclosure of and terms for third-party components or sub-services included in the SaaS offering.

**Standard pattern:** vendor identifies third-party components (typically in a schedule or by reference to a website); pass-through of third-party terms where applicable; vendor remains responsible for third-party performance under the MSA.

**Unusual:** broad disclaimers of vendor responsibility for third-party components — flag as critical for customer if third-party components are material to service delivery; missing identification of third-party components when service obviously depends on them; pass-through of third-party terms that conflict with the MSA.

## Tier 3 — Reviewed in detail in `comprehensive` only

### 3.1 Notice mechanics

Email + physical mail typically; specified addresses; deemed delivered timing.

### 3.2 Integration / Entire Agreement

Standard integration clause; amendments in writing.

### 3.3 Amendment Requirements

Already covered in §2.6 (change-of-terms mechanics) where unilateral modification is contemplated.

### 3.4 Severability

Standard severability clause.

### 3.5 Waiver

Standard non-waiver clause.

### 3.6 Counterparts and Electronic Signatures

Standard.

### 3.7 Definitions Completeness

Verify that defined terms are actually defined; flag undefined uses or used terms that aren't defined.

### 3.8 Headings

Standard "headings are for convenience only" clause.

## Tier 4 — SaaS-specific provisions

### 4.1 Acceptable Use Policy (AUP)

**Standard pattern:** AUP referenced or attached; restrictions on customer use (no malicious code, no service abuse, no resale or unauthorized access, no scraping); vendor's right to enforce AUP via suspension or termination.

**Unusual:** AUP terms that effectively block legitimate use; vendor's right to unilaterally modify AUP without notice; AUP enforcement without notice or cure.

### 4.2 Customer Data Definition

**Standard pattern:** "Customer Data" defined as data submitted by or for customer; customer retains ownership; clear distinction from "Vendor Data" (operational telemetry, anonymized usage data).

**Unusual:** narrow Customer Data definition that excludes data customer expects to be customer's; vendor data definition that includes customer-identifying data.

### 4.3 Data Residency and Localization

**Standard pattern:** vendor specifies data center locations; data residency commitments where customer requires; sub-processor disclosure (typically by reference to DPA).

**Unusual:** no commitment on data location; right to move data without notice; data residency commitments that don't match vendor's actual infrastructure.

### 4.4 Sub-processor Management

Typically covered by DPA. MSA-level reference should track DPA.

### 4.5 Audit Rights †

**Standard pattern:** customer's audit rights typically routed through SOC 2 Type II reports plus on-site audit on cause; vendor's audit rights typically of customer's compliance with AUP and license metrics.

**Unusual:** asymmetric audit rights (vendor audits customer but not vice versa); vendor's broad audit rights with substantial fees; no customer audit rights even via report review.

### 4.6 Security Incident Response

**Standard pattern:** typically covered by DPA; MSA-level reference should track. Where MSA contains independent security incident provisions, check timeline (24-72 hours typical), required content, cooperation obligations.

### 4.7 Business Continuity / Disaster Recovery

**Standard pattern:** stated RTO and RPO commitments; reference to BC/DR plan; testing cadence.

**Unusual:** missing entirely in enterprise contracts (flag); vague commitments without specific RTO/RPO.

### 4.8 Support and Maintenance Windows

**Standard pattern:** support hours specified; response time commitments by severity tier; planned maintenance windows.

**Unusual:** unspecified maintenance windows; response time commitments that don't match SLA exclusions.

### 4.9 Third-Party Authentication and SSO

**Standard pattern:** support for SAML 2.0, OIDC, SCIM (where applicable); customer's responsibility for IdP configuration; vendor's responsibility for federation reliability.

**Unusual:** SSO available only on premium tier (flag for enterprise customer); vendor's right to charge for SSO (becoming less common but historically present).

### 4.10 API Rate Limits and Overage Handling

**Standard pattern:** rate limits specified in documentation; overage handling specified (throttling, blocking, billing for additional capacity); customer notification before service-affecting limits.

**Unusual:** rate limits not documented; overage handling that allows vendor to suspend service without notice; overage billing without cap.
