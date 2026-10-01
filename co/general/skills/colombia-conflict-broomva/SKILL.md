---
name: colombia-conflict-broomva
title: colombia-conflict — CEV final-report knowledge engine
description: Knowledge engine over the Colombian Truth Commission (CEV) final report "Hay Futuro Si Hay Verdad" (2022) — the findings, statistics, armed-actor responsibilities, differential harms, coined lexicon, and the 67-recommendation roadmap for non-repetition (no repetición). Uses a kg/LLM-wiki retrieval architecture (substrate-canonical knowledge pages + a dense catalog projection for tier-1 routing + body-grep tier-2 + the agent as query engine) plus data-backed tools, including an `align` check that scores a proposed policy/action against the report's recommendation roadmap. USE WHEN reasoning about the Colombian armed conflict, peace process, transitional justice, victims, reconciliation, paramilitarism, the FARC-EP/ELN, narcotrafficking and drug policy, land/agrarian questions, the enemigo interno, falsos positivos, the Unión Patriótica genocide, social-leader killings, differential harms (ethnic peoples, women and LGBTIQ+, children, exiles, campesinado), territorial/human security,
  memory, or non-repetition; when designing, evaluating or critiquing a peacebuilding/policy intervention against the CEV evidence; when asked what the report found or recommends on a topic; or when you need a sourced conflict statistic, responsibility share, or coined concept. NOT FOR downloading/ingesting the report (that was a one-off pipeline); NOT FOR live news on the current Colombian government; NOT FOR individual criminal responsibility (that is the JEP's role — this skill carries the CEV's COLLECTIVE ethical-political responsibility). Triggers on "comisión de la verdad", "truth commission", "hay futuro si hay verdad", "Colombian conflict", "non-repetition", "no repetición", "paz grande", "transitional justice Colombia", "falsos positivos", "paramilitarismo", "JEP/CEV".
author: broomva
author_url: https://github.com/broomva/skills/tree/main/skills/knowledge/colombia-conflict
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: co
practice: general
language: en
sources:
- title: 01 02 Apex
  path: references/digests/01-02-apex.md
- title: 03 Historia
  path: references/digests/03-historia.md
- title: 04 Violaciones
  path: references/digests/04-violaciones.md
- title: 05A Territorial Crosscut
  path: references/digests/05a-territorial-crosscut.md
- title: 05B Territorial Andean
  path: references/digests/05b-territorial-andean.md
- title: 05C Territorial South
  path: references/digests/05c-territorial-south.md
- title: 06 Impactos
  path: references/digests/06-impactos.md
- title: 07 Testimonial
  path: references/digests/07-testimonial.md
- title: 08 Etnico
  path: references/digests/08-etnico.md
- title: 09 Genero
  path: references/digests/09-genero.md
- title: 10 Ninez
  path: references/digests/10-ninez.md
- title: 11 Exilio
  path: references/digests/11-exilio.md
- title: Knowledge Index
  path: references/knowledge-index.md
- title: Lexicon
  path: references/lexicon.md
- title: Synthesis
  path: references/synthesis.md
---

# colombia-conflict — CEV final-report knowledge engine

A permanent, queryable knowledge layer distilled from the Colombian Truth
Commission's final report **Hay Futuro Si Hay Verdad** (2022 — 11 tomos / 24
books / ~8,900 pp / ~3.67M words). It carries the report's substantive
**learnings and insights**, and gives agents tools to **act on the problematics
the report describes** — above all, the goal of **no repetición** (non-repetition).

## Architecture (kg / LLM-wiki)

Mirrors the workspace's `kg` LLM-as-index pattern:

- **Substrate (canonical)** — `references/`: the 12 per-volume digests +
  `synthesis.md` (master consolidation) + `lexicon.md`. These are the knowledge
  pages; the agent reasons over them.
- **Full-text grounding** — `references/fulltext/*.txt.gz`: the complete
  extracted text of all 24 volumes (~3.67M words, gzipped ~7.7 MB). `cc.py
  source` greps this for **verbatim** source passages — the digests summarize,
  the full text lets you quote the report exactly.
- **Source binaries (on demand)** — `sources/MANIFEST.json` lists the 11
  downloadable units (10 digital PDFs + the Colombia-adentro ZIP, each with
  sha256). `scripts/fetch_sources.sh` pulls + verifies the 385 MB of PDFs when
  actually needed; they are deliberately **not** committed.
- **Projection (routing)** — `references/knowledge-index.md`: a dense, one-line-
  per-item catalog auto-generated from `data/` + digest headers. Tier-1 retrieval
  scores against this.
- **Structured data** — `data/`: `statistics.json` (the conflict universe),
  `actors.json` (collective-responsibility shares), `recommendations.json` (67
  recs / 8 blocks), `concepts.json` (the coined lexicon).
- **Engine** — `scripts/cc.py`: two-tier `load` (catalog tier-1 → body-grep
  tier-2), data queries, the `align` non-repetition scorer, and the catalog
  generator. **The agent is the query engine** — `load` surfaces the relevant
  pages; the agent does the reasoning.

## When to reach for it

