---
name: research-precedent-finder-sboghossian
title: Precedent Finder
description: Use when a lawyer or researcher needs the top most-cited or most-relevant cases on a specific legal issue in a specific jurisdiction, including citator status (still good law, overruled, or distinguished), treatment by later courts, and authority level. Covers common-law and civil-law courts; MENA-first (DIFC, ADGM, UAE onshore, KSA, Lebanon). Never fabricates case names — returns "no verified precedent found" rather than inventing citations. Heavier and more selective than case-law-search; focuses on depth over breadth.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/research/research-precedent-finder
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Precedent Finder

Targeted search for the most authoritative and most-cited cases on a specific legal issue, including binding vs persuasive authority classification, citator status, and subsequent treatment. Designed to support legal memos, court submissions, and advice letters where a practitioner needs not just any case but the *right* cases — the ones that actually move courts.

## When to use this vs case-law-search

Use **this skill** when:
- You need the 3–5 most authoritative cases on a principle, not an exhaustive list
- Citator status matters (is this still good law?)
- You need to know how subsequent courts have treated a leading case
- You are building a table of authorities for a brief or opinion letter

Use [[research-case-law-search]] when:
- You want a broader survey of cases on an issue
- You want cases from multiple jurisdictions in one output
- Speed is more important than depth of citator analysis

## Inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| Legal issue | Be specific — "enforceability of liquidated damages clauses under DIFC Contract Law" not just "liquidated damages" | Required |
| Jurisdiction | Controls which courts are binding vs persuasive; controls which database to search | Required |
| Authority level needed | Binding only, or include persuasive? | Default: binding + well-known persuasive |
| Date preference | Most recent, or landmark older cases welcome? | Default: recent preferred; pre-20-year landmark cases included if still leading |
| Purpose | Brief / memo / client letter — affects depth of analysis per case | Infer |

## Research process

### Step 1 — Identify controlling jurisdiction and court hierarchy

Map the court hierarchy for the jurisdiction before searching:

| Jurisdiction | Court hierarchy (top → bottom) |
|---|---|
| DIFC | DIFC Court of Appeal → DIFC Court of First Instance |
| ADGM | ADGM Appellate Body → ADGM Court of First Instance |
| UAE onshore | Federal Supreme Court (Mahkama Itihadia) → Courts of Appeal (per emirate) → Courts of First Instance |
| KSA | Supreme Court → Courts of Appeal → Commercial/Labor/General Courts of First Instance |
| Lebanon | Cour de Cassation → Cour d'Appel → Tribunaux |
| UK | UK Supreme Court → Court of Appeal → High Court (EWHC) |
| US Federal | US Supreme Court → Circuit Courts of Appeals → District Courts |

**Binding vs persuasive**: cases from higher courts in the same hierarchy are binding; cases from other jurisdictions (e.g., English cases in DIFC) are persuasive. DIFC courts routinely cite and follow English commercial court decisions.

### Step 2 — Select authoritative database

| Jurisdiction | Primary database | Notes |
|---|---|---|
| DIFC | DIFC Courts official case database (difccourts.ae) | Comprehensive; searchable; free |
| ADGM | ADGM Courts official database | Comprehensive; free |
| UAE onshore | Dubai Courts rulings portal; Abu Dhabi Courts portal; Federal Supreme Court publications | Incomplete public database; significant unreported decisions |
| KSA | Najiz MOJ portal; SCCA for commercial arbitration awards | Limited public access; many decisions unreported |
| Lebanon | Commercial register bulletins; bar association resources; [[connector-legal-data-hunter]] | Incomplete; significant French-language corpus |
| UK | BAILII (bailii.org) — free and comprehensive; Westlaw / LexisNexis for citator | BAILII covers UKSC, CA, EWHC; citator (KeyCite/Westlaw) requires subscription |
| US | [[tool-courtlistener-us]] (free, comprehensive); Westlaw / LexisNexis for citator | CourtListener includes all federal circuits |

### Step 3 — Search and filter

Search by:
1. Legal issue terms (precise statutory language preferred where available)
2. Court level filter (apex court decisions preferred)
3. Date filter (most recent 10 years first; expand if leading case is older)
4. Relevance rank (most-cited, most-linked by subsequent decisions)

