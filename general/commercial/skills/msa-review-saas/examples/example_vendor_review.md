# Worked Example — Vendor Perspective, Customer-Prepared MSA Template

This example shows the skill applied to a customer-drafted SaaS MSA from the vendor's perspective. The scenario: a SaaS vendor has been given a Fortune 100 enterprise customer's standard MSA template and asked whether they can sign it. This inverts the usual review pattern (vendor drafts, customer reviews) and produces meaningfully different findings.

## Input

**Perspective:** vendor
**Review depth:** comprehensive
**Jurisdiction:** New York (governing law in the customer's template)
**Deal context:** "Strategic enterprise customer; multi-year deal contemplated; customer's template, presented as standard for all customer's vendor agreements; significant deal value; customer is requiring use of their template as a condition of proceeding."
**Order Form provided:** no
**Prior agreements:** none

**Document (excerpts — actual document is 22 pages):**

> **§5.1 Service Levels.** Vendor commits to a monthly uptime of 99.99%, calculated based on total minutes in each calendar month during which the Service is available for use by Customer's authorized users. The SLA shall apply at all times other than during scheduled maintenance, of which Vendor must provide at least seven (7) days' advance notice and which shall not exceed two (2) hours per month. SLA failures shall result in service credits as set forth in Schedule A; in addition, in the event of three (3) or more SLA failures in any twelve (12)-month period, Customer shall have the right to terminate this Agreement immediately upon written notice with full refund of any prepaid amounts.
>
> **§7.2 Limitation of Liability.** EXCEPT FOR LIABILITY ARISING FROM (A) A PARTY'S BREACH OF CONFIDENTIALITY OR DATA PROTECTION OBLIGATIONS, (B) A PARTY'S INDEMNIFICATION OBLIGATIONS, (C) A PARTY'S GROSS NEGLIGENCE, WILLFUL MISCONDUCT, OR FRAUD, OR (D) BODILY INJURY OR DEATH, IN NO EVENT SHALL EITHER PARTY'S TOTAL AGGREGATE LIABILITY ARISING OUT OF OR RELATING TO THIS AGREEMENT EXCEED THE GREATER OF (X) FIFTY MILLION DOLLARS ($50,000,000) OR (Y) FIVE TIMES (5x) THE FEES PAID OR PAYABLE TO VENDOR DURING THE TWELVE (12)-MONTH PERIOD PRECEDING THE EVENT GIVING RISE TO LIABILITY.
>
> **§8.1 Vendor Indemnification.** Vendor shall defend, indemnify, and hold harmless Customer and its affiliates, officers, directors, employees, and agents from and against any and all claims, damages, losses, expenses, and liabilities (including reasonable attorneys' fees) arising out of or relating to: (a) any actual or alleged infringement of any intellectual property right by the Service; (b) any breach of this Agreement by Vendor; (c) any negligent or willful act or omission of Vendor or its personnel; (d) any breach of data protection or security obligations by Vendor; or (e) any non-compliance with applicable law by Vendor in providing the Service.
>
> **§9.1 Service Modifications.** Vendor shall not materially modify the Service in a manner that decreases functionality available to Customer without Customer's prior written consent. Vendor shall provide at least one hundred eighty (180) days' notice of any deprecation or removal of any feature or functionality.
>
> **§10.1 Customer Termination Rights.** Customer may terminate this Agreement at any time, with or without cause, upon thirty (30) days' written notice to Vendor. Upon such termination, Customer shall be entitled to a pro-rata refund of any prepaid fees attributable to the period after termination.
>
> **§10.2 Vendor Termination Rights.** Vendor may terminate this Agreement only for Customer's uncured material breach, with at least sixty (60) days' notice and opportunity to cure.
>
> **§11.1 Audit Rights.** Customer shall have the right, upon thirty (30) days' written notice, to audit Vendor's facilities, systems, and records relevant to Vendor's compliance with this Agreement and applicable law, no more than twice per twelve (12)-month period (and additionally upon any actual or suspected security incident or breach), at Customer's expense for routine audits and at Vendor's expense for any audit revealing material non-compliance.
>
> *(Other excerpts truncated.)*

## Output

# MSA Review — SaaS: Customer Template, [Customer Name] MSA

**Perspective:** Vendor
**Review depth:** Comprehensive
**Document type:** Customer-drafted SaaS MSA template
**Governing law:** New York
**Term:** not shown in excerpts; verify
**Order Form provided:** No
**Prior agreements considered:** None

## Bottom line

**Customer-favorable, signable but with three material commercial concerns the vendor should address before signing.** This template inverts the usual pattern: it was drafted by the customer's outside counsel and reflects customer-favorable positions on most issues. As a vendor evaluating signability, the document is unusually generous to the customer — but it is not unreasonable, and many of the customer-favorable provisions are within market for enterprise deals. The three issues warranting vendor's attention are: (1) the 99.99% SLA with narrow exclusions and a chronic-failure termination right (§5.1) — vendor must be confident operations can support this; (2) the liability cap of greater of $50M or 5x annual fees (§7.2) — the absolute floor is unusual and creates exposure proportional to the dollar amount, not the deal size; (3) the broad audit rights with vendor-pays for material non-compliance (§11.1) — operationally significant and costly if audits become routine.

The remaining provisions are favorable to customer but within market for enterprise deals; vendor can sign with appropriate operational and financial preparation.

## Critical issues

*None.* No issue rises to "do not sign" severity from a vendor perspective.

## Material issues

### §5.1 — 99.99% SLA with narrow exclusions and chronic-failure termination right

**What the document says:** 99.99% monthly uptime; only excludes scheduled maintenance with 7-day notice and capped at 2 hours per month; three SLA failures in 12 months = customer immediate termination right with full refund of prepaid amounts.

**Why it warrants vendor's attention:** 99.99% is the highest tier of enterprise SaaS SLA; achievable but operationally demanding. The 2-hour-per-month cap on scheduled maintenance is tight; many vendors use longer maintenance windows for substantial updates. The narrow exclusion list (no force majeure broadly defined; no cloud-provider exclusions; no customer-caused issues exclusion) puts vendor on the hook for issues that vendor cannot fully control. The chronic-failure termination right with full prepaid refund means three SLA misses unwind the deal — a serious operational risk.

**Vendor considerations:**

1. **Operational confidence:** is 99.99% achievable on this customer's specific service profile? Internal operations should sign off before vendor commits.
2. **Maintenance windows:** 2 hours per month is tight for a large SaaS platform. Vendor should consider negotiating to 4 hours per month or 8 hours per quarter, with adjustable cap for major upgrades.
3. **Exclusions:** vendor should consider negotiating customary exclusions:
   - Force Majeure Events (with reasonable definition).
   - Customer-caused issues (e.g., customer's misuse, customer's own systems failures, customer's third-party providers).
4. **Chronic-failure termination right:** the customer's right to terminate after three SLA misses with full refund is aggressive. Vendor should consider negotiating to: (i) "material" SLA failures (defined threshold below 99.0% in a single month), (ii) longer rolling window, (iii) cure opportunity, (iv) refund cap.

**Recommended fallback positions for negotiation:**
- Maintenance windows: 4 hours per month or 8 hours per quarter.
- Add force majeure exclusion.
- Add customer-caused issues exclusion.
- Chronic-failure termination right: only on three failures below 99.0% within 6 months, with 30-day cure opportunity.

### §7.2 — Liability cap with absolute dollar floor

**What the document says:** mutual cap at greater of $50M or 5x fees paid in prior 12 months. Carve-outs for confidentiality, data protection, indemnification, gross negligence, willful misconduct, fraud, and bodily injury / death.

**Why it warrants vendor's attention:** the 5x annual fees multiplier is generous to customer compared to the 1x or 2x typical of enterprise SaaS; combined with the $50M floor, it creates substantial potential exposure. For deals where annual fees are below $10M, the $50M floor controls — meaning a deal with $5M annual fees has a $50M liability cap (10x annual fees), which is significantly above market.

The carve-outs are reasonable and consistent with customer-favorable enterprise practice; the only one that might warrant vendor pushback is the data protection carve-out (which functions as an uncapped exposure for data incidents).

**Vendor considerations:**

1. **Insurance coverage:** does vendor's E&O / cyber / commercial general liability coverage extend to $50M? Coverage gaps create uncapped exposure to vendor balance sheet.
2. **Data protection carve-out:** uncapped exposure for data protection breaches is the most significant individual risk. Vendor should consider whether to negotiate a super-cap for data incidents (e.g., 5x annual fees with $20M floor) rather than uncapped.
3. **Deal economics:** the cap is not commensurate with deal value at lower fee levels. Vendor's pricing should reflect this risk; if deal margins do not justify a $50M floor, vendor should negotiate.

**Recommended fallback positions:**
- Cap structure: 5x annual fees (no absolute dollar floor, or floor reduced to $25M).
- Data protection carve-out: replace uncapped exposure with super-cap (5x annual fees with $20M floor).
- Bodily injury / death carve-out: standard and acceptable; retain.

### §11.1 — Broad audit rights with vendor-pays for material non-compliance

**What the document says:** customer audit rights twice per 12 months, plus on incident/breach; at customer's expense for routine, vendor's expense if material non-compliance found.

**Why it warrants vendor's attention:** twice-per-year on-site audits plus incident-triggered audits is operationally substantial; customer-borne cost for routine audits is reasonable, but vendor-pays for "material non-compliance" creates an asymmetric incentive — customer has lower cost incentive to limit audit scope. "Material non-compliance" is undefined, so the vendor-pays trigger is ambiguous.

**Vendor considerations:**

1. **Operational impact:** twice-per-year on-site audits across multiple customers can be a substantial operational burden. Vendor's approach should default to providing SOC 2 Type II reports for routine compliance verification, with on-site audits reserved for cause.
2. **Definition of "material non-compliance":** undefined trigger leaves vendor exposed to customer's interpretation. Vendor should negotiate a more specific definition (e.g., findings that result in regulator action, that cause customer's data breach notification, or that exceed a defined materiality threshold).
3. **Cost allocation:** vendor-pays for any "material" finding is asymmetric; standard is vendor-pays only for findings that constitute breach of the agreement.

**Recommended fallback positions:**
- Routine audits: SOC 2 Type II report review by default; on-site audit on cause once per year.
- Incident-triggered audits: scope limited to the matter at issue; reasonable advance notice; cooperation requirements.
- Cost allocation: customer-pays unless audit reveals breach of this Agreement (clear contractual standard, not "material non-compliance").

## Minor issues and observations

- **§8.1 Vendor indemnification:** scope is broad — "any breach of this Agreement," "any negligent act," "any non-compliance with applicable law." Standard for customer-favorable enterprise drafts; vendor should ensure procedural protections (notice, control of defense, no settlement without consent) are present elsewhere in the indemnification section. Verify in full document.
- **§9.1 Service modifications:** 180-day deprecation notice is generous to customer but operationally manageable; standard is 60-90 days, but enterprise deals often see 180+. Vendor should confirm no in-flight deprecations would breach this on signing.
- **§10.1 Customer termination for convenience:** 30 days with pro-rata refund is customer-favorable; standard for enterprise deals is 30-90 days with proportional refund. Vendor should accept or negotiate to 60 days for operational predictability.
- **§10.2 Vendor termination rights:** vendor can terminate only for customer's uncured material breach with 60-day cure. Customer-favorable but standard for enterprise. Vendor should confirm payment-default termination is covered (the "material breach" definition should include payment default).
- **Governing law: New York.** Acceptable; customer-favorable forum that vendor can defend in.

## Missing standard protections

- **Customer payment obligations:** verify §7.2's carve-out from cap includes customer's payment obligations (typical and important); not visible in excerpt.
- **Vendor's indemnity exceptions:** standard exceptions to vendor IP indemnity (modification, combination, customer-provided content) — verify they are present in §8.1 or elsewhere.
- **Customer indemnity:** customer template may have minimized customer's indemnity scope; verify customer indemnity exists for customer's content, customer's misuse, customer's violations of law.
- **Suspension rights:** verify vendor has reasonable suspension rights for customer's non-payment after notice/cure.

## Operational red flags

None of significant concern from a vendor perspective. The customer-favorable provisions are within market for enterprise deals.

## Conflicts with prior agreements

None — `prior_agreements` was not provided.

## Recommended next steps

1. **Sign with the three material redlines proposed above (§5.1, §7.2, §11.1).** The customer template is signable; the three areas warrant negotiation but not refusal.
2. **Internal sign-offs before commitment:**
   - Operations: confirm 99.99% SLA achievability on customer's service profile.
   - Finance/Risk: confirm $50M liability cap is within insurance coverage; identify any uncovered exposure.
   - Compliance: review audit-rights operational implications.
3. **Verify missing items in full document:** customer payment carve-out from cap; vendor IP indemnity exceptions; customer indemnity scope; vendor suspension rights.
4. **Pre-decide fallback positions** for all three material issues. Customer's procurement / legal team will likely push back on each; vendor should know its walk-away point.

## Items requiring human judgment

- **Operational confidence on 99.99% SLA:** can vendor deliver this for this customer's expected usage profile? Engineering and operations sign-off, not a legal call.
- **Financial exposure analysis:** does $50M cap with vendor-borne carve-outs fall within risk tolerance? Risk and finance functions should weigh in.
- **Strategic value of this customer:** customer-favorable terms are typical for strategic enterprise customers. Whether to accept tighter terms in exchange for the relationship is a sales/strategic call.
- **Audit operations capacity:** can vendor support twice-per-year on-site audits for this customer? Legal operations, compliance, and security teams should weigh in.

---

## What this example demonstrates

- **Vendor-perspective calibration is materially different from customer-perspective.** The same document might surface 6+ critical issues from the customer side; from the vendor side it surfaces no critical issues and 3 material ones. This reflects the rubric's expectation: "typical SaaS MSA reviewed from the vendor side (where vendor drafted) will surface 0-1 critical issues" — but this example is a customer-drafted template, where vendor surfaces somewhat more issues than for a vendor's own draft, but still fewer than customer reviewing vendor draft.
- **The "Internal sign-offs" recommendation reflects that vendor reviewing customer template needs cross-functional input.** Operations, finance, compliance — these are vendor stakeholders that don't appear when customer reviews vendor draft.
- **Customer-favorable provisions can still be signable.** The 99.99% SLA, the high liability cap, the broad audit rights, and the customer termination for convenience are all customer-favorable, but most are within market for enterprise deals. Severity calibration recognizes this — calling everything that favors the other side "critical" would lose calibration when something genuinely problematic appears.
- **Pre-deciding fallback positions is a vendor-specific recommendation pattern.** The skill's vendor-perspective output emphasizes negotiation strategy rather than negotiation requirements: "the customer will push back; what's our walk-away point?"
- **The bottom line opens with "signable but..." rather than "not signable."** Calibration to the document. A vendor reviewing a vendor-drafted MSA finds even fewer issues; a customer reviewing a customer-drafted MSA finds even fewer issues. This document is somewhere in between, and the report reflects that.
- **Missing items are flagged as "verify in full document" rather than treated as findings.** The excerpts don't show every section; the report lists what to confirm rather than fabricating findings about what's not visible.
