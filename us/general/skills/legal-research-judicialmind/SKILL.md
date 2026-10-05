---
name: legal-research-judicialmind
title: Legal Research
description: Legal research and case law analysis skill. Use when the user needs to find case law, analyze statutes, search legal precedents, verify citations, or conduct comprehensive legal research. Triggers on keywords like "case law", "legal research", "precedent", "statute", "citation", "find cases", "Shepardize", "KeyCite", "legal authority".
author: judicialmind
author_url: https://github.com/judicialmind/legal-skills/tree/main/skills/legal-research
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: general
language: en
sources:
- title: Citation Guide
  path: references/citation-guide.md
- title: Search Templates
  path: references/search-templates.md
- title: Sources
  path: references/sources.md
---

# Legal Research

This skill provides expert guidance for conducting thorough legal research across all practice areas and jurisdictions.

## Core Capabilities

### 1. Case Law Research
- Federal and state court opinions
- Circuit court analysis and splits
- Supreme Court precedent tracking
- Unpublished opinion considerations

### 2. Statutory Research
- Federal statute interpretation (U.S.C.)
- State statute variations
- Legislative history analysis
- Regulatory code research (C.F.R.)

### 3. Citation Verification
- Shepard's Citations / KeyCite analysis
- Treatment history (followed, distinguished, overruled)
- Negative treatment alerts
- Subsequent history tracking

### 4. Secondary Sources
- Treatises and hornbooks
- Law review articles
- Practice guides
- Restatements

## Research Methodology

### IRAC Framework
1. **Issue**: Identify the precise legal question
2. **Rule**: Find governing law and standards
3. **Application**: Analyze how law applies to facts
4. **Conclusion**: Synthesize findings

### Search Strategy
1. Start with secondary sources for unfamiliar areas
2. Identify key cases from annotations
3. Use headnotes/topics for comprehensive searching
4. Verify currency with citators
5. Check for recent developments

## Authoritative Sources

### Primary Databases (Subscription)
| Source | Strengths | Access |
|--------|-----------|--------|
| Westlaw | KeyCite, comprehensive | westlaw.com |
| LexisNexis | Shepard's, news | lexisnexis.com |
| Bloomberg Law | Transactional, dockets | bna.com |

### Free Legal Resources
| Source | Content | URL |
|--------|---------|-----|
| Cornell LII | Statutes, CFR, USC | law.cornell.edu |
| Google Scholar | Case law, articles | scholar.google.com |
| CourtListener | Federal/state cases | courtlistener.com |
| Justia | Cases, statutes | justia.com |
| Caselaw Access | Historical cases | case.law |

### Court Databases
| Court | Database | URL |
|-------|----------|-----|
| Federal | PACER | pacer.gov |
| SCOTUS | supremecourt.gov | supremecourt.gov |
| State | Varies | [state].courts.gov |

## Citation Format

### Bluebook Standard
```
[Case Name], [Volume] [Reporter] [Page], [Pinpoint] ([Court] [Year])

Example:
Miranda v. Arizona, 384 U.S. 436, 444 (1966)
```

### Common Reporters
- U.S. - Supreme Court
- F.3d/F.4th - Federal Circuit Courts
- F. Supp. 3d - Federal District Courts
- Regional reporters (N.E.2d, P.3d, etc.)

## Research Workflow

```
┌─────────────────────────────────────────────────┐
│  1. Define Research Question                     │
│     - Identify legal issues                      │
│     - Note jurisdiction and time constraints     │
└─────────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────┐
│  2. Background Research                          │
│     - Secondary sources for overview             │
│     - Identify key terms and concepts            │
└─────────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────┐
│  3. Find Primary Authority                       │
│     - Case law search                            │
│     - Statutory research                         │
│     - Regulatory review                          │
└─────────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────┐
│  4. Verify & Update                              │
│     - Shepardize/KeyCite all authorities         │
│     - Check for recent developments              │
│     - Note any negative treatment                │
└─────────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────┐
│  5. Analyze & Synthesize                         │
│     - Organize by weight of authority            │
│     - Identify binding vs. persuasive            │
│     - Note circuit splits or conflicts           │
└─────────────────────────────────────────────────┘
```

## Best Practices

### Do
- Always verify citations are still good law
- Check for recent amendments to statutes
- Note the jurisdiction and binding effect
- Document your search strategy
- Use multiple databases for comprehensive coverage

### Don't
- Rely solely on headnotes without reading cases
- Cite unpublished opinions without checking rules
- Ignore negative treatment history
- Skip secondary sources in unfamiliar areas
- Assume federal law applies without checking state variations

## Integration with Other Skills

- **brief-writing**: Research feeds into brief drafting
- **litigation**: Motion research and case strategy
- **contract-lifecycle**: Statutory requirements research
- **compliance-tracking**: Regulatory research

## Reference Files

For detailed source lists and search templates, see:
- `references/sources.md` - Comprehensive legal database guide
- `references/search-templates.md` - Common search strategies
- `references/citation-guide.md` - Citation format reference
