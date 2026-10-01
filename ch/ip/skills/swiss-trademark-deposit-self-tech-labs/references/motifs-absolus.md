# Motifs absolus

Use this reference for Swiss absolute-ground analysis under art. 2 LPM and related IPI practice.

## Core Checks

- Run `sign_risk_screen` first to surface obvious issues, then do legal reasoning. The screen is conservative and does not replace the analysis.
- Distinctiveness: the sign must identify commercial origin, not merely describe the goods/services.
- Public domain: generic, customary, laudatory, or necessary signs are normally refused unless secondary meaning is shown.
- Descriptiveness: assess direct meaning, ordinary perception, foreign-language comprehension in Switzerland, and the connection to claimed goods/services.
- Deception: reject signs that mislead on nature, quality, origin, production method, or other material characteristics.
- Public order and morality: flag offensive, unlawful, or misleading official associations.
- Official signs: check Swiss flag, Swiss cross, Red Cross, public coats of arms, official emblems, and protected international signs.
- Indications of provenance: Swissness and geographic terms require consistency with goods/services and applicable provenance rules.
- Shapes and 3D signs: analyze usual shape, technical necessity, aesthetic value, and imposed form.
- Language: account for ordinary understanding in German, French, Italian, and English; do not screen a verbal sign only in the filing language.

## Risk Scale

- Green: arbitrary or fanciful for the goods/services.
- Orange: evocative, weakly distinctive, descriptive in part, or rescued by figurative/composite elements.
- Red: directly descriptive, generic, deceptive, official-sign conflict, or technically necessary shape.

## MCP Discipline

Before a final orange or red conclusion, call `search_taf_decisions` with the sign, key descriptive terms, relevant classes, and statutory article where known. Use `find_similar_signs` for comparable sign structures and `get_taf_decision` when a reference materially affects the conclusion.

## Practitioner Notes

Distinguish absolute grounds from relative grounds. The IPI examines absolute grounds at filing but does not perform opposition-style conflict analysis. For weak verbal marks, consider a genuinely distinctive composite, narrower goods/services, or an acquired-distinctiveness strategy where the facts support it. Registration of a composite does not imply exclusive rights in each descriptive element.

## Official Sources

- [IPI — Grounds for refusal](https://www.ige.ch/en/protecting-your-ip/trade-marks/before-you-apply/requirements-for-protection/grounds-for-refusal/segni-pubblici-protetti): descriptiveness, deception, public order, multilingual examination, acquired distinctiveness, and the boundary between examination and earlier-right searches.
- [IPI — Requirements for protection](https://www.ige.ch/en/protecting-your-ip/trade-marks/before-you-apply/requirements-for-protection): official overview and links to protected public signs and conflict risk.

The local TAF report is an extracted, partial corpus. Treat extraction confidence as a retrieval aid, not a reliability score for the legal proposition itself.
