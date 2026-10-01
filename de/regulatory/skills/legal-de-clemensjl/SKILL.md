---
name: legal-de-clemensjl
title: German mandatory online legal texts
description: Use when writing, reviewing, or fixing legally required texts for a German website, webshop, app, or newsletter — Impressum, Datenschutzerklärung, Cookie-Banner, AGB, Widerrufsbelehrung, Kündigungsbutton, Gewährleistung, Barrierefreiheitsinformationen — or when asked whether a German online presence is rechtskonform. Also use when an Austrian or US legal template is about to be reused for Germany, when personal data processing starts, or before a site goes live.
author: clemensjl
author_url: https://github.com/clemensjl/claude-skills/tree/main/skills/legal-de
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: regulatory
language: de
sources:
- title: Barrierefreiheit
  path: references/barrierefreiheit.md
- title: Checklist
  path: references/checklist.md
- title: Cookies
  path: references/cookies.md
- title: Datenschutz Intern
  path: references/datenschutz-intern.md
- title: Datenschutz
  path: references/datenschutz.md
- title: Fernabsatz Agb
  path: references/fernabsatz-agb.md
- title: Gewaehrleistung
  path: references/gewaehrleistung.md
- title: Impressum
  path: references/impressum.md
- title: Intake
  path: references/intake.md
- title: Kuendigungsbutton
  path: references/kuendigungsbutton.md
- title: Marketing
  path: references/marketing.md
- title: Produktpflichten
  path: references/produktpflichten.md
- title: Streitbeilegung Dsa
  path: references/streitbeilegung-dsa.md
- title: Widerruf
  path: references/widerruf.md
---

# German mandatory online legal texts

Compulsory texts for German websites, webshops, apps and newsletters. The governing acts are DDG (Digitale-Dienste-Gesetz, the German digital services act), TDDDG (Telekommunikation-Digitale-Dienste-Datenschutz-Gesetz, the telecom and digital services privacy act), MStV (Medienstaatsvertrag, the interstate media treaty), DSGVO/BDSG, BGB and EGBGB, UWG, PAngV, BFSG and BFSGV, VSBG, plus the product-side acts VerpackG/VerpackDG, ElektroG, BattDG and TextilKennzG.

**Core principle: § 5 TMG no longer exists.** The Telemediengesetz was repealed and replaced by the Digitale-Dienste-Gesetz on **14.05.2024** (DDG of 06.05.2024, BGBl. 2024 I Nr. 149). The Impressum duty is now **§ 5 DDG**; the liability privilege is **§ 7 DDG**; the ePrivacy/cookie rule sits in **§ 25 TDDDG** (the TTDSG was renamed TDDDG by the same act); and the NetzDG is gone, absorbed into the DSA and DDG. Almost every CMS plugin, generator and language model still emits "§ 5 TMG", "§ 25 TTDSG" or "§ 55 RStV". A text carrying any of those is out of date on its face and gets rewritten, not patched.

## Not legal advice

This skill produces drafts and findings, not legal advice. Before go-live:

- Webshop, subscription, payment processing, children's data, health data or platform operation: **obtain sign-off from a lawyer.**
- Free first-line help in Germany: the local **IHK** (Industrie- und Handelskammer, chamber of commerce — `ihk.de`) for Impressum and e-commerce duties; the competent **Landesdatenschutzbehörde** (state DPA, list at `bfdi.bund.de`) and the **BfDI** for data protection questions; the **Bundesfachstelle Barrierefreiheit** (`bundesfachstelle-barrierefreiheit.de`), which advises Kleinstunternehmen free of charge under § 15 BFSG; the **Verbraucherzentrale** (`verbraucherzentrale.de`) on the consumer side.
- Every generated text carries a visible `<!-- ENTWURF – juristisch nicht freigegeben -->` HTML comment until the user confirms legal sign-off. Never remove the marker silently.

Never omit and never soften this section in the output.

