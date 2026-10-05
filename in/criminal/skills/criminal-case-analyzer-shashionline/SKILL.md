---
name: criminal-case-analyzer-shashionline
title: Criminal Case Analyzer Skill
description: Systematic criminal case analysis providing structured evaluation of fact patterns, applicable offences, evidence strength, burden of proof, and defense/prosecution strategies
author: shashionline
author_url: https://github.com/shashionline/indian-law-plugin/tree/master/skills/criminal-case-analyzer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: in
practice: criminal
language: en
---

# Criminal Case Analyzer Skill

## Skill Metadata
- **Skill ID**: criminal_case_analyzer
- **Version**: 1.0.0
- **Domain**: Criminal Law (India)
- **Specialization**: Systematic case analysis, strategy development
- **Dependencies**: All 28 criminal law protocols
- **Effective Date**: January 2025

---

## Skill Purpose

Reusable analytical capability for **systematic criminal case analysis**, providing structured evaluation of:
- Fact patterns and timelines
- Applicable offences and ingredients
- Evidence strength and admissibility
- Burden of proof allocation
- Defense and prosecution strategies
- Risk assessment and recommendations

---

## Input Parameters

### Required Inputs:
1. **Case Facts**: Detailed narrative of what happened
2. **Date of Incident**: Determines IPC vs BNS applicability
3. **Perspective**: Defense or Prosecution
4. **Current Stage**: FIR, investigation, arrest, trial, appeal

### Optional Inputs:
5. **Evidence Available**: Witness statements, documents, forensic reports
6. **Accused Details**: Background, antecedents, personal circumstances
7. **Specific Questions**: Targeted issues to address

---

## Analysis Framework

### Phase 1: Fact Analysis and Organization

**Objective**: Extract and structure key facts

**Process**:
```
1. **Chronological Timeline**:
   - When did each event occur?
   - Sequence of events leading to offence
   - Post-offence actions

2. **Actor Identification**:
   - Victim(s): Name, age, relationship to accused
   - Accused: Name, age, occupation, antecedents
   - Witnesses: Eyewitnesses, formal witnesses (police, doctor)
   - Third parties: Any other relevant persons

3. **Location Analysis**:
   - Where did offence occur?
   - Jurisdiction (determines police station, court)
   - Public vs private place (may affect offence classification)

4. **Actus Reus (Physical Act)**:
   - What physical act was committed?
   - How was it committed? (Weapon? Force? Deception?)
   - What was the result? (Death, injury, loss)

5. **Mens Rea (Mental State)**:
   - Intention to commit act?
   - Knowledge of consequences?
   - Negligence or recklessness?
   - Premeditation vs sudden provocation?

6. **Motive**:
   - Why did accused commit act? (Relevant but not essential)
   - Strengthens prosecution case if established
```

**Output**: Structured fact summary with timeline, actors, actus reus, mens rea

---

### Phase 2: Offence Identification

**Objective**: Identify all applicable offences

**Process**:
```
1. **Determine Applicable Law**:
   - If offence occurred BEFORE July 1, 2024: Use IPC 1860
   - If offence occurred ON OR AFTER July 1, 2024: Use BNS 2023
   - Read IL-CRIM-IPC-BNS-TRANSITION.md for mapping

2. **Primary Offence Analysis**:
   - Based on actus reus and mens rea, identify main offence
   - Examples:
     - Death caused + intention → Murder (IPC 302 / BNS 103)
     - Death caused + knowledge but no intention → Culpable homicide not amounting to murder (IPC 304 / BNS 105)
     - Sexual assault → Rape (IPC 376 / BNS 64-71)
     - Property taken + force → Robbery (IPC 392 / BNS 309)

3. **Related Offences**:
   - Identify all additional offences committed
   - Example: Rape case may include:
     - Rape (IPC 376 / BNS 64)
     - Criminal intimidation (IPC 506 / BNS 351)
     - Wrongful confinement (IPC 342 / BNS 127)

4. **Essential Ingredients Check**:
   - For each identified offence, list essential ingredients
   - Read relevant protocol (e.g., IL-CRIM-MURDER.md)
   - Extract ingredients from protocol

5. **Fact-to-Ingredient Mapping**:
   - Map available facts to each ingredient
   - Identify which ingredients are established
   - Identify gaps or weaknesses
```

