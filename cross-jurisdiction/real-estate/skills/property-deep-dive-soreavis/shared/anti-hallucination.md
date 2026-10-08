# Anti-Hallucination Guard — Mandatory Layer

This document is **non-negotiable**. Every output produced by `property-deep-dive` must pass these guards before being shown to the user. Property due-diligence drives six- to seven-figure decisions; a fabricated tax rate or risk classification can mislead a buyer into real losses.

The goal is not "no hallucinations." That's the lie. The goal is: **every claim is either sourced, computed transparently, or labelled as uncertain with the verification path the user can take.** When the model can't satisfy that bar, it must say so explicitly.

## The five hallucination patterns to suppress

These are the documented failure modes of LLM-driven research. The skill must actively defeat each one.

### 1. **Slot-filling fabrication**

The pressure to fill every cell of a table or every bullet of a list. When asked "what is the taxe foncière rate?" with no data, the model invents a plausible number.

**Defeat**: Empty cells stay empty with `—` and the source returns no data. Output the cell as `data not publicly available — verify at <authoritative source>` rather than fabricating.

### 2. **Confident extrapolation**

Treating an estimate as a measurement. "VLC ≈ €3,500/year" presented as fact when it's a national-average extrapolation onto an unverified parcel.

**Defeat**: Every estimated number is **prefixed** with `~` or `est.` or `≈` and tagged with a confidence label. Every sentence containing a computed number names the inputs.

### 3. **Stale-data assertion**

Quoting 2022 rates as "current" when the year is 2026, with no temporal flag.

**Defeat**: Every numeric source carries an "as of" date. If the data is >12 months old, the output must say `(<year> data; rates may have changed)`.

### 4. **Source identity conflation**

Treating a listing's claim as equivalent to a government register; treating commune-level data as parcel-level; conflating "Wibarren" with "Iribarren" because both look right.

**Defeat**: Source rank table — primary > secondary > listing > inference. Never silently upgrade. When a name is taken from OSM/cadastre, don't normalize it — quote it verbatim.

### 5. **Synthesis without anchors**

Generating a plausible-sounding paragraph that has no underlying citations. Common in TL;DR / summary blocks.

**Defeat**: TL;DR bullets must each be **traceable** to a sourced claim earlier in the document. The pre-output validator flags any TL;DR bullet whose claim isn't anchored upstream.

## Source ranking — never silently upgrade

| Tier | Examples | Trust level |
|---|---|---|
| **Primary government** | Géorisques DICRIM PDF, INSEE, gov.uk Land Registry, Catastro, BORIS, Sispea | ✅ Citable as fact |
| **Primary regulated entity** | Conseil Départemental traffic counts, EDF PPI plaquette, IRSN/ASNR radon map, BRGM | ✅ Citable as fact |
| **Secondary aggregator** | impots-locaux.org, meilleursagents.com, immo-portal averages, Selectra | ⚠️ Quote but cross-check |
| **Listing platform** | SAFTI, SeLoger, Rightmove, Idealista, ImmoScout24 | ⚠️ Seller-controlled, often outdated/incomplete |
| **Forum / Reddit / blog** | r/violinist, FrenchEntrée, Mumsnet | 🟡 Anecdotal, never as basis for verdict |
| **Model inference** | Claude's own extrapolation | 🔴 Must be labelled `est.` and shown with inputs |

When two sources at the same tier disagree, output BOTH and explain the gap.

When a higher-tier source contradicts a lower-tier one, the higher tier wins and the lower one gets `(superseded — see <higher source>)`.

## Confidence labels — required on every verdict

Every section ends with a confidence band:

- **HIGH**: 2+ primary sources agree, data <12 months old, claim is parcel-specific (not commune-level extrapolated)
- **MEDIUM**: 1 primary source OR 2 secondary, or data 12–36 months old, or claim is locality-aggregated
- **LOW**: only secondary/computed, or data >36 months old, or sources contradictory, or claim depends on unverified listing data

Output template extension for every section:

```markdown
**Confidence**: HIGH | MEDIUM | LOW — <one-sentence justification>
```

## The eight mandatory pre-output checks

Before printing the final report, the skill **must** scan its draft against these checks. Each `❌` requires a fix-pass.

### Check 1: Numeric citations

Scan every number in the body. Each must satisfy ONE of:
- ✅ Inline citation: `€145,000 (SAFTI listing 1627075)`
- ✅ Linked to Sources block: `€912/m² [Netvendeur](url)`
- ✅ Computed transparently: `€620/m² (€145,000 ÷ 234 m²)`
- ✅ Estimated with hedge: `~€3,500/yr est.`

If a number has none of these → **either find a source, mark it `est.` with reasoning, or remove it.**

### Check 2: "Is" statements about parcel-specific facts

