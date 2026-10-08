---
name: wiki-research-sboghossian
title: Legal Research Methodology
description: Use when a user asks about legal research methodology, how to structure a research workflow, source-triangulation techniques, hypothesis-driven legal analysis, or how to find and verify primary and secondary legal authorities across MENA and international jurisdictions. Provides a comprehensive reference on research process design for legal professionals and AI-assisted legal tools.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/wiki/wiki-research
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Legal Research Methodology

## Scope

This knowledge pack covers legal research workflows, hypothesis-driven analysis, and source-triangulation practices used by legal professionals and legal AI tools. It applies across all jurisdictions but highlights specific MENA considerations where the research landscape differs from common-law traditions.

---

## Core Principle: Hypothesis-Driven Research

Effective legal research is not a library browse — it is a structured inquiry process anchored to a specific legal question. The hypothesis-driven model:

1. **State the legal question precisely.** "Can a Lebanese employer terminate a fixed-term contract before expiry without triggering Article 50 liability?" is researchable. "Is termination legal?" is not.
2. **Form an initial hypothesis.** Based on plain reading of applicable law, form a working answer. This prevents confirmation bias — you are looking to test the hypothesis, not confirm it.
3. **Identify the source hierarchy** for the applicable jurisdiction (see below).
4. **Research primary sources first.** Statute, decree-law, regulation, case law in that order.
5. **Triangulate.** Cross-check the conclusion across at least three independent authoritative sources before treating it as reliable.
6. **Identify counter-arguments.** Actively seek authority that contradicts the hypothesis; document it.
7. **State conclusions with confidence levels.** Well-settled law vs. contested vs. unsettled.

---

## Source Hierarchy by Jurisdiction Type

### Civil-Law Jurisdictions (Lebanon, Egypt, Saudi Arabia, UAE-onshore, France)

| Tier | Source type | Notes |
|------|-------------|-------|
| 1 | Constitution | Hierarchy baseline |
| 2 | Codified statutes / decree-laws | Official Gazette versions authoritative |
| 3 | Executive regulations / ministerial decisions | Often amend statutes operationally |
| 4 | Judicial decisions | Persuasive, not binding precedent (unlike common law) |
| 5 | Academic doctrine (fiqh / doctrine) | Influential in KSA; in LB, leading treatises cited in court |
| 6 | Comparative law / Model laws | Useful for gap-filling in unsettled areas |

Civil-law research trap: published case law is sparse and court databases are incomplete. A single favorable decision is weak authority; look for consistent court of cassation lines.

### Common-Law Jurisdictions (DIFC, ADGM, UK, US)

| Tier | Source type | Notes |
|------|-------------|-------|
| 1 | Statute / Regulations | DIFC Laws; ADGM Regulations |
| 2 | Binding precedent | Court of Appeals and above |
| 3 | Persuasive precedent | Other common-law jurisdictions, lower courts |
| 4 | Academic commentary | Annotated statutes, leading treatises |
| 5 | Regulatory guidance | FCA, DFSA, FSRA guidance notes |

### Islamic Law Overlay (KSA, potentially UAE)

In Saudi Arabia, Sharia principles are a primary source of law. Research must consider:
- Relevant Quran and Sunnah provisions as interpreted by contemporary Islamic jurisprudence
- SAMA / SAFCSP regulatory circulars that translate Sharia compliance into operational rules
- Fatwas from recognized bodies (e.g., Council of Senior Scholars) for novel instruments
- The distinction between prohibited (haram) elements (riba, gharar, maysir) and permissible commercial structures

---

## Research Workflow (Step by Step)

### Phase 1 — Issue Spotting (5–10 min)
- Decompose the client problem into discrete legal issues
- Map each issue to: applicable jurisdiction + applicable body of law (contract, tort, regulatory, etc.)
- Prioritize issues by materiality and by deadline pressure

### Phase 2 — Primary Source Search (20–40 min)
- Identify the controlling statute or regulation
- Read the relevant provisions in the original language if possible (Arabic text controls in most MENA civil-law jurisdictions)
- For UAE: check Federal level + Emirate level (some subjects are dual-regulated)
- For KSA: check Royal Decrees via Nizam platform; check ministerial resolutions
- For DIFC/ADGM: search the official DIFC Laws portal / ADGM Legal Portal

### Phase 3 — Case Law Search (15–30 min)
- Civil law: use official court publication databases where available; academic research databases for Lebanon (Lexis Nexis Lebanon), KSA, Egypt
- Common law: Westlaw, LexisNexis, DIFC Courts public judgments
- Search by statutory article number, not just keywords — courts cite articles

### Phase 4 — Secondary Source Triangulation (10–20 min)
- Review at least one leading academic treatise or bar association commentary
- For MENA issues: top regional law review articles (Arab Law Quarterly, Middle East Law and Governance)
- Check practitioner alerts from major regional firms (published as client updates)

### Phase 5 — Synthesis and Confidence Assessment
State the conclusion in structured form:
```
Issue: [precise question]
Governing law: [statute / instrument]
Analysis: [reasoning chain]
Conclusion: [answer]
Confidence: [High / Medium / Low] — [reason for uncertainty if medium/low]
Counter-argument: [strongest opposing view, if any]
Sources: [numbered list]
```

---

## MENA-Specific Research Challenges

- **Language**: statutes in Arabic; many English translations are unofficial and may not reflect the latest amendments. Always note which version you relied on.
- **Date of amendment**: MENA legislation is frequently amended by ministerial decision without consolidated re-publication. Check the Official Gazette for amendments after the base statute.
- **Unpublished decisions**: courts in LB, EG, KSA do not publish all decisions. A "there is no case law" finding often means there is no published case law — different things.
- **Regulatory circulars**: SAMA, CBUAE, CMA, BdL each issue circulars that effectively amend primary law without legislative process. These must be researched separately.
- **Sharia variation**: Hanbali school governs KSA; Maliki and Hanafi influence LB/EG. Conclusions from one school may not transfer.

---

## AI-Assisted Research Protocols

When legal AI tools (including this assistant) perform research:

1. **Primary source first** — AI should never substitute synthesized summaries for actual primary source text on a point of law. Quote the provision.
2. **Hallucination guard** — Article numbers, case citations, and regulatory thresholds must be verified independently. Do not rely on AI-generated citations without checking the source document.
3. **Triangulate AI output** — treat AI summary as a starting point, not a conclusion. Run the same query across two independent channels.
4. **Note knowledge cutoff** — AI models have training cutoffs; legislative amendments after the cutoff will be missed.
5. **Jurisdiction specificity** — prompt with "under [specific statute/jurisdiction]" to reduce generic output.

---

## How to Use This Pack

Use this pack as a methodology reference when:
- Setting up a research protocol for a new matter
- Training junior lawyers or AI-assisted legal tools on research quality standards
- Auditing the reliability of AI-generated legal conclusions
- Building research templates for frequently-recurring legal questions

---

## Caveats & Currency

Research standards evolve as new databases, regulatory portals, and AI tools become available. The MENA legal database landscape has improved significantly since 2020 but remains less comprehensive than US/UK equivalents. Verify the current availability of databases in your jurisdiction before designing a research workflow.

## Related Skills

- [[wiki-topic]]
- [[wiki-strategy]]
- [[research-jurisdiction-comparison]]
- [[review-contract-redline]]
- [[heuristic-always-state-jurisdiction-first]]
