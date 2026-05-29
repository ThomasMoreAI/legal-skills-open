# Tier 0 — Parse and normalize

Tier 0 is the foundation. Every later tier depends on it. Tier 0 reaches no determinations; it produces the parse record that the rule tiers operate on.

## Inputs

From the alert: screened name, matched name, list name, list version (optional), upstream match score (optional), any secondary identifiers, listed-entry detail (full text of the list entry including aliases, identifiers, biographic fields).

## Outputs

A parse record with the following structure:

```
screened_name_parse:
  script: Latin | Cyrillic | Arabic | Han | Hangul | Hebrew | Thai | Greek | Devanagari | mixed | other
  language_hint: detected source language (e.g., en, es, ar, fa, ru, zh, ko)
  naming_convention: Hispanic | Portuguese | Arabic | Russian | East_Asian | Indonesian_Burmese | Western_default | ambiguous
  components:
    anchor: [list of anchor strings]
    non_anchor: [list of non-anchor strings]
  parse_confidence: high | low

matched_name_parse:
  [same shape]

listed_party_type: individual | entity | vessel | aircraft | unknown
screened_party_type: provided | user_confirmed | inferred | unknown
listed_aliases_parsed: [list of {alias, parse} entries from the list entry]
identifiers_on_listed_entry: dict of identifier type to list of values (passport, national_id, tax_id, registration_number, dob, pob, nationality, address)
identifiers_on_screened_party: same shape
```

## Step 1: Script detection

Detect the script of each name. Most are Latin-script in screening systems even when the underlying name is Arabic, Persian, Russian, Chinese — because the screening systems transliterate. Look at the raw characters.

If both names are Latin-script but the language hints (see Step 2) suggest one or both are transliterations from non-Latin sources, mark `language_hint` accordingly and treat transliteration variants as a Tier 3 consideration.

If one name is in native script and the other is Latin-script (e.g., the list entry includes Arabic-script aliases and the screened name is a Latin transliteration), record both and use the language-aware matching path.

## Step 2: Language hint

For Latin-script names, use linguistic markers to infer the likely source language:

- **Hispanic markers**: two surnames, surnames starting with "de la", "del", "García", "Martínez", "López", "González", common given names like "José", "María"
- **Portuguese/Brazilian markers**: surnames "da Silva", "Santos", "Oliveira", "Pereira"; given names like "João", "Ricardo"; Portuguese spelling patterns ("ão", "ç")
- **Arabic markers**: particles "Al-", "El-", "Bin", "Ibn", "Abu", "Umm"; names like "Mohammed/Muhammad/Mohamed/Mohamad", "Ahmed/Ahmad", "Hassan", "Khalid/Khaled", "Yousef/Yusuf"
- **Persian/Iranian markers**: "Reza", "Hossein", "Mahdi", "Mehdi", surnames ending in "-zadeh", "-pour", "-nia", "-i"
- **Russian/Slavic markers**: patronymics ending in "-ovich", "-evich", "-ovna", "-evna"; surnames ending in "-ov", "-ev", "-sky", "-skaya"
- **East Asian markers** (Chinese): single-syllable surnames "Wang", "Li", "Zhang", "Chen", "Liu", "Yang", "Huang", "Wu", "Zhao"
- **Korean markers**: surnames "Kim", "Lee", "Park", "Choi", "Jung", "Kang"
- **Vietnamese markers**: surnames "Nguyen", "Tran", "Le", "Pham", "Hoang"
- **Indonesian/Malay markers**: single names common; particles "bin"/"binti"; names like "Muhammad", "Siti"

These markers are heuristic. When a name has multiple plausible origins (e.g., "Ali" — Arabic, Persian, Turkish, South Asian), record the ambiguity rather than picking one.

## Step 3: Naming-convention classification

Map the language hint to a naming convention using `naming-conventions.md`. If markers conflict or are absent, mark convention as `ambiguous` and set `parse_confidence` to `low`.

## Step 4: Structural parse

For each name, separate components into anchor (identity-bearing) and non-anchor (context) per the convention. The conventions reference defines the rules per convention. Examples:

