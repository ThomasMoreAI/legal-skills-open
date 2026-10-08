---
name: review-compliance-gap-analysis-sboghossian
title: Compliance Gap Analysis
description: Use when a compliance officer, legal team, or external adviser needs to map an organization's current compliance posture against applicable regulatory frameworks — identifying gaps, quantifying severity, and recommending remediation. Covers AML/KYC (FATF 40 Recommendations + Travel Rule), sanctions (OFAC, UN, EU, MENA national lists), data protection (GDPR, KSA PDPL, UAE PDPL, Bahrain, Egypt), anti-bribery (FCPA, UK Bribery Act, MENA laws), ESG/disclosure, and sector-specific frameworks (banking, fintech, insurance, healthcare). Outputs a structured gap register with severity tiers.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-compliance-gap-analysis
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# Compliance Gap Analysis

Structured assessment of an organization's compliance posture against one or more regulatory frameworks, producing a gap register with severity ratings, remediation priorities, and estimated effort. Used as input to compliance program design, external audit preparation, board reporting, and regulatory examination preparation.

## When to use this

- An organization is entering a new jurisdiction and needs to understand the compliance build required
- A compliance programme is being refreshed after a regulatory change
- An M&A transaction requires compliance due diligence on the target
- A regulator has issued a finding or information request and the organization needs to understand its exposure
- Internal audit is scoping a compliance review and needs a framework

## Inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| Organization description (sector, size, geographic footprint) | Determines which frameworks apply and at what level | Required |
| Frameworks to assess | Specify: AML, sanctions, data protection, anti-bribery, ESG, sector-specific, or "all applicable" | Required or infer from sector + jurisdiction |
| Current-state documentation (policies, procedures, controls, audit reports) | Enables gap assessment vs a baseline; without it, assessment is hypothetical | Provide if available |
| Regulatory correspondences or prior findings | Indicates known gaps already identified by a regulator | Provide if available |
| Risk appetite / materiality threshold | Determines what counts as a "blocker" vs a "polish" item | Default: any regulatory breach = blocker; best-practice gaps = improvement |

## Framework coverage

### AML / KYC (FATF 40 Recommendations)

**Core requirements**:
- Customer Due Diligence (CDD): identification, verification, beneficial ownership identification (≥ 25% UBO threshold, per [[research-beneficial-ownership-lookup]])
- Enhanced Due Diligence (EDD): for high-risk customers (PEPs, high-risk jurisdictions, complex structures)
- Ongoing monitoring: transaction monitoring, periodic KYC refresh
- Suspicious Transaction Reporting (STR): to financial intelligence unit (UAEFIU, SAMA/SAFIU, BDL-SIC)
- Record keeping: 5 years minimum (most MENA jurisdictions) from end of relationship
- FATF Travel Rule: for virtual asset transfers ≥ threshold (USD/EUR/AED 1,000 equivalent), originator and beneficiary information must travel with the transfer

**MENA-specific AML gaps commonly found**:
- Failure to identify/verify beneficial owners beyond the direct account holder
- Inadequate PEP screening (often limited to international lists; missing local PEPs)
- No documented risk appetite for customer types and jurisdictions
- Transaction monitoring rules not calibrated to the customer's expected behavior
- DNFBP (real estate, legal, accounting) obligations often not implemented — UAE Cabinet Decision No. 10 of 2019 extended AML obligations to DNFBPs

### Sanctions

**Core requirements**:
- Screen customers, counterparties, and UBOs against all applicable lists (per [[research-sanctions-screening]])
- Freeze assets of designated parties; file Suspicious Transaction Report
- Maintain a documented screening process, screening frequency, and match-disposition workflow
- Re-screen at meaningful events (transaction trigger, periodic refresh, news alert)

**Gap patterns**:
- Screening only the direct party, not UBOs
- Using a sanctions screening tool not configured for Arabic-script name matching
- No documented process for handling near-matches (screening produces false positives; the process for clearing them must be documented)
- Not re-screening existing customers when lists are updated (daily updates to OFAC SDN are common)

### Data Protection

Multiple overlapping regimes may apply simultaneously:

| Framework | Trigger | Key requirements |
|-----------|---------|-----------------|
| GDPR | EU personal data processed | Lawful basis per processing activity; privacy notice; records of processing; DPIAs for high-risk; 72-hour breach notification; DSR handling |
| UAE PDPL (Federal Decree-Law No. 45 of 2021) | UAE personal data | Consent or legitimate interest; privacy policy; data controller obligations; 72-hour breach notification |
| KSA PDPL (Royal Decree M/19 of 2021) | KSA personal data | Consent required for most processing; cross-border transfer restrictions; NDMO registration |
| Bahrain PDPL | Bahrain personal data | Broadly similar to GDPR |
| Egypt PDPL (Law No. 151 of 2020) | Egypt personal data | ITIDA registration; consent; 72-hour breach notification |

For a full GDPR-specific review, see [[review-gdpr-readiness]].

**Cross-border transfer gap (MENA)**: Many MENA companies use US-hosted cloud services; cross-border transfer mechanisms under KSA PDPL and UAE PDPL are still developing. Standard Contractual Clauses (SCCs) used for GDPR compliance may not satisfy KSA PDPL Article 29 requirements.

### Anti-Bribery

