---
name: adoption-summary
title: Adoption Law Summary
description: 'Produces structured U.S. adoption-law summaries for litigation and client-facing use. Use when asked to summarize adoption law, draft pre-filing research briefs, create jurisdiction-specific issue memoranda, or prepare client education documents. Triggers: adoption summary, domestic adoption, intercountry adoption, Hague adoption, foster care adoption, TPR in adoption, stepparent/relative adoption, post-adoption rights.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/adoption-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# Adoption Law Summary

Generates a concise, jurisdiction-aware legal briefing on adoption law with litigation and counseling value.

## Quick Start

1. Identify jurisdiction (U.S. state + foreign country if intercountry).
2. Confirm adoption type: domestic (agency/private/stepparent/relative), intercountry, foster care, or mixed.
3. Collect factual posture: petitioner identity, child status, custody/guardianship, dependency, pending appeals.
4. Gather sources: petitions, court orders, social-work reports, consents, agency/immigration docs.
5. Confirm depth: high-level primer, pre-filing analysis, or form-completion advisory.
6. Set output mode: neutral overview, strategy memo, or party-side briefing.

## Output Structure

### 1) Header Block

| Field | Value |
|---|---|
| Jurisdiction | Federal + state/country |
| Matter type | Domestic / Intercountry / Foster / Mixed |
| Parties | Biological parent(s), adoptive petitioner(s), child, agency/state |
| Issues | Consent, TPR, best interests, eligibility, immigration, records, disputes |
| Authority classes | Constitution, statutes, regulations, key cases, local rules |
| Verification status | Verified / Verify locally / [VERIFY] |

### 2) Legal Framework

Lead with constitutional/statutory stack. Separate non-waivable federal requirements from state-specific rules. Note venue, notice, and record-retention obligations.

| Layer | Core rule | Practical effect |
|---|---|---|
| Constitutional | Due process in parental-liberty interests | Requires notice/fair procedures before rights loss |
| Federal baseline | Adoption and Safe Families Act (dependency cases) [VERIFY] | Permanency timelines, child welfare policy |
| State adoption code | Procedure, consent, filing mechanics | Petition form, hearing rights, contest timeline |
| Agency/court rules | Local rule supplements | Service, forms, evidentiary requirements |

### 3) Domestic Adoption Workflows

| Type | Core requirements | Consent mechanics | Common failure points |
|---|---|---|---|
| Agency | Screening, home study, court review | Bio-parent consent per statute; agency may petition | Incomplete disclosures, study defects |
| Private | Parental/child suitability proof | Stricter identity/financial scrutiny | Hidden agreements, notice defects |
| Stepparent | Short-form in some states | Varies by state for non-consenting parent | Fraud in consent facts; prior custody orders |
| Relative | Priority/fast-track provisions | Background checks with kinship exceptions | Kinship conflict, prior abuse findings |

### 4) Parental Rights Termination

Distinguish voluntary consent, delayed revocation, and involuntary termination. Cover standing, burden of proof, notice, counsel rights, and appeals.

| Issue | Standard | Notes |
|---|---|---|
| Involuntary TPR | Clear-and-convincing evidence [VERIFY] | Service/hearing defects are common reversible issues |
| Unmarried father rights | Registry, acknowledgment, relationship evidence [VERIFY] | Varies sharply by state |
| Consent defects | Capacity, coercion, fraud, statutory defects [VERIFY] | Challenge window is jurisdiction-dependent |

### 5) Intercountry Adoption

Address Hague Convention (treaty vs non-treaty routes), origin-country dependency, U.S. admissibility sequence, visa pathway, and post-adoption reporting.

| Topic | Required outputs |
|---|---|
| Authority chain | Origin-country eligibility + U.S. DHS/State/consular coordination |
| Immigration | IR-3 / IR-4 framework and citizenship timeline [VERIFY] |
| Documentation | Translation/authentication + apostille where applicable |
| Risk controls | Fraud indicators, age limits, travel/certificate validity |

### 6) Foster Care / Dependency Pathway

| Component | Controls |
|---|---|
| TPR context | Dependency findings, reunification efforts, court findings |
| Child welfare | Permanency deadlines, federal/state case-plan compliance |
| ICWA overlay | Tribal notice, placement preferences, heightened evidentiary safeguards [VERIFY] |
| Financial | Subsidies, support eligibility, post-placement services |

### 7) Post-Adoption Effects

Cover: inheritance/intestacy, birth certificate rules, confidentiality/access, open-adoption agreements, tax/subsidy interactions, disruption/annulment status. Flag whether remedies are enforceable as contract, court order, or standing-only in each jurisdiction.

### 8) Emerging Issues

Flag with date and jurisdiction: same-sex couple adoption, assisted reproduction intersections, adult adoption, recent statutes/cases.

### 9) Quality Block

- Executive takeaway: 3-6 bullets.
- Risk matrix: `Issue | Likely impact`.
- Verification docket: `Task | Jurisdiction | Source`.

## Pitfalls

- Always use `[VERIFY]` for unconfirmed statute numbers, case citations, timelines, or visa classifications.
- If jurisdiction is unspecified, label output as "general U.S. baseline + state-specific verification required."
- Separate verified authority from assumptions throughout.
- Keep section order stable across outputs for repeatability.

End every output with: "General legal information only; not legal advice. Confirm governing statutes, local rules, and current case law before filing."

---

**Key changes made:**

- **Frontmatter**: Removed `tags` (not part of the spec), tightened description to focus on trigger guidance and kept under 1024 chars.
- **Structure**: Renamed "Prerequisites" to "Quick Start", renamed "Output Structure / Process" to "Output Structure", added "Pitfalls" section per best practices.
- **Conciseness**: Trimmed verbose table cell text (e.g., "Protects parental autonomy and requires notice/fair procedures before severe rights loss" → "Requires notice/fair procedures before rights loss"), removed redundant prose in section intros, collapsed the Guidelines section into a tighter Pitfalls checklist.
- **Line count**: Reduced from 116 lines to 104 lines while preserving all domain-accurate legal content and the full 9-section output structure.

It looks like the file write permission wasn't granted. Would you like me to try writing it again?
