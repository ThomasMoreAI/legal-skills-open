---
name: prompt-pack-code-of-conduct-sboghossian
title: Code of Conduct
description: Use when a company needs to draft or update a Code of Conduct (or Business Ethics Policy) covering ethical principles, conflicts of interest, gifts and entertainment, anti-bribery and corruption, confidentiality, fair dealing, compliance with laws, and reporting and enforcement mechanisms. Relevant across MENA (UAE, KSA, LB, EG), DIFC/ADGM, and internationally; must address both local anti-corruption law and applicable extraterritorial regimes (UK Bribery Act, US FCPA) for companies with international exposure.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-code-of-conduct
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Code of Conduct

A Code of Conduct is one of the most visible governance documents a company produces — it signals values to employees, regulators, and counterparties. It must be aspirational enough to set a cultural standard and specific enough to guide decisions in the gray areas where employees face real choices.

## When to use this

- A company is incorporating or scaling and needs a foundational governance document.
- An existing Code needs to be updated following a regulatory change, a compliance incident, or an international listing requirement.
- A MENA company operating internationally needs to address extraterritorial anti-corruption laws (UK Bribery Act 2010, US FCPA) alongside local law.
- An investor or counterparty due diligence process has identified the absence of a Code as a red flag.
- The company is seeking a listing on a regulated exchange (DFM, ADX, Tadawul, LSE, NYSE) with mandatory governance disclosure requirements.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Company name and jurisdiction(s) of operation | Determines applicable law and cultural calibration | Ask the user |
| Company size and sector | A financial institution or government contractor needs more specificity than a small tech firm | Ask the user |
| Applicable anti-corruption regimes | UK Bribery Act applies to UK-nexus companies; US FCPA applies to any company with US listing or operations | Ask the user; include both if in doubt |
| Whether the company interacts with government officials | Determines depth of public official / procurement section | Ask the user |
| Whether a whistleblowing / speak-up channel already exists | Allows cross-reference to existing mechanism | Ask the user |

## Optional inputs

- Existing policies the Code should cross-reference (Anti-Bribery Policy, Gifts & Entertainment Policy, Conflict of Interest Policy).
- Whether the Code applies to third parties (suppliers, agents, JV partners) — increasingly required under supply-chain due diligence frameworks.
- Languages in which the Code will be published (Arabic version required for UAE/KSA onshore enforcement).
- Acknowledgment and training requirements.

## Document structure

### 1. Introduction and CEO / Leadership message
A personal statement from the CEO or Chair establishing tone from the top. Not just a formality — regulators and juries have treated the presence or absence of a credible leadership message as evidence of culture.

### 2. Scope and applicability
- Applies to all employees, directors, officers, and (if stated) agents, contractors, and JV partners.
- State governing law for interpretation disputes.
- Note that the Code supplements, and does not replace, applicable law.

