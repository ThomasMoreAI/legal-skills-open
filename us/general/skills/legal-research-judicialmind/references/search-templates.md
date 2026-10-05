# Legal Research Search Strategies

## Overview

Effective legal research combines strategic search techniques with efficient use of available databases. This guide covers search methodologies for major legal research platforms.

## Boolean Search Fundamentals

### Core Operators

| Operator | Function | Example |
|----------|----------|---------|
| AND | Both terms required | contract AND breach |
| OR | Either term acceptable | employee OR worker |
| NOT | Excludes term | negligence NOT gross |
| " " | Exact phrase | "summary judgment" |
| ( ) | Groups terms | (contract OR agreement) AND breach |

### Proximity Operators

**Westlaw:**
| Operator | Function | Example |
|----------|----------|---------|
| /s | Same sentence | breach /s contract |
| /p | Same paragraph | negligence /p standard |
| /n | Within n words | employment /5 discrimination |
| +n | Within n words, in order | motion +3 dismiss |

**Lexis:**
| Operator | Function | Example |
|----------|----------|---------|
| w/s | Same sentence | breach w/s contract |
| w/p | Same paragraph | negligence w/p standard |
| w/n | Within n words | employment w/5 discrimination |
| pre/n | Within n words, preceding | motion pre/3 dismiss |

### Wildcards and Expanders

**Root Expanders:**
```
employ! = employ, employee, employer, employment, employed
negligen! = negligence, negligent, negligently
```

**Character Wildcards:**
```
wom*n = woman, women
defen*ant = defendant, defendants
```

## Search Strategy Framework

### Step 1: Define the Research Question

```
RESEARCH QUESTION TEMPLATE

Legal Issue: _________________________________
Jurisdiction: ________________________________
Relevant Facts: ______________________________
Key Parties/Entities: ________________________
Time Period: _________________________________
Type of Authority Needed: ____________________
```

### Step 2: Identify Search Terms

```
TERM DEVELOPMENT WORKSHEET

Core Concepts:
1. [Main legal concept] → synonyms: ____________
2. [Secondary concept] → synonyms: ____________
3. [Factual element] → synonyms: ______________

Legal Terms of Art:
- [Specific legal terminology]
- [Statutory language]
- [Standard phrases]

Factual Terms:
- [Industry-specific terms]
- [Common descriptions]
- [Party-type identifiers]
```

### Step 3: Construct Searches

```
SEARCH BUILDING PROCESS

1. Start Narrow:
   "summary judgment" /s "breach of contract" /s material

2. Expand if Too Few Results:
   "summary judgment" /p breach /p contract

3. Narrow if Too Many Results:
   Add jurisdictional filter
   Add date restriction
   Add additional required terms

4. Use Alternatives:
   (dismiss! OR "summary judgment") /p (breach OR violat!)
   /p (contract OR agreement)
```

## Platform-Specific Tips

### Westlaw Edge

**Content Types:**
- Cases: Federal and state courts
- Statutes: Annotated codes
- Regulations: CFR with history
- Secondary: Treatises, law reviews, practice guides
- Briefs: Court filings
- Expert Materials: Daubert, expert testimony

**Efficient Features:**
```
Filters:
- Jurisdiction dropdown
- Date range slider
- Document type selectors
- Key Number System

Advanced Search:
- Field searches: TI(title) TE(text) SY(synopsis)
- Locate in Results
- Search Within Results

KeyCite:
- Citing References
- Negative Treatment
- Table of Authorities
```

**Sample Searches:**
```
Employment discrimination:
title vii /s "disparate impact" /s "business necessity"

Contract formation:
(offer /s accept!) /p (contract OR agreement) /p (form! OR creat!)

Personal injury:
negligence /s (duty OR breach) /s proximate /s cause
```

### Lexis+

**Content Types:**
- Cases: Comprehensive coverage
- Statutes: Annotated codes
- Regulations: Administrative materials
- Secondary: Matthew Bender, law reviews
- News: Legal news, business news
- Public Records: Company, property, people

**Efficient Features:**
```
Filters:
- Practice area filters
- Timeline visualization
- Document segments

Search Tools:
- Headnotes search
- Segment searching
- More Like This

Shepard's Citations:
- Citing Decisions
- Treatment analysis
- Table of Authorities
```

**Sample Searches:**
```
Securities fraud:
"10b-5" w/p scienter w/p (intent! OR reckless!)

ERISA:
erisa w/s fiduciary w/s (duty OR breach OR prudent!)

Products liability:
(defect! OR dangerous) w/s (design OR manufactur! OR warn!)
```

### Bloomberg Law

