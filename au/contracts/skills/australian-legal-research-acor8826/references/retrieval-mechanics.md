# Retrieval Mechanics

**Every agent reads this before fetching anything.** It owns the *how* of retrieval so the orchestrator and agent briefs can stay about *strategy*. Carried over from the base skill and extended with Layer 0 (jurisd), the citator recipe, and source-authority ranking.

---

## Layer 0 — jurisd (preferred retrieval backend, optional)

If the `jurisd` MCP server is registered (an optional local-first AU/NZ legal MCP — see the skill's install notes), **prefer its tools over everything below.** jurisd provides authority-ranked AustLII search with pinpoint extraction, clean full-text fetch (HTML/PDF), deterministic provision + subsection lookup, an offline citation-graph tool, and AGLC4 formatting — native versions of the things the fallback stack does by hand. It shares this skill's "degrade visibly, never silently" philosophy, so it slots into the single-threaded-fallback model cleanly.

**Precedence + fallback rule.** Once per research session, if jurisd is available, call `list_data_modules` to see what offline coverage exists. Then, for each retrieval need, try the jurisd tool first and fall through to the fallback stack (Primitives, the citator recipe, the cheat sheet — all below) when **any** of these hold:
- jurisd is not registered;
- a jurisd tool returns a typed not-found / empty result;
- the feature needs a module that isn't installed (the offline citator and offline provision lookup are bounded by installed modules).

Never treat a jurisd miss as the end of the search — fall through. Never treat jurisd as a hard dependency — the skill must work without it.

**Tool → task mapping** (jurisd tool ⇒ our need ⇒ fallback if jurisd is absent/empty):

| Need | jurisd (Layer 0) | Fallback |
|------|------------------|----------|
| Find cases on a topic | `search_cases` (authority-ranked, pinpoints; `method` auto/title/phrase/boolean, `jurisdiction`, `sortBy`) | `web_search` + cheat sheet |
| Find/verify a known citation | `resolve_citation` (`mode=auto`/`validate`) | CaseLaw search / AustLII viewdoc |
| Full judgment text | `fetch_document_text` (HTML/PDF; `citeKey` saves a local copy) | `web_fetch` / Chrome |
| **Who cites this case (citator)** | `find_citing` (offline, module-bounded — **legislation-only today**, so no help for case citators yet); `search_cases` on the case name to *discover* citing judgments | **the citator recipe below** (the working method for case-cites-case) |
| Read a provision + subsections | `get_provision`; `get_act_structure` | legislation.gov.au / legislation.nsw.gov.au / classic.austlii |
| Concept recall over a corpus | `semantic_search_local` (needs module + embeddings) | `web_search` |
| AGLC4 citation / para pinpoint | `format_citation` (`mode=pinpoint` with `url` + `paragraphNumber`/`phrase`) | hand-format per `references/aglc4-citation.md` |
| Cache / bibliography | `cite`, `bibliography` (`op=export` → `.bib`) | the research ledger + the AGLC4 Table of Authorities (`references/aglc4-citation.md` §5) |

**Notes for the agents.**
- The **citator** is the biggest historical gap, and **jurisd v0.5.0 does not close it**: there is no live citator, and `find_citing` (offline) is bounded by installed modules — `legislation-cth` carries legislation→legislation edges only, so it returns nothing for case-cites-case (confirmed: `find_citing` on Nobarani → empty). For "who cites this case", the **free-source citator recipe below is the working method**, optionally seeded by `search_cases` on the case name to surface citing judgments. If a decisions module with case→case edges is later installed, `find_citing` becomes the offline citator and this note should be revisited.
- For **legislation subsection extraction** (the legislation agent's required output), `get_provision` returns the provision deterministically — offline if the covering module is installed (`legislation-cth` covers Commonwealth law, directly relevant to Federal Court matters); else fall through to the registers.
- Every jurisd local answer carries `metadata.source = "local_module"` with a snapshot date + staleness advisory — record currency from it.
- jurisd's AustLII fetches are **tier-1 primary** for the source-authority ranking; a jurisd-fetched judgment satisfies the "confirm on a primary source" rule.
- The validation gate's existence check can use `resolve_citation mode=validate`; AGLC4 form via `format_citation`.
- **Live / enhanced layers (host-configured).** jurisd's `search_cases`/`search_legislation` hit live AustLII and, where the host has search keys set (Exa primary, Tavily opt-in), fall back to those when AustLII is Cloudflare-blocked — so a search *miss* is a genuine miss, not a transport failure. `semantic_search_local` returns baseline local-cosine results, or Isaacus-reranked results when that key is set; the ranking is usable either way. None of this changes how you call the tools — jurisd handles it internally and degrades visibly.

---

## Primitives (fallback stack)

> Use these when jurisd (Layer 0) is unavailable or returns empty. They are the skill's floor — it works with only these.

| Primitive | Use it for |
|-----------|-----------|
| `web_fetch` / `WebFetch` | CaseLaw NSW pages, NSW legislation, the Federal Register, court/official PDFs — these accept plain fetches |
| Web search (`WebSearch` in Claude Code; `web_search` elsewhere — the runtime's search tool) | Finding URLs when the citation/source isn't known (Google has full-text indexed AustLII, CaseLaw, Jade, court sites); resolving a citation to a Jade article; the citator recipe. See the **web-search recipes** below. |
| Claude in Chrome (`navigate`, `get_page_text`, `read_page`, `find`) | AustLII case + legislation pages **when a bare fetch is blocked** — AustLII *may* reject bare fetches with 403/410 (notably under Cowork). Try `web_fetch` first; fall back to Chrome only on a 403/410. In a plain `web_fetch` environment AustLII often fetches directly. **Jade (jade.io) always requires Chrome** — it 403s every bare fetch. |

**Verification is non-negotiable.** Never assert a citation, quote, holding, judge, or date from memory — fetch the source. If a fetch fails, mark the item UNVERIFIED and say so. States are verified / suspect / overridden, never "probably fine".

### Web-search recipes (per need)

Web search is a first-class retrieval path, not just a fallback. The recipes that work:

- **Topic discovery:** proposition + court, e.g. `procedural fairness new trial FCAFC`, optionally
  `site:austlii.edu.au cases/cth/FCA` to bias to a court's judgments (never the bare domain).
- **Citation → URL resolution:** the citation in quotes plus a host bias —
  `"[2018] HCA 36" site:austlii.edu.au` or `"[2018] HCA 36" site:jade.io` (Jade article pages are
  well indexed and surface the case name + report citations in the snippet).
- **Party-name discovery:** `"Smith v Jones" [year]` + court code if known.
- **Citator (forward citations):** the citator recipe below — citation + proposition + target court.
- **Practice-note discovery:** note identifier + court site, e.g. `"SC Eq 3" site:supremecourt.nsw.gov.au`.
- **Legislation ID discovery:** `"Bankruptcy Act 1966" site:legislation.gov.au`.

Search-result snippets are **leads**, not sources — a snippet can verify that a page exists and
roughly what it holds, but every relied-on fact still comes from fetching the page itself.

---

## Jade (BarNet Jade, jade.io) — free-tier judgment source & citator lead

Jade hosts authentic copies of Australian judgments (all HCA, federal and state superior courts)
with paragraph anchors and a citation network. The free tier shows judgment text and basic
citation panels; JadePro features (advanced citator views, alerts) sit behind a login — that
logged-in path belongs to the **`jade-research`** sibling skill, not this one.

**Access mechanics (observed):**
1. **Bare `web_fetch` to jade.io always returns 403** — both `jade.io/article/<id>` and
   `jade.io/summary/mnc/<Y>/<COURT>/<N>`. Do not retry; go via search + Chrome.
2. **Resolve a citation to its Jade article via web search:** `site:jade.io "<neutral citation>"`
   → `https://jade.io/article/<id>` (e.g. `site:jade.io "[1992] HCA 23"` → `jade.io/article/67683`,
   and the snippet itself confirms the case name + report citations — a useful existence lead).
3. **Open the article via Claude in Chrome** (`navigate` → `get_page_text`) — Jade is a
   JavaScript app, so Chrome is the only primitive that renders it.
4. **MNC summary URL pattern** (hand-construction): `https://jade.io/summary/mnc/<YEAR>/<COURT>/<NUMBER>`.

**What to use Jade for:**
- **Judgment text fallback** when AustLII 403s *and* the case is not on CaseLaw NSW / the HCA site.
- **Citator leads** — the article page's citation panel ("cited by" / cases citing) seeds the
  citator recipe; harvest the candidates, then confirm each on tier 1.
- **Citation resolution / existence leads** — the `site:jade.io` snippet confirms a medium-neutral
  citation maps to a real case with its report citations.

**Tier rule:** Jade is **tier 2** — authentic text, good for existence and text — but anything
relied on in a **filed document** is still confirmed on a tier-1 source (AustLII / CaseLaw NSW /
court site / register). If Chrome is not connected, Jade is unreachable (bare fetches 403);
say so and use the other tiers.

---

## Source-authority ranking (use the highest tier you can reach; required for anything relied on in court)

1. **Primary** — AustLII, CaseLaw NSW, the High Court site (hcourt.gov.au), Federal Register (legislation.gov.au), NSW legislation (legislation.nsw.gov.au). The judgment/statute itself.
2. **Official-party host / authentic aggregator** — a regulator or court publishing the judgment PDF (e.g. asic.gov.au, fedcourt.gov.au), and **BarNet Jade (jade.io)**, which hosts authentic judgment copies (see the Jade section above for access mechanics). Reliable for existence and text.
3. **Chambers / law-society summaries** — barristers' chambers case notes, Law Society journals, court bulletins. Good for *leads* and catchwords; confirm text on tier 1–2.
4. **General aggregators** — casenote.au, issuu, blogs, Lexology. **Leads only.** Never the sole basis for a citation relied on in court.

Rule: a finding may be *surfaced* from any tier, but anything that will be **relied upon in a filed document** must be confirmed on a **tier-1 primary source**. The validation gate records the tier consulted for each authority.

---

## Citator recipe — building a "cited by" list on free sources (fallback)

> **This is the working method for case citators.** jurisd v0.5.0 has no live citator, and its offline `find_citing` covers installed modules only (legislation today, not case→case). So for "cases citing X", use this recipe — optionally seeded by jurisd `search_cases` on the case name. (If a future jurisd decisions module adds case→case edges, prefer `find_citing` and treat this recipe as the fallback.)

AustLII's **LawCite** citator and **SINO** search are behind Cloudflare Turnstile and cannot be driven programmatically — **do not attempt them**. Build subsequent-treatment / citing-case lists this way instead:

1. **Do NOT use a bare `site:austlii.edu.au` search** for citator work — it returns AustLII's *recent-announcements / index* pages, not citing cases. (Observed failure mode.)
2. **Search the neutral citation + the proposition + the target court**, e.g.
   `"[2018] HCA 36" Federal Court procedural fairness new trial`. This surfaces later judgments that discuss it.
3. **Harvest authorities lists from judgment PDFs.** Later judgments list the cases they cite; official/chambers PDFs are indexed by Google. Finding the target in another judgment's authorities list is strong evidence of a citing case — then open that judgment to see *how* it was used.
4. **Harvest Jade's citation panel (tier-2 lead — the best free citator seed).** Resolve the target
   to its Jade article (`site:jade.io "<neutral citation>"` → `jade.io/article/<id>`), open it via
   Chrome (bare fetches 403 — see the Jade section), and read the cases-citing panel visible on the
   free tier. Each entry is a citing-case candidate to confirm on tier 1.
5. **Use other aggregator/citator summary pages as further leads** — casenote.au, chambers "case
   note" posts. Treat as tier-3/4: confirm on a primary source.
6. **For NSW citing cases**, search CaseLaw NSW full text directly:
   `web_fetch https://www.caselaw.nsw.gov.au/search?query=<URL-encoded case name or citation>`.
7. **Confirm each candidate** on a tier-1 source and record the pinpoint where it cites the target, plus the how-cited classification (followed / applied / cited-in-argument / mentioned-as-history / distinguished).

Always state the limitation in the memo: a full-text-search citator is not guaranteed exhaustive.

---

## Tool-selection cheat sheet

### Retrieving a known NSW case → CaseLaw NSW (`web_fetch`)
Official source, clean text, no header issues. Covers NSWSC, NSWCA, NSWDC, NSWLEC, NSWCCA, NSWCATxx, NSWIRComm, NSWChC.

Step 1 — find the decision ID:
```
web_fetch https://www.caselaw.nsw.gov.au/search?query=%5B2021%5D+NSWSC+741
```
The page returns up to 20 `/decision/<hex-id>` links. **Do not take the first** — it is often a featured/recent decision, not your match. Scan the anchors and pick the one whose displayed text contains the target citation `[YEAR] COURT NUMBER` exactly. If none match, the case may be non-NSW or older → AustLII via Chrome.

Step 2 — fetch the judgment:
```
web_fetch https://www.caselaw.nsw.gov.au/decision/<hex-id>
```
Official DOCX (downloadable copy): append `/export.docx`.

### Retrieving any other Australian court (HCA, FCA, FCAFC, VSC, QSC, …) → Claude in Chrome
AustLII rejects bare fetches (403/410); Chrome supplies headers. Construct the viewdoc URL from the medium-neutral citation `[YEAR] COURT NUMBER`:
```
https://www.austlii.edu.au/cgi-bin/viewdoc/au/cases/<state>/<COURT>/<YEAR>/<NUMBER>.html
```
Then `navigate(url=…)` → `get_page_text`. Capture the case name from `<title>` and the RTF/PDF links from the sidebar if a download is needed.

State paths for AustLII URLs:

| Court prefix | State path |
|--------------|-----------|
| HCA, FCAFC, FCA, AAT, AATA | `cth` |
| NSW* | `nsw` (but prefer CaseLaw NSW) |
| VSC, VSCA, VCC, VCAT | `vic` |
| QSC, QCA, QDC, QCAT | `qld` |
| SASC, SASCFC, SADC, SACAT | `sa` |
| WASC, WASCA, WADC, WASAT | `wa` |
| TASSC, TASFC | `tas` |
| ACTSC, ACTCA, ACAT | `act` |
| NTSC, NTCA | `nt` |

If Chrome isn't connected, the HCA site (hcourt.gov.au) and official court/regulator PDFs are tier-1/2 fallbacks for many judgments; otherwise note the limitation.

### Retrieving a case on Jade (free tier) → web search + Chrome
When AustLII is blocked or misses the case (see the Jade section above for the full mechanics):
```
1. WebSearch  site:jade.io "[YEAR] COURT NUMBER"   → https://jade.io/article/<id>
2. navigate https://jade.io/article/<id>  →  get_page_text     (bare web_fetch always 403s)
```
Tier 2: good for existence, text, and the citation panel; confirm on tier 1 before filing.

### Searching for cases on a topic (citation unknown)
`web_search` with the proposition + court, optionally `site:austlii.edu.au cases/cth/HCA` to bias to a court's judgments (not the bare domain). Open the best result via Chrome. For NSW, search CaseLaw NSW directly.

### Finding a case by party name
`web_search "Smith v Jones" [year]`, adding the court code if known. For likely-NSW: CaseLaw NSW `/search?query=Smith+v+Jones`.

### Subsequent treatment ("is this still good law")
Use the **citator recipe** above. AustLII's LawCite is walled — do not use it directly.

### Verifying a citation exists
1. NSW? Search CaseLaw NSW; if a decision matches, fetch and confirm the case name.
2. Other court? Construct the AustLII URL, open via Chrome. Loads with the expected name → valid. "Document not found" → wrong.
3. Cross-check party names; mismatches mean a wrong citation.
4. If the user attributes a proposition, find it in the page text; if absent, say so — don't paraphrase from memory.

**Refuse to confirm a citation you cannot fetch.** Say it appears wrong/unavailable rather than "probably correct".

### Extracting CaseLaw NSW metadata
CaseLaw exposes a `<dt>/<dd>` list — scan the page text for these labels and copy verbatim (do not fill from memory):
```
Medium Neutral Citation · Hearing dates · Decision date · Jurisdiction · Before ·
Catchwords · Parties · Cases Cited · Legislation Cited · Representation
```

---

## Legislation

### NSW
```
web_fetch https://legislation.nsw.gov.au/view/whole/html/inforce/current/act-YYYY-NNN
```
Specific section: append `#sec.XX`. As-amended single-section view:
`https://legislation.nsw.gov.au/view/html/inforce/current/act-YYYY-NNN#sec.XX`.
For currency as at a past date, use the point-in-time view rather than `current`.

Common slugs: Civil Procedure Act 2005 `act-2005-028`; Supreme Court Act 1970 `act-1970-052`; Evidence Act 1995 `act-1995-025`; Contracts Review Act 1980 `act-1980-016`; Conveyancing Act 1919 `act-1919-006`. UCPR: `sl-2005-0418#sec.X.X`.

### Commonwealth (Federal Register)
```
web_fetch https://www.legislation.gov.au/<ID>/latest/text
```
`<ID>` e.g. `C2004A00946`. Unknown ID → `web_search "Bankruptcy Act 1966" site:legislation.gov.au`. Use the point-in-time compilation for currency as at a past date.

### Commonwealth (AustLII consolidated Acts) → Chrome
Section-level pinpoint URLs:
```
navigate https://classic.austlii.edu.au/au/legis/cth/consol_act/<slug>/s<N>.html → get_page_text
```
Common slugs: Bankruptcy Act 1966 `ba1966142`; Corporations Act 2001 `ca2001172`; Federal Court of Australia Act 1976 `fcoaa1976249`; Competition and Consumer Act 2010 `caca2010265`.

**Extract the operative subsection text** for the memo, note defined terms and any cross-referenced rules/regs.

---

## URL patterns (hand-construction)
```
AustLII case:  https://www.austlii.edu.au/cgi-bin/viewdoc/au/cases/<state>/<COURT>/<YEAR>/<NUMBER>.html
AustLII RTF:   https://www.austlii.edu.au/au/cases/<state>/<COURT>/<YEAR>/<NUMBER>.rtf
AustLII PDF:   https://www.austlii.edu.au/cgi-bin/sign.cgi/au/cases/<state>/<COURT>/<YEAR>/<NUMBER>
CaseLaw NSW:   https://www.caselaw.nsw.gov.au/decision/<decision_id>
CaseLaw DOCX:  https://www.caselaw.nsw.gov.au/decision/<decision_id>/export.docx
NSW legis:     https://legislation.nsw.gov.au/view/html/inforce/current/<slug>
Cth legis:     https://www.legislation.gov.au/<ID>/latest/text
AustLII legis: https://classic.austlii.edu.au/au/legis/<state>/consol_act/<slug>/s<N>.html
```
State codes: `cth`, `nsw`, `vic`, `qld`, `sa`, `wa`, `tas`, `act`, `nt`.

---

## Recovery when a fetch fails

| Symptom | Likely cause | Fix |
|---|---|---|
| Fetch to AustLII returns 403/410 | bare fetch rejected | open the same URL via Claude in Chrome; if Chrome is unavailable, try Jade via `site:jade.io` search (also Chrome-only) or the HCA/court site |
| Fetch to jade.io returns 403 | Jade rejects **all** bare fetches (observed) | resolve via `site:jade.io "<citation>"`, open the article via Chrome; no Chrome → Jade unreachable, use other tiers |
| CaseLaw NSW returns nothing useful | wrong decision ID, or non-NSW case | re-search `…/search?query=…`; non-NSW → AustLII via Chrome |
| Chrome not connected | extension/session inactive | tell the user; use tier-1/2 fallbacks (HCA site, official PDFs) — AustLII-blocked and Jade pages are unreachable without it — or offer `jade-research` |
| Both AustLII + CaseLaw miss the case | unreported on the main free sources | try free-tier Jade (search + Chrome, above); still missing → `jade-research` skill (paywalled, logged-in JADE in Chrome) |
| Web search returns junk/index pages | terms too broad, or bare `site:austlii` | use the web-search recipes / citator recipe; citation in quotes; add court code; party name only |

---

## Quoting & court hierarchy

**Quoting:** use the exact fetched text with paragraph numbers; do not paraphrase quotes; flag suspected OCR errors in older AustLII judgments.

**Hierarchy (for weighting):** binding on NSWSC — HCA, NSWCA. Binding on FCA single judge — FCAFC, HCA. Persuasive — other state CAs; FCAFC on federal questions. Authoritative on federal statutes — HCA, FCAFC.
