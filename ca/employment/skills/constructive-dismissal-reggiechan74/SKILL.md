---
name: constructive-dismissal-reggiechan74
title: Constructive Dismissal Assessment Report
description: Assess whether workplace conditions constitute constructive dismissal
author: reggiechan74
author_url: https://github.com/reggiechan74/JobOps/tree/main/plugins/jobops/skills/constructive-dismissal
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

This command defaults to **Ontario, Canada** constructive dismissal law.

### Ontario Constructive Dismissal Framework

**The Farber v. Royal Trust Test (Leading Canadian Case)**:
- A constructive dismissal occurs when the employer unilaterally makes a substantial change to a fundamental term of the employment contract
- The employee must ask: "Would a reasonable person in my circumstances conclude that the essential terms of the employment contract have been substantially changed?"

**Key Ontario Principles:**
- **Unilateral Change**: Employer cannot fundamentally change job duties, compensation, reporting structure, or working conditions without consent
- **Fundamental Breach**: Changes must go to the root of the employment contract
- **Employee's Response**: Must object to changes and not "condone" them by continuing to work without protest
- **Working Under Protest**: Employee can continue working while objecting in writing to preserve claims

**Damages Available (Ontario):**
- **Reasonable Notice**: Common law notice (often 1 month per year of service, up to 24 months) based on Bardal factors
- **ESA Minimums**: Employment Standards Act provides minimum termination and severance pay
- **Bad Faith Damages**: Additional damages if employer acted in bad faith (Honda Canada v. Keays)
- **Human Rights Damages**: If constructive dismissal involved discrimination

**Critical Timing:**
- Must object to changes promptly (working under protest letter recommended)
- Must not wait too long before resigning (or may be seen as condoning)
- Continuing to work for extended period without objection may waive claims

**For US/UK users**: Specify `--jurisdiction=US` or `--jurisdiction=UK` for jurisdiction-specific standards.

## CRITICAL LEGAL DISCLAIMERS

**READ THESE DISCLAIMERS ALOUD TO THE USER AT SESSION START - THIS IS MANDATORY:**

### Disclaimer 1: This Is NOT Legal Advice
> **WARNING**: Constructive dismissal is a LEGAL DOCTRINE with jurisdiction-specific standards, case law precedents, and evidentiary requirements that vary significantly by location. This analysis is EDUCATIONAL ONLY and does NOT constitute legal advice. You MUST consult with a qualified employment attorney in your jurisdiction before making ANY decisions about resignation or legal claims.

### Disclaimer 2: Resignation Is a One-Way Door
> **CRITICAL**: Once you resign, you cannot un-resign. Premature resignation can:
> - Forfeit your ability to claim constructive dismissal
> - Waive unemployment benefits in many jurisdictions
> - Eliminate severance negotiation leverage
> - Make your departure appear voluntary
> - Weaken or destroy potential legal claims
>
> **DO NOT RESIGN** until you have consulted with an employment attorney and fully understand the implications.

### Disclaimer 3: Documentation Is Everything
> Your ability to prove constructive dismissal depends almost entirely on contemporaneous documentation. If you haven't been documenting, start NOW - but understand that building a strong case takes time.

### Disclaimer 4: Employer Actions After Complaint Matter
> Courts and tribunals generally require that you give your employer a reasonable opportunity to remedy the situation before resigning. Resigning immediately after a single incident - even a serious one - may not qualify as constructive dismissal in most jurisdictions.

### Disclaimer 5: Standards Vary Significantly by Jurisdiction
> What constitutes constructive dismissal in Canada may not qualify in Texas. What qualifies in California may not work in the UK. Jurisdiction matters enormously. This analysis provides general frameworks but cannot substitute for jurisdiction-specific legal advice.


## What Is Constructive Dismissal?

### Legal Definition

**Constructive dismissal** (also called constructive discharge or constructive termination) occurs when an employer's conduct is so unreasonable, hostile, or fundamentally breaches the employment relationship that a reasonable person in the employee's position would feel compelled to resign.

**Key Principle**: The resignation is treated BY LAW as an involuntary termination, potentially entitling the employee to:
- Wrongful termination remedies
- Severance pay
- Notice period compensation
- Damages for bad faith conduct
- Unemployment benefits (in some jurisdictions)

### The Core Test (General Framework)

Most jurisdictions apply some version of this test:

1. **Employer Action/Condition**: The employer took action or allowed conditions that fundamentally changed the employment relationship
2. **Objectively Intolerable**: A reasonable person in the employee's position would find the conditions intolerable
3. **Employer Intent or Knowledge**: The employer either intended to force resignation OR knew/should have known conditions were intolerable
4. **Reasonable Opportunity to Remedy**: The employee gave the employer reasonable notice and opportunity to remedy the situation (in most jurisdictions)
5. **Resignation as Direct Result**: The employee resigned because of, and shortly after, the intolerable conditions

