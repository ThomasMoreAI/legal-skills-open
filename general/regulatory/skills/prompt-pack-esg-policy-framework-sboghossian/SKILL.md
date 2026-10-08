---
name: prompt-pack-esg-policy-framework-sboghossian
title: ESG Policy Framework
description: Use when drafting an ESG (Environmental, Social, and Governance) policy framework for a company — covering environmental commitments, social responsibility, governance standards, stakeholder engagement, sustainability reporting, and alignment with applicable ESG standards such as TCFD, GRI, SASB, and ISSB. Applicable across MENA (where Vision 2030, UAE Net Zero 2050, and regulatory ESG requirements are driving adoption), EU (CSRD, SFDR), UK, and internationally. Trigger when a company needs to articulate and document its ESG commitments for investors, regulators, or reporting purposes.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-esg-policy-framework
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# ESG Policy Framework

## When to use this

Use this skill when drafting or updating an ESG (Environmental, Social, and Governance) policy framework — the document that defines a company's commitments, governance structure, and reporting approach for ESG matters. ESG policy frameworks have moved from optional to near-mandatory for companies raising institutional capital, operating in regulated sectors, or listed on exchanges in the MENA region, EU, or UK.

Typical triggers:
- Institutional investor requires ESG policy before committing capital
- Company listing on ADX, DFM, Tadawul, or LSE where ESG disclosure is required
- PE or VC fund requires portfolio company to adopt ESG framework as a condition of investment
- Corporate governance audit identifies absence of formal ESG documentation
- Company wants to participate in sustainability indices (MSCI ESG, FTSE4Good) or tenders requiring ESG credentials

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Company name, sector, and jurisdiction | Affects which ESG standards and regulatory requirements apply | Ask |
| Stage of ESG maturity | Is this a first framework or an update? | Ask |
| Key ESG risks and opportunities for the business | The substance of the framework | Ask |
| Applicable regulatory requirements | CSRD, SFDR, SCA/UAE ESG guidance, KSA ESG rules, TCFD | Ask |
| Reporting framework target | GRI, SASB, ISSB/IFRS S1–S2, TCFD | Ask |

## Optional inputs

- Carbon footprint / scope 1, 2, 3 emissions data (if available)
- Existing policies that will be integrated (EHS, community investment, anti-corruption)
- Sustainability commitments already made publicly
- Board-level ESG committee structure (or plan to establish one)
- Supply chain ESG requirements

## Document structure

### 1. Introduction and Commitment Statement

- Board-level statement of commitment to ESG principles
- Why ESG matters for this company: link to business strategy, stakeholder relationships, long-term value creation
- Scope of the framework: which entities, geographies, operations are covered
- Effective date and review cycle (typically annual)

### 2. Governance Structure

**Board oversight**:
- Which board committee has ESG oversight (audit committee, dedicated sustainability committee, or full board)?
- Board members' ESG qualifications / diversity commitments
- ESG performance metrics linked to executive compensation?

**Management responsibility**:
- Chief Sustainability Officer / ESG Director (if any)
- Sustainability team structure
- ESG working group (cross-functional: legal, finance, operations, HR, communications)

**Reporting and accountability**:
- Internal ESG reporting to board: frequency, format
- External ESG disclosure: annual sustainability report, integrated report, or regulatory filing

### 3. Environmental Pillar

**Climate and energy**:
- Net-zero target: year and scope (UAE Net Zero 2050 Strategy aligns with national ambition; KSA Vision 2030 includes 50% renewables by 2030)
- Scope 1, 2, and 3 greenhouse gas emissions inventory (aligned with GHG Protocol)
- Carbon reduction pathway: absolute reduction targets or intensity targets by year
- Renewable energy transition: % of energy from renewable sources; timeline
- TCFD alignment: disclosure of climate-related financial risks and opportunities

**Resource efficiency**:
- Water usage reduction targets (particularly relevant in water-scarce MENA)
- Waste management: reduction, recycling, circular economy commitments
- Responsible procurement: sustainable sourcing standards for key inputs

**Physical climate risk**:
- Assessment of physical climate risks (extreme heat, sea-level rise, water stress) on operations
- Adaptation measures for MENA-based operations (heat stress management for outdoor workers; cooling efficiency)

### 4. Social Pillar

**Workforce and human capital**:
- Diversity, equity, and inclusion: targets for gender diversity, nationality diversity (Emiratization / Saudization performance), and disability inclusion
- Living wage commitment
- Health and safety: target zero-harm; TRIR (Total Recordable Incident Rate) targets
- Training and development: hours of training per employee per year; career development investment
- Worker wellbeing: mental health programs; flexible working; employee assistance

**Supply chain and human rights**:
- Supplier code of conduct: ESG requirements for key suppliers
- Forced labor and child labor prohibition: explicit statement; supply chain audit program
- Conflict minerals / responsible sourcing (if applicable to sector)

