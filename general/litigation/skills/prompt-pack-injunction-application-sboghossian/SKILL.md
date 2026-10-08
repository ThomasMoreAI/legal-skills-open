---
name: prompt-pack-injunction-application-sboghossian
title: Injunction Application
description: Use when drafting an application for a preliminary or permanent injunction in court litigation — addressing the four-factor test of likelihood of success on the merits, irreparable harm, balance of hardships, and public interest. Applicable for civil courts in UAE (onshore and DIFC/ADGM), Lebanon, Egypt, KSA, UK, EU, and US. Distinct from the emergency arbitrator application skill which is for arbitral interim relief. Trigger when a client needs a court order to restrain a party from taking an action or to compel performance before a full trial.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-injunction-application
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Injunction Application

## When to use this

Use this skill when a party to litigation needs to apply for injunctive relief — an order from the court either restraining a party from taking a specific action (prohibitory injunction) or requiring a party to take a specific action (mandatory injunction). Injunctions are one of the most powerful tools in litigation because they can alter the status quo before the full case is resolved.

Distinct from [[prompt-pack-emergency-arbitrator-application]] (which is for arbitral interim measures) and from [[prompt-pack-enforcement-of-judgment]] (which is post-judgment execution).

Typical triggers:
- Company needs to stop a former employee from joining a competitor in violation of a non-compete
- Intellectual property holder needs to stop infringement immediately (not wait for trial)
- Assets are being dissipated and a Mareva (freezing) injunction is needed
- A developer is about to demolish a structure in a property dispute and immediate restraint is needed
- A party is breaching a contract in a way that will cause irreversible damage

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Court and jurisdiction | Determines the legal test and procedural rules | Ask |
| Client / applicant identity | The party seeking the injunction | Ask |
| Respondent identity | The party to be restrained | Ask |
| Description of the conduct to be restrained or ordered | Defines the relief sought | Ask with specificity |
| Urgency and timing | Why the injunction cannot wait for a full hearing | Ask |
| Legal basis for the underlying claim | The injunction must support a viable main claim | Ask |

## Optional inputs

- Whether the application is ex parte (without notice to the respondent) or inter partes (with notice)
- Whether damages would be an adequate remedy (critical to the test)
- Evidence of the respondent's financial position (for Mareva injunctions)
- Undertaking in damages the applicant is willing to give
- Prior correspondence with the respondent

## Document structure

### 1. Heading and court details

- Court name, division (Chancery Division in UK; DIFC Court of First Instance; UAE Court of First Instance)
- Case title: [Applicant] v [Respondent]
- Application type: "Without Notice Application for Interim Injunction" or "On Notice Application"

### 2. Introduction

State the relief sought in one paragraph:
> "The Applicant, [name], applies for an interim injunction restraining the Respondent, [name], from [specific conduct] pending the trial of this action / until further order."

### 3. Background facts (supporting affidavit or witness statement)

The application is typically supported by an affidavit or witness statement containing:
- The commercial relationship between the parties
- The right or obligation the Applicant seeks to protect
- The conduct of the Respondent that triggers the application
- The date the Applicant became aware of the threatened or actual breach
- Urgency: what will happen if the injunction is not granted today

The witness statement should be a first-person account of the facts; hearsay must be identified and explained.

### 4. Legal analysis — the test for an injunction

The test varies by jurisdiction but follows a common structure in most common-law and hybrid systems:

#### Common-law test (DIFC Courts, ADGM Courts, UK — _American Cyanamid_ v _Ethicon_)

**a) Serious question to be tried**: Is there a "serious question" on the main claim? This is a low threshold — the claimant need not show they will win, only that the claim is not frivolous.

**b) Would damages be an adequate remedy?**
- If the Applicant would be adequately compensated by damages at trial, a court is less likely to grant an injunction
- Where the harm is: unique (cannot be replaced); uncertain in quantification; to a business relationship or reputation; or the Respondent is unlikely to be able to pay damages — the injunction is more justified

**c) Balance of convenience (balance of hardships)**:
- The court weighs: harm to Applicant if injunction refused vs. harm to Respondent if injunction granted
- If the balance is even, the court may consider: preservation of the status quo; strength of each party's case
- Applicant's cross-undertaking in damages: the court will usually require the Applicant to undertake to compensate the Respondent for losses caused by the injunction if the Applicant ultimately fails at trial

**d) Public interest** (relevant in some cases: IP, competition, regulatory)

#### Mareva / Freezing injunction (asset preservation)

Higher threshold; Applicant must show:
- Good arguable case on the merits
- Real risk that the Respondent will dissipate assets before judgment
- Amount frozen limited to the Respondent's apparent liability; must not cripple the Respondent's business

