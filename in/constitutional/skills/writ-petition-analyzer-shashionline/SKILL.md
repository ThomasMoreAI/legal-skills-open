---
name: writ-petition-analyzer-shashionline
title: Writ Petition Analyzer
description: Analyze writ petition viability - assess locus standi, alternative remedy, grounds for judicial review, appropriate writ type, and likelihood of success
author: shashionline
author_url: https://github.com/shashionline/indian-law-plugin/tree/master/skills/writ-petition-analyzer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: in
practice: constitutional
language: en
---

# Writ Petition Analyzer

## Purpose
Perform systematic legal analysis to determine if writ petition under Article 226 (High Court) or Article 32 (Supreme Court) is viable, assess chances of success, recommend appropriate writ type, and provide strategic guidance.

## Skill Workflow

### Step 1: Gather Case Facts

When invoked, extract/request the following:

**Essential Information**:
1. **User's Issue**: What happened? What is user challenging?
   - Government action (order passed, permission denied, etc.)
   - Government inaction (duty not performed, service not delivered)

2. **Respondent**: Who is the authority?
   - Central/State Government department
   - Local body (municipality, panchayat)
   - PSU, statutory corporation
   - Private entity (check if "State" under Article 12)

3. **Facts**:
   - When did violation occur?
   - What did user do? (Applied for service, received order, etc.)
   - What did authority do/not do?
   - Any alternative remedy pursued? (Departmental appeal, tribunal, etc.)

4. **Relief Sought**: What does user want?
   - Quash an order
   - Compel authority to do something (issue license, grant permission, etc.)
   - Declare action unconstitutional
   - Compensation

5. **Timing**:
   - When did cause of action arise?
   - How long ago? (Check for laches - delay)

### Step 2: Writ Viability Assessment Framework

Analyze in the following sequence:

---

#### A. Respondent Classification - Is It "State"?

**Test**: Writs issue ONLY against "State" (Article 12).

**State Includes**:
- ✅ Central/State Government
- ✅ Parliament, State Legislatures
- ✅ Local authorities (municipalities, panchayats)
- ✅ "Other authorities" (if Ajay Hasia test satisfied):
  - Financially/functionally controlled by government?
  - Deep and pervasive state control?
  - Performing public/sovereign function?
  - Created by statute for public purpose?

**Examples**:
- ✅ LIC, ONGC, Air India (PSUs) → State
- ✅ Universities, Medical Council (statutory bodies) → State
- ❌ Private companies (no government control) → NOT State
- ❌ Private schools (unless government-aided with deep control) → Usually NOT State

**Analysis Output**:
```
**Respondent**: [Name of authority]
**Classification**: [State / NOT State]
**Reasoning**: [Why it's State - government department / PSU with state control / OR why NOT State - private entity]

**Writ Maintainability**: [Yes, against State / No, writ not maintainable - suggest civil suit instead]
```

**If NOT State**: Stop analysis. Recommend civil suit, not writ.

---

#### B. Locus Standi - Does User Have Standing?

**Test**: Who can file writ?

**Traditional Standing** (Aggrieved Person):
- User's own legal right violated
- Direct, personal interest in matter

**PIL Standing** (Public Interest Litigation):
- Issue affects public/marginalized groups
- Affected persons unable to approach court
- User is bonafide (NGO, public-spirited citizen)
- Substantial question of public importance

**Analysis**:
1. **Is user directly affected?**
   - If YES → Strong standing (aggrieved person)
   - If NO → Check PIL viability

2. **If NOT directly affected, is PIL appropriate?**
   - Does issue affect large public/marginalized groups?
   - Are affected persons poor/illiterate/unable to approach court?
   - Is user bonafide (NGO working in field, credible activist)?
   - **OR is it publicity PIL** (politician, busybody, vested interest)?

**Analysis Output**:
```
**Standing Assessment**:
- **Directly Affected**: [Yes - User is aggrieved person / No - Not personally affected]
- **Legal Right Violated**: [Fundamental right (Article __) / Statutory right (__ Act, Section __) / Contractual right]

[If PIL applicable:]
- **PIL Viability**: [Strong/Moderate/Weak]
- **Public Interest Element**: [Describe how issue affects public]
- **Bonafide Assessment**: [User is NGO/activist with credibility / OR User appears to be publicity-seeker]

**Standing Conclusion**: [User has strong standing / Moderate standing (PIL possible but must prove bonafide) / Weak standing (likely to be dismissed)]
```

---

#### C. Alternative Remedy - Must It Be Exhausted?

**General Rule**: Must exhaust alternative statutory remedy (tribunal, departmental appeal) before writ.

