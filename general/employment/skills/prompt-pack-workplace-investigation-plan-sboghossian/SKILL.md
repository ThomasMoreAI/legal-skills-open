---
name: prompt-pack-workplace-investigation-plan-sboghossian
title: Workplace Investigation Plan
description: Use when an HR, legal, or compliance team needs to design a structured investigation plan for a workplace complaint — harassment, discrimination, misconduct, fraud, or policy violation. Covers investigation scope, witness identification, interview framework, evidence preservation, confidentiality controls, timeline, and reporting chain. Applicable across MENA and international jurisdictions; especially important where labor law mandates procedural fairness in disciplinary proceedings.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-workplace-investigation-plan
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Workplace Investigation Plan

## When to use this

Use this skill at the outset of a workplace investigation — before any interviews are conducted — to produce a structured plan that will guide the investigation from initiation to report. A written investigation plan serves three functions: (1) it ensures the investigation is thorough and procedurally fair; (2) it documents that the company followed a reasonable process (important if the matter later becomes litigation or regulatory); (3) it allocates responsibility between HR, legal, and management.

Typical triggers:
- An employee files a formal complaint of harassment, discrimination, bullying, or sexual misconduct
- A whistleblower report through the speak-up hotline alleges fraud, corruption, or serious policy violation
- Management discovers evidence of suspected theft, data breach, or abuse of authority
- A customer or supplier alleges misconduct by a company employee
- A regulatory body inquires about a specific incident involving company personnel

**Important:** The investigation plan must be completed and approved before the first witness interview. Starting interviews before agreeing on scope and methodology risks bias challenges and evidence contamination.

## Required inputs

| Input | Why it matters | Sensible default |
|-------|---------------|-----------------|
| Nature of the complaint / allegation | Determines scope, investigator qualifications, and applicable policies | Prompt user — provide the complaint text or a summary |
| Identity of complainant (or anonymous channel reference) | Shapes confidentiality obligations and right-to-reply procedures | Prompt user |
| Identity of respondent(s) (the alleged wrongdoer) | Determines conflict checks for investigator; shapes interim measures | Prompt user |
| Jurisdiction / country of employment | Determines procedural requirements and applicable labor law | Prompt user |
| Company policies engaged | The investigation must assess conduct against specific policies | Prompt user (Code of Conduct, Harassment Policy, Whistleblower Policy, etc.) |
| Seniority / organizational relationship | Affects who can lead the investigation and whether external investigators are required | Prompt user |

## Optional inputs

- **Prior complaints or incidents** involving the same individuals (informs scope and pattern analysis)
- **Interim measures already taken** (suspension, separation) — affects witness access
- **Legal hold requirements** — if the matter has litigation potential, a legal hold must be issued before the plan is finalized
- **Regulatory notification obligations** — some sectors require reporting an investigation to regulators (DFSA, FSRA, SCA) even before conclusions are reached
- **Union or employee representative involvement** — if applicable in the jurisdiction
- **Cross-border dimension** — if the conduct spans multiple countries, document which law applies

## Investigation plan structure

The plan should be a written internal document, typically 3–8 pages, signed off by the investigation lead and relevant oversight (General Counsel, CHRO, or Audit Committee depending on seniority of the respondent).

---

### 1. Investigation reference and classification

| Field | Content |
|---|---|
| Case reference | Internal reference number (e.g., INV-2026-001) |
| Date opened | |
| Nature of complaint | [Harassment / Misconduct / Fraud / Other] |
| Complainant | Name / Anonymous (hotline ref: [X]) |
| Respondent | Name and title |
| Jurisdiction | Country of employment |
| Policies potentially breached | List |
| Severity classification | [Tier 1: Minor / Tier 2: Serious / Tier 3: Critical] |
| Investigator(s) | Name, title, and independence declaration |

---

### 2. Scope of investigation

Define:
- **What is being investigated:** the specific allegations (quote the complaint or summarize with precision); do not investigate broader matters not covered by the complaint unless new facts emerge
- **What is not in scope:** related grievances or historical matters that are not part of this complaint (prevents scope creep)
- **Applicable time period:** the date range of the alleged conduct
- **Standard of proof:** balance of probabilities (on the evidence, is it more likely than not that the alleged conduct occurred?) — this is the standard in employment investigations across most jurisdictions, not the criminal "beyond reasonable doubt" standard

### 3. Investigator and conflict check

- Identify the lead investigator and any assisting investigator
- Document why the investigator is independent of both complainant and respondent
- If the respondent is a senior executive, consider whether an external independent investigator (law firm, forensic HR specialist) should be appointed to avoid actual or perceived bias
- Document that the investigator has completed relevant training (ACAS, CIPDH, or equivalent; HR investigation certification)

### 4. Interim measures

Before the investigation begins, consider whether interim measures are required:
- **Suspension with pay:** appropriate if the respondent's continued presence could intimidate witnesses or interfere with evidence; must be framed as a neutral administrative step, not a disciplinary measure (this is critical in UAE, KSA, and Lebanon where premature disciplinary characterization affects procedural fairness rights)
- **Physical separation:** if suspension is disproportionate, separate workspaces or remote work
- **System access restriction:** particularly in fraud or data-related matters
- **Communication restrictions:** no contact between respondent and complainant or key witnesses during the investigation

*Jurisdiction note:* In UAE (Federal Decree-Law 33/2021 on Labour), suspension with pay during investigation is permissible; indefinite suspension without due process risks a wrongful dismissal claim. KSA Labour Law (Royal Decree M/51/2005) — suspension permitted for investigation purposes. DIFC / ADGM — DIFC Employment Law 2019: employer has broad authority to suspend pending investigation; DIFC Court will scrutinize whether the investigation was genuinely independent.