**CRITICAL**: Failing ANY element typically defeats the claim.


## Jurisdiction-Specific Standards

Parse the `--jurisdiction` argument to provide tailored guidance:

### If --jurisdiction=US or --jurisdiction=federal (United States Federal Standard)

**The Harris v. Forklift Systems Framework (U.S.)**

Under U.S. federal law, constructive discharge requires:
1. **Deliberate Employer Action**: The employer deliberately made working conditions intolerable
2. **Objective Standard**: A reasonable person would have felt compelled to resign
3. **Intent to Force Resignation**: Evidence that employer intended to force the employee out

**Additional Considerations**:
- The burden of proof is on the employee
- Mere dissatisfaction or difficult working conditions are insufficient
- Single incidents rarely qualify (unless egregious)
- Pattern of conduct is typically required
- Must typically exhaust internal remedies first

**State Variations** (note these are general patterns - specifics vary):
- **California**: More employee-friendly, recognizes broader range of conditions
- **Texas**: Higher bar, requires more egregious conduct
- **New York**: Moderate standard, pattern of conduct typically required
- **Florida**: At-will state with higher threshold for claims

### If --jurisdiction=Canada or --jurisdiction=ON/BC/AB/etc.

**Canadian Standard: Fundamental Breach of Employment Contract**

Canada recognizes constructive dismissal when the employer:
1. **Unilaterally Changes Essential Terms**: Significant changes to compensation, duties, reporting structure, or working conditions
2. **Fundamentally Breaches Contract**: Actions that breach express or implied terms of employment
3. **Creates Hostile Environment**: Conduct making continued employment untenable

**The Farber v. Royal Trust Test**:
- Would a reasonable person in the employee's circumstances conclude that the essential terms of the employment contract had been substantially changed?

**Key Canadian Considerations**:
- Notice period damages typically 1 month per year of service (common law)
- Provincial Employment Standards provide minimums
- Bad faith damages possible (Wallace/Honda damages)
- Must typically object to changes before resigning
- "Working under protest" period is recognized
- Condoning changes over time may waive claims

**Provincial Variations**:
- Ontario: Well-developed case law, reasonable notice damages
- British Columbia: Similar to Ontario
- Alberta: Slightly different damages calculations
- Quebec: Civil law jurisdiction with different framework

### If --jurisdiction=UK (United Kingdom)

**UK Standard: Repudiatory Breach of Contract**

Under UK law, constructive dismissal occurs when:
1. **Employer's Conduct**: Amounts to a fundamental or repudiatory breach of contract
2. **Breach of Trust**: Destroys or seriously damages the implied duty of mutual trust and confidence
3. **Employee Response**: Employee resigns in response to the breach (not for unrelated reasons)
4. **Timing**: Employee does not delay too long (or may be seen as affirming the breach)

**Key UK Considerations**:
- Must prove breach of express or implied contractual term
- The "last straw" doctrine allows cumulative minor incidents
- Must not wait too long after breach to resign
- Employment Tribunal claims must be filed within 3 months minus 1 day
- ACAS early conciliation required before tribunal claim

### If --jurisdiction not specified (Default: Ontario)

When no jurisdiction is specified, **default to Ontario, Canada** and apply the Canadian/Farber v. Royal Trust test framework.

If user appears to be in a different jurisdiction (mentions US state, UK, etc.), confirm:
> **I'm defaulting to Ontario, Canada employment law. If you're in a different jurisdiction (e.g., a US state or UK), please specify using `--jurisdiction=X` (e.g., `--jurisdiction=California`, `--jurisdiction=UK`) for jurisdiction-specific guidance.**


## Common Qualifying Conditions

### Category 1: Compensation and Benefits Changes (HIGH Weight)

**Typically Qualifying Conditions:**
- [ ] Significant pay reduction (typically 10%+ without consent)
- [ ] Elimination of commission or bonus structure without replacement
- [ ] Demotion affecting compensation
- [ ] Reduction in hours for hourly employees
- [ ] Removal of significant benefits (health insurance, pension contributions)
- [ ] Failure to pay earned wages, commissions, or bonuses

**Assessment Questions:**
- What percentage reduction in total compensation occurred?
- Was written consent obtained?
- Were business justifications provided?
- Were others similarly affected?

### Category 2: Role and Responsibility Changes (HIGH Weight)

**Typically Qualifying Conditions:**
- [ ] Demotion in title or authority without cause
- [ ] Significant reduction in responsibilities
- [ ] Removal from key projects or accounts
- [ ] Stripping of supervisory responsibilities
- [ ] Assignment to demeaning or humiliating duties
- [ ] Fundamental change in job description without consent
- [ ] Elimination of role with offer of inferior position

**Assessment Questions:**
- How does new role compare to original job offer/description?
- What authority/responsibilities were removed?
- Is the change documented in writing?
- What business justification was provided?

### Category 3: Work Location Changes (MEDIUM-HIGH Weight)

