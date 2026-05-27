---
name: antitrust-investigation-summary
title: Antitrust Internal Investigation Summary
description: Drafts privilege-protective, board-ready executive summary memoranda of internal antitrust investigation findings for US federal law. Covers monopolization, vertical restraints, acquisitions, FTC Act Section 5, tech-platform conduct, risk assessment, and remediation. Use when drafting antitrust investigation summaries, board memos on competition risk, or internal compliance investigation reports.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/antitrust-investigation-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: antitrust
language: en
---

# Antitrust Internal Investigation Summary

Produces a privilege-protective, board-ready memo synthesizing internal antitrust investigation findings for technology platform companies under US federal law.

## Quick Start

Before drafting, collect:

- **Investigation charter** — directing authority, investigators, dates, privilege posture
- **Factual record** — triggering complaint, implicated contracts, internal comms, product decision docs, regulator correspondence
- **Interview materials** — Upjohn-warned summaries (role, topics, key assertions)
- **Market context** — products, monetization, rivals, switching costs, network effects, prior assessments
- **Remediation status** — stop-gap steps, policy updates, product/contract changes
- **Procedural posture** — anticipated litigation, M&A, preservation holds

If critical inputs are missing, request them: "To provide a competent risk assessment, I require [specific items]."

## Output Structure

The memo contains seven sections in order.

### 1. Privilege Header

Every page:

```
ATTORNEY–CLIENT PRIVILEGED / ATTORNEY WORK PRODUCT
Prepared at the direction of counsel to provide legal advice regarding
antitrust compliance and potential exposure. Intended solely for [Company]
senior leadership and the Board of Directors. Do not forward outside
those who need to know for purposes of receiving legal advice.
```

### 2. Executive Summary

BLUF format. Frame each finding as: **Issue → Key Facts → Legal Significance → Risk Level → Recommended Action**

Anchor three risk pillars:

- **Legal Liability** — strength of potential claims
- **Regulatory Scrutiny** — DOJ/FTC enforcement probability
- **Reputational Impact** — downstream effects on partners, developers, public

### 3. Investigation Scope & Methodology

Cover: triggering event, time period, products/units, conduct categories, document sources, custodian/interview counts, analyses performed, known gaps. Be specific without creating a discovery roadmap.

### 4. Key Findings

Organize by **issue**, not witness or chronology. Map each finding to:

| Theory | Statute | Key Elements |
|---|---|---|
| Monopolization | Sherman Act § 2 | Monopoly power + willful acquisition/maintenance [VERIFY citations] |
| Vertical restraints | Sherman Act § 1 | Agreement + unreasonable restraint (rule of reason) |
| Acquisitions | Clayton Act § 7 | May substantially lessen competition [VERIFY current Merger Guidelines] |
| Unfair methods | FTC Act § 5 | Broader than Sherman/Clayton; reaches gatekeeping conduct [VERIFY citations] |

**Tech-platform issue checklist:**

- [ ] Self-preferencing (ranking, defaults, API access)
- [ ] Tying / bundling
- [ ] De facto exclusivity (rebates, defaults)
- [ ] Anti-steering provisions
- [ ] Interoperability / API restrictions
- [ ] MFN / parity clauses
- [ ] Killer acquisitions
- [ ] Ecosystem lock-in / switching cost manipulation

For each finding: (1) conduct, (2) record evidence including hot documents, (3) procompetitive rationale, (4) contrary evidence, (5) uncertainties.

### 5. Risk Assessment

Three layers:

| Layer | Question |
|---|---|
| **Legal** | Plausible statutory theory? |
| **Factual** | Evidence strength? Discovery exposure? |
| **Enforcement** | DOJ/FTC likely to prioritize? [VERIFY current posture] |

Also address: relevant market definition, key pivots, counterfactual analysis. Avoid pseudo-quantification ("70% chance") — use risk drivers.

### 6. Remediation Recommendations

Frame as **strategic risk mitigation**, not admission. Three tiers:

| Tier | Timeframe | Examples |
|---|---|---|
| Immediate | 0–30 days | Stop-gap changes, messaging |
| Structural | 1–6 months | Policy/contract revisions, approval pathways |
| Monitoring | Ongoing | Audits, training, metrics |

Tie each to a finding. Assign ownership and timeline. Use advisory language: "revise provisions that could be characterized as conditioning" not "cease illegal tying."

### 7. Regulatory Exposure & Readiness

Cover: pending inquiries, likely theories mapped to facts [VERIFY agency priorities], key risk documents/witnesses, preparedness status, strategic options.

Readiness checklist:

- [ ] Preservation holds functioning
- [ ] External counsel retained
- [ ] Response protocol for CIDs/subpoenas
- [ ] Messaging guidelines updated
- [ ] HSR considerations (if M&A dimension)

## Drafting Rules

**Privilege-protective:**

- Advisory language throughout ("evidence could be interpreted as…" not "the company fixed prices")
- Separate facts from analysis from recommendations
- Never make conclusory admissions — use "potential theories," "enforcement risk," "facts that could be argued to support"
- Privilege framework: *Upjohn*, *Hickman v. Taylor*, Fed. R. Civ. P. 26(b)(3), Fed. R. Evid. 501 [VERIFY citations]

**Adversarial resilience:**

- Draft as if a regulator will read despite privilege claims
- Test every sentence: quoted out of context in a complaint, would it be damaging?
- Address hot documents directly — acknowledge, contextualize, assess
- Balance exclusionary findings against procompetitive benefits

**Anti-hallucination (non-negotiable):**

- Every citation and doctrinal statement must be verified or marked `[VERIFY]`
- Every factual assertion traceable to a document, interview, or dataset
- Separate verified facts from counsel's assessment
- Confirm the record supports characterizations like "systematic" or "widespread"

## Scope and Ethics

- **US federal antitrust only** — flag state AG, private class action, and international (EU Art. 102, DMA, UK) exposure for specialist follow-up
- Present risk in circuit-neutral terms unless circuit is specified and verified
- Counsel represents the organization (Model Rule 1.13), not individuals
- **Attorney must review all output** — this is a drafting aid, not legal advice
- Do not input unnecessary personal data; follow organization's secure AI workflow