| Framework | Jurisdictional reach | Key requirements |
|-----------|---------------------|-----------------|
| FCPA (US) | US persons, US-listed companies, anything in US commerce | Prohibits bribery of foreign government officials; accounting provisions require accurate books |
| UK Bribery Act 2010 | UK-incorporated entities, persons carrying on business in UK | Broadest reach: strict liability for commercial organisations that fail to prevent bribery; extends to private-to-private bribery |
| KSA Anti-Bribery Law (Royal Decree M/36 of 2017) | KSA entities and persons | Prohibits both offering and receiving bribes; applies to public sector officials and private sector |
| UAE Federal Law No. 31 of 2021 (Penal Code) | UAE entities and persons | Anti-bribery provisions covering public officials; gift policies required for regulated entities |

**Common gaps in MENA anti-bribery programs**:
- Facilitation payments: illegal under UK Bribery Act (no exception); FCPA has a narrow exception (being narrowed by enforcement); illegal under MENA laws
- Third-party agent diligence: many MENA transactions use intermediaries; inadequate due diligence on agents is the most common FCPA/UKBA enforcement trigger
- No written anti-bribery policy; no training; no speak-up mechanism

### ESG / Disclosure

| Framework | Scope | Key requirements |
|-----------|-------|-----------------|
| CSRD (EU Corporate Sustainability Reporting Directive) | EU companies + non-EU companies with EU operations above threshold | Mandatory sustainability reporting against ESRS standards; third-party assurance |
| SEC Climate Disclosure Rule (US) | SEC registrants | Mandatory disclosure of climate risks, GHG emissions (Scopes 1 and 2) |
| Saudi Green Initiative / ESG | KSA-listed and large private companies | Increasing expectation of ESG disclosure aligned with Saudi Vision 2030 |
| Abu Dhabi Net Zero 2050 / Dubai 2040 | UAE entities | Voluntary targets; increasingly expected for regulated entities |

### Sector-specific frameworks

| Sector | Additional frameworks |
|--------|----------------------|
| Banking | BCBS Basel III/IV; CRD VI (EU); CBUAE CAR; SAMA Capital Adequacy |
| Insurance | Solvency II (EU); CBUAE Insurance Authority regulations; SAMA insurance circulars |
| Fintech | DFSA Innovation Testing Licence; FSRA RegLab; SAMA/CMA sandbox; EU MiCA for crypto assets |
| Healthcare | HIPAA (US); NMC/DOH/DHA clinical governance standards (UAE); HAAD standards |
| Telecoms | TRA UAE; CITC KSA; SMEX Lebanon |

## Review methodology

### Step 1 — Framework scoping

Confirm which frameworks apply based on:
- Sectors in which the organization operates
- Jurisdictions in which it is licensed or operates
- Nature of its customer base (retail, professional, government)
- Whether it handles EU personal data (triggers GDPR)
- Whether it has US or UK operations (triggers FCPA / UK Bribery Act)

### Step 2 — Current-state assessment

For each requirement within each framework, assess:
- Is there a documented policy or procedure?
- Are controls implemented in practice (not just on paper)?
- Is there evidence of training and awareness?
- Are there audit results confirming effectiveness?

### Step 3 — Gap identification

For each gap, record:
- The specific requirement not met (with framework citation)
- The nature of the gap: complete absence vs partial implementation vs documentation gap vs effectiveness gap
- Evidence reviewed (or absence of evidence)

### Step 4 — Severity rating

| Severity | Definition | Typical remediation timeline |
|----------|-----------|------------------------------|
| **Blocker (Critical)** | Active regulatory breach; regulatory enforcement risk; immediate professional-liability exposure | Fix within 30 days |
| **Material (High)** | Significant gap that would be cited in a regulatory examination; reputational risk if exploited | 60–90 day remediation plan |
| **Moderate** | Best-practice gap; unlikely to trigger enforcement but would be noted in audit | 90–180 day improvement plan |
| **Minor** | Documentation gap or process improvement; no current regulatory risk | Next annual cycle |

**Materiality principle**: distinguish "blockers" (a compliance program that is entirely absent for a mandatory framework) from "polish" (a program that exists but has minor documentation gaps). A regulator assessing a CBUAE examination will weight these very differently.

## Output format

```json
{
  "organizationProfile": "string",
  "frameworksAssessed": ["list"],
  "assessmentDate": "ISO date",
  "gaps": [
    {
      "framework": "AML | Sanctions | GDPR | UAE-PDPL | KSA-PDPL | Anti-Bribery | ESG | Sector-specific",
      "requirement": "specific requirement description with regulatory citation",
      "currentState": "description of what currently exists",
      "requiredState": "description of what is required",
      "gap": "description of the delta",
      "severity": "Blocker | Material | Moderate | Minor",
      "remediationAction": "specific action to close the gap",
      "owner": "function responsible (Legal | Compliance | IT | HR | Finance)",
      "targetDate": "ISO date",
      "estimatedEffort": "small (days) | medium (weeks) | large (months)"
    }
  ],
  "summary": {
    "totalGaps": number,
    "blockers": number,
    "material": number,
    "moderate": number,
    "minor": number
  },
  "prioritizedRoadmap": "Ordered list of top 10 remediation actions by severity + effort"
}
```

## Limits and escalation

- This skill produces a gap register as a starting point, not a completed audit. A formal compliance audit requires on-site testing, document review, and interviews.
- For GDPR, [[review-gdpr-readiness]] provides a more detailed 10-area review.
- For sanctions, [[research-sanctions-screening]] is required for transaction-level screening.
- For AML, [[research-beneficial-ownership-lookup]] is required to complete UBO identification.
- Regulatory enforcement risk assessments require jurisdiction-qualified legal counsel.

## Related skills

- [[research-regulator-guidance-lookup]]
- [[research-regulation-lookup]]
- [[research-sanctions-screening]]
- [[research-beneficial-ownership-lookup]]
- [[review-gdpr-readiness]]