## Workflow

1. **Collect the facts before writing anything.** Without the answers every text is guesswork. Questions in `references/intake.md`.
2. **Determine the obligation matrix** (below): which texts this specific project actually needs.
3. **Read the matching reference file for each obligation, then draft.** Never from memory — the section numbers are too specific and several changed in 2024–2026.
4. **Run `references/checklist.md`,** report findings with the norm and the location.
5. Output the sign-off notice, leave the draft marker in place.

**Output shape.** Exactly four parts, in this order:

1. the legal text or finding itself, with the draft marker
2. the list of `[[MISSING: …]]` items the user must supply
3. adjacent open obligations in the same project, one sentence each
4. the sign-off notice

The norm sits inline next to the statement it belongs to. Reference file names and paths belong in none of the four parts — they are working material, not deliverable.

## Obligation matrix

| Situation | Required texts with norm | Reference |
|---|---|---|
| Any commercially operated website or app | Impressum (§ 5 DDG), responsible person if journalistic-editorial (§ 18 Abs 2 MStV) | `impressum.md` |
| Any processing of personal data, including server logs and contact forms | Datenschutzerklärung (Art 13, 14 DSGVO) | `datenschutz.md` |
| Non-essential cookies, analytics, pixels, embeds, remote fonts | Consent before access, cookie section (§ 25 TDDDG) | `cookies.md` |
| Selling to consumers online | Pre-contractual information (§ 312d BGB, Art 246a EGBGB), correct order button (§ 312j Abs 3 BGB), prices (PAngV) | `fernabsatz-agb.md` |
| Selling to consumers online | Widerrufsbelehrung and Muster-Widerrufsformular (§§ 312g, 355, 356 BGB, Anlagen 1 und 2 zu Art 246a EGBGB) plus the electronic Widerrufsfunktion (§ 356a BGB) | `widerruf.md` |
| Any paid continuing obligation concluded online | Kündigungsbutton (§ 312k BGB) | `kuendigungsbutton.md` |
| Selling goods or digital products | Gewährleistung (§§ 434 ff BGB), digital products and updates (§§ 327 ff, 327f BGB), Garantie (§ 479 BGB) | `gewaehrleistung.md` |
| Newsletter, e-mail, telephone or SMS advertising; sponsored content | § 7 UWG, § 5a Abs 4 UWG, § 6 DDG | `marketing.md` |
| B2C services in e-commerce, not a Kleinstunternehmen | Accessibility of the service and the § 14 Abs 1 Nr 2 BFSG information | `barrierefreiheit.md` |
| Shipping goods, electricals, batteries or textiles | LUCID registration, stiftung ear, BattDG, TextilKennzG | `produktpflichten.md` |
| Consumer contracts; hosting, UGC, marketplaces | § 36 VSBG statement, DSA contact points and notice-and-action | `streitbeilegung-dsa.md` |
| Any personal data at all | Verarbeitungsverzeichnis, AVV, TOM, breach process, DPO check (§ 38 BDSG) — internal, not published | `datenschutz-intern.md` |

## Hard rules

