---
name: prompt-pack-regulatory-change-impact-assessment-sboghossian
title: Regulatory Change Impact Assessment
description: Use when a lawyer or compliance officer needs to analyze the operational and legal impact of a new regulation or regulatory amendment on a company or industry. Produces a structured impact assessment covering affected operations, compliance gaps, required policy changes, implementation timeline, and risk mitigation. Especially relevant for MENA companies facing rapid regulatory evolution in fintech, data protection, corporate governance, and capital markets.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-regulatory-change-impact-assessment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# Regulatory Change Impact Assessment

## When to use this

Use this skill when:
- A regulator (CBUAE, SCA, ADGM FSRA, DFSA, SAMA, CMA-SA, FRA Egypt) issues a new law, regulation, circular, or implementing regulation that affects a client's business.
- A law has been amended (e.g., UAE Federal Decree-Law on Commercial Companies, Saudi Companies Law) and the client needs to know which current practices must change.
- An industry is entering new regulatory territory (e.g., UAE Virtual Asset Regulation, Saudi fintech sandbox exit, DIFC new employment law) and the client needs a gap analysis before the compliance deadline.
- A cross-border business is impacted by regulatory change in multiple jurisdictions simultaneously (e.g., GCC VAT harmonization, FATF grey-list impacts, new cross-border data flow restrictions).

**Do not use** this skill as a substitute for a full legal opinion — it produces a structured memo; a qualified lawyer must verify the analysis against the actual text of the new regulation.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Name/reference of the new regulation or amendment** | Anchors the entire analysis; without it, output is generic | Ask — do not guess the instrument |
| **Description of the company/industry** | Determines which provisions apply and what operations are affected | Ask: "What does the company do, and where does it operate?" |
| **Jurisdiction(s) of operation** | Regulations are territorial; a UAE company and a DIFC company face different rules even within the same city | Ask; default to UAE onshore if unclear |
| **Effective date of the regulation** | Sets the urgency and implementation timeline | Ask; if unknown, state "effective date TBD — verify" |
| **Existing compliance posture (if known)** | Enables a genuine gap analysis rather than a generic checklist | Optional but valuable |

## Optional inputs

- **Sector-specific licenses held** — e.g., FSRA Category 3C license, UAE payment services license, Saudi CMA brokerage license — determines which rules apply.
- **Prior impact assessments** — allows the output to build on existing work rather than starting from scratch.
- **Risk appetite of the client** — conservative clients may want a zero-tolerance gap list; commercial clients may want a prioritized list by materiality.

## Document structure (output memo)

1. **Executive summary** — 3–5 bullet points: what changed, why it matters to this client, and the top compliance priorities. Designed to be read by senior management without legal background.
2. **Regulatory change overview**
   - Name and reference of the regulation
   - Issuing authority
   - Effective date and phase-in periods
   - Official summary of intent
   - Where to find the full text
3. **Applicability analysis** — does this regulation apply to the client? Scope of application (entity type, activity, threshold, territorial nexus). Flag if applicability is uncertain — note the specific ambiguity.
4. **Affected operations inventory** — table mapping each operational area (customer onboarding, contract terms, reporting, data handling, product features, employment, tax) to the relevant new requirement.

   | Operational Area | Current Practice | New Requirement | Gap? |
   |---|---|---|---|
   | [e.g., KYC/AML process] | [describe] | [what the regulation requires] | Yes / No / Partial |

5. **Compliance gap analysis** — for each gap identified: severity (high/medium/low), probability of regulatory action if unaddressed, and remediation effort.
6. **Required policy and contract changes** — list of internal policies, standard contracts, customer terms, or employee agreements that need amendment. Note whether changes require regulatory pre-approval (e.g., some UAE licensed entities must submit revised policies to the regulator before implementation).
7. **Implementation timeline and priorities**
   - Must-do before effective date (hard deadline)
   - Should-do within 90 days of effective date
   - Nice-to-have / best-practice improvements
8. **Risk mitigation strategies** — for each high-severity gap: specific action, responsible function (legal, compliance, operations, IT), estimated effort, and escalation path if action cannot be completed in time.
9. **Open questions and legal uncertainties** — items where the regulation is ambiguous, implementing guidance has not been issued, or the firm's interpretation is uncertain. Flag for escalation to specialized counsel or direct regulatory inquiry.
10. **Next steps** — specific action items with owners and deadlines.

## Jurisdictional / practice notes

### UAE — onshore
- UAE regulatory change often comes with short implementation windows (sometimes 30–90 days from publication in the Official Gazette).
- Key regulators: CBUAE (banking, payments, insurance), SCA (capital markets), MOHRE (employment), UAE Data Office (data protection), VARA (virtual assets).
- Ministry of Economy notifications and ADNOC/SWF-related sector rules must be checked separately.
- Arabic text of regulations is authoritative; English translations may lag or differ.

### DIFC / ADGM
- DFSA (DIFC) and FSRA (ADGM) both have mature regulatory change consultation processes; responses to consultations can influence final rules.
- Both publish regulatory change calendars — subscribe to stay ahead.
- Changes to DFSA Rules (Rulebook modules) or ADGM Regulations are immediately binding on licensees.

### KSA
- SAMA, CMA, ZATCA (tax authority), and HRSD (employment) each issue regulations in their sectors.
- Arabic-language regulatory texts are controlling; always read the Arabic version.
- Some regulations require companies to appoint a Saudi compliance officer or maintain local records.

### Egypt
- FRA (Financial Regulatory Authority) and CBE (Central Bank of Egypt) regulate financial services.
- Egyptian law frequently issues ministerial decrees implementing framework laws; check implementing decrees, not just the primary law.

### GCC-wide
- GCC Unified VAT Agreement underpins each member state's VAT law; changes at the GCC level may cascade into national law.
- FATF membership and grey-listing status affects AML/CTF obligations across the region; monitor FATF mutual evaluation reports.

## Drafting standards

- Write the executive summary for a CFO or COO audience — no legal jargon.
- Use the gap table format; do not write a discursive narrative where a table would communicate faster.
- Label each gap by severity (High / Medium / Low) based on: (a) regulatory penalty exposure, (b) likelihood of regulatory scrutiny, (c) operational disruption if unaddressed.
- Cite the specific article or section of the new regulation for each requirement — do not paraphrase loosely.
- Do not invent article numbers — if you are not certain of the precise citation, write "[verify article reference]".
- Date the memo and note which version of the regulation was analyzed; regulatory texts can be amended post-publication.

## Common mistakes

- **Analyzing the wrong instrument.** Regulations are often amended by subsequent circulars; ensure you have the most current version including any implementing regulations and guidance notes.
- **Missing phase-in provisions.** Many MENA regulations have staggered effective dates by entity size or license type; confirm whether the client falls into the early or late cohort.
- **Treating a gap analysis as a compliance certificate.** The memo identifies gaps; it does not constitute a legal opinion that the company is compliant. Include a standard disclaimer.
- **Ignoring Arabic-language nuances.** For UAE and KSA regulations, key definitions in the Arabic text may differ subtly from the English translation; the Arabic version governs in case of conflict.
- **Failing to escalate ambiguity.** Regulators sometimes welcome no-action letter requests or informal guidance; the assessment should flag where a direct regulatory inquiry is warranted.

## Related skills

- [[prompt-pack-regulatory-filing-checklist]]
- [[prompt-pack-stablecoin-issuance-framework]]
- [[prompt-pack-related-party-transaction-policy]]
- [[prompt-pack-privacy-policy]]
- [[heuristic-always-state-jurisdiction-first]]
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]]
