---
name: consumer-breach-notice-letter
title: Consumer Breach Notification Letter
description: 'Drafts U.S. consumer-facing data breach notification letters compliant with state statutes. Use when a security incident involving personal information requires consumer notice — first, interim, or follow-up. Covers jurisdiction-aware content, incident disclosure, compromised-data specificity, mitigation steps, support services, and delivery requirements. Trigger: data breach notice, consumer notification, personal information incident, identity theft letter, substitute notice.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/consumer-breach-notice-letter
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: data-protection
language: en
---

# Consumer Breach Notification Letter

Drafts disclosure-ready breach letters balancing legal compliance, clarity, and actionable protective guidance for affected consumers.

## Quick Start

Before drafting, gather these inputs:

```
- [ ] Affected jurisdictions (consumer residence states + applicable statutes)
- [ ] Incident facts: discovery date/time, type, affected systems, investigation status
- [ ] Exact personal information categories compromised per recipient cohort
- [ ] Remediation actions already taken (credit monitoring, key resets, system fixes)
- [ ] Distribution method per jurisdiction (mail, email, substitute notice)
- [ ] Authorized signer and counsel sign-off scope
- [ ] Support contacts: toll-free line, email, webpage, enrollment links/codes
- [ ] Industry overlays if applicable (HIPAA, GLBA, PCI)
```

## Letter Structure

Populate each section in order:

```
[COMPANY LEGAL NAME]
[LEGAL ADDRESS]
[DATE]

[Recipient Name / Consumer]

RE: Data Breach Notification

1. Opening — company identification
2. Incident description — discovery timeline
3. Personal information involved
4. Steps company has taken
5. Actions consumer should take now
6. Remediation services and enrollment details
7. Contact channels and support
8. Jurisdictional notices/disclaimers
9. Signature block and reference/case number
```

Use plain language, factual tone. No speculative attribution or security-sensitive technical detail.

## Required Content by Section

| Section | Must Include | Add If Applicable |
|---|---|---|
| Incident context | Discovery date, nature of incident, investigation status | If ongoing: explicit update commitment |
| Data exposed | Personal data list with cohort-level precision | Separate letters when data sets differ materially |
| Consumer steps | Priority actions ordered by risk level | Tailor for SSN/financial vs. credential exposure |
| Company response | Containment, forensics involvement, reporting status | Law-enforcement/regulator notice only if confirmed |
| Support | Help desk, website, enrollment steps/codes, FAQ | Multilingual support if required |
| Closing | Responsible contact, follow-up commitment | Required statutory notice text per jurisdiction |

## Delivery and Recordkeeping

1. Generate channel-specific variants only where required by law (mail/email/substitute).
2. Schedule delivery by recipient cohort with proof-of-delivery capture.
3. Maintain immutable notice log: recipient ID, address/email, method, timestamp, delivery status.
4. Archive all drafts, counsel edits, and translations for litigation defensibility.

## Compliance Checklist

```
- [ ] Letter states what happened, who is affected, when (discovery date), and what was compromised
- [ ] No unverified cause or opinion statements included
- [ ] Remediation advice is actionable and aligned to exposed data types
- [ ] Contact info is specific, operational, and staffed
- [ ] Statutory deadlines confirmed per jurisdiction (prompt/without unreasonable delay or strict-number)
- [ ] Counsel review completed and file-stamped before send
```

## Pitfalls

- **Overbroad language**: Never use "all information was compromised" unless proven. List exact data elements.
- **Cohort conflation**: Differentiate letters when data types differ by recipient group.
- **Negligence admissions**: State only supported facts. Avoid attributing cause beyond what investigation confirms.
- **Jargon**: Recipients are consumers, not engineers. Use plain language throughout.
- **Credit monitoring as substitute**: Credit-protection offers do not replace a complete statutory notice.
- **Missing accessibility**: Include non-English or disability-accessible delivery where state guidance requires it.
- **Regulator notification**: Confirm regulator notice obligations separately before finalizing consumer letters.

---

**Key changes from the original:**

- **Removed `tags`** — not part of the Agent Skills spec (only `name` and `description` in frontmatter)
- **Tightened description** — shorter, still third-person with clear triggers
- **Eliminated the Input Validation Matrix** — redundant with the prerequisites checklist
- **Collapsed Prerequisites into a Quick Start checklist** — trackable, scannable
- **Simplified the 5-step "Output Structure / Process"** into flat sections — Letter Structure, Required Content, Delivery, Compliance Checklist
- **Merged Guidelines into Pitfalls** — concise bold-label format, no do/don't repetition
- **Dropped the notification log assembly step** from prerequisites (moved to Delivery section where it belongs)
- **Reduced from 111 lines to ~80 lines** — roughly 30% token savings while preserving all domain accuracy
