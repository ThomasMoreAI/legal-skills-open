---
name: intel-us-court-ai-chats-not-privileged-heppner-sboghossian
title: 'Intel — US Court: AI Chats Not Privileged (Heppner v. Heppner)'
description: Use when a lawyer or user is about to paste privileged client information into an AI assistant, or when discussing the legal status of AI conversation logs under attorney-client privilege. Covers the Heppner v. Heppner (Feb 2026) federal court ruling that user-AI conversations are not protected by attorney-client privilege, practical implications for legal practice, privacy and redaction obligations, and what this means for AI legal tool design and usage policies across MENA and international jurisdictions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/intel/intel-us-court-ai-chats-not-privileged-heppner
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Intel — US Court: AI Chats Not Privileged (Heppner v. Heppner)

## Scope

**Heppner v. Heppner** (US federal court, February 2026) is a landmark ruling on the discoverability of AI-assisted legal work. The court held that conversations between a party (or their lawyer) and an AI assistant are **not protected by attorney-client privilege** and are subject to discovery in litigation. This knowledge pack explains the ruling, its immediate practical implications, the equivalent status across other jurisdictions, and what it means for AI legal tool design.

---

## The Heppner ruling

| Attribute | Detail |
|---|---|
| Case | Heppner v. Heppner |
| Court | US Federal Court (district; specific circuit not stated in source) |
| Date | February 2026 |
| Holding | User-AI conversations are NOT protected by attorney-client privilege |
| Consequence | AI chat content is discoverable in litigation |

### Core reasoning (inferred from holding)
Attorney-client privilege requires:
1. A communication
2. Between a lawyer and a client
3. Made in confidence
4. For the purpose of seeking or giving legal advice

An AI system is not a lawyer. Therefore, conversations with an AI — even if the user is seeking legal advice-like guidance — lack the lawyer/client element required for privilege. The AI provider's servers (or logs retained by the service) are not protected by any analog to the attorney work-product doctrine unless the AI conversation was part of a privileged lawyer-client communication (e.g., the lawyer drafted a prompt as part of providing advice, not merely using AI as a research tool).

---

## Practical implications for legal practice

### 1. AI prompt content is discoverable

If a party or lawyer inputs case facts, client confidences, or legal strategy into an AI tool, that input is not privileged:
- Discovery requests can seek "all AI chat logs relating to [matter]"
- The opposing party can demand production of what was asked of the AI and what it responded
- This includes: prompts, uploaded documents, AI responses, revision requests

### 2. Lawyer must treat AI prompts as non-confidential

Lawyers using AI tools must:
- Avoid pasting client-identifying information, confidential facts, or privileged strategy into AI systems
- Treat AI prompts as potentially discoverable documents from the outset of any matter
- Apply the same care to AI inputs as to emails, notes, or memos that would be discoverable

### 3. Redaction before AI input is now operationally critical

Best practice (post-Heppner):
- **Anonymize / pseudonymize** client names, counterparty names, and identifying deal terms before pasting into AI
- **Hypothetical framing**: "assume a company in [industry] has this fact pattern" rather than identifying the actual client
- **Output review**: confirm AI output does not contain client-identifying information before sharing or filing

### 4. Firm-level AI policies must be updated

Law firms should update AI usage policies to:
- Prohibit entry of unpseudonymized client data into third-party AI tools
- Define what client data can be used for AI prompting and with what safeguards
- Log AI tool usage for conflict checks and matter management
- Distinguish: enterprise AI with data isolation agreements (defensible) vs. consumer AI with no such agreements (higher risk)

---

## Enterprise AI vs. consumer AI distinction

The privilege and confidentiality risk differs:

| AI tool type | Data isolation | Heppner risk level |
|---|---|---|
| Enterprise API (Anthropic, OpenAI) with no-training agreement | Data not used for training; not logged in retrievable form by default | Lower (but not eliminated) |
| Consumer ChatGPT, Claude.ai (free) | Data may be retained and reviewed; no enterprise isolation | Higher |
| Firm-hosted on-premise AI | No third-party exposure | Lowest |
| Louis (BYO key model) | User's own Anthropic key; Anthropic API terms apply | Similar to enterprise API |

Note: even "no-training" agreements do not necessarily mean logs are inaccessible in litigation via subpoena. The safest practice is pseudonymization regardless of tool.

---

## Cross-jurisdictional status

Heppner is a US federal ruling; its direct effect is limited to US litigation. However, similar principles apply elsewhere:

| Jurisdiction | AI chat privilege status | Notes |
|---|---|---|
| US | Not privileged (Heppner, Feb 2026) | Discoverable in litigation |
| UK | Likely not privileged | No equivalent ruling yet; legal advice privilege requires a lawyer; AI is not one |
| DIFC / ADGM | Likely not privileged | English common-law framework; same analysis as UK |
| UAE (onshore) | No specific ruling; civil law | Discovery is more limited in UAE civil procedure; but AI logs not equivalent to attorney communications |
| KSA | No specific ruling | Islamic law + civil procedure; confidentiality protections apply; AI privilege status unclear |
| LB | No specific ruling | Civil law; attorney-client confidentiality protected by Lawyers Statute; AI not a lawyer |
| EG | No specific ruling | Civil procedure; attorney confidentiality under Lawyers Regulation Law; AI not covered |
| EU | Not privileged; GDPR overlay | GDPR adds data retention and purpose limitation constraints on AI providers |

**MENA practitioner takeaway**: While no MENA court has issued a Heppner-equivalent ruling, the underlying logic applies universally — AI is not a lawyer, so conversations with AI lack the professional-relationship element of privilege in any jurisdiction.

---

## Implications for Louis design

Heppner creates an affirmative obligation for legal AI platforms:

1. **Privilege disclaimer on client-data input**: Louis should surface a reminder when a user appears to be pasting case-specific client information: "AI chats with legal assistants are not attorney-client privileged. Consider anonymizing client details before input."

2. **Pseudonymization assistant**: Louis can offer to help the user pseudonymize a document before analysis — replacing names, company identifiers, and matter-specific details with generic placeholders.

3. **No-log mode**: for enterprise customers, offer a documented no-log or minimal-log configuration to reduce discoverable footprint.

4. **Clear output labeling**: Louis output is not privileged legal advice — this must be stated, not assumed.

The companion skill [[safety-ai-not-privileged-disclaimer-us-heppner]] governs the specific behavioral response when Louis detects potential privilege-sensitive input.

---

## What to do when you see a user pasting sensitive client data

1. Surface the Heppner-aware disclaimer: "AI conversations are not attorney-client privileged. If this matter is in litigation or likely to be, consider using only anonymized facts."
2. Offer pseudonymization: "Want me to help you anonymize the client and party names before proceeding?"
3. Proceed with analysis if user consents, and flag in the output that the response is based on pseudonymized/anonymized facts.

---

## Related skills

- [[safety-ai-not-privileged-disclaimer-us-heppner]]
- [[safety-confidentiality-wall]]
- [[intel-anthropic-claude-for-word]]
- [[kb-professional-conduct-ai]]
