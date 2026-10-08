# Foreign-language preservation policy

Every report this skill emits is in English by default. But the underlying property regimes are governed by statutes, regulators, document forms, and registries that have **native names in the local language** — not English. If the report paraphrases those to English without keeping the original, the reader cannot search for the original term, look it up at the regulator, or quote it to a local lawyer.

This document codifies the **preservation policy**: the rule, the format, when it applies, what's exempt, and how it integrates with anti-hallucination.

---

## The rule

> **Every native-language statute / regulator / document form / registry / programme name in the report MUST appear in its original form alongside the English translation.** Translate to help the reader understand; preserve the native term so the reader can search, cite, or query.

This is **non-negotiable** — same tier as the anti-hallucination contract. A report that says "the French Civil Code Article 682" without `Code civil Art. 682` next to it has degraded the reader's ability to verify the claim.

---

## The format

The native term is **primary**; the English is the gloss. Two acceptable patterns:

### Pattern A — inline gloss (preferred for short terms)

```
Code civil Art. 682 (French Civil Code Article 682)
Naalakkersuisut (Government of Greenland)
Inatsisartutlov nr. 78 af 21. november 2025 (Greenlandic Parliament Act No. 78 of 21 November 2025)
Hypothèque Légale Spéciale (statutory mortgage / bond on the title)
```

### Pattern B — backtick-quoted (preferred inside dense prose or when the native term contains punctuation)

```
The `Loi 65-557 du 10 juillet 1965` governs co-ownership (copropriété) in France.
The `Bauleiter` (site supervisor) must be appointed under German construction law.
The `不動産登記法` (Real Property Registration Act, Japan) requires deed registration within 30 days.
```

### Pattern C — quoted with translation footnote (for long native passages)

```
The Mineral Resources Authority states: "In Greenland there is no privately owned land, all rights to any use of land is administered by the Government of Greenland."
```

Source-anchored direct quotes preserve the native passage verbatim; a translation follows only if the quote is in a language the report's English-reader audience would not recognise.

---

## When the policy applies

Preserve the native term whenever ANY of:

1. **Statute names** — `Code civil`, `Bürgerliches Gesetzbuch`, `Codice Civile`, `Inatsisartutlov`, `Løgtingslóg`, `Tynwald Act`, etc.
2. **Article / section identifiers** — `Art. 682`, `§ 917 BGB`, `c.c. Art. 1051`, `s. 35A`
3. **Regulator / authority names** — `Naalakkersuisut`, `Comptroller of Revenue`, `JFSC`, `BaFin`, `AMF`, `DLD`
4. **Document forms / instruments** — `Modelo 720`, `Form 8938`, `T1135`, `IFI`, `Quadro RW`, `FBAR FinCEN 114`, `eligibility certificate (CG50A)`
5. **Registry / cadastre names** — `Tinglysning`, `Land Registry`, `Catasto`, `Cadastre`, `Grundbuch`, `Public Registry of Contracts`
6. **Programme / scheme names** — `Inatsisartutlov nr. 78/2025`, `2(1)(e) HVR`, `Cat-2`, `HEPSS`, `Goldener Visum`, `NHR`, `Olim`, `Bestellerprinzip`
7. **Court / tribunal names** — `Royal Court of Jersey`, `Tribunal de grande instance`, `Cour Royale`, `Bundesgerichtshof`, `Hoge Raad`
8. **Tax / fee names** — `Eigenmietwert`, `taxe foncière`, `IMU`, `IBI`, `IRPF`, `Modelo 210`, `kommunalskattur`, `tinglýsingargjald`
9. **Legal terms with no English equivalent** — `usucapione`, `okupa`, `arealtildeling`, `partages`, `mainlevée`, `Hypothèque Légale Spéciale`, `Coutume de Normandie`, `Auflassung`, `vente en l'état futur d'achèvement` (VEFA)

---

## When the policy DOES NOT apply

Don't waste reader attention preserving terms that are already in their canonical English form:

- **English-origin terms** — "Land Registry" (UK/IM/JE/GG use this as the canonical name in English contexts), "Companies Act", "Stamp Duty"
- **Multilateral / international institutions with well-known English names** — EU, OECD, IMF, IPCC, UN, WTO, BIS, ECB, IFRS
- **Currencies in their ISO codes** — EUR, USD, GBP, DKK, CHF, JPY — though the local form (€, $, £) may also appear
- **Country / region names** — France, Germany, Hong Kong, etc.
- **Genuinely English statutes from English-speaking jurisdictions** — `Stamp Duties (Amendment) Act 37/2024` (Gibraltar, English-origin) doesn't need a "translation" since it's already English

If you're unsure: **preserve**. The cost of an extra parenthetical is trivial; the cost of a reader unable to find the original is large.

---

## How this integrates with anti-hallucination

The foreign-language preservation policy is layer 8 of the anti-hallucination contract:

