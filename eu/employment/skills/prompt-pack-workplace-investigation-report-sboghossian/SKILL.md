---
name: prompt-pack-workplace-investigation-report-sboghossian
title: Workplace Investigation Report
description: Use when an HR, legal, or compliance investigator needs to draft the formal report documenting the outcome of a workplace investigation — including the allegation summary, investigation methodology, witness interviews, evidence reviewed, factual findings, credibility assessments, policy violations identified, and recommendations for disciplinary action or remediation. The report is the primary evidentiary document if the matter becomes litigation or regulatory.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-workplace-investigation-report
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: employment
language: en
---

# Workplace Investigation Report

## When to use this

Use this skill after a workplace investigation has concluded and the investigator needs to produce the formal written report. The investigation plan ([[prompt-pack-workplace-investigation-plan]]) should have been followed before drafting the report.

The investigation report is a critical document for three reasons:
1. **Disciplinary proceedings:** It forms the factual basis for any disciplinary action against the respondent; without a robust report, disciplinary action is vulnerable to procedural challenge
2. **Litigation defense:** If the complainant or respondent later brings a labor claim, the report is the company's primary documentary evidence that the investigation was thorough, impartial, and procedurally fair
3. **Regulatory compliance:** In regulated industries (financial services, healthcare), the investigation report may be required as part of regulatory disclosure

**Audience:** The report is typically addressed to the General Counsel, CHRO, or Audit Committee — not circulated broadly. Consider legal privilege implications (see §Privilege note below).

## Inputs

| Input | Why it matters |
|---|---|
| Investigation plan and case reference | Connects report to the authorized scope |
| Interview notes / transcripts | Source for witness summaries and credibility assessments |
| Evidence collected (emails, messages, CCTV, documents) | Source for evidence section |
| Company policies engaged | Standard against which conduct is measured |
| Legal advice received (if privileged) | Shapes findings framing and redaction decisions |
| Jurisdiction(s) | Determines applicable law for policy violations and disciplinary consequences |

## Document structure

---

### Cover page

```
STRICTLY CONFIDENTIAL — LEGAL PRIVILEGE APPLIES
[COMPANY NAME]
WORKPLACE INVESTIGATION REPORT
Case Reference: [INV-XXXX-XXX]
Subject: Investigation into allegations of [nature of complaint]
Investigator: [Name, Title]
Date: [Date of report]
Prepared for: [General Counsel / CHRO / Audit Committee]
Distribution: RESTRICTED
```

---

### 1. Executive summary (1–2 pages)

- One-paragraph summary of allegations
- One-paragraph summary of investigation methodology
- Key findings (bulleted: finding and whether substantiated / unsubstantiated / partially substantiated)
- Recommendation summary (disciplinary action; remediation; policy change; no action)

---

### 2. Allegations and scope

State the allegations in neutral, precise terms — not using the complainant's emotive language, and not pre-judging:

> "The investigation was opened in response to a complaint dated [Date] by [Complainant Name / Anonymous Hotline Ref], alleging that [Respondent Name], [Title], [nature of conduct: e.g., 'subjected the complainant to repeated unwanted physical contact and verbal abuse on at least three occasions between [Date] and [Date]']."

List each discrete allegation separately (Allegation 1, Allegation 2, etc.) as this maps to findings.

State scope limitations: "The investigation was limited to the allegations set out above for the period [start date] to [end date]. This report does not address [any excluded matters]."

---

### 3. Investigation methodology

State clearly:
- Date investigation opened and by whose authorization
- Investigators' names, titles, and independence statement ("The investigators have no prior relationship with either the complainant or respondent and have no conflict of interest")
- Investigation steps taken:
  - Documents reviewed (list categories: emails, chat logs, CCTV, HR files, etc.)
  - Witnesses interviewed (list names / roles / dates of interview, without disclosing witness statements in this section)
  - Legal hold issued on [date]
  - Any interim measures taken

*Do not describe the substance of interviews here — that belongs in §5.*

---

### 4. Evidence reviewed

Organize the evidence by type, not by allegation:

**Documentary evidence:**
| Exhibit | Description | Date | Source | Relevance |
|---|---|---|---|---|
| INV-E001 | Email from [Respondent] to [Complainant] | [Date] | IT extraction | Allegation 1 |
| INV-E002 | WhatsApp message thread (20 messages) | [Date range] | Complainant's device | Allegations 1 and 2 |
| INV-E003 | CCTV footage [Room/Floor] [Timestamp] | [Date] | Security team | Allegation 2 |

**Digital / forensic evidence:**
- Describe any forensic review (email metadata, access logs, device image)
- Note any evidence that was unavailable and why (deleted messages; device not retained)

---

### 5. Witness summaries

For each witness (use a separate numbered sub-section per witness):

**5.1 [Complainant Name], [Title]**
- Date, time, and method of interview
- Summary of evidence given — direct, factual, non-emotive; what the witness said, not the investigator's interpretation
- Documents referenced during interview

**5.2 [Respondent Name], [Title]**
- Date, time, and method of interview
- Summary of response to each allegation
- Any supporting evidence offered by the respondent
- Note if respondent declined to answer any questions

**5.3 [Witness Name], [Title]**
- Date, time, and method of interview
- Summary of relevant evidence
- Note if witness had limited direct knowledge

*Do not include full verbatim transcripts in the body of the report — attach as appendices if required.*

---

### 6. Credibility assessments

This is often the most challenging and consequential section. For each key witness:

- **Consistency:** Was the account internally consistent? Did it change between a prior informal account and the formal interview?
- **Corroboration:** Is the account corroborated by documentary evidence, other witnesses, or contemporaneous records?
- **Demeanour:** (exercise caution — demeanor is a poor reliability indicator and courts / tribunals treat it skeptically) Note only if extreme and relevant
- **Motive to fabricate:** Is there any credible motive for the witness to give a false account? (Avoid speculating; only note if evidence-based)
- **Specific vs. general:** Specific accounts that include identifying details (dates, locations, exact words) are generally more reliable than vague general allegations

> Example: "Having reviewed the evidence, the investigator found [Complainant]'s account to be credible. The account was consistent across the initial complaint and the formal interview. It is supported by [Exhibit INV-E002] and corroborated in material respects by [Witness Name]. [Respondent]'s account, by contrast, is contradicted by [Exhibit INV-E001] which was sent on [date], a date on which [Respondent] claimed to have had no contact with [Complainant]."

---

### 7. Findings

Address each allegation separately:

**Allegation 1:** [State the allegation precisely]

*Finding:* **Substantiated** / **Partially substantiated** / **Unsubstantiated**

*Basis for finding:* [Concise narrative explaining what evidence supports or does not support the finding; reference exhibits; do not repeat the full evidence summary]

**Allegation 2:** ...

---

### 8. Policy violations identified

For each substantiated or partially substantiated finding, state which company policy (or applicable law) was violated:

> "The conduct described in Allegation 1 constitutes a violation of [Company]'s [Harassment and Bullying Policy] §[3.2], which prohibits [quote the relevant policy provision]. The conduct may also constitute [harassment / a hostile work environment] under [applicable law: DIFC Employment Law 2019 Art. [X] / UAE Labour Law FDL 33/2021 Art. [X] / etc.]."

---

### 9. Recommendations

State recommendations proportionate to the findings:

- **Disciplinary action:** If substantiated, recommend disciplinary proceedings; state the range of potential sanctions (warning, suspension, demotion, termination); note that the disciplinary committee or the decision-maker must make the final disciplinary decision — the investigator's role is to make findings of fact, not to impose sanction
- **Remediation:** Training, mediation, separation of parties, management intervention
- **Policy or process improvements:** If the investigation revealed a systemic issue (e.g., inadequate reporting channels, manager behavior pattern), recommend policy review
- **No action:** If allegations are unsubstantiated, recommend closure of the investigation; address whether a counter-complaint is warranted if the complaint was clearly made in bad faith

---

### 10. Privilege and confidentiality

