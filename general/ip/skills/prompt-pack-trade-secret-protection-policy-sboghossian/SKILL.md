---
name: prompt-pack-trade-secret-protection-policy-sboghossian
title: Trade Secret Protection Policy
description: Use when a company needs to draft or overhaul an internal trade secret protection policy — the governance document that identifies, classifies, controls access to, and enforces protection of confidential business information that derives commercial value from secrecy. Relevant for technology, pharmaceutical, financial, and manufacturing firms operating in MENA (UAE, KSA, Lebanon, Egypt), EU, and UK where trade secret law varies materially in scope and remedies.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-trade-secret-protection-policy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# Trade Secret Protection Policy

## When to use this

Use this skill when a company needs to draft, review, or update the internal governance policy that operationalizes trade secret protection. This is the companion document to an NDA — the NDA binds outside parties; the trade secret policy governs insiders (employees, contractors, interns) and processes. Typical triggers:

- Pre-IPO or M&A due diligence reveals no documented trade secret policy (a common deal risk flag)
- A company is establishing R&D operations in a MENA jurisdiction and needs a policy that will hold up under local law
- An employee departure or suspected misappropriation prompts a reactive audit
- External counsel advises that "reasonable measures" to protect secrets are not sufficiently documented for litigation

A well-drafted policy is essential to establish the "reasonable measures" element required to claim trade secret protection under virtually every jurisdiction's statute or case law.

## Required inputs

| Input | Why it matters | Sensible default |
|-------|---------------|-----------------|
| Company name and industry | Industry shapes the types of trade secrets and common threat vectors | Prompt user |
| Jurisdictions of operation | Determines applicable statute and enforcement mechanisms | All jurisdictions where company has employees or operations |
| Categories of trade secrets | Policy cannot protect secrets it doesn't define | Prompt user to enumerate; see structure §1 below |
| Employee / contractor population | Scope of who must sign and comply | All employees, consultants, officers, and seconded staff |
| IT systems in scope | Defines the digital perimeter | All company-owned and BYOD devices, cloud services, collaboration tools |

## Optional inputs

- **Existing NDA / employment contract clauses** — policy should be consistent with existing contractual obligations
- **Classification system** (e.g., Confidential / Highly Confidential / Public) — enables tiered access controls
- **Regulatory context** (e.g., sector-specific data protection requirements) — financial data, health data, government contracts may have additional statutory overlays
- **Incident history** — prior leaks inform the tailored controls section
- **Third-party relationships** (JV partners, suppliers with access to IP) — extends the policy's reach

## Document structure

1. **Purpose and scope** — explains why the policy exists; defines who it applies to (employees, contractors, temps, officers, third parties with system access); states it is a condition of employment/engagement
2. **Definition of trade secrets** — enumerate categories: formulas and processes, technical specifications, source code, financial models, customer lists and pricing, business strategies, personnel information, pending patent applications, undisclosed product roadmaps; include a catch-all clause ("any other information that the Company treats as confidential and which derives independent economic value from its secrecy")
3. **Classification system** — three-tier: (a) Public, (b) Confidential (internal use only), (c) Highly Confidential / Trade Secret (need-to-know basis); include marking requirements for documents, emails, and files
4. **Identification and inventory** — procedure for identifying and registering trade secrets in a central register; assigned ownership (business unit head); annual review cycle
5. **Access controls** — least-privilege principle; role-based access; mandatory approval workflow for elevated access; prohibition on storing trade secrets on personal devices or unauthorized cloud services
6. **Employee obligations** — duty of confidentiality during and after employment; use restrictions (only for authorized company purposes); notification obligation upon discovery of unauthorized access or disclosure; post-termination non-use obligations (note: non-compete enforceability varies sharply by jurisdiction)
7. **Third-party sharing protocols** — all sharing requires: (a) NDA in place, (b) manager approval, (c) minimum necessary disclosure, (d) log entry in sharing register; vendor DPA required if sharing involves personal data
8. **Physical security** — clean-desk policy; locked storage for printed materials; visitor escort procedures; secure destruction requirements (cross-cut shredding, certified electronic destruction)
9. **Digital security** — encryption at rest and in transit; DRM for sensitive documents; audit trails on access; prohibition on unapproved AI/cloud tools that may ingest trade secrets (critical for MENA firms where sovereign data concerns apply)
10. **Incident response** — suspected misappropriation: immediate notification to legal / CISO; evidence preservation instructions; cooperation with investigation; potential law enforcement referral
11. **Monitoring and enforcement** — company's right to monitor systems; consequences of violation (disciplinary action up to termination; civil and criminal referral); whistleblower protection for good-faith reports
12. **Training** — mandatory onboarding training; annual refresher; acknowledgment log
13. **Governing law and enforcement** — identifies the applicable trade secret statute by jurisdiction (see table below); notes remedies (injunctions, damages, criminal prosecution)
14. **Policy maintenance** — annual review; version control; legal sign-off requirement

