---
name: search-prior-art-pjt222
title: Search Prior Art
description: Search for prior art relevant to a specific invention or patent claim. Covers patent literature, non-patent literature (academic papers, products, open source), defensive publications, and standard-essential patents. Use when evaluating whether an invention is novel and non-obvious before filing, challenging the validity of an existing patent, supporting a freedom-to-operate analysis, documenting a defensive publication, or responding to a patent office action questioning novelty or obviousness.
author: pjt222
author_url: https://github.com/pjt222/agent-almanac/tree/main/i18n/caveman/skills/search-prior-art
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# Search Prior Art

Run structured prior art search to find publications, patents, products, disclosures predating specific invention. Used to assess patentability (can this be patented?), challenge validity (should this patent have been granted?), or establish freedom-to-operate (is this design covered by existing rights?).

## When Use

- Evaluating whether invention is novel + non-obvious before filing patent
- Challenging validity of existing patent by finding prior art examiner missed
- Supporting freedom-to-operate analysis by finding prior art that limits blocking patent's scope
- Documenting defensive publication to prevent others from patenting concept
- Responding to patent office action that questions novelty or obviousness

## Inputs

- **Required**: Invention description (what does, how works, what problem solves)
- **Required**: Search purpose (patentability, invalidity, FTO, defensive)
- **Required**: Critical date (filing date of patent app, or invention date for prior art)
- **Optional**: Known related patents or publications
- **Optional**: Tech classification codes (IPC, CPC)
- **Optional**: Key inventors or companies in field

## Steps

### Step 1: Decompose Invention into Searchable Elements

Break invention into constituent technical features.

1. Read invention description (or patent claims if searching against existing patent)
2. Extract **essential elements** — each independent technical feature.
   - What components does it have?
   - What steps does process follow?
   - What technical effect does it achieve?
   - What problem does it solve and how?
3. Identify **novel combination** — what makes this different from known art.
   - New element added to known elements?
   - New combination of known elements?
   - Known element applied in new field?
4. Generate search terms per element.
   - Technical terms, synonyms, abbreviations
   - Broader + narrower terms (hierarchy)
   - Alternative descriptions of same concept
5. Document **Search Map**: elements, terms, relationships

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

**Got:** Complete decomposition with search terms per element. Novel combination identified — this is what search must either find (to invalidate) or confirm absent (to support novelty).

**If fail:** Invention too abstract to decompose? Ask for more specific description. Claims unclear? Focus on broadest reasonable interpretation of each claim element.

### Step 2: Search Patent Literature

Search patent databases systematically.

1. Construct queries combining element terms.
   - Search each element individually first (broad)
   - Then combine elements to find closer art (narrow)
   - Use classification codes to filter by tech area
2. Search multiple databases.
   - **Google Patents**: Good for full-text search, free, large corpus
   - **USPTO PatFT/AppFT**: US patents + applications, official source
   - **Espacenet**: European patents, excellent classification search
   - **WIPO Patentscope**: PCT applications, global coverage
3. Apply date filters.
   - Prior art must predate **critical date** (filing date or priority date)
   - Include publications up to 1 year before filing (grace period varies by jurisdiction)
4. For each relevant result, record.
   - Document number, title, filing date, publication date
   - Which elements it discloses (map to Search Map)
   - Whether it discloses novel combination
5. Classify results by relevance.
   - **X reference**: Discloses invention alone (anticipation)
   - **Y reference**: Discloses key elements, combinable with other refs (obviousness)
   - **A reference**: Background art, defines general state of art

**Got:** Classified list of patent references mapped to invention elements. X references (if found) = showstoppers for novelty. Y references = building blocks for obviousness arguments.

**If fail:** No relevant patent art found? Does not mean novel — non-patent literature (Step 3) may have critical reference. Absence in one database does not mean absence everywhere.

### Step 3: Search Non-Patent Literature

Search academic papers, products, open source, other non-patent disclosures.

1. **Academic literature**.
   - Google Scholar, arXiv, IEEE Xplore, ACM Digital Library
   - Search using same terms from Step 1
   - Conference papers + workshop proceedings often predate patent filings
2. **Products and commercial disclosures**.
   - Product docs, user manuals, marketing materials
   - Internet Archive (Wayback Machine) for date-verified web content
   - Trade publications + press releases
3. **Open source and code**.
   - GitHub, GitLab — search for implementations of technical features
   - README files, docs, commit histories for date evidence
   - Software releases with version dates
4. **Standards and specifications**.
   - IEEE, IETF (RFCs), W3C, ISO standards
   - Standards-essential patents must be disclosed; search standard bodies' IP databases
