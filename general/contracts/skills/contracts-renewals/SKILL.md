---
name: contracts-renewals
title: Contracts & Renewals
description: This skill should be used when the task involves manage contract creation, track renewal dates, handle amendments, process auto-renewals, and make sure revenue doesn't walk out the door.
author: erphq
author_url: https://github.com/erphq/skills/tree/main/departments/sales-crm/03-org-1k-plus/contracts-renewals
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Contracts & Renewals

## What This Process Does

Contract management covers everything from the moment a customer says "yes" to a quote through the entire life of the agreement — execution, amendments, renewals, and eventually expiration or termination. Renewal management is the specific discipline of making sure your existing contracts get renewed on time and ideally at higher values. For any business with recurring revenue (subscriptions, maintenance agreements, retainers, leases), renewals are where the money is. It costs 5-7x more to win a new customer than to renew an existing one. A missed renewal is lost revenue that was already yours. A late renewal creates gaps in coverage and service disruptions that damage the relationship. This process ensures every contract is tracked, every renewal is flagged well in advance, amendments are handled cleanly, and auto-renewals work as intended.

## Start Here: ERP•AI Templates

Before building anything from scratch, check ERP•AI's template library. The Selling module includes the Sales Order doctype (which serves as a contract record), and there are contract management capabilities in the CRM module. The Subscription doctype handles recurring billing and auto-renewal logic. ERP•AI's workflow engine can manage approval routing for contract amendments. Deploy the CRM and Selling modules, set up your contract templates using print formats, and configure the Subscription module for recurring agreements.

## Build — Setting It Up

### With Agents

Tell your agent: "Set up contract and renewal management. We have [number] of active contracts, most are [annual/multi-year], and we need [30/60/90] days advance notice on renewals." The agent will:

- Create a contract record structure with key fields (start date, end date, auto-renewal flag, renewal notice period, contract value, payment terms, key clauses)
- Build renewal calendars showing every contract's renewal date across the next 12 months
- Set up tiered alert workflows (90 days out: account manager notified; 60 days: renewal opportunity created; 30 days: manager escalation if no action taken)
- Configure auto-renewal rules for contracts with evergreen clauses
- Create amendment workflows with version tracking so you always know the current terms
- Build dashboards showing renewal pipeline, at-risk renewals, and renewal rate trends
- Set up contract templates with your standard terms, clause library, and dynamic fields
- Import existing contracts from spreadsheets or another system, mapping key dates and terms

### Key Decisions

**Contract record structure: simple or detailed?** At minimum, track parties, dates, value, and renewal terms. For more control, add clause-level tracking, obligation management, and compliance milestones. Start simple and add detail as your volume and complexity justify it.

**Renewal ownership: sales or customer success?** In many companies, the original sales rep owns the renewal. In others, a customer success manager handles renewals while sales focuses on new business. In some, a dedicated renewals team handles everything. The right model depends on your deal complexity and customer relationship structure.

**Auto-renewal policy: opt-in or opt-out?** Some contracts auto-renew unless the customer cancels within a notice period. Others require active renewal. Know the legal requirements in your jurisdictions — some regions restrict auto-renewal clauses for consumer contracts. Make sure your system respects the notice period and sends timely notifications.

**Pricing on renewal: same, escalated, or renegotiated?** Flat renewals keep the same price. Escalation clauses increase by a fixed percentage or CPI index. Renegotiated renewals reopen pricing each term. Your choice affects both revenue predictability and customer retention.

**Amendment process: informal or formal?** Small changes (adding a user, minor scope adjustment) might be handled with an email confirmation. Material changes (pricing, term, scope) should require a formal amendment document. Define the threshold clearly.

### Common Mistakes

**No single source of truth for contract dates.** The contract PDF is in a shared drive, the end date is in a spreadsheet, and the billing system has a different renewal date. Pick one system as the master and sync everything to it.

**Renewal alerts that fire too late.** If your sales cycle is 60 days and you alert the rep 30 days before renewal, you've already lost the negotiation window. Set alerts based on how long your renewal process actually takes, plus buffer.

**Ignoring the auto-renewal trap.** Your contract auto-renews, but the customer wanted to cancel and missed the notice window. Now you have a legal dispute and a furious customer. Send proactive renewal confirmations even for auto-renewals — it's better customer experience and reduces disputes.

**No amendment trail.** The contract was amended three times over two years. Nobody can find amendment #2. The current terms are unclear. Always version contracts and maintain a clean amendment history linked to the master contract.

**Treating all renewals the same.** A $500K strategic account and a $5K commodity contract don't need the same renewal process. Tier your renewals by value, risk, and strategic importance. High-value renewals get executive sponsorship; low-value renewals can auto-process.

