# Worked Example — Customer Perspective, Vendor-Prepared SaaS MSA

This example shows the skill applied to a vendor-drafted SaaS MSA from the customer's perspective. The scenario: a Fortune 1000 enterprise customer is evaluating a new SaaS analytics platform; the vendor has presented its standard MSA template.

## Input

**Perspective:** customer
**Review depth:** comprehensive
**Jurisdiction:** Delaware (governing law in the document)
**Deal context:** "First-time vendor evaluation; multi-year enterprise deal contemplated; service will process customer transactional data including PII"
**Order Form provided:** no
**Prior agreements:** "We executed a mutual NDA with this vendor 8 months ago for the evaluation."

**Document (excerpts — actual document is 28 pages, 14 sections):**

> **§7.1 Limitation of Liability.** EXCEPT FOR LIABILITY ARISING FROM (A) A PARTY'S BREACH OF CONFIDENTIALITY OBLIGATIONS, (B) A PARTY'S INDEMNIFICATION OBLIGATIONS, OR (C) CUSTOMER'S PAYMENT OBLIGATIONS, IN NO EVENT SHALL EITHER PARTY'S TOTAL AGGREGATE LIABILITY ARISING OUT OF OR RELATING TO THIS AGREEMENT EXCEED THE FEES PAID OR PAYABLE BY CUSTOMER TO VENDOR DURING THE SIX (6)-MONTH PERIOD IMMEDIATELY PRECEDING THE EVENT GIVING RISE TO LIABILITY.
>
> **§8.1 Vendor IP Indemnity.** Vendor shall defend Customer against any third-party claim that Customer's authorized use of the Service infringes such third party's United States patent, copyright, or trade secret rights, and shall pay damages finally awarded against Customer with respect to such claims, provided that Customer (i) promptly notifies Vendor in writing of the claim, (ii) gives Vendor sole control of the defense and settlement, and (iii) provides reasonable cooperation. Vendor's obligations under this Section 8.1 shall not apply to claims arising from (a) modification of the Service by anyone other than Vendor, (b) combination of the Service with products or services not provided by Vendor, (c) Customer Data or Customer's content, or (d) Customer's use of the Service in violation of this Agreement.
>
> **§9.2 Customer Data License.** Customer hereby grants to Vendor a worldwide, non-exclusive, royalty-free license to access, use, copy, transmit, and display Customer Data solely as necessary to provide the Service and for Vendor's internal business purposes, including without limitation product improvement, training of artificial intelligence and machine learning models, security analytics, and benchmarking. Customer Data may be used in aggregated and anonymized form for any purpose.
>
> **§9.3 Feedback.** Any suggestions, ideas, comments, or feedback provided by Customer regarding the Service shall become the sole property of Vendor, and Customer hereby assigns all right, title, and interest in such feedback to Vendor.
>
> **§10.1 Service Level Agreement.** Vendor commits to a monthly uptime of 99.5%, calculated as the percentage of total minutes in a month during which the Service is Available. The SLA excludes (i) scheduled maintenance, (ii) emergency maintenance, (iii) Force Majeure Events, (iv) issues caused by Customer or Customer's third-party providers, (v) issues caused by Vendor's third-party cloud infrastructure providers, and (vi) any factor beyond Vendor's reasonable control. Customer's sole and exclusive remedy for any SLA failure is service credits as set forth in the SLA Policy at [URL].
>
> **§11.1 Term.** The initial term of this Agreement is three (3) years from the Effective Date. The Agreement shall automatically renew for successive one (1)-year periods unless either party provides written notice of non-renewal at least ninety (90) days prior to the end of the then-current term.
>
> **§11.4 Termination for Convenience.** Customer has no right to terminate this Agreement for convenience during the initial term or any Renewal Term.
>
> **§11.5 Renewal Pricing.** Vendor may increase fees for any Renewal Term to reflect Vendor's then-current pricing, in Vendor's sole discretion.
>
> **§12.3 Modifications.** Vendor may modify this Agreement, the Acceptable Use Policy, and the SLA Policy at any time by providing notice to Customer (which may be provided via Customer's account dashboard or by email). Customer's continued use of the Service after such notice constitutes acceptance of the modifications.
>
> **§13.4 Suspension.** Vendor may suspend the Service or Customer's access to the Service immediately upon notice if Customer (a) fails to pay any amount when due, (b) violates the Acceptable Use Policy, (c) breaches this Agreement, or (d) Vendor reasonably believes that suspension is necessary to protect the Service or other customers.
>
> *(Other excerpts truncated for brevity.)*

## Output

# MSA Review — SaaS: [Vendor] Master Subscription Agreement

**Perspective:** Customer
**Review depth:** Comprehensive
**Document type:** SaaS Master Subscription Agreement
**Governing law:** Delaware
**Term:** 3 years initial, auto-renews 1 year, 90-day non-renewal notice
**Order Form provided:** No
**Prior agreements considered:** Mutual NDA dated [8 months ago]

## Bottom line

**Materially unfavorable to customer; not signable as drafted.** The MSA contains six critical issues that, individually, each warrant negotiation, and that, collectively, make the document substantially below market for a multi-year enterprise deal involving customer PII. The most consequential issues are: (1) ML training rights on customer data without opt-out (§9.2); (2) liability cap at 6 months of fees with no super-cap for security incidents (§7.1); (3) 99.5% SLA with exclusions broad enough to swallow the commitment, including vendor's own cloud provider (§10.1); (4) unilateral right to modify all MSA terms by notice with continued-use deemed acceptance (§12.3); (5) suspension rights without notice or cure (§13.4); and (6) 90-day non-renewal opt-out window with no cap on renewal price increases (§11.1, §11.5). These are not edge-case findings; they are core commercial terms that an enterprise customer in this category should not accept. Recommend either substantial negotiation across these six items, or proposing customer's own template instead.

## Critical issues

### §7.1 — Liability cap below market with no super-cap for security incidents

**What the document says:** mutual cap at 6 months of fees paid, with carve-outs for confidentiality breach, indemnification, and customer payment obligations. No super-cap for any category of damages.

**Why it's a problem:** for an enterprise SaaS MSA processing customer PII, market-standard liability cap is 12 months of fees minimum; many enterprise deals run to 24 months or 2x annual fees. A 6-month cap is materially below market and creates substantial exposure on data-related incidents. More problematically, there is no super-cap for security incidents — an industry-standard convention is to provide 2x or 3x the base cap for data breach and security incident damages. Without super-cap, the customer's recovery in a data breach is limited to what amounts to roughly half of one year's contract fees, which is unlikely to cover even direct breach response costs (notification, credit monitoring, forensic investigation), much less downstream damages (regulatory fines, civil litigation, reputational harm).

**Recommended language for §7.1:**

> "Except for liability arising from (a) a party's breach of confidentiality obligations, (b) a party's indemnification obligations, (c) Customer's payment obligations, (d) a party's gross negligence or willful misconduct, or (e) a Security Incident as defined in the DPA, in no event shall either party's total aggregate liability arising out of or relating to this Agreement exceed the fees paid or payable by Customer to Vendor during the twelve (12)-month period immediately preceding the event giving rise to liability. **Notwithstanding the foregoing, with respect to liability arising from a Security Incident, the cap shall be three times (3x) the amount set forth in the preceding sentence.**"

### §9.2 — ML training rights on customer data without opt-out

**What the document says:** customer grants vendor a license to use customer data for "internal business purposes, including without limitation product improvement, training of artificial intelligence and machine learning models, security analytics, and benchmarking." Aggregated and anonymized data may be used for "any purpose."

**Why it's a problem:** the license to use customer data for ML training is the dominant 2025-2026 issue in SaaS contracts and the most serious finding in this document for an enterprise customer. Customer data used for ML training can produce model behavior that reflects customer-specific patterns and information; even with claimed anonymization, model weights can encode customer-identifying signals. For a customer processing transactional data including PII, this is a fundamental data-protection issue. Beyond the ML concern, the broader "internal business purposes" language extends well beyond what is necessary to provide the service.

The "aggregated and anonymized" carve-out provides limited protection. The anonymization standard is unspecified; vendor's anonymization may be weaker than GDPR-grade, and aggregated outputs from a single customer's data can still reveal customer-identifying information if the customer's data is distinctive.

**Recommended language for §9.2:**

> "Customer hereby grants to Vendor a worldwide, non-exclusive, royalty-free license to access, use, copy, transmit, and display Customer Data **solely as necessary to provide the Service to Customer and to perform Vendor's obligations under this Agreement**. Vendor shall not use Customer Data for any other purpose, including but not limited to product improvement, training of artificial intelligence or machine learning models, marketing, benchmarking, or sale to third parties. Vendor's use of Customer Data shall be subject to the data protection obligations set forth in the Data Processing Agreement."

If vendor is unable to remove ML training rights entirely, the fallback position is: explicit opt-in with documented mechanism, narrow scope to specific model categories that do not produce customer-identifying outputs, GDPR-grade anonymization standard, and IP indemnity for any model output that reflects customer data.

### §10.1 — SLA exclusions swallow the commitment, including vendor's own cloud provider

**What the document says:** 99.5% uptime commitment with exclusions including "issues caused by Vendor's third-party cloud infrastructure providers" and "any factor beyond Vendor's reasonable control."

**Why it's a problem:** the cloud-infrastructure exclusion is critical. Modern SaaS services run on cloud infrastructure (AWS, Azure, GCP); excluding cloud-provider issues from SLA effectively excludes most operational outages, since most outages trace to cloud-infrastructure issues. The "any factor beyond Vendor's reasonable control" clause is even broader and effectively unlimited.

A 99.5% uptime commitment is also below enterprise market — 99.9% is standard for enterprise SaaS, with 99.95% or 99.99% for tier-1 services. SLA credits as "sole and exclusive remedy" forecloses customer's exit rights even for chronic SLA breach.

**Recommended language for §10.1:**

Replace exclusions with narrowly-defined list:

> "The SLA excludes only the following: (i) scheduled maintenance windows of which Vendor has provided at least seventy-two (72) hours advance notice; (ii) emergency maintenance required to address active security threats, with prompt subsequent notice to Customer; (iii) Force Majeure Events as defined in Section [X], excluding for clarity any failure of Vendor's third-party cloud infrastructure providers (such failures are Vendor's responsibility); (iv) issues directly caused by Customer's actions in violation of this Agreement; and (v) issues directly caused by Customer's third-party providers operating outside the Service."

Increase uptime commitment to 99.9% as floor; consider 99.95% if deal value warrants.

Add chronic-SLA-breach termination right:

> "If Vendor fails to meet the SLA in three (3) months within any rolling six (6)-month period, Customer may terminate this Agreement for cause upon written notice, with refund of any prepaid amounts attributable to the period after termination."

### §12.3 — Unilateral right to modify all MSA terms

**What the document says:** vendor may modify the Agreement, AUP, and SLA Policy at any time by notice; continued use constitutes acceptance.

**Why it's a problem:** this turns the entire MSA into a moving target. Vendor can unilaterally change liability terms, payment terms, data protection terms, indemnity scope, anything. "Continued use constitutes acceptance" is a contract of adhesion structure that is increasingly disfavored, particularly for material commercial terms. Customer cannot meaningfully evaluate the deal because what customer signs is not necessarily what customer is bound to.

**Recommended language for §12.3:**

> "Vendor may modify the Acceptable Use Policy and the SLA Policy upon at least thirty (30) days' prior written notice to Customer, provided that any modification that materially decreases Customer's rights or materially increases Customer's obligations shall require Customer's prior written consent. Modifications to this Agreement (other than the Acceptable Use Policy and SLA Policy) require the mutual written agreement of both parties. Customer's continued use of the Service shall not constitute acceptance of any modification."

### §13.4 — Suspension without notice or cure

**What the document says:** vendor may suspend the service or customer's access immediately upon notice for non-payment, AUP violation, breach, or vendor's reasonable belief that suspension is necessary.

**Why it's a problem:** for a customer integrating this analytics platform with operational systems, even a few hours of suspension causes business disruption; a few days can be catastrophic. Suspension "immediately upon notice" with no cure period is unworkable for enterprise services. Vendor's reasonable-belief standard for protective suspension is overly permissive.

**Recommended language for §13.4:**

> "Vendor may suspend the Service or Customer's access to the Service in the following circumstances:
>
> (a) For non-payment of undisputed amounts, after providing at least fifteen (15) days' written notice and an opportunity to cure;
>
> (b) For material violation of the Acceptable Use Policy, after providing notice and a reasonable opportunity to cure (with cure period proportional to the nature of the violation, but in no case less than five (5) business days);
>
> (c) Immediately, upon notice, if and only if Vendor reasonably and in good faith believes that immediate suspension is necessary to prevent material harm to the Service, to other customers, or to third parties; in such case, Vendor shall promptly work with Customer to restore service as soon as the harm is mitigated.
>
> Suspension does not excuse Customer's payment obligations only to the extent the suspension is for Customer's non-payment; for any other suspension, Customer's payment obligations are tolled during the suspension period."

### §11.1 + §11.5 — 90-day non-renewal window with no cap on renewal pricing

**What the document says:** auto-renewal with 90-day notice of non-renewal; renewal pricing in vendor's "sole discretion."

**Why it's a problem:** 90-day opt-out window is aggressive (60-day standard); combined with no cap on renewal pricing, customer faces unbounded financial commitment with limited ability to exit. The user must remember the deadline 90 days in advance, calculate it correctly relative to a 3-year initial term, and predict whether to renew without knowing renewal pricing (vendor sets pricing in sole discretion). This is a structural lock-in mechanism.

**Recommended language for §11.1 and §11.5:**

> "**§11.1 Term.** The initial term of this Agreement is three (3) years from the Effective Date. The Agreement shall automatically renew for successive one (1)-year periods unless either party provides written notice of non-renewal at least sixty (60) days prior to the end of the then-current term. Vendor shall provide Customer with written notice ninety (90) days before the non-renewal deadline reminding Customer of the upcoming deadline; failure to provide such notice extends the non-renewal deadline by thirty (30) days.
>
> **§11.5 Renewal Pricing.** Vendor may increase fees for any Renewal Term, provided that any such increase shall not exceed the greater of (a) the percentage increase in the Consumer Price Index for All Urban Consumers (CPI-U) for the prior twelve months or (b) five percent (5%). Vendor shall notify Customer of any proposed renewal pricing at least one hundred twenty (120) days prior to the end of the then-current term."

## Material issues

### §8.1 — Patent indemnity scope

The vendor IP indemnity in §8.1 covers "United States patent, copyright, or trade secret rights." It does not cover trademark, foreign-jurisdiction patents, or any other IP rights. For an enterprise customer with international operations, this is a meaningful gap.

**Recommended adjustment:** extend scope to all IP rights in jurisdictions where vendor markets the service (typically US plus jurisdictions where customer's authorized users are located).

### §9.3 — Feedback assignment

Feedback assignment to vendor is broadly scoped. For an enterprise customer that may be in adjacent technology spaces, this could capture customer-developed ideas in customer's own product roadmap.

**Recommended adjustment:** narrow feedback assignment to feedback specifically about vendor's service; preserve customer's rights in customer's pre-existing IP and customer's product development.

### Missing: DPA reference

The MSA does not reference a Data Processing Agreement. For a service processing customer PII, this is a critical gap, but it's listed as material here because the user can typically request a DPA and the vendor likely has one available.

**Recommended adjustment:** require execution of a DPA as a condition of MSA effectiveness; review DPA against applicable regimes (GDPR if EU resident data; US state privacy if US resident data) using DPA Checklist Review.

## Minor issues and observations

- **Governing law:** Delaware. Acceptable; neutral commercial forum.
- **Jurisdiction/venue:** not shown in excerpts; verify.
- **Confidentiality:** not shown in excerpts; verify it's mutual and runs at least 3 years.
- **Notice mechanics:** not shown in excerpts; verify email + physical mail with reasonable deemed-delivery timing.
- **Counterparts and electronic signatures:** verify standard clause is present.
- **Definitions:** verify "Service," "Customer Data," "Confidential Information," "Material Breach," and other operative terms are clearly defined.
- **Acceptable Use Policy:** §12.3 references AUP modification rights; verify AUP is attached or available at signing.
- **Audit rights:** not shown in excerpts; verify customer audit rights are present (typically SOC 2 report review with on-site audit on cause).

## Missing standard protections

- **DPA reference (see above).**
- **Super-cap for security incidents** (addressed in §7.1 redline above).
- **Termination for chronic SLA breach** (addressed in §10.1 redline above).
- **No-license language** in IP section: explicit statement that disclosure of confidential information does not grant any IP rights. Standard but verify presence.
- **Bankruptcy / insolvency termination right** for both parties.
- **Source code escrow** for an enterprise deal of this size — not mandatory but increasingly common; consider requesting.

## Operational red flags

- **§9.2 ML training rights** — addressed as critical above.
- **§12.3 unilateral modification** — addressed as critical above.
- **§13.4 suspension without notice** — addressed as critical above.
- **No customer termination for convenience (§11.4)** — typical for enterprise SaaS but worth user awareness; combined with the issues above, customer's optionality is significantly limited.

## Conflicts with prior agreements

The user provided that a mutual NDA was executed 8 months ago. The MSA's confidentiality provisions (not shown in excerpts; verify presence) should be reviewed for consistency with that NDA. Specifically: (i) does the MSA explicitly preserve or supersede the NDA? (ii) do the MSA's confidentiality terms cover the same scope? (iii) do the survival periods align? Common drafting issue: MSA has integration clause ("entire agreement") that would extinguish the NDA, leaving information shared during evaluation potentially unprotected if MSA confidentiality is narrower. Verify and resolve.

## Recommended next steps

1. **Do not sign as-is.** The combination of six critical issues makes the MSA materially below market for an enterprise deal of this size and sensitivity.
2. **Negotiate the redlines proposed above.** The recommendations on §7.1, §9.2, §10.1, §12.3, §13.4, §11.1/§11.5 should be non-negotiable for the customer. Material issues (§8.1, §9.3, DPA) are the second tier.
3. **Consider proposing customer's own MSA template instead.** With six critical issues plus material issues, redrafting may be more efficient than incremental redlining. If customer has an enterprise SaaS MSA template, presenting that template may be faster.
4. **Require execution of DPA as condition of MSA effectiveness.** Run DPA Checklist Review against the resulting DPA.
5. **Verify all referenced documents are attached or pre-executed at signing.** AUP, SLA Policy, DPA, security exhibit (if any).
6. **Address conflicts with the existing mutual NDA.** Either preserve the NDA's protections via explicit reservation in the MSA's integration clause, or migrate the NDA's protections into the MSA's confidentiality section.

## Items requiring human judgment

- **Negotiation strategy:** the user has six critical issues. Whether to push hard on all of them, prioritize a subset, or propose customer's own template depends on the user's leverage with this vendor (deal size, alternative providers, timing pressure) — which the skill cannot assess.
- **Specific liability cap level:** 12 months of fees is the recommended floor, but the appropriate cap for this specific deal depends on potential damages from a worst-case scenario (data breach magnitude, business disruption magnitude). Customer's risk team should model.
- **ML training rights:** if vendor refuses to remove ML training rights entirely, the fallback positions (explicit opt-in, narrow scope, GDPR-grade anonymization) are negotiation points. Customer's data classification team should advise on whether any ML use of customer's transactional data is acceptable.
- **Whether to proceed with this vendor at all:** with this many critical issues, the user may want to assess whether this vendor is a viable partner. If competing alternatives have more market-aligned MSAs, the negotiation cost may exceed the value of this specific vendor.

---

## What this example demonstrates

- **Six critical issues, all distinct.** Severity calibration to a vendor-favorable enterprise MSA from customer perspective. The rubric's expectation ("typical commercial SaaS MSA reviewed in good faith from the customer side will surface 1-3 critical issues") is exceeded here because this is a notably below-market document — which is correct for the document and the appropriate calibration.
- **The ML training rights finding is treated as the most serious issue.** This reflects the 2025-2026 commercial reality: ML training rights are the dominant new issue in SaaS contracts, and an enterprise customer processing PII should not accept default ML training language.
- **Recommended language is concrete and lawyer-grade.** Each critical finding has specific replacement language, not just "negotiate this." The customer can paste the proposed language directly into a redline.
- **Severity calibration responds to deal context.** The 6-month liability cap is severe in an enterprise deal involving customer PII; in a small-dollar SMB deal with no PII, the same cap would be material rather than critical. The skill's calibration uses `deal_context`.
- **Conflicts with prior agreements section does work.** The user provided that a mutual NDA exists; the report flags potential MSA-vs-NDA conflict and the integration-clause issue. Without `prior_agreements` input, this section would be omitted.
- **Items requiring human judgment defers what the skill cannot assess.** Negotiation strategy, cap level for specific deal, ML training acceptability, vendor viability — all routed to the user's judgment.
- **Bottom line opens with the recommendation, not the analysis.** "Materially unfavorable; not signable as drafted."
