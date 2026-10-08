---
name: severance-review-reggiechan74
title: Severance Package Analysis Report
description: Analyze severance packages and termination agreements for fairness and negotiation opportunities
author: reggiechan74
author_url: https://github.com/reggiechan74/JobOps/tree/main/plugins/jobops/skills/severance-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ca
practice: employment
language: en
---

## Configuration

Read `.jobops/config.json`. If missing, stop with:

> JOBOPS NOT CONFIGURED
> Run /jobops:setup to initialize your workspace.

Use `config.directories.<key>` for all file paths in this skill.
Use `config.preferences.cultural_profile` if this skill generates resume-style content.
Use `config.preferences.default_jurisdiction` if this skill has jurisdiction-sensitive logic (crisis/legal skills accept `--jurisdiction=<ISO-3166-2>` to override).

## Default Jurisdiction: Ontario, Canada

This command defaults to **Ontario, Canada** employment law framework. Key principles:

- **Common Law Notice**: Ontario employees are typically entitled to reasonable notice (1 month per year of service, up to 24 months) based on Bardal factors: age, tenure, position, availability of similar employment
- **ESA Minimums**: Employment Standards Act provides minimum statutory entitlements (termination pay, severance pay for 5+ years at large employers)
- **No At-Will Employment**: Employers must provide reasonable notice or pay in lieu; just cause terminations are rare and require serious misconduct
- **Provincial Health Insurance**: OHIP provides basic coverage; extended health benefits (dental, vision, prescription) are employer-provided
- **ROE Coding**: Record of Employment determines EI eligibility; "Code M" (dismissal) preserves benefits
- **Human Rights**: Ontario Human Rights Code protects against discrimination (broader than US federal law)

**For US users**: Specify `--jurisdiction=US` or mention your state. US employment involves COBRA, ADEA/OWBPA age requirements, at-will employment, and state-specific laws.

## Important Disclaimers

**CRITICAL**: Read these disclaimers ALOUD to the user at session start:

1. **Not Legal Advice**: This analysis is informational, not legal advice. For legally complex situations (discrimination claims, non-compete enforceability, pension/benefit plan issues, class action waivers), strongly recommend consultation with an employment lawyer.
2. **Jurisdiction Matters**: This analysis defaults to Ontario, Canada employment law. Other provinces and US states have different requirements. Confirm your jurisdiction for accurate guidance.
3. **No Guarantee of Accuracy**: Severance agreements are complex legal documents. This analysis may miss nuances that a qualified attorney would catch.
4. **Time Sensitivity**: Most severance agreements have signing deadlines. Factor in time needed for legal review if pursuing that route.
5. **Confidentiality Reminder**: Severance terms are often confidential. Be mindful of what you share and with whom.


## Phase 0: Statutory & Case Law Research (MANDATORY)

**CRITICAL**: Before performing ANY analysis, you MUST conduct jurisdiction-specific legal research using web search. This phase is non-negotiable and must be completed before proceeding to document parsing or any other phase.

### 0.1 Identify Applicable Jurisdiction

Determine the governing jurisdiction from:
1. The agreement's governing law clause (if document already provided)
2. The user's stated location
3. Default: Ontario, Canada

### 0.2 Statutory Research

Use web search to research and document the **current** statutory framework. Do NOT rely solely on training data — statutes are amended frequently.

**For Ontario (default):**
- **Employment Standards Act, 2000 (ESA)**: Current termination pay (s.54-62) and severance pay (s.63-66) provisions, including any recent amendments
- **Ontario Human Rights Code**: Current protected grounds and remedies relevant to termination
- **Bill 27 (Working for Workers Act, 2021)** and subsequent amendments: Non-compete restrictions for non-executives
- **ESA mass termination rules** (if applicable): Current thresholds and notice periods
- **Canada Labour Code** (if federally regulated employer): Division IX termination provisions
- **Employment Insurance Act**: Current EI eligibility rules, waiting periods, and benefit calculations

**For US jurisdictions:**
- Federal: WARN Act, OWBPA/ADEA, Title VII, ADA as applicable
- State-specific: Relevant employment statutes, non-compete laws, mini-WARN acts
- Local ordinances if applicable

**For other jurisdictions:**
- Research the equivalent statutory employment protections

### 0.3 Case Law Research

Use web search to find **recent and leading case law** relevant to the specific severance situation. Focus on:

**For Ontario:**
- **Bardal factors / reasonable notice**: Search for recent Ontario Superior Court and Court of Appeal decisions on reasonable notice periods for comparable roles (similar tenure, age, position level, industry)
- **Waksdale v. Swegon (2020 ONCA 391)**: Confirm current status — this landmark case invalidated termination clauses that violated ESA minimums, even if the ESA-compliant portion was separate. Check for any subsequent legislative or judicial developments
- **Release enforceability**: Recent decisions on what makes a severance release valid or voidable in Ontario (e.g., Rubin v. Home Depot, Titus v. William F. Chicken)
- **Duty to mitigate**: Current case law on mitigation obligations and how they affect reasonable notice awards
- **Bad faith damages**: If applicable, search for Honda Canada v. Keays (SCC) and recent applications regarding manner of dismissal damages
- **Non-compete enforceability post-Bill 27**: Any court decisions interpreting the Working for Workers Act restrictions
- **Constructive dismissal** (if relevant): Recent case law on what constitutes constructive dismissal

**For US jurisdictions:**
- State-specific non-compete enforceability precedents
- OWBPA compliance requirements from recent decisions
- Relevant circuit court decisions on release validity

### 0.4 Document Research Findings

Present a summary of research findings before proceeding:

```
LEGAL RESEARCH SUMMARY
======================
Jurisdiction: [Province/State]
Research Date: [Today's date]

APPLICABLE STATUTES:
| Statute | Key Provisions | Relevance |
|---------|---------------|-----------|
| [Statute name] | [Sections] | [How it applies] |
| ... | ... | ... |

KEY CASE LAW:
| Case | Citation | Principle | Relevance |
|------|----------|-----------|-----------|
| [Case name] | [Year, Court, Citation] | [Legal principle established] | [How it applies to this package] |
| ... | ... | ... | ... |

REASONABLE NOTICE RANGE (from case law):
- Low estimate: [X months] (based on [case])
- Mid estimate: [X months] (based on [case])
- High estimate: [X months] (based on [case])
- Key factors: age [X], tenure [X years], position [level], re-employment prospects [assessment]

STATUTORY MINIMUMS:
- ESA termination pay: [X weeks]
- ESA severance pay: [X weeks, if applicable]
- Total statutory floor: [X weeks]

NOTES ON RECENT LEGAL DEVELOPMENTS:
- [Any recent legislative changes, pending bills, or evolving case law trends]
```

**Important**: If web search is unavailable or returns insufficient results, clearly disclose this limitation to the user and recommend they verify statutory provisions with a lawyer. Do not fabricate citations or case law.

---

## Modes of Operation

Parse the mode from arguments:
- **Default (no flags)**: Full document analysis with term extraction and assessment
- `--benchmark`: Include comprehensive market benchmarking and industry comparisons
- `--counter-offer`: Generate specific counter-proposal language and negotiation strategy

If both flags are specified, perform all analyses.


## Input Documents

**Argument Handling**:
- If `$1` is provided: Load specified agreement file
- If `$1` not provided: Ask user to provide the severance agreement document

**Accepted Document Types**:
- Separation agreements
- Severance packages
- Termination letters with release language
- Settlement agreements
- Mutual separation agreements
- Retirement incentive packages
- Voluntary separation program (VSP) offers
- Reduction in force (RIF) documentation

**Load Career Context**:
If career context is needed (tenure for severance formula, industry benchmarks), read `WorkHistory/*.md` files directly from `{config.directories.resume_source}`. Compute tenure from explicit Start/End dates. Do NOT load `candidate_profile.json` — removed in v2.2.0.


## Phase 1: Document Parsing & Term Extraction

### 1.1 Load and Parse Agreement

@$1

Read the agreement and extract document metadata:

```
DOCUMENT METADATA
=================
| Field | Value |
|-------|-------|
| Document Type | [Separation Agreement/Severance Package/etc.] |
| Company Name | [Employer] |
| Employee Name | [If visible] |
| Date Presented | [Date] |
| Signing Deadline | [Date] |
| Revocation Period | [X days] |
| Effective Date | [Date or trigger] |
| Governing Law | [State/Province] |
| Number of Pages | [X] |
```

### 1.2 Extract Core Severance Terms

**Monetary Terms:**

```
SEVERANCE COMPENSATION
======================
| Component | Value | Calculation | Notes |
|-----------|-------|-------------|-------|
| Base Severance | $XXX | [X weeks/months] | [Formula if stated] |
| Bonus Proration | $XXX or N/A | [% of target] | [Conditions] |
| Accrued PTO Payout | $XXX or N/A | [Days × rate] | [Cap if any] |
| Retention/Stay Bonus | $XXX or N/A | | |
| Outplacement Services | $XXX value or N/A | [Provider/duration] | |
| Other Cash | $XXX or N/A | [Description] | |
| TOTAL CASH VALUE | $XXX | | |
```

**Benefits Continuation (Ontario):**

```
BENEFITS CONTINUATION
=====================
| Benefit | Duration | Company Contribution | Notes |
|---------|----------|---------------------|-------|
| Extended Health (Rx, paramedical) | X months | [Full/Partial/Conversion] | |
| Dental Insurance | X months | | |
| Vision Insurance | X months | | |
| Life Insurance | X months | | |
| Disability Insurance | X months | | |
| Health Spending Account (HSA) | [Continuation terms] | | |
| EAP | X months | | |
| RRSP/DPSP Matching | [Final contribution terms] | | |
| Other Benefits | | | |
```