## Maintain — Keeping It Healthy

### Dashboards & Alerts

**Renewal Calendar:** A timeline view of all contracts coming up for renewal in the next 6-12 months, color-coded by value and risk status. This is the single most important view for your renewals team.

**Renewal Rate:** Track gross renewal rate (percentage of contracts renewed) and net renewal rate (including expansion and contraction). A gross renewal rate below 85% signals retention problems. Net retention above 100% means you're growing within your base.

**Renewal Pipeline:** Similar to a sales pipeline — renewals by stage (upcoming, in progress, committed, at risk, churned). Track value, not just count, because losing one large contract matters more than losing five small ones.

**At-Risk Renewals:** Flag contracts where the customer has open support tickets, declining usage, missed payments, or hasn't responded to renewal outreach. These need immediate intervention.

**Contract Expiration Report:** Contracts expiring without a renewal in progress. This catches the ones that slipped through the cracks. Alert at 45 days before expiry if no renewal activity exists.

### Exception Handling

**Customer wants to cancel during auto-renewal window:** Have a clear process — acknowledge the request, confirm the effective date, trigger offboarding or win-back workflows as appropriate. Don't make it adversarial.

**Pricing disputes on renewal:** Customer disputes the renewal price, especially if escalation clauses kicked in. Have a process for pricing review that involves the account owner, not just billing. Sometimes a small concession saves a large relationship.

**Contract lapses (gap in coverage):** The old contract expired before the new one was signed. Define your policy — do you continue service on good faith? Do you apply retroactive terms? Have a standard "renewal pending" bridge process.

**Multi-year contracts with annual reviews:** Some contracts have annual price or scope reviews within a multi-year term. Track these internal milestones as distinct from the contract end date.

**Acquisition or merger changes:** Your customer gets acquired, or you get acquired. Contract assignment, novation, and change-of-control clauses activate. Have a playbook for handling inherited contracts.

### Routine Tasks

**Daily (agent-automated):** Send renewal reminders to account owners, update renewal pipeline status, flag expiring contracts with no activity, process auto-renewal notifications.

**Weekly (agent-assisted):** Review at-risk renewals, follow up on outstanding renewal proposals, update renewal forecasts, check for contract amendments needing processing.

**Monthly (human-reviewed):** Renewal rate analysis, churn post-mortems for lost renewals, pricing trend analysis, contract compliance audits, at-risk account intervention planning.

**Quarterly (strategic):** Renewal process effectiveness review, pricing strategy for upcoming renewals, customer health scoring calibration, contract template and terms updates.

## Scale — Growing It

### Adding Complexity

**Multi-product contracts:** Customers with multiple products may have different renewal dates for each. Decide whether to co-term (align all products to one renewal date) or manage multiple renewal events per customer. Co-terming simplifies management but requires proration math.

**Partner-managed renewals:** If channel partners own the customer relationship, they may manage renewals. You need visibility into partner renewal pipelines, partner performance on renewal rates, and a process for when partners fail to renew on time.

**Government and public sector contracts:** Option years, period of performance extensions, and modifications follow a specific regulatory process. Build a separate workflow for government contracts with FAR-compliant modification procedures.

**Global contracts:** Master service agreements with local country addenda, multi-currency billing, and jurisdiction-specific terms. The "contract" is really a hierarchy of documents. Track the master and all local agreements together.

**Usage-based contracts with minimums:** Contracts that guarantee a minimum spend but bill on actual usage above that floor. Renewal involves reviewing actual vs. committed usage and right-sizing the next term. Under-usage may trigger renegotiation or downsell.

### Automation Opportunities

**Predictive churn modeling:** Agents analyze customer behavior (support tickets, usage trends, payment patterns, engagement levels) to predict which renewals are at risk months before the renewal date. Early intervention dramatically improves renewal rates.

**Automated renewal generation:** For standard renewals (same terms, standard escalation), agents generate the renewal document, apply the price increase, and send it to the customer automatically. The account manager is notified but doesn't have to do the administrative work.

**Smart co-terming:** When a customer adds a new product mid-term, agents calculate the proration, propose a co-termed renewal date, and generate the amendment — accounting for credit on the remaining term of existing products.

**Contract intelligence:** Agents read contract documents and extract key terms, obligations, renewal clauses, and risk factors. They flag non-standard clauses, upcoming obligations, and terms that differ from your current standard.

**Renewal pricing optimization:** Agents analyze customer health, competitive alternatives, price sensitivity, and expansion opportunities to recommend optimal renewal pricing — maximizing both retention probability and revenue growth.

### When to Redesign

