---
name: citation-extraction-en-matematicsolutions
title: Citation extraction - find every citation before you check it
description: 'Extracts the legal citations from an English-language text by pattern and rule, with no LLM in the extraction step, so the same text yields the same list every run - ECLI (CJEU and national), EU act identifiers (CELEX, Official Journal references, Regulation and Directive numbers), case names, and cited provisions (Article/section). It then normalises, deduplicates and resolves short references (ibid., id., supra, op. cit., the above-cited judgment) to their antecedent. The front end to verification: collect what is cited, then check it. Unusual or malformed citation formats can still be missed, so treat the output as a working list rather than a guarantee. Jurisdiction-neutral, EU-aware. Use when: "list every citation in this text", "what authorities are cited", "extract the provisions", "pull the case references", "what is cited here" - before verification or before sending.'
author: matematicsolutions
author_url: https://github.com/matematicsolutions/awesome-matematic-skills-en/tree/main/verification-foundation/skills/citation-extraction-en
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Citation extraction - find every citation before you check it

## Philosophy

**You can only verify what you first find.** Grounding a citation checks whether it exists in the
source - but it runs on a list that someone has to assemble first. This skill is that front-end: it
walks the text and lists every authority, so none slips past verification. A missed citation is an
unverified one.

Extraction is **mechanical** (patterns + rules, not an LLM) on purpose - a model asked to find
citations might miss one or invent one. Local, jurisdiction-neutral, EU-aware.

## Three steps (after eyecite)

1. **Extraction** - recognise and capture every reference by the patterns below.
2. **Aggregation** - resolve short references (ibid. / id. / supra / op. cit. / "the above-cited
   judgment") to their antecedents by the pointer-aware rules below, so they count as one citation,
   not several.
3. **Hand-off** - pass the structured list to verification (grounding) and, for EU sources, to
   eu-sparql-search for retrieval.

## Citation patterns

### Case law
- **ECLI (EU)**: `ECLI:EU:C:2020:559` (Court of Justice), `ECLI:EU:T:2019:...` (General Court).
- **ECLI (national)**: `ECLI:NL:HR:2021:...`, `ECLI:DE:BGH:...`, `ECLI:PL:SN:...`.
- **Case names / numbers**: `Party v Party`; CJEU case numbers `C-123/20`, `C-123/20 P` (appeal),
  joined cases `C-123/20 and C-124/20`; General Court `T-456/19`.

### EU legislation
- **CELEX**: `32016R0679`, `32019L0790` (sector + year + type + number).
- **Named acts**: `Regulation (EU) 2016/679`, `Directive 2019/790`, `Regulation (EC) No 1/2003`.
- **Official Journal**: `OJ L 119`, `OJ C 326`.

### Provisions
- `Article 5(1)(a) GDPR`, `Art. 263 TFEU`, `section 12`, `§ 3(2)`.

## Aggregation - short references (antecedents)

Short reference forms carry **different resolution rules** - they cannot all be sent to the nearest
antecedent:

- `ibid.` / `id.` / `loc. cit.` - the immediately preceding authority.
- `supra` / `op. cit.` - often carry a **pointer** that overrides proximity: an author, a title
  fragment, or a note number ("Kranenborg, op. cit., p. 12"; "supra note 14"). Resolve by the pointer
  first; fall back to proximity only when the reference is bare.
- Descriptive forms (`the cited judgment`, `the above-cited`) - match by described attributes (court,
  party, subject), not position alone.

Where more than one antecedent matches, or none does, mark the reference **unresolved - manual
review** instead of guessing: a wrong merge silently fuses two distinct authorities into one. Count
each resolved reference as the same citation as its antecedent, but keep where it occurs.

## Output format

```
CITATIONS FOUND (n):
| # | Type | Citation (normalised) | Occurrences (offset/page) | Antecedent (if short ref) |
| 1 | EU case law | C-311/18 (Schrems II) | p.3, p.7 (ibid.) | - |
| 2 | EU legislation | Regulation (EU) 2016/679 | p.2 | - |
| 3 | provision | Article 5(1)(a) GDPR | p.4 | - |

TO VERIFY: pass the "Citation" column to grounding; EU sources to eu-sparql-search.
```

## Limits

- Extraction catches references in a known format. A descriptive reference with no identifier ("the
  Court's data-protection case law") has nothing to match - mark it "no identifier, manual check".
- This is not existence verification - it says what is cited, not whether the citation is real.
- Patterns cover the common EU/ECLI formats; an unusual citation style may slip - at high stakes,
  review by hand as well.

## Attribution

The extraction -> aggregation -> annotation architecture is based on **eyecite** (Free Law Project),
**BSD-2-Clause**. US reporter regexes dropped; ECLI, CELEX/OJ and EU-citation patterns and the
antecedent rules are MateMatic's own. MateMatic interpretation, not the position of any bar or regulator.

<!-- shared-rules:begin (generated from ../../SHARED-RULES.md by scripts/shared-rules-sync.py - do not edit here) -->
## Shared rules of the verification-foundation plugin

These rules apply to every skill in this plugin, including where the skill itself is silent. They are copied into each skill, so they hold whether you install the whole plugin or a single skill.

### Five layers of protection (before any disclaimer)

1. **Source verification** - provisions and case law from databases, not the model's memory.
2. **Confidence class** - every legal claim marked: verified / check / do not use.
3. **Premise check** - facts from the user are tested before analysis.
4. **Explicit negative scope** - each skill states what it does NOT do.
5. **Human gate** - a qualified person reviews and approves the output.

If an error would pass without being stopped by layers 1-5, the fault is in the skill. Fix the tool, do not add a note. "This is not legal advice" stops no error and transfers no responsibility.

### Confidence tags

- **Verified** - source checked in this session, with a full identifier: `(GDPR Art. 6)`, `(Case C-311/18, CJEU)`.
- **Check** - plausible, unverified: `[check on EUR-Lex]`.
- **Do not use** - an invented case number or provision. Omit it, never fabricate.

The tag sits next to the line it concerns. A case number that exists is not enough - check the content.

### Human gate

Nothing is sent, filed, signed or published before a qualified person checks and approves it. A skill output is a draft, not a finished document.

### Scope

The verification foundation is jurisdiction-neutral - the method, not the substance of any one legal system. It connects to no external source (no MCP connectors) and makes no outbound calls of its own; what you type still goes to your configured model (see https://github.com/matematicsolutions/awesome-matematic-skills-en/blob/main/TRUST.md). Substance comes from separate plugins (eu-law-sources). Deep national law (e.g. Polish case law) lives in the Polish marketplace, by design.
<!-- shared-rules:end -->
