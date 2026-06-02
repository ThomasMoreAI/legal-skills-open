---
name: search-prior-art-2
title: Search Prior Art
description: Prior art search for invention|patent claim. Patent + non-patent (academic, products, OSS), defensive pubs, standard-essential patents. Use → eval novelty+non-obvious pre-file, challenge existing patent validity, support FTO analysis, document defensive pub, respond to office action questioning novelty.
author: pjt222
author_url: https://github.com/pjt222/agent-almanac/tree/main/i18n/caveman-ultra/skills/search-prior-art
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# Search Prior Art

Structured prior art search → find pubs|patents|products|disclosures predating invention. Used for patentability (can patent?), validity challenge (should have been granted?), FTO (covered by existing rights?).

## Use When

- Eval novelty+non-obvious pre-file
- Challenge existing patent validity → find art examiner missed
- Support FTO → find art limiting blocking patent scope
- Document defensive pub → prevent others patenting concept
- Respond to office action questioning novelty|obviousness

## In

- **Required**: Invention desc (what, how, problem)
- **Required**: Purpose (patentability|invalidity|FTO|defensive)
- **Required**: Critical date (filing date or invention date)
- **Optional**: Known related patents|pubs
- **Optional**: Tech classification codes (IPC, CPC)
- **Optional**: Key inventors|companies

## Do

### Step 1: Decompose Invention

Break into constituent technical features.

1. Read desc (or claims if vs existing patent)
2. Extract **essential elements** — each independent feature:
   - Components?
   - Process steps?
   - Technical effect?
   - Problem + how solved?
3. ID **novel combination** — what's diff from known:
   - New element added to known?
   - New combo of known?
   - Known element new field?
4. Gen search terms per element:
   - Tech terms, synonyms, abbrev
   - Broader+narrower (hierarchy)
   - Alt descriptions
5. Doc **Search Map**: elements, terms, relationships

```
Search Map Example:
+------------------+-----------------------------------+-----------+
| Element          | Search Terms                      | Priority  |
+------------------+-----------------------------------+-----------+
| Attention layer  | attention mechanism, self-         | High      |
|                  | attention, multi-head attention    |           |
| Sparse routing   | mixture of experts, sparse MoE,   | High      |
|                  | top-k routing, expert selection    |           |
| Training method  | knowledge distillation, teacher-   | Medium    |
|                  | student, progressive training      |           |
+------------------+-----------------------------------+-----------+
```

→ Complete decomposition w/ terms per element. Novel combo ID'd → search must find (invalidate) or confirm absent (support novelty).

If err: too abstract → ask more specific. Claims unclear → broadest reasonable interp per element.

### Step 2: Search Patent Literature

Patent DBs systematic.

1. Construct queries:
   - Each element individually first (broad)
   - Combine to find closer art (narrow)
   - Classification codes filter by tech area
2. Multi DBs:
   - **Google Patents**: Full-text, free, large
   - **USPTO PatFT/AppFT**: US patents+apps, official
   - **Espacenet**: EU, excellent classification
   - **WIPO Patentscope**: PCT, global
3. Date filters:
   - Prior art must predate **critical date**
   - Up to 1yr pre-filing (grace varies by jurisdiction)
4. Per relevant result record:
   - Doc number, title, filing date, pub date
   - Which elements disclosed (map to Search Map)
   - Discloses novel combo?
5. Classify by relevance:
   - **X**: Discloses invention alone (anticipation)
   - **Y**: Key elements, combinable (obviousness)
   - **A**: Background art

→ Classified patent ref list mapped to elements. X (if found) = showstoppers for novelty. Y = building blocks for obviousness.

If err: no relevant patent art → doesn't mean novel — non-patent (Step 3) may have critical ref. Absence in 1 DB ≠ absence everywhere.

### Step 3: Non-Patent Literature

Academic, products, OSS, other.

1. **Academic**:
   - Google Scholar, arXiv, IEEE Xplore, ACM Digital Library
   - Same Step 1 terms
   - Conf papers + workshop proceedings often predate patents
2. **Products + commercial**:
   - Product docs, manuals, marketing
   - Internet Archive (Wayback) for date-verified web
   - Trade pubs + press releases
3. **OSS + code**:
   - GitHub, GitLab — search impls of features
   - READMEs, docs, commit history for date evidence
   - Software releases w/ ver dates
4. **Standards**:
   - IEEE, IETF (RFCs), W3C, ISO
   - Standards-essential patents must be disclosed; search standard bodies' IP DBs
