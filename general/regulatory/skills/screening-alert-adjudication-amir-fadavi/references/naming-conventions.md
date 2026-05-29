# Naming conventions

This reference defines anchor and non-anchor components per naming convention. Anchor components are the identity-bearing parts of a name — the parts that genuinely distinguish one person from another. Non-anchor components are context (given names, kunyas, patronymics, second surnames in some conventions).

For matching purposes:
- **Anchor overlap** is required for a name match to be considered.
- **Non-anchor overlap alone** is insufficient — it triggers FP-2 in Tier 1.

## Hispanic (Spanish-speaking world: Spain, Mexico, Colombia, Argentina, Venezuela, Peru, Chile, etc.)

**Standard form:** `[given names] [paternal surname] [maternal surname]`

Example: "María Isabel García López"
- Given names: "María Isabel"
- Paternal surname: "García" — **anchor**
- Maternal surname: "López" — non-anchor (corroborating)

**Anchors:** paternal surname (always), maternal surname (when present, secondary anchor — useful for disambiguation but not strictly required)

**Non-anchors:** given names

**Notes:**
- A person is usually known by paternal surname alone in formal contexts ("Sr. García"). In casual contexts, given name + paternal surname.
- The "de" particle joins surnames: "de la Cruz", "del Río". Treat as part of the surname.
- Married women in some Hispanic countries append "de [husband's paternal surname]" — e.g., "García de Méndez". The "Méndez" component is the spouse's surname, not the woman's own anchor.
- Variations in spelling and accents: "García" / "Garcia"; "López" / "Lopez". Treat as equivalent.

## Portuguese / Brazilian

**Standard form:** `[given names] [maternal surname] [paternal surname]` (note: order is REVERSED from Spanish)

Example: "João Carlos Silva Santos"
- Given names: "João Carlos"
- Maternal surname: "Silva" — secondary anchor
- Paternal surname: "Santos" — **primary anchor**

**Anchors:** paternal surname (the final surname — opposite of Spanish position)

**Non-anchors:** given names; maternal surname is corroborating

**Notes:**
- Multiple surnames are common in Brazilian names (4+ total tokens). The last one is the paternal.
- Particles "da", "das", "de", "do", "dos" connect surnames. Treat as part of the following surname.

## Arabic

**Standard form (varies by region — Gulf, Levant, Maghreb differ):** `[kunya] [ism] [nasab] [nisba]`

Example: "Abu Bakr Mohammad bin Abdullah al-Tikriti"
- Kunya: "Abu Bakr" — "father of Bakr", honorific, non-anchor
- Ism: "Mohammad" — given name, **anchor**
- Nasab: "bin Abdullah" — "son of Abdullah", father's name, **anchor** (when present, strong identifier)
- Nisba: "al-Tikriti" — origin/tribe/profession, non-anchor (geographic or tribal identifier)

**Anchors:** ism (personal name) and father's name from the nasab (when present)

**Non-anchors:** kunya (honorific) and nisba (origin descriptor)

**Notes:**
- "Bin" / "Ibn" / "Bint" (son of / daughter of) is a relationship marker; the name that follows is the parent's name.
- "Al-" / "El-" is a definite article often attached to nisba ("al-Baghdadi" = "the Baghdadi"). The article doesn't carry identity weight by itself.
- The same source-language Arabic name has many Latin transliterations — see `transliteration-variants.md`.
- Family names in the Western sense are less consistent in Arabic culture. Identification often relies on the chain of ism + father's nasab + grandfather's nasab.

## Persian / Iranian

**Standard form:** `[given names] [family name]`

Example: "Mohammad Reza Hashemi-Rafsanjani"
- Given names: "Mohammad Reza" — non-anchor
- Family name: "Hashemi-Rafsanjani" — **anchor**

**Anchors:** family name (usually the last token, often distinctive)

**Non-anchors:** given names

**Notes:**
- Many Persian family names end in: -zadeh ("son of"), -pour, -nia, -i (relational), -kia. These suffixes don't reduce identity weight.
- The Persian alphabet is closely related to Arabic but with additional letters. Persian transliterations sometimes follow Arabic conventions and sometimes diverge — see `transliteration-variants.md`.

## Russian and Slavic (Russia, Belarus, Ukraine, Bulgaria, Serbia)

**Standard form:** `[given name] [patronymic] [family name]`

Example: "Vladimir Vladimirovich Petrov"
- Given name: "Vladimir" — non-anchor
- Patronymic: "Vladimirovich" — non-anchor (this is "son of Vladimir", a relational form, not a middle name)
- Family name: "Petrov" — **anchor**

**Anchors:** family name

**Non-anchors:** given name, patronymic

**Patronymic forms:** male suffixes -ovich, -evich, -ich; female suffixes -ovna, -evna, -ichna. Always derived from father's given name.

**Family name endings:** -ov/-ova, -ev/-eva, -in/-ina, -sky/-skaya, -tsky/-tskaya. The male and female forms of the same family name refer to the same family.