**Content Types:**
- Cases: All jurisdictions
- Statutes: 50-state surveys
- Regulations: Federal and state
- Transactional: Deal analysis, precedent
- Dockets: Full docket coverage
- Practical Guidance: Practice centers

**Efficient Features:**
```
Analytics:
- Litigation Analytics
- Points of Law
- Smart Code

Practical Tools:
- Clause analysis
- Contract templates
- Deal comparison

Bloomberg Intelligence:
- Legal analyst reports
- Industry analysis
```

**Sample Searches:**
```
M&A:
merger w/5 (material w/3 adverse w/3 change)

Banking:
"qualified residential mortgage" OR QRM

Healthcare:
stark w/p exception w/p (fair market OR commercially reasonable)
```

## Research Workflows

### Case Research Workflow

```
CASE RESEARCH PROTOCOL

1. Find One Good Case
   - Start with secondary source cite
   - Or use natural language search
   - Or start with known statute

2. Expand from That Case
   - Check headnotes/topics
   - Find citing references
   - Check cited authorities
   - Search for similar facts

3. Update and Verify
   - KeyCite/Shepardize all cases
   - Check for negative treatment
   - Confirm still good law

4. Organize Results
   - Most authoritative first
   - Group by issue
   - Note circuit splits
   - Track unfavorable authority
```

### Statutory Research Workflow

```
STATUTORY RESEARCH PROTOCOL

1. Find Relevant Statute
   - Search annotated code
   - Check popular name table
   - Start from secondary source

2. Read in Context
   - Read surrounding sections
   - Check definitions section
   - Review legislative history

3. Find Interpretive Authority
   - Case annotations
   - Agency regulations
   - Legislative history
   - Secondary sources

4. Update
   - Check for amendments
   - Pending legislation
   - Recent cases interpreting
```

### Multi-Jurisdictional Research

```
50-STATE SURVEY APPROACH

1. Identify the Question
   - Precise legal question
   - Relevant fact patterns

2. Find Survey Starting Points
   - ALR annotations
   - Law review surveys
   - Treatise state-by-state sections
   - Bloomberg 50-state surveys

3. Verify and Update
   - Each jurisdiction
   - Recent changes
   - Pending legislation

4. Create Comparison Chart
   - Standard elements
   - Variations
   - Majority/minority rules
```

## Search Templates by Practice Area

### Contract Disputes

```
Formation:
(offer w/3 accept!) w/p (contract OR agreement)

Breach:
breach! w/p (material OR substantial) w/p (contract OR agreement)

Damages:
(contract OR agreement) w/p (consequential OR incidental OR
expectation) w/p damages

Defenses:
(statute w/3 fraud) OR (parol evidence) OR (unconscionab!)
```

### Employment Law

```
Discrimination:
(title vii OR "civil rights act") w/p (discriminat! OR retaliat!)
w/p (race OR gender OR sex OR religion OR national origin)

Wage and Hour:
(flsa OR "fair labor standards") w/p (exempt! OR overtime OR
minimum wage)

Wrongful Termination:
(wrongful OR unlawful) w/3 (terminat! OR discharg! OR dismiss!)
```

### Intellectual Property

```
Patent Infringement:
(claim construction OR markman) w/p (patent! w/3 infring!)

Trademark:
(likelihood w/3 confusion) w/p (trademark OR service mark)

Trade Secret:
(trade secret OR confidential information) w/p (misappropriat!
OR disclosure)
```

### Personal Injury

```
Negligence:
(duty w/3 care) w/p breach w/p (proximate OR actual) w/p cause

Premises Liability:
(slip OR trip OR fall) w/p (invitee OR licensee OR trespasser)

Products Liability:
(product! w/3 liab!) w/p (defect! w/3 (design OR manufactur! OR warn!))
```

## Research Documentation

### Search Log Template

```
RESEARCH LOG

Matter: _________________________________
Researcher: _____________________________
Date: __________________________________

Search 1:
Database: _______________________________
Search String: __________________________
Results: ________________________________
Relevant Hits: __________________________

Search 2:
[Continue for each search]

Key Authorities Found:
1. _____________________________________
2. _____________________________________
3. _____________________________________

Issues Requiring Further Research:
_______________________________________

Time Spent: _____________________________
```

## Cost Management

### Efficiency Tips

1. **Plan before searching** - Reduce trial and error
2. **Use free resources first** - Google Scholar, court websites
3. **Start narrow** - Expand only if needed
4. **Use headnotes/topics** - More targeted than full-text
5. **Batch similar research** - Same session efficiencies
6. **Download, don't revisit** - Save documents locally
7. **Know database strengths** - Use the right tool for the job