- **No § 5 TMG, no § 25 TTDSG, no § 55 RStV, no NetzDG.** TMG and NetzDG were repealed on 14.05.2024 by the DDG; the TTDSG was renamed TDDDG on the same date. Correct citations are § 5 DDG, § 7 DDG, § 25 TDDDG, § 18 MStV. A text citing the old norms is generated from a stale template and is rewritten in full.
- **Delete every ODR link.** Regulation (EU) 2024/3228 repealed the ODR Regulation and the EU ODR platform stopped operating on **20.07.2025**. The Art 14 ODR-VO linking duty is gone. A remaining link is dead and can itself be a misleading commercial practice. Never re-insert it, whatever a template says.
- **The consent age in Germany is 16.** Art 8 Abs 1 DSGVO sets 16; Germany did not use the opening clause to lower it, and the BDSG contains no lower threshold. Below 16 the holder of parental responsibility must consent. Do not copy Austria's 14.
- **No terminal access before consent.** § 25 Abs 1 TDDDG requires consent for storing or reading information on the user's device, independent of whether the data is personal. Only transmission and strictly necessary access are exempt (§ 25 Abs 2 TDDDG). No analytics, pixel, map, video or remote-font request may fire before an active decision.
- **The order button must read "zahlungspflichtig bestellen".** § 312j Abs 3 BGB requires the button to be labelled legibly *with nothing other than* those words or an equally unambiguous formulation. Otherwise the consumer is not bound (§ 312j Abs 4 BGB). "Absenden", "Weiter", "Jetzt kaufen" fail.
- **Three different buttons, three different norms.** Order button: **§ 312j Abs 3 BGB** ("zahlungspflichtig bestellen"). Cancellation button for continuing obligations: **§ 312k BGB** ("Verträge hier kündigen" plus "jetzt kündigen"). Electronic withdrawal function: **§ 356a BGB** ("Vertrag widerrufen" plus "Widerruf bestätigen"), mandatory from **19.06.2026**. These are routinely confused; every statement about a button carries the right paragraph or none.
- **No Austrian norms.** ECG, MedienG, FAGG, KSchG, UGB, Firmenbuch, GISA, UID, "Rücktrittsrecht", "Bezirksgericht": if any of these appear, the text came from an Austrian template and is rewritten, not patched.
- **Never invent facts about the business.** Handelsregister number and court, VAT ID, Geschäftsführer, supervisory authority, chamber, professional title, registered address: if unknown it becomes `[[MISSING: Handelsregisternummer]]` both in the text and in the report back to the user.
- **Geographic address, no PO box.** § 5 Abs 1 Nr 1 DDG requires the address of the place of establishment. For a sole trader without business premises that is the home address. If the user does not want that published, it is a business decision (coworking address, registered office), not a wording problem. Raise it immediately instead of working around it.

## False friends

| Assumption imported from elsewhere | Position in Germany |
|---|---|
| § 5 TMG Impressum | § 5 DDG since 14.05.2024; TMG repealed |
| § 25 TTDSG cookies, or § 15 Abs 3 TMG pseudonymous tracking | § 25 TDDDG; § 15 TMG has not existed since 2021 |
| § 55 Abs 2 RStV responsible person | § 18 Abs 2 MStV since 07.11.2020 |
| NetzDG reporting duties for platforms | Repealed 14.05.2024; DSA plus DDG apply |
| Austrian § 5 ECG, §§ 24/25 MedienG, § 14 UGB | § 5 DDG plus § 18 MStV; company data from § 35a GmbHG / § 80 AktG / § 37a HGB |
| Austrian "Rücktrittsrecht", "Rücktrittsbelehrung" | Widerrufsrecht, Widerrufsbelehrung (§§ 312g, 355 BGB) |
| Austrian FAGG § 8 order button, § 13a FAGG withdrawal button | § 312j Abs 3 BGB and § 356a BGB — different wording, different dates |
| Austrian consent age 14 (§ 4 Abs 4 DSG) | 16, Art 8 DSGVO unmodified |
| Firmenbuch, FN, UID ATU, GISA, Bezirksgericht | Handelsregister, HRA/HRB, USt-IdNr. DE (§ 27a UStG), Amtsgericht |
| US: "no cookie banner needed", opt-out is enough | § 25 Abs 1 TDDDG requires prior opt-in consent |
| US: "Terms of Service" / "Privacy Policy" as a legal category | AGB measured against §§ 305–310 BGB; Datenschutzerklärung measured against Art 13/14 DSGVO |
| US: arbitration clause and class-action waiver in consumer terms | Ineffective against German consumers under §§ 307 ff BGB |
| "Erklärung zur Barrierefreiheit" as under BITV 2.0 | That is public-sector law (§ 12b BGG). Private business owes the information under § 14 Abs 1 Nr 2 BFSG in conjunction with Anlage 3 Nr 1 BFSG |

