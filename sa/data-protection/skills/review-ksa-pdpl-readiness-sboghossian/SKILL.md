---
name: review-ksa-pdpl-readiness-sboghossian
title: KSA PDPL Readiness Review
description: Use when assessing a contract, data-processing agreement, DPIA, or organizational practice for compliance readiness against Saudi Arabia's Personal Data Protection Law (PDPL). Covers lawful-basis mapping, data subject rights obligations, cross-border transfer rules, DPO appointment thresholds, breach notification timing, ROPA requirements, and sensitive data handling — all with reference to the SDAIA regulatory framework effective September 2024.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-ksa-pdpl-readiness
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: sa
practice: data-protection
language: en
---

# KSA PDPL Readiness Review

## When to use this

Use this skill when:
- A Saudi-established or Saudi-targeting organization needs to assess PDPL compliance
- Reviewing a commercial contract that involves processing personal data of Saudi residents
- Drafting or reviewing a data-processing agreement (DPA) for a KSA-based operation
- Preparing a Data Protection Impact Assessment (DPIA) for a high-risk processing activity
- Conducting due diligence on a KSA acquisition where data-handling practices are in scope

Pair with [[draft-privacy-policy-mena]] for consumer-facing privacy notice work, and with a UAE PDPL review where the organization operates across both GCC jurisdictions.

## Regulatory Framework

Saudi Arabia's Personal Data Protection Law was issued by Royal Decree M/19 on 9 Sha'ban 1443H (corresponding to 11 March 2022). It entered into force in September 2023 with a grace period, and enforcement by SDAIA (Saudi Data & AI Authority) became active in September 2024.

Key instruments:
- **PDPL** (Royal Decree M/19): the primary statute
- **PDPL Implementing Regulations**: issued by SDAIA; provide granular requirements
- **SDAIA Guidelines and Circulars**: sector-specific guidance (health, financial, government)
- **Cross-Border Data Transfer Framework**: adequacy determinations and alternative mechanisms

SDAIA is the competent supervisory authority. Violations can result in fines of up to SAR 5,000,000 and criminal liability for intentional violations.

## Review Methodology

Work through the following checklist. For each item, document the current state, any gap, and a remediation path.

### 1. Lawful Basis

