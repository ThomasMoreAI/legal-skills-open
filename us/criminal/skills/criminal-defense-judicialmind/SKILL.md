---
name: criminal-defense-judicialmind
title: Criminal Defense
description: Criminal defense law skill for defense representation and criminal proceedings. Use when the user needs assistance with criminal charges, motions practice, discovery, plea negotiations, sentencing, or appeals. Triggers on keywords like "criminal", "felony", "misdemeanor", "indictment", "arraignment", "bail", "plea", "sentencing", "probation", "appeal", "suppression", "Miranda", "Fourth Amendment".
author: judicialmind
author_url: https://github.com/judicialmind/legal-skills/tree/main/skills/criminal-defense
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: criminal
language: en
sources:
- title: Appeals
  path: references/appeals.md
- title: Motion Practice
  path: references/motion-practice.md
- title: Sentencing Guide
  path: references/sentencing-guide.md
---

# Criminal Defense

This skill provides expert guidance for criminal defense practice from investigation through appeal.

## Core Capabilities

### 1. Pretrial Practice
- Initial appearance and bail
- Discovery analysis
- Motion practice
- Investigation

### 2. Trial Preparation
- Jury selection
- Evidence review
- Witness preparation
- Trial strategy

### 3. Plea Negotiations
- Charge bargaining
- Sentence bargaining
- Cooperation agreements
- Diversion programs

### 4. Sentencing and Appeals
- Sentencing advocacy
- Post-conviction remedies
- Direct appeals
- Habeas corpus

## Criminal Procedure Overview

### Federal Criminal Process
```
Investigation → Arrest/Summons → Initial Appearance →
Preliminary Hearing (if no GJ) → Grand Jury/Indictment →
Arraignment → Discovery → Pretrial Motions →
Plea or Trial → Sentencing → Appeal
```

### Key Timeframes (Federal)
| Event | Rule | Deadline |
|-------|------|----------|
| Initial appearance | Rule 5(a) | Without unnecessary delay |
| Preliminary hearing | Rule 5.1 | 14 days (detained) / 21 days (released) |
| Indictment | Rule 6 | 30 days if detained |
| Arraignment | Rule 10 | Prompt |
| Speedy Trial | 18 U.S.C. §3161 | 70 days from indictment/appearance |
| Discovery | Rule 16 | Varies by court |
| Pretrial motions | Rule 12 | Per court schedule |

## Constitutional Rights

### Fourth Amendment (Search & Seizure)

**Warrant Requirement**:
- Neutral magistrate
- Probable cause
- Particularity (place and items)

**Warrant Exceptions**:
| Exception | Requirements |
|-----------|--------------|
| Consent | Voluntary, scope limited |
| Search Incident to Arrest | Lawful arrest, immediate area |
| Automobile | Probable cause, mobile vehicle |
| Plain View | Lawful position, immediately apparent |
| Exigent Circumstances | Hot pursuit, destruction of evidence, emergency |
| Terry Stop | Reasonable suspicion |
| Inventory | Standardized procedures |

**Exclusionary Rule**: Evidence from unconstitutional search excluded
**Exceptions**: Good faith, independent source, inevitable discovery, attenuation

### Fifth Amendment

**Self-Incrimination**:
- Miranda warnings required for custodial interrogation
- Custody + interrogation = Miranda required
- Waiver must be knowing, intelligent, voluntary
- Invocation must be unambiguous

**Miranda Warnings**:
1. Right to remain silent
2. Anything said can be used against you
3. Right to an attorney
4. If cannot afford, one will be appointed

**Double Jeopardy**:
- Same offense, same sovereign
- Attaches when jury sworn or first witness
- Exceptions: Hung jury, mistrial at defendant's request, appeal reversal

### Sixth Amendment

**Right to Counsel**:
- At all critical stages
- Attaches at initiation of adversarial proceedings
- Effective assistance required (Strickland)

**Confrontation Clause**:
- Right to cross-examine witnesses
- Testimonial hearsay requires opportunity for cross (Crawford)

**Speedy Trial**:
- Barker v. Wingo factors: Length, reason, assertion, prejudice

## Discovery (Federal Rule 16)

### Government Must Disclose
- Defendant's statements
- Defendant's prior record
- Documents and tangible objects
- Reports of examinations/tests
- Expert witness disclosures

### Brady Material
**Prosecutor Must Disclose**:
- Evidence favorable to defendant
- Material to guilt or punishment
- Includes impeachment evidence (Giglio)

**Timing**: Sufficiently in advance for effective use

### Jencks Act (18 U.S.C. §3500)
- Witness statements after direct examination
- Prior statements related to testimony
- Defense must move for production

## Pretrial Motions