- Your renewal rate has dropped below 80% for two consecutive quarters
- Contract amendments are taking more than two weeks to process
- You have more than 50 contracts and are still tracking them in spreadsheets
- You've introduced a subscription model alongside your existing contract model
- Your legal team is spending more than 25% of their time on routine renewals
- Customer complaints about the renewal process appear in satisfaction surveys

## By Industry

**1. Manufacturing**
Contracts cover equipment supply agreements, maintenance agreements, and long-term supply contracts. Renewals often involve price renegotiation tied to raw material indices. Blanket purchase agreements renew annually with quantity adjustments based on demand forecasts. Track warranty periods separately from service contracts.

**2. Healthcare**
Contracts with hospitals and health systems are often tied to GPO agreements with fixed terms. Medical device service contracts include uptime guarantees and preventive maintenance schedules. Renewals require value analysis committee approval. Regulatory changes (FDA, CMS) can require mid-term contract modifications.

**3. Education**
Software and service contracts align with fiscal years (typically July 1 to June 30). Multi-year contracts are common to lock in pricing across budget cycles. Grant-funded contracts expire when the grant ends, regardless of the contract term. Procurement may require board approval for renewals above certain thresholds.

**4. Retail**
Vendor agreements with retailers include annual trade terms, promotional calendars, and rebate schedules. Renewals often coincide with category reviews where the retailer evaluates all suppliers simultaneously. Loss of a major retail contract can eliminate 20-40% of revenue overnight.

**5. Hospitality**
Contracts include management agreements, franchise agreements, and corporate rate agreements. Hotel management contracts are typically 10-20 year terms with performance benchmarks. Corporate rate agreements renew annually through an RFP process. Group booking contracts have cancellation and attrition clauses that need careful tracking.

**6. Construction**
Contracts are project-based, not recurring. Change orders are the "amendment" equivalent — tracking scope changes, cost impacts, and schedule adjustments. Master service agreements with repeat clients cover multiple projects. Warranty periods (typically 1-2 years after project completion) require tracking for defect liability.

**7. Real Estate**
Leases are the primary contract type — commercial leases are 3-10 years with renewal options. Track critical dates: lease commencement, rent escalation dates, option exercise deadlines, and expiration. Missing an option exercise deadline can cost a tenant their space. Property management agreements renew annually.

**8. Agriculture**
Contracts for crop inputs (seed, fertilizer, chemicals) are annual, typically signed in fall/winter for spring delivery. Equipment leases follow useful-life cycles (3-5 years). Land leases renew annually or by crop rotation cycle. Grain contracts lock in forward pricing — tracking delivery obligations is critical.

**9. Banking & Financial Services**
Treasury management agreements, correspondent banking contracts, and technology vendor contracts all have different renewal cycles. Loan facilities renew or refinance at maturity. Track covenant compliance throughout the term, not just at renewal. Regulatory changes can require contract amendments across the entire portfolio.

**10. Insurance**
Policy renewals are the core business — every policy has a renewal date. Track retention rate by product, agent, and customer segment. Reinsurance treaties renew annually (typically January 1) and require extensive actuarial analysis. Program administrator agreements have performance requirements that must be tracked throughout the term.

**11. Legal**
Retainer agreements and engagement letters are the primary contracts. Annual retainer renewals involve reviewing matter volumes and adjusting rates. Outside counsel guidelines from corporate clients impose terms that must be tracked for compliance. Alternative fee arrangements (AFAs) have performance milestones that trigger billing events.

**12. Government**
Contracts have strict periods of performance, option years that the government may or may not exercise, and regulatory modification procedures. Track option exercise deadlines — if the government doesn't exercise an option on time, the contract may require re-competition. Continuing resolutions can delay contract renewals by months.

**13. Pharma**
Managed care contracts, GPO agreements, and distribution agreements have rebate structures that must be tracked meticulously. Contract pharmacies under 340B require careful inventory management. Clinical trial site agreements have milestone-based terms. Licensing agreements for drug compounds involve royalty calculations tied to sales.

**14. Automotive**
Dealer franchise agreements are long-term with performance requirements. Fleet management contracts renew annually based on fleet size and utilization. Supplier contracts include annual price renegotiations, volume commitments, and quality requirements. Extended warranty contracts have specific claims management obligations.

**15. Telecom**
Service contracts typically have 1-3 year terms with early termination fees. Enterprise agreements bundle multiple services and locations. Renewal is a competitive event — competitors target your customers 90 days before renewal. Track service level credits throughout the term as they affect renewal negotiations.

**16. Media & Entertainment**
Content licensing agreements have fixed terms with complex rights windows (exclusive for 12 months, non-exclusive for 24 months after). Ad sales annual agreements (upfronts) involve volume commitments with cancellation options. Talent contracts have option years and performance escalators.