**Typically Qualifying Conditions:**
- [ ] Forced relocation to distant location without consent
- [ ] Material change in commute (varies by jurisdiction - often 30+ miles)
- [ ] Removal of remote work arrangements without justification
- [ ] Reassignment to inferior workspace (punitive in nature)
- [ ] Geographic change affecting family/personal life significantly

**Assessment Questions:**
- How far is the new location from original?
- What notice was provided?
- What is the employment contract's mobility clause (if any)?
- Are relocation expenses offered?

### Category 4: Hostile Work Environment (HIGH Weight - Often Requires Pattern)

**Typically Qualifying Conditions:**
- [ ] Harassment by supervisor that employer failed to stop
- [ ] Pervasive discrimination based on protected characteristics
- [ ] Bullying, intimidation, or abusive conduct (pattern required)
- [ ] Sexual harassment not remedied after complaint
- [ ] Racial, gender, or other discriminatory harassment
- [ ] Creating unbearable psychological stress through conduct

**Critical Requirements:**
- **Pattern of Conduct**: Usually requires ongoing pattern, not single incident
- **Employer Knowledge**: Must typically show employer knew or should have known
- **Failure to Remedy**: Employer failed to take appropriate corrective action
- **Objective Standard**: Would affect a reasonable person, not just the complainant

### Category 5: Retaliation and Bad Faith (VERY HIGH Weight)

**Typically Qualifying Conditions:**
- [ ] Retaliation for protected activity (whistleblowing, discrimination complaint, etc.)
- [ ] Adverse action after protected leave (FMLA, parental leave, disability leave)
- [ ] Punishment for exercising legal rights
- [ ] Bad faith changes following legitimate complaint
- [ ] Creating pretextual performance issues after protected activity

**Red Flags for Retaliation:**
- Timing correlation between protected activity and adverse action
- Sudden negative feedback after protected activity
- Treatment differs from similarly situated employees
- Documented positive performance suddenly becomes "problematic"

### Category 6: Unsafe or Illegal Conditions (VERY HIGH Weight)

**Typically Qualifying Conditions:**
- [ ] Employer requiring illegal conduct
- [ ] Unsafe working conditions not remedied
- [ ] OSHA/safety violations
- [ ] Fraud, securities violations, or other illegal activity expected
- [ ] Regulatory violations the employee would be complicit in

**Special Considerations:**
- May have additional whistleblower protections
- May qualify for enhanced damages
- Document carefully - may need regulatory reporting

### Category 7: Breach of Employment Terms (Variable Weight)

**Typically Qualifying Conditions:**
- [ ] Breach of express contractual promises
- [ ] Violation of written policies that created enforceable obligations
- [ ] Failure to honor promotion or advancement commitments
- [ ] Breach of non-compete in exchange for nothing
- [ ] Material change to employment terms without consideration


## Input Document Handling

**Argument Handling:**
- If `$ARGUMENTS` contains a file path: Load specified incident log or documentation
- If no file specified: Conduct interview to gather information

@$ARGUMENTS

**Accepted Document Types:**
- Incident logs with dated entries
- Email correspondence
- HR communications
- Performance reviews (before and after)
- Employment contract and offer letter
- Company policies and handbooks
- Medical documentation (if health affected)
- Complaint filings and responses
- Personal notes with contemporaneous dates


## Phase 1: Comprehensive Intake Assessment

### 1.1 Condition Documentation Inventory

If documents provided, catalog:

```
INCIDENT/CONDITION DOCUMENTATION INVENTORY
==========================================
| # | Date | Condition/Incident | Source Document | Severity |
|---|------|-------------------|-----------------|----------|
| 1 | [Date] | [Description] | [File/Source] | High/Med/Low |
```

### 1.2 Structured Interview

**If documentation is limited, conduct structured interview:**

#### Section A: Baseline Establishment
1. **"Describe your employment situation before problems began."**
   - Job title, responsibilities, compensation
   - Relationship with manager
   - Performance reviews and feedback
   - Length of employment

2. **"When did you first notice conditions changing?"**
   - Specific date or timeframe
   - What triggered the change (if known)
   - Initial warning signs

#### Section B: Condition Assessment
3. **"Walk me through each significant change or incident, with dates."**
   - Create chronological timeline
   - Document each condition with specificity
   - Note witnesses present

4. **"For each condition, what specific impact has it had on you?"**
   - Professional impact (duties, authority, compensation)
   - Personal impact (health, family, finances)
   - Psychological impact

#### Section C: Remediation Attempts
5. **"What complaints have you made, and to whom?"**
   - Written complaints (dates, recipients, content)
   - Verbal complaints (dates, witnesses)
   - HR involvement
   - Union involvement (if applicable)

6. **"How has your employer responded to your complaints?"**
   - Remediation attempts
   - Dismissiveness or retaliation
   - Timeline of responses
   - Follow-up actions

