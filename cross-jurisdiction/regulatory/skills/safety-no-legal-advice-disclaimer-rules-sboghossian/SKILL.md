---
name: safety-no-legal-advice-disclaimer-rules-sboghossian
title: Legal-Information-Not-Advice — Rule Set
description: Use to govern when, where, and how the legal-information-not-legal-advice disclaimer must appear. Defines the precise line between permissible legal information and regulated legal advice, specifies which surface types require inline disclaimers vs. page-level disclaimers vs. no disclaimer (lawyer/eFirm surfaces), and provides ready-to-use disclaimer language for consumer chat, public tools, and drafted documents. Core safety rail for all consumer-facing and public-tool output.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/safety/safety-no-legal-advice-disclaimer-rules
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: regulatory
language: en
---

# Legal-Information-Not-Advice — Rule Set

## When to use this

This skill governs every consumer-facing or public-tool output. It fires when:
- The platform is generating a substantive legal response for a non-lawyer user.
- A document is being drafted for a consumer (public) user.
- A public tool (`/tools/*`) produces a legal result.
- The system needs to determine whether to surface a disclaimer and what form it should take.

It does **not** fire for:
- Lawyer/eFirm surfaces where the user is the qualified counsel.
- In-house counsel surfaces operating in professional B2B mode.
- Non-substantive responses (greetings, clarifying questions, navigation help).

## The core distinction

**Legal information** (permitted): explaining what the law generally says, describing typical options available to a category of person, providing the procedural framework, explaining what documents are commonly used.

**Legal advice** (not permitted without license): applying the law to a specific person's specific facts and telling them what to do. The test is whether the output "counsels a specific client" or merely "informs a category of person."

| Permitted | Not permitted |
|-----------|--------------|
| "Contracts in Lebanon require offer, acceptance, and consideration under the Code of Obligations." | "Based on what you've described, you have a valid contract claim and should sue." |
| "Employers in the UAE must provide a minimum 30-day notice for termination under the Labour Law." | "Your employer has wrongfully terminated you and you will receive 3 months' compensation." |
| "A will in KSA must comply with Islamic inheritance law (Sharia faraid rules)." | "Under your specific family situation, your estate would be distributed as follows..." |
| "Here is a standard NDA template for review by your lawyer." | "This NDA is binding on your counterparty and you don't need a lawyer to review it." |

## Disclaimer content — by surface

### Surface 1 — Consumer chat (inline footer per substantive response)

> *This is legal information, not legal advice. For your specific situation, consult a qualified lawyer in your jurisdiction.*

**When to surface**: on every substantive legal response in consumer chat. Inline — after the response content, not before (avoids interrupting the answer).

**When to omit**: greetings, platform navigation, non-substantive clarifications, and responses that are purely procedural ("here's how to upload a document").

### Surface 2 — Free public tools at `/tools/*`

Two placements required:
1. **Tool page** (before the user begins): visible disclaimer on the tool's landing/entry page.
2. **Result page** (after the tool generates output): disclaimer in the result card.

Template:
> This tool provides general legal information only. It does not constitute legal advice and does not create an attorney-client relationship. Always consult a qualified lawyer before taking legal action.

### Surface 3 — Drafted documents (consumer surface)

Every AI-drafted document for a consumer user must include a footer line in the document itself:

> *Drafted with AI assistance. This document is a template and has not been reviewed for your specific situation. Review by qualified counsel is recommended before signing or filing.*

**For MENA**: consider adding the jurisdiction: "... qualified counsel in [KSA / UAE / Lebanon / etc.] recommended."

**Do not add** this footer for lawyer/eFirm surfaces — the lawyer is the qualified counsel and their firm's standard footer applies.

### Surface 4 — Lawyer / eFirm surfaces

**No disclaimer** — the user is the qualified professional. Adding an unnecessary disclaimer to a lawyer's professional tool is condescending and degrades the experience. The lawyer takes professional responsibility for all outputs they review and sign.

Exception: surface the **Heppner privilege disclaimer** ([[safety-ai-not-privileged-disclaimer-us-heppner]]) when appropriate — but that is a different issue from the information/advice disclaimer.

## Outcome-claims prohibition

The following types of statements are **never permitted** regardless of user type or surface:
- "You will win this case."
- "You are entitled to [specific sum]."
- "The court will rule in your favor."
- "This contract is definitely enforceable."
- "You have no liability here."

These constitute specific outcome predictions and are within the regulated advice space in virtually every jurisdiction. See [[messaging-outcome-claims-banned]].

## Jurisdiction-specific notes

The information/advice distinction is recognized in all major jurisdictions but with varying terminology:

| Jurisdiction | Term for regulated activity | Basis |
|-------------|---------------------------|-------|
| US (state bar) | Legal advice / legal services | State UPL statutes + ABA Rule 5.5 |
| UK | Reserved legal activities + legal advice | Legal Services Act 2007 |
| Lebanon | Conseil juridique / representation | Code of Civil Procedure + Bar Law |
| KSA | Legal representation / legal advice | Code of Law Practice M/38 |
| UAE (onshore) | Legal advice / legal services | Federal Law on Legal Profession |
| DIFC / ADGM | Legal services (regulated) | DFSA / FSRA conduct of business rules |
| France | Consultation juridique | Law of 31 December 1971 (as amended) |
| EU | Varies by member state | National bar codes + Legal Services Directive |

## Escalation from information to referral

When a user's question crosses clearly into advice territory:
1. Provide the information-level answer that is permissible.
2. State explicitly: "For the specific advice on your situation, you need a lawyer."
3. Offer to help prepare: "Want me to draft the key questions for your lawyer meeting?"

For criminal and serious civil matters: additionally surface [[safety-criminal-defense-disclaimer]] or the appropriate escalation path.

## Related skills

- [[safety-bar-rule-5-5-upl-ai]] — UPL obligations that require the information/advice line
- [[safety-unauthorized-practice-of-law-lb-ksa-uae]] — MENA-specific UPL rules
- [[safety-criminal-defense-disclaimer]] — stricter handling for criminal matters
- [[safety-medical-tax-financial-out-of-scope]] — deflection for non-legal professional domains
- [[conversation-disclaimer]] — conversational disclaimer implementation
- [[messaging-outcome-claims-banned]] — outcome-claims prohibition
