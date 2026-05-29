# Readability Metrics — Reference

Loaded when the audit reaches Step 4. Computes one or more readability scores depending on the document's language and shows the underlying counts so the user can verify.

## Counting primitives

All formulas in this file rely on five counts. Compute them once and reuse.

- **W** — total words. A word is a maximal sequence of alphabetic characters (Unicode letters), counting hyphenated forms as a single word.
- **S** — total sentences. A sentence ends at `.`, `!`, `?`, or `;` when followed by whitespace and a capital letter. Treat numbered list items as separate sentences if each item is grammatically complete.
- **Sy** — total syllables (English and French) or **CH** — total characters (German Amstad uses a syllable variant; LIX uses long-word counts).
- **LW** — "long words" = words of more than 6 characters (LIX convention).
- **C** — clauses (used for the Wiener Sachtextformel).

For all languages: exclude headings, page numbers, signature blocks, and table-of-contents entries from W and S. Keep the same exclusions consistent across pillars so the counts agree.

## English

### Flesch Reading Ease

```
FRE = 206.835 − 1.015 × (W/S) − 84.6 × (Sy/W)
```

Where Sy is total syllables. Score range: in practice 0–100, can go negative for very hard text or above 100 for very simple text.

Interpretation bands (Flesch's original):

| Score | Band | Typical reader |
| --- | --- | --- |
| 90–100 | Very Easy | 5th-grade child |
| 80–89 | Easy | 6th-grade |
| 70–79 | Fairly Easy | 7th-grade |
| 60–69 | Standard | 8th–9th-grade |
| 50–59 | Fairly Difficult | high school |
| 30–49 | Difficult | college |
| 0–29 | Very Difficult | university graduate / specialist |

Typical scores for reference:

- Plain-language consumer T&C, well-drafted: 55–65.
- Average newspaper article: 60–70.
- Average US legal contract: 25–45.
- US Supreme Court opinion: 30–40.

### Flesch–Kincaid Grade Level

```
FKGL = 0.39 × (W/S) + 11.8 × (Sy/W) − 15.59
```

Expressed as a US school grade level. FKGL 16 ≈ college senior; FKGL 12 ≈ end of high school.

### LIX (works across languages, useful for English too)

```
LIX = (W/S) + 100 × (LW/W)
```

Where LW = words over 6 characters. Bands:

| LIX | Band |
| --- | --- |
| < 30 | Very easy |
| 30–39 | Easy |
| 40–49 | Standard |
| 50–59 | Difficult |
| 60+ | Very difficult |

## French

### Kandel–Moles adaptation of Flesch (1958)

```
FRE_FR = 207 − 1.015 × (W/S) − 73.6 × (Sy/W)
```

Tuned to French syllable structure (French words average more syllables per word than English). Use the same interpretation bands as English Flesch, with caution: French texts naturally score 5–10 points lower than equivalent-difficulty English texts because of higher syllable density.

Typical scores for reference:

- French consumer CGU, well-drafted: 50–60.
- Average French press article (*Le Monde*): 50–60.
- Average French commercial contract: 20–40.

### LIX

Same formula as English, with French "long word" threshold also > 6 characters. French has longer average word length than English, so LIX runs slightly higher.

Bands as for English.

### Indice Gunning adapted for French (optional)

```
IG_FR = 0.4 × ((W/S) + 100 × (HW/W))
```

Where HW = words with 3 or more syllables (excluding compound words and inflected forms). Useful for cross-checking — should agree directionally with Kandel–Moles.

## German

### Amstad adaptation of Flesch (1978)

```
FRE_DE = 180 − (W/S) − 58.5 × (Sy/W)
```

Note the different constants from English. Score range 0–100.

Interpretation bands (Amstad):

| Score | Band | Typical reader |
| --- | --- | --- |
| 90–100 | Sehr leicht | Grundschule |
| 80–89 | Einfach | 6. Klasse |
| 70–79 | Eher einfach | 7. Klasse |
| 60–69 | Mittel | 8.–9. Klasse |
| 50–59 | Eher schwer | Realschule / Sekundarstufe |
| 30–49 | Schwer | Abitur |
| 0–29 | Sehr schwer | Hochschulbildung |

Typical scores:

- *Bild-Zeitung*: 65–75.
- *FAZ* / *Süddeutsche*: 45–55.
- Average German AGB: 15–35.
- BGB itself: 15–25.

### Wiener Sachtextformel (Bamberger & Vanecek, 1984)

Designed for non-fiction German prose. Several variants; WSTF 1 is the standard:

```
WSTF = 0.1935 × MS + 0.1672 × SL + 0.1297 × IW − 0.0327 × ES − 0.875
```

Where:
- **MS** = percentage of words with three or more syllables.
- **SL** = mean sentence length in words.
- **IW** = percentage of words with more than six letters.
- **ES** = percentage of monosyllabic words.

Output is a school-grade level from 4 (easy) to 15 (very difficult). Useful as a complement to Amstad because it captures sentence length and word length independently.

### LIX

Same formula. German has longer average word length than English, so LIX runs higher; bands shift up:

| LIX (German) | Band |
| --- | --- |
| < 35 | Sehr leicht |
| 35–44 | Leicht |
| 45–54 | Standard |
| 55–64 | Schwer |
| 65+ | Sehr schwer |

## Translating raw scores into the pillar score

For each computed metric, map the band to a 0–100 component:

| Band | Component |
| --- | --- |
| Very Easy / Sehr leicht | 95 |
| Easy / Einfach / Leicht | 85 |
| Fairly Easy / Eher einfach | 75 |
| Standard / Mittel | 65 |
| Fairly Difficult / Eher schwer | 50 |
| Difficult / Schwer | 30 |
| Very Difficult / Sehr schwer | 15 |

Then **calibrate against the audience identified in Step 1**:

- **Consumer-facing document.** Apply the component scores as-is.
- **Employee-facing document.** Add 5 to the component (consumer baseline is slightly stricter than employee baseline).
- **B2B sophisticated parties.** Add 15 to the component (genre-typical scores are lower for B2B; do not punish them for that).
- **Court filing, statute, internal-counsel document.** Add 25 to the component.

Cap calibrated components at 100.

Pillar score = mean of the calibrated components for all readability metrics computed. Round to integer.

## What to put in the pillar report section

For each metric, report:

```
Metric: Flesch Reading Ease (English)
Counts: W=4,812; S=215; Sy=8,037
Raw score: 28.4
Band: Very Difficult
Audience: consumers (no calibration adjustment)
Component score: 15
```

Then aggregate at the end of the section:

```
Pillar score: 18 / 100
Interpretation: Document scores in the "Very Difficult" band on every applied
metric. For a consumer-facing document, this is materially below the standard
of comparable well-drafted T&Cs (which typically score 55–65 on Flesch Reading
Ease).
```

## Edge cases

- **Documents under 100 words.** Do not produce a score. Note "Document too short for meaningful readability assessment".
- **Documents with tables or bullet-heavy sections.** Compute the metric on prose paragraphs only, exclude tables and bullet lists from W and S counts. Note in the methodology.
- **Documents with heavy mathematical notation or code.** Exclude code blocks from W; note in methodology.
- **Mixed-language documents.** Compute the metric on the dominant-language portion only; note the exclusion.
- **Hyphenated words.** Count as one word for W.
- **Numerals.** Count "1,000,000" as one word, with one syllable for FRE purposes (count as a long word for LIX since the rendered form is over 6 characters).

## Syllable counting heuristic (English)

For automated estimation when exact counts are not available:

1. Count vowel groups (`aeiouy`, with `y` only between consonants).
2. Subtract 1 for each silent terminal `e` (but not in `le`).
3. Add 1 if the word ends in `le` preceded by a consonant.
4. Minimum 1 syllable per word.

This is the textbook heuristic; it is approximate. State the heuristic in the methodology.

## Syllable counting heuristic (French)

1. Count vowel groups, treating `oi`, `ai`, `ei`, `au`, `eau`, `ou`, `eu` as single vowel groups.
2. Silent terminal `e` is generally silent in modern French — subtract 1 (except in poetry / liturgical contexts).
3. Words ending in *-tion*, *-sion* count the final group as one syllable, not two.
4. Minimum 1 syllable per word.

## Syllable counting heuristic (German)

1. Count vowel groups, treating *au*, *ei/ai*, *eu/äu*, *ie* as diphthongs (one syllable each).
2. Schwa terminations (*-e*, *-en*, *-er*, *-el*) generally count as a syllable in German (unlike French silent e).
3. Compounds: count syllables of each component separately and sum.
4. Minimum 1 syllable per word.

## Sources

- Flesch, R. (1948). *A New Readability Yardstick*. Journal of Applied Psychology, 32(3), 221–233.
- Kincaid, J. P. et al. (1975). *Derivation of New Readability Formulas* (Research Branch Report 8-75, US Navy).
- Kandel, L. & Moles, A. (1958). *Application de l'indice de Flesch à la langue française.* Cahiers d'études de Radio-Télévision.
- Amstad, T. (1978). *Wie verständlich sind unsere Zeitungen?* Universität Zürich.
- Bamberger, R. & Vanecek, E. (1984). *Lesen — Verstehen — Lernen — Schreiben.* Jugend und Volk Verlag.
- Björnsson, C.-H. (1968). *Läsbarhet.*