5. **Defensive pubs**:
   - IBM Technical Disclosure Bulletin
   - Research Disclosure journal
   - IP.com Prior Art DB
6. Verify **pub date** before critical date:
   - Web: Wayback for date evidence
   - Software: release dates|commit timestamps
   - Papers: pub date not submission

→ Non-patent refs complement patent search. Academic + OSS often most powerful — describe details more explicitly than patents.

If err: non-patent sparse → tech primarily corp R&D (patent-heavy). Shift emphasis to patent + combo-based obviousness.

### Step 4: Analyze + Map

Eval how art relates to invention.

1. **Claim chart** mapping art → elements:

```
Claim Element vs. Prior Art Matrix:
+------------------+--------+--------+--------+--------+
| Element          | Ref #1 | Ref #2 | Ref #3 | Ref #4 |
+------------------+--------+--------+--------+--------+
| Element A        |   X    |   X    |        |   X    |
| Element B        |        |   X    |   X    |        |
| Element C        |   X    |        |   X    |        |
| Novel combo A+B+C|        |        |        |        |
+------------------+--------+--------+--------+--------+
X = element disclosed in this reference
```

2. **Novelty**: Single ref discloses all elements?
   - Yes → anticipated (not novel)
   - No → may be novel (proceed obviousness)
3. **Obviousness**: Few refs (2-3) combinable to cover all?
   - Motivation to combine? (skilled person sees reason?)
   - Teach away? (suggest wouldn't work?)
4. **FTO**: Does art narrow blocking patent claims?
   - Art overlapping blocking patent's claims limits enforceable scope
5. Document analysis w/ specific passage citations

→ Clear claim chart showing element coverage by refs, w/ novelty + obviousness assessment. Each mapping cites specific passages|figures.

If err: chart shows gaps (elements not in any art) → those = potentially novel. Focus follow-up on specific gaps.

### Step 5: Document + Deliver

Package for intended use.

1. Write **Prior Art Search Report**:
   - Purpose + scope
   - Methodology (DBs, queries, date ranges)
   - Results summary (count, classification breakdown)
   - Top refs w/ detailed analysis (claim charts)
   - Assessment: novelty, obviousness, FTO implications
   - Limitations + further-search recommendations
2. Organize refs:
   - Sorted by relevance (X first, Y, A)
   - Each w/ full bibliographic + access link
   - Key passages highlighted|extracted
3. Recommendations by purpose:
   - **Patentability**: File|don't, suggested claim scope by gaps
   - **Invalidity**: Strongest combo, suggested legal arg
   - **FTO**: Risk level, design-around opportunities, licensing
   - **Defensive**: Whether to publish defensive disclosure based on white space

→ Complete organized report directly supporting decision. Refs accessible, analysis traceable.

If err: inconclusive (no strong X|Y, but relevant background) → state clearly: "No anticipatory art; closest addresses A+B not C. Recommend file w/ claims emphasizing C." Inconclusive valid + useful.

## Check

- [ ] Invention decomposed into searchable elements
- [ ] Novel combo explicitly ID'd
- [ ] Patent DBs searched (min 2)
- [ ] Non-patent searched (academic + products + OSS)
- [ ] All refs predate critical date (verified)
- [ ] Claim chart maps elements w/ passage citations
- [ ] Novelty + obviousness assessed w/ reasoning
- [ ] Classified (X, Y, A)
- [ ] Report has methodology, limitations, recommendations
- [ ] Reproducible (queries + DBs documented)

## Traps

- **Keyword tunnel vision**: Exact terms only misses synonyms. Use Step 1 hierarchy.
- **Patent-only search**: Non-patent (papers, products, code) often more explicit. Don't skip Step 3.
- **Date carelessness**: Must predate critical date. Brilliant ref 1 day after = worthless.
- **Ignore foreign**: Major inventions may first appear in CN|JP|KR|DE patents. MT makes searchable.
- **Confirmation bias**: Searching to confirm novelty vs to find invalidating art. Best search tries hardest to find closest.
- **Stop too early**: First results rarely best. Iterate based on field vocabulary revealed.

## →

- `assess-ip-landscape` — broader landscape mapping
- `screen-trademark` — TM-specific (diff DBs + legal frame than patent)
- `file-trademark` — TM filing post-screen
- `review-research` — lit review methodology overlaps
- `security-audit-codebase` — systematic methodology parallels (thoroughness, doc, reproducibility)
