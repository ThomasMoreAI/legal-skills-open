---
name: safety-unauthorized-practice-of-law-lb-ksa-uae-sboghossian
title: UPL — Unauthorized Practice of Law in LB / KSA / UAE
description: Use when assessing whether a specific AI output or action in a Lebanese, Saudi, or UAE context constitutes or risks constituting unauthorized practice of law. Covers the precise acts reserved to inscribed/licensed lawyers in each jurisdiction, what AI drafting and analysis can freely do, the specific rule for eFirm (lawyer-supervised) vs consumer surfaces, and the required checkpoint language for court filings. MENA-specific companion to safety-bar-rule-5-5-upl-ai.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/safety/safety-unauthorized-practice-of-law-lb-ksa-uae
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: sa
practice: finance
language: en
---

# UPL — Unauthorized Practice of Law in LB / KSA / UAE

## When to use this

Apply when:
- A user in Lebanon, Saudi Arabia, or UAE asks the AI to perform an act that may require bar admission or licensing.
- A court filing is about to be submitted and sign-off obligations need to be identified.
- An eFirm is configuring output modes for lawyers practicing in one of these jurisdictions.
- A consumer user in MENA asks the AI to "be their lawyer" or represent them.

## Lebanon — Law of the Bar / Code of Civil Procedure

### Reserved acts (require Beirut Bar / regional bar inscription)
- **Court representation**: appearing as counsel of record before Lebanese civil, commercial, criminal, and administrative courts.
- **Signing pleadings**: signing memoirs (مذكرات), applications, and submissions filed with courts as counsel.
- **Signing certifying legal opinions**: formal legal opinions given for a fee by a registered lawyer under their bar number.
- **Notarial acts by lawyer-notaries**: some notarial functions performed by registered lawyers (not the same as a general notary public).

### What AI can do freely in Lebanon
- Drafting documents for client or lawyer review.
- Legal research and analysis (not submitted as signed advice).
- Explaining the Lebanese Code of Obligations and Contracts (Law of Obligations / Code Libanais des Obligations et des Contrats), Code of Civil Procedure, and other statutes.
- Preparing a document that a registered lawyer will review, sign, and file.

### AI output rule for Lebanon
> For any document intended for submission to a Lebanese court, or any legal opinion to be issued formally: "This document requires review and sign-off by an advocate inscribed with the Beirut Bar Association, Tripoli Bar, or the relevant regional bar before it can be filed or issued."

**On eFirm surfaces**: the user is the inscribed lawyer. Surface this as a checkpoint confirmation, not a refusal:
> "Ready for your review and signature as counsel of record."

## Saudi Arabia — Code of Law Practice (Royal Decree M/38) + MOJ Regulations

### Reserved acts (require Saudi Bar license)
- **Pleading before Saudi courts**: the right of audience before all Saudi courts (commercial, civil, criminal, labor, administrative — including SAMA tribunal, ZATCA courts) is restricted to Saudi-licensed lawyers.
- **Foreign counsel**: foreign lawyers may only appear under a registered partnership with a Saudi law firm; they cannot independently hold themselves out as Saudi counsel.
- **Sharia courts**: pleas before Sharia courts require Sharia-qualified counsel (typically a practicing Saudi lawyer with the relevant court accreditation).
- **MOJ e-filing systems (Najiz platform)**: filings require the lawyer's registered Saudi Bar credentials; AI cannot file on behalf of a party.
- **Notarial acts (Tawthiq)**: notarial certification before a Saudi notary (Tawthiq) requires the physically present parties and the notary; AI cannot substitute.

### What AI can do freely in Saudi Arabia
- Drafting any document type for lawyer review: MOA, SHA, employment contracts, NDAs, commercial agreements.
- Legal research under KSA law (Saudi regulations, royal decrees, SAMA/CMA circulars, labor law).
- Analysis of Saudi case law and regulatory guidance.
- Preparing a pleading that the licensed Saudi lawyer will review, sign, and file through Najiz.

### AI output rule for KSA
> For any court filing, MOJ submission, regulatory filing, or Sharia court document: "This document must be filed by a lawyer licensed under Royal Decree M/38. Please have your Saudi-licensed counsel review and submit through the Najiz platform / relevant court system."

**Sharia court matters specifically**: "Sharia court proceedings require Sharia-qualified counsel. Please ensure your counsel holds the appropriate court accreditation."

## UAE — Federal Law on the Legal Profession + Emirate Bars + DIFC / ADGM

### Onshore UAE — reserved acts
- **Court representation**: UAE national lawyers hold preference for advocacy in onshore UAE courts. Non-UAE-national lawyers must hold UAE bar admission for regular court practice.
- **Civil/commercial filings in onshore courts**: representations before Dubai Courts, Abu Dhabi Courts, Sharjah Courts etc. require licensed UAE counsel.
- **Corporate filings requiring legal certification**: certain DED (Department of Economic Development) filings, ADCO, DED notarizations may require licensed counsel countersignature.

### DIFC Courts
- **Registered practitioners only**: non-national lawyers registered before the DIFC Courts may appear. Registration is obtained through the DIFC Courts Practitioners Committee.
- **Non-registered lawyers**: may advise clients but cannot act as advocate of record before the DIFC Court.

### ADGM Courts
- **Similar to DIFC**: registered practitioners before the ADGM Court; registration required for advocacy.
- Both DIFC and ADGM permit a broader range of international practitioners than onshore UAE courts.

### What AI can do freely in UAE
- Drafting contracts governed by UAE law (Federal laws, DIFC law, ADGM law as applicable).
- Legal research under UAE federal statutes, DIFC laws, ADGM regulations.
- Drafting court pleadings for lawyer review and signature.
- Regulatory guidance on UAE corporate, employment, and commercial law.

### AI output rule for UAE
For onshore UAE filings:
> "This document is intended for filing before [UAE court / DED / regulatory body]. It requires sign-off by a UAE-licensed lawyer before submission."

For DIFC/ADGM:
> "This document is intended for filing before [DIFC/ADGM Court]. It must be submitted by a practitioner registered before that court."

## The four operational rules (all three jurisdictions)

1. **Draft freely** — document drafting and legal research are not UPL in any of these jurisdictions.
2. **Never hold the AI out as counsel of record** — no AI-produced document should describe the AI as the user's lawyer.
3. **Checkpoint for court filings** — always append the jurisdiction-appropriate sign-off advisory on any document marked for court submission.
4. **eFirm surface treatment** — on eFirm tenants, assume the user is the admitted lawyer. Surface the sign-off checkpoint as a workflow step, not a refusal. The lawyer is in control.

## Referral to bar associations

For users who need a licensed lawyer in these jurisdictions:
- **Lebanon**: Beirut Bar Association (`bar.org.lb`); Tripoli Bar Association.
- **KSA**: Saudi Bar Association (`sba.org.sa`); Ministry of Justice lawyer directory (`moj.gov.sa`).
- **UAE**: UAE Bar Associations (emirate-level: Dubai Legal Affairs Dept; Abu Dhabi Bar Association).
- **DIFC**: DIFC Courts registered practitioners list (`difccourts.ae`).
- **ADGM**: ADGM Courts registered practitioners list (`adgmcourts.com`).

## Related skills

- [[safety-bar-rule-5-5-upl-ai]] — general UPL principles and ABA Rule 5.5
- [[safety-no-legal-advice-disclaimer-rules]] — information vs advice line
- [[safety-criminal-defense-disclaimer]] — heightened handling for criminal matters
- [[inst-lb-bar-association-integration]] — integration with Lebanese bar referral system
- [[conversation-refusal-policy]] — general refusal patterns for out-of-scope requests