## Jurisdictional notes

| Jurisdiction | Key instrument | Notable points |
|---|---|---|
| UAE (onshore) | Federal Decree-Law No. 31/2021 (Crimes and Penalties) + Commercial Transactions Law; DIFC: Contract Law + Common Law | Criminal liability for trade secret theft under UAE Penal Code; injunctive relief available; "reasonable measures" not separately defined but courts look to contractual obligations as evidence |
| DIFC / ADGM | Common law; DIFC Contract Law; ADGM companies may rely on English common law of confidentiality | Springboard doctrine applies (prevents unjust enrichment from misappropriated secrets); courts will grant urgent injunctions |
| KSA | Commercial Court Law; Regulatory framework under ZATCA and SAGIA; no standalone trade secret act — protection via contract and unfair competition principles | Employment contracts must include confidentiality clauses; Saudi courts enforce injunctions but enforcement timelines can be lengthy; Arabic employment contract prevails |
| Lebanon | Code of Obligations and Contracts (Art. 230-233 on tort); Industrial Property Law No. 240/2000 | Criminal penalties for industrial espionage; civil damages; no standalone trade secret statute — relies on tort and contract |
| Egypt | Intellectual Property Law No. 82/2002 (Part III — Trade Secrets and Undisclosed Information) | Explicitly recognizes trade secrets as protectable; requires "reasonable measures"; civil and criminal remedies; Cairo courts active in injunction practice |
| EU | Trade Secrets Directive 2016/943 (transposed into national law) | Harmonized definition: (i) secret, (ii) commercial value, (iii) reasonable steps taken; national transpositions vary on remedies |
| UK | Common law of confidentiality; Trade Secrets (Enforcement, etc.) Regulations 2018 (post-Brexit adoption of EU Directive) | "Springboard" doctrine; breach of confidence action; "reasonable steps" required |
| US | Defend Trade Secrets Act (DTSA) 2016 + state laws (most follow Uniform Trade Secrets Act) | Federal civil cause of action; ex parte seizure orders available; criminal prosecution under Economic Espionage Act |

**MENA trap — post-termination non-competes:** Non-compete covenants are enforceable in UAE and KSA if limited in duration (typically ≤ 2 years) and geographic scope and if the employee had access to genuine trade secrets. Lebanon and Egypt place tighter limits on duration. Courts in all MENA civil-law jurisdictions will reduce unreasonably broad restrictions. The trade secret policy should state that non-compete obligations are governed by employment contracts (not this policy alone).

**AI tools trap:** Employees using public AI assistants (ChatGPT, Gemini, Copilot) may inadvertently disclose trade secrets. Policy must explicitly list prohibited uses of external AI tools and require legal/IT approval for any approved AI tool that processes company data.

## Drafting standards

- **Define "reasonable measures" explicitly** — regulators and courts in all jurisdictions require concrete protective measures; a vague policy offers minimal legal protection
- **Tiered classification** must map to concrete access controls — if all confidential information is in one bucket, the policy lacks operational meaning
- **Acknowledgment requirement** — every employee and contractor must sign an acknowledgment upon hire and annually; retain records for at least 7 years (or the applicable limitation period)
- **Post-termination reminders** — exit checklist should include: device return, deletion of company data from personal devices, reminder letter of confidentiality obligations; document this process
- Do not use US-style "work product" or DTSA-specific language as the operative framework if the governing jurisdiction is civil law — translate concepts to the applicable statute

## Common mistakes

- **No classification system** — protection is easier to demonstrate if information is visibly marked as confidential
- **Policy not signed by employees** — unsigned policy provides weak evidentiary foundation
- **AI tool gaps** — omitting AI tools from "prohibited disclosure channels" is now the most frequent gap
- **Broad non-compete drafted inside the policy** — non-compete obligations belong in employment contracts, not internal policies; a policy clause may not be independently enforceable
- **No incident response procedure** — missing this makes forensic investigation and litigation harder
- **Single language** — in KSA and UAE, an Arabic version (or a bilingual version with Arabic governing) is necessary for the policy to be enforceable against Arabic-speaking employees in labor proceedings

## Related skills

- [[prompt-pack-nda-unilateral]]
- [[prompt-pack-nda-mutual]]
- [[prompt-pack-work-for-hire-agreement]]
- [[prompt-pack-vendor-data-protection-addendum]]
- [[kb-ip-mena]]
- [[heuristic-always-state-jurisdiction-first]]
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]]