#### Section D: Current Status
7. **"What is your current employment status?"**
   - Still employed?
   - On leave?
   - Working remotely?
   - Reduced hours?

8. **"Have you consulted with an employment attorney yet?"**
   - If yes: What was their assessment?
   - If no: Strong recommendation to do so before any resignation


## Phase 2: Condition Severity Analysis

### 2.1 Severity Rating Framework

For each documented condition, assess severity:

```
CONDITION SEVERITY ANALYSIS
===========================

| Condition | Category | Severity | Ongoing? | Evidence Level |
|-----------|----------|----------|----------|----------------|
| [Condition 1] | [Cat 1-7] | 🔴 Severe / 🟡 Moderate / 🟢 Minor | Yes/No | Strong/Moderate/Weak |

SEVERITY DEFINITIONS:
- 🔴 SEVERE: Fundamental breach likely qualifying for CD claim
- 🟡 MODERATE: Significant issue but may need pattern/additional factors
- 🟢 MINOR: Unlikely to support CD claim alone; may contribute to pattern
```

### 2.2 Pattern Analysis

**Single Incident vs. Pattern Assessment:**

Courts and tribunals typically require a pattern of conduct unless a single incident is egregious. Analyze:

- **Number of incidents/conditions**: Single vs. multiple
- **Duration of conditions**: Days, weeks, months
- **Escalation pattern**: Are conditions getting worse?
- **Cumulative effect**: "Last straw" doctrine applicability

```
PATTERN ANALYSIS
================
Number of documented conditions: [X]
Duration of intolerable conditions: [X days/weeks/months]
Escalation observed: Yes/No
"Last straw" event identified: [If applicable]
Pattern strength: Strong/Moderate/Weak/Insufficient
```

### 2.3 Reasonable Person Standard Application

**The Objective Test:**

Would a reasonable person in the employee's position, considering:
- The nature and severity of the conditions
- The duration of the conditions
- The employer's response to complaints
- Industry and role norms
- Geographic and economic context

...have felt compelled to resign?

```
REASONABLE PERSON ANALYSIS
==========================
Overall assessment: [ ] Yes - Reasonable person likely compelled to resign
                   [ ] Maybe - Borderline; additional factors needed
                   [ ] No - Conditions unlikely to meet threshold

Factors supporting reasonable person standard: [List]
Factors against reasonable person standard: [List]
```


## Phase 3: Exhaustion of Remedies Analysis

### 3.1 Internal Remedy Requirements

**CRITICAL**: Most jurisdictions require that the employee:
1. Complain to the employer about intolerable conditions
2. Give the employer reasonable opportunity to remedy
3. Employer fails to remedy or makes situation worse

**Exhaustion Checklist:**
```
EXHAUSTION OF REMEDIES CHECKLIST
================================
[ ] Complained in writing to direct supervisor
    Date: [Date] | Evidence: [Document]
[ ] Complained in writing to HR
    Date: [Date] | Evidence: [Document]
[ ] Complained to higher management (skip-level)
    Date: [Date] | Evidence: [Document]
[ ] Used internal grievance procedure (if available)
    Date: [Date] | Evidence: [Document]
[ ] Filed union grievance (if applicable)
    Date: [Date] | Evidence: [Document]
[ ] Gave employer reasonable time to respond
    Timeline: [Duration between complaint and resignation consideration]
[ ] Employer's response documented
    Response: [Summary of employer response]

EXHAUSTION STATUS:
[ ] COMPLETE - All reasonable internal remedies exhausted
[ ] PARTIAL - Some remedies attempted; additional steps recommended
[ ] MINIMAL - Insufficient complaint/remedy documentation
[ ] NONE - No formal complaints on record
```

### 3.2 Employer Response Assessment

**How did the employer respond to complaints?**

```
EMPLOYER RESPONSE ANALYSIS
==========================
| Complaint Date | Issue Raised | Employer Response | Response Quality |
|----------------|--------------|-------------------|------------------|
| [Date] | [Issue] | [Response] | Adequate/Inadequate/None |

OVERALL EMPLOYER RESPONSE RATING:
[ ] Good Faith Effort - Employer made reasonable attempts to remedy
[ ] Inadequate Response - Response was insufficient or ineffective
[ ] Retaliation - Conditions worsened after complaint
[ ] Ignored - No meaningful response to complaints
[ ] No Complaint Made - Cannot assess employer response
```


## Phase 4: Evidence Quality Assessment

### 4.1 Documentation Strength Analysis