Standard order includes: a worldwide assets schedule above a minimum threshold; exclusions for living expenses and legal fees; notice to third parties (banks).

#### Anton Piller / Search order

Even higher threshold:
- Extremely strong prima facie case
- Actual damage would be very serious
- There is real possibility that the Respondent would destroy evidence if given notice

#### Civil-law conservatory measures (UAE onshore, Lebanon, Egypt)

Civil-law courts use different terminology and tests:
- UAE: "Conservatory measures" (tadabeer tahatiyyah) under UAE Civil Procedure Law; can include: attachment orders (hajz); injunction to prevent specific acts; appointment of a custodian
- The UAE Civil Procedure Law (Federal Law No. 42 of 2022, as amended) and its DIFC/ADGM equivalents set out the procedure
- Lebanon: "Mesures provisoires" under Lebanese Code of Civil Procedure; judge in chambers can grant urgent conservatory measures
- Egypt: "Ijra'at tahatiyyah" under Egyptian Civil Procedure Code; similar conservatory measures framework

### 5. Specific relief requested

State the injunction terms with precision:

**Prohibitory injunction (restrain conduct)**:
> "The Respondent, whether by itself or through its directors, employees, agents, or otherwise, be restrained until further order of this Court from: (a) [specific act 1]; (b) [specific act 2]."

**Mandatory injunction (compel action)**:
> "The Respondent do forthwith: (a) [specific action to be taken]; (b) [deliver/provide/restore specific item]."

**Mareva injunction (asset freeze)**:
> "The Respondent must not remove from [jurisdiction] or in any way dispose of, deal with, or diminish the value of any of its assets in [jurisdiction] up to the value of USD [amount]. This includes, without limitation, [specific assets identified]."

### 6. Applicant's cross-undertaking in damages

Almost all interim injunction applications require the Applicant to give:
> "The Applicant gives the Court an undertaking to comply with any order the Court may make if the Court later finds that this order has caused loss to the Respondent for which the Applicant should pay."

The value of this undertaking must be considered: if the injunction is ultimately refused or dissolved, the Applicant may owe substantial compensation.

### 7. Ex parte (without notice) applications

Where the application is made without notice to the Respondent:
- Full and frank disclosure: the Applicant must disclose all material facts, including those that might support the Respondent's position — failure to do so is grounds to discharge the order
- Urgency justification: explain specifically why the matter is so urgent that it could not wait for notice
- Fortification of cross-undertaking: courts may require security (money paid into court) for ex parte orders

## Jurisdictional notes

| Jurisdiction | Interim measure | Test | Enforcement |
|---|---|---|---|
| **DIFC Courts** | Interim injunction | American Cyanamid / balance of convenience | DIFC Court enforcement; DIFC Bailiff Service |
| **ADGM Courts** | Interim injunction | Similar to DIFC | ADGM Court enforcement |
| **UAE onshore courts** | Conservatory attachment; provisional injunction | Urgency + prima facie case + potential prejudice | Court of Execution enforcement after order |
| **Lebanon** | Mesures provisoires (judge in chambers) | Urgency + apparent right | Lebanese enforcement courts (slow) |
| **Egypt** | Provisional measures | Urgency + likelihood of right + irreparable harm | Egyptian court bailiff; practically challenging |
| **KSA** | "Hajz tahatiyyati" (conservative attachment) via execution court | Urgency + apparent right + risk of dissipation | Saudi Execution Court |
| **UK** | Interim injunction | American Cyanamid; higher for mandatory; even higher for search order | High Court Enforcement Officers; contempt of court |

## Common mistakes

- **Insufficient urgency**: Courts see "emergency" applications that are not actually emergencies; if the applicant knew about the conduct for weeks before applying, courts are skeptical.
- **No cross-undertaking offered**: Failing to offer a cross-undertaking in damages will result in refusal; consider whether the undertaking can be fortified with a payment into court.
- **Over-broad injunction terms**: Courts will refuse injunctions that are not clearly defined — "restrain the Respondent from acting in any way adverse to the Applicant" is not an injunction; specify the exact conduct.
- **Full and frank disclosure failures (ex parte)**: Omitting facts that favor the Respondent in an ex parte application can result in the order being discharged and costs being awarded against the Applicant.
- **Injunction as the first step without a notice letter**: Courts in some jurisdictions expect the Applicant to have sent a demand or warning letter before applying for an injunction (except where notice would defeat the purpose); send a legal notice first.

## Related skills

- [[prompt-pack-emergency-arbitrator-application]]
- [[prompt-pack-draft-legal-notice]]
- [[prompt-pack-enforcement-of-judgment]]
- [[prompt-pack-discovery-request]]
