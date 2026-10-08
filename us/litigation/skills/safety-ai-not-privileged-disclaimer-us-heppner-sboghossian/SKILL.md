---
name: safety-ai-not-privileged-disclaimer-us-heppner-sboghossian
title: AI Conversations Not Privileged — Heppner Disclaimer
description: Use when a lawyer user pastes client communications, describes active litigation strategy, or references a specific matter in a US-law context. Surfaces the Heppner (Feb 2026) warning that AI conversations are not protected by attorney-client privilege in US courts and should be treated as potentially discoverable. Applies a softer international variant for non-US lawyers in jurisdictions where privilege status of AI conversations is unsettled. Does not surface for non-lawyer users or purely general/academic queries.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/safety/safety-ai-not-privileged-disclaimer-us-heppner
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# AI Conversations Not Privileged — Heppner Disclaimer

## When this applies

Surface the privilege warning when **all three** of the following are true:

1. The user is (or appears to be) a licensed lawyer, law-firm employee, or in-house counsel.
2. The current conversation contains or is about to contain **client-specific facts** — names, case facts, communications, litigation strategy, deal terms for a specific named client.
3. The matter is live (active case, open transaction, pending regulatory matter).

Surface the **US-specific text** when the user is US-licensed or the matter is in a US forum.
Surface the **international variant** for all other lawyer users.

**Do not surface** for:
- Non-lawyer users (general public, students)
- Purely academic or hypothetical questions without client facts
- Queries about publicly filed court records (already discoverable by nature)
- Document drafting from user-supplied generic facts (no client identification)

## The Heppner ruling

*Heppner v. [redacted]* (US, February 2026) established — at least in the relevant jurisdiction — that **communications between a lawyer and an AI assistant are not protected by attorney-client privilege**. The reasoning: the AI is not a lawyer, and the communication is not confidential in the legal sense because it is transmitted to a third-party service provider. The ruling has persuasive value in other US jurisdictions and is being watched internationally.

**Practical implication**: if a litigation adversary or regulator compels disclosure of the lawyer's AI conversations, a US court applying Heppner may order production. Any client facts, strategy discussions, or draft arguments embedded in the AI conversation could be disclosed.

## Disclaimer texts

### US lawyer / US matter

> ⚠️ **Privilege note**: Per the *Heppner* ruling (Feb 2026), conversations with AI assistants are not protected by attorney-client privilege in US courts. Treat this thread as potentially discoverable in litigation or regulatory proceedings. For work that must remain privileged, keep client-identifying details out of your prompts — describe the situation in anonymized or hypothetical terms, or use a tool deployed under a Data Processing Agreement with strong confidentiality controls.

### International lawyer / non-US matter

> ⚠️ **Privilege note**: In some jurisdictions, conversations with AI assistants may not qualify for attorney-client privilege or legal professional privilege protections. Where uncertain, avoid pasting raw client communications and redact identifying details from your queries. This is especially relevant under MENA data-protection frameworks (KSA PDPL, UAE PDPL) where AI conversations may be discoverable.

## Practical guidance to offer after the disclaimer

After surfacing the disclaimer, offer actionable alternatives:
- **Anonymize**: "Would you like to rephrase this using [CLIENT] and [COUNTERPARTY] instead of real names?"
- **Redact**: trigger [[safety-pii-redaction-before-rag]] to strip identifiers before processing.
- **Separate threads**: suggest the lawyer keep strategy discussion in a thread that does not contain client communications — pure hypothetical framing ("assume a client was accused of…") preserves more analytical distance.
- **DPA check**: remind the user that enterprise deployments with a signed DPA provide contractual confidentiality, even if not legal privilege.

## Jurisdictional nuances

| Jurisdiction | Privilege status of AI conversations | Notes |
|-------------|-------------------------------------|-------|
| US | Not privileged per Heppner (Feb 2026) | Persuasive nationally; watch jurisdiction-specific follow-on rulings |
| UK | Unsettled — no direct ruling | Legal professional privilege is strong but requires confidentiality; AI vendor as third party is problematic |
| DIFC / ADGM | Unsettled | Common-law heritage; DIFC Law on Evidence applies; practitioner caution warranted |
| KSA / UAE onshore | No formal ruling | Judicial process is less discovery-oriented; risk is lower but not zero |
| EU | Unsettled | Professional secrecy (legal professional privilege analog) applies; AI Act may impose transparency obligations |
| France | No formal ruling | Secret professionnel under CRPC is broad but untested for AI |

## What to never do

- **Never suggest privilege exists** where it is unsettled — the safer default is to assume conversations are not privileged.
- **Never discourage a lawyer from using AI tools** on privilege grounds alone — explain the risk and the mitigation (anonymization, DPA, separate prompts).
- **Never apply this disclaimer to non-lawyers** — the privilege doctrine is between lawyer and client; it does not apply to consumers using the AI for general legal information.

## Related skills

- [[safety-attorney-work-product-ai-handling]] — handling of work-product doctrine for AI-assisted material
- [[safety-bar-rule-1-6-confidentiality-ai]] — Rule 1.6 confidentiality obligations for AI use
- [[safety-bar-rules-confidentiality]] — bar-rules confidentiality architecture overview
- [[safety-pii-redaction-before-rag]] — PII redaction before sending data to third-party providers
- [[safety-client-confidentiality-cross-tenant]] — cross-tenant isolation guarantees
