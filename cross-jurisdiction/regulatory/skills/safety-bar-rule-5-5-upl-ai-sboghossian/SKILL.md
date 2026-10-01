---
name: safety-bar-rule-5-5-upl-ai-sboghossian
title: Bar Rule 5.5 — Unauthorized Practice of Law and AI
description: Use when assessing whether AI-generated legal output may constitute unauthorized practice of law (UPL) in a given jurisdiction, or when configuring the appropriate output mode (consumer-informational vs. lawyer-supervised) for a given user. Covers ABA Model Rule 5.5 and its analogs in US states, Lebanon, Saudi Arabia, UAE (onshore and DIFC/ADGM), UK, and France. Defines the line between permissible legal information and impermissible legal advice, and the acts AI must never perform (court appearance, pleading filing, client representation).
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/safety/safety-bar-rule-5-5-upl-ai
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: regulatory
language: en
---

# Bar Rule 5.5 — Unauthorized Practice of Law and AI

## When to use this

Apply when:
- Configuring output mode for a new user whose professional role is unknown or consumer.
- A user asks the AI to represent them, file documents on their behalf, or establish a client relationship.
- A user asks whether AI can "be their lawyer."
- A user attempts to submit AI-generated pleadings without lawyer sign-off.
- A compliance review of the AI product is assessing UPL exposure.

## The UPL rule — what it prohibits

### ABA Model Rule 5.5 (US)
Rule 5.5(a): "A lawyer shall not practice law in a jurisdiction in violation of the regulation of the legal profession in that jurisdiction, or assist another in doing so."

The rule, combined with state-specific UPL statutes, means that an AI system that provides specific legal advice — as opposed to general legal information — to a consumer without lawyer supervision may constitute UPL by the AI provider or the deploying organization.

**The advice/information distinction** is the critical line:
- **Legal information**: explaining what the law generally says, how a process works, what documents are typically needed — this is not UPL.
- **Legal advice**: applying the law to a specific person's facts and telling them what to do — this is regulated legal services in most jurisdictions.

### Variation by US state
UPL definitions vary significantly:
- **Narrow states** (e.g., some southwestern states): UPL applies primarily to court representation; document preparation services occupy a gray zone.
- **Broad states** (e.g., some northeastern states): UPL can extend to any advice on legal rights and obligations.
- **LegalZoom / online legal services**: the US has struggled with the line between document-prep services and legal advice; outcomes vary by state and court.

## MENA jurisdiction rules

### Lebanon — Law of the Bar (Qanun Niqabat al-Muhamin)
- Only inscribed members of the Beirut Bar Association or regional bars (Tripoli, etc.) may represent clients before Lebanese courts.
- Document preparation and legal information provision are not per se UPL in Lebanon, but appearing in court as a representative or signing legal submissions as counsel requires bar inscription.
- AI-generated court documents must be signed by inscribed counsel before filing.

### Saudi Arabia — Code of Law Practice (Royal Decree M/38)
- Pleading before Saudi courts is restricted to licensed Saudi lawyers; foreign lawyers may only appear under registered partnerships.
- The Ministry of Justice (MOJ) has specific e-filing systems that require a registered lawyer's credentials.
- Sharia-court matters require Sharia-qualified counsel.
- AI tools may draft; licensed lawyers must sign and file.

### UAE — Federal Law on the Legal Profession + Emirate Bars
- Representation in onshore UAE courts: restricted to UAE-national lawyers or lawyers with UAE licensing.
- DIFC Court: permits non-national practitioners registered before the court.
- ADGM Court: similar to DIFC; registered practitioners only.
- Corporate document filings (company formation, regulatory submissions) often require licensed counsel countersignature.

## European rules

### UK — SRA Code of Conduct / Legal Services Act 2007
Legal activities (including exercising a right of audience, conducting litigation, and providing legal advice) are regulated under the Legal Services Act 2007. Providing these as a "business" without authorization is a criminal offense.

AI tools may assist lawyers; they may not autonomously provide regulated legal services or establish client relationships.

### France — Règlement Intérieur National (RIN) / Code de Procédure Civile
Representation before French courts (postulation, plaidoirie) is reserved for registered avocats. AI-drafted submissions must be signed by an avocat inscrit. Consultation juridique for fee is also restricted to authorized professionals under Law No. 71-1130.

## What AI can and cannot do

### Permitted (everywhere)
- Providing general legal information — explaining how contract formation works, what an NDA is, how to read a court timeline.
- Drafting template documents for the user's review and a licensed lawyer's final sign-off.
- Research and analysis that a lawyer reviews and adopts.
- Procedural information — how to file, what forms exist, what deadlines apply generally.
- Helping users prepare questions for their lawyer.

### Never permitted (anywhere)
- Representing a user in court proceedings — appearing as counsel, submitting pleadings as the user's legal representative.
- Filing documents in official systems as the user's lawyer of record.
- Establishing an attorney-client relationship.
- Giving binding legal advice in a jurisdiction that requires a license for that activity (i.e., telling a specific user "you should sue X" or "you will win").

## Surface-specific modes

| User surface | Output mode | Rationale |
|-------------|-------------|-----------|
| Consumer public chat | Informational only; disclaimer on every substantive response | UPL risk; user not a licensed lawyer |
| Free public tools | Informational + template; disclaimer on tool page and result | UPL risk; anonymous consumer |
| Lawyer / eFirm surface | Professional B2B; lawyer is the licensed professional | Lawyer is the qualified counsel; AI is the tool |
| In-house counsel | Professional B2B; counsel is the qualified professional | Same as eFirm; counsel signs off |

See [[safety-no-legal-advice-disclaimer-rules]] for the full disclaimer surface-rules.

## Edge case — supervised AI in law firms

The US and UK have both developed frameworks for supervised AI use in law firms (similar to "supervised practice" for law students). AI-generated work that is reviewed, verified, and signed off by a licensed attorney does not constitute UPL — the lawyer is practicing law using an AI tool. This is the eFirm model: the lawyer supervises and signs; the AI drafts and researches.

## Refusal language

If a user asks AI to be their lawyer of record, appear in court, or perform a reserved legal activity:
> I can help you understand your options and prepare materials, but I'm not able to be your lawyer. I can't file documents as your legal representative, appear in court on your behalf, or give you binding legal advice. For your specific situation, you'll need a licensed [lawyer / avocat / muhami] in [jurisdiction]. Would you like help preparing your questions for them?

## Related skills

- [[safety-unauthorized-practice-of-law-lb-ksa-uae]] — jurisdiction-specific UPL rules for LB, KSA, UAE
- [[safety-no-legal-advice-disclaimer-rules]] — disclaimer surface rules
- [[safety-bar-rule-1-1-competence-ai]] — competence obligations for AI use
- [[safety-criminal-defense-disclaimer]] — stricter handling for criminal matters
- [[conversation-refusal-policy]] — refusal patterns for out-of-scope requests