The PDPL recognizes the following lawful bases for processing (narrower than GDPR's six):

| Basis | Conditions |
|---|---|
| Consent | Explicit, specific, informed, and capable of withdrawal without detriment |
| Contract | Processing necessary for performance of a contract with the data subject |
| Legal obligation | Processing required by Saudi law or regulation |
| Vital interests | Necessary to protect life or health of the data subject or a third party |
| Legitimate interests | More narrowly construed than GDPR Article 6(1)(f); subject to SDAIA guidance |
| Public task | For government entities processing in exercise of official authority |

Flag: (a) reliance on "legitimate interests" without a documented balancing test — SDAIA takes a narrow view; (b) consent obtained without a mechanism for withdrawal; (c) bundled consent (consent for multiple purposes in a single checkbox).

### 2. Data Subject Rights

The PDPL grants the following rights that must be operationally supported:

| Right | Response timeframe | Notes |
|---|---|---|
| Right of access | Specified in implementing regulations | Must be provided in Arabic if requested |
| Right of rectification | Specified in implementing regulations | Must notify downstream processors |
| Right of erasure | Specified in implementing regulations | Subject to retention obligations under Saudi law |
| Right to data portability | Available in certain categories | Narrower than GDPR — check implementing regs |
| Right to object to automated decisions | Including profiling | Must offer human review |

Operational check: does the organization have a documented process (with response SLAs) for each right? Is the request intake mechanism available in Arabic?

### 3. Cross-Border Data Transfers

The PDPL restricts transfer of personal data outside KSA unless one of the following applies:

- **Adequacy decision**: SDAIA has published a list of countries with adequate data protection (check current SDAIA registry — list subject to update)
- **Controller assurances**: the receiving controller provides contractual guarantees at least equivalent to the PDPL (analogous to GDPR Standard Contractual Clauses — SDAIA has issued model clauses)
- **Vital interests / legal claims**: transfer necessary to protect the data subject's life or to establish or defend legal claims
- **Public interest**: limited to government transfers

Practical implications:
- US, EU, UK, UAE: adequacy status must be verified against current SDAIA list
- Cloud service providers with servers outside KSA: ensure DPA includes SDAIA-approved transfer mechanism
- MENA multi-jurisdiction: if data flows from KSA to UAE and then to EU, each hop requires its own lawful transfer basis

### 4. Data Protection Officer (DPO) Appointment

DPO appointment is mandatory for:
- Organizations that process sensitive data at scale
- Organizations that process data of more than a specified threshold (see implementing regulations for current numerical threshold)
- Organizations whose core activities involve systematic monitoring of data subjects

Flag if: organization processes health, biometric, genetic, racial/ethnic, religious, or criminal data and has no designated DPO; DPO lacks adequate independence; DPO role is bundled with conflicting responsibilities (e.g., head of IT also serving as DPO).

### 5. Sensitive Data Handling

The PDPL defines sensitive data to include:

- Health and medical data
- Genetic and biometric data
- Racial or ethnic origin
- Religious beliefs or practices
- Criminal records or convictions
- Financial data beyond general income information
- Location data that could reveal sensitive patterns

Requirements for sensitive data: explicit consent (not just consent); higher security standards; in some categories, prohibition on processing unless strictly necessary.

### 6. Privacy Notices

A PDPL-compliant privacy notice must include:

- Identity and contact information of the controller
- Categories of personal data processed
- Purpose(s) of processing with lawful basis for each
- Recipients and cross-border transfer disclosures
- Retention period or criteria for determining retention
- Data subject rights and how to exercise them
- Contact details for SDAIA complaint channel

Notice must be in Arabic (or bilingual Arabic-English if serving both audiences). Plain language is required — dense legal boilerplate does not satisfy the "informed consent" standard.

### 7. Breach Notification

The PDPL requires notification to SDAIA within **72 hours** of becoming aware of a personal data breach that is likely to result in harm to data subjects. This mirrors GDPR timing. Additionally:

- Data subjects must be notified if the breach is likely to cause serious harm
- The breach record must be maintained internally
- The notification to SDAIA must include: nature of breach, categories and approximate number of data subjects affected, likely consequences, measures taken or proposed

Flag any contract or DPA that: (a) requires the processor to notify the controller in a timeframe that does not allow the controller to meet the 72-hour SDAIA window; (b) places breach notification costs entirely on the processor without indemnification alignment.

### 8. Records of Processing Activities (ROPA)

Organizations must maintain ROPA equivalent records documenting:

- Purposes of processing for each category
- Categories of data subjects and personal data
- Recipients including cross-border recipients
- Retention schedules
- Security measures

Flag if: no ROPA exists; ROPA is outdated and does not reflect current systems; ROPA is not accessible to SDAIA on request.

### 9. Data Processor Obligations

The PDPL imposes direct obligations on data processors (not just controllers), similar to GDPR. A compliant DPA between controller and processor must include:

- Processing only on documented instructions of the controller
- Confidentiality obligations on all persons authorized to process
- Implementation of appropriate technical and organizational security measures
- Notification obligations for breach
- Conditions for engaging sub-processors (controller approval; flow-down of obligations)
- Cooperation with SDAIA audits
- Deletion or return of data on termination

## What to Flag

| Severity | Issue |
|---|---|
| Critical | Processing sensitive data without explicit consent and no alternative lawful basis |
| Critical | Cross-border transfers with no lawful transfer mechanism |
| Critical | No breach notification procedure or timeline inconsistent with 72-hour rule |
| Critical | DPO appointment obligatory but not made |
| High | Privacy notice missing or non-compliant (not in Arabic; missing required fields) |
| High | Data subject rights process absent or response SLAs undocumented |
| High | No ROPA maintained |
| Medium | Consent mechanism lacks withdrawal functionality |
| Medium | Sub-processor list not maintained; no controller approval for new sub-processors |
| Low | Retention periods not documented per data category |

## Output Format

```json
{
  "gaps": [
    {
      "requirement": "<PDPL article or implementing reg reference>",
      "current_state": "<description>",
      "severity": "critical|high|medium|low",
      "remediation": "<action required>"
    }
  ],
  "readiness_score": 0-100,
  "critical_actions": [
    "<immediate actions required>"
  ],
  "dpo_required": true/false,
  "cross_border_transfers_identified": true/false,
  "sensitive_data_categories_present": ["health", "biometric", ...]
}
```

## Limits and Escalation

- SDAIA guidance evolves; verify adequacy determination list against current SDAIA portal before advising on cross-border transfers
- Sector-specific rules (healthcare, financial, government) may impose stricter requirements — escalate for sector-specific advice
- Criminal liability provisions require review by a qualified Saudi lawyer
- This skill covers the PDPL framework; it does not cover the Cybercrime Law, the Cloud Computing Regulatory Framework, or sector-specific SAMA/CITC data rules, which may impose additional obligations

## Related Skills

- [[draft-privacy-policy-mena]]
- [[draft-data-processing-agreement]]
- [[review-msa-deep-review]]
- [[review-ip-ownership-clarity]]
- [[review-missing-clauses]]