Scan for parcel-specific claims using `is`, `has`, `connects to`. Examples:
- "The property is connected to mains drains."
- "The lot is in the flood zone."
- "The house has asbestos."

Each such statement requires a parcel-level source (ERRIAL, cadastre overlay, sale diagnostic). If only commune-level data supports it → soften to `the commune is in zone X — parcel-level confirmation required via <verification path>`.

### Check 3: Date stamps

Every external data point gets an "as of" date. Sweep for:
- Tax rates → `(<year> rates from <source>)`
- Price/m² → `(<month year> Netvendeur)`
- Traffic counts → `(<year> Conseil Départemental)`
- Population → `(<year> INSEE)`

If data is >12 months old, append `— rates/figures may have changed since`.

### Check 4: Listing-trust flagging

Any field that comes from a listing platform (SAFTI/SeLoger/Rightmove etc.) must be tagged:
- `(per listing — verify with cadastre / on visit)`

Critical fields to flag from listing alone: surface m², year built, condition, energy rating, sewer type, land area. Listings are seller-controlled marketing.

### Check 5: TL;DR anchor check

For each TL;DR bullet, find its supporting claim in the body. If a TL;DR makes a claim not made in the body → either remove it from TL;DR or add the supporting claim+source to the body.

### Check 6: Empty-source handling

For every cell in a table, every bullet that should have data: if the source returned nothing, the output is `data not publicly available — <verification path>` NOT a plausible-looking guess.

If a whole section couldn't be filled (e.g., country playbook is scaffold-only and lookups return 404) → output the section header with:

```markdown
## <Section name>

⚠️ **Data not retrieved.** This section's primary sources for <country> were unreachable or returned no parcel-level data during this run. Verification path:
1. <step 1>
2. <step 2>
```

### Check 7: Foreign-language preservation

Every native-language statute, regulator, document form, registry, programme, court, or tax name in the draft MUST appear in its original form alongside the English gloss — the native term primary, the translation as the gloss:

```
Code civil Art. 682 (French Civil Code Article 682)
Modelo 720 (Spanish foreign-asset declaration form)
```

Scan the draft for any English-only paraphrase of a native legal term (e.g. "the French Civil Code Article 682" with no `Code civil Art. 682` next to it) and add it to the fix-pass list before output: the reader must be able to search, cite, or query the original term at the regulator or with a local lawyer. Policy, format patterns, and the full applies/exempt list are in `shared/foreign-language-preservation.md`.

### Check 8: Contradiction surfacing

If during the run two sources gave conflicting numbers (e.g., commune avg €/m² of €896 from netvendeur vs €912 from impots-locaux), the output explicitly says:

```markdown
Sources disagree:
- Netvendeur (Feb 2026): €912/m²
- Meilleurs Agents (Apr 2025): €896/m²
- Difference likely due to <method/timing/sample>
- Using <chosen value> for our calculation; sensitivity: ±X% impact
```

Never silently pick one and present it as canonical.

## Forbidden phrasings

These phrases generate hallucination pressure. Replace per the table:

