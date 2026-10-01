# Product Governance Implementation Guide (MiFID II / IDD)

Comprehensive guide to implementing product governance requirements for manufacturers and distributors under MiFID II and IDD.

## Regulatory Framework

### MiFID II Product Governance

**Legal Basis:**
- MiFID II Directive Article 16(3) and 24(2)
- Commission Delegated Directive (EU) 2017/593
- ESMA Guidelines on MiFID II product governance (June 2017)

**Effective Date:** January 3, 2018

**Applies To:**
- Investment firms manufacturing financial instruments
- Investment firms distributing financial instruments
- Credit institutions providing investment services

### IDD Product Governance

**Legal Basis:**
- IDD Article 25 (manufacturers)
- IDD Article 27 (distributors)
- EIOPA Guidelines on Product Oversight & Governance (April 2017)

**Effective Date:** October 1, 2018

**Applies To:**
- Insurance manufacturers (undertakings)
- Insurance distributors (intermediaries, agents, tied agents)
- Insurance-based investment products (IBIPs) - MiFID-like requirements

## Manufacturer Obligations

### Target Market Identification

**Requirement:** Identify target market for each product in sufficient detail

**Dimensions to Consider:**

**1. Type of Clients:**
- Retail, professional, eligible counterparty
- Categories within (e.g., mass affluent, HNW, institutional)

**2. Knowledge and Experience:**
- No knowledge (basic informed investor)
- Basic knowledge (simple products previously)
- Informed investor (understands investments)
- Advanced (complex products, sophisticated)

**3. Financial Situation:**
- Ability to bear losses
  - No capital loss
  - Limited capital loss (lose up to X%)
  - Losses beyond initial investment acceptable
- Income level / net worth thresholds

**4. Risk Tolerance and Compatibility:**
- Risk/reward profile
- Preservation
- Growth
- Income
- Speculation

**5. Objectives and Needs:**
- Investment horizon (short, medium, long term)
- Return objectives (capital preservation, growth, income, hedging)
- Liquidity needs

### Positive and Negative Target Market

**Positive Target Market:**
Characteristics of clients for whom product is compatible

**Example - Equity Fund:**
```
POSITIVE TARGET MARKET:

Type of Client:
- Retail and professional clients

Knowledge & Experience:
- Informed investors
- Understand equity risk and volatility
- Familiar with investment funds

Financial Situation:
- Can bear potential loss of invested capital
- No need for capital guarantee
- Minimum investment: €1,000

Risk Tolerance:
- Medium to high risk tolerance
- Accepts volatility for growth potential
- Compatible with SRI 5-6 (1-7 scale)

Objectives:
- Long-term capital growth (10+ years)
- No near-term liquidity needs
- Comfortable with market fluctuations
```

**Negative Target Market:**
Characteristics of clients for whom product NOT compatible

**Example - Equity Fund (continued):**
```
NEGATIVE TARGET MARKET:

- Clients seeking capital preservation or guarantees
- Clients with low risk tolerance (SRI 1-2)
- Clients with short investment horizon (<5 years)
- Clients needing regular income or liquidity
- Clients unable to bear potential loss of capital
- Clients with no investment experience
```

### Product Approval Process

**Steps:**

**1. Product Design:**
- Assess client needs and market gap
- Design features to meet target market needs
- Identify costs, complexity, risks

**2. Assess Product:**
- Risk/reward profile
- Costs (explicit and implicit)
- Complexity
- Liquidity
- Target market compatibility

**3. Scenario Analysis:**
- Stress testing
- How product performs in adverse scenarios
- Impact on target market

**4. Distribution Strategy:**
- Appropriate distribution channels
- Sales processes aligned with target market
- Staff competence and training

**5. Approval:**
- Product approval committee or designated person
- Document decision and rationale
- Record target market determination

**6. Ongoing Review:**
- Monitor product performance
- Review at least annually or when trigger event
- Update target market if needed