**Output**: List of applicable offences with ingredients and fact mapping

---

### Phase 3: Evidence Evaluation

**Objective**: Assess strength and admissibility of evidence

**Process**:
```
1. **Evidence Categorization**:

   **A. Oral Evidence**:
   - Eyewitness testimony
   - Victim statement
   - Expert opinion (doctor, FSL)
   - Character evidence

   **B. Documentary Evidence**:
   - FIR copy
   - Dying declaration
   - Medical reports
   - Contracts, letters (in fraud/cheating cases)

   **C. Electronic Evidence**:
   - WhatsApp messages
   - CCTV footage
   - Call detail records (CDR)
   - GPS data
   - Social media posts

   **D. Physical Evidence**:
   - Weapon (murder weapon, knife)
   - Stolen goods (theft/robbery cases)
   - Fingerprints, DNA
   - Blood-stained clothes

2. **Admissibility Analysis** (Use IL-CRIM-EVIDENCE-ADMISSIBILITY.md):

   For each piece of evidence:

   **Step 1: Relevancy** (Section 5 Evidence Act/BSA)
   - Is it fact in issue or relevant fact?
   - If not relevant → INADMISSIBLE

   **Step 2: Hearsay Check** (Section 60)
   - Is witness testifying to what they personally saw/heard?
   - OR is it hearsay (heard from someone else)?
   - If hearsay → Check exceptions (dying declaration, admission, etc.)

   **Step 3: Electronic Evidence** (Section 65B)
   - If electronic → Section 65B certificate required (Anvar P.V. case)
   - Without certificate → INADMISSIBLE

   **Step 4: Confession Check** (Sections 24-30)
   - Confession to police → ALWAYS INADMISSIBLE (Section 25)
   - Confession before Magistrate (Section 164) → Admissible if voluntary

   **Step 5: Primary vs Secondary** (Sections 62-65)
   - Original document (primary) preferred
   - Photocopy (secondary) only if original unavailable (Section 65)

3. **Strength Assessment**:

   **Direct Evidence**:
   - Eyewitness saw accused commit crime → Strong if credible
   - Check witness credibility: Interested witness? Related? Contradictions?

   **Circumstantial Evidence**:
   - No direct evidence, only circumstances (motive, opportunity, recovery)
   - Apply Panchsheel Principles (Sharad Sarda case):
     1. Circumstances fully established?
     2. Consistent only with guilt?
     3. Conclusive nature?
     4. Exclude every hypothesis except guilt?
     5. Chain complete (no missing link)?
   - If any principle fails → Weak circumstantial case

   **Corroboration**:
   - Single witness enough? OR corroboration needed?
   - Dying declaration: Can be sole basis if truthful (Laxman case)
   - Sexual assault: Victim testimony sufficient; no corroboration required

4. **Chain of Custody** (Physical Evidence):
   - Seizure → Sealing → FSL → Court production
   - Any break in chain → Evidence may be unreliable
```

**Output**: Evidence inventory with admissibility status and strength rating

---

### Phase 4: Burden of Proof Analysis

**Objective**: Determine who must prove what and to what standard

