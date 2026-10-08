---
name: safety-attorney-work-product-ai-handling-sboghossian
title: Attorney Work-Product and AI — Handling Guide
description: Use when a lawyer user is preparing litigation materials, strategy memos, or other attorney work-product using AI assistance, and there is a risk that disclosure to the AI provider could waive work-product protection. Covers the conditions under which work-product doctrine protection survives AI-tool use, best practices for minimizing waiver risk, data-processing agreement requirements, and cross-border considerations for MENA and EU clients. Pairs with the Heppner privilege disclaimer.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/safety/safety-attorney-work-product-ai-handling
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Attorney Work-Product and AI — Handling Guide

## When this applies

Trigger when:
- A lawyer is using AI to prepare a litigation strategy memo, legal brief, internal analysis, or privileged communication about a client matter.
- A lawyer asks whether sharing client documents with an AI tool is "safe" from a privilege / work-product perspective.
- An enterprise legal team is evaluating AI vendors for work-product-sensitive tasks.
- A user asks about data residency, training data policies, or confidentiality of AI conversations.

## Work-product doctrine — essentials

The attorney work-product doctrine (US: FRCP 26(b)(3); UK: legal professional privilege; DIFC/ADGM: analogous under their Evidence Laws; MENA civil-law jurisdictions: siri mihna / professional secrecy concepts) protects from discovery materials prepared by or for an attorney in anticipation of litigation.

**Key condition for protection**: the material must remain confidential. Voluntary disclosure to a third party that is not under a duty of confidentiality can waive work-product protection.

**Does using an AI tool waive work-product protection?**

This depends on three factors:
1. **Contractual confidentiality**: does the AI vendor commit, by contract (DPA or enterprise agreement), not to use, disclose, or train on the content? If yes, the disclosure is arguably not to an adversarial third party.
2. **Training data policy**: consumer-grade AI tools often retain and may train on inputs — a clear waiver risk.
3. **Enterprise vs consumer deployment**: enterprise deployments with data-processing agreements (DPAs) and no-training clauses provide much stronger protection than consumer-grade tools.

The *Heppner* ruling (Feb 2026) addressed privilege rather than work-product specifically — [[safety-ai-not-privileged-disclaimer-us-heppner]] — but the same risk analysis applies: if an AI conversation is subpoenaed or ordered produced, both attorney-client privilege and work-product doctrine may be challenged.

## Best practices for work-product protection

### Before using AI for litigation work

1. **Verify the DPA**: confirm the AI vendor has executed a Data Processing Agreement that:
   - Prohibits use of data for model training.
   - Commits to confidentiality obligations.
   - Defines data retention and deletion.
   - Identifies the legal basis for processing and data residency.

2. **Check deployment type**: enterprise / private deployment (no data shared with other tenants, no training) is categorically safer than a shared consumer endpoint.

3. **Engagement letter disclosure**: update the firm's standard engagement letter to disclose that AI tools are used in matter work, that the tool is subject to a DPA, and what the client's rights are. This preserves attorney-client relationship and informed consent.

4. **Matter-level access controls**: ensure that only lawyers and staff assigned to the matter can access AI conversations about that matter.

### During AI-assisted work-product creation

- **Do not paste full unredacted client communications** into a consumer-grade AI tool. Rephrase in hypothetical or summarized form, or use a tool with enterprise confidentiality controls.
- **Prefer anonymization**: use [[safety-pii-redaction-before-rag]] to strip identifying details before sending to any third-party LLM endpoint.
- **Work product label**: mark AI-assisted drafts as attorney work product in the file management system.
- **Log access**: maintain an audit trail of who sent what to the AI tool ([[ops-audit-log-export]]).

### Cross-border data considerations

If client documents originated in:
- **EU**: GDPR Art. 28 requires a DPA with the AI vendor; cross-border transfer rules apply (SCCs) — see [[safety-cross-border-data-transfer-gcc-eu]].
- **KSA**: KSA PDPL Art. 29 requires contractual assurances before transferring to an AI vendor outside KSA.
- **UAE**: UAE PDPL Art. 22 requires contractual safeguards or UAE Data Office adequacy determination.
- **MENA cluster preference**: where available, request that client data be processed in an EU-West or ME-South region to minimize cross-border transfer obligations.

## What the platform guarantees (for enterprise-deployed instances)

- No training on tenant data — contractually committed.
- Tenant-isolated storage: no data leakage between tenants (see [[safety-client-confidentiality-cross-tenant]]).
- Cross-region data residency available for MENA clients.
- Access logs preserved per [[ops-audit-log-export]]; exportable for client disclosure if requested.
- PII redaction configurable per matter.

## Escalation

If a lawyer is unsure whether their work product may have been compromised:
1. Identify what was sent to the AI tool and whether the tool operates under a DPA with no-training clause.
2. Consult the firm's general counsel or ethics counsel.
3. For US matters: check the relevant state bar's ethics opinion on AI use — many bars have issued 2024–2025 opinions addressing this question.
4. Consider remediation: if material was sent to a consumer tool without protection, assess whether privilege/work-product can still be claimed and whether disclosure is required.

## Related skills

- [[safety-ai-not-privileged-disclaimer-us-heppner]] — Heppner ruling and privilege disclaimer
- [[safety-bar-rule-1-6-confidentiality-ai]] — Rule 1.6 confidentiality obligations
- [[safety-bar-rules-confidentiality]] — bar-rules confidentiality architecture
- [[safety-pii-redaction-before-rag]] — PII redaction before external LLM calls
- [[safety-cross-border-data-transfer-gcc-eu]] — cross-border data transfer obligations
- [[safety-client-confidentiality-cross-tenant]] — cross-tenant isolation
