---
name: due-diligence-summary
title: Due Diligence Summary
description: Produces structured U.S. transactional due diligence summaries with risk ratings, document citations, and follow-up actions. Triggers when the user requests a due diligence summary, diligence report, red-flag memo, or data room analysis for M&A, investment, or partnership transactions.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/due-diligence-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [analysis, summarization, transactional]
---

# Due Diligence Summary

Decision-ready diligence summary with risk ratings, evidence citations, and next-step actions for U.S. transactional matters.

---

## Related skills

- **Environmental subset** — `phase-i-esa` for ASTM E1527-21 site assessments; `environmental-regulation-summaries` for governing-statute identification; `environmental-indemnity` and `environmental-covenant-and-easement` for risk-allocation drafting.
- **Real estate subset** — `real-estate-transaction-summary` for property-transaction memos that include diligence; `title-commitment` for title-side review.
- **Corporate subset** — `corporate-bylaws`, `articles-of-incorporation`, `pro-forma-cap-table` for governance review.
- **Compliance subset** — `compliance-summaries` for cross-sector regulatory posture; `hipaa-baa` and related healthcare skills for HIPAA-regulated targets.
- **Outputs** — `legal-memo` for substantive opinions arising from diligence findings; `engagement-letter-review` for scope confirmation upstream.

## Quick Start

Gather before beginning:

1. **Transaction snapshot** — type, parties, structure, timeline, target entities
2. **Scope definition** — in/out-of-scope categories, materiality threshold, jurisdictions
3. **Data room index** — document list with stable IDs and dates
4. **Substantive materials** — governance docs, financials, contracts, IP schedules, litigation files, HR/benefits, real estate, tax, environmental records
5. **Privilege/confidentiality designation** and allowed audience

## Workflow

1. **Map scope to inventory** — mark each category Complete / Partial / Missing using the coverage checklist.
2. **Extract findings** — facts, obligations, restrictions, change-of-control and consent triggers.
3. **Classify** each finding as Fact, Representation, or Open Issue.
4. **Rate risk and materiality** — quantify exposure where possible.
5. **Flag conflicts** across sources; resolve by authority and date.
6. **Produce summary** using the deliverable template; cite every material finding as `[Doc ID or Title, date, page/section]`.

### Risk Scale

| Rating | Meaning | Action |
|--------|---------|--------|
| High | Likely deal impact or material exposure | Escalate; require resolution/mitigation |
| Medium | Manageable; needs diligence or contractual protection | Track; address in docs/price |
| Low | Informational or minor exposure | Note; monitor if cumulative |

### Coverage Checklist

| Category | Expected Core Docs |
|----------|--------------------|
| Corporate/Governance | Charter, bylaws, consents, cap table, subsidiary org |
| Financials/Debt | Audited/unaudited FS, debt docs, guarantees, liens |
| Contracts | Top customer/vendor, assignment/consent, exclusivity |
| IP/Tech | IP schedule, licenses, OSS use, assignments |
| Litigation/Reg | Docket list, claims history, agency letters |
| HR/Benefits | Payroll, key employee agreements, benefits plans |
| Real Estate/Assets | Leases, deeds, asset schedules |
| Tax | Returns, audits, NOLs, nexus |
| Environmental | Phase I ESA (ASTM E1527-21), Phase II reports, environmental permits (NPDES, Title V, RCRA), CERCLA / state cleanup status, environmental indemnity provisions, ECOAs, PFAS exposure, reportable historical releases |

## Deliverable Template

### Executive Summary
- Deal snapshot (type, parties, target, valuation if known)
- Top 5 red flags with risk rating and cited evidence
- Missing critical items

### Scope & Coverage
- In-scope categories and jurisdictions
- Coverage checklist with gaps and rationale

### Key Findings by Category

One table per category (Corporate/Governance, Financials/Debt, Contracts, IP/Tech, Litigation/Regulatory, HR/Benefits, Real Estate/Assets, Tax, Environmental):

| Issue | Evidence | Risk | Materiality | Follow-up |
|-------|----------|------|-------------|-----------|

### Conflicts & Discrepancies

| Topic | Conflicting Sources | Assessment | Action |
|-------|---------------------|------------|--------|

### Open Items / Follow-Up Requests

| Item | Rationale | Requested From | Priority |
|------|-----------|----------------|----------|

### Recommended Actions
- Contractual protections (rep, warranty, indemnity, covenants)
- Price or structure adjustments
- Pre-closing conditions or consents

## Pitfalls & Checks

- Separate confirmed facts from representations and open issues — never conflate.
- Flag missing expected documents as findings with risk and impact.
- Use exact dates, parties, dollar amounts, and governing law when available.
- Label unsigned drafts as non-authoritative.
- For regulated industries, add a compliance subsection (HIPAA, FDA, FINRA/SEC, OFAC, FCPA, state licensing); mark statutes `[VERIFY]` if uncertain.
- Stay neutral and evidence-driven — do not advocate for or against the deal.
- Preserve privilege and confidentiality; limit distribution as instructed.

---

## Troubleshooting

- **Data room incomplete or actively being populated.** Mark each missing-document line as a finding (Risk: Medium-High depending on category) with a follow-up request. A summary built on a partial data room is signed only with explicit scope limitation in the Executive Summary.
- **Source documents conflict (e.g., cap table vs. board consents).** Show both readings side-by-side with citations; flag for resolution by counsel. Do not silently reconcile by date — older documents may control where amendments aren't on file.
- **Regulated-industry target without familiar compliance lens.** Engage industry-specific counsel; flag and rate Unknown-but-material rather than guessing. Examples: HIPAA covered-entity status; banking BSA/AML; broker-dealer registration.
- **Environmental concerns surfaced but no Phase I in the data room.** Risk is Medium-to-High depending on industrial use history. Recommend a Phase I ESA per ASTM E1527-21 as a closing condition or pre-LOI step, and an environmental indemnity in the definitive agreement.
- **Privilege risk on shared diligence.** When buyer's counsel and seller's counsel share substantive analysis, joint-defense / common-interest agreements are the usual mechanism. Note any unprivileged exchanges in the deliverable.