If a duty comes to mind that cannot be traced to a concrete German norm, do not assert it — report it as an open question.

## Common mistakes

| Mistake | Why it is wrong |
|---|---|
| Impressum citing § 5 TMG | The act was repealed on 14.05.2024 |
| "Diese Website verwendet Cookies. OK" | Not consent within § 25 Abs 1 TDDDG |
| Google Fonts loaded from Google servers | LG München I, 20.01.2022, 3 O 17493/20: €100 damages under Art 82 DSGVO for dynamic embedding without consent |
| Datenschutzerklärung without a legal basis per purpose | Art 13 Abs 1 lit c DSGVO requires the basis for each processing operation |
| "Jetzt kaufen" as the order button | § 312j Abs 3 BGB demands the payment obligation in the label |
| Cancellation button behind a login | Incompatible with the "unmittelbar und leicht zugänglich" requirement of § 312k BGB |
| Retention offers on the cancellation confirmation page | BGH, 16.07.2026, I ZR 200/25: the confirmation page may contain nothing beyond what § 312k BGB provides |
| No electronic Widerrufsfunktion in the shop | § 356a BGB applies from 19.06.2026 to distance contracts concluded via an online interface |
| Widerrufsbelehrung without the Muster-Widerrufsformular | Anlage 2 zu Art 246a § 1 Abs 2 EGBGB is a mandatory component |
| Strike-through price without the 30-day reference | § 11 Abs 1 PAngV requires the lowest total price of the last 30 days |
| Newsletter without double opt-in | § 7 Abs 2 Nr 2 UWG requires prior express consent and the sender bears the burden of proof |
| Shop live without LUCID registration | § 9 VerpackG / VerpackDG: registration precedes the first shipment; unregistered distribution is prohibited |
| ODR link still in the Impressum | Platform shut down 20.07.2025 |

## Reference files

Each contains the statutory basis with a status date, the mandatory content points, a template with `[[…]]` slots, and checkpoints.

If the `legal-eu` skill is installed, read it for the EU-level baseline; this skill covers the national layer on top of it.

- `references/intake.md` — questionnaire to run before the first text
- `references/impressum.md` — § 5 DDG, § 18 MStV, § 35a GmbHG, § 80 AktG, § 27a UStG, DSA contact point
- `references/datenschutz.md` — Art 13/14 DSGVO, BDSG deviations, § 26 BDSG, age 16, third countries
- `references/datenschutz-intern.md` — § 38 BDSG DPO threshold, Verarbeitungsverzeichnis, AVV, TOM, breach reporting
- `references/cookies.md` — § 25 TDDDG, § 26 TDDDG and EinwV, banner requirements, fonts/maps/video
- `references/fernabsatz-agb.md` — § 312d BGB, Art 246a EGBGB, § 312j Abs 3 BGB, § 312l BGB, PAngV
- `references/widerruf.md` — §§ 312g, 355, 356, 356a BGB, Anlagen 1 und 2, exceptions
- `references/kuendigungsbutton.md` — § 312k BGB, exact wording, case law on placement
- `references/gewaehrleistung.md` — §§ 434 ff BGB, §§ 327 ff BGB, § 327f, § 479 BGB
- `references/marketing.md` — § 7 UWG, § 5a Abs 4 UWG, § 6 DDG, double opt-in evidence
- `references/barrierefreiheit.md` — BFSG, BFSGV, Kleinstunternehmen, Anlage 3 information, market surveillance
- `references/produktpflichten.md` — VerpackG/VerpackDG and LUCID, ElektroG, BattDG, TextilKennzG
- `references/streitbeilegung-dsa.md` — §§ 36, 37 VSBG, ODR shutdown, DSA and DDG platform duties
- `references/checklist.md` — pre-launch checklist mapped to norms
