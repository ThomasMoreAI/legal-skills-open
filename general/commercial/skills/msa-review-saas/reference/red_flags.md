# Red Flags and Operational Issues

This reference drives Pass 4 of the review. These are issues to flag *whenever they appear*, regardless of perspective, because they create operational risk, suggest the counterparty is using the MSA for purposes beyond the stated relationship, or signal that the document was drafted from a template inappropriate for the deal.

A red flag is not necessarily a deal-breaker. Many of these are negotiable or acceptable in context. But every red flag deserves explicit treatment in the review report so the user can make a deliberate business judgment.

## Provisions that signal vendor leverage

### Unilateral amendment rights

Vendor's right to modify the MSA, AUP, or service terms unilaterally on notice. The customer's "continued use" is sometimes deemed acceptance.

**Why it's a red flag:** the entire framework agreement becomes a moving target. What customer signs is not necessarily what customer is bound to. In long deals, terms can drift substantially.

**Severity:**
- Critical — if material MSA terms (liability, indemnification, data protection, payment) can be unilaterally modified.
- Material — if only AUP or operational terms can be unilaterally modified.
- Minor — if any unilateral modification is paired with a customer right to terminate without penalty.

**Mitigation:** customer should demand that material MSA changes require mutual agreement; AUP and operational changes acceptable with notice and a customer right to terminate within a reasonable window if changes are unacceptable.

### Acceleration clauses

Vendor's right to demand all remaining contract value on customer's uncured material breach.

**Why it's a red flag:** converts ordinary commercial disputes into existential financial events. A disputed late payment can trigger acceleration; even if customer eventually wins on the merits, the cash-flow impact of the acceleration demand is substantial.

**Severity:** material in most deals; critical when paired with broad breach definitions or short cure periods.

**Mitigation:** customer should limit acceleration to specific severe breaches (insolvency; final adjudication of breach; documented payment default after extended cure).

### Suspension without notice

Vendor's right to suspend service for non-payment, AUP violation, or other breach without notice or cure period.

**Why it's a red flag:** vendor can take service offline before customer has opportunity to address the alleged breach. For business-critical services, even a few hours of suspension causes customer harm; a few days can be catastrophic.

**Severity:** critical in most deals where service is business-critical; material in lower-stakes deals.

**Mitigation:** require notice (typically 10-15 days for non-payment; immediate for severe AUP violations); require cure opportunity for cure-able breaches.

### Most-favored-nation clauses on pricing or terms

Provisions requiring vendor to extend better terms to customer if vendor offers them to other customers.

**Why it's a red flag:** uncommon and operationally complex. Vendor must track all customer terms to verify compliance; customer must monitor vendor's other deals to enforce.

**Severity:** flag whenever present. Material if it creates substantial reporting burden; minor if it's narrowly scoped.

## IP and data overreach

### Customer data for vendor's "internal business purposes"

Customer-data license to vendor that extends beyond service operation to vendor's own business uses — analytics, benchmarking, marketing, model training.

**Why it's a red flag:** customer expects data to be used to provide the service. "Internal business purposes" can swallow that expectation.

**Severity:**
- Critical — if customer data is sensitive (PII, financial, health) and license includes ML training without opt-out.
- Material — if license includes broad anonymization or aggregation rights that effectively monetize customer data.
- Minor — if license is narrowly scoped to specific operational purposes (security analytics, fraud detection) with adequate safeguards.

**Mitigation:** narrow the license to specific service-operation uses; require opt-in for any use beyond service operation; require GDPR-grade anonymization for any aggregation rights.

### ML training rights on customer data

Vendor's right to use customer data for training machine-learning models.

**Why it's a red flag:** the dominant 2025-2026 issue in SaaS contracts. Customer data used for ML training can produce model behavior that reflects customer-specific information, creating IP and confidentiality risks. Even with anonymization, model weights can encode customer-specific patterns.

**Severity:** critical in most enterprise deals; material in others. The default should be no ML training rights; if vendor insists, require explicit opt-in mechanism, narrow scope to specific model categories, and IP indemnity for model output.

### Feedback assignment

Customer feedback (suggestions, ideas, improvements) becomes vendor's property.

**Why it's a red flag:** customer cannot evaluate or use the service without giving feedback. Broad feedback assignment captures customer-developed ideas.

**Severity:** material; can be critical in deals where customer is in adjacent space to vendor.

**Mitigation:** narrow feedback assignment to feedback specifically about the vendor's service; preserve customer's rights in customer's own pre-existing IP and customer's own product development.

## Termination and renewal traps

### Auto-renewal with long opt-out windows

Auto-renewal with notice periods over 60 days.

**Why it's a red flag:** customer must remember the deadline far in advance. Combined with no vendor obligation to remind customer, this becomes a "gotcha" mechanism that locks customers into renewals they didn't actively want.

**Severity:** material. Critical if combined with no termination-for-convenience and significant renewal price increases.

**Mitigation:** negotiate to 30-60 days; require vendor to send a non-renewal-deadline reminder (e.g., 90 days before deadline).

### Renewal price increase without cap

Vendor's right to set renewal pricing without limit.

**Why it's a red flag:** customer faces unbounded financial commitment in long deals. Year 3 pricing can be substantially higher than Year 1 with no recourse short of terminating.

**Severity:** material in deals over 1 year; can be critical in long-term deals.

