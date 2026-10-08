---
name: legal-research-assistant-shashionline
title: Legal Research Assistant
description: Multi-source legal research workflow for Indian law covering statutes, case law, and secondary sources. This skill should be used when conducting comprehensive legal research, finding relevant precedents, or analyzing statutory provisions across India Code, Indian Kanoon, and other free legal databases.
author: shashionline
author_url: https://github.com/shashionline/indian-law-plugin/tree/master/skills/legal-research-assistant
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: in
practice: contracts
language: en
---

# Legal Research Assistant

This skill provides structured workflows for comprehensive legal research using freely available Indian legal resources.

## Purpose

Conduct systematic legal research by:
1. Searching across multiple authoritative sources (India Code, Indian Kanoon, government databases)
2. Following source hierarchy (Constitution → Statutes → Case Law → Secondary Sources)
3. Validating currency of law (checking amendments, repeals, superseding judgments)
4. Organizing research findings with proper citations

## When to Use This Skill

Use this skill when:
- Researching a new legal question from scratch
- Finding relevant statutes and case law on a topic
- Validating current applicability of legal provisions
- Building comprehensive legal analysis
- Preparing legal opinions or protocols

## Research Sources (All Free Access)

### Primary Sources

**1. India Code** (indiacode.nic.in)
- All Central Acts from 1836 onwards
- Current versions with amendments
- Search by Act name, year, or keyword
- Download PDFs of bare acts

**2. Indian Kanoon** (indiankanoon.org)
- 1.4M+ cases (SC, 24 HCs, 17 tribunals)
- 20,000+ documents added daily
- Full-text search with Boolean operators
- Case citators (cases citing a judgment)

**3. Supreme Court Website** (sci.gov.in)
- Latest judgments
- Cause lists
- Constitution Bench decisions

**4. e-Courts Portal** (ecourts.gov.in)
- Case status across district courts
- Judgment Information System
- Virtual hearings

**5. Law Commission Reports** (lawcommissionofindia.nic.in)
- Policy recommendations
- Law reform proposals
- Reports 1-279+

### Secondary Sources (Free)

- **Legal Services India** (legalservicesindia.com)
- **Legal Bites** (legalbites.in)
- **SCC Online Blog** (scconline.com/blog)
- **Bar & Bench** (barandbench.com)

## Research Workflow

### Step 1: Define Research Question

Formulate precise question:
- ✅ GOOD: "What is the limitation period for filing suit for specific performance of sale agreement under Limitation Act 1963?"
- ❌ VAGUE: "Tell me about specific performance"

Identify:
- **Legal Issue**: [e.g., Limitation period]
- **Domain**: [e.g., Civil Law - Specific Relief]
- **Jurisdiction**: [e.g., All India / Specific State]
- **Time Period**: [e.g., Current law / Historical]

### Step 2: Statutory Research (India Code)

**Search Strategy**:
1. Identify relevant Act(s)
2. Read bare statutory provisions
3. Check for amendments
4. Note cross-references

**Example Search**:
```
Topic: Limitation for specific performance
→ Search "Limitation Act 1963" on India Code
→ Navigate to Schedule
→ Find Article 54: "For the specific performance of a contract" - 3 years
→ Check for amendments post-1963
```

Refer to: @references/statutory-search-guide.md

### Step 3: Case Law Research (Indian Kanoon)

**Search Techniques**:

**Boolean Operators**:
- `AND`: Both terms must appear
- `OR`: Either term can appear
- `NOT`: Exclude term
- `" "`: Exact phrase

**Examples**:
```
"specific performance" AND "limitation" AND "Article 54"
"Section 3(d)" AND "evergreening" AND "Novartis"
"arbitrability" AND ("Vidya Drolia" OR "BALCO")
```

**Filters**:
- Court: Supreme Court, specific High Court
- Year Range: 2020-2024 for recent law
- Citation: Search by AIR/SCC number

**Citator Function**:
- Find cases citing a landmark judgment
- Track judicial treatment (followed, distinguished, overruled)

Refer to: @references/case-law-search-guide.md

### Step 4: Validate Currency

**Check**:
1. **Amendments**: Has statute been amended since judgment?
2. **Repeals**: Has provision been repealed/replaced (e.g., IPC → BNS)?
3. **Overruling**: Has case been overruled by larger bench?
4. **Legislative Changes**: New Acts superseding old law?

**Example**:
```
Research on IPC Section 377:
- Original provision: Criminalized homosexuality
- Navtej Johar (2018): SC partially struck down Section 377
- Current status: Only bestiality remains criminal
→ Must cite Navtej Johar + current reading of Section 377
```