```
EVIDENCE STRENGTH ASSESSMENT
============================

STRONG EVIDENCE (Direct, Contemporaneous, Corroborated):
- Written communications from employer documenting changes
- Emails, letters, or memos with dates and signatures
- Contemporaneous personal notes made at time of incidents
- Witness statements (signed, dated)
- HR records documenting complaints and responses
- Medical documentation if health affected

MODERATE EVIDENCE (Indirect but Supportive):
- Later-created summary documents
- Circumstantial evidence of changes
- Verbal accounts (your recollection)
- Pattern evidence without specific documentation

WEAK EVIDENCE (May Not Survive Challenge):
- Undated personal recollections
- Hearsay without corroboration
- Speculation about employer intent
- Evidence created specifically for litigation

YOUR EVIDENCE INVENTORY:
| Evidence Type | Description | Strength | Location |
|---------------|-------------|----------|----------|
| [Type] | [Description] | Strong/Moderate/Weak | [Where stored] |

OVERALL EVIDENCE ASSESSMENT: Strong/Moderate/Weak/Insufficient
```

### 4.2 Evidence Gaps Identification

**What documentation is missing that would strengthen a potential claim?**

```
CRITICAL EVIDENCE GAPS
======================
[ ] Missing: Written record of [specific condition/change]
[ ] Missing: Complaint documentation to employer
[ ] Missing: Employer response (or lack thereof) in writing
[ ] Missing: Witness statements for key incidents
[ ] Missing: Medical documentation for health impacts
[ ] Missing: Comparator evidence (how others treated)
[ ] Missing: Policy documentation showing violation

RECOMMENDED EVIDENCE GATHERING:
1. [Specific action to gather evidence]
2. [Specific action to gather evidence]
3. [Specific action to gather evidence]
```


## Phase 5: Risk Assessment Matrix

### 5.1 Comprehensive Risk Analysis

```
CONSTRUCTIVE DISMISSAL RISK ASSESSMENT
======================================

| Factor | Rating | Evidence | Notes |
|--------|--------|----------|-------|
| Condition Severity | 🔴🟡🟢 | [Evidence] | [Notes] |
| Pattern Established | 🔴🟡🟢 | [Evidence] | [Notes] |
| Reasonable Person Threshold | 🔴🟡🟢 | [Assessment] | [Notes] |
| Remedies Exhausted | 🔴🟡🟢 | [Evidence] | [Notes] |
| Evidence Strength | 🔴🟡🟢 | [Summary] | [Notes] |
| Employer Response | 🔴🟡🟢 | [Evidence] | [Notes] |
| Timing Considerations | 🔴🟡🟢 | [Analysis] | [Notes] |
| Jurisdiction Favorability | 🔴🟡🟢 | [Research] | [Notes] |

RATING KEY:
🔴 Favorable for CD claim / High risk for employer
🟡 Moderate / Uncertain
🟢 Unfavorable for CD claim / Low risk for employer
```

### 5.2 Claim Viability Assessment

```
CONSTRUCTIVE DISMISSAL CLAIM VIABILITY
=====================================

OVERALL ASSESSMENT: [ ] STRONG [ ] MODERATE [ ] WEAK [ ] INSUFFICIENT

STRONG factors supporting claim:
1. [Factor 1]
2. [Factor 2]
3. [Factor 3]

WEAK factors undermining claim:
1. [Factor 1]
2. [Factor 2]
3. [Factor 3]

CRITICAL GAPS that must be addressed:
1. [Gap 1]
2. [Gap 2]
3. [Gap 3]

PRELIMINARY VIABILITY SCORE: [X/10]
(Note: This is NOT legal advice. An employment attorney should assess actual viability.)
```


## Phase 6: Critical Mistakes to Avoid

### 6.1 Common Errors That Destroy Claims

**MISTAKE 1: Resigning Too Quickly**
> **Risk**: Courts may find you did not give employer opportunity to remedy
> **Mitigation**: Document complaints, wait for response, then assess

**MISTAKE 2: Not Complaining in Writing**
> **Risk**: No evidence employer knew about intolerable conditions
> **Mitigation**: Always follow up verbal complaints with written confirmation

**MISTAKE 3: Not Giving Employer Time to Remedy**
> **Risk**: "Reasonable opportunity" requirement not met
> **Mitigation**: Wait adequate time after complaint before resigning

**MISTAKE 4: Waiting Too Long (Condoning Conditions)**
> **Risk**: Continued work may be seen as acceptance of new terms
> **Mitigation**: Object to changes promptly; consider "working under protest" letter

**MISTAKE 5: Resigning for Wrong Reasons**
> **Risk**: If you cite other reasons (new job), CD claim weakened
> **Mitigation**: Resignation must be clearly caused by intolerable conditions

**MISTAKE 6: Burning Bridges at Departure**
> **Risk**: Emotional exit may undermine credibility; provide ammunition to employer
> **Mitigation**: Keep departure professional regardless of circumstances

**MISTAKE 7: Not Preserving Evidence**
> **Risk**: Evidence on company systems may be deleted
> **Mitigation**: BCC personal email; save key documents to personal storage

**MISTAKE 8: Discussing Resignation Before Attorney Consultation**
> **Risk**: May make statements that undermine case
> **Mitigation**: Consult attorney BEFORE telling anyone at work about plans


## Phase 7: Pre-Resignation Checklist

