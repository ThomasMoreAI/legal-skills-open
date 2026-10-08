---
name: safety-compliance-attorney-work-product-ai-handling-sboghossian
title: Attorney Work-Product AI Handling
description: Use when a law firm or legal team needs to handle AI-generated work product consistently with attorney work-product doctrine and professional confidentiality obligations across multiple jurisdictions. Covers the five core principles — enterprise-only AI, engagement letter disclosure, matter file documentation, data residency for MENA matters, and avoiding consumer-grade AI for privileged work. Applies to any jurisdiction where attorney work-product doctrine or professional secrecy rules protect litigation preparation materials.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/safety-compliance/safety-compliance-attorney-work-product-ai-handling
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Attorney Work-Product AI Handling

## When This Applies

Apply this skill whenever a law firm or in-house legal team uses AI to assist with:
- Litigation preparation (pleadings, memoranda, discovery analysis, deposition prep)
- Legal advice communications with clients that may later be subject to privilege review
- Work involving confidential client information of any nature

This skill establishes the five-principle framework for safe AI use in a legal professional context. It applies regardless of jurisdiction — the specific privilege doctrine name varies, but professional secrecy / client confidentiality obligations exist in every jurisdiction in the supported set.

## The Five Principles

### Principle 1 — Use Enterprise AI with No-Training and Tenant Isolation

**Why**: Consumer-grade AI (e.g., a free-tier chat interface) typically trains on user inputs. A lawyer submitting a client's confidential memorandum to a consumer AI that uses the input to improve its model has potentially disclosed that client's confidential information to the AI vendor's infrastructure — a serious professional responsibility breach.

**The standard**: only use AI in the legal context where:
- The vendor contractually commits to **not training** on client data
- Client data is stored and processed in **tenant-isolated** infrastructure (not shared across users)
- The vendor has **data processing agreements** (DPAs) compliant with applicable privacy laws (GDPR, KSA PDPL, UAE PDPL, DIFC DPL)
- The vendor's security practices are documented and auditable (SOC 2, ISO 27001, or equivalent)

**In practice**: Louis at the enterprise tier meets this standard. Free-tier or unauthenticated use does not. Never use unauthenticated AI sessions for client-specific work.

### Principle 2 — Disclose AI Use in the Engagement Letter

**Why**: Most jurisdictions' professional responsibility rules require lawyers to obtain informed consent before taking actions that materially affect the representation. Using AI tools that process client information is such an action.

**The standard engagement letter disclosure** (adapt to jurisdiction-specific requirements):

> "Firm uses AI tools, including [name/type of tool], to assist attorneys in legal research, document drafting, and analysis. AI tools are operated under enterprise agreements requiring the AI vendor to maintain strict confidentiality, not to train on client data, and not to disclose client information. AI-assisted work product is reviewed and supervised by a licensed attorney before delivery to Client. Use of AI tools does not constitute disclosure to a third party for purposes of attorney-client privilege or professional secrecy. Client may opt out of AI-assisted work by written notice to Firm."

**MENA-specific note**: professional secrecy (سر المهنة in Arabic; secret professionnel in French) is a fundamental obligation under bar rules in Lebanon, KSA, UAE, and Egypt. Engagement letter disclosure of AI tool use should be included in all matters, as bar associations in these jurisdictions are developing guidance on AI in legal practice.

### Principle 3 — Log AI-Assisted Work in the Matter File

**Why**: In litigation, AI-assisted documents may need to appear on a privilege log. In professional responsibility proceedings, the attorney must be able to demonstrate supervision of AI output. In billing disputes, the attorney must be able to demonstrate the value of the work.

**Documentation standards**:

For each piece of AI-assisted work product incorporated into advice or pleadings:

| What to record | Where | How |
|---|---|---|
| That AI was used | Matter file note | "AI assistance used for [description]; reviewed by [attorney] on [date]" |
| Which AI tool was used | Matter file | Tool name and enterprise tier/version |
| That the output was reviewed by a licensed attorney | Matter file note | Supervising attorney's initials and date |
| Any material AI hallucination caught and corrected | Matter file | Note the error and correction; important for quality control patterns |

If the matter moves to US litigation: AI-assisted documents on the privilege log should be described as "[Type] prepared with AI assistance; supervised and approved by [attorney name]; protected as attorney work product." This documentation demonstrates attorney involvement and prevents the argument that the work product was "generated by an AI" and therefore lacks human authorship.

### Principle 4 — Avoid Consumer-Grade AI for Privileged Work

**Categories of AI that should never be used for privileged legal work**:

- Free-tier chat interfaces where the provider trains on user inputs
- AI accessed through a personal (non-firm) account with no enterprise data agreements
- AI interfaces where the user cannot verify tenant isolation
- Shared AI tools where multiple users' queries may cross-contaminate

**Practical test**: if you would not forward a client email to a random third party for analysis, do not submit client information to an AI product that you cannot verify operates under a no-training, tenant-isolated enterprise agreement.

**When traveling or using personal devices**: use only firm-provisioned AI tools on firm-managed devices or through firm VPN/secure access. The same client confidentiality rules apply on personal devices.

### Principle 5 — Data Residency for MENA Matters

**Why**: KSA PDPL, UAE PDPL, and DIFC Data Protection Law restrict the cross-border transfer of personal data. Client data from MENA matters may include personal data of individuals (their contracts, communications, health information). Processing this data on servers located outside the applicable jurisdiction requires a lawful transfer mechanism.

**Practical requirements**:

| Matter jurisdiction | Data residency requirement |
|---|---|
| KSA | Client data should be processed in a KSA or GCC-region server; cross-border transfer to US/EU servers requires a PDPL-compliant transfer mechanism |
| UAE (onshore) | UAE PDPL cross-border transfer rules apply; adequacy or contractual safeguards required |
| DIFC | DIFC Data Protection Law Art. 26: data may be transferred only to adequate countries or with appropriate safeguards |
| EU (GDPR) | Standard Contractual Clauses or adequacy decision required for transfer outside EEA |
| Lebanon | Data protection law is pending; general professional secrecy principles apply |

When using Louis for MENA matters: ensure the enterprise agreement specifies the server region for data storage and processing. If the enterprise agreement does not include MENA-region hosting, flag this for the IT/compliance team.

## Summary Checklist

For each new matter where AI assistance will be used:

- [ ] Confirm AI tool is enterprise-tier with no-training + tenant isolation
- [ ] Confirm data processing agreement (DPA) is in place with the vendor
- [ ] Include AI disclosure in the client engagement letter before first AI-assisted work
- [ ] Identify the applicable data residency requirement and confirm compliance
- [ ] Brief the supervising attorney on AI supervision obligations
- [ ] Confirm matter file documentation protocol is in place

## Professional Responsibility Note

This skill summarizes general principles. Bar rules on AI use are evolving rapidly — in particular:
- The ABA's Formal Opinion 512 (2024) on generative AI
- State bar ethics opinions (California, New York, Florida, and others)
- UAE Federal Bar Association and Lebanese Bar Association developing guidance
- DIFC Legal Services Regulatory Authority: no specific AI guidance as of this baseline

Supervising attorneys are responsible for staying current with their bar's guidance. This skill provides a baseline; local counsel should verify against the most current professional responsibility rules.

## Related Skills

- [[safety-compliance-ai-not-privileged-disclaimer-us]]
- [[safety-compliance-client-data-retention-mena-rules]]
- [[router-confidence-scorer]]
- [[router-escalation]]