**Process** (Use IL-CRIM-BURDEN-PROOF.md):
```
1. **General Rule**:
   - **Burden on PROSECUTION** to prove guilt
   - **Standard**: BEYOND REASONABLE DOUBT (very high standard)

2. **What Prosecution Must Prove**:
   - All essential ingredients of offence
   - Actus reus (physical act committed)
   - Mens rea (intention/knowledge/negligence)
   - Identity of accused
   - No general exception applies

3. **Burden on Accused** (Section 105):
   - **If accused claims general exception** (self-defense, insanity, mistake, etc.)
   - **Standard**: PREPONDERANCE OF PROBABILITIES (balance of probabilities - lower than beyond reasonable doubt)
   - Accused need NOT prove beyond reasonable doubt, only show "more likely than not"

4. **Presumptions** (Sections 113A, 113B, 114):

   **Section 113A: Abetment of Suicide by Married Woman**:
   - If married woman commits suicide within 7 years + husband/relatives subjected her to cruelty
   - **Presumption**: Husband/relatives abetted suicide
   - **Effect**: Reverse burden on accused

   **Section 113B: Dowry Death**:
   - If woman dies within 7 years of marriage + cruelty/harassment for dowry proved
   - **Presumption**: Husband/relatives caused dowry death
   - **Effect**: Reverse burden on accused

5. **Practical Application**:

   **Example: Murder with Self-Defense Claim**:
   - Prosecution must prove:
     1. Accused caused death (beyond reasonable doubt)
     2. With intention to cause death (beyond reasonable doubt)
   - Accused must prove:
     1. Self-defense (preponderance of probabilities)
     2. Imminent threat, no retreat, proportionate force

   **Example: Dowry Death**:
   - Prosecution must prove:
     1. Woman died within 7 years of marriage
     2. Cruelty/harassment for dowry occurred soon before death
   - Then presumption arises under Section 113B
   - Accused must rebut presumption (prove innocence)
```

**Output**: Burden allocation matrix showing who proves what and to what standard

---

### Phase 5: Strategy Development

**Objective**: Develop prosecution or defense strategy

#### A. PROSECUTION STRATEGY

**If perspective is Prosecution**:

```
1. **Case Strengths**:
   - List strongest evidence
   - Direct evidence available?
   - Credible witnesses?
   - Forensic evidence (DNA, fingerprints)?

2. **Case Weaknesses**:
   - Identify gaps
   - Missing evidence?
   - Witness credibility issues?
   - Circumstantial evidence chain incomplete?

3. **Evidence Collection Priority**:
   - What additional evidence needed?
   - Witnesses not yet examined?
   - Forensic tests pending?
   - Section 65B certificates obtained?

4. **Anticipated Defenses**:
   - What will defense argue?
   - Self-defense claim likely?
   - Alibi expected?
   - Exception under IPC/BNS?

5. **Prosecution Strategy**:
   - How to prove each ingredient?
   - Witness examination order
   - Documentary evidence production plan
   - Cross-examination preparation
   - Closing argument themes
```

#### B. DEFENSE STRATEGY

**If perspective is Defense**:

```
1. **Prosecution Weaknesses**:
   - Where is prosecution case weak?
   - Unreliable witnesses?
   - Evidence inadmissible?
   - Ingredients not proved?

2. **Defense Options**:

   **Option A: Challenge Prosecution Case**:
   - Show reasonable doubt
   - Highlight contradictions
   - Challenge admissibility
   - Cross-examination strategy
   - NO burden on defense to prove innocence

   **Option B: Affirmative Defense (Exception)**:
   - Claim general exception (self-defense, insanity, etc.)
   - Read IL-CRIM-GENERAL-EXCEPTIONS.md
   - Gather evidence to prove exception
   - Remember: Burden on accused (Section 105)
   - Standard: Preponderance (easier than beyond reasonable doubt)

   **Option C: Alibi**:
   - Accused was elsewhere when offence occurred
   - Alibi witnesses
   - Documentary proof (bills, tickets, CCTV)

3. **Cross-Examination Strategy**:
   - Identify prosecution witnesses to discredit
   - Prepare leading questions
   - Confront with prior inconsistent statements (Section 161)
   - Show bias/interest

4. **Section 313 Preparation**:
   - Anticipate incriminating circumstances to be put
   - Prepare coherent explanations
   - Right to remain silent vs duty to explain

5. **Defense Evidence**:
   - Defense witnesses needed?
   - Should accused testify? (Pros and cons)
   - Expert evidence to rebut prosecution experts?
```

**Output**: Comprehensive strategy document with action items

---

### Phase 6: Risk Assessment

**Objective**: Identify risks and mitigation strategies