### 7.1 Mandatory Steps Before Any Resignation

```
PRE-RESIGNATION CHECKLIST - CONSTRUCTIVE DISMISSAL
==================================================

DOCUMENTATION REQUIREMENTS:
[ ] All intolerable conditions documented with dates and specifics
[ ] All written complaints to employer saved (copies in personal possession)
[ ] Employer responses (or non-responses) documented
[ ] Witness information collected (names, contact info, willingness to support)
[ ] Personal notes contemporaneous and dated
[ ] Medical documentation obtained (if health affected)

EXHAUSTION REQUIREMENTS:
[ ] Complained IN WRITING to appropriate parties (supervisor, HR, management)
[ ] Gave employer reasonable time to respond and remedy (typically 2-4 weeks minimum)
[ ] Employer failed to remedy OR conditions worsened OR retaliation occurred
[ ] Used internal grievance procedures (if available)
[ ] Documented employer's inadequate response

LEGAL CONSULTATION REQUIREMENTS:
[ ] Consulted with employment attorney in relevant jurisdiction
[ ] Understood jurisdiction-specific legal standards
[ ] Received assessment of claim viability
[ ] Discussed optimal timing for resignation (if proceeding)
[ ] Understood potential remedies and realistic outcomes
[ ] Reviewed resignation letter language

FINANCIAL PREPARATION:
[ ] Understand impact on unemployment eligibility in jurisdiction
[ ] Have financial runway of [X months] if income stops
[ ] Understand severance implications
[ ] Reviewed any non-compete or restrictive covenant implications

CAREER PREPARATION:
[ ] Resume updated
[ ] References secured (from current employer if safe; from elsewhere)
[ ] Job search initiated (if timing permits)
[ ] LinkedIn/network activated discretely

FINAL PRE-RESIGNATION CHECKS:
[ ] Evidence preserved to personal devices/storage
[ ] No company property or confidential information taken
[ ] Clear on what to say (and not say) in resignation
[ ] Understand notice period requirements
[ ] Know what happens to benefits, PTO, pending compensation
```

### 7.2 Checklist Status Summary

```
PRE-RESIGNATION READINESS ASSESSMENT
====================================

Documentation: [ ] Complete [ ] Partial [ ] Incomplete
Exhaustion: [ ] Complete [ ] Partial [ ] Incomplete
Legal Consultation: [ ] Complete [ ] Scheduled [ ] Not Done
Financial Prep: [ ] Complete [ ] Partial [ ] Not Assessed
Career Prep: [ ] Complete [ ] Partial [ ] Not Started

OVERALL READINESS: [ ] READY [ ] NEARLY READY [ ] NOT READY

CRITICAL GAPS BEFORE RESIGNATION:
1. [Gap 1]
2. [Gap 2]
3. [Gap 3]

RECOMMENDATION:
[ ] PROCEED with caution after addressing gaps
[ ] WAIT - Critical steps not completed
[ ] DO NOT RESIGN until attorney consultation complete
```


## Phase 8: Alternative Strategies

### 8.1 Stay and Document Strategy

**When to Consider:**
- Claim viability is currently weak but could strengthen
- Need time to build documentation
- Financial constraints prevent immediate departure
- Want to maximize potential damages

**Actions:**
1. Continue working while documenting everything
2. File written complaints creating paper trail
3. Request changes in writing; respond in writing
4. Build witness network
5. Seek medical documentation if health affected
6. Consider "working under protest" letter

**Risks:**
- Prolonged stress and difficult working conditions
- Conditions may improve, weakening claim
- May reach "acceptance" threshold if wait too long

### 8.2 Internal Escalation Strategy

**When to Consider:**
- Have not yet escalated to senior management
- Employer may not be fully aware of conditions
- Want to exhaust remedies before resignation

**Actions:**
1. Escalate complaints to skip-level management
2. File formal grievance if procedure exists
3. Request investigation by HR
4. Document all escalation attempts

### 8.3 External Agency Complaint Strategy

**When to Consider:**
- Discrimination, harassment, or retaliation involved
- Want to create official record outside employer
- Need external investigation

**Available Agencies:**
- **US**: EEOC (discrimination), OSHA (safety), DOL (wage violations)
- **Canada**: Provincial Human Rights Commission, Employment Standards Branch
- **UK**: ACAS, Employment Tribunal

**Benefits:**
- Creates official record
- May trigger investigation
- Preserves legal deadlines
- Shows good faith exhaustion

### 8.4 Negotiate Exit Package Strategy

**When to Consider:**
- Constructive dismissal claim has merit
- Prefer clean break to litigation
- Have leverage for negotiation
- Risk tolerance is moderate

**Leverage Points:**
- Documented intolerable conditions
- Protected class implications
- Pattern of conduct evidence
- Potential legal claims
- Employer's desire to avoid litigation/publicity

**Typical Package Components:**
- Severance payment
- Extended benefits
- Neutral reference
- Non-disparagement (mutual)
- Resignation vs. termination characterization