**17. Energy & Utilities**
Power purchase agreements (PPAs) are 15-25 year contracts with detailed performance, pricing, and curtailment provisions. Fuel supply contracts renew annually or quarterly. Renewable energy certificate (REC) offtake agreements have specific delivery obligations. Rate case outcomes affect all customer contracts simultaneously.

**18. Food & Beverage**
Co-manufacturing agreements include volume commitments, quality specifications, and pricing tied to ingredient costs. Distribution agreements define territories, exclusivity, and minimum purchase requirements. Franchise agreements (restaurant chains) are multi-decade commitments with renewal options and performance standards.

**19. Logistics & Transport**
Freight contracts are typically annual with rate reviews. Warehousing agreements include storage rates, handling charges, and volume commitments. Third-party logistics (3PL) contracts have service level requirements and gain-sharing provisions. Dedicated fleet contracts commit specific equipment and drivers for a term.

**20. Nonprofit**
Grant agreements have defined performance periods and reporting requirements. Government grants may have option years. Corporate sponsorship agreements renew annually, usually with a pitch process. Donor-advised fund agreements are perpetual but require ongoing stewardship. Track conditional pledges alongside contracts.

**21. SaaS / Technology**
Subscription contracts are the lifeblood — annual or multi-year with auto-renewal clauses. Track expansion (upsells, added seats), contraction (downgrades), and churn separately. Renewal is the primary revenue event for customer success teams. Enterprise agreements have custom terms that complicate the renewal process.

**22. Professional Services**
Master service agreements (MSAs) provide the framework; statements of work (SOWs) define specific engagements. The MSA renews periodically while SOWs start and end independently. Track aggregate spend against volume discount thresholds. Managed services contracts have specific deliverable schedules and SLAs.

**23. Defense & Aerospace**
Government contracts follow FAR modification procedures. Options must be exercised by specific dates. IDIQ contracts have ordering periods and maximum ceiling values to track. Subcontracts flow down prime contract terms, so prime contract changes cascade. Security classification levels may change during the contract term.

**24. Mining**
Mine service contracts are tied to mine life and production volumes. Equipment leases align with mine plan durations. Offtake agreements for mined commodities have volume commitments and pricing formulas tied to market indices. Environmental bonding requirements may change and require contract amendments.

**25. Chemicals**
Supply agreements include take-or-pay provisions, price adjustment formulas tied to feedstock indices, and force majeure clauses that are especially relevant given supply chain volatility. Quality specifications are contractual obligations — failing to meet spec triggers remedies. Toll manufacturing agreements define conversion fees and minimum volumes.

**26. Textiles & Apparel**
Licensing agreements (brand licensing for apparel) have royalty minimums and sales targets. Manufacturing agreements define quality standards, delivery schedules, and compliance requirements (labor, environmental). Retail exclusive agreements restrict distribution channels. Fabric supply contracts lock in pricing for a season.

**27. FMCG**
Joint business plans (JBPs) with major retailers function as annual contracts defining promotional commitments, volume targets, and trade spending. Distribution agreements define territories and service levels. Co-packing agreements have volume commitments and quality specifications. Promotional agreements may be quarterly within an annual framework.

**28. Electronics**
Supply agreements include volume commitments, pricing corridors, and allocation priorities during shortages. Technology licensing agreements involve royalty calculations on units shipped. Component end-of-life agreements define last-time-buy quantities and extended support terms. Design collaboration agreements share IP with complex ownership terms.

**29. Oil & Gas**
Production sharing contracts (PSCs) define how revenue splits between the operator and the host government. Service contracts are tied to well programs and production phases. Midstream agreements (gathering, processing, transportation) have dedication provisions and minimum volume commitments. Joint operating agreements (JOAs) govern multi-party operations.

**30. Jewelry & Luxury**
Consignment agreements define which pieces the retailer holds without owning. Wholesale agreements include minimum purchase requirements and authorized retailer standards. Custom design contracts specify materials, design approval milestones, and delivery dates. Brand licensing agreements protect brand standards and define royalty structures.


## ERP•AI & Proto

**ERP•AI**: The CRM module tracks contracts with custom fields for renewal dates, terms, and values. The Subscription doctype handles recurring billing with auto-renewal logic. Workflow engine manages amendment approvals. Integration between Subscription, Sales Invoice, and Customer doctypes provides end-to-end contract-to-revenue visibility.

**Proto**: Proto agents handle contracts and renewals through the ORAI cycle — Observing contract milestones and customer health signals, Reasoning about renewal risk based on usage patterns and engagement history, Acting by generating renewal documents and triggering intervention workflows for at-risk accounts, and Iterating by learning from renewal outcomes to improve churn prediction accuracy.