**Note**: OHIP (Ontario Health Insurance Plan) provides basic medical coverage regardless of employment status. Extended health benefits cover prescription drugs, dental, vision, and paramedical services.

**Equity Treatment:**

```
EQUITY & STOCK TREATMENT
========================
| Equity Type | Unvested Amount | Treatment | Notes |
|-------------|-----------------|-----------|-------|
| Stock Options | [Shares/Value] | [Accelerated/Forfeited/Pro-rata] | Exercise window: [X days] |
| RSUs | [Shares/Value] | [Accelerated/Forfeited/Pro-rata] | |
| Performance Shares | [Shares/Value] | [Treatment] | |
| ESPP | [Amount] | [Treatment] | |
| Deferred Comp | [Amount] | [Treatment] | |
```

### 1.3 Extract Restrictive Covenants

**Non-Compete Provisions:**

```
NON-COMPETE ANALYSIS
====================
| Element | Terms | Assessment |
|---------|-------|------------|
| Duration | [X months/years] | [Reasonable/Excessive] |
| Geographic Scope | [Description] | [Reasonable/Excessive] |
| Industry/Role Scope | [Description] | [Reasonable/Excessive] |
| Enforcement Mechanism | [Injunction/Damages/Clawback] | |
| Consideration | [Included in severance/Separate] | |
| Carve-outs | [Exceptions if any] | |
```

**Non-Solicitation Provisions:**

```
NON-SOLICITATION ANALYSIS
=========================
| Element | Terms | Assessment |
|---------|-------|------------|
| Employee Non-Solicit Duration | [X months/years] | |
| Customer Non-Solicit Duration | [X months/years] | |
| Scope Definition | [Who is covered] | |
| Active vs. Passive Recruitment | [Terms] | |
```

**Confidentiality Provisions:**

```
CONFIDENTIALITY ANALYSIS
========================
| Element | Terms | Notes |
|---------|-------|-------|
| Duration | [Time-limited/Perpetual] | |
| Scope | [Trade secrets only/Broader] | |
| Carve-outs | [Exceptions] | |
| Return of Materials | [Requirements] | |
```

### 1.4 Extract Release Terms

```
RELEASE OF CLAIMS
=================
| Element | Terms | Concern Level |
|---------|-------|---------------|
| Claims Released | [List specific claims] | |
| Time Period Covered | [All past claims/Specific period] | |
| Unknown Claims Waiver | [Yes/No - CA Civil Code 1542] | |
| Carve-outs | [What's NOT released] | |
| ADEA Waiver | [Yes/No - Age discrimination] | |
| Class Action Waiver | [Yes/No] | |
| Government Agency Rights | [Preserved/Waived] | |
```

### 1.5 Extract Other Key Provisions

```
ADDITIONAL PROVISIONS
=====================
| Provision | Terms | Notes |
|-----------|-------|-------|
| Non-Disparagement | [Mutual/One-sided] | |
| Reference Provision | [What company will say] | |
| Cooperation Obligation | [Scope/Duration/Compensation] | |
| Return of Property | [Requirements] | |
| Acknowledgment of Voluntariness | [Terms] | |
| No Admission of Liability | [Standard/Modified] | |
| Modification/Amendment | [Requirements] | |
| Entire Agreement | [Yes/No] | |
| Severability | [Yes/No] | |
| Assignment | [Terms] | |
```


## Phase 2: Red Flag Detection

### 2.1 Legal Compliance Red Flags

**Ontario Release Validity Requirements:**

```
RELEASE VALIDITY CHECK (ONTARIO)
================================
| Requirement | Present | Compliant | Notes |
|-------------|---------|-----------|-------|
| Written in clear, understandable language | [Yes/No] | [Yes/No] | Courts scrutinize complex legalese |
| Employee advised to seek legal counsel | [Yes/No] | [Yes/No] | Strengthens enforceability |
| Reasonable time to consider | [Yes/No] | [Yes/No] | No statutory minimum, but should be reasonable |
| Fresh consideration provided | [Yes/No] | [Yes/No] | Must exceed ESA minimums to be valid release |
| No duress or undue pressure | [Yes/No] | [Yes/No] | Quick deadlines may indicate duress |
| Clear description of claims released | [Yes/No] | [Yes/No] | Vague releases may be unenforceable |
| ESA rights not waived | [Yes/No] | [Yes/No] | Cannot contract out of ESA minimums |
```

**Mass Termination Requirements (Ontario ESA)** (if 50+ employees terminated in 4-week period):