| ❌ Forbidden | ✅ Replace with |
|---|---|
| "approximately €X" | `~€X (computed from <inputs>)` or `~€X (est., <reason>)` |
| "in the area of" | exact range with sources |
| "typical for the region" | named local benchmark with source |
| "as of recent data" | `(<year> data, source <X>)` |
| "industry average" | named survey + year + sample size |
| "experts say" | named source or removed |
| "studies show" | named study + year + URL |
| "should be around" | `est. <range>; verify with <auth>` |
| "is likely connected to" | `probability connected: <X>% based on <Y>` (only after running the skill's actual probability heuristic) |

## Hedging language calibration

Every uncertain claim requires calibrated hedging. Use these tiers:

| Phrase | Confidence implication |
|---|---|
| "is", "has", "does" | Asserted as fact — must be sourced |
| "appears to", "indicates that" | Source is suggestive but not direct |
| "probably", "likely" | Inference based on multiple weak signals |
| "may", "could" | Single weak signal or reasoning only |
| "we cannot determine from publicly accessible sources" | Tried, failed — use this freely |

Choose the weakest accurate tier. If you only have one weak signal, don't say "is" or "has."

## Computed-number transparency rule

Every derived number must show the computation inputs in-line OR in a footnote:

```markdown
Estimated annual taxe foncière: ~€833 (= 37.04% × 50% × est. VLC €4,500)
                                       ↑ rate     ↑ statutory ↑ inferred from rural cat. 5–6 typical
```

If the user can't reverse the math, the number isn't transparent.

## Source-disagreement protocol

When two sources at the **same tier** disagree:
1. Both are quoted with their date
2. The gap is explained (different methodology, different time, different sample)
3. The chosen number for downstream calculations is named, with the reason
4. The sensitivity is given (e.g., "±3% impact on tax estimate")

When sources at **different tiers** disagree:
1. Higher-tier wins
2. Lower-tier is quoted with `(superseded by <higher>)`
3. If the user previously cited the lower-tier source, surface this transparently

## Address-vs-commune trap

Many French/EU registers are **commune-level**, not parcel-level. Examples:

| Source | Granularity | What you can ASSERT vs INFER |
|---|---|---|
| DICRIM | Commune | "The commune is at risk of X" — NOT "this property is at risk of X" |
| IAL | Commune | "Argiles in the IAL village-center band is X" — NOT "this lot has argiles X" |
| RGA map (commune) | Commune surface | "The commune has zones of X" — NOT "this lot has X" |
| ERRIAL | Parcel | Can assert parcel-level — but must be requested per parcel |
| Cadastre overlay | Parcel | Can assert parcel-level for visible features |
| OSM | Mixed | Tags on individual ways/parcels = parcel; commune relations = commune |
| TMJA traffic | Road segment | Can quote for that segment — extrapolating to the property's specific road needs map confirmation |

**Rule**: If the source is commune-level, the verb in the output must be commune-level. Never silently elevate to parcel-level.

## The one-pass self-validation prompt

Before printing the final report, the skill performs this self-check (mentally, no need to print):

```
For each section in the draft:
  For each numeric claim:
    - Does it have a source link OR a computation OR an "est." tag?
    - If from a listing, is it tagged "per listing"?
    - If based on commune data, is the verb commune-level?
  For each assertion of fact:
    - Is the source primary government, primary regulated, secondary, listing, or model inference?
    - Is the assertion language calibrated to that source tier?
  For the TL;DR:
    - Each bullet must trace to a body claim
  For empty data:
    - Did I write "data not publicly available" or did I fabricate?
```

If any check fails → fix that line BEFORE outputting.

## Final required footer

Every report ends with this disclaimer (the user must always see it):

```markdown
---

## ⚠️ Verification responsibilities

This report aggregates publicly accessible data and clearly-labelled estimates. **Before signing**, the buyer must independently verify:

1. **Tax figures** — request the seller's most recent annual tax bill (avis de taxe foncière in FR, Grundsteuerbescheid in DE, Council Tax bill in UK, etc.).
2. **Risk disclosures** — pull the official parcel-level risk document (ERRIAL in FR, Risikoauskunft in DE, Energy & Environmental Search in UK, etc.).
3. **Sewer connection** — telephone the local authority responsible (mairie / Bürgeramt / council water company) for parcel-level confirmation.
4. **Building condition** — commission an independent surveyor for any pre-1990 build.
5. **Listing claims** — anything from the seller's listing (surface, year, energy rating, condition) must be re-verified with cadastre and a physical visit.

**This report is decision-support, not legal/tax advice.** AI-assisted aggregations contain risk of error. Critical figures must be confirmed with primary sources or qualified professionals.

---

*Generated by `/property-deep-dive` on <date>. Confidence levels per section above.*
```

This footer is non-removable — it's part of every save and every terminal output.

## Failure-mode logging

When the skill encounters a failure that affects output quality, log it openly in a `## ⚠️ Run quality notes` block at the bottom of the report (before the verification footer):

```markdown
## ⚠️ Run quality notes

During this run:
- DICRIM PDF for <commune> was a scanned image; risk extraction relied on visual page reads (medium confidence on numerical specifics).
- Conseil Départemental traffic PDF was unreachable (404); traffic estimates are inferred from OSM road class only (LOW confidence).
- Listing surface (234 m²) was not cross-checked against cadastre.
- The seller's diagnostic file (DDT) was not provided; some 1975-build hazards (asbestos, lead, electrical) are inferred from build year, not measured.
```

This block is **mandatory whenever any source failed or any tool errored** during the run. It tells the user where to be sceptical.

## Test scenarios for self-evaluation

When developing or extending the skill, run these test cases and ensure no fabrication:

1. **Address with no DICRIM PDF**: should say "DICRIM not available for this commune" — not invent risks
2. **Address from a country with scaffold-only playbook**: should produce best-effort + scaffolding warning
3. **Listing with missing surface**: should NOT compute €/m² with a guessed surface — should flag the gap
4. **Brand-new build (post-2020)**: should NOT apply 1970s-era hazards
5. **Property in Paris vs Adriers**: tax rates and risks should differ — the skill must not template-paste
6. **Missing INSEE code**: should ask the user OR resolve before continuing — not fabricate
7. **Source returns 403/login wall**: should say so, not guess content

If any test produces a fabricated claim, escalate to debug.

## Operator philosophy

> "I'd rather output `data not available — call the mairie at +33...` than risk a confident-sounding lie. The user came here to make a major life decision. They need to know what we know AND what we don't."

This is the contract. The skill's value comes from honesty about data limits, not from the illusion of completeness.