**Exceptions** (When writ maintainable despite alternative remedy):
1. **Jurisdictional Error**: Tribunal/authority lacks jurisdiction
2. **Violation of Natural Justice**: No hearing given, bias
3. **Perversity**: Order based on no evidence, absurd
4. **Fundamental Right Violation**: Article 32/226 for fundamental rights not easily ousted
5. **Delay/Ineffective Remedy**: Alternative remedy so delayed it's illusory

**Analysis**:
1. **Is alternative remedy available?**
   - Tribunal (CAT, NCLT, ITAT, DRT, NGT, etc.)?
   - Departmental appeal?
   - Statutory appeal authority?

2. **If YES, does exception apply?**
   - Check against 5 exceptions above

3. **If NO exception**: Writ likely to be dismissed on "alternative remedy" ground.

**Analysis Output**:
```
**Alternative Remedy Available**: [Yes - CAT/NCLT/Departmental Appeal/etc. / No]

[If Yes:]
**Exception Applicable**: [Yes/No]
- **Exception Type**: [Jurisdictional error / Natural justice violation / Perversity / Fundamental right / Delay]
- **Reasoning**: [Explain why exception applies]

**Recommendation**:
- [If exception applies: Writ maintainable despite alternative remedy]
- [If no exception: Exhaust alternative remedy first (file CAT/tribunal), then writ if unsuccessful]
```

---

#### D. Grounds for Judicial Review

**Test**: Does user's case engage grounds for judicial review?

**Wednesbury Grounds**:
1. **Illegality**: Action beyond jurisdiction, contrary to law
2. **Irrationality**: So unreasonable no reasonable authority would do it
3. **Procedural Impropriety**: Natural justice violated (no hearing, bias)
4. **Proportionality**: Action disproportionate to objective
5. **Malafide**: Action for improper purpose, malicious

**Constitutional Violations**:
- **Article 14**: Arbitrary, discriminatory
- **Article 19(1)(a-g)**: Fundamental freedoms violated (speech, movement, profession, etc.)
- **Article 21**: Life, liberty, livelihood violated

**Analysis**:
Identify which grounds apply to user's case.

**Analysis Output**:
```
**Grounds for Judicial Review** (Applicable to your case):

1. **[Ground Name - e.g., Illegality]**
   - **Basis**: [Action violates __ Act, Section __ / Ultra vires / No jurisdiction]
   - **Evidence**: [Impugned order cites wrong provision / Authority acted beyond powers]

2. **[Ground Name - e.g., Procedural Impropriety]**
   - **Basis**: Natural justice violated - [No hearing given / Biased authority]
   - **Evidence**: [User not given opportunity to be heard / Decision-maker has conflict of interest]

3. **[Constitutional Violation - e.g., Article 14]**
   - **Basis**: Action is arbitrary/discriminatory
   - **Evidence**: [Similarly situated persons treated differently / No rational nexus to objective]

**Strength of Grounds**: [Strong - Clear violation / Moderate - Arguable / Weak - Tenuous connection]
```

---

#### E. Appropriate Writ Type Selection

**Match User's Need to Writ Type**:

**Mandamus** ("We command"):
- **When**: Authority refuses to perform legal duty
- **Conditions**:
  - Duty is mandatory (not discretionary)
  - User has legal right
  - No adequate alternative remedy
- **Example**: Passport approved but not issued → Mandamus to issue

**Certiorari** ("To be certified"):
- **When**: Order already passed, want to quash
- **Grounds**: Jurisdictional error, natural justice violation, error of law
- **Example**: University dismissed student without hearing → Certiorari to quash dismissal order

**Prohibition** ("Forbid"):
- **When**: Proceedings ongoing, want to stop
- **Timing**: Before final order (preventive)
- **Example**: Tribunal hearing case beyond jurisdiction → Prohibition to stop proceedings

**Habeas Corpus** ("Produce the body"):
- **When**: Illegal detention
- **Urgency**: Extreme (HC may hear same day)
- **Example**: Person held by police beyond 24 hours without magistrate production → Habeas corpus

**Quo Warranto** ("By what authority"):
- **When**: Challenge unauthorized office holding
- **Conditions**: Public office, person presently holding, appointment violates eligibility
- **Example**: VC appointed without UGC norms → Quo warranto

**Multiple Writs**: Can seek multiple in single petition (Certiorari to quash + Mandamus to compel correct decision).

**Analysis Output**:
```
**Appropriate Writ Type**: [Mandamus / Certiorari / Prohibition / Habeas Corpus / Quo Warranto]

**Why This Writ**:
- **User's Need**: [Compel duty performance / Quash illegal order / Stop excess jurisdiction / Secure release / Challenge appointment]
- **Writ Function**: [Mandamus compels mandatory duty / Certiorari quashes illegal order / etc.]

**Conditions Met**: [List conditions for this writ and confirm user's case meets them]

**Relief Formula**:
"Issue writ of [writ type] directing respondent to [specific relief]."
```

