# Perspective Lens

The same MSA clause can be a green light, a yellow flag, or a critical issue depending on which side the user is on. This reference flips the lens for the perspective-sensitive provisions.

## Operating principle

In a SaaS MSA, the vendor is typically the drafter and the customer is typically reviewing. This means most MSAs in the wild are vendor-favorable by default; reading from the customer perspective surfaces a longer list of issues. That doesn't make customer review more valuable — it means the calibration is different.

When the user is on the vendor side, the question is not "what's wrong with this document" (since the vendor likely drafted it) but "is this document defensible against pushback we'll receive, and have we left ourselves room to negotiate?" Vendor-perspective review is about identifying provisions where customer pushback is likely and pre-deciding the fallback positions.

When the user is on the customer side, the question is "what should we negotiate, what should we accept, what should we walk on?" Customer-perspective review is about distinguishing the must-fix issues from the could-fix-but-acceptable issues.

## Limitation of Liability

**Vendor lens:** wants the lowest defensible cap and the broadest exclusions. Concerns:
- A cap below 12 months of fees may not survive customer scrutiny in a competitive deal.
- Missing carve-outs for customer's payment obligations (a drafting error if absent — vendor wants payment carved out).
- Super-cap demands from customer for security incidents are increasingly standard; pre-decide the fallback (typically 2x or 3x base cap).
- Indirect/consequential damages exclusion should mirror cap exclusions.

**Customer lens:** wants a cap appropriate to potential damage and carve-outs that protect against critical risks. Concerns:
- Cap below 12 months of fees is below market; ask for 12 months minimum, 24 months for enterprise deals.
- Missing super-cap for security incidents is a serious gap if customer data is sensitive.
- Missing carve-outs for gross negligence, willful misconduct, and fraud — flag whichever are missing.
- Disclaimers of indirect/consequential damages can swallow real harm; ensure carve-outs mirror cap carve-outs.
- No "limit on customer's payment obligation" — should be carved out from cap (vendor might draft this in but flag if missing).

## Indemnification

**Vendor lens:** wants narrow IP indemnity scope and broad customer indemnity. Concerns:
- IP indemnity scope should exclude common abuse cases (modification, combination, customer content, customer-provided specifications).
- Procedural protections (notice, control of defense, no settlement without consent) protect vendor's defense strategy.
- Customer indemnity for customer's data and use is standard; ensure it covers third-party claims arising from customer's content and from customer's misuse.

**Customer lens:** wants vendor IP indemnity that actually covers anticipated risks. Concerns:
- Patent indemnity exclusion is increasingly common in cost-sensitive deals — flag as material; in deals involving novel technology, request inclusion.
- "Sole and exclusive remedy" language for IP infringement can prevent customer from seeking other remedies (e.g., termination) — flag.
- IP indemnity exceptions (modification, combination, etc.) should be reasonable and not so broad they swallow the indemnity.
- Customer indemnity scope should be limited to customer's actual conduct and not extend to broad scenarios where vendor has more visibility (e.g., third-party claims that vendor's service infringes third-party rights — that's vendor's indemnity, not customer's).

## IP and Customer Data Ownership

**Vendor lens:** wants clear ownership of service IP and broad rights in customer data for service operation and improvement. Concerns:
- Customer data license should be broad enough to cover all operational uses (storage, transmission, processing for the service, backup, security operations).
- "Service improvement" license to use customer data is increasingly contested — pre-decide fallback (offer opt-out, narrow to specific uses, exclude sensitive customer data).
- ML training rights are the dominant 2025-2026 contested issue. Vendor's posture should be clear: include only with explicit customer opt-in or specific deal authorization, never as a default term.
- Feedback assignment to vendor is standard; ensure scope is limited to feedback specifically about the service.

**Customer lens:** wants clear ownership of customer data and narrow vendor use rights. Concerns:
- Customer data license to vendor should be narrowly scoped to "providing the service" — not "internal business purposes" or other broad language.
- "Service improvement" license is a common vendor ask; consider whether customer data is sensitive enough to refuse, and whether anonymization is verifiable.
- ML training rights are typically a no — flag as critical and require explicit removal or opt-in mechanism.
- "Aggregated and anonymized" data carve-outs are often weaker than they appear; verify the anonymization standard meets customer's standards (GDPR-grade or similar).
- Feedback assignment should be limited to feedback about the service, not all communications between the parties.

## Warranties and Disclaimers

**Vendor lens:** wants minimal express warranties and broad disclaimers. Concerns:
- Express warranties should be specific and verifiable (substantially in accordance with documentation; provided in workmanlike manner; vendor has rights to provide service).
- Disclaimer of implied warranties is essential.
- "AS IS" warranty disclaimer is aggressive and signals to customer that vendor is unwilling to stand behind the service — pre-decide whether to use or fall back to standard express warranties.

