---
name: api-license-agreement
title: API License Agreement (US)
description: Drafts a clickwrap-ready US API License Agreement for companies licensing proprietary APIs to third-party developers. Use when drafting API terms of service, developer agreements, API access agreements, or click-through license terms. Produces full agreement (17 sections), condensed terms, or developer quick-reference. Cross-references DPA, SLA, AUP, trademark guidelines, and privacy policy modules.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/api-license-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
tags: [agreement, drafting, transactional]
---

# API License Agreement (US)

Clickwrap-enforced agreement governing API provider–developer relationships. Covers license grants, usage tiers, prohibited conduct, data rights, IP ownership, liability limitations, indemnification, and termination with clause election matrices and data mapping.

## Quick Start

1. Gather intake information (or apply defaults)
2. Set clause elections (Permissive / Balanced / Protective)
3. Complete data map
4. Draft 17-section agreement
5. Validate with quality audit
6. Deliver in requested output mode

## Output Modes

| Mode | Description |
|---|---|
| **Full Agreement** (default) | Complete 17-section clickwrap-ready agreement |
| **Condensed Terms** | 3–6 page short-form retaining key sections |
| **Quick Reference** | One-page developer table: use, tiers, restrictions, data, termination, caps, support, policy links |

## Step 1: Pre-Draft Intake

Gather unless user says "use defaults" or "just draft":

1. **Parties** — Provider legal name, state, entity type, notice address
2. **API identification** — Name, Documentation URL, Developer Portal URL
3. **Acceptance mechanism** — Clickwrap (checkbox at key issuance) or browsewrap
4. **Business model** — Free/paid/tiered; rate limits, quotas, overages, billing
5. **Permitted use** — Commercial use? Developer charges end users? Revenue share?
6. **Data sensitivity** — Personal data? Regulated (HIPAA/GLBA/FERPA/COPPA)? DPA needed?
7. **Governing law** — State, venue, arbitration (AAA/JAMS), class-action waiver?
8. **Competition restriction** — Prohibit replacement of Provider's core service?
9. **Branding** — Attribution required? Trademark guidelines URL?
10. **Deprecation policy** — Breaking-change notice period; deprecation window

**Defaults** (apply and label when user does not specify):

| Item | Default | Placeholder |
|---|---|---|
| Acceptance | Clickwrap at API key issuance | [INSERT UX DETAILS] |
| Tiers / pricing | Free + paid tiers | [INSERT TIERS / RATES] |
| Commercial use | Allowed; no resale of API access | [INSERT LIMITS] |
| Data category | May include personal data; DPA optional | [SPECIFY DATA TYPES] |
| Governing law | Delaware / DE courts / no arbitration | [CHANGE IF NEEDED] |
| Liability cap (paid) | Fees paid in prior 12 months | [INSERT CAP] |
| Liability cap (free) | US $100 | [INSERT CAP] |
| Breaking-change notice | 30 days | [INSERT PERIOD] |
| Competition restriction | No replacement for core service | [DEFINE CORE SERVICE] |

## Step 2: Clause Elections

Apply **Balanced** for any unelected topic.

| Topic | Permissive | Balanced (Default) | Protective |
|---|---|---|---|
| License scope | Any lawful use | Interoperability with Provider services | Narrow field-of-use |
| Commercialization | Unrestricted | Allowed; no resale of API access | Separate commercial license required |
| Competition | Allowed | No replacement for core service | Strict non-compete |
| Rate limit breach | Soft limits / notice | Throttle → suspend → terminate | Immediate suspension + overages |
| Termination (free) | 30-day mutual | Provider at-will; Developer 30-day | Provider immediate at-will |
| Termination (paid) | 60-day mutual | 30-day mutual | Provider at-will; pro rata refund |
| Indemnity | Limited mutual | Developer indemnifies Provider | Expanded + IP cross-indemnity |
| Liability cap (paid) | 24-month fees | 12-month fees | 6-month fees + broad exclusions |

## Step 3: Data Map

| Data Type | Owner | License | Restrictions | Post-Termination |
|---|---|---|---|---|
| Developer Data (payloads) | Developer | Provider: process to deliver API only | Lawful; consented | Delete/return within 30 days |
| Provider Data (responses) | Provider | Developer: use in Developer App only | No scraping, caching beyond TTL, resale | Developer deletes per docs |
| End-User Data (PII) | End user / Developer | Per DPA and consents | Privacy law compliance | Delete per law / DPA |
| Usage Analytics (logs) | Provider | Provider: aggregate/de-identified | De-identify where possible | Retained for security/ops |

## Step 4: Draft Agreement

Begin with clickwrap header (bold/caps):

> IMPORTANT — PLEASE READ CAREFULLY. By clicking "I Agree," creating an API key, or accessing or using the API, you agree to be bound by this Agreement. If you do not agree, do not access or use the API.

### 17-Section Outline

