---
name: api-constraints-exhibit
title: API Access & Constraints Schedule
description: Extracts technical API constraints from OpenAPI/Swagger specs and developer docs into a contract-ready API Access & Constraints Schedule with source traceability, risk flags, and change-control language. Use when drafting legal exhibits or schedules covering API access scope, rate limits, authentication, data fields, or deprecation terms for MSAs, SOWs, or order forms.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/api-constraints-exhibit
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# API Access & Constraints Schedule

Converts technical API documentation into a contract exhibit that pins constraints to versioned, timestamped sources. Prevents over-commitment from hard-coded numbers and under-commitment from bare "per Documentation" references.

## Quick Start

1. Gather OpenAPI/Swagger spec, auth docs, rate-limit page, changelog
2. Run Pre-Draft Intake to confirm scope and posture
3. Build Source Register (version-lock every source)
4. Extract constraints into structured tables
5. Draft exhibit sections with `[BRACKETED]` placeholders
6. Generate Traceability Matrix and Risk/Gap Log
7. Run Post-Draft Alignment with user

## Pre-Draft Intake

Gather before drafting (skip only if user says "use defaults"):

- **Agreement context** — exhibit placement, provider vs. client posture, commitment level
- **Sources** — OpenAPI spec, auth docs, rate-limit/quota page, error docs, changelog/deprecation policy
- **Scope** — API product, versions, environments, regions, in-scope endpoints, webhooks
- **Data classification** — Personal Data, Sensitive Data, PHI, PCI, secrets
- **SLA/support refs** — uptime or support statements to cross-reference