### 8.5 Medical Leave Strategy

**When to Consider:**
- Conditions have affected mental or physical health
- Need time to plan without working in hostile environment
- Want to preserve employment while assessing options

**Actions:**
1. Obtain medical documentation of condition
2. Request appropriate leave (FMLA, disability, stress leave)
3. Use time to consult attorney and plan
4. Return or resign based on circumstances


## Phase 9: Risk/Benefit Analysis

### 9.1 Comprehensive Decision Matrix

```
CONSTRUCTIVE DISMISSAL DECISION MATRIX
======================================

IF YOU RESIGN NOW CLAIMING CD:
Potential Benefits:
- [Benefit 1: e.g., severance, damages, notice pay]
- [Benefit 2: e.g., unemployment eligibility]
- [Benefit 3: e.g., escape from intolerable conditions]
Potential Risks:
- [Risk 1: e.g., claim may be denied]
- [Risk 2: e.g., litigation costs and stress]
- [Risk 3: e.g., career impact during dispute]
Probability of Success: [Assessment]

IF YOU STAY AND DOCUMENT:
Potential Benefits:
- [Benefit 1: e.g., stronger case]
- [Benefit 2: e.g., continued income]
- [Benefit 3: e.g., more time to job search]
Potential Risks:
- [Risk 1: e.g., conditions worsen]
- [Risk 2: e.g., health impact]
- [Risk 3: e.g., may reach "acceptance" threshold]

IF YOU NEGOTIATE EXIT:
Potential Benefits:
- [Benefit 1: e.g., clean break]
- [Benefit 2: e.g., guaranteed compensation]
- [Benefit 3: e.g., neutral reference]
Potential Risks:
- [Risk 1: e.g., may get less than litigation]
- [Risk 2: e.g., release of claims]
- [Risk 3: e.g., NDA restrictions]

IF YOU SIMPLY RESIGN (no CD claim):
Potential Benefits:
- [Benefit 1: e.g., immediate escape]
- [Benefit 2: e.g., no litigation]
- [Benefit 3: e.g., move on quickly]
Potential Risks:
- [Risk 1: e.g., no compensation]
- [Risk 2: e.g., unemployment issues]
- [Risk 3: e.g., forfeit potential claims]
```

### 9.2 Financial Impact Analysis

```
FINANCIAL IMPACT ASSESSMENT
===========================

POTENTIAL RECOVERY (if CD claim successful):
- Notice period damages: [Estimate based on jurisdiction/tenure]
- Severance: [If applicable]
- Bad faith damages: [If applicable in jurisdiction]
- Aggravated damages: [If applicable]
- Legal costs: [If recoverable in jurisdiction]
TOTAL POTENTIAL RECOVERY: $[Range]

COSTS OF PURSUING CLAIM:
- Legal fees (if not contingency): $[Estimate]
- Lost income during dispute: $[Estimate]
- Stress/health costs: [Subjective]
- Time investment: [Hours/Months]
TOTAL POTENTIAL COSTS: $[Range]

NET EXPECTED VALUE:
[Recovery probability] × [Potential recovery] - [Costs] = $[Range]

COMPARISON TO NEGOTIATED EXIT:
Typical negotiated severance: $[Estimate]
Probability of achieving: [Higher/Lower than litigation]
Time to resolution: [Shorter/Longer]
```


## Phase 10: If Proceeding with Constructive Dismissal Claim

### 10.1 Resignation Letter Considerations

**DO Include:**
- Clear statement that you are resigning due to intolerable conditions
- Brief summary of key conditions (without excessive detail)
- Reference to complaints made and employer's failure to remedy
- Statement that you consider this a constructive dismissal
- Request for confirmation of receipt

**DO NOT Include:**
- Excessive emotional language
- Every grievance in detail (save for legal proceedings)
- Personal attacks on individuals
- Anything you cannot prove
- Admission of any wrongdoing

**Sample Language Framework:**
> "Due to the intolerable working conditions described in my complaints dated [dates], and [Employer]'s failure to remedy these conditions despite adequate opportunity, I have no reasonable alternative but to resign effective [date]. I consider this resignation to be a constructive dismissal resulting from [brief description of fundamental breach/intolerable conditions]."

**CRITICAL**: Have an employment attorney review resignation letter language BEFORE submitting.

### 10.2 Timing Considerations

**Optimal Timing Factors:**
- After exhausting internal remedies
- After documenting employer's failure to remedy
- Before conditions are "accepted" through continued work
- After attorney consultation
- When financial/career circumstances permit
- If applicable: before upcoming vesting, bonus, or benefit dates

**Poor Timing:**
- Immediately after single incident (unless egregious)
- Before any written complaint
- During employer's "reasonable time" to remedy
- Long after last complaint without follow-up

### 10.3 Immediate Post-Resignation Steps