```
MASS TERMINATION COMPLIANCE CHECK
=================================
| Required Element | Present | Notes |
|-----------------|---------|-------|
| Ministry of Labour notification | [Yes/No] | Employer must file Form 1 |
| Extended notice period (8-16 weeks) | [Yes/No] | Based on number affected |
| Benefits continuation during notice | [Yes/No] | ESA requirement |
| Written notice to employees | [Yes/No] | Individual notice required |
```

**For US users**: ADEA/OWBPA requires 21-day consideration (45 for group layoffs), 7-day revocation period, and specific disclosures for employees 40+.

### 2.2 Substantive Red Flags

Evaluate and flag the following concerns:

```
RED FLAG ASSESSMENT
===================

CRITICAL RED FLAGS (Potential Deal-Breakers):
---------------------------------------------
[ ] Overly broad release of unknown future claims
[ ] Waiver of rights to file Human Rights Tribunal or Ministry of Labour complaints
[ ] One-sided non-disparagement (only binds employee)
[ ] Clawback provisions triggered by broad conditions
[ ] Non-compete with no geographic or temporal limits (likely unenforceable in Ontario anyway)
[ ] Waiver of vested benefits (pension, RRSP/DPSP match)
[ ] Requirement to cooperate indefinitely without compensation
[ ] Unreasonably short signing deadline (may indicate duress)
[ ] Package less than ESA statutory minimums (unenforceable release)
[ ] Release of claims not yet known or accrued
[ ] Forum selection clause outside Ontario

SIGNIFICANT RED FLAGS (Strong Negotiation Points):
--------------------------------------------------
[ ] Below-market severance amount (less than common law reasonable notice)
[ ] Non-compete duration exceeds 12 months
[ ] Non-compete geographic scope unreasonably broad
[ ] Non-solicitation covers all company employees
[ ] No reference letter or neutral reference guarantee
[ ] Extended benefits less than 3 months
[ ] Equity forfeiture of nearly-vested shares
[ ] Stock option exercise window less than 90 days
[ ] Cooperation clause with no time limit
[ ] Must return company laptop/equipment immediately
[ ] Acknowledgment of "just cause" termination (waives notice entitlement)
[ ] Forfeiture of accrued but unpaid bonuses
[ ] ROE coded as "quit" or "cause" (affects EI eligibility)

MODERATE RED FLAGS (Worth Addressing):
--------------------------------------
[ ] Confidentiality broader than trade secrets
[ ] Return of property includes personal devices
[ ] Vague or no reference provision
[ ] No outplacement services
[ ] Immediate termination of benefits
[ ] No acknowledgment of contributions
[ ] No commitment to ROE coding (Code M preferred)
```

### 2.3 Missing Provisions Check

```
MISSING PROVISIONS ANALYSIS (ONTARIO)
=====================================
| Provision | Present | Concern If Missing |
|-----------|---------|-------------------|
| Mutual non-disparagement | [Yes/No] | One-sided protection |
| Reference letter language | [Yes/No] | No control over references |
| ROE coding commitment | [Yes/No] | Employer may code as quit/cause, affecting EI |
| Extended benefits continuation | [Yes/No] | Must arrange own coverage during notice period |
| Outplacement services | [Yes/No] | No transition support |
| Equity treatment | [Yes/No] | May forfeit unvested equity |
| Bonus proration | [Yes/No] | May lose earned bonus |
| Vacation/PTO payout | [Yes/No] | ESA requires payout of earned vacation |
| Cooperation compensation | [Yes/No] | Free labor obligation |
| Survival of D&O indemnification | [Yes/No] | Loss of director/officer coverage |
```


## Phase 3: Package Valuation

### 3.1 Total Cash Value Calculation

```
PACKAGE VALUATION SUMMARY
=========================

CASH COMPONENTS:
| Component | Gross Value | After-Tax Est. | Notes |
|-----------|-------------|----------------|-------|
| Base Severance | $XXX | $XXX | [Tax treatment] |
| Bonus Proration | $XXX | $XXX | |
| PTO Payout | $XXX | $XXX | |
| Other Cash | $XXX | $XXX | |
| SUBTOTAL CASH | $XXX | $XXX | |

BENEFITS VALUE (ONTARIO):
| Component | Monthly Cost | Duration | Total Value |
|-----------|--------------|----------|-------------|
| Extended Health (Rx, paramedical) | $XXX | X months | $XXX |
| Dental | $XXX | X months | $XXX |
| Vision | $XXX | X months | $XXX |
| Life Insurance | $XXX | X months | $XXX |
| SUBTOTAL BENEFITS | | | $XXX |

Note: Basic medical (hospital, physician) covered by OHIP regardless of employment.

EQUITY VALUE (Estimated):
| Component | Shares | Price Est. | Total Value |
|-----------|--------|------------|-------------|
| Accelerated Options | XXX | $XX | $XXX |
| Accelerated RSUs | XXX | $XX | $XXX |
| SUBTOTAL EQUITY | | | $XXX |

OTHER VALUE:
| Component | Estimated Value |
|-----------|-----------------|
| Outplacement Services | $XXX |
| Career Coaching | $XXX |
| Extended Email Access | [Intangible] |
| SUBTOTAL OTHER | $XXX |

======================================
TOTAL PACKAGE VALUE (GROSS): $XXX,XXX
TOTAL PACKAGE VALUE (EST. NET): $XXX,XXX
======================================
```

