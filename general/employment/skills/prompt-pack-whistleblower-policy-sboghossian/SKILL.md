---
name: prompt-pack-whistleblower-policy-sboghossian
title: Whistleblower Policy
description: Use when a company needs to draft or update an internal whistleblower (speak-up) policy covering reporting channels for suspected wrongdoing, types of reportable concerns, investigation procedures, anti-retaliation protections, and confidentiality guarantees. Relevant for corporate governance compliance across MENA and international jurisdictions, especially for publicly listed companies, financial institutions, and multinationals with EU or US operations where mandatory whistleblower frameworks apply.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-whistleblower-policy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Whistleblower Policy

## When to use this

Use this skill when:

- A company is establishing or revising a whistleblower / "speak-up" policy as part of its corporate governance framework
- An entity must comply with mandatory whistleblower reporting requirements (EU Whistleblower Directive, US Sarbanes-Oxley, Dodd-Frank, UK PIDA, DIFC / ADGM governance standards)
- A board or audit committee requires a policy documenting the anonymous reporting channel and anti-retaliation protections
- An M&A legal team identifies that the target lacks a compliant whistleblower policy during due diligence
- A company is responding to a regulatory inquiry about its internal controls and needs to demonstrate an operative speak-up system

The policy must be genuinely operational — not boilerplate. A policy that exists on paper but is not trained, communicated, or enforced provides minimal legal protection and may itself become evidence in a regulatory proceeding.

## Required inputs

| Input | Why it matters | Sensible default |
|-------|---------------|-----------------|
| Company name and sector | Shapes which concerns are reportable and which regulatory frameworks apply | Prompt user |
| Jurisdictions of operation | Determines mandatory requirements and anti-retaliation scope | All jurisdictions where company employs or contracts workers |
| Reporting channel options | Internal (HR, legal, hotline, ombudsman) vs. external; anonymous vs. identified | Include at least one anonymous channel; external option recommended |
| Applicable whistleblower laws | Mandatory framework reference | Per jurisdiction (see notes below) |
| Scope of covered persons | Employees only, or also contractors, suppliers, former employees | Broad coverage recommended; EU Directive requires contractors |

## Optional inputs

- **Third-party hotline provider** — many companies use external anonymous hotline (e.g., EthicsPoint, NAVEX, SpeakUp); specify in the policy
- **Audit committee / board oversight role** — whether the audit committee receives all reports or only those involving senior management
- **Existing internal investigation procedure** — policy should cross-reference the investigation procedure
- **Multilingual requirements** — policy must be accessible in all languages of the company's workforce
- **Confidentiality procedure for legal hold** — hotline records may be subject to legal hold; address in data retention section

## Document structure

1. **Purpose and commitment** — company's commitment to ethical conduct and open reporting; purpose of the policy (create a safe reporting environment; detect and remediate wrongdoing; comply with applicable law)

2. **Scope — who is covered** — all employees (permanent, temporary, part-time); contractors, consultants, and agents; former employees (for matters they reported during employment); members of the company's board; third-party suppliers and joint venture partners (if applicable); specific inclusion of workers in all jurisdictions

3. **What can be reported (reportable concerns)** — non-exhaustive list:
   - Fraud, corruption, bribery, kickbacks
   - Financial irregularities, accounting fraud, securities fraud
   - Health and safety violations
   - Environmental breaches
   - Data protection and privacy violations
   - Harassment, discrimination, or bullying
   - Conflicts of interest not disclosed
   - Violations of company policy or applicable law
   - Retaliation against a prior reporter
   - Government contract or procurement violations
   - Sanctions and export control violations (for MENA entities operating internationally)

4. **How to report — reporting channels**
   - **Internal channels:** direct manager (if not implicated), HR, legal department, compliance officer
   - **Anonymous hotline:** 24/7 third-party operated; caller ID not recorded; accessible in [relevant languages]
   - **Board / audit committee channel:** for concerns involving senior management, CFO, or CEO
   - **External reporting:** company encourages internal reporting first but acknowledges employees' legal right to report to external regulators (DFSA, SCA, FCA, SEC, relevant labor authority, etc.) — anti-retaliation protections apply regardless of which channel is used
   - Specify contact details for each channel

5. **Confidentiality** — reporter's identity protected to the maximum extent possible consistent with conducting a fair investigation; when disclosure is unavoidable (e.g., criminal proceedings), reporter is informed in advance; information about the report shared only on a need-to-know basis; records stored securely; data protection law compliance

6. **Anti-retaliation protections** — company strictly prohibits retaliation against any person who reports in good faith; prohibited retaliation includes: dismissal, demotion, salary reduction, harassment, threats, blacklisting, negative performance reviews, refusal of promotion; definition of "good faith" (reporter genuinely believed concern was valid; knowingly false reports are not protected); remedies for retaliated-against reporters (reinstatement, compensation, legal action); managers personally liable for authorized retaliation

7. **Investigation procedure** — reference to separate [[prompt-pack-workplace-investigation-plan]]; key commitments in this policy: initial triage within [5 business days]; acknowledgment to reporter (where not anonymous); investigation by qualified, impartial investigator; conclusion within [60–90 days] unless extension documented; feedback to reporter on outcome (in general terms, preserving third-party confidentiality)