**Mitigation:** cap on renewal increases (CPI + X%; flat percentage; mutual agreement).

### Termination-for-cause with effectively unusable cure periods

Cure periods that are too long (60+ days for material breach) or breach definitions that are too narrow to capture the customer's actual concerns.

**Why it's a red flag:** customer cannot meaningfully terminate for cause; the right is on paper only.

**Severity:** material. Critical in deals where service performance is a meaningful concern.

**Mitigation:** standard 30-day cure period for non-monetary breach; shorter for monetary; broad breach definition that captures material service failures.

### Forfeiture on termination

Loss of all prepaid amounts on termination.

**Why it's a red flag:** even when the customer terminates for cause (vendor's breach), customer loses prepaid fees.

**Severity:** material when prepaid amounts are significant; critical when termination for cause forfeits prepaid amounts (which is unfair to the non-breaching party).

**Mitigation:** prepaid amounts refunded on customer's termination for cause; pro-rata refund on termination for convenience (where allowed).

## SLA and performance traps

### Force majeure swallowing the SLA

FM clause defined to include cloud-provider outages, vendor's own infrastructure failures, or "any disruption beyond commercially reasonable control."

**Why it's a red flag:** vendor's service depends on infrastructure; if all infrastructure issues are FM, the SLA is meaningless.

**Severity:** critical for customer in deals where service availability matters; material in others.

**Mitigation:** FM defined narrowly to true external events (natural disasters, war, government action). Vendor's infrastructure choices are vendor's responsibility, not FM.

### SLA exclusions that swallow the SLA

Excluded periods (scheduled maintenance with no time bound; force majeure broadly defined; customer-caused issues defined broadly) that effectively eliminate uptime commitment.

**Why it's a red flag:** customer's reasonable expectation of high availability is contractually negated by exclusions.

**Severity:** critical for customer; the SLA is the operational commitment.

**Mitigation:** scheduled maintenance must be with reasonable advance notice and during off-hours; FM defined narrowly; customer-caused issues clearly defined and limited.

### SLA credits as truly exclusive remedy

Customer's only remedy for SLA breach is service credits, even for chronic or material failures.

**Why it's a red flag:** customer is locked into vendor regardless of vendor's performance. A vendor that consistently misses SLA can do so indefinitely with credits as the only consequence.

**Severity:** material; critical in business-critical deals.

**Mitigation:** customer's right to terminate for cause on chronic SLA breach (e.g., three months of SLA misses in a six-month period); right to terminate without penalty if SLA falls below stated threshold for stated period.

## Hidden customer obligations

### Customer indemnity scope beyond customer's actual conduct

Customer indemnifies vendor for "any claim arising out of customer's use of the service" without limitation.

**Why it's a red flag:** the scope can extend to claims for which customer has no fault — third-party IP claims based on vendor's service architecture, claims arising from vendor's own conduct, etc.

**Severity:** material; critical in some configurations.

**Mitigation:** customer indemnity scoped to customer's content, customer's misuse, and customer's violations of laws — not customer's mere use of the service.

### "Sole and exclusive remedy" language

Provisions stating that a specific remedy (e.g., SLA credits, refund) is the customer's "sole and exclusive remedy" for a particular type of breach.

**Why it's a red flag:** can prevent customer from seeking other remedies (termination, damages) even for severe breaches.

**Severity:** material; critical when paired with material breach scenarios.

**Mitigation:** carve-outs for material breaches, repeated breaches, indemnification obligations, and confidentiality breaches.

## Drafting indicators that warrant caution

### Unusual length or structure

SaaS MSAs typically run 8-30 pages. Over 35 pages typically signals enterprise-grade complexity that warrants extra attention; over 60 pages signals significant non-standard provisions.

### Definitions section larger than operative provisions

Substantive obligations sometimes hide in definitions. Read definitions especially carefully for "Permitted Use," "Customer Data," "Confidential Information," "Affiliate," "Force Majeure Event," and "Material Breach."

### Heavy use of "notwithstanding" and "subject to"

Conjunctions that create exceptions that can swallow rules. Parse carefully.

### Cross-references to documents not provided

References to "the Documentation," "the AUP," "the SLA Policy," "the Privacy Policy" that aren't attached or defined. Customer is being asked to agree to terms not in the document.

**Severity:** material — customer should require attachment or formal incorporation of all referenced documents at signing.

### Misapplied templates

Some MSAs are clearly drafted from templates intended for different deal types:

- Perpetual-license agreement converted to SaaS without removing perpetual-license provisions.
- B2C SaaS template used in an enterprise deal (consumer-protection language, broader vendor disclaimers).
- Government SaaS template used in a private deal (FedRAMP language, FAR clauses).

When the document feels like it's about something other than the actual deal, flag template misalignment in "Items requiring human judgment."

## Conflicts with existing agreements

If the user provided business context indicating prior agreements between the parties (existing MSA, prior NDA, related services agreement), check the document for:

- Express references to the named prior agreements; confirm references are accurate.
- Integration / entire-agreement clauses that purport to override prior agreements (this can extinguish prior protections).
- Provisions that conflict with terms in the prior agreements.
- Term provisions that don't account for existing relationships (e.g., MSA term running concurrently with an existing services engagement).

If `prior_agreements` was not provided, this check is skipped — do not speculate about agreements the user did not mention.