State:
- Report prepared at the direction of [General Counsel / outside counsel] in anticipation of potential litigation / regulatory proceedings
- Report is protected by legal professional privilege (where applicable — legal advice privilege / litigation privilege depending on jurisdiction)
- Distribution restricted to: [list]
- Recipients must treat the report as strictly confidential

*Privilege note:* In DIFC, ADGM, UK, and US, legal advice privilege attaches to communications between lawyers and clients made for the dominant purpose of obtaining legal advice. Investigation reports prepared at the direction of counsel in anticipation of litigation may attract litigation privilege. In UAE onshore, LB, and EG civil proceedings, privilege principles are less developed; engage local counsel on privilege strategy before distributing.

---

### Appendices

- Appendix A: Interview transcripts or notes (if required)
- Appendix B: Key exhibits (key documents; full exhibit list may be in a separate evidence bundle)
- Appendix C: Investigation timeline
- Appendix D: Relevant policy extracts

---

## Jurisdictional notes

| Jurisdiction | Key procedural fairness requirement | Timing |
|---|---|---|
| UAE (Federal) | Employee must be notified of allegations in writing and given opportunity to respond before dismissal; investigation report supports this obligation | Investigation and disciplinary process should be completed within 2–3 months to avoid prejudice claims |
| DIFC | DIFC Employment Law 2019: employer must have genuine reasonable grounds for disciplinary action; DIFC Court scrutinizes procedural fairness | No statutory timeline; DIFC Court considers reasonableness |
| ADGM | Similar to DIFC | Similar |
| KSA | Labour Law requires disciplinary committee; formal disciplinary procedure; investigation report supports committee process | Investigation should be completed before disciplinary committee convened |
| Lebanon | Labour Law and Code of Obligations; procedural fairness in dismissal required | No statutory investigation timeline |
| Egypt | Labour Law 12/2003 Art. 69: employer must investigate before terminating for gross misconduct; investigation record required | Statutory requirement |
| EU | Varies by member state; investigation report may be required by works council; data protection obligations on processing investigation data | EU Whistleblower Directive: feedback to reporter within 3 months |
| UK | ACAS Code of Practice: full investigation before disciplinary hearing; written findings shared with the employee before the hearing; right to be accompanied | Unreasonable delay treated as procedural unfairness by Employment Tribunal |

## Drafting standards

- **Neutral language throughout** — the report must be defensible as impartial; avoid language that suggests the investigator had a pre-determined view; describe conduct, not character
- **Findings of fact, not law** — the investigator finds facts; legal characterization (was this unlawful harassment under applicable law?) is for legal counsel; include only where expressly authorized
- **Balance of probabilities standard** — findings should be expressed in terms of whether the alleged conduct "more likely than not occurred" — not "proven beyond reasonable doubt"
- **No names in recommendations section** — recommendations should be generic ("disciplinary proceedings should be considered") not "X should be dismissed" — that decision belongs to the disciplinary decision-maker
- **Version control** — use version numbers; drafts should be watermarked "DRAFT — PRIVILEGED AND CONFIDENTIAL"; final report should be clearly marked as final

## Common mistakes

- **Findings exceed the scope** — investigating matters not covered by the original complaint, creating new exposure
- **No credibility assessment** — a report that simply lists what each person said without assessing whose account is more credible leaves the decision-maker without guidance
- **Recommending specific disciplinary outcomes** — the investigator's role is fact-finding; recommending termination conflates two distinct functions and may expose the company to bias claims
- **Failing to give the respondent the opportunity to respond to adverse findings** — most jurisdictions require the respondent to see the allegations and respond before a final finding is made
- **No privilege marking** — investigation reports without privilege marking are more easily disclosed in subsequent litigation
- **Report circulated too widely** — every additional recipient is a potential data protection risk and weakens privilege arguments

## Related skills

- [[prompt-pack-workplace-investigation-plan]]
- [[prompt-pack-whistleblower-policy]]
- [[prompt-pack-employment-termination-letter]]
- [[kb-employment-mena]]
- [[heuristic-always-state-jurisdiction-first]]