### 3.2 Tax Considerations

```
TAX TREATMENT NOTES (CANADA)
============================
| Component | Tax Treatment | Considerations |
|-----------|---------------|----------------|
| Severance Pay | Employment income, withholding | May push into higher bracket; consider RRSP contribution |
| Retiring Allowance | May be eligible for RRSP rollover | Pre-1996 service years: $2K/year direct RRSP contribution |
| Bonus Proration | Employment income | Same as regular bonus |
| Vacation Payout | Employment income | Immediate taxation |
| Extended Benefits | Generally not taxable | When company pays directly |
| Outplacement | Generally not taxable | If reasonable value |
| Equity Acceleration | Depends on type | Stock options, RSUs have different treatment |
```


## Phase 4: Benchmarking Analysis (--benchmark mode)

### 4.1 Industry Standard Comparisons

**Severance Formula Benchmarks:**

```
SEVERANCE BENCHMARKING
======================

YOUR PACKAGE:
- Tenure: [X years]
- Severance Weeks: [X weeks]
- Formula: [X weeks per year of service]

INDUSTRY BENCHMARKS:
| Level | Common Formula | Your Package | Assessment |
|-------|----------------|--------------|------------|
| Individual Contributor | 1-2 weeks per YOS | [X weeks] | [Above/At/Below] |
| Manager | 2-3 weeks per YOS | [X weeks] | [Above/At/Below] |
| Director | 2-4 weeks per YOS | [X weeks] | [Above/At/Below] |
| VP/Executive | 3-6 weeks per YOS | [X weeks] | [Above/At/Below] |
| C-Suite | 6-24 months | [X months] | [Above/At/Below] |

TYPICAL MINIMUMS:
| Tenure | Minimum Weeks | Your Package |
|--------|---------------|--------------|
| < 1 year | 2-4 weeks | [X weeks] |
| 1-3 years | 4-8 weeks | [X weeks] |
| 3-5 years | 8-12 weeks | [X weeks] |
| 5-10 years | 12-26 weeks | [X weeks] |
| 10+ years | 26+ weeks | [X weeks] |
```

**Benefits Continuation Benchmarks (Ontario):**

```
BENEFITS CONTINUATION BENCHMARKING
==================================
| Benefit | Typical Range | Your Package | Assessment |
|---------|---------------|--------------|------------|
| Extended health/dental continuation | 3-12 months | [X months] | [Above/At/Below] |
| Full benefits continuation | 1-3 months | [X months] | [Above/At/Below] |
| Outplacement | $3K-$15K value | [$X value] | [Above/At/Below] |
```

Note: Unlike US COBRA (employee pays), Ontario packages typically include employer-paid benefits continuation during notice period.

**Equity Treatment Benchmarks:**

```
EQUITY TREATMENT BENCHMARKING
=============================
| Treatment | Common Practice | Your Package | Assessment |
|-----------|-----------------|--------------|------------|
| Vesting Acceleration | None to pro-rata | [Your terms] | |
| Option Exercise Window | 90 days standard | [X days] | |
| RSU Treatment | Forfeit or pro-rata | [Your terms] | |
```

### 4.2 Geographic Considerations (Ontario)

Use web research to identify:
- Ontario ESA requirements (mass termination rules for 50+ employees)
- Ontario non-compete enforceability (largely unenforceable since Bill 27, 2021)
- Regional salary benchmarks (GTA vs. other Ontario regions)
- Common law reasonable notice precedents for similar roles

**For US users**: Research state-specific WARN Act requirements, non-compete enforceability, and local labor law variations.

### 4.3 Company-Specific Context

Research:
- Company's typical severance practices (Glassdoor, Blind)
- Recent layoff patterns and packages offered
- Financial health indicators
- Litigation history with former employees


## Phase 5: Negotiation Strategy (--counter-offer mode)

### 5.1 Negotiability Assessment