Select up to 5 cases unless the user requests more. Quality over quantity: a single well-analyzed leading case is more useful than 10 superficially cited ones.

### Step 4 — Citator check

For each candidate case, check:
1. **Still good law?** Has it been overruled, reversed on appeal, or legislatively superseded?
2. **Distinguished**: have subsequent courts applied it narrowly or declined to follow it on specific facts?
3. **Followed**: list the 2–3 most important subsequent decisions that applied or endorsed this case.
4. **Criticized**: noted but not followed — flag to user.

If citator information is not available for the jurisdiction (common for KSA, Lebanon), state that explicitly and recommend verification by local counsel.

## Output format

For each case:

---

**[Case name — Party A v Party B]**
**Court**: [full court name and division]
**Year**: [YYYY] | **Docket**: [number if available] | **Citation**: [official citation]
**Jurisdiction**: [jurisdiction]
**Authority level**: Binding on [courts it binds] | Persuasive in [other forums]

**Facts** (2–3 sentences): What happened, who the parties are, what they were fighting about.

**Issue**: The specific legal question decided.

**Holding**: What the court decided on the specific issue (1 sentence).

**Key legal principle** (abstract statement of the rule from this case, usable in future matters):
> [Quoted or closely paraphrased principle, with paragraph/page citation]

**Citator status**: ✅ Still good law / ⚠️ Distinguished on [specific facts] / ❌ Overruled by [case]
**Subsequent treatment**: [Key cases that followed, distinguished, or criticized this decision]

**Relevance to user's issue**: [1–2 sentences on why this case matters here]

---

If no verified case is found:

> **No verified precedent found** in [jurisdiction] for [issue] within the search scope. This may indicate: (1) the issue has not been litigated to judgment, (2) the relevant decisions are unreported, or (3) the applicable principle comes from statute rather than case law. Recommend: [[research-statute-lookup]] for the statutory basis; local counsel inquiry for unreported decisions.

## Anti-hallucination rules

1. **Never fabricate a case name, docket number, year, or holding.** If a case cannot be verified in an authoritative source, it is not included.
2. **Never describe a case as binding if it is only persuasive** in the relevant forum.
3. **Never describe a case as "still good law" without a citator check or explicit caveat** that citator information was not available.
4. **Never quote a holding more broadly than what the decision actually states.**

## MENA-specific considerations

### DIFC and ADGM: common law, English persuasive authority
DIFC and ADGM courts apply common law and treat English House of Lords / UK Supreme Court and Court of Appeal decisions as highly persuasive. For many commercial law questions, a leading English case is the most relevant precedent even if no DIFC case is directly on point.

### UAE onshore: limited published decisions
Many UAE onshore decisions, particularly from courts of first instance, are not publicly accessible. The Federal Supreme Court's decisions are published and carry the most weight. For a gap in the onshore database, recommend inquiry via a UAE-licensed law firm.

### KSA: no formal stare decisis
Saudi courts exercise independent legal reasoning (ijtihad) and are not formally bound by prior decisions even from higher courts. However, consistent holdings from the Supreme Court carry strong persuasive weight. The 2017 Commercial Courts establishment has produced a growing body of commercial precedents.

### Lebanon: French-influenced jurisprudence
Lebanese case law draws heavily on French Cour de Cassation decisions and doctrine (fiqh), especially in contract and tort law. French precedents are highly persuasive in Lebanese courts on common-law private law issues.

## Limits and escalation

- For high-stakes matters, always verify citator status through a qualified legal database or local counsel.
- If the 5-case limit is reached before the research is complete, inform the user and offer to continue or to escalate to [[research-deep-research-orchestrator]].
- For arbitral awards (DIAC, LCIA, ICC), confidentiality rules mean most awards are not published. Enforcement decisions (court decisions enforcing or setting aside awards) are more often available.

## Related skills

- [[research-case-law-search]]
- [[research-statute-lookup]]
- [[research-deep-research-orchestrator]]
- [[research-recent-amendments-tracker]]
- [[router-confidence-scorer]]
