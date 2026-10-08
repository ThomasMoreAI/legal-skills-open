---
name: workflow-full-due-diligence-pack-sboghossian
title: Full Legal Due Diligence Pack
description: Use when orchestrating a full legal due diligence exercise for an M&A transaction, private equity investment, or acquisition financing. Covers ten parallel workstreams (corporate, commercial contracts, employment, IP, real estate, litigation, regulatory, tax, data privacy, financial), with MENA-specific flags for change-of-control, foreign ownership restrictions, PDPL readiness, and open-source IP compliance. Produces a structured DD report with green/amber/red workstream ratings.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/workflow/workflow-full-due-diligence-pack
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Full Legal Due Diligence Pack

## Purpose

This workflow orchestrates a complete legal due diligence exercise for acquisitions, equity investments, and financing transactions. It produces a structured DD report with per-workstream risk ratings, a critical findings memo, and a recommended list of actions (reps & warranties scope, specific indemnities, escrow requirements, and required pre-closing remediation).

---

## Inputs

| Input | Required | Notes |
|-------|---------|-------|
| Target company name + jurisdiction | Yes | Drives applicable law for each workstream |
| Transaction type | Yes | Acquisition / equity investment / debt financing — affects scope |
| Materiality threshold | Yes | Tie to deal size: e.g., findings >$50k flagged; >$500k red |
| Data room access | Yes | All documents must be accessible before commencing |
| Deal timeline | Yes | Drives workstream prioritization and depth |
| Buyer's side priorities | Yes | Any specific areas of concern from acquirer |
| Exclusivity terms | Recommended | Know how much time is available |

---

## Logic — Workstream Overview

All ten workstreams run in parallel. Each produces: **RAG rating** (Green / Amber / Red) + **list of findings** + **recommended actions**.

### RAG Rating Criteria

| Rating | Meaning | Response |
|--------|---------|---------|
| Green | No material issues found | Confirm in rep |
| Amber | Issues present but manageable | Targeted indemnity or escrow; disclosure schedule note |
| Red | Material issue requiring action | Pre-closing remediation OR price adjustment OR walk-away |

---

## Workstream 1 — Corporate

**Scope**: legal existence and authority of the target

Checklist:
- [ ] Certificate of incorporation / trade license (current and valid)
- [ ] Memorandum and Articles of Association (current, consolidated version)
- [ ] Cap table — fully diluted; all share classes, options, warrants, convertible instruments
- [ ] Shareholder register — confirms legal ownership
- [ ] Board minutes — last 3 years; resolutions for major decisions; authorization trail
- [ ] Related-party transactions — arms-length? properly approved?
- [ ] Foreign ownership compliance — is the ownership structure compliant with the jurisdiction's FDI/foreign ownership rules?
- [ ] UBO (Ultimate Beneficial Ownership) disclosures — AML/regulatory requirement in UAE, KSA, DIFC
- [ ] Corporate group structure — any subsidiaries, JVs, branches?

**MENA-specific flags:**
- UAE mainland: foreign ownership restrictions still apply in certain sectors (check the Positive List under FDI Law); verify local partner arrangements
- KSA: foreign investment license required (MISA license); verify it is current and covers the actual business activity
- DIFC/ADGM: more flexible foreign ownership; verify regulated activity licenses (DFSA/FSRA) if applicable

---

## Workstream 2 — Commercial Contracts

**Scope**: material contracts that drive revenue or create obligations

Checklist:
- [ ] Top 20 contracts by revenue — check for change-of-control provisions (do they require consent on acquisition?)
- [ ] Assignability — can contracts be transferred to the acquirer without consent?
- [ ] Key customer contracts — concentration risk; auto-renewal vs. renegotiation risk
- [ ] Key supplier contracts — critical dependency? exclusivity?
- [ ] Exclusivity clauses — does the target have exclusivity obligations that restrict the acquirer's other business?
- [ ] Most-favored-nation (MFN) or pricing commitments
- [ ] Termination-for-convenience clauses — can customers exit quickly?
- [ ] Force majeure coverage — COVID/pandemic clauses; war clauses (relevant for MENA)
- [ ] Government contracts — procurement rules; anti-assignment; local content requirements

**Red flags:**
- Revenue concentration (>30% from a single customer who can terminate)
- Change-of-control provisions requiring third-party consent that may not be obtainable
- Unusual exclusivity or non-compete obligations that bind the acquirer

---

## Workstream 3 — Employment

**Scope**: material employment obligations and key personnel risk

Checklist:
- [ ] Top 10 employees + key contractors — contract review; severance exposure; garden leave
- [ ] Restrictive covenants — non-compete, non-solicit enforceability in the jurisdiction
- [ ] Equity / incentive plans — vesting schedules; change-of-control acceleration provisions
- [ ] Employment classification — are contractors correctly classified? Misclassification creates statutory employment liability
- [ ] Government registrations current? (Qiwa/GOSI in KSA; MOHRE/WPS in UAE; NSSF in LB)
- [ ] Pending or threatened employment claims
- [ ] EOSG/EOSA accruals — are they fully provisioned in the accounts?
- [ ] Collective agreements or employee representation — consultation obligations on acquisition

---

## Workstream 4 — Intellectual Property

**Scope**: IP assets and ownership clarity

Checklist:
- [ ] IP ownership — is all material IP owned by the company or properly licensed in?
- [ ] IP created by founders — was it assigned formally? (see [[draft-ip-assignment]])
- [ ] IP created by employees — employment agreements contain IP assignment provisions?
- [ ] IP created by contractors — work-for-hire or assignment clause in contractor agreements?
- [ ] Registered IP portfolio — trademarks, patents, domain names: current, valid, renewed?
- [ ] Open-source software — list all OSS used in the product; identify any copyleft licenses (GPL, LGPL, AGPL) that impose licensing obligations
- [ ] Trade secrets — are NDAs in place for employees and contractors with access?
- [ ] License agreements (in) — any material IP licensed in? assignable on transaction?
- [ ] License agreements (out) — any IP licensed to third parties? exclusivity?

