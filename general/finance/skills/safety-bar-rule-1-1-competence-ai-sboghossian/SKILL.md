---
name: safety-bar-rule-1-1-competence-ai-sboghossian
title: Bar Rule 1.1 — Competence and AI Use
description: Use when a lawyer user needs guidance on the professional-responsibility duty of competence as it applies to AI tool use in legal practice. Covers ABA Model Rule 1.1 and its analogs in MENA bars (Lebanese Bar, Saudi Bar, UAE Bar, DIFC/ADGM Rules of Professional Conduct) and European bar codes (UK SRA, French CNB/RIN). Specifically addresses what "understanding the technology" means in practice, verification obligations, hallucination risk, and how to document AI use in matter files to satisfy competence duties.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/safety/safety-bar-rule-1-1-competence-ai
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# Bar Rule 1.1 — Competence and AI Use

## When to use this

Apply whenever a lawyer user:
- Asks whether they can rely on AI-generated legal research or citations.
- Asks about their professional obligations when using AI drafting tools.
- Is about to submit AI-assisted work to a court or regulatory body.
- References a jurisdiction's bar rules in relation to AI.
- Has encountered what may be an AI hallucination in their work.

## The competence duty — what the rules say

### ABA Model Rule 1.1 (US)
"A lawyer shall provide competent representation to a client. Competent representation requires the legal knowledge, skill, thoroughness and preparation reasonably necessary for the representation."

Comment 8 (as updated): "To maintain the requisite knowledge and skill, a lawyer should keep abreast of changes in the law and its practice, *including the benefits and risks associated with relevant technology*." This comment was added in 2012 and has become the primary hook for AI-competence obligations.

### MENA analogs

**Lebanon — Beirut Bar / Tripoli Bar**: The Lebanese Code of Professional Conduct (Nizám al-mihna) imposes a general competence duty on advocates. There is no AI-specific commentary as of May 2026, but the general principle — that a lawyer is responsible for the work product they sign — is clear and well-established.

**Saudi Arabia — Saudi Bar (Code of Law Practice, Royal Decree M/38)**: Article 18 and related provisions require lawyers to handle matters with care and professional skill. Submissions to Saudi courts that contain inaccurate legal citations could expose the lawyer to disciplinary action under the Code and before the Ministry of Justice.

**UAE — Federal Law on the Legal Profession (and emirate bars)**: Similar to KSA; DIFC and ADGM courts each have Rules of Professional Conduct that include competence requirements modeled on the SRA Code of Conduct.

**DIFC / ADGM**: Practitioners registered before these courts are subject to the DIFC Courts Practice Direction on Professional Conduct and the ADGM Court Procedure Rules, both of which incorporate competence obligations analogous to the SRA.

### European analogs

**UK — SRA Code of Conduct**: Paragraph 3.2 requires solicitors to "maintain the level of competence and legal knowledge needed to practise effectively." The Law Society and BSB have issued 2023–2024 guidance that technology competence — including understanding AI limitations — falls within this obligation.

**France — Règlement Intérieur National (RIN)**: The general professional duties under the RIN (especially diligence and competence) apply to AI-assisted work. The Conseil National des Barreaux has issued a preliminary position on AI ethics for lawyers.

## What "competence with AI" means in practice

A competent lawyer using AI for legal work must understand:

1. **What the tool does and does not do**
   - Large language models generate plausible text — they do not search databases unless explicitly connected to one with Retrieval Augmented Generation (RAG).
   - Without RAG or real-time access, case citations may be entirely fabricated (hallucinated) — this is what happened in *Mata v. Avianca* (2023).
   - AI cannot reliably know whether a statute has been amended after its training cutoff.

2. **Verification obligation — non-delegable**
   - The lawyer, not the AI, bears responsibility for the accuracy of every citation, statutory reference, and legal proposition in their work product.
   - Independent verification means checking the primary source: the official reporter, official gazette, or authenticated court database — not another AI query.

3. **Scope limitations**
   - AI may be unreliable on jurisdictionally novel questions, very recent decisions, and areas where training data is sparse (e.g., MENA civil-law nuances, Sharia-influenced commercial law).
   - A competent practitioner calibrates reliance accordingly — higher caution on novel jurisdictional questions.

4. **Confidentiality risks**
   - The lawyer must understand that consumer AI tools may train on inputs, that conversations may not be privileged (see [[safety-ai-not-privileged-disclaimer-us-heppner]]), and that confidentiality duties under Rule 1.6 / local analogs require appropriate tool selection.

5. **Documentation**
   - Some bars are moving toward requiring that AI use be documented in matter files. Even where not yet required, best practice is to note: which AI tool was used, for what task, and that the output was independently verified.

## Consequences of failure

### Professional discipline
- Sanctions range from private admonition to suspension or disbarment depending on severity.
- *Mata v. Avianca* (SDNY 2023): two attorneys fined $5,000 each; motion to dismiss sanctioned because briefs cited non-existent AI-generated cases.
- Subsequent US cases have resulted in similar sanctions.

### Malpractice
- A lawyer who files a brief with a fabricated citation, or relies on an AI-generated legal opinion without verification, may face a malpractice claim if the client suffers harm (missed deadline, adverse judgment based on inaccurate law).
- The standard is what a competent lawyer in the same circumstances would have done — verification is the standard.

### Court sanctions
- Courts have inherent power and Rule 11/equivalent authority to sanction lawyers who file inaccurate or misleading papers, regardless of whether AI was involved.

## Practical checklist for AI-assisted legal work

- [ ] Understand the tool's capabilities and limitations before relying on it.
- [ ] Verify every case citation against the official reporter or authenticated database.
- [ ] Verify every statutory/regulatory reference against the current official text.
- [ ] Flag jurisdictionally novel questions for additional human research.
- [ ] Check AI training cutoff — is the question one where recent changes matter?
- [ ] Document AI use in the matter file.
- [ ] Check applicable court's local rules / chambers orders for AI-disclosure requirements ([[safety-ai-disclosure-required-tribunals]]).
- [ ] Ensure AI tool is appropriate for confidentiality obligations ([[safety-bar-rule-1-6-confidentiality-ai]]).

## Related skills

- [[safety-bar-rule-1-6-confidentiality-ai]] — confidentiality obligations for AI tool use
- [[safety-bar-rule-5-5-upl-ai]] — unauthorized practice limits
- [[safety-ai-not-privileged-disclaimer-us-heppner]] — privilege status of AI conversations
- [[safety-ai-disclosure-required-tribunals]] — disclosure requirements for AI-assisted court filings
- [[safety-bar-rules-confidentiality]] — confidentiality architecture overview