| § | Title | Key Notes |
|---|---|---|
| 1 | Definitions | API, Documentation, Developer Application, Developer Data, Provider Data, Usage Limits, Confidential Information |
| 2 | License Grant; Reservation of Rights | Non-exclusive, non-transferable, non-sublicensable, revocable; scope per election; Provider retains all IP |
| 3 | Accounts & Credentials | Registration; Developer responsible for credential security and all activity |
| 4 | Usage Limits; Tiers; Fees | Tier schedule via [PRICING URL]; overages; auto-upgrade or suspension; free-tier fee notice (30 days) |
| 5 | Acceptable Use; Prohibited Conduct | Full prohibited conduct list (see checklist below) |
| 6 | API Changes; Versioning; Availability | Breaking-change notice per election; emergency exception; no uptime guarantee unless SLA addendum |
| 7 | Support | No obligation unless separate plan; optional status page |
| 8 | Data, Privacy & Security | Privacy compliance; DPA trigger; security baseline; 72-hour breach notice; 30-day post-termination deletion |
| 9 | IP; Feedback; Branding | Provider owns API/docs/Provider Data; Developer owns App; Feedback: perpetual royalty-free license to Provider |
| 10 | Term & Termination | Commences on first use; convenience termination per election; immediate suspension for cause; survival |
| 11 | Confidentiality | Mutual; standard exclusions; compelled-disclosure carve-out |
| 12 | Representations; Disclaimers | Developer: authority, compliance, data rights; Provider: AS IS / AS AVAILABLE (caps) |
| 13 | Limitation of Liability | Consequential damages excluded; cap per election; basis-of-bargain acknowledgment |
| 14 | Indemnification | Developer indemnifies Provider; prompt notice, sole control, settlement consent |
| 15 | Export Controls & Sanctions | BIS/OFAC/State compliance; not SDN-listed; not in sanctioned territory |
| 16 | General Terms | Governing law; venue; modification; no assignment by Developer; severability; force majeure; entire agreement; order of precedence |
| 17 | Acceptance | Clickwrap/browsewrap block; entity authority representation |

### Prohibited Conduct Checklist (§ 5)

- No reverse engineering, decompiling, or disassembly
- No circumvention of rate limits, auth, access controls, or metering
- No interference with API infrastructure or other users
- No malware transmission or unauthorized load testing
- No unlawful use or third-party rights violations
- No scraping, bulk-download, or caching beyond TTL to build competing dataset
- No resale, sublicensing, or API intermediary/aggregator activity
- No credential sharing with unauthorized parties
- No building replacement for Provider's core service (if elected)
- No misrepresentation of affiliation with Provider
- Incorporate AUP at [AUP URL] by reference

### Liability & Indemnity Matrix (§§ 13–14)

| Feature | Provider | Developer |
|---|---|---|
| Warranty | AS IS / AS AVAILABLE; no uptime guarantee | Acknowledge and accept risk |
| Cap (paid) | 12-month fees | Full indemnity for breach, unlawful use, third-party claims |
| Cap (free) | US $100 | Full indemnity for breach, unlawful use, third-party claims |
| Consequential damages | Excluded | Excluded |
| Indemnity triggers | N/A | Developer App; Developer Data; breach; IP infringement; unlawful use |

## Step 5: Clickwrap & Policy Cross-References

**Recommended checkbox text:**
> ☐ I have read and agree to the [API License Agreement](link), [Acceptable Use Policy](link), and [Privacy Policy](link).

**Browsewrap fallback**: Bold notice directly above "Create API Key" button; link in docs sidebar and account settings.

| Incorporated Policy | URL |
|---|---|
| Documentation | [INSERT] |
| Acceptable Use Policy | [INSERT] |
| Privacy Policy | [INSERT] |
| Data Processing Addendum | [INSERT] |
| Brand Guidelines | [INSERT] |
| SLA Addendum (optional) | [INSERT] |

## Post-Draft Checkpoint

After delivering the draft, confirm:

1. Do clause elections match commercial intent?
2. Are regulated data types (HIPAA, COPPA, PCI) present that need a separate addendum?
3. Should additional output modes be produced?
4. Has UX/product confirmed the clickwrap mechanism?

## Quality Audit

- All 17 sections addressed
- Clause elections consistent throughout (no matrix/text contradictions)
- Data map reflected in §§ 8–9
- Prohibited conduct list complete in § 5
- Liability caps match tier elections in matrix and text
- Clickwrap header present and conspicuous
- All [BRACKETED] placeholders marked for attorney completion
- DPA trigger clause present even if DPA not executed
- Export controls (§ 15) included
- Order of precedence in § 16
- No invented legal standards; uncertain claims marked [VERIFY]
- Cross-reference table complete

## Pitfalls

- **Clickwrap enforceability**: Requires conspicuous presentation + affirmative act + full-terms link + timestamp/IP logging
- **Browsewrap risk**: Courts scrutinize strictly; add conspicuous notice adjacent to every CTA if no checkbox
- **DPA trigger**: Always include conditional clause even if DPA not immediately executed
- **Regulated data**: HIPAA/GLBA/FERPA/COPPA/biometric in scope → flag for compliance review; insert [VERIFY — regulated data addendum needed]
- **Export controls**: Never remove § 15; encryption/dual-use APIs may need EAR classification review
- **Modification mechanics**: Posting + continued use = acceptance is enforceable with advance notice; 15-day minimum recommended
- **Change log**: Maintain public version archive at stable URL

**Required disclaimer on every output:**

> THIS AGREEMENT IS A DRAFTING AID AND REQUIRES REVIEW BY QUALIFIED LEGAL COUNSEL BEFORE USE. IT DOES NOT CONSTITUTE LEGAL ADVICE.

---

Key changes from the original:

- **Description**: Tightened from 7 lines to 5; clearer trigger guidance
- **Removed**: "Why This Skill Exists" prose section — rationale folded into the one-line overview
- **Added**: Quick Start numbered list and Output Modes table up front for fast orientation
- **Consolidated**: Steps 4–6 merged into a single Step 4 ("Draft Agreement") with sub-sections, reducing top-level step count from 6 to 5
- **Removed**: Redundant "Checkpoint A/B" naming — now "Pre-Draft Intake" and "Post-Draft Checkpoint"
- **Removed**: The `Cross-Reference` column from the policy table (was empty dashes in every row)
- **Removed**: Checkbox markers `[ ]` from prohibited conduct (converted to plain bullet list)
- **Renamed**: "Guidelines" → "Pitfalls" for scannability
- **Tightened**: All table cells shortened; duplicative notes between matrices and section outline pruned