1. **Preserve Evidence**: Ensure all documentation is in personal possession
2. **Request Confirmation**: Get written acknowledgment of resignation
3. **ROE/Documentation**: Request Record of Employment (Canada) or equivalent
4. **Benefits Information**: Confirm COBRA/benefits continuation options
5. **Final Pay**: Confirm final paycheck, accrued PTO, pending compensation
6. **Legal Filing Deadlines**: Confirm with attorney when claims must be filed
7. **Unemployment Claim**: File if eligible (explain CD situation)


## Phase 11: Integration Points

This assessment integrates with other JobOps commands:

### Related Commands

- **`/code-red`**: For full employment crisis assessment (PIPs, terminations, conflicts)
- **`/buildresume`**: If transitioning to job search, create targeted resume
- **`/assessjob`**: Evaluate fit for new opportunities
- **`/briefing`**: Prepare for interviews while managing current situation
- **`/osint`**: Research potential new employers

### Recommended Workflow

1. Run `/constructive-dismissal` for initial assessment
2. If claim viable and proceeding with exit: Run `/code-red --mode=exit` for transition planning
3. Prepare for job search: Run `/buildresume` and `/assessjob` for target opportunities


## Phase 12: Output Deliverables

### 12.1 Assessment Report

Save comprehensive analysis to: `{config.directories.crisis_management}/constructive_dismissal_{YYYYMMDD}.md`

Structure:
```markdown
# Constructive Dismissal Assessment Report
## Date: [Date]
## Jurisdiction: [Jurisdiction]


## DISCLAIMERS
[Reproduce all critical disclaimers]


## Executive Summary
[2-3 sentence summary of situation and preliminary assessment]
**Preliminary CD Viability: [Strong/Moderate/Weak/Insufficient]**
**Primary Recommendation: [Stay/Go/Negotiate/Consult Attorney]**


## Documented Conditions
[Table of all documented intolerable conditions with severity ratings]

## Condition Severity Analysis
[Detailed assessment of each condition]

## Pattern Analysis
[Assessment of pattern vs. single incident]

## Reasonable Person Assessment
[Would a reasonable person feel compelled to resign?]

## Exhaustion of Remedies Status
[Analysis of complaints, employer responses, remaining remedies]

## Evidence Strength Assessment
[Current evidence quality and gaps]

## Risk Assessment Matrix
[Full risk analysis]

## Claim Viability Assessment
[Preliminary viability score with factors]


## Strategic Options Analysis
[Analysis of each alternative strategy]

## Risk/Benefit Analysis
[Decision matrix and financial impact]


## Recommendations

### Immediate Actions (Next 24-48 Hours)
1. [Action item]
2. [Action item]

### Short-Term Actions (1-2 Weeks)
1. [Action item]
2. [Action item]

### Recommended Path
[Primary recommendation with rationale]


## Pre-Resignation Checklist Status
[Complete checklist with current status]


## Critical Reminders
1. **DO NOT RESIGN** until consulting with employment attorney
2. **DOCUMENT EVERYTHING** in writing
3. **PRESERVE EVIDENCE** to personal devices
4. **EXHAUST REMEDIES** before resignation
5. **TIMING MATTERS** - not too fast, not too slow


## Appendix
### Interview Notes
[Summary of user responses]

### Evidence Inventory
[Detailed list of available evidence]

### Jurisdiction-Specific Considerations
[Relevant legal standards for user's jurisdiction]
```


## Tone and Approach

Throughout this assessment, maintain:

- **Cautious and measured**: Emphasize that resignation is irreversible
- **Educational not directive**: Provide frameworks, not decisions
- **Legally humble**: Consistently remind of attorney consultation need
- **Evidence-focused**: Ground all assessments in documented facts
- **Strategic**: Focus on building the strongest possible position
- **Empathetic**: Acknowledge the difficulty of the situation
- **Practical**: Provide actionable steps, not just theory


## Error Handling

**If insufficient documentation:**
- Note limitations explicitly
- Provide guidance on evidence that should be gathered
- Recommend not making decisions based on incomplete assessment

**If jurisdiction not specified:**
- Provide general framework only
- Strongly recommend jurisdiction specification
- Note that standards vary significantly

**If situation appears to require immediate legal intervention:**
- Stop assessment
- Prioritize attorney consultation recommendation
- Provide resources for finding employment counsel

**If discrimination or retaliation indicators present:**
- Note additional complexity and protections
- Recommend attorney consultation for these specific issues
- Reference applicable agency complaints (EEOC, HRC, etc.)


## Session Start

Begin by:
1. Reading any provided incident log or documentation (`$ARGUMENTS` if specified)
2. **READING ALL CRITICAL DISCLAIMERS ALOUD** (mandatory)
3. Determining jurisdiction (from `--jurisdiction` or asking user)
4. Conducting structured interview if documentation limited
5. Proceeding through assessment phases
6. Generating comprehensive output report


Now executing Constructive Dismissal Assessment...