**Notes:**
- Ukrainian family names often end in -enko, -uk, -chuk.
- Cyrillic-to-Latin transliteration varies. "Александр" can become Aleksandr, Alexander, Aleksander. Treat documented variants as equivalent — see `transliteration-variants.md`.

## East Asian — Chinese, Korean, Vietnamese (family name first)

**Standard form:** `[family name] [given names]`

Example (Chinese): "Wang Wei"
- Family name: "Wang" — **anchor** (one syllable, comes first)
- Given name: "Wei" — non-anchor

Example (Korean): "Kim Min-Jun"
- Family name: "Kim" — **anchor**
- Given name: "Min-Jun" — non-anchor

Example (Vietnamese): "Nguyễn Văn Anh"
- Family name: "Nguyễn" — **anchor**
- Middle name: "Văn" — non-anchor (sometimes traditional gender marker)
- Given name: "Anh" — non-anchor

**Anchors:** family name (first position)

**Non-anchors:** given names

**Critical care needed:** In Western screening systems and Latin-script transliterations, East Asian names are sometimes reordered to Western convention (family name last). This produces structural ambiguity. When in doubt: check whether the surname is a known East Asian family name; if so, the East Asian family name is the anchor regardless of position in the string.

**Common Chinese family names (top ~20 cover most of the population):** Wang, Li, Zhang, Liu, Chen, Yang, Zhao, Huang, Zhou, Wu, Xu, Sun, Hu, Zhu, Gao, Lin, He, Guo, Ma, Luo.

**Common Korean family names:** Kim, Lee/Yi, Park/Pak, Choi/Choe, Jung/Jeong, Kang, Cho/Jo, Yoon/Yun, Jang.

**Common Vietnamese family names:** Nguyễn, Trần, Lê, Phạm, Hoàng/Huỳnh, Phan, Vũ/Võ.

## Japanese

**Standard form:** `[family name] [given name]` in Japanese; often reversed to `[given] [family]` in Latin transliteration

Example: "Tanaka Hiroshi" (Japanese order) = "Hiroshi Tanaka" (Western order). Same person.

**Anchors:** family name

**Notes:**
- In screening systems with Latin-script entries, Western order is more common. Don't assume position alone — check whether the surname is a known Japanese family name.
- Common Japanese family names: Sato, Suzuki, Takahashi, Tanaka, Watanabe, Ito, Yamamoto, Nakamura, Kobayashi, Kato, Yoshida, Yamada, Sasaki.

## Indonesian / Malay / Burmese

**Standard form:** Varies. Many Indonesians and Burmese have a single name (no surname). Malays follow Arabic conventions with "bin"/"binti".

Examples:
- Single name: "Sukarno", "Suharto" — entire name is **anchor**
- With bin/binti: "Ahmad bin Hassan" — "Ahmad" is given, "Hassan" is father's name; both potentially anchor in low-data screening
- Burmese: "Aung San Suu Kyi" — multiple syllables, no clear surname; treat full name as **anchor** with all tokens required

**Anchors:** the full name (since there's no consistent decomposition into family vs. given)

**Notes:** Parse confidence is often `low` for these — limited matching options, treat with caution. The structural-mismatch FP rules (FP-2, FP-6) generally don't fire for these names because the structure doesn't support clean component decomposition.

## Western default (English-speaking, German, French, Italian, Scandinavian, etc.)

**Standard form:** `[given names] [family name]`

Example: "John Robert Smith"
- Given names: "John Robert" — non-anchor
- Family name: "Smith" — **anchor**

**Anchors:** family name (last position)

**Non-anchors:** given names

**Notes:**
- Compound surnames (hyphenated or two-word): "Smith-Jones", "van der Berg", "Le Pen". Treat the full compound as the anchor.
- Particles: "von", "van", "de", "le", "la", "del". Part of the surname.
- Generational suffixes: Jr., Sr., II, III. Non-anchor, useful for disambiguation between father/son sharing a name.

## Ambiguous or low-confidence parses

When name structure markers are absent or conflicting:
- Single token of unclear origin (e.g., "Mohammed" alone could be many things)
- Two tokens with no clear convention markers ("Ali Hassan" — Arabic? Persian? Turkish? South Asian?)
- A name that fits multiple conventions equally well

→ Set `naming_convention: ambiguous` and `parse_confidence: low`. The structural-mismatch FP rules (FP-2, FP-6) do not fire on low-confidence parses. Other rules still apply.

## How to use this reference

When parsing a name in Tier 0:

1. Identify likely source language via markers from `tier-0-parsing.md`.
2. Look up the relevant convention here.
3. Apply the anchor / non-anchor decomposition.
4. Set parse confidence based on how cleanly the name fits the convention.

When evaluating FP-2 or FP-6 in later tiers, the anchor/non-anchor split from Tier 0 is what these rules operate on. The rules don't re-parse the name — they use the parse record.