### 5. Witness list

| Witness | Role | Relationship to complaint | Priority | Interview method |
|---|---|---|---|---|
| Complainant | First-hand account | Complainant | High | In-person / video |
| Respondent | Right to respond | Respondent | High | In-person / video |
| [Witness 1] | Observer / corroborating | Neutral | Medium | Written questions or video |
| [Witness 2] | Character / conduct history | Neutral | Low | Written questions |

- List all potential witnesses; rank by relevance
- Include any witnesses the respondent identifies as relevant (fairness obligation — respondent must have an opportunity to provide their account and suggest witnesses)
- Document why any potential witness has been excluded from the list

### 6. Interview questions framework

**Complainant interview questions (adapt to allegations):**
- Describe the incident(s) in your own words. When and where did each incident occur?
- Who was present at the time?
- How did the conduct affect you?
- Have you previously reported this conduct? To whom, and what was the response?
- Are there any witnesses who can corroborate your account?
- Are there any relevant documents, messages, or emails you can provide?
- Is there anything else you believe is relevant to this investigation?

**Respondent interview questions (adapt to allegations):**
- You have been provided with a summary of the allegations. [Read / give summary.] What is your response?
- Please describe your recollection of [the specific incident(s)].
- Were there any witnesses present?
- Do you have any documents, messages, or emails that support your account?
- Is there any reason why the complainant would make a false complaint against you?
- Are there any other people you think the investigator should speak to?

**Witness interview questions (general):**
- What is your professional relationship to [complainant] / [respondent]?
- Did you witness any of the following events? [List specific events.]
- What did you observe? Describe in your own words.
- Did you discuss this with any colleagues?
- Have you previously been asked to comment on this matter?

### 7. Evidence preservation

Before interviewing any witnesses:
- Issue a legal hold notice to IT, HR, and relevant managers: preserve all emails, messages (WhatsApp, Teams, Signal), call logs, access logs, CCTV footage, and physical documents relating to the complainant, respondent, and the period under investigation
- Instruct IT to suspend any automatic deletion policies for the covered accounts / time period
- Collect and secure physical documents (if applicable)
- Document the chain of custody for any evidence collected

### 8. Confidentiality protocol

- All parties to the investigation (complainant, respondent, witnesses, investigators) must be instructed to maintain confidentiality
- Disclosure limited to those with a need to know
- No discussion of the investigation on internal messaging platforms or by email (use encrypted channel or in-person)
- Document all persons who received information about the investigation
- Address the risk of counter-claims: if the respondent discloses the complaint to colleagues in retaliation, this itself may constitute a policy violation

### 9. Timeline

| Milestone | Target date |
|---|---|
| Plan approved | [Date + 2 business days after complaint received] |
| Legal hold issued | [Same day as plan approval] |
| Interim measures implemented | [Within 1 business day of plan approval] |
| Complainant interview | [Within 5 business days of plan approval] |
| Witnesses interviewed | [Within 10 business days of plan approval] |
| Respondent interview | [After all other interviews completed; within 15 business days] |
| Preliminary findings review | [Within 5 business days of last interview] |
| Final report drafted | [Within 10 business days of preliminary findings] |
| Findings communicated to parties | [Within 5 business days of report approval] |

*Note:* UAE and DIFC labor law do not specify investigation timelines, but unreasonable delay (> 3 months without explanation) can expose the employer to a procedural unfairness claim. EU Whistleblower Directive requires feedback to the reporter within 3 months.

### 10. Reporting chain and escalation

- **Day-to-day oversight:** [HR Director / General Counsel]
- **Escalation for conflicts of interest or senior executives:** [CEO / Audit Committee Chair]
- **Legal privilege:** [Name of outside counsel] advising on the investigation; communications should be clearly marked as protected by legal professional privilege
- **Board notification threshold:** if the allegation implicates a C-suite executive, board or audit committee must be notified before interviews commence

## Jurisdictional notes

| Jurisdiction | Key consideration |
|---|---|
| UAE (Federal) | Labour Law FDL 33/2021; disciplinary procedure must be documented; employee must be given opportunity to respond before dismissal; Arabic language for formal notices |
| DIFC | DIFC Employment Law 2019; procedural fairness required; DIFC Court will scrutinize investigation quality in unfair dismissal claims |
| ADGM | ADGM Employment Regulations 2019 — similar to DIFC |
| KSA | Saudi Labour Law (Royal Decree M/51/2005); investigation and disciplinary committee required for terminations; formal notice requirements; Arabic required |
| Lebanon | Code of Obligations and Contracts; Labour Law; procedural fairness in employment dismissal; no specific investigation procedure mandated |
| Egypt | Egyptian Labour Law 12/2003; investigation required before dismissal for gross misconduct; company must notify Ministry of Manpower in certain cases |
| EU | National transpositions of Whistleblower Directive; national employment law varies; employee representatives (works councils) may have consultation rights |
| UK | ACAS Code of Practice on Disciplinary and Grievance Procedures; Employment Tribunals apply ACAS Code in assessing fairness; minimum standards: written notice, investigation, right to be accompanied at hearing |

## Related skills

- [[prompt-pack-workplace-investigation-report]]
- [[prompt-pack-whistleblower-policy]]
- [[prompt-pack-employment-termination-letter]]
- [[kb-employment-mena]]
- [[heuristic-always-state-jurisdiction-first]]