- **Hispanic, "Maria Gonzalez Lopez"** → anchor: ["Gonzalez"] (paternal surname), non_anchor: ["Maria", "Lopez"] (given name, maternal surname). Maternal surname matters but is secondary.
- **Hispanic, "Jose Andrea Coronado"** → anchor: ["Coronado"], non_anchor: ["Jose", "Andrea"]
- **Arabic, "Abu Bakr Mohammad bin Abdullah al-Tikriti"** → anchor: ["Mohammad", "Abdullah"] (ism + father's nasab), non_anchor: ["Abu Bakr" (kunya), "al-Tikriti" (nisba)]
- **Russian, "Vladimir Vladimirovich Petrov"** → anchor: ["Petrov"], non_anchor: ["Vladimir" (given), "Vladimirovich" (patronymic)]. Note: middle component is patronymic, not a middle name in the Western sense.
- **East Asian, "Wang Wei"** → anchor: ["Wang"] (family name, comes first), non_anchor: ["Wei"] (given name)
- **Western default, "John Robert Smith"** → anchor: ["Smith"], non_anchor: ["John", "Robert"]

When a name has only one token (e.g., Indonesian single-name conventions), the single token is the anchor. Parse confidence is `low` because verification options are limited.

## Step 5: Parse confidence

Set `parse_confidence` to:

- **`high`** when language markers are clear, the convention is unambiguous, and component roles are confidently assigned
- **`low`** when any of: convention is ambiguous; the name structure doesn't match the inferred convention; a single token of unclear origin; transliteration produced a structure that doesn't fit any standard pattern

`low` parse confidence disables the structural-mismatch FP rules (FP-2, FP-6) in later tiers for that name pair. The reasoning: we won't auto-clear on a parse we don't trust.

## Step 6: Alias inventory

Extract every alias from the listed entry (a.k.a., f.k.a., n.k.a., low-quality aliases, strong aliases). Parse each through Steps 1–4 the same way as the main name.

This matters because:
1. The actual match might be against an alias, not the primary listed name. Identify which.
2. Some aliases drop or reorder name components in ways that look like FP candidates at the surface but actually represent how the listed party is known. If a listed party has a documented alias "Jose Andrea" (without surname), then "Jose Andrea" matched against this party is *not* an FP-2 case — the alias is real.

## Step 7: Identifier inventory

Catalog every identifier on each side:

- **Date of birth**: full (day/month/year), partial (year only, year-month, year range), or absent. Note multiple DOBs (listed entries often have many).
- **Place of birth**: city + country, country only, or absent. Multiple POBs possible (parties have lived in multiple places). When recording POB, also record any documented alternate name for the city or country per `place-name-equivalences.md` — e.g., a listed POB "Leningrad, USSR" is recorded with alternate "St. Petersburg" and successor-state "Russia". This makes Tier 2's POB comparison resilient to historical renamings.
- **Nationality / citizenship**: list all, note primary if indicated. Watch for dual nationals.
- **National ID numbers**: passport, national ID card, tax ID, driver's license. Capture issuer and number.
- **For entities**: registration number, country of incorporation, registered address, tax ID, LEI.
- **For vessels**: IMO number, MMSI, flag state, prior names, prior flags.

The identifier inventory feeds Tier 2 directly. A missing identifier on either side means the corresponding Tier 2 rules can't fire — that's the conservative default.

## Step 8: Type determination

`listed_party_type` comes from the list entry's type field directly. Most major lists tag this explicitly (SDN_TYPE = "Individual", "Entity", "Vessel", "Aircraft").

`screened_party_type` source priority:

1. **Provided** — given in the alert input. Use as-is. Confidence: high.
2. **User_confirmed** — in interactive mode, ask the user once if not provided. Use the answer. Confidence: high.
3. **Inferred** — in batch mode when not provided. Use structural cues (entity suffixes "LLC", "Ltd", "S.A.", "GmbH", "OAO"; vessel cues "M/V", "M/T", "S.S."). If no cues, default to "individual" but flag as `inferred`. Confidence: low.
4. **Unknown** — when inference produces no signal at all.

Type-mismatch rules in later tiers respect this confidence. FP-1 (type mismatch) requires high-confidence types on both sides — it never fires on `inferred` types.

## Output

Produce the parse record as defined at the top of this file. This record is referenced by every subsequent tier and included in the final audit output.