### Example Product Approval Documentation

**Product:** Multi-Asset Balanced Fund

```
PRODUCT APPROVAL MEMORANDUM

Date: January 15, 2025
Product: Multi-Asset Balanced Fund
Product Code: MAB-2025

Target Market:
- Client Type: Retail and professional
- Knowledge: Basic to informed investors
- Risk Tolerance: Medium (SRI 3-4)
- Investment Horizon: 5-10 years
- Objective: Balanced growth and income

Product Features:
- Asset Allocation: 60% equities, 40% bonds
- Geographic Diversification: Global
- Currency: EUR hedged
- Liquidity: Daily dealing
- Minimum Investment: €5,000
- Management Fee: 0.75% annually
- Total Cost: 1.0% (including transaction costs)

Risk Assessment:
- Market risk: Medium (diversified across asset classes)
- Credit risk: Low to medium (investment grade bonds)
- Currency risk: Low (EUR hedged)
- Liquidity risk: Low (daily dealing, liquid underlying assets)
- SRI: 3 (medium risk)

Scenario Analysis:
- 2008 Financial Crisis scenario: -20% drawdown (acceptable for medium risk profile)
- Rising interest rate scenario: -5% (bond allocation affected, manageable)
- Equity bear market: -15% (cushioned by bond allocation)

Distribution Strategy:
- Direct sales via website (suitable for self-directed investors)
- Financial advisers (suitability assessment required)
- Execution-only platforms (with appropriateness warning if outside target market)
- No cold calling or unsolicited marketing

Approval:
- Product Approval Committee: Approved
- Compliance Officer: Reviewed and approved
- Effective Date: February 1, 2025

Next Review: February 1, 2026 (or sooner if material change)
```

### Information to Distributors

**Manufacturer Must Provide Distributors:**
- Target market identification (positive and negative)
- Product costs and charges
- Risk/reward profile
- Distribution strategy
- Any circumstances that would trigger product review

**Format:**
- Standardized template (many use EMT - European MiFID Template)
- Sufficient detail for distributor to understand and distribute appropriately

**Example Information to Distributor:**
```
PRODUCT INFORMATION FOR DISTRIBUTORS
Multi-Asset Balanced Fund

Positive Target Market:
- Type: Retail, professional
- Knowledge: Basic to informed
- Risk Tolerance: Medium (SRI 3-4)
- Horizon: 5-10 years
- Needs: Balanced growth, moderate risk

Negative Target Market:
- Capital preservation seekers
- Short horizon (<3 years)
- Very low or very high risk tolerance
- Need for guaranteed returns

Distribution Channels:
- Advised sales (recommended)
- Execution-only (with warnings if outside target market)
- NOT suitable for: Cold calling, high-pressure sales

Costs:
- Management fee: 0.75%
- Total expense ratio: 1.0%
- Entry/exit charges: None
- Ongoing adviser fees: As agreed with client

Review Triggers:
- Significant outperformance/underperformance (>5% vs peers)
- Change in risk profile (SRI change)
- Regulatory changes affecting product
- Material complaints or mis-selling

Contact for Questions:
productgovernance@manufacturer.com
```

## Distributor Obligations

### Understand and Use Manufacturer Information

**Requirement:** Obtain target market information from manufacturer