---

#### F. Delay/Laches Assessment

**No Statutory Limitation** for writs, but **laches** (unexplained delay) can bar relief.

**Analysis**:
1. **When did cause of action arise?** (Date of impugned order / date of violation)
2. **When is user filing writ?** (Current date)
3. **Delay**: [X months/years]
4. **Is delay explained?**
   - Reasonable if: 0-6 months (fresh), 6-12 months (acceptable with explanation)
   - Questionable if: 1-3 years (must explain)
   - Likely barred if: 5-10+ years (laches applies)

**Analysis Output**:
```
**Timing Analysis**:
- **Cause of Action**: [Date]
- **Current Date**: [Date]
- **Delay**: [X months/years]

**Laches Risk**: [Low - Delay minimal / Moderate - 1-2 year delay, must explain / High - 3+ years, strong explanation needed]

**Explanation for Delay** (if applicable): [User pursuing alternative remedy / Unaware of rights / Just discovered violation / etc.]

**Recommendation**: [File immediately - no delay issue / File with detailed delay explanation in petition / Delay may bar relief - weak case on laches]
```

---

### Step 3: Forum Selection - HC or SC?

**High Court (Article 226)**:
- Fundamental rights + **any legal right**
- Discretionary (HC may refuse)
- Local/state issues
- Faster, cheaper

**Supreme Court (Article 32)**:
- **Only fundamental rights**
- Guaranteed remedy
- National importance
- Costly, slower admission

**Recommendation Logic**:
- If only legal/statutory right (not fundamental) → **HC only**
- If fundamental right + local issue → **HC** (faster, cheaper)
- If fundamental right + national policy/multiple states → **SC**

**Analysis Output**:
```
**Forum Recommendation**: [High Court / Supreme Court]

**Reasoning**:
- **Right Violated**: [Fundamental right (Article __) → SC/HC both possible / Legal right only → HC only]
- **Scope**: [Local/state issue → HC / National importance → SC]
- **Practical Considerations**: [HC faster and cheaper for local issues / SC if need authoritative precedent]

**Recommended Court**: [High Court of [State] / Supreme Court of India]
**Territorial Jurisdiction**: [Based on: Cause of action arose in [State] / Respondent's office in [State] / Petitioner's residence in [State]]
```

---

### Step 4: Likelihood of Success Assessment

**Synthesize all factors to assess chances**:

**Strong Case** (70-90% success likelihood):
- Clear statutory violation
- Mandatory duty not performed (no discretion)
- Natural justice violated
- Fundamental right clearly violated
- Strong evidence
- No alternative remedy OR exception applies
- Minimal delay

**Moderate Case** (40-70% success likelihood):
- Arguable legal violation
- Some discretion involved (but arbitrary exercise)
- Grounds present but need strong advocacy
- Alternative remedy exists but exception arguable
- Some delay (1-2 years, explainable)

**Weak Case** (10-40% success likelihood):
- Involves policy decision (court reluctant to interfere)
- Discretionary action (unless proven malafide/arbitrary)
- Alternative remedy not exhausted, no exception
- Significant unexplained delay (3+ years)
- Weak grounds (tenuous legal basis)

**Analysis Output**:
```
**Overall Assessment**: [Strong/Moderate/Weak Case]

**Success Likelihood**: [70-90% / 40-70% / 10-40%]

**Strengths**:
1. [Clear violation of __ Act, Section __]
2. [Fundamental right (Article __) violated]
3. [No alternative remedy available]

**Weaknesses**:
1. [Some delay - must explain]
2. [Involves some discretion - must prove arbitrary]
3. [Alternative remedy available - but exception applies because...]

**Recommendation**:
- [If Strong: Strongly recommend filing writ petition]
- [If Moderate: Writ petition viable, engage experienced advocate]
- [If Weak: Consider alternative remedies (tribunal, representation, RTI) before writ]
```

---

### Step 5: Strategic Recommendations