Run [[review-ip-ownership-clarity]] as part of this workstream.

---

## Workstream 5 — Real Estate

**Scope**: premises and property obligations

Checklist:
- [ ] Leases — all locations; term, rent, break clauses, renewal options, assignment on change of control
- [ ] Owned property — title, encumbrances, mortgage/charge (registered?)
- [ ] Dilapidations exposure at lease end
- [ ] Planning / zoning compliance
- [ ] Statutory registration current? (Ejari in Dubai; Tawtheeq in Abu Dhabi; Ejar in KSA)

---

## Workstream 6 — Litigation

**Scope**: pending and contingent legal liability

Checklist:
- [ ] Pending litigation — court and arbitration proceedings; amounts at stake
- [ ] Threatened claims — received demand letters or pre-action notices
- [ ] Settled claims in last 5 years — what was the issue and amount?
- [ ] Regulatory investigations or enforcement actions
- [ ] Dispute resolution clauses in material contracts — arbitration? forum?

**Red flags:** material pending claims; pattern of commercial disputes; regulatory investigations

---

## Workstream 7 — Regulatory / Licensing

**Scope**: licenses, permits, and regulatory compliance

Checklist:
- [ ] All operating licenses current and valid for the actual business activities
- [ ] Financial services licenses (if applicable) — DFSA, FSRA, SAMA, CBUAE authorization
- [ ] Data protection filings / DPO appointment where required
- [ ] Sector-specific compliance: healthcare, education, legal, financial services all have bespoke licensing
- [ ] Foreign direct investment restrictions — approvals required on change of control?
- [ ] Trade sanctions compliance — no dealings with sanctioned parties (OFAC, EU, UN)

Run [[review-compliance-gap-analysis]] and [[research-licensing-requirements-lookup]] as part of this workstream.

---

## Workstream 8 — Tax

**Scope**: tax compliance and open liabilities

Checklist:
- [ ] Corporate tax filings current (UAE CT applies from June 2023; KSA 20% on foreign shareholder profits; LB various)
- [ ] VAT registration and filings — UAE 5%; KSA 15%; others
- [ ] Withholding tax on dividends / interest / royalties — applicable in KSA, LB; UAE 0% for most
- [ ] Transfer pricing — intercompany transactions at arm's length? documentation adequate?
- [ ] Open tax assessments or disputes
- [ ] Tax losses carried forward — available to acquirer?
- [ ] Employee payroll tax compliance

---

## Workstream 9 — Data Privacy

**Scope**: personal data compliance posture

Checklist:
- [ ] Data inventory — what personal data is collected, processed, stored?
- [ ] Privacy notice / policy — current, accurate, accessible?
- [ ] Consent mechanisms — valid legal basis for each processing activity?
- [ ] Third-party data processors — DPAs in place? (see GDPR Art. 28 and PDPL equivalents)
- [ ] International data transfers — SCCs or equivalent for transfers outside adequate jurisdictions?
- [ ] Breach history — any notified or unnotified breaches?
- [ ] UAE PDPL compliance posture (Federal Decree-Law 45/2021)
- [ ] KSA PDPL compliance posture (Saudi PDPL, effective September 2023)
- [ ] GDPR compliance if serving EU data subjects

---

## Workstream 10 — Financial / Disclosure Schedule

**Scope**: reconcile legal DD findings with financial statements

Checklist:
- [ ] EOSG provisions — are they correctly calculated and fully provisioned?
- [ ] Litigation reserves — do the accounts reflect pending claims?
- [ ] Lease liabilities — IFRS 16 / ASC 842 right-of-use assets vs. actual lease obligations
- [ ] Contingent liabilities — guarantees, letters of credit, off-balance sheet arrangements
- [ ] Revenue recognition — does it match the contractual basis?
- [ ] Related-party transactions — arms-length and disclosed?

---

## Output — Due Diligence Report Structure

### Report Sections

1. **Executive Summary** (1 page)
   - Transaction overview
   - Overall DD verdict (Green / Amber / Red at portfolio level)
   - Top 3–5 critical findings requiring buyer attention

2. **Critical Findings** (3 pages)
   - Each material issue: workstream, description, quantum, recommended action

3. **Workstream Sections** (5–10 pages each)
   - Per-workstream: RAG rating, findings list, recommended actions (indemnity / specific rep / escrow / pre-closing fix)

4. **Disclosure Schedule Recommendations**
   - Which items to flag for negotiation; what the seller needs to disclose against which reps

5. **Reps & Warranties Scoping**
   - Based on DD findings, areas where reps should be strengthened or where buyer should seek specific indemnities

6. **Post-Closing Actions Calendar**
   - Remediation items; filing deadlines; integration milestones

---

## Why This Matters

Legal due diligence converts transaction risk from unknown to quantified. Each workstream finding becomes an input to the deal structure: price adjustments, specific indemnities, escrow sizing, and earn-out conditions are all driven by DD output. A thorough DD also protects the buyer: knowledge of a defect at DD prevents it from ripening into a rep & warranty claim later.

---

## Related Skills

- [[review-ip-ownership-clarity]]
- [[review-compliance-gap-analysis]]
- [[research-licensing-requirements-lookup]]
- [[draft-ip-assignment]]
- [[workflow-investment-round-closing-pack]]
- [[workflow-startup-incorporation-pack]]
- [[wiki-vc-startups]]