**Process**:
```
1. **Legal Risks**:
   - What is worst-case outcome?
   - Maximum sentence for offences charged?
   - Likelihood of conviction based on evidence?

2. **Procedural Risks**:
   - Delay in trial?
   - Witness turning hostile?
   - Evidence degradation (physical evidence)?

3. **Strategic Risks**:
   - For Defense: Alibi breaks down under cross-examination?
   - For Prosecution: Key witness credibility destroyed?

4. **Mitigation Strategies**:
   - How to reduce risks?
   - Backup witnesses?
   - Alternative defenses?
   - Plea bargaining options? (Section 265A-265L CrPC / 290-305 BNSS)
```

**Output**: Risk matrix with mitigation plan

---

## Output Format

```markdown
# CRIMINAL CASE ANALYSIS REPORT

## CASE SUMMARY
[One-paragraph overview]

## FACT ANALYSIS

### Timeline
| Date/Time | Event | Actors Involved |
|-----------|-------|-----------------|
| [Date] | [Event description] | [Actors] |

### Key Facts
- **Victim**: [Details]
- **Accused**: [Details]
- **Actus Reus**: [Physical act]
- **Mens Rea**: [Mental state]
- **Motive**: [If established]

## OFFENCE ANALYSIS

### Applicable Law
- Offence Date: [Date]
- Applicable Statute: [IPC 1860 / BNS 2023]

### Offences Identified

#### Primary Offence: [Offence Name]
**Statutory Provision**: [IPC/BNS Section]
**Punishment**: [Imprisonment + Fine details]

**Essential Ingredients**:
1. [Ingredient 1]
   - Status: Established / Not Established / Uncertain
   - Evidence: [Supporting evidence]

2. [Ingredient 2]
   - Status: [As above]
   - Evidence: [As above]

#### Related Offences
- [Offence 2]: [Section]
- [Offence 3]: [Section]

## EVIDENCE EVALUATION

### Evidence Inventory

| Evidence Type | Description | Admissible? | Strength | Notes |
|---------------|-------------|-------------|----------|-------|
| Oral | Eyewitness X | Yes | Strong | Credible, no contradictions |
| Documentary | Medical report | Yes | Strong | Corroborates injury |
| Electronic | WhatsApp msgs | No | N/A | No Section 65B certificate |
| Physical | Murder weapon | Yes | Medium | Chain of custody gap |

### Circumstantial Evidence Analysis
[If applicable, apply Panchsheel Principles]

## BURDEN OF PROOF

### On Prosecution (Beyond Reasonable Doubt)
- [Element 1 to prove]
- [Element 2 to prove]

### On Accused (Preponderance of Probabilities)
- [If exception claimed: Element to prove]

### Presumptions Applicable
- [Section 113A / 113B / etc. if applicable]

## STRATEGY RECOMMENDATIONS

### [For Prosecution / For Defense]

**Strengths**:
- [Strength 1]
- [Strength 2]

**Weaknesses**:
- [Weakness 1]
- [Weakness 2]

**Recommended Approach**:
[Detailed strategy]

**Action Items**:
1. [Action 1 with timeline]
2. [Action 2 with timeline]

## RISK ASSESSMENT

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | High/Medium/Low | High/Medium/Low | [Strategy] |

## NEXT STEPS

1. **Immediate** (0-7 days): [Actions]
2. **Short-term** (1-4 weeks): [Actions]
3. **Long-term** (1-3 months): [Actions]

## PROTOCOL REFERENCES
- [Protocol 1]
- [Protocol 2]
```

---

## Skill Limitations

1. **Protocol-Dependent**: Analysis quality depends on reading relevant protocols
2. **Fact-Dependent**: Accuracy depends on completeness of facts provided
3. **Not Legal Advice**: This is analytical tool, not substitute for licensed counsel
4. **India-Specific**: Applies only to Indian criminal law
5. **Current as of January 2025**: Laws may change

---

## Integration with Agents

This skill is used by:
- **criminal-law-specialist** agent: For comprehensive case analysis
- **criminal-procedure-expert** agent: For procedural strategy
- **evidence-analyst** agent: For evidence evaluation component

Can be invoked via:
- `/criminal-law-advice` command
- Direct agent consultation

---

**End of Skill: criminal_case_analyzer**