```
NEGOTIABILITY MATRIX
====================

TYPICALLY NEGOTIABLE:
| Element | Your Terms | Target | Priority | Strategy |
|---------|-----------|--------|----------|----------|
| Severance amount | [Current] | [Target] | [1-5] | [Approach] |
| COBRA subsidy duration | [Current] | [Target] | [1-5] | [Approach] |
| Non-compete scope/duration | [Current] | [Target] | [1-5] | [Approach] |
| Stock option exercise window | [Current] | [Target] | [1-5] | [Approach] |
| Equity acceleration | [Current] | [Target] | [1-5] | [Approach] |
| Reference language | [Current] | [Target] | [1-5] | [Approach] |
| Non-disparagement mutuality | [Current] | [Target] | [1-5] | [Approach] |
| Cooperation compensation | [Current] | [Target] | [1-5] | [Approach] |
| Signing deadline extension | [Current] | [Target] | [1-5] | [Approach] |

SOMETIMES NEGOTIABLE (Depends on Circumstances):
| Element | Your Terms | Notes |
|---------|-----------|-------|
| Release scope | [Current] | Easier if potential claims exist |
| Outplacement value | [Current] | Often flexible |
| Announcement language | [Current] | If departure is newsworthy |
| Departure date | [Current] | If flexibility helps transition |
| Title at departure | [Current] | If promotion was imminent |

RARELY NEGOTIABLE (Standard Boilerplate):
| Element | Notes |
|---------|-------|
| Entire agreement clause | Standard legal protection |
| Severability | Standard |
| Governing law | Usually company's state |
| Assignment | Standard |
```

### 5.2 Counter-Proposal Template

Generate specific language for each priority negotiation point:

```
COUNTER-PROPOSAL LANGUAGE
=========================

PRIORITY 1: [Element]
Current: "[Current language]"
Requested: "[Proposed new language]"
Rationale: [Why this is reasonable]

PRIORITY 2: [Element]
Current: "[Current language]"
Requested: "[Proposed new language]"
Rationale: [Why this is reasonable]

[Continue for top 5 priorities]
```

### 5.3 Negotiation Script

```
NEGOTIATION APPROACH
====================

OPENING STATEMENT:
"Thank you for presenting this separation agreement. I've reviewed it carefully and
would like to discuss a few modifications that would make this work for both parties."

KEY TALKING POINTS:
1. [Point with supporting rationale]
2. [Point with supporting rationale]
3. [Point with supporting rationale]

IF THEY PUSH BACK:
- "I understand your position. Could we explore [alternative]?"
- "What flexibility exists on [specific element]?"
- "If [X] isn't possible, would you consider [Y] instead?"

WALK-AWAY CONSIDERATIONS:
- What is the minimum acceptable package?
- What terms are absolute deal-breakers?
- What leverage points exist (potential claims, knowledge, relationships)?

CLOSING:
"I appreciate your willingness to discuss this. Can we schedule a follow-up
for [date] to finalize the terms?"
```

### 5.4 Leverage Assessment

```
LEVERAGE ANALYSIS
=================

YOUR LEVERAGE POINTS:
| Factor | Strength | How to Use |
|--------|----------|------------|
| Tenure/Institutional Knowledge | [High/Med/Low] | [Strategy] |
| Potential Legal Claims | [High/Med/Low] | [Strategy] |
| Transition Complexity | [High/Med/Low] | [Strategy] |
| Relationships/Client Knowledge | [High/Med/Low] | [Strategy] |
| Non-public Information | [High/Med/Low] | [Strategy] |
| Market Demand for Skills | [High/Med/Low] | [Strategy] |

COMPANY'S LEVERAGE POINTS:
| Factor | Impact | Mitigation |
|--------|--------|------------|
| Standard policy/precedent | [High/Med/Low] | [Approach] |
| Budget constraints | [High/Med/Low] | [Approach] |
| Just cause documentation | [High/Med/Low] | [Approach] |
| Time pressure | [High/Med/Low] | [Approach] |

Note: Ontario employees have strong notice entitlements; "at-will" employment does not exist. Employers need just cause (high bar) or must pay reasonable notice.
```


## Phase 6: Timeline Management

### 6.1 Critical Dates

```
TIMELINE ANALYSIS
=================

KEY DATES (ONTARIO):
| Event | Date | Days Remaining | Action Required |
|-------|------|----------------|-----------------|
| Agreement Presented | [Date] | N/A | |
| Signing Deadline | [Date] | [X days] | Review/Negotiate |
| Last Day of Employment | [Date] | [X days] | Transition |
| Benefits End | [Date] | [X days] | Arrange private coverage if needed |
| ROE Issuance Expected | [Termination + 5 days] | | Verify correct coding |
| First Severance Payment | [Date] | [X days] | |
| Non-Compete Begins | [Date] | [X days] | Often unenforceable in Ontario |
| Non-Compete Ends | [Date] | [X days] | |
| EI Application Window | [Termination + 4 weeks] | | Apply after waiting period | |

RECOMMENDED TIMELINE (ONTARIO):
| Day | Action |
|-----|--------|
| Today | Complete initial review |
| Day 2-3 | Consult employment lawyer if complex issues |
| Day 5-7 | Prepare counter-proposal |
| Day 7-10 | Submit counter-proposal |
| Day 10-14 | Negotiate modifications |
| By Deadline | Sign if satisfied (no statutory waiting period in Ontario) |

Note: Ontario has no mandatory 21-day consideration or 7-day revocation period like US OWBPA. However, courts may consider very short deadlines as evidence of duress. Request reasonable time if deadline is too tight.
```