### Motion to Suppress (Fourth Amendment)
```
MOTION TO SUPPRESS EVIDENCE

Defendant moves to suppress [evidence] on the grounds that
it was obtained in violation of the Fourth Amendment.

STATEMENT OF FACTS
[Factual basis for motion]

ARGUMENT
I. THE SEARCH/SEIZURE VIOLATED THE FOURTH AMENDMENT
   A. [No warrant/invalid warrant]
   B. [No applicable exception]

II. THE EXCLUSIONARY RULE REQUIRES SUPPRESSION
   A. [Evidence is fruit of unlawful search]
   B. [No exception applies]

REQUEST FOR HEARING
Defendant requests an evidentiary hearing on this motion.
```

### Motion to Suppress Statements (Fifth Amendment)
- Involuntary statements
- Miranda violations
- Sixth Amendment violations (post-charging)
- Delay in presentment (McNabb-Mallory)

### Other Common Motions
| Motion | Purpose |
|--------|---------|
| Motion to Dismiss | Challenge sufficiency of indictment |
| Bill of Particulars | Compel specification of charges |
| Severance | Separate counts or defendants |
| Change of Venue | Pretrial publicity |
| Motion in Limine | Exclude prejudicial evidence |
| Franks Hearing | Challenge warrant affidavit |

## Trial Practice

### Jury Selection (Voir Dire)

**Challenges**:
- For cause: Unlimited, bias shown
- Peremptory: Limited number, cannot be discriminatory (Batson)

**Batson Challenge Steps**:
1. Prima facie case of discrimination
2. Race-neutral explanation required
3. Court determines if pretext

### Burden of Proof
- Prosecution must prove every element beyond a reasonable doubt
- Defendant has no burden to prove innocence
- Defendant may raise affirmative defenses (varies by jurisdiction)

### Common Defenses
| Defense | Elements |
|---------|----------|
| Alibi | Defendant elsewhere |
| Self-defense | Reasonable belief of imminent harm, proportionate response |
| Duress | Threat of death/serious harm, no reasonable escape |
| Entrapment | Government inducement + no predisposition |
| Insanity | Varies by jurisdiction (M'Naghten, irresistible impulse) |
| Intoxication | Voluntary (specific intent); involuntary (general) |

## Sentencing

### Federal Sentencing Guidelines

**Calculation Steps**:
1. Determine base offense level
2. Apply specific offense characteristics
3. Apply adjustments (role, obstruction, acceptance)
4. Calculate criminal history category
5. Determine guideline range
6. Consider departures and variances

**18 U.S.C. §3553(a) Factors**:
1. Nature and circumstances of offense
2. History and characteristics of defendant
3. Purposes of sentencing (punishment, deterrence, protection, rehabilitation)
4. Kinds of sentences available
5. Sentencing guidelines and policy statements
6. Need to avoid unwarranted disparities
7. Need for restitution

### Sentencing Memorandum
```
1. Introduction
2. Personal history and characteristics
3. Acceptance of responsibility
4. Sentencing guideline calculation
5. §3553(a) analysis
6. Proposed sentence
7. Supporting exhibits
```

### Sentencing Options
| Option | Description |
|--------|-------------|
| Imprisonment | BOP custody |
| Probation | Supervision in community |
| Supervised release | Post-imprisonment supervision |
| Fine | Monetary penalty |
| Restitution | Compensation to victims |
| Forfeiture | Property seizure |
| Special conditions | Treatment, restrictions |

## Appeals

### Direct Appeal
**Timing**: Notice within 14 days (federal criminal)
**Scope**: Issues preserved in trial court
**Standards of Review**:
- De novo: Legal questions
- Clear error: Factual findings
- Abuse of discretion: Evidentiary rulings
- Plain error: Unpreserved errors

### Post-Conviction Remedies

**28 U.S.C. §2255** (Federal Prisoners):
- Sentence imposed in violation of Constitution/laws
- Court lacked jurisdiction
- Sentence exceeds statutory maximum
- Subject to attack collaterally

**Habeas Corpus** (State Prisoners - §2254):
- Exhaustion of state remedies required
- AEDPA deference to state courts
- Procedural default bars
- Actual innocence gateway

### Ineffective Assistance of Counsel (Strickland)
1. **Deficient performance**: Fell below objective standard of reasonableness
2. **Prejudice**: Reasonable probability of different outcome

## Integration with Other Skills

- **litigation**: Motion practice, trial skills
- **legal-research**: Case law research
- **brief-writing**: Appellate briefs
- **immigration**: Immigration consequences
- **e-discovery**: Digital evidence

## Reference Files

For detailed guidance:
- `references/motion-practice.md` - Criminal motion templates
- `references/sentencing-guide.md` - Federal sentencing guidelines
- `references/appeals.md` - Post-conviction procedures