1. **Sourced** — every claim has a primary-government URL
2. **Computed** — every derived figure shows its inputs
3. **Estimated** — every model-inference is labelled `~` / `est.` / `≈`
4. **Date-stamped** — every numeric fact has a `(<year> data)` stamp
5. **Confidence-labelled** — every section ends with a `**Confidence**` label
6. **Native-term-preserved** ← **this policy**
7. **Forbidden-phrasings-clean** — no "approximately X" / "industry average" / etc.
8. **Listing-vs-cadastre-honest** — listing claims tagged separately from cadastral

A claim that paraphrases a French statute as "the Civil Code Article 682" without `Code civil Art. 682` next to it is technically sourced + dated + confidence-labelled but FAILS the preservation check. The CI guard and authoring guidance enforce it.

---

## How this integrates with `--lang=<iso639-1>` translation

When the operator requests an output translation via `--lang` (see `shared/output-translation.md`), the preservation policy **gets stricter, not looser**:

- The translated report MUST keep the original-language native terms verbatim (untranslated), in whatever target-language paragraphs reference them
- Example: an `--lang=de` translation of a Jersey playbook mentions `Loi (1991) sur la copropriété` AS-IS in the German prose — the translation gloss is added in German, not by re-translating the French native term to German
- Glossary-mode (`--lang-scope=glossary-only`) is the explicit reverse pattern — a separate native-term → target-language explanation appendix

This protects the reader who is reading a non-English report but still needs to look up the native statute.

---

## Authoring checklist

Before submitting any output (terminal, MD file, or report):

- [ ] Every statute named in English ALSO has its native form (or vice versa) — `Code civil Art. 682` not just "Civil Code Article 682"
- [ ] Every regulator named in English ALSO has its native form — `Naalakkersuisut (Government of Greenland)` not just "Government of Greenland"
- [ ] Every document / form / instrument has its native form — `Modelo 720`, not "Spanish foreign-asset declaration form"
- [ ] Every native-language passage that's worth quoting is **quoted verbatim** with a translation only if the audience couldn't parse it
- [ ] Programme names use the official local label first — `Inatsisartutlov nr. 78/2025` not "the November 2025 Greenland Real Estate Acquisition Act"
- [ ] Where multiple official languages coexist (Jersey: English + French + Norman-French · Greenland: Greenlandic + Danish · Faroe Islands: Faroese + Danish), all relevant forms appear

---

## Examples from shipped playbooks

These are the kinds of preservation patterns the policy aims to make universal. Each example is from a shipped country playbook:

| Country | Native form preserved | English gloss |
|---|---|---|
| France | `Code civil Art. 682` | French Civil Code Article 682 (right of way over enclosed land) |
| Germany | `BGB § 917` | German Civil Code Section 917 (Notwegrecht / necessity easement) |
| Greenland | `Inatsisartutlov nr. 78 af 21. november 2025` | Greenlandic Parliament Act No. 78 of 21 November 2025 |
| Greenland | `Naalakkersuisut` | Government of Greenland |
| Greenland | `arealtildeling` | right-to-use land allocation (NOT ownership — Greenland has no private land) |
| Jersey | `Loi (1991) sur la copropriété des immeubles bâtis` | Jersey Law on Co-Ownership of Built Properties 1991 |
| Jersey | `Comptroller of Revenue` | tax authority (Jersey) |
| Jersey | `Hypothèque Légale Spéciale` | statutory special mortgage / bond on title (Jersey + Guernsey) |
| Guernsey | `Greffe` + `Cour Royale` | Court Registry + Royal Court (Guernsey) |
| Guernsey | `Coutume de Normandie` | Norman customary law (Guernsey land-law foundation) |
| Isle of Man | `Tynwald` | Manx Parliament |
| Isle of Man | `advocate` (NOT solicitor) | Manx-qualified legal practitioner |
| Faroe Islands | `Løgting` + `Løgtingslóg` | Faroese Parliament + Parliamentary Act |
| Faroe Islands | `kommunalskattur` | municipal income tax (Faroe Islands) |
| Italy | `Codice Civile Art. 1051` | Italian Civil Code Article 1051 (right of way over enclosed land) |
| Spain | `Código Civil Art. 564` | Spanish Civil Code Article 564 (servidumbre de paso) |
| Japan | `不動産登記法` (Real Property Registration Act) | governs deed registration in Japan |
| Japan | `既存不適格` vs `違反` | "lawful pre-existing nonconforming" vs "illegal construction" |
| Mexico | `fideicomiso` | bank trust required for foreigners in Restricted Zone |
| Brazil | `terreno de marinha` | foreshore land + `laudêmio` coastal-zone fee |

---

## Audit (future)

A separate sweep (task #31 in the project task list) audits all 109 existing playbooks for native-term-preservation violations. Until that sweep ships, new playbooks (any added after 2026-05-27) must comply from day one.

---

## Status

Last refreshed: 2026-05-27.
**Confidence**: HIGH (policy doc; rule is deterministic and machine-checkable).
