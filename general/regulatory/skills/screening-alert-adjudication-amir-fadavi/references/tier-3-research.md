# Tier 3 — Targeted external research

Tier 3 runs only when Tier 2 didn't reach a determination and the case has a realistic research path. The tier uses web search and fetching to confirm or contradict identity. Token-efficient, language-aware, source-ranked, fully snapshotted.

## Gating — when Tier 3 is even attempted

Enter Tier 3 only if at least one of the following is true:

- **G-1: A unique-enough identifier exists on at least one side that web search can plausibly anchor.** Examples: a specific role/title with date ("former Deputy Minister of Energy, 2014–2017"), a narrow geographic footprint (a single small jurisdiction with documented operations), a distinctive profession, a named organizational affiliation, a documented relationship to another identified party.

- **G-2: A specific verifiable claim in the list entry can be confirmed or contradicted via primary sources.** Examples: the list entry states a death date that can be verified against a primary source; a sanction-lift or delisting date that can be verified against the issuing agency; a role change documented by a government registry.

- **G-3: A transliteration ambiguity from Tier 0 is the only obstacle.** Source-language search is likely to resolve whether the screened name and listed name represent the same source-language name.

If **none** of G-1, G-2, G-3 holds → escalate without entering Tier 3. Don't burn tokens on cases that web research cannot conclude. The escalation record must explain that the gating failed.

## Source ranking

Evidence is admissible into Tier 3 determinations only from ranked sources:

- **Rank A** — list publisher's own entry detail page; primary government records (corporate registries, court filings, official gazettes, sanctions agency press releases, central bank publications, parliamentary records)
- **Rank B** — major news outlets with editorial standards: Reuters, AP, AFP, BBC, Financial Times, Wall Street Journal, Bloomberg, and country-equivalent tier-1 outlets (Le Monde, Süddeutsche Zeitung, NHK, Yomiuri, Asahi, Folha de São Paulo, etc.)
- **Rank C** — specialist trade press (industry publications with editorial standards), regional reputable outlets, NGO and IGO reports (FATF, UN panel reports, Transparency International country reports, OCCRP investigations)
- **Rank D** — everything else (blogs, social media, forums, content farms, sites of unknown provenance)

**Rules:**
- TP-3 and FP-7 fire only on Rank A or Rank B evidence.
- Rank C corroborates Rank A/B but never drives a determination alone.
- Rank D is never admitted into the determination record. Rank D pages may surface in search results but are filtered out before contributing.

## The four-rung language ladder

Execute rungs in order. Advance to the next rung only when the current rung's results are insufficient. "Sufficient" means at least one Rank A or B source retrieved that addresses identity directly. "Insufficient" means: all Rank C/D results, or Rank A/B results are about a different person sharing the name, or no substantive hits.

### Rung 1 — Native-script, native-language

**Trigger:** Tier 0 classified at least one of the names as non-Latin-script in origin (Arabic, Persian, Russian, Chinese, Korean, Japanese, Hebrew, Thai, Greek, etc.), or marked the language hint as non-English.

**Query construction:** Anchor name rendered in native script + most distinctive context identifier (role, employer, jurisdiction) also in the native language where natural.

Examples:
- Listed Tehran-based individual "Mohammad Reza Hashemi, former director of X Holding": Persian-script query combining محمد رضا هاشمی with the Persian rendering of the organization name.
- Listed PRC entity "Beijing X Trading Co.": Simplified Chinese query combining 北京…贸易有限公司 with relevant industry terms.
- Listed Russian individual: Cyrillic query.

### Rung 2 — Native-language, Latin-script

**Trigger:** Rung 1 insufficient, OR the source language is natively Latin-script with diacritics (Turkish, Vietnamese, Indonesian, Polish, Czech, etc.), OR the language uses both scripts in formal sources (Serbian, Azerbaijani).

**Query construction:** Anchor name in the standard Latin transliteration used by the source country's official records, plus context terms in the native language using Latin characters.

### Rung 3 — English-language coverage of the relevant region/sector

**Trigger:** Rungs 1–2 insufficient (or not applicable because the name is Latin-script English-language to begin with).

**Query construction:** Anchor name in its standard Latin form + English context terms, biased toward outlets with strong regional coverage. Examples: Reuters and AP regional desks; Financial Times for global business; Al-Monitor and Middle East Eye for MENA; South China Morning Post for Greater China; Moscow Times for Russia; Nikkei Asia for East/Southeast Asia.

### Rung 4 — Transliteration variant sweep

**Trigger:** Rungs 1–3 insufficient AND Tier 0 flagged the name as having documented transliteration variants (see `transliteration-variants.md`).