### 6.2 Extension Request Template

If more time is needed:

```
DEADLINE EXTENSION REQUEST
==========================

Subject: Request for Extension - Separation Agreement Review

Dear [HR Contact],

Thank you for presenting the separation agreement dated [date]. Given the complexity
and importance of this document, I am requesting an extension of the signing deadline
from [current date] to [requested date].

This additional time will allow me to:
- [Carefully review all terms]
- [Consult with legal counsel]
- [Consider the implications for my family]

I remain committed to working toward a mutually agreeable resolution and appreciate
your consideration of this request.

Best regards,
[Name]
```


## Phase 7: Pre-Signing Checklist

### 7.1 Final Review Checklist

```
BEFORE SIGNING - VERIFY:
========================

UNDERSTANDING:
[ ] I understand every provision in this agreement
[ ] All unclear terms have been explained or clarified
[ ] I understand what I am giving up (claims released)
[ ] I understand what I am receiving (compensation and benefits)
[ ] I understand ongoing obligations (non-compete, cooperation, confidentiality)

LEGAL COMPLIANCE (ONTARIO):
[ ] Reasonable time to consider has been provided
[ ] Package exceeds ESA statutory minimums (required for valid release)
[ ] I have been advised to consult an employment lawyer
[ ] Release language is clear about claims being waived
[ ] ESA rights are preserved (cannot contract out of minimums)

NEGOTIATION COMPLETE:
[ ] All requested modifications addressed (accepted, rejected, or compromised)
[ ] Final version reflects all agreed changes
[ ] No last-minute additions or modifications slipped in
[ ] Comparison with original version confirms only agreed changes

PRACTICAL MATTERS (ONTARIO):
[ ] I have copies of all relevant documents
[ ] I have removed personal items from workplace
[ ] I have saved personal contacts outside company systems
[ ] I understand the return of property requirements
[ ] ROE coding has been confirmed (Code M preferred for EI)
[ ] Extended benefits continuation period is clear
[ ] I understand when to apply for EI (1-week waiting period after termination)

MENTAL READINESS:
[ ] I have had adequate time to consider this decision
[ ] I am not signing under duress or time pressure
[ ] I am comfortable with the trade-offs involved
[ ] I have discussed this with trusted advisors
```

### 7.2 Post-Signing Reminders

```
AFTER SIGNING (ONTARIO):
========================

IMMEDIATE (Within 1 Week):
[ ] Verify ROE received with correct coding (Code M for dismissal)
[ ] Apply for EI online at Service Canada (after 1-week waiting period)
[ ] Confirm extended benefits continuation start date

WITHIN 30 DAYS:
[ ] Arrange private health/dental coverage if benefits end soon
[ ] Update beneficiary designations if needed
[ ] Begin job search activities
[ ] Utilize outplacement services if provided
[ ] Exercise stock options if applicable (note deadlines)
[ ] Maximize RRSP contribution if receiving lump sum (tax planning)

ONGOING:
[ ] Comply with all agreement obligations
[ ] Keep copy of signed agreement in safe place
[ ] Track any cooperation requests and ensure compensation
[ ] Monitor non-compete end date (if applicable, often unenforceable)
[ ] Complete EI reports every 2 weeks while job searching
```


## Phase 8: Output Deliverables

### 8.1 Comprehensive Analysis Report

Save complete analysis to: `{config.directories.crisis_management}/severance_review_{YYYYMMDD}.md`

Structure:
```markdown
document_file: [path to agreement]
company: [company name]
generated_by: /severance-review
generated_on: [ISO8601 timestamp]
output_type: severance_analysis
status: [draft/final]
version: 1.0
total_package_value: $XXX,XXX
overall_assessment: [Favorable/Fair/Unfavorable]
recommendation: [Sign/Negotiate/Decline/Seek Legal Counsel]

# Severance Package Analysis Report
## Company: [Company Name]
## Date: [Date]


## Executive Summary
[2-3 sentence summary of package value and key concerns]
**Recommendation**: [Primary recommendation]


## Package Overview
[Extracted terms summary]

## Total Package Valuation
[Complete valuation breakdown]

## Red Flags Identified
[All red flags with severity and recommendations]

## Benchmarking Analysis (if --benchmark)
[Market comparisons]

## Negotiation Strategy (if --counter-offer)
[Counter-proposal and talking points]

## Timeline & Deadlines
[Critical dates and recommended actions]

## Pre-Signing Checklist
[Verification items]

## Recommendations
[Prioritized action items]


## Appendix
### Document Inventory
[List of documents analyzed]

### Glossary of Terms
[Key legal terms explained]

### When to Consult an Attorney
[Situations requiring legal expertise]
```

