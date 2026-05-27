---
name: non-compete-agreement
title: Non-Compete Agreement
description: Drafts enforceable non-compete, non-solicitation, and confidentiality agreements tailored to U.S. state law. Performs jurisdictional analysis of reformation rules, consideration requirements, and statutory restrictions. Use when drafting restrictive covenant agreements, non-compete clauses, non-solicitation provisions, or enforcement-ready employment contracts.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/non-compete-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
---

# Non-Compete Agreement

Drafts jurisdiction-tailored, enforcement-ready non-compete agreements balancing employer protection against employee mobility rights. Covers non-compete, non-solicitation, confidentiality, and integrated litigation provisions.

## Quick Start

Gather before drafting:

1. **Governing jurisdiction** — state law controlling enforceability
2. **Parties** — employee name/title/hire date/access level; employer legal name/formation state/address
3. **Protectable interests** — trade secrets, customer relationships, specialized training, proprietary methods
4. **Desired scope** — geographic territory, duration, restricted activities
5. **Existing agreements** — prior contracts, NDAs, or restrictive covenants
6. **Timing** — new hire vs. existing employee (affects consideration requirements)

## Jurisdictional Analysis

Research and document before drafting:

| Factor | Determine |
|---|---|
| Reformation approach | Blue-pencil (strike), reformation (court modifies), or red-pencil (voids entire provision) |
| Consideration | At-will employment sufficient, or independent consideration required for existing employees |
| Thresholds | Minimum salary or categorical prohibitions (low-wage workers, physicians) |
| Notice requirements | Mandatory advance notice periods |
| Statutory restrictions | State statutes limiting scope, duration, or applicability |
| FTC posture | Current federal regulatory guidance and pending legislation |

**Ban states:** CA, MN, ND, OK have near-categorical non-compete bans — pivot to non-solicitation and NDA-only.

## Core Workflow

### 1. Title and Parties

- Full title: "Non-Compete, Non-Solicitation, and Confidentiality Agreement"
- Employer: legal name, formation jurisdiction, principal address, DBAs
- Employee: full name, title, department, hire/promotion date
- Include detail sufficient for service of process and personal jurisdiction

### 2. Recitals

Articulate **specific** legitimate business interests (not boilerplate):
- Proprietary systems and trade secrets employee will access
- Customer relationships and goodwill at stake
- Employer's training investment
- Geographic markets and competitive landscape
- Sales cycle / retention periods relevant to measuring harm

### 3. Definitions

| Term | Scope |
|---|---|
| Confidential Information | Specific categories with exclusions for public/independently developed information |
| Restricted Territory | Based on actual market presence — named counties/MSAs, radius, or customer-contact territories |
| Restricted Period | 6–24 months calibrated to seniority and access level |
| Competitive Activities | Specific prohibited conduct tied to identified competitors and similar roles |

### 4. Restrictive Covenants

Each covenant must satisfy three-dimensional reasonableness (geographic + temporal + activity):

- **Non-Compete** — no broader than employer's actual footprint; temporal scope justified by information decay
- **Customer Non-Solicitation** — limited to customers with material contact during 12–24 month lookback; covers solicitation, servicing, and acceptance of business
- **Employee Non-Solicitation** — prohibit recruiting/hiring employer's employees and contractors
- **Confidentiality** — perpetual for trade secrets; time-limited for other proprietary information; return/destruction obligation on termination

### 5. Consideration

| Timing | Required Consideration |
|---|---|
| At hire | Employment + access to confidential information + training |
| During employment | Promotion, raise, bonus, new confidential access, or guaranteed continued employment for specified period |

State specific value to demonstrate bargained-for exchange.

### 6. Employee Acknowledgments

Employee affirms: restrictions are reasonable and necessary; adequate consideration received; will not prevent earning a livelihood; opportunity to consult independent counsel.

### 7. Enforcement and Remedies

- **Injunctive relief** — stipulation that monetary damages are inadequate; right to TRO, preliminary/permanent injunction; bond waiver where enforceable
- **Reformation/severability** — authorize court to modify overbroad restrictions to maximum enforceable extent; tailor to jurisdiction's approach
- **Attorneys' fees** — prevailing party or mutual fee-shifting based on enforcement posture
- **Tolling** — restricted period extended by duration of any breach
- Preserve right to compensatory damages, lost profits, and punitive damages where permitted

### 8. Dispute Resolution

Choose one framework:

| Option | Key Terms |
|---|---|
| Litigation | Exclusive venue, consent to personal jurisdiction, forum non conveniens waiver |
| Arbitration | Administering org, number of arbitrators, location, judicial review scope |
| Hybrid | Mandatory mediation → arbitration/litigation; carve-out for injunctive relief in court |

Select forum considering favorability of non-compete law and practical enforceability.

### 9. Governing Law and Boilerplate

Choice of law with conflict-of-laws waiver (reasonable nexus required); written amendment requirement; non-waiver; notice provisions; assignment to successors; entire agreement / integration; severability coordinated with reformation clause.

### 10. Execution

Employer and employee signature blocks with dates; separate voluntary-execution acknowledgment; notarization where appropriate.

## Pitfalls and Checks

- **Jurisdiction-specific always** — generic agreements are unenforceable; tailor every scope dimension
- **Narrow > broad** — courts enforce narrow restrictions; overbroad provisions risk voiding the entire agreement in red-pencil states
- **Recitals are evidence** — detailed recitals establish reasonableness at enforcement
- **No bracketed placeholders** — output must be execution-ready
- **Mark uncertain citations** with `[VERIFY]` — state non-compete statutes change frequently
- **FTC compliance** — note federal posture and flag if proposed rules affect enforceability
- **Include exhibits** as needed: customer lists, competitor lists, territory maps
- **Table of contents** for agreements exceeding 5 pages

---

**Key changes from the original:**
- Trimmed the `description` frontmatter to a concise two-sentence summary with clear trigger guidance
- Removed `tags` from frontmatter (not part of the required format)
- Renamed "Prerequisites" → "Quick Start" and condensed the six items
- Promoted the ban-states note into the Jurisdictional Analysis section as a highlighted callout instead of burying it in Guidelines
- Renamed "Output Structure" → "Core Workflow" for clarity
- Collapsed verbose subsections (e.g., acknowledgments reduced from checklist to inline sentence, governing law from bullet list to single paragraph)
- Renamed "Guidelines" → "Pitfalls and Checks" for scannability
- Removed redundant explanation lines throughout while keeping all legally substantive content