**Query construction:** Cycle through documented variant spellings of the anchor name + same context terms used in earlier rungs. Don't try every theoretical variant — only the ones the variants reference documents as common in practice.

**Note:** Rung 4 is skipped if Tier 0 didn't flag transliteration ambiguity. Western-origin English names don't need Rung 4.

## Retrieval cap

Hard cap: 8 distinct page fetches per case, **across all rungs combined**. Indicative budget allocation (adjust as the case requires):

- Rung 1: 2–3 fetches
- Rung 2: 2–3 fetches (if invoked)
- Rung 3: 2 fetches
- Rung 4: 1 fetch

If a rung resolves the case, remaining budget is unused.

If the cap is reached without resolution → escalate with the full retrieval record.

## Token-efficient search posture

- Start with the cheapest informative query: anchor name + the single most distinctive context identifier. Don't open with a long disambiguating query — let the first result tell you whether the easy path works.
- If the first query is silent or ambiguous, expand the second query by adding a second context term, not by adding boolean operators or quotes.
- Don't re-query slight variations on a failed query. Move up the ladder instead.
- If a search returns results that look promising at the title/snippet level, fetch the full page once. Don't fetch multiple variants of the same source.

## Snapshotting

Every retrieved page that contributes to the determination is captured into the evidence record:

- URL (exact)
- Retrieval timestamp (ISO 8601 UTC)
- Source rank (A/B/C/D as assessed by you)
- Extracted passage (the specific text that supports the determination)
- Contribution flag (did this retrieval contribute to the firing of TP-3 or FP-7, or to its non-firing)

This is what makes "same evidence → same decision" enforceable. A case can be re-audited against the snapshot record even if the live web has changed.

## TP-3 — Externally corroborated identity match

**Preconditions:**
- At least one Rank A or B source has been retrieved that addresses identity directly
- The retrieved source(s) confirm specific identifying facts about the listed party that also match the screened party (e.g., role at a specific organization during a specific period; nationality at the relevant time; documented life event)

**Fires when:**
- **Two independent Rank A or B sources** each confirm at least one specific identifying fact AND those facts collectively distinguish the listed party from other people sharing the name
- AND no Rank A or B source in the retrieval record contradicts identity

**Outcome:** TP, confirmed

**Audit:** List each contributing Rank A/B retrieval (URL + timestamp + extracted passage), the specific identifying fact each confirms, and the explicit reasoning that the combined facts identify the screened party as the listed party.

**Why two independent sources:** Single-source confirmation is vulnerable to source error, source reuse (one outlet copying from another), and source manipulation. Two independent Rank A/B confirmations is the conservative bar.

## FP-7 — Externally established distinct identity

**Preconditions:**
- At least one Rank A or B source has been retrieved that establishes the screened party as a documented, distinct individual or entity

**Fires when:**
- The retrieved source establishes biographic facts about the screened party that contradict the listed party on at least one anchor identifier — profession at the relevant period, nationality at the relevant time, age cohort, documented life events
- AND the contradiction is direct, not inferred from absence of evidence

**Outcome:** FP, cleared

**Audit:** The contributing retrieval(s), the specific contradiction(s), confirmation that the contradiction is positive (not "no evidence found that they're the same"), and the explicit reasoning.

**Why "positive identification":** Absence of evidence that the screened party is the listed party is not the same as evidence that they're different. FP-7 requires the latter. Examples:

- Screened "Hassan Rouhani" matched against a listed party of the same name: a Rank A retrieval establishes the screened party as a 28-year-old software developer in Manchester with no political role, while the listed party is the former President of Iran. Direct contradiction. FP-7 fires.
- A Rank A source about the listed party is retrieved but nothing about the screened party is found. This is **not** FP-7 — it's absence of evidence. Escalate.

## Multi-list and cross-list signals

If the same screened name has hits across multiple lists (e.g., SDN + PEP + adverse media), and the listed entries on different lists differ on identifiers, that's a signal the matches are on a generic name and supports FP across all hits. If the listed entries on different lists are clearly the same target (consistent identifiers), and the screened party matches the consistent profile, that supports TP.

This is contextual reasoning, not an independent rule. It enters the audit record under "cross-list correlation" and informs whether TP-3 or FP-7 has the evidence it needs.

## Exit from Tier 3

- **TP-3 fired** → output TP determination, stop, produce audit record
- **FP-7 fired** → output FP determination, stop, produce audit record
- **Retrieval cap reached or all applicable rungs exhausted without firing** → escalate with the full retrieval record

The escalation record explicitly states which rungs ran, what was retrieved at each, why each was deemed insufficient, and what specific information would have allowed determination. This is the analyst's starting point.