### 8.2 Quick Reference Card

Also generate a one-page summary:

```markdown
# Severance Quick Reference - [Company]

**Package Value**: $XXX,XXX (gross) / $XXX,XXX (est. net)
**Signing Deadline**: [Date] ([X days] remaining)
**Jurisdiction**: Ontario, Canada

## Key Terms
- Severance: [X weeks/months] (ESA: X weeks + Common Law: X months)
- Benefits: [X months extended health/dental continuation]
- Non-Compete: [X months, scope] (likely unenforceable in Ontario)

## Top 3 Red Flags
1. [Flag 1]
2. [Flag 2]
3. [Flag 3]

## Top 3 Negotiation Priorities
1. [Priority 1]: Ask for [X]
2. [Priority 2]: Ask for [X]
3. [Priority 3]: Ask for [X]

## Recommended Next Steps
1. [Action] by [Date]
2. [Action] by [Date]
3. [Action] by [Date]

## Seek Attorney If:
- [Condition 1]
- [Condition 2]
- [Condition 3]
```


## Special Situations

### Reduction in Force (RIF) / Group Layoff (Ontario)

If this is part of a group layoff:
- Verify ESA mass termination requirements met (50+ employees in 4-week period triggers extended notice)
- Check for Ministry of Labour Form 1 notification (employer obligation)
- Evaluate whether selection criteria suggest discrimination (Human Rights Code)
- Extended notice periods apply: 8 weeks (50-199), 12 weeks (200-499), 16 weeks (500+)
- Benefits must continue during statutory notice period

**US users**: Check WARN Act applicability (60-day notice for 100+ employees), OWBPA 45-day consideration period.

### Executive Packages

For VP-level and above:
- Expect enhanced severance (6-24 months typical)
- Review change-in-control provisions if applicable
- Evaluate D&O insurance continuation
- Consider reputation protection clauses
- Review announcement and press release language

### Retirement Incentives

For voluntary separation programs:
- Evaluate pension bridge payments
- Review retiree medical eligibility
- Consider Social Security coordination
- Evaluate 401(k) matching true-up

### Constructive Dismissal Concerns

If departure was not truly voluntary:
- Document circumstances leading to departure
- Preserve evidence of hostile conditions
- Note any retaliation timeline
- Consider whether release should include additional consideration


## When to Strongly Recommend Legal Counsel

Flag these situations for attorney consultation:

1. **Potential Discrimination Claims**: Pattern evidence of age, race, gender, disability, or other protected class discrimination
2. **Retaliation Concerns**: Termination followed whistleblowing, complaint, or protected activity
3. **Significant Equity**: Large unvested equity positions or complex option situations
4. **Non-Compete Concerns**: Role or industry where non-compete would severely limit career options
5. **Class Action Waiver**: Complex releases with class action waivers
6. **Unusual Provisions**: Terms you've never seen or don't understand
7. **High Stakes**: Package value exceeds $100,000 or involves executive-level considerations
8. **Pressure Tactics**: Employer pressuring for quick signature or threatening consequences
9. **International Complications**: Cross-border employment or immigration implications
10. **Inadequate Consideration**: Package seems well below market without explanation


## Tone Guidelines

Throughout this analysis, maintain:

- **Informative but not alarmist**: Identify issues without creating unnecessary anxiety
- **Practical and actionable**: Focus on what the candidate can actually do
- **Balanced perspective**: Acknowledge both employee and employer perspectives
- **Empowering**: Help candidate understand options and make informed decisions
- **Appropriately cautious**: Know when to recommend professional legal review
- **Time-aware**: Respect deadlines while ensuring adequate consideration


## Error Handling

**If agreement file not provided**:
- Request user provide the document
- Explain what document types are accepted
- Offer to analyze when document is available

**If agreement is incomplete or unclear**:
- Note missing sections
- Document assumptions made
- Recommend requesting complete documentation from employer

**If situation exceeds analysis scope**:
- Clearly identify limitations
- Recommend appropriate professional resources
- Continue with analysis where possible


## Session Start

Begin by:
1. Reading the provided agreement (`$1` if specified)
2. Delivering the disclaimers
3. **Conducting Phase 0: Statutory & Case Law Research** — use web search to research current statutes and relevant case law for the applicable jurisdiction. This is MANDATORY before any analysis proceeds.
4. Presenting the Legal Research Summary to the user
5. Parsing document metadata and terms (Phase 1)
6. Identifying red flags (Phase 2) — informed by the legal research
7. Calculating package value (Phase 3) — using statutory minimums and case law notice ranges as benchmarks
8. If `--benchmark`: Performing market analysis (Phase 4)
9. If `--counter-offer`: Generating negotiation strategy (Phase 5) — citing specific case law to support negotiation positions
10. Saving comprehensive analysis report


Now executing Severance Review analysis...