**Customer lens:** wants meaningful express warranties that survive disclaimers. Concerns:
- "Substantially in accordance with documentation" is the weakest standard meaningful warranty — accept if drafted with adequate remedy (typically credit/refund; sometimes termination right for material warranty breach).
- "AS IS" warranty disclaimer is unusual and warrants negotiation — at minimum, vendor should warrant rights to provide and freedom from malicious code.
- Vendor warranty of right to provide the service is critical (without it, customer has no recourse if vendor's IP turns out to be encumbered).
- Vendor warranty of security and data protection commitments should be present; if scattered through the agreement, ensure they collectively cover customer's expectations.

## Term and Termination

**Vendor lens:** wants long terms, auto-renewal protection, narrow customer termination rights. Concerns:
- Auto-renewal with reasonable notice (30-60 days) is standard; longer windows (90+ days) are aggressive and increasingly contested.
- No customer termination for convenience is standard for enterprise SaaS but often negotiated; pre-decide fallback (allow with proportional refund; allow with cap on refund; allow only after initial term).
- Termination for cause requires breach with notice and cure; ensure cure period is reasonable (30 days standard) and breach definitions aren't so broad that minor issues become termination triggers.
- Renewal price increases — vendor wants flexibility; customer wants caps. Pre-decide fallback (CPI + X%; flat percentage cap; mutual agreement).

**Customer lens:** wants strong termination rights and predictable renewal. Concerns:
- Auto-renewal opt-out window over 60 days is aggressive — negotiate down.
- No customer termination for convenience in a long-term deal is a meaningful constraint — consider cost of negotiation vs. value of optionality.
- Renewal price increases without cap are a material concern in long deals; require a cap (CPI + X%; or fixed maximum percentage).
- Termination-for-cause cure periods that are excessively long (60+ days) effectively prevent termination on serious breach — flag as material.
- Vendor's right to terminate on minor customer breach (e.g., late payment after one missed deadline) without cure — flag as material.

## Payment, Pricing, Renewal Pricing

**Vendor lens:** wants prompt payment, late fees, suspension rights, and pricing flexibility. Concerns:
- Suspension for non-payment should have notice/cure (10-15 days) but be exercisable; without it, vendor has no leverage on non-paying customer.
- Acceleration on uncured material breach is aggressive; pre-decide whether to use or fall back to ordinary breach remedies.
- Renewal pricing flexibility — vendor wants no cap; customer typically wants cap.

**Customer lens:** wants predictable pricing and protections against vendor leverage. Concerns:
- Suspension without notice is critical issue; require notice and cure period.
- Acceleration clauses are aggressive; negotiate to limit acceleration to material non-payment after extended cure.
- Renewal pricing without cap is a material concern; require cap.
- Late fees beyond what state law allows are flag-but-not-critical (excess unenforceable); customer can accept and rely on enforceability law.

## SLA

**Vendor lens:** wants achievable SLA commitments, broad exclusions, and limited remedies. Concerns:
- Uptime commitment should reflect actual operational reality with margin; over-committing creates SLA-credit liability.
- Exclusions (scheduled maintenance with adequate notice; force majeure with reasonable scope; customer-caused issues) protect against false-positive SLA misses.
- SLA credits should cap (typically 25-50% of monthly fees); credits as sole remedy is standard.
- Reporting requirements should be customer-must-request (not vendor-must-proactively-credit) — administrative protection for vendor.

**Customer lens:** wants meaningful uptime commitment, narrow exclusions, and proportional remedies. Concerns:
- Uptime below 99.5% is below market for enterprise SaaS; flag as material.
- Excessively broad exclusions effectively eliminate the SLA — flag.
- SLA credits as truly exclusive remedy for repeated material failures (chronic SLA breach) — flag and negotiate exit right.
- Customer-must-request remedy structure puts administrative burden on customer; consider negotiating proactive credit.

## Confidentiality

**Vendor lens:** wants reasonable mutual confidentiality with carve-outs that don't restrict vendor's product development or marketing.

**Customer lens:** wants reasonable mutual confidentiality. The customer-data confidentiality is typically governed by DPA, not by general confidentiality clause; check that customer's confidentiality protections aren't subordinated to vendor's narrower confidentiality definitions.

## Force Majeure

**Vendor lens:** wants broad FM scope to excuse non-performance during disruptions. Concerns:
- Cloud-provider outage inclusion in FM is increasingly contested; pre-decide whether to push.
- Notice and termination right after extended FM are reasonable customer asks; pre-decide thresholds.

**Customer lens:** wants narrow FM to keep vendor on the hook for service performance. Concerns:
- FM that includes vendor's cloud provider outage swallows the SLA — flag as material.
- Asymmetric FM (vendor's performance excused, customer's payment obligations not) is standard and acceptable for most customers; flag if extreme.
- No termination right after extended FM is a real concern in long deals.

## Audit Rights

**Vendor lens:** wants minimal customer audit rights (typically routed through SOC 2 reports) and useful audit rights of customer's compliance with AUP and license metrics.

**Customer lens:** wants meaningful audit rights of vendor's compliance with security and data protection commitments. SOC 2 Type II report review is industry-standard primary mechanism; on-site audit on cause is customary backup. Vendor's audit rights of customer should be limited to AUP compliance and license metrics, not broader operational matters.

## Watching for "vendor-favorable mutual"

A persistent pattern in SaaS MSAs labeled with mutual-sounding language but practically asymmetric. Indicators:

- Mutual cap with carve-outs that practically only apply to customer (e.g., carve-out for "your" payment obligations doesn't help customer).
- Mutual indemnity where vendor's IP indemnity is narrowly scoped and customer's content indemnity is broadly scoped.
- Mutual confidentiality where customer's data is carved out into the (narrower) DPA confidentiality terms while vendor's confidential information stays under the (broader) MSA confidentiality.
- Mutual termination rights but with different breach definitions (vendor can terminate on customer's "any breach"; customer can terminate only on vendor's "material breach uncured for 30 days").

When reviewing as customer, conduct an asymmetry check: would the same provisions read differently if the parties' positions were reversed? If yes, the mutual labeling is cosmetic.