### Step 5: Organize Findings

**Structure**:
1. **Statutory Provisions** (with citations)
2. **Binding Precedents** (Supreme Court cases)
3. **Persuasive Authorities** (HC cases, Law Commission)
4. **Analysis** (how authorities apply to question)

**Citation Format**:
- Use proper AIR/SCC citations (refer to legal-citation-validator skill)
- Include pinpoint references (specific page/paragraph)
- Note ratio decidendi vs obiter dicta

### Step 6: Synthesize & Document

Create structured research memo:
```markdown
# Research Memorandum

## Question Presented
[Precise legal question]

## Brief Answer
[1-2 sentence conclusion]

## Applicable Law

### Statutory Provisions
- [Act, Year], Section [X]: "[Relevant text]"

### Case Law
- [Case Name], [Citation]: [Holding]

### Analysis
[How law applies to facts]

## Conclusion
[Detailed answer with legal reasoning]
```

## Source Hierarchy

When conflicts arise, follow this hierarchy:

1. **Constitution of India** (supreme law)
2. **Supreme Court Judgments** (binding on all courts)
3. **Central Statutes** (as interpreted by SC)
4. **High Court Judgments** (binding within state)
5. **Tribunal Decisions** (subject to HC writ)
6. **Law Commission Reports** (persuasive, not binding)
7. **Academic Commentary** (persuasive)

**Example Conflict**:
```
If HC judgment contradicts earlier SC judgment:
→ SC judgment prevails (larger bench can overrule smaller bench SC decision)
→ Note HC judgment for persuasive value only
```

## Advanced Search Scripts

### Script 1: Bulk Case Citator
**File**: @scripts/case_citator.py

Search all cases citing a landmark judgment:
```python
# Usage: python case_citator.py "Kesavananda Bharati" "AIR 1973 SC 1461"
# Returns: List of all cases on Indian Kanoon citing this judgment
```

### Script 2: Statutory Amendment Tracker
**File**: @scripts/amendment_tracker.py

Check amendment history of any Act:
```python
# Usage: python amendment_tracker.py "Arbitration and Conciliation Act" 1996
# Returns: Timeline of all amendments with dates
```

Refer to: @scripts/ directory for implementation

## Integration

### With Protocols
- Use this skill when creating new IL-* protocols
- Ensures research is comprehensive before drafting

### With Agents
- Contract-law-specialist, civil-procedure-specialist, etc. use this for deep research
- Master orchestrator delegates complex research queries here

### With Commands
- `/legal-research <question>` invokes this skill's workflow

## Example Research Workflows

### Example 1: New Legal Question
**Question**: "Can mediated settlement agreement be challenged under Section 34 A&C Act?"

**Workflow**:
1. Search India Code: Arbitration & Conciliation Act 1996 + Mediation Act 2023
2. Find Section 29, Mediation Act 2023: MSA has status of arbitral award
3. Search Indian Kanoon: "mediated settlement" AND "Section 34"
4. Find relevant cases interpreting enforceability
5. Synthesize: MSA under Mediation Act 2023 ≠ arbitral award under A&C Act 1996, different challenge mechanisms

### Example 2: Transitional Law
**Question**: "Is IPC Section 300 or BNS equivalent applicable to offense committed in June 2024?"

**Workflow**:
1. Check India Code: BNS effective date = July 1, 2024
2. Transitional provisions: Offenses before July 1 governed by IPC
3. Answer: IPC Section 300 applies (offense in June 2024)

### Example 3: Recent Development
**Question**: "Latest SC position on cryptocurrency regulation?"

**Workflow**:
1. Indian Kanoon search: "cryptocurrency" (filter: SC, 2020-2024)
2. Find: Internet and Mobile Association of India v. RBI (2020)
3. Check subsequent developments via Law Commission reports
4. Search: "Digital Personal Data Protection Act 2023" cross-references

## Tools Required

This skill uses:
- **Read**: Access reference files
- **Grep**: Search for keywords in protocols
- **Bash**: Execute Python research scripts

## Disclaimer

This skill provides research methodology guidance. It does not constitute legal advice. Always:
- Verify all citations against primary sources
- Check currency of law as of research date
- Consult qualified advocates for legal opinions
- Do not rely solely on secondary sources

---

**Skill Version**: 1.0.0
**Last Updated**: 2025-12-05
**Part of**: Indian Law Knowledge Ecosystem
**Dependencies**: legal-citation-validator