**Community and stakeholder engagement**:
- Local community investment: percentage of pre-tax profit or fixed amount; geographic focus
- Stakeholder engagement: methodology for identifying and engaging key stakeholders
- Grievance mechanisms: how affected communities can raise concerns

**Customer and product responsibility**:
- Product safety and quality standards
- Responsible marketing (no misleading claims; fair pricing)
- Data privacy and cybersecurity (link to privacy policy)

### 5. Governance Pillar

**Board composition and independence**:
- Board diversity targets (gender, expertise, independence ratios)
- Director independence standards
- Succession planning for key roles

**Anti-corruption and business ethics**:
- Zero-tolerance policy for bribery, corruption, and facilitation payments
- Alignment with FCPA (for US-nexus companies), UK Bribery Act, and applicable local laws (UAE Anti-Corruption Law, KSA Anti-Bribery and Corruption Law)
- Gifts and hospitality policy
- Whistleblowing: confidential reporting channel; protection from retaliation
- Anti-money laundering and sanctions compliance

**Transparency and disclosure**:
- Regular ESG reporting (GRI Standards, ISSB/IFRS S1 and S2)
- Third-party assurance of ESG data (reasonable vs. limited assurance)
- Executive compensation linked to ESG KPIs

**Tax responsibility**:
- Commitment to paying the right amount of tax in the right jurisdiction
- Country-by-country reporting (if applicable threshold exceeded)
- No use of aggressive or abusive tax structures

### 6. ESG Reporting Framework Alignment

State which external frameworks the policy is aligned with:

| Framework | Coverage |
|---|---|
| **GRI Standards (Global Reporting Initiative)** | Comprehensive impact-based ESG reporting; most widely used globally |
| **SASB (Sustainability Accounting Standards Board)** | Industry-specific materiality standards |
| **TCFD (Task Force on Climate-related Financial Disclosures)** | Climate risk governance, strategy, risk management, and metrics |
| **IFRS S1 / S2 (ISSB)** | Sustainability and climate-related financial disclosures — the new global standard (2024+) |
| **UN SDGs** | Alignment with Sustainable Development Goals where relevant |
| **GCC-specific**: SCA ESG Reporting Guidance (UAE) | UAE SCA requires ESG reporting from listed companies; guidance updated periodically |
| **Saudi Exchange ESG Reporting Guide** | Tadawul-listed companies; voluntary but increasingly expected |
| **EU CSRD** | Applicable to large EU entities and EU subsidiaries of non-EU parents above thresholds |

### 7. Materiality Assessment

Describe the process for identifying material ESG topics:
- Double materiality: impact on people/environment AND financial materiality to the company (EU CSRD standard)
- Stakeholder engagement: consultation with employees, investors, customers, community
- Peer benchmarking: comparison with industry ESG disclosures
- Output: materiality matrix identifying priority topics

### 8. Targets, KPIs, and Commitments

Provide specific, measurable commitments:

| ESG topic | Current baseline | Target | Year |
|---|---|---|---|
| GHG emissions (Scope 1+2) | [X tCO2e] | Net zero | 2050 / 2030 |
| Renewable energy | [X%] | 100% | [Year] |
| Gender diversity — senior management | [X%] | 40% female | [Year] |
| Lost-time injury rate | [X] | Zero harm | Ongoing |
| Employee training hours | [X hrs/employee] | [Target] | [Year] |

### 9. Caveats and Currency

ESG regulatory requirements are evolving rapidly. This policy framework should be reviewed annually against:
- MENA regulatory updates (UAE SCA guidance, Saudi Exchange guidance, Tadawul ESG requirements)
- ISSB standards updates
- EU CSRD phasing (applies to EU operations; supply chain requirements broaden over time)
- Applicable sanctions and conflict-minerals lists

## Common mistakes

- **Generic aspirational statements without targets**: "We are committed to the environment" without measurable commitments is dismissed by sophisticated investors; include specific, time-bound targets.
- **Forgetting Scope 3 emissions**: Supply chain emissions (Scope 3) are typically the largest source of GHG emissions for trading and manufacturing companies; omitting them understates the company's climate footprint.
- **No board-level ownership**: An ESG policy endorsed only by a CSR manager rather than the board does not signal genuine governance integration.
- **Misalignment with local regulatory requirements**: UAE SCA requirements for listed companies and KSA Exchange requirements are specific; the framework must address them, not just TCFD or GRI.
- **Claiming alignment with a framework without actual disclosure**: Stating "we align with GRI" without actually publishing GRI-aligned disclosures is greenwashing and creates regulatory and reputational risk.

## Related skills

- [[prompt-pack-insider-trading-policy]]
- [[prompt-pack-employee-handbook]]
- [[prompt-pack-due-diligence-report]]
- [[prompt-pack-investment-agreement-venture-capital]]