**Actions:**
1. Request target market info for all products distributed
2. Review and understand target market
3. Identify own distribution target market (may be subset of manufacturer's)
4. Ensure sales process matches target market

### Distributor Target Market

**May Narrow Manufacturer's Target Market:**

**Example:**
```
Manufacturer Target Market: All retail clients

Distributor Target Market (subset):
- Retail clients with €50,000+ investable assets
- Seeking advisory service (not execution-only)
- Focused on UK and Ireland markets

Rationale:
- Distributor specializes in advised sales to affluent clients
- Narrower target market aligns with distributor's business model
- Still within manufacturer's target market
```

**Cannot Broaden Beyond Manufacturer's Target Market**

### Distribution Strategy

**Align Distribution with Target Market:**

**Sales Channels:**
- Advised vs execution-only
- Digital vs in-person
- Direct marketing vs referrals

**Sales Process:**
- Suitability assessment (for advice)
- Appropriateness assessment (execution-only complex products)
- Warnings if outside target market

**Staff Training:**
- Understand product features and risks
- Identify target market characteristics
- Conduct proper assessments

**Example Distribution Strategy Matrix:**

| Product | Target Market | Recommended Channel | Sales Process |
|---------|--------------|-------------------|--------------|
| Equity Fund (SRI 6) | Experienced, high risk tolerance, long horizon | Advised sales only | Full suitability assessment |
| Balanced Fund (SRI 4) | Moderate experience, medium risk, 5+ year horizon | Advised or execution-only (with appropriateness) | Suitability (advised) or appropriateness (exec-only) |
| Money Market Fund (SRI 1) | All retail, low risk, short horizon | Any channel including digital | Minimal (non-complex product) |
| Structured Product (SRI 5) | Sophisticated, understand derivatives, medium-high risk | Advised sales only | Enhanced suitability, complexity explanation |

### Sales Outside Target Market

**Scenario:** Product sold to client outside target market

**Distributor Actions:**

**1. Identify Sales Outside Target Market:**
- Regular monitoring (monthly/quarterly reports)
- Compare client profile to product target market
- Flag exceptions

**2. Investigate:**
- **Exceptional Circumstances?**
  - Client specifically requested product
  - Proper suitability/appropriateness done
  - Client understands and accepts mismatch
  - Documented rationale

- **Or Mis-Selling?**
  - Adviser misunderstood target market
  - Inadequate assessment
  - High-pressure sales
  - Client uninformed

**3. Remediate If Necessary:**
- Contact clients sold outside target market
- Offer to switch to appropriate product
- Compensate if losses due to mis-selling

**4. Root Cause Analysis:**
- Why did sales outside target market occur?
- Training gap?
- Incentive structure issue?
- Product information unclear?

**5. Implement Controls:**
- Enhanced training
- System controls (flags/alerts)
- Review of sales materials
- Changes to incentive structure if needed

**6. Report to Manufacturer:**
- Inform manufacturer of sales outside target market
- Provide data and analysis
- Joint review of target market appropriateness

**Example Remediation:**
```
Product: High Yield Bond Fund (Target Market: Informed investors, high risk tolerance, long horizon)

Sales Outside Target Market Identified:
- 15 sales (out of 200 total) to clients with low risk tolerance (SRI 1-2 preferred)

Investigation:
- Clients were seeking yield and focused on current income
- Advisers emphasized yield, downplayed credit risk
- Clients not informed of potential capital loss in credit event

Remediation:
- Contacted 15 clients
- Explained risks and target market mismatch
- Offered switch to investment grade bond fund (no charge)
- 12 clients switched, 3 declined (acknowledged risk, wished to remain)

Root Cause:
- Training inadequate on credit risk
- Incentive structure rewarded sales without quality check

Controls Implemented:
- Mandatory credit risk training for all advisers
- System alert when selling high yield products to low-risk-tolerance clients (requires compliance override with documented reason)
- Monthly report of sales by target market match
- Removed sales-only incentives; added compliance/quality metrics

Reported to Manufacturer:
- Shared data and analysis
- Manufacturer confirmed target market appropriate, enhanced distributor communications on risks
```

### Reporting to Manufacturer

**Requirement:** Provide information to manufacturer to support product review

**Information to Provide:**

**Sales Data:**
- Volume of sales by period
- Sales by client category (retail, professional)
- Sales within vs outside target market

**Client Feedback:**
- Complaints related to product
- Client questions or confusion about features
- Satisfaction feedback

**Market Developments:**
- Competitive products
- Regulatory changes
- Market conditions affecting product

**Recommendations:**
- Suggested target market adjustments
- Product enhancements
- Distribution strategy changes

**Frequency:** At least annually or more frequently if material issues

## Product Reviews

### Manufacturer Review Requirements

**Regular Review:** At least annually

**Review Triggers (immediate review):**
- Material change in product (fees, strategy, risk profile)
- Significant distribution outside target market
- Material complaints or mis-selling
- Poor performance vs peers or expectations
- Regulatory changes affecting product
- Market event affecting product

**Review Process:**

**1. Assess Product Performance:**
- Returns vs benchmark and peers
- Risk metrics (volatility, drawdown)
- Costs (have they increased?)
- Liquidity (any issues?)

**2. Review Target Market:**
- Is target market still appropriate?
- Have client needs changed?
- Regulatory changes affecting target market?

**3. Analyze Distributor Feedback:**
- Sales data (within target market?)
- Complaints or issues
- Market intelligence

**4. Evaluate Distribution Strategy:**
- Are distribution channels still appropriate?
- Any changes needed to sales process?
- Additional distributor communication needed?

**5. Update if Necessary:**
- Revise target market
- Adjust distribution strategy
- Communicate changes to distributors
- Update client-facing materials

**6. Document:**
- Review date
- Findings
- Actions taken
- Next review date

### Distributor Review Requirements

**Regular Review:** At least annually

**Review Scope:**
- Sales within vs outside target market
- Product suitability for distributor's client base
- Complaints and issues
- Any changes in manufacturer's target market or product

**Action If Product No Longer Suitable:**
- Cease offering product
- Notify existing clients
- Suggest alternatives
- Inform manufacturer

## Conflicts of Interest in Product Governance

### Manufacturer Conflicts

**Potential Conflicts:**
- Pressure to create products that are profitable for firm rather than suitable for clients
- Incentives to broaden target market to increase sales
- Reluctance to discontinue underperforming products

**Management:**
- Independent product approval committee
- Compliance oversight of target market determination
- Separation of product design from sales incentives
- Clear policies prioritizing client interests

### Distributor Conflicts

**Potential Conflicts:**
- Higher commissions for certain products
- Proprietary products (firm's own funds)
- Shelf space fees or marketing support from manufacturers
- Sales targets or incentives

**Management:**
- Disclose conflicts to clients
- Sell based on suitability, not compensation
- Independent advice (if offering): Cannot favor proprietary or high-commission products
- Compliance review of sales by product (detect bias)

**Example Conflict Disclosure:**
```
We distribute both proprietary products (funds managed by our affiliate) and third-party products.

When we recommend our proprietary Multi-Asset Balanced Fund, we receive the full management fee (0.75%), which is higher than the commission we receive from third-party funds (typically 0.25-0.50%).

This creates a conflict of interest as we have a financial incentive to recommend our proprietary fund.

However, we only recommend our proprietary fund when it is suitable for your needs and objectives. Our recommendations are based on suitability, not compensation.

If you have concerns about this conflict, we can discuss third-party alternatives.
```

## ESMA Supervisory Briefing and Common Deficiencies

### Common Deficiencies Identified by NCAs

**1. Generic Target Markets:**
- Target market too broad ("all retail clients")
- Insufficient detail for meaningful assessment
- Solution: Specific criteria for each dimension (knowledge, risk tolerance, horizon, etc.)

**2. Inconsistent Implementation:**
- Differences between product documentation and actual sales
- Target market defined but not used in distribution
- Solution: Ensure sales process aligns with documented target market

**3. Inadequate Manufacturer-Distributor Communication:**
- Manufacturer provides minimal information
- Distributor doesn't request or use information
- Solution: Standardized information exchange (EMT templates), regular dialogue

**4. Sales Outside Target Market Not Monitored:**
- No systems to detect off-target sales
- No investigation or remediation
- Solution: Regular reporting, automated alerts, root cause analysis

**5. Product Reviews Not Conducted:**
- No annual reviews
- Reviews superficial (box-ticking)
- Solution: Comprehensive review process, documented findings and actions

**6. Lack of Documentation:**
- Target market determination not recorded
- Reviews not documented
- Distributor feedback not retained
- Solution: Robust recordkeeping, governance minutes, compliance files

## Product Governance Documentation Checklist

### Manufacturer Documentation

- [ ] Product approval memorandum (with target market, risk assessment, distribution strategy)
- [ ] Product approval committee minutes (or designated person decision)
- [ ] Target market determination (positive and negative)
- [ ] Scenario analysis and stress testing results
- [ ] Information provided to distributors (EMT or equivalent)
- [ ] Distribution agreements (specifying product governance obligations)
- [ ] Annual product review reports
- [ ] Ad-hoc review reports (if trigger events)
- [ ] Distributor feedback (sales data, complaints, recommendations)
- [ ] Changes to product or target market (with rationale and communication to distributors)

### Distributor Documentation

- [ ] Target market information received from manufacturer
- [ ] Distributor's target market determination (if different/subset)
- [ ] Distribution strategy aligned with target market
- [ ] Sales process and controls (suitability/appropriateness)
- [ ] Staff training on product and target market
- [ ] Sales data by target market match (within vs outside)
- [ ] Investigation of sales outside target market (and remediation if needed)
- [ ] Feedback provided to manufacturer
- [ ] Annual review of products distributed (suitability for client base)
- [ ] Decisions to cease distribution (with rationale)

## Best Practices

**Manufacturer Best Practices:**

**1. Involve Compliance from Product Design:**
- Compliance reviews target market determination
- Independent challenge to sales/product teams

**2. Use Data and Research:**
- Client needs research
- Market analysis
- Product performance data

**3. Clear Governance:**
- Product approval committee with diverse membership (product, risk, compliance, distribution)
- Documented approval process and criteria

**4. Regular Distributor Engagement:**
- Quarterly or semi-annual meetings
- Share performance data and market intelligence
- Gather feedback on target market and distribution

**5. Robust Review Process:**
- Annual reviews comprehensive, not superficial
- Trigger-based reviews when material changes
- Document findings and actions

**Distributor Best Practices:**

**1. Request Full Information from Manufacturers:**
- Don't accept minimal disclosures
- Ask questions if target market unclear

**2. Align Sales Process with Target Market:**
- Train staff on each product's target market
- System controls to flag off-target sales
- Quality assurance reviews

**3. Monitor and Report:**
- Regular sales analysis by target market
- Investigate outliers promptly
- Provide meaningful feedback to manufacturers

**4. Independent Compliance Oversight:**
- Compliance reviews sales quality
- Not just volume, but suitability
- Incentives aligned with client outcomes, not just sales

**5. Document Everything:**
- Target market understanding
- Sales process and controls
- Investigations and remediations
- Reviews and decisions

## Resources

**ESMA Guidelines:**
- ESMA Guidelines on MiFID II Product Governance (ESMA/2017/1320)
- Available: https://www.esma.europa.eu

**EIOPA Guidelines:**
- EIOPA Guidelines on Product Oversight & Governance (EIOPA-BoS-17-007)
- Available: https://www.eiopa.europa.eu

**European MiFID Template (EMT):**
- Industry standard for manufacturer-distributor information exchange
- Available through industry associations

**National Competent Authority Guidance:**
- BaFin (Germany), AMF (France), FCA (UK - pre-Brexit), Central Bank (Ireland), etc.
- Check your home NCA website for specific guidance

---

**Product governance is core to MiFID II and IDD compliance. Manufacturers must identify clear target markets and provide information to distributors. Distributors must use this information, distribute to appropriate clients, and report back to manufacturers. Both must conduct regular reviews and document all processes.**