### 3. Our values and ethical principles
- Integrity, transparency, accountability, respect, and fairness (or the company's stated values).
- State that the company competes on merit, not connections.

### 4. Conflicts of interest
- Definition: a situation where personal interests conflict with the company's interests.
- Disclosure obligation: all potential conflicts must be disclosed to the line manager and/or compliance function immediately.
- Common examples: outside employment, investments in competitors or suppliers, personal relationships with counterparties, family members in relevant roles.
- Process: written disclosure → review by compliance / legal → management approval or recusal.
- Board members: address separately if applicable (often governed by the Articles / MoA and applicable companies law).

### 5. Gifts, hospitality, and entertainment
- Policy: gifts and hospitality may only be given or received if they are modest in value, not in cash, not given to or from a public official without compliance pre-approval, and would not embarrass the company if disclosed publicly.
- Thresholds: set a monetary cap (e.g., USD 100 / AED 400 per occasion; USD 250 / AED 1,000 per year per counterparty) — below the de minimis under UK Bribery Act guidance.
- Prohibition: no gifts to or from government officials without prior written approval, even if permitted by local custom.
- Log: maintain a gifts and hospitality register.

### 6. Anti-bribery and anti-corruption
This is the highest-stakes section. Key elements:
- Absolute prohibition on bribing any person, public official or private, directly or through an intermediary.
- Prohibition on "facilitation payments" (UK Bribery Act and US FCPA do not recognise a facilitation payment exception for most scenarios; local MENA laws are not uniform on this).
- Due diligence on agents, intermediaries, and JV partners who interact with government.
- Prohibition on making political contributions on behalf of the company without board approval.
- Prohibition on charitable donations that are, in substance, bribes.

**MENA legal framework note:**
- **UAE:** Federal Decree-Law No. 31 of 2021 (Penal Code) prohibits bribery of public officials; the Anti-Money Laundering Law (Federal Decree-Law No. 20 of 2018) covers corruption proceeds.
- **KSA:** Anti-Bribery Law (Royal Decree M/36, 2017); applies to public and private sector; Nazaha (Oversight and Anti-Corruption Authority) is the enforcement body.
- **Lebanon:** Penal Code Articles 351–366 cover bribery; Law No. 175 of 2020 established the National Anti-Corruption Commission (NACC).
- **Egypt:** Penal Code and Law No. 58 of 1937; Administrative Prosecution Authority and Central Auditing Organization have investigative roles.
- **UK Bribery Act 2010:** Applies to any company carrying on a business in the UK; corporate offence of failure to prevent bribery has no intent requirement — the defence requires adequate procedures.
- **US FCPA:** Applies to issuers listed on US exchanges, US companies, and any person acting in the US territory; anti-bribery and accounting provisions.

### 7. Confidentiality and information security
- Obligation to protect confidential information of the company and of third parties.
- Prohibition on insider trading using material non-public information (especially relevant for listed companies or companies with listed group members).
- Data privacy obligations (UAE PDPL, DIFC/ADGM data protection law, GDPR if applicable).
- Social media and public communications policy cross-reference.

### 8. Fair dealing and competition
- Compete on merit; do not engage in anti-competitive practices (price-fixing, market allocation, bid rigging).
- Do not obtain competitive intelligence through improper means.
- Treat all suppliers, customers, and counterparties honestly and fairly.
- GCC competition law note: UAE Federal Competition Law (Federal Decree-Law No. 36 of 2023); KSA Competition Law (Royal Decree No. M/75, 2019).

### 9. Compliance with laws and regulations
- Comply with all applicable laws in every jurisdiction in which the company operates.
- Employees in regulated sectors (financial services, healthcare, telecoms) must comply with sector-specific regulatory requirements.
- Report actual or suspected violations of law to the compliance function.

### 10. Reporting violations and whistleblower protections
- Obligation to report known or suspected violations via the company's speak-up channel.
- Multiple reporting channels: compliance function, legal, anonymous hotline, escalation to the Audit Committee.
- Non-retaliation commitment: any retaliation against a good-faith reporter is itself a serious violation.
- **MENA note:** Whistleblower protections in MENA are less developed than in the UK or EU; the Code should commit to protection regardless of whether local law requires it. UAE does not have a general whistleblower protection law as of 2026; DIFC has limited employment protections.

### 11. Consequences for violations
- Violations may result in disciplinary action up to and including termination and referral to law enforcement.
- Personal liability: employees are personally liable for their own misconduct; the company does not indemnify employees for criminal conduct.

### 12. Training, acknowledgment, and certification
- Annual training on the Code.
- Annual written certification by all employees.
- Third-party certifications (agents, major suppliers) as required by the risk-based anti-bribery program.

## Drafting standards

- Written in plain language; avoid dense legal text in the body (put detailed legal analysis in a separate policy or FAQ annex).
- Use real examples in the gray-area sections (gifts, conflicts) — "a dinner worth AED 500 paid for by a supplier" is more useful than abstract rules.
- Arabic translation required for entities incorporated and operating in UAE onshore, KSA, LB, and EG. The Arabic version should be the operative version in those jurisdictions.
- The Code should be reviewed by local counsel in each jurisdiction of operation before final publication.

## Common mistakes

- A Code that is aspirational but unenforceable — no thresholds, no process, no consequences.
- Failing to address the UK Bribery Act "failure to prevent" offence for internationally-active MENA companies.
- No whistleblower protection commitment — this undermines the reporting obligation.
- Using a US-centric template that references US laws inapplicable to MENA operations without adaptation.
- No process for updating the Code after a regulatory change or compliance incident.

## Related skills

- [[prompt-pack-corporate-governance-policy]]
- [[prompt-pack-delegation-of-authority-matrix]]
- [[prompt-pack-director-indemnification-agreement]]
- [[prompt-pack-whistleblowing-policy]]
- [[prompt-pack-anti-bribery-policy]]
