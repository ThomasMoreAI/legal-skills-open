---
name: safety-ai-disclosure-required-tribunals-sboghossian
title: AI Disclosure Requirements Before Tribunals
description: Use when a lawyer or user indicates that AI-assisted work product (research, drafts, briefs, or submissions) will be filed with or presented to a court, tribunal, or regulatory body. Triggers the appropriate AI-disclosure reminder and citation-verification warning based on the forum's rules. Covers US courts (post-Mata v. Avianca standing orders), UK Bar Standards Board guidance, DIFC/ADGM courts, KSA/UAE onshore courts, French ordre des avocats, and EU AI Act implications. Hard-blocks any request to conceal AI use from a tribunal.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/safety/safety-ai-disclosure-required-tribunals
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# AI Disclosure Requirements Before Tribunals

## When to use this

Apply this skill whenever the user signals that AI-assisted content will be submitted to a court, arbitral tribunal, regulatory body, or other adjudicative forum. Trigger phrases include:
- "I'm filing this brief / motion / memorial"
- "I'm submitting this to the court / tribunal / panel"
- "Can you draft my pleading / submission"
- "I need this for my case before [forum]"
- "Is this citation correct for filing?"

The disclosure obligation varies significantly by jurisdiction and forum — this skill maps those rules and generates the correct reminder.

## Jurisdiction-by-jurisdiction rules

### United States — Federal and State Courts

**General landscape (post-Mata v. Avianca, 2023):**
*Mata v. Avianca* (SDNY 2023) produced sanctions against attorneys who filed a brief containing AI-hallucinated case citations. The resulting attention prompted standing orders across the US federal system. As of mid-2026, requirements have proliferated unevenly.

Key categories of current US court AI rules:

| Rule type | What it requires | Examples |
|-----------|-----------------|---------|
| Mandatory disclosure certificate | Certify that AI was or was not used; certify all citations independently verified | Several SDNY judges, ND Texas, ND Cal |
| Disclosure with detail | Name the tool used; describe its role | Some chambers orders |
| Certification of independent verification | Lawyer certifies each citation checked against primary source | ND Tex Standing Order (Judge Pittman and others) |
| No specific rule yet | General duty of candor applies; Mata serves as cautionary precedent | Many districts |

**Practical rule for all US courts**: before any brief is filed, the attorney must independently verify every citation. No AI-generated citation should appear unverified. Check the specific court's local rules and the judge's standing/chambers orders — they can vary judge to judge within the same district.

**Appellate courts**: Second Circuit, Fifth Circuit, and others have issued guidance. Always check the court's website for current standing orders.

### United Kingdom

The UK Bar Standards Board (BSB) issued 2023 guidance clarifying that the **duty of candor to the court** under the BSC Code of Conduct extends to AI-assisted submissions. Specific obligations:
- A barrister may not make a representation to a court that they believe to be false — this includes permitting an AI-hallucinated citation to appear in a settled submission without verification.
- AI use is not itself prohibited; verification and accuracy are the barrister's responsibility.
- Solicitors: SRA guidance is similarly candor-focused; no blanket prohibition on AI drafting.

### DIFC Courts / ADGM Courts

As of May 2026, neither court has issued a formal AI-disclosure practice direction. However:
- The DIFC Courts' Practice Directions and the ADGM Court Rules both incorporate a duty of candor consistent with their English-law heritage.
- Given the trajectory post-Mata, a practice direction on AI use is widely anticipated.
- **Safe practice**: apply the same verification discipline as for UK courts; flag any AI-assisted citations with a note in the submission file.

### KSA Onshore Courts / UAE Onshore Courts

No formal AI-disclosure rules exist in either jurisdiction as of May 2026. The duty of accuracy in pleadings is inherent in Saudi and UAE civil/commercial procedure codes, but no AI-specific overlay has been issued.

**Practical implication**: the absence of a specific rule does not eliminate the professional responsibility risk — filing a submission containing fabricated citations could constitute misconduct under the Saudi Bar Advocates Law (Royal Decree M/38) or UAE Federal Law on the Legal Profession.

### France — Ordre des Avocats

The French Conseil National des Barreaux (CNB) and Paris Bar were developing guidance as of early 2026. No final rule yet. The general principle under the Règlement Intérieur National (RIN) is that the lawyer signs and is responsible for every submission — AI does not alter that responsibility.

### EU — AI Act Implications

The EU AI Act (Regulation 2024/1689, entered into force August 2024; most obligations apply from August 2026) classifies certain AI systems used in justice administration as **high-risk** (Annex III, item 8). High-risk systems must:
- Meet transparency requirements
- Be subject to human oversight
- Maintain logs of use

Where an AI tool is classified as high-risk under the AI Act, its operator must provide users with meaningful information about its capabilities and limitations. A legal AI used for court-submission drafting may fall within this classification depending on configuration. Practitioners should verify whether their tool's operator has conducted an AI Act conformity assessment.

## Default behavior — what to append to court-submission output

When any output is destined for a court filing:

**For all jurisdictions:**
> ⚠️ **Citation verification required**: Verify every case citation, statute reference, and quotation independently against the primary source before filing. AI systems can generate plausible but non-existent citations. Filing inaccurate citations may lead to sanctions, adverse professional conduct findings, or reputational damage.

**For US-licensed lawyers:**
> ⚠️ **AI-disclosure check**: Many US federal courts now require a certification that AI was or was not used in preparing this filing, and/or that all citations have been independently verified. Check the local rules and standing orders for the specific judge before filing.

**For all jurisdictions where rules are unsettled:**
> ⚠️ **Disclosure check**: Disclosure rules for AI-assisted court filings are evolving rapidly. Check your court's current practice directions before submitting.

## Hard refusal

If a user asks to conceal, omit, or disguise AI use in a court filing, refuse directly:
> This request asks me to help deceive a tribunal about the origin of legal work. That would violate every bar code's duty of candor. I won't do it. I can help you draft a compliant AI-disclosure certificate or footnote instead.

## Escalation path

- Unknown court rules: direct user to the court's official website, local rules page, and chambers orders.
- AI Act applicability assessment: refer to [[review-compliance-gap-analysis]] for EU AI Act high-risk classification.
- Professional conduct risk: [[safety-bar-rule-1-1-competence-ai]] for competence framing.

## Related skills

- [[safety-bar-rule-1-1-competence-ai]] — competence duties and technology understanding
- [[safety-bar-rule-1-6-confidentiality-ai]] — confidentiality when using AI for client matters
- [[safety-ai-not-privileged-disclaimer-us-heppner]] — privilege status of AI conversations
- [[safety-no-legal-advice-disclaimer-rules]] — scope of permissible AI output
- [[safety-bar-rule-5-5-upl-ai]] — unauthorized practice limits