5. **Defensive publications**.
   - IBM Technical Disclosure Bulletin
   - Research Disclosure journal
   - IP.com Prior Art Database
6. For each result, verify **publication date** before critical date.
   - Web pages: use Wayback Machine for date evidence
   - Software: use release dates or commit timestamps
   - Papers: use publication date, not submission date

**Got:** Non-patent references that complement patent search. Academic papers + open-source code often most powerful prior art — describe technical details more explicitly than patents.

**If fail:** Non-patent literature sparse? Tech may be primarily developed in corporate R&D (patent-heavy). Shift emphasis to patent literature, focus on combination-based obviousness argument.

### Step 4: Analyze and Map Results

Evaluate how collected prior art relates to invention.

1. Make **claim chart** mapping prior art to invention elements.

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

2. Assess **novelty**: Does any single reference disclose all elements?
   - If yes → invention anticipated (not novel)
   - If no → invention may be novel (proceed to obviousness)
3. Assess **obviousness**: Can small number of references (2-3) be combined to cover all elements?
   - Motivation to combine? (would skilled person see reason to combine these?)
   - References teach away from combination? (suggest it would not work?)
4. For **FTO searches**: Does prior art narrow blocking patent's claims?
   - Prior art that overlaps with blocking patent's claims limits enforceable scope
5. Document analysis clear with citation to specific passages

**Got:** Clear claim chart showing which elements covered by which references, with assessment of novelty + obviousness. Each mapping cites specific passages or figures.

**If fail:** Claim chart shows gaps (elements not in any prior art)? Those gaps = potentially novel aspects. Focus follow-up searches on those specific gaps.

### Step 5: Document and Deliver

Package search results for intended use.

1. Write **Prior Art Search Report**.
   - Purpose + scope of search
   - Search methodology (databases, queries, date ranges)
   - Results summary (number of references found, classification breakdown)
   - Top references with detailed analysis (claim charts)
   - Assessment: novelty, obviousness, FTO implications
   - Limitations + recommendations for further search
2. Organize references.
   - Sorted by relevance (X first, then Y, then A)
   - Each reference with full bibliographic data + access link
   - Key passages highlighted or extracted
3. Recommendations by search purpose.
   - **Patentability**: File/don't file, suggested claim scope based on prior art gaps
   - **Invalidity**: Strongest combination of references, suggested legal argument
   - **FTO**: Risk level, design-around opportunities, licensing considerations
   - **Defensive**: Whether to publish as defensive disclosure based on white space found

**Got:** Complete, well-organized search report that supports intended decision. References accessible, analysis traceable.

**If fail:** Search inconclusive (no strong X or Y, but some background)? State conclusion clear: "No anticipatory art found; closest art addresses elements A and B but not C. Recommend filing with claims emphasizing element C." Inconclusive = valid + useful result.

## Checks

- [ ] Invention decomposed into distinct searchable elements
- [ ] Novel combination explicit identified
- [ ] Patent databases searched (min 2 databases)
- [ ] Non-patent literature searched (academic + products + open source)
- [ ] All references predate critical date (dates verified)
- [ ] Claim chart maps elements to references with passage citations
- [ ] Novelty + obviousness assessed with reasoning
- [ ] Results classified by relevance (X, Y, A references)
- [ ] Report includes methodology, limitations, recommendations
- [ ] Search reproducible (queries + databases documented)

## Pitfalls

- **Keyword tunnel vision**: Search only exact terms misses synonyms + alternative descriptions. Use term hierarchy from Step 1
- **Patent-only search**: Non-patent literature (papers, products, code) often more explicit than patents. Do not skip Step 3
- **Date carelessness**: Prior art must predate critical date. Brilliant reference from one day after filing date worthless
- **Ignore foreign language art**: Major inventions may first appear in Chinese, Japanese, Korean, German patent literature. Machine translation makes these searchable
- **Confirmation bias**: Search to confirm novelty rather than find invalidating art. Best search tries hardest to find closest art
- **Stop too early**: First few results rarely best. Iterate search terms based on what early results reveal about field's vocabulary

## See Also

- `assess-ip-landscape` — Broader landscape mapping that contextualizes specific prior art searches
- `screen-trademark` — Trademark-specific conflict screening (different databases, different legal framework than patent prior art)
- `file-trademark` — Trademark filing procedures for when screening complete
- `review-research` — Literature review methodology overlaps significant with prior art search
- `security-audit-codebase` — Systematic search methodology parallels (thoroughness, documentation, reproducibility)
