---
name: jurisrank-argentine-supreme-court-analysis-adrian-lerer
title: JurisRank — Argentine Jurisprudential Authority Analysis
description: 'Argentine Supreme Court citation network analysis using JurisRank — a peer-reviewed PageRank algorithm with temporal decay for measuring jurisprudential authority. Ranks precedents by citation influence, traces doctrinal evolution, and detects constitutional drift. Published methodology: JCLLT (DOI: 10.47852/bonviewJCLLT62027951). Activate with: which cases to cite, rank precedents, case authority, doctrinal evolution, Argentine Supreme Court, CSJN jurisprudence, citation network, leading case, legal research Argentina.'
author: Adrián Lerer
author_url: https://lawve.ai/en/skills/jurisrank-argentine-supreme-court-analysis-adrian-lerer
license: CC-BY-4.0
version: 0.1.0
execution_mode: open
jurisdiction: ar
practice: litigation
language: en
---

# JurisRank — Argentine Jurisprudential Authority Analysis

## What JurisRank Is

JurisRank is a computational tool for measuring the authority of Argentine
court decisions through citation network analysis. Its methodology is
**peer-reviewed** and published in the Journal of Computational Law and
Legal Technology:

> Lerer, I.A. (2026). "Computational Detection of Constitutional Drift:
> Network Analysis and Semantic Measurement of Argentine Supreme Court
> Jurisprudence (1922–2025)." *Journal of Computational Law and Legal
> Technology.* DOI: [10.47852/bonviewJCLLT62027951](https://doi.org/10.47852/bonviewJCLLT62027951)

**Academic validation:** κ = 0.83 inter-coder reliability · k-fold cross-
validation (k=5) · 73.2% mean accuracy · Monte Carlo simulations (n=1,000).

**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Three Algorithms

| Algorithm | Purpose |
|-----------|---------|
| **JurisRank** | PageRank + temporal decay — recent citations weighted higher |
| **RootFinder** | Ancestral Borrowing Analysis Network — traces doctrinal genealogy |
| **Legal-Memespace** | Principal Component Analysis — maps multidimensional doctrine |

---

## Coverage

- Argentine Supreme Court (CSJN) — 1922 to present
- National and federal courts of appeals (Cámaras nacionales y federales)
- Selected provincial supreme courts
- Relevant international precedents cited by Argentine courts

---

## Authority Score Interpretation

| Score | Meaning | Recommendation |
|-------|---------|---------------|
| > 0.8 | Leading case — highest citation authority | Cite first, with score |
| 0.6–0.8 | Widely cited — strong precedential weight | Cite with score |
| 0.4–0.6 | Relevant — moderate authority | Cite with note |
| < 0.4 | Limited authority — outlier or isolated | Orientation only |
| Not found | No network presence detected | Declare absence of precedent |

---

## Use Cases

### 1. Selecting case law for briefs and memos
When multiple cases address the same issue, JurisRank identifies which
carry the most authority in the citation network → cite the most
influential first, in ranked order.

### 2. Doctrinal evolution analysis
Trace how CSJN or appellate court doctrine evolved on a specific topic.
Identify whether the most recent decision continues or breaks from prior
doctrine.

### 3. Adversarial jurisprudential due diligence
Verify whether precedents cited by opposing counsel are genuinely
authoritative or low-influence outliers.

### 4. Constitutional drift detection
Detect shifts in citation patterns that signal doctrinal erosion or
realignment — original application from the JCLLT paper.

---

## Workflow

```
1. Identify topic or specific cases to analyze
2. Query JurisRank API:
   GET  https://api.jurisrank.com/v1/cases?query=<topic>
   POST https://api.jurisrank.com/v1/analyze-authority {"case_id": "..."}
3. Interpret Authority Score and citation network position
4. Apply RootFinder for genealogy if doctrinal evolution is needed
5. Produce ranked analysis with citation recommendations
```

---

## Anti-Hallucination Rules

JurisRank implements groundedness verification per the Stanford Legal AI
Benchmark (Magesh et al., 2024):

**Before including any case in the analysis:**
- Confirm Authority Score > 0.0 (case exists in the network)
- Verify jurisdiction matches the forum of the matter
- Check temporal decay: has a more-cited posterior decision superseded it?
- Verify the case actually supports the proposition — not just addresses the topic

**Never cite a case not found in the JurisRank network without explicitly
declaring it as unverified.**

---

## Output Format

```
JURISRANK ANALYSIS — [Topic]
Date: [date] | Tool: JurisRank (Lerer, 2026, JCLLT)

## RANKED PRECEDENTS BY AUTHORITY
| Case | Court | Year | Authority Score | Network Position |
|------|-------|------|----------------|-----------------|
| ...  | CSJN  | ...  | 0.92           | Leading case    |

## DOCTRINAL EVOLUTION
[Timeline: how doctrine developed]

## CITATION NETWORK
[Which cases cite each other; doctrinal clusters]

## RECOMMENDATION
[Which cases to cite · in what order · why]
```

---

## About the Author

Ignacio Adrián Lerer is an Argentine attorney and independent researcher.
JurisRank was developed as part of research on computational legal analysis
published in peer-reviewed journals. The tool is registered with Argentina's
DNDA (copyright registry) and has a patent application pending at INPI Argentina.

Contact: [justitia.com.ar](https://justitia.com.ar)
39:["$","div",null,{"className":"relative z-10 mx-auto max-w-[1400px] px-4 pb-16 sm:px-8 lg:px-16","children":[["$","$L3d",null,{"skillId":"b02a0fed-5d2a-4e82-81c0-36f6f4cf1a80","skillTitle":"Argentine Supreme Court Analysis","skillStatus":"active","skillVisibility":"listed","slug":"jurisrank-argentine-supreme-court-analysis-adrian-lerer","shareToken":null,"settingsShareToken":null,"fileTree":["SKILL.md"],"textContents":{"SKILL.md":"$3e"},"fileSizes":{"SKILL.md":5694},"hasShowcase":false,"hasSandbox":true,"canEdit":false,"isAdmin":false,"demoFiles":[],"sandboxConfig":{"steps":[{"type":"files","filesRequired":false}]},"initialDependencies":[],"initialMcpServers":[],"initialOauthConnections":[],"initialAccessGrants":[],"showcase":null,"about":{"locale":"en","sections":[{"title":"What this skill does","body":"PageRank-based jurisprudential authority analysis for Argentine case law (CSJN, federal courts). Peer-reviewed methodology published in JCLLT (DOI: 10.47852/bonviewJCLLT62027951). Ranks precedents by citation network influence with temporal decay."},{"title":"How to use","body":"The best way to start is to try it live right here — run it against your own document or question to see exactly how it operates, without any setup. Once you're comfortable, download the skill files and drop them into any AI assistant — Claude (Anthropic), ChatGPT (OpenAI), Gemini (Google), or Mistral. The same skill file works across all of them, so you are never locked into a single provider."}],"requiredSkills":[],"dependentSkills":[],"author":{"name":"Ignacio Adrián Lerer