8. **Disclosure and false reports** — reporter duty to report accurately to the best of their knowledge; deliberately false or malicious reports may constitute misconduct subject to disciplinary action; this provision must be narrowly drafted to not chill legitimate reporting

9. **Record-keeping and data protection** — hotline records retained for [5–7 years] or as required by local law; access restricted to investigation team; records subject to company data protection policy; data subject rights of the reported individual are addressed in the investigation procedure

10. **Governance** — policy owned by [General Counsel / Chief Compliance Officer]; annual review cycle; board / audit committee receives annual summary of reports, outcomes, and trends (anonymized); amendment process; version control

11. **Communication and training** — policy distributed to all covered persons; new-hire training required; annual refresher; managers trained on anti-retaliation obligations; accessible on company intranet in all relevant languages

12. **Governing law** — policy is governed by applicable law in each jurisdiction of operation; where there is conflict between this policy and local law, the more protective standard applies

## Jurisdictional notes

| Jurisdiction | Key instrument | Notable requirement |
|---|---|---|
| EU | Directive (EU) 2019/1937 (Whistleblower Protection Directive), transposed by 2021 | Mandatory for companies with 50+ employees; 3-month report feedback deadline; anonymous reporting channel required; broad personal scope (contractors, shareholders); ban on retaliation including in civil proceedings |
| UK | Public Interest Disclosure Act 1998 (PIDA) + Employment Rights Act | "Protected disclosure" if worker reasonably believes information is true and in the public interest; employment tribunal remedy; no separate mandatory hotline requirement (but good practice) |
| DIFC | DIFC Employment Law 2019 Art. 62 — protected disclosures; DFSA conduct rules for regulated firms | DFSA requires regulated entities to have effective whistleblower arrangements; DIFC Court will enforce anti-retaliation claims |
| ADGM | ADGM Employment Regulations 2019; FSRA conduct requirements for regulated entities | Similar to DIFC; FSRA requires robust speak-up culture |
| UAE (onshore) | No comprehensive whistleblower law; Labour Law (Federal Decree-Law 33/2021) protects against unfair dismissal; sector-specific rules (Central Bank, SCA) | Policy operates primarily as contractual commitment; Central Bank Circular requiring banks to have compliance reporting channels |
| KSA | No standalone whistleblower law; SAMA (Saudi Central Bank) requires financial institutions to have complaint and reporting mechanisms; Combating Corruption Commission (Nazaha) public reporting channel | Policy should align with SAMA reporting requirements for financial sector; Arabic version required for employee-facing documents |
| Lebanon | Code of Obligations and Contracts applies; Labor Law protects against arbitrary dismissal; no standalone whistleblower statute | Policy provides contractual protection; courts apply general employment and tort principles |
| Egypt | No comprehensive whistleblower law; Egyptian Labor Law; CBE circulars for banking sector | CBE requires banks to have internal reporting mechanisms; general anti-retaliation based on Labor Law Art. 69 |
| US | Sarbanes-Oxley Act (public companies); Dodd-Frank Act (securities violations — SEC bounty program); FCPA enforcement context | SOX requires audit committee reporting channel; Dodd-Frank provides financial rewards for tips leading to SEC enforcement; policies must not obstruct protected disclosures |

**MENA cultural note:** In Gulf cultures, a "speak-up" culture may be less developed than in Western organizations. The policy should be supplemented with training that emphasizes the company's genuine commitment to non-retaliation and that addresses the cultural stigma around "reporting on colleagues." Manager training is particularly important.

**Language requirement:** In UAE and KSA, employee-facing policies should be in Arabic (or bilingual with Arabic). A policy only in English that employees cannot read provides minimal protection in labor proceedings.

## Drafting standards

- **Anti-retaliation clause must have teeth** — specify concrete remedies (reinstatement, compensation), not just a vague policy statement
- **Anonymous channel is not optional** — employees will not report if they fear identification; even where confidentiality cannot be guaranteed (e.g., small team), state the commitment clearly
- **Do not conflate with grievance procedure** — whistleblower reports concern wrongdoing by others; personal grievances are handled separately; confusing the two dilutes both
- **Feedback obligation** — the EU Directive requires feedback within 3 months; even outside EU, committing to feedback (in general terms) increases trust in the system
- **False reporting carve-out must be narrow** — broad language threatening discipline for "unsubstantiated" reports will chill legitimate disclosures

## Common mistakes

- **Policy exists but is not communicated** — a policy that employees don't know about offers no protection
- **No anonymous channel** — anonymous channels are the standard for effective reporting; identified-only systems generate under-reporting
- **Anti-retaliation clause too vague** — "the company does not retaliate" without specifics is unenforceable
- **No feedback mechanism** — reporters who hear nothing assume their report was ignored; required by EU Directive and best practice elsewhere
- **Conflating with HR grievance procedure** — whistleblower reports should go to compliance / legal, not HR, to avoid conflicts of interest
- **Single language** — non-English-speaking employees may not understand or use an English-only policy

## Related skills

- [[prompt-pack-workplace-investigation-plan]]
- [[prompt-pack-workplace-investigation-report]]
- [[prompt-pack-anti-bribery-compliance-policy]]
- [[kb-corporate-governance-mena]]
- [[heuristic-always-state-jurisdiction-first]]