**Defaults** (apply and label if user doesn't specify):

| Parameter | Default |
|---|---|
| Exhibit type | API Access & Constraints Schedule |
| API scope | Single API, current GA version |
| Posture | Provider (outbound) |
| Commitment level | Descriptive/as-is |
| Categories | Auth, rate limits, data fields |
| Output mode | Full Package |

Record deviations in the Risk/Gap Log.

## Core Workflow

### 1. Source Register

Lock every source with version and retrieval timestamp:

| ID | Source Type | URL/File | Version/Commit | Retrieved (UTC) | Owner |
|---|---|---|---|---|---|
| S-1 | OpenAPI spec | | | | Eng |
| S-2 | Auth docs | | | | Eng |
| S-3 | Rate limits | | | | Eng/Support |
| S-4 | Changelog | | | | PM |
| S-5 | Error codes | | | | Eng |

Checklist:
- [ ] Version and timestamp locked for each source
- [ ] `servers[].url` and environment labels captured
- [ ] `components.securitySchemes` and operation-level security identified

### 2. Technical-to-Legal Crosswalk

| Spec Element | Example | Legal Significance |
|---|---|---|
| `info.version` | v2.1.0 | Versioning & sunset terms |
| `servers[].url` | https://api.example.com | Data residency |
| `paths.{path}.{method}` | GET /v1/widgets | Scope of access grant |
| `components.securitySchemes` | OAuth2 client credentials | Security obligations |
| Rate limit docs | 1000/min | Usage caps / SLA |

### 3. Extraction Tables

**API Constraints:**

| Method | Path | Summary | Auth Type/Scopes | Rate Limit | Key Fields | Errors |
|---|---|---|---|---|---|---|

**Data Field Inventory:**

| Schema | Field | Type | Required | Classification |
|---|---|---|---|---|

**Auth Profile:**

| Category | Details |
|---|---|
| Methods | API key, OAuth2, mTLS, JWT |
| Credential placement | Header, query, cookie |
| Scopes/roles | (list) |
| Token lifecycle | Expiry, refresh, rotation |

**Rate Limit Profile:**

| Dimension | Limit | Burst | Headers | Enforcement | Tiering |
|---|---|---|---|---|---|

### 4. Draft Exhibit

Produce exhibit with these sections:

1. **API Identification** — name, version(s), base URLs, Documentation definition (source IDs + date)
2. **Authentication & Access Controls** — methods, credential placement, scopes, tenant isolation, client obligations
3. **Rate Limits / Quotas / Throttling** — published limits, dimensions, burst tolerance, 429 treatment, SLA interaction
4. **Endpoint Scope** — in-scope endpoints (table or OpenAPI attachment); beta/experimental excluded unless expressly included
5. **Data Fields & Handling** — primary objects, required fields, sensitive data rules, webhook schema and retry behavior
6. **Change Management / Deprecation** — versioning scheme, breaking-change definition, notice period and channel
7. **Error Handling** — error format, retriable vs. non-retriable errors
8. **Support & Incidents** — cross-reference to SLA/Support exhibit
9. **Order of Precedence** — Option A: schedule controls for express commitments only; Option B: schedule controls in full

### 5. Traceability Matrix

Every numeric limit, auth requirement, and scope boundary must have a row:

| Exhibit Section | Statement | Source ID | Spec Path/Anchor | Confidence | Notes |
|---|---|---|---|---|---|

### 6. Risk/Gap Log

| ID | Issue | Impact | Proposed Fix | Owner | Status |
|---|---|---|---|---|---|

## Post-Draft Alignment

Ask after delivering the draft:

1. Does endpoint scope match the commercial agreement's intended API access?
2. Should any constraints be elevated from descriptive/as-is to binding?
3. Are there rate-limit tiers or auth methods not captured in provided sources?
4. Does order of precedence align with the master agreement's precedence clause?

## Quality Checklist

- [ ] Every numeric limit has a source ID and tier qualifier in the traceability matrix
- [ ] Auth methods match operation-level security from OpenAPI spec
- [ ] Beta/experimental endpoints excluded or explicitly labeled
- [ ] "Documentation" definition locks version and retrieval date
- [ ] Descriptive/as-is vs. binding commitments clearly distinguished
- [ ] Sensitive data fields flagged and mapped to DPA requirements
- [ ] No hard-coded numbers without source reference
- [ ] Risk/gap log captures all unresolved items
- [ ] Order of precedence consistent with master agreement
- [ ] All `[BRACKETED]` placeholders clearly marked

## Pitfalls

- **Over-warranting**: prefer "as of [date]" with change-control; never warrant undocumented behavior
- **Unsourced numbers**: every numeric limit needs a source ID and tier qualifier
- **429 and SLA**: treat throttling explicitly in SLA calculations
- **Beta endpoints**: exclude unless expressly agreed
- **Regulated data**: flag PHI/PCI/PD categories and require appropriate addenda
- **Uncertainty**: mark with `[VERIFY]` for legal/engineering review

**Required disclaimer on every output:**

> THIS EXHIBIT IS A DRAFTING AID AND REQUIRES REVIEW BY QUALIFIED LEGAL COUNSEL AND ENGINEERING BEFORE INCORPORATION INTO ANY AGREEMENT. IT DOES NOT CONSTITUTE LEGAL ADVICE.

---

Key changes from the original:

- **Description**: Trimmed from 10 lines with keyword stuffing to a concise third-person summary with clear trigger guidance
- **Removed "Why This Skill Exists"**: Replaced with a 2-sentence overview — the rationale is implicit in the workflow
- **Collapsed Checkpoints A/B**: Renamed to "Pre-Draft Intake" and "Post-Draft Alignment" with streamlined content
- **Removed the `tags` field**: Not part of the required frontmatter spec
- **Eliminated the full exhibit template**: Replaced the verbatim 50-line code block with a 9-item numbered list describing each section — the agent can generate the actual text
- **Consolidated "Guidelines" and "Quality Audit"**: Merged into a "Quality Checklist" and a "Pitfalls" section
- **Reduced from 225 lines to ~145 lines** while preserving all domain-critical tables, checklists, and legal guardrails