Load this skill whenever a task touches the Colombian armed conflict or its
aftermath — peacebuilding, transitional justice, victims and reparation,
paramilitarism, the FARC-EP/ELN, drug policy, the land/agrarian question, the
*enemigo interno*, *falsos positivos*, the UP genocide, social-leader killings,
differential harms (ethnic peoples, women/LGBTIQ+, children, exiles,
*campesinado*), territorial/human security, memory, or **non-repetition** — and
whenever you must ground a claim in a **sourced** statistic, responsibility
share, recommendation, or coined concept rather than guessing.

## Usage

```bash
# Two-tier kg retrieval over the knowledge pages
python3 scripts/cc.py load "desaparición forzada responsabilidad" -n 6

# Query the 67 recommendations
python3 scripts/cc.py rec --theme drug-policy
python3 scripts/cc.py rec --block 6            # the human-security block
python3 scripts/cc.py rec --search "social leaders protection"

# Sourced statistics / actors / lexicon
python3 scripts/cc.py stat homicides
python3 scripts/cc.py stat --all
python3 scripts/cc.py actor paramilitaries
python3 scripts/cc.py concept --search "cuerpo-territorio"

# "Does this proposal advance no repetición?" — score against the roadmap.
# align is LEXICAL overlap + a curated anti-pattern (contrary-stance) check —
# it flags proposals that CONTRADICT a block (e.g. "increase fumigation"), but it
# is not a full stance model: reason about polarity and gaps yourself.
python3 scripts/cc.py align "a program to legalize coca cultivation and support campesinos cocaleros"

# Verbatim grounding — grep the full source text for exact passages
python3 scripts/cc.py source "Bojayá iglesia" -n 3
python3 scripts/cc.py source "responsabilidad del Estado en el paramilitarismo"

# Regenerate the routing catalog (after editing data/ or references/)
python3 scripts/cc.py index            # write
python3 scripts/cc.py index --check    # CI: exit 1 if stale

# Fetch the source PDFs (385 MB) on demand, sha256-verified
scripts/fetch_sources.sh [DEST_DIR]
python3 scripts/build_manifest.py      # regenerate the manifest from a local corpus
```

### Recommended agent flow

1. **`load <topic>`** to pull the relevant knowledge-page sections into context.
2. Read the cited `references/` page(s) for the full, faithful detail.
3. Use `rec` / `stat` / `actor` / `concept` for precise sourced facts.
4. **`source <topic>`** when you need to quote the report **verbatim** (grounding
   a claim in the exact source prose, not the digest summary).
5. For a proposed intervention, run **`align`** to see which recommendation
   blocks it advances — then reason about gaps the report would flag
   (impunity, structural causes, differential harms, *terceros civiles*).

## The substance (one screen)

- **Thesis** — *Hay futuro si hay verdad.* The war (≈9M victims, ~90% civilian)
  persists because structural causes were never confronted; the demand is **No
  Matar** and *sacar las armas de la política*.
- **Causal web (*entramado*)** — land/agrarian question · restricted democracy +
  *enemigo interno* · selective State (*más territorio que Estado*) · narco +
  the war on drugs · impunity · economic model + *terceros civiles*.
- **Responsibility (collective)** — paramilitaries lead homicide/disappearance;
  FARC-EP lead kidnapping/recruitment; the State owns *falsos positivos* and
  bears responsibility *for* paramilitarism. *"A mayor poder, mayor
  responsabilidad."*
- **Differential architecture** — ethnic peoples, women/LGBTIQ+, children,
  exiles and territories get their own volumes; a single national narrative
  would reproduce the erasure that enabled the war.
- **Telos** — 67 recommendations / 8 blocks: full Accord implementation, ELN
  negotiation, integral reparation + memory, inclusive democracy, **drug-war →
  legal regulation**, breaking impunity, **human security**, agrarian/territorial
  reform, a culture of peace.

## Provenance & honesty

- Source: comisiondelaverdad.co, CC BY-NC-SA 4.0. Statistics carry their
  registry (RUV / CNMH / JEP-CEV-HRDAG) and both figures where the report prints
  two. `recommendations.json` is encoded at block granularity (faithful to the
  synthesis, not a verbatim transcription of all 67 articles).
- This is **collective** (ethical-political) responsibility as the CEV framed it
  — not individual criminal guilt (the JEP's domain).
- The **full extracted text** (all 24 volumes, gzipped) **is** bundled under
  `references/fulltext/` for verbatim grounding. The 385 MB of source **PDFs**
  are not committed — they are fetched + sha256-verified on demand via
  `scripts/fetch_sources.sh` (`sources/MANIFEST.json`).

## References

- `references/synthesis.md` — the master consolidated synthesis.
- `references/digests/*.md` — 12 per-volume sourced digests.
- `references/lexicon.md` — the coined-concepts glossary.
- `references/knowledge-index.md` — the tier-1 routing catalog (generated).
- `references/fulltext/*.txt.gz` — full extracted text of all 24 volumes (verbatim grounding).
- `sources/MANIFEST.json` + `scripts/fetch_sources.sh` — on-demand PDF retrieval.
