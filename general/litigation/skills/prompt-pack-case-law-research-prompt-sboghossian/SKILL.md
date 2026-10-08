---
name: prompt-pack-case-law-research-prompt-sboghossian
title: Case Law Research Prompt
description: Use when a disputes lawyer, in-house counsel, or legal researcher needs a structured case law research output on a specific legal topic, covering leading authorities, their facts, legal principles, court decisions, and practical takeaways for practitioners. Designed for MENA, DIFC/ADGM, GCC, UK, EU, and any specified jurisdiction; acknowledges that case law plays a different role in civil-law versus common-law systems.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-case-law-research-prompt
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Case Law Research Prompt

Case law research is the backbone of legal argument in common-law systems and increasingly influential in civil-law jurisdictions where courts publish reasoned opinions. This skill produces a structured research note covering the leading authorities on a given topic, formatted for immediate use in a court submission, arbitration brief, or client advice.

## When to use this

- Preparing a skeleton argument or statement of case that must cite controlling authorities.
- A client or deal team needs to understand how courts have interpreted a specific clause type, legal doctrine, or statutory provision.
- The lawyer needs to brief junior associates on the leading cases before drafting submissions.
- Building a "state of the law" section for a legal opinion or an expert report.
- Checking whether the law has evolved since the lawyer last researched the point.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Legal topic or issue | Defines the research question | Ask the user to be as specific as possible |
| Jurisdiction(s) | Case law is jurisdiction-specific; common-law vs. civil-law output differs fundamentally | Ask the user — do not default to US or UK |
| Court level or forum | Supreme courts / cassation courts carry more weight | Default to appellate and supreme courts unless stated otherwise |
| Intended use | Submission, opinion, client note, academic — shapes the depth and format | Ask the user |
| Time period | Recent cases most relevant; sometimes historical development matters | Default to last 15 years unless stated otherwise |

## Optional inputs

- Specific cases the user already knows about (to confirm they are included and to add authority).
- Opposing authority the user is trying to distinguish.
- Whether secondary sources (legal texts, academic commentary) should be included.
- Target audience (judge, client, arbitral tribunal) — shapes the technical depth.

## Research methodology

### Step 1 — Frame the legal question precisely
Restate the topic as a focused legal question (e.g., "When will an English court imply a duty of good faith into a commercial contract?"). A sharp question produces better-targeted results.

### Step 2 — Identify the governing legal system
- **Common law** (DIFC, ADGM, UK, US, HK, SG): case law is binding precedent; landmark decisions must be cited.
- **Civil law** (UAE onshore, KSA, LB, EG, FR, most MENA): codified law is primary; court decisions (particularly cassation courts) have persuasive authority and are increasingly published and cited.
- **Mixed / hybrid** (Qatar QFC, Bahrain): apply the rules of the system governing the dispute.

### Step 3 — Structure the research note per case
For each case, provide:

| Field | Content |
|---|---|
| Case name | Full case name as reported |
| Jurisdiction / court | Court and country |
| Year decided | Year of the decision |
| Facts | 2–4 sentence summary of the material facts |
| Legal issue | The precise question the court decided |
| Decision | The outcome and the court's reasoning |
| Principle established | The rule of law the case stands for, in one sentence |
| Practical takeaway | What a practitioner should do or avoid based on this case |
| Current status | Still good law / overruled / qualified by later cases |

### Step 4 — Organize authorities
Present cases in one or more of the following structures depending on the user's need:
- **Chronological:** Shows evolution of the law.
- **By principle:** Groups cases under the sub-rules they establish.
- **For vs. against:** Useful when the law is contested or the research is for adversarial use.

### Step 5 — Synthesize
After the per-case analysis, provide a one-paragraph synthesis: what the current state of the law is, where the uncertainty lies, and any notable trends (judicial activism, divergence between jurisdictions, etc.).

## Civil-law jurisdiction guidance

In **UAE** (onshore), **KSA**, **Lebanon**, and **Egypt**, the primary authorities are:
- The relevant Civil Code or Commercial Code (named, well-established provisions).
- Decisions of the Court of Cassation (Mahkamat al-Naqd in LB/EG; Supreme Court in UAE; Supreme Court / Board of Grievances in KSA).
- These decisions are often unpublished in searchable commercial databases; the researcher should acknowledge this limitation and note which decisions have been officially published.

In **DIFC / ADGM**, decisions are published on the respective court websites and follow common-law citation formats; binding precedent applies.

In **international arbitration** (ICC, LCIA, DIAC, ICSID), there is no doctrine of binding precedent; tribunals cite prior awards as persuasive authority only. Acknowledge this distinction when citing arbitral awards.

## What not to do

- Do not fabricate case names, citations, or holdings. If a case cannot be verified, say so.
- Do not treat the same case as authoritative across different legal systems without noting the jurisdictional distinction.
- Do not omit unfavorable authorities — the lawyer needs to know what they face.
- Do not confuse persuasive and binding authority without flagging the distinction.

## Output format

A research note structured as:
1. **Research question** — one sentence.
2. **Jurisdiction and legal system** — one sentence.
3. **Leading cases** — per-case tables as above.
4. **Synthesis** — one paragraph.
5. **Open questions / limitations** — any gaps in the research, sources that could not be verified, or areas where expert local counsel should confirm.

Footer: "Research note prepared by [Author/AI tool]; not a substitute for legal advice; verify all citations before reliance."

## Limits and escalation

- AI-generated case law research must be verified against primary sources before filing in any court or tribunal. Hallucinated citations have led to adverse costs orders.
- In KSA and LB, the availability of published court decisions is limited; escalate to local counsel for authoritative research.
- Where the law is actively evolving (e.g., AI liability, crypto-asset regulation), flag that recent regulatory guidance or unreported decisions may not be captured.

## Related skills

- [[prompt-pack-case-assessment-memo]]
- [[prompt-pack-complex-law-simple-summary]]
- [[prompt-pack-convert-law-into-checklist]]
- [[prompt-pack-litigation-strategy-memo]]
- [[prompt-pack-arbitration-statement-of-claim]]
