---
name: safety-compliance-ai-not-privileged-disclaimer-us-sboghossian
title: AI Not-Privileged Disclaimer — US
description: Use when generating legal work product using AI for US-jurisdiction matters or advising US-based law firms on disclosure obligations. Governs when and how to disclose AI assistance in the engagement letter, matter file, and client communications so that attorney-client privilege and attorney work-product doctrine are not inadvertently waived. Provides model disclosure language for engagement letters and internal matter documentation protocols.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/safety-compliance/safety-compliance-ai-not-privileged-disclaimer-us
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
---

# AI Not-Privileged Disclaimer — US

## When This Applies

Apply this skill whenever:
- An attorney licensed in a US jurisdiction is using Louis to assist with a client matter
- The AI-assisted work product may be reviewed in a US court or regulatory proceeding
- The firm needs to disclose AI use in its engagement letter or retainer
- A client asks whether AI use affects the confidentiality or privilege status of communications

This skill is specifically for US privilege doctrine. MENA jurisdictions have their own professional responsibility frameworks — for those, see relevant MENA bar association rules.

## The Privilege Problem

Attorney-client privilege (ACP) and the attorney work-product doctrine (WPD) are two distinct protections:

**Attorney-client privilege**: protects confidential communications between a lawyer and client made for the purpose of obtaining or giving legal advice. The privilege belongs to the client and can be waived.

**Work-product doctrine** (Hickman v. Taylor, 329 US 495 (1947); codified in FRCP Rule 26(b)(3)): protects materials prepared by or for an attorney in anticipation of litigation or for trial. Core work product (mental impressions, conclusions, opinions) receives near-absolute protection.

**The AI vendor disclosure risk**: when a law firm transmits client information to a third-party AI vendor for processing, this could constitute a disclosure to a third party that waives privilege. Whether it does depends on:

1. **The "functional equivalent" test** (derived from *Upjohn Co. v. United States*, 449 US 383 (1981) principles): if the AI tool functions as the equivalent of an agent or functional assistant of the attorney, its use may not constitute a waiver. Courts have not yet uniformly resolved whether AI providers meet this test.

2. **Confidentiality agreement with the AI vendor**: if the vendor has contractually committed to keeping client information confidential and not using it for any purpose beyond providing the service (including not training models on client data), this strengthens the argument that no waiver occurred.

3. **Absence of actual third-party access**: if the AI operates in a fully isolated, tenant-specific environment where the vendor's employees have no access to the specific client communications, the risk of inadvertent waiver is reduced.

4. **Circuit-specific analysis**: the "common interest" and "necessity" exceptions to privilege waiver vary by US federal circuit. The safest approach is to document the firm's AI use policy in advance rather than relying on post-hoc judicial determinations.

## Louis's Architecture (Relevant Context)

Louis at the enterprise tier operates as:
- **No-training**: client data is not used to train or fine-tune any AI model
- **Tenant isolation**: each firm's data is logically separated from other tenants
- **Contractually bound**: the vendor agreement confirms that Louis's operator will not access, disclose, or process client data outside the scope of providing the service

This architecture supports the argument that Louis, as used in the enterprise tier, is functionally equivalent to an agent of the firm for purposes of privilege analysis. However, US courts have not yet issued definitive rulings on AI-assisted legal work and privilege — counsel should treat this as an evolving area and include express written disclosures to be safe.

## Required Disclosure Protocol

### 1. Engagement Letter Disclosure

Include the following in every new client engagement letter where AI tools will be used:

> "The Firm uses artificial intelligence tools, including [identify tool], to assist attorneys with legal research, document review, and drafting. These tools operate under enterprise-tier agreements that prohibit the AI vendor from training on or disclosing client data. The AI tools serve as attorney assistants in the provision of legal services. The Firm's use of AI tools does not constitute disclosure of confidential information to a third party for privilege or work-product purposes and does not waive attorney-client privilege or the work-product doctrine. Client consents to the Firm's use of AI tools in connection with this engagement. Client may opt out of AI-assisted work by providing written notice to the Firm, in which case the Firm will provide the same legal services without AI assistance, which may affect timing and cost."

### 2. Matter File Documentation

For each matter where AI-assisted work product is generated, the supervising attorney should record in the matter file:
- The date and nature of AI assistance used
- A statement confirming that the output was reviewed and approved by a licensed attorney
- Any AI-generated content that was incorporated into advice delivered to the client should be noted as "prepared with AI assistance, reviewed and approved by [attorney name]"

### 3. Privilege Log Entries

If the matter proceeds to litigation and a privilege log is required, AI-assisted documents should be logged as:
- Author: "[Attorney Name] with AI assistance"
- Description: "Attorney work product prepared with AI assistance; mental impressions of [attorney] are the controlling work product"

### 4. Professional Responsibility Compliance

US state bar authorities are issuing guidance on AI use. As of this skill's baseline:
- **California State Bar**: issued formal guidance requiring competency in AI tools used for client matters; disclosure of AI use recommended
- **New York State Bar**: issued ethics opinion recommending disclosure of AI use where it would be material to the client
- **ABA**: issued formal opinion 512 (2024) addressing competence, confidentiality, and supervision obligations when using AI tools

The supervising attorney must:
1. Have competency in the AI tool being used (understand its outputs and limitations)
2. Review and supervise AI-generated output before delivering it as legal advice
3. Not charge clients for AI-generated work product as if it were attorney time (billing ethics)
4. Disclose AI use when required by applicable bar rules

## Consumer / Non-Enterprise Context

On consumer-facing surfaces (non-enterprise, non-authenticated), Louis is not operating as an attorney's tool — it is providing information, not legal advice. The privilege analysis does not directly apply. However:

- Louis should still include the standard "this is not legal advice" disclaimer in responses to US users
- Louis should still escalate to [[router-escalation]] for high-stakes legal questions where a US-licensed attorney is needed

## When to Cite This Skill

Invoke the disclosure protocol whenever:
- A US-licensed attorney is starting a new client engagement and asks about AI use disclosure
- A client questions whether AI use affects confidentiality
- A matter moves to litigation and a privilege log is being prepared
- A bar disciplinary issue or ethics inquiry arises about AI use in the representation

## Related Skills

- [[safety-compliance-attorney-work-product-ai-handling]]
- [[safety-compliance-client-data-retention-mena-rules]]
- [[router-confidence-scorer]]
- [[router-escalation]]
