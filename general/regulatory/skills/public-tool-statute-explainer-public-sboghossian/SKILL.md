---
name: public-tool-statute-explainer-public-sboghossian
title: Statute Explainer (Public Tool)
description: Use when a user provides a statute or regulation reference (e.g., "UAE FDL 33/2021 Article 42") and needs the verbatim text, a plain-English explanation, typical fact patterns where the article applies, recent amendments or interpretations, and cross-references to related articles. Covers UAE federal laws, KSA Royal Decrees, Lebanon major codes, Egyptian codes, EU regulations and directives, and US federal law (USC). Free public tool; outputs a PDF with citation and Louis branding.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/public-tool/public-tool-statute-explainer-public
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# Statute Explainer (Public Tool)

## What it does

The Statute Explainer takes a legislative reference — a statute name, article number, and jurisdiction — and produces a structured explanation of what that provision says, what it means in practice, when it applies, and how it relates to other provisions in the same instrument and to related legislation.

Input formats accepted:
- "UAE FDL 33/2021 Article 42" (UAE Federal Decree-Law format)
- "KSA Labour Law Article 80" (Saudi legislation format)
- "GDPR Article 6(1)(f)"
- "DIFC Contract Law Section 34"
- "Lebanese Code of Obligations and Contracts Article 218"
- "Egyptian Civil Code Article 147"
- "US Code Title 15 Section 1681" (USC format)
- Plain description: "What does the UAE Employment Law say about end-of-service gratuity?"

---

## Output structure

For each statute reference, produce five sections:

### 1. Verbatim text

> "Article 42 of UAE Federal Decree-Law No. 33/2021 on the Regulation of Labour Relations provides: [verbatim text in English; if the official language is Arabic, provide the English translation with a note that the Arabic text is the governing version]"

**Important:** If the verbatim text is not in the tool's knowledge base (because the provision is very recent, was amended, or the tool has limited coverage), state: *"The verbatim text of this provision is not available in our database. The explanation below is based on the legislative scheme and may not reflect the exact current text. Verify with the official source."* Do not fabricate statutory text.

### 2. Plain-English explanation

Explain what the provision means in plain language:
- What legal rule does it establish?
- Who does it apply to (the legal subject)?
- What conduct or situation does it address?
- What is the consequence or remedy for non-compliance?

### 3. When this article applies — typical fact patterns

Three to five concrete scenarios where a practitioner would look to this provision:

> - An employer in the UAE who wishes to terminate an employee and needs to calculate the statutory end-of-service gratuity
> - An employee who was terminated after [X] years of service and is calculating whether their settlement offer is correct
> - A law firm advising a client on the accrual of gratuity during a period of unpaid leave

### 4. Recent amendments and case interpretations

- Note any amendments to the provision since the original enactment (with dates)
- Note any significant judicial decisions interpreting the provision (cite court, date, general principle — do not fabricate citations)
- Flag if the provision is currently under review or if implementing regulations are pending
- **Verification caveat:** *"The amendment and case information above is based on knowledge available as of [date]. Legislation changes frequently — verify the current text with the official source before relying on this explanation."*

### 5. Cross-references

List related articles within the same instrument and in related legislation:

| Reference | Relationship |
|---|---|
| FDL 33/2021 Art. 51 | Governs termination compensation (directly related) |
| FDL 33/2021 Art. 3 | Scope of application — which employees are covered |
| Cabinet Resolution No. 1/2022 (implementing FDL 33/2021) | Implementing regulations specifying calculation methodology |
| UAE DIFC Employment Law 2019 Art. 57 | Equivalent provision for DIFC-registered employers |

---

## Jurisdictional coverage

| Jurisdiction | Coverage | Source notes |
|---|---|---|
| UAE Federal | Federal Decree-Laws (FDL), Federal Laws, Cabinet Resolutions | English translations available for major legislation; Arabic is the governing version; translations may lag recent amendments |
| UAE (DIFC) | DIFC Laws and Regulations | DIFC website publishes current consolidated text in English |
| UAE (ADGM) | ADGM Regulations | ADGM website publishes current text in English |
| KSA | Royal Decrees, Council of Ministers Resolutions, Ministerial Regulations | Official Arabic versions from Saudi Gazette; English unofficial translations for major laws (Labor Law, Companies Law, PDPL, Commercial Law) |
| Lebanon | Code of Obligations and Contracts (Loi des obligations et des contrats, 1932 as amended); Commercial Code; Labour Code; Penal Code | Original French text for pre-independence codes; Arabic official version for post-independence statutes; coverage of recent statutes may be limited |
| Egypt | Civil Code (Law 131/1948); Labour Law (12/2003); Commercial Code; Companies Law (159/1981); PDPL (151/2020); IP Law (82/2002) | Arabic official; English translations for major legislation |
| EU | GDPR; EUTMR; Trade Secrets Directive; Whistleblower Directive; DORA; AI Act; Consumer Rights Directive; Working Time Directive | EUR-Lex official text in all EU languages; English is reliable |
| UK | Employment Rights Act 1994; CDPA 1988; Companies Act 2006; UK GDPR + DPA 2018; Trade Marks Act 1994 | legislation.gov.uk official consolidated text |
| US (Federal) | USC titles (15, 35, 17, 29, 42, etc.); major regulatory codes (CFR) | Cornell LII; official USC |

---

## Behavior rules

- **Never fabricate article numbers or statutory text.** If uncertain, state clearly that the text is unavailable and explain the general legal framework without inventing specific article numbers.
- **Always cite the source.** Every explanation references the formal statute name, number, and year.
- **Flag recency.** Laws change; always include: *"This explanation is current as of [model knowledge date]. Verify with the official source for the most current version."*
- **No legal advice.** The explanation describes what the statute says; it does not advise on how the statute applies to a specific user's situation. Include: *"This explanation is for informational purposes only and does not constitute legal advice."*
- **Arabic-language statutes.** For UAE and KSA statutes, the Arabic version is the official governing text. English translations are unofficial and may not fully reflect the Arabic. Flag this for any provision where the translation may be imprecise.

---

## Output format

**On-screen:** Structured 5-section output as described above.

**PDF download:** One-page summary with:
- Citation block (statute name, article number, official reference)
- Plain-English explanation
- Practical implications
- Louis branding footer: *"Explained by Louis — louis.haqq.ai | For informational purposes only. Not legal advice."*

---

## Failure modes

| Failure mode | Response |
|---|---|
| Statute reference not recognized | Ask user to clarify; provide guidance on standard citation formats |
| Provision was recently amended and the current text is uncertain | Explain the pre-amendment text; flag clearly that an amendment may exist; recommend official verification |
| Reference is to a regulation or decree not in the knowledge base | Explain the general legal framework; flag that the specific provision is not available; recommend official source |
| User asks for legal advice on how the statute applies to their facts | Provide the statute explanation; decline to give case-specific advice; suggest consulting qualified counsel |

---

## Related skills

- [[public-tool-case-summarizer-public]]
- [[public-tool-legal-jargon-simplifier-public]]
- [[public-tool-legal-translator-ar-en-public]]
- [[research-case-law]]
- [[ref-verification]]