**Evidence to Gather**:
- Impugned order (if challenging an order)
- Correspondence with authority
- RTI responses (government's own admission of facts)
- Statutory provisions, rules, Citizens Charter (to prove mandatory duty)
- Similar cases where relief granted (if available)

**Procedural Strategy**:
- If alternative remedy exists: Pursue it first (unless exception clear), then writ if fails
- If urgent: File interim application (stay order, preserve status quo)
- Engage advocate experienced in [service law/administrative law/constitutional law] writs

**Interim Relief Viability**:
- Prima facie case: [Strong/Moderate]
- Balance of convenience: [In favor of user/authority]
- Irreparable injury: [Will user suffer if interim stay not granted?]

**Timeline & Costs Estimate**:
- **Filing to Admission**: 2-4 weeks
- **Admission to Disposal**: 6 months - 3 years (varies by HC backlog)
- **Costs**: ₹30,000 - ₹2,50,000+ (court fee + advocate fee + miscellaneous)

**Analysis Output**:
```
**Strategic Recommendations**:

**Evidence to Gather**:
1. [Impugned order copy]
2. [Correspondence with respondent]
3. [RTI response showing __ (if applicable)]
4. [Statutory provision copy (__ Act, Section __) proving mandatory duty]

**Procedural Path**:
[Recommend: Direct writ / Exhaust alternative remedy first / RTI first for evidence, then writ]

**Interim Relief**:
[Strong case for interim stay - user suffers irreparable harm if order implemented / Moderate - may or may not get stay / Weak - unlikely to get interim relief]

**Advocate Engagement**:
Strongly recommend engaging advocate experienced in [administrative law writs / service law / constitutional law].

**Timeline**: 6 months - 2 years (realistic for final disposal)

**Estimated Costs**:
- Court fee: ₹5,000 - 10,000
- Advocate fee: ₹25,000 - 2,00,000+ (depends on case complexity, advocate seniority)
- Miscellaneous: ₹5,000 (drafting, photocopies, travel)
- **Total**: ₹35,000 - ₹2,50,000+
```

---

### Step 6: Consolidated Output

Provide user with comprehensive analysis in structured format:

```markdown
# Writ Petition Viability Analysis

## Your Issue (Summary)
[2-3 sentence summary of user's problem]

---

## Viability Assessment

### 1. Respondent Classification
**Respondent**: [Name]
**Is "State"?**: [Yes/No]
**Reasoning**: [Why it's State / Why not]
**Writ Maintainability**: [Yes/No]

### 2. Locus Standi
**Standing**: [Aggrieved person / PIL applicant]
**Legal Right Violated**: [Article __ / __ Act, Section __]
**Standing Strength**: [Strong/Moderate/Weak]

### 3. Alternative Remedy
**Available**: [Yes - CAT/Tribunal / No]
**Exception Applicable**: [Yes - Natural justice violation / No]
**Recommendation**: [Direct writ / Exhaust remedy first]

### 4. Grounds for Judicial Review
1. **[Ground 1]**: [Illegality - violates __ Act]
2. **[Ground 2]**: [Procedural impropriety - no hearing]
3. **[Constitutional]**: [Article 14 - arbitrary]

**Ground Strength**: [Strong/Moderate/Weak]

### 5. Appropriate Writ Type
**Recommended Writ**: [Mandamus / Certiorari / Prohibition / Habeas Corpus / Quo Warranto]
**Relief Formula**: "Issue writ of [writ] directing respondent to [specific action]."

### 6. Delay/Laches
**Delay**: [X months/years]
**Laches Risk**: [Low/Moderate/High]
**Explanation Needed**: [Yes - provide detailed explanation / No - fresh case]

### 7. Forum Recommendation
**Forum**: [High Court of [State] / Supreme Court]
**Reasoning**: [Local issue, legal right → HC / National, fundamental right → SC]

---

## Overall Assessment

**Success Likelihood**: [Strong: 70-90% / Moderate: 40-70% / Weak: 10-40%]

**Strengths**:
1. [Clear statutory violation]
2. [Fundamental right engaged]
3. [No alternative remedy]

**Weaknesses**:
1. [Some delay]
2. [Discretionary element]

**Recommendation**: [Strongly recommend filing writ / Viable but engage experienced advocate / Consider alternatives before writ]

---

## Strategic Guidance

**Evidence to Gather**: [List]

**Procedural Path**: [Direct writ / Alternative remedy first / RTI + writ]

**Interim Relief**: [Strong/Moderate/Weak case for stay]

**Timeline**: 6 months - 2 years

**Costs**: ₹35,000 - ₹2,50,000+

**Advocate Engagement**: Strongly recommended (writ petitions require legal expertise)

---

**Protocols for Detailed Study**:
- CIVIC-WRIT-BASICS (Writ jurisdiction, locus standi)
- CIVIC-WRIT-TYPES (Five writs explained)
- [CIVIC-TRIBUNALS if alternative remedy involves tribunal]
```

---

## Integration with Agents

This skill is invoked by:
- **admin-law-specialist** when user asks "Can I file writ?"
- **india-civic-law-specialist** orchestrator for writ viability questions

Skill returns comprehensive analysis enabling user to make informed decision on writ filing.

---

**Writ petitions are powerful constitutional remedies. This skill ensures citizens approach courts only with viable cases, saving time and costs.**
