---
name: legal-fr-clemensjl
title: Mandatory legal texts — France
description: Use when writing, reviewing, or fixing legally required texts for a French website, webshop, app, or newsletter — mentions légales, politique de confidentialité, bandeau cookies, CGV, CGU, droit de rétractation, garantie légale, déclaration d'accessibilité — or when asked whether a French online presence is conforme. Also use when a German, US, or generic-EU legal template is about to be reused for France, when personal data processing starts, or before a site goes live.
author: clemensjl
author_url: https://github.com/clemensjl/claude-skills/tree/main/skills/legal-fr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: regulatory
language: fr
sources:
- title: Accessibilite
  path: references/accessibilite.md
- title: Cgv Vente Distance
  path: references/cgv-vente-distance.md
- title: Checklist
  path: references/checklist.md
- title: Cookies
  path: references/cookies.md
- title: Donnees Personnelles
  path: references/donnees-personnelles.md
- title: Garantie Conformite
  path: references/garantie-conformite.md
- title: Intake
  path: references/intake.md
- title: Marketing
  path: references/marketing.md
- title: Mediation
  path: references/mediation.md
- title: Mentions Legales
  path: references/mentions-legales.md
- title: Plateformes Sren Dsa
  path: references/plateformes-sren-dsa.md
- title: Resiliation
  path: references/resiliation.md
- title: Retractation
  path: references/retractation.md
- title: Rgpd Interne
  path: references/rgpd-interne.md
---

# Mandatory legal texts — France

Drafting and auditing the texts a French online presence must publish. The governing instruments are the LCEN (loi n° 2004-575 du 21 juin 2004 pour la confiance dans l'économie numérique), the loi Informatique et Libertés (loi n° 78-17 du 6 janvier 1978) alongside the GDPR, the Code de la consommation, the Code de commerce, the Code des postes et des communications électroniques (CPCE), loi n° 2005-102 du 11 février 2005 for accessibility, and loi n° 2024-449 du 21 mai 2024 (loi SREN) for the DSA layer.

**Core principle.** France stacks three duties on the EU baseline that no generic template carries. First, the **mentions légales**: since 23 May 2024 they no longer sit in the famous article 6-III LCEN — the loi SREN moved them to **article 1-1 LCEN**, backed by a criminal offence in **article 1-2 LCEN** (one year and 75 000 €). Article 1-1 I 4° obliges the publisher to name its **hébergeur** with name, address and telephone number, a disclosure no other member state demands. Second, every B2C trader must name — and pay for — a **médiateur de la consommation** referenced by the CECMC (articles L612-1 and L616-1 du Code de la consommation). Third, cookies are policed under **article 82 de la loi 78-17** through the **CNIL's own doctrine** (délibération n° 2020-091 and recommandation n° 2020-092), which is more operational and more aggressively enforced than the EDPB baseline. A German or generic-EU template fails all three.

## Not legal advice

This skill produces drafts and audit findings, not legal advice. Before going live:

- With a webshop, subscription, payment flow, children's data, health data, or a platform hosting third-party content: **obtain sign-off from a lawyer (avocat)**.
- Free first-line help: **DGCCRF** for consumer law and reporting (`signal.conso.gouv.fr`, `economie.gouv.fr/dgccrf`), **CNIL** for data protection (`cnil.fr`, telephone helpline), **ARCOM** for DSA and digital accessibility (`arcom.fr`), the local **CCI** (`cci.fr`) for company-law and registration questions, the **CECMC** list of referenced médiateurs (`economie.gouv.fr/mediation-conso`), and free consultations at a **maison de justice et du droit** or the local **ordre des avocats**.
- Every generated text carries a visible `<!-- BROUILLON – non validé juridiquement -->` HTML comment until legal sign-off is confirmed. Never remove the marker silently.

Never omit or soften this section in the output.

## Workflow

1. **Run the intake first.** No text before the answers exist. Questions in `references/intake.md`. Unanswered items become `[[MISSING: …]]`, never invented.
2. **Determine the obligation matrix** (below): which texts this specific project actually needs.
3. **Read the reference file for each required text before drafting.** Never from memory — the article numbers are too specific and the LCEN renumbering of 2024 breaks recall.
4. **Run `references/checklist.md`** and report each finding with its article and its location.
5. Emit the sign-off notice and leave the draft marker in place.

**Output shape.** Exactly four parts, in this order:

1. the legal text or the audit finding itself, with the draft marker
2. the list of `[[MISSING: …]]` items the user must supply
3. adjacent obligations still open in the same project, one sentence each
4. the sign-off notice

The norm sits next to the statement it supports. Reference file names and paths belong in none of the four parts — they are working material, not deliverable.

## Obligation matrix

| Situation | Required texts, with the norm | Reference |
|---|---|---|
| Any online public communication service | Mentions légales (article 1-1 LCEN) | `mentions-legales.md` |
| Registered in the RCS or the RNE | RCS mention, unique identification number, capital, siège (article R123-237 du code de commerce) | `mentions-legales.md` |
| Any processing of personal data, including server logs | Politique de confidentialité (RGPD art 13/14 + loi 78-17) | `donnees-personnelles.md` |
| Cookies, analytics, pixels, embeds, third-party fonts | Consent banner and cookie policy (article 82 de la loi 78-17) | `cookies.md` |
| Selling to consumers online | CGV, precontractual information (L111-1, L221-5), order button (L221-14) | `cgv-vente-distance.md` |
| Selling to consumers online | Rétractation notice plus formulaire type (L221-18 ff, annexe à l'article R221-1) | `retractation.md` |
| Selling goods or digital content | Garantie légale de conformité (L217-3 ff), vices cachés (C. civ. 1641 ff) | `garantie-conformite.md` |
| Subscription or any contract concluded electronically | Fonctionnalité de résiliation (L215-1-1, D215-1 à D215-3) | `resiliation.md` |
| Any B2C trader | Named médiateur de la consommation (L612-1, L616-1) | `mediation.md` |
| Newsletter, email or SMS marketing, influencer campaigns | Opt-in (L34-5 CPCE), disclosure mentions (loi n° 2023-451) | `marketing.md` |
| B2C digital service, not a microenterprise | Accessibility conformity, déclaration d'accessibilité (art 47 loi 2005-102, L412-13 C. conso) | `accessibilite.md` |
| Hosting, forum, comments, marketplace, UGC | DSA point of contact, notice and action, CGU | `plateformes-sren-dsa.md` |
| Any personal data at all | Registre des traitements, contrats sous-traitants, breach process (internal, not published) | `rgpd-interne.md` |
| Audience under 15 | Joint consent of the minor and the holder of parental authority (article 45 de la loi 78-17) | `donnees-personnelles.md` |

## Hard rules

- **The mentions légales are in article 1-1 LCEN, not article 6-III.** Loi n° 2024-449 du 21 mai 2024 moved them there with effect 23 May 2024; article 6 LCEN now governs intermediary services. Any text or citation still pointing at "article 6-III de la LCEN" is out of date and gets rewritten, not patched. The offence is article 1-2 LCEN: one year and 75 000 € for a natural person or the de jure or de facto director of a legal person, 375 000 € for the legal person.
- **Name the hébergeur.** Article 1-1 I 4° LCEN requires the name, denomination or company name, the address **and** the telephone number of the hosting provider. Omitting the host is the single most common defect in French mentions légales built from a foreign template.
- **The ODR platform is dead.** Règlement (UE) 2024/3228 repealed règlement (UE) n° 524/2013 with effect 20 July 2025; complaints stopped being accepted on 20 March 2025. Article L616-2 du Code de la consommation still formally refers to it and is now without object. Never emit an ODR link. If a legacy text contains one, delete it and point to the named médiateur instead.
- **The digital consent age is 15, not 16.** Article 45 de la loi 78-17: a minor may consent alone from fifteen; below fifteen the processing is lawful only if consent is given **conjointement** by the minor and the holder or holders of parental authority.
- **Nothing fires before consent.** No analytics, pixel, map, video or third-party font request may be sent before an affirmative act. Under CNIL délibération n° 2020-091, continued browsing is not consent and pre-ticked boxes are void; under recommandation n° 2020-092 refusing must be as easy as accepting, on the first layer of the banner.
- **The fonctionnalité de rétractation is mandatory since 19.06.2026.** Article L221-21 alinéa 3 du Code de la consommation, inserted by ordonnance n° 2026-2 du 5 janvier 2026, requires a free withdrawal function on the online interface for **all** distance contracts concluded through one — not only financial services, despite the ordonnance's title. Article D221-5 (décret n° 2026-3) fixes the labels: « renoncer au contrat ici » and, on the separate confirmation control, « confirmer la rétractation », plus an accusé de réception on a durable medium carrying the content of the declaration and the date and heure it was sent. The online *form* under alinéa 2 remains optional; the *function* is not.
- **The order button must say it costs money.** Article L221-14 du Code de la consommation: the function used to validate the order carries, **à peine de nullité**, the clear and legible wording « commande avec obligation de paiement » or an equally unambiguous formula. "Valider", "Continuer", "Envoyer" do not bind the consumer.
- **Every B2C trader names a médiateur.** Article L612-1 gives the consumer a free right of recourse; article L616-1 obliges the trader to communicate the competent médiateur's contact details. Breach is an administrative fine of up to 3 000 € for a natural person and 15 000 € for a legal person (article L641-1). A médiateur must be actually contracted and referenced by the CECMC — inventing a name is worse than omitting one.
- **Repair extends the guarantee by six months.** Article L217-13 du Code de la consommation: « Tout bien réparé dans le cadre de la garantie légale de conformité bénéficie d'une extension de cette garantie de six mois. » Replacement after a failed repair starts a fresh guarantee period. This has no German or generic-EU counterpart and must appear in the CGV.
- **Never invent company facts.** SIREN, RCS city, capital social, TVA intracommunautaire number, ordre professionnel, hébergeur, supervisory authority, registered address: if unknown it becomes `[[MISSING: …]]` in the text and in the report back to the user.
- **CGU and CGV are different documents.** CGV govern the sale (Code de la consommation, articles L111-1, L221-5, L221-14, L217-3 ff). CGU govern the use of the service — account, moderation, licence, liability, DSA notice and action. Merging them produces a document that satisfies neither.

## False friends

Foreign duties feel plausible and get invented under time pressure. None of these exists in France in the stated form.

| Imported assumption | Position in France |
|---|---|
| § 5 TMG / § 5 DDG Impressum | Article 1-1 LCEN, plus article R123-237 du code de commerce for registered traders |
| "Impressum" as the link label | The page is called **Mentions légales**; the Austrian/German Offenlegung has no counterpart |
| Kündigungsbutton, § 312k BGB | Article L215-1-1 with D215-1 à D215-3: an entry point marked « résilier votre contrat » and a confirmation marked « notification de la résiliation ». Different wording, different flow, different scope |
| German Widerrufsbutton § 356a BGB transposed directly into French wording | Same underlying norm — CRD article 11a — but the prescribed labels are French and fixed: « renoncer au contrat ici » and « confirmer la rétractation » (article D221-5). Never translate the German strings. See `retractation.md`. |
| "Widerrufsrecht" / "Rücktrittsrecht" | **Droit de rétractation**, 14 days, article L221-18 |
| Handelsregister, HRB, Amtsgericht | RCS with the city of the greffe, numéro unique d'identification (SIREN), tribunal de commerce or tribunal des activités économiques |
| USt-IdNr. after § 27a UStG | Numéro de TVA intracommunautaire, format FR + 2 characters + SIREN |
| BDSG, DPO required from 20 employees | Loi 78-17; no headcount threshold, GDPR article 37 applies unchanged |
| Consent age 16 | 15, article 45 de la loi 78-17 |
| Cookie rules taken from the EDPB alone | CNIL délibération n° 2020-091 and recommandation n° 2020-092 are the operative doctrine and are enforced under article 82 de la loi 78-17 |
| Link to the EU ODR platform | Shut down 20 July 2025, see hard rules |
| Citing directives (2011/83/UE, 2019/771) in the CGV | Cite the Code de la consommation articles that actually bind: L111-1, L221-5, L221-14, L221-18, L221-28, L217-3, L217-13 |
| US "Terms of Service" and "Privacy Policy" as one page | Mentions légales, politique de confidentialité, CGV and CGU are four distinct documents with distinct mandatory content |

If an obligation comes to mind that cannot be traced to a concrete French norm, it is reported as an open question, not asserted.

## Common mistakes

| Mistake | Why it is wrong |
|---|---|
| Mentions légales without the hébergeur | Article 1-1 I 4° LCEN requires name, address and telephone of the host |
| Citing article 6-III LCEN | Repealed in that form since 23 May 2024 by loi n° 2024-449 |
| "Ce site utilise des cookies. OK" | No valid consent under article 82 de la loi 78-17; no refusal option on the first layer |
| Google Fonts, Maps or YouTube loaded before consent | Terminal access and third-country transfer before an affirmative act |
| Privacy policy without a legal basis per purpose | RGPD article 13(1)(c) requires the basis for each processing |
| No mention of the directives post mortem | Article 85 de la loi 78-17, a French-only right |
| Order button labelled "Commander" alone | Article L221-14 requires the payment obligation to be explicit, à peine de nullité |
| No médiateur named | Articles L612-1 and L616-1; administrative fine under L641-1 |
| Garantie limited to one year for new goods B2C | Article L217-3 gives two years; article L217-7 presumes the defect for 24 months |
| Subscription cancellable only by registered letter | Article L215-1-1 requires an electronic cancellation functionality |
| Homepage without the accessibility conformity mention | Article 47 de la loi n° 2005-102 as amended by ordonnance n° 2023-859 |
| Influencer post without the commercial-intent mention | Loi n° 2023-451 as amended by ordonnance n° 2024-978 |

## Reference files

Each contains the statutory basis with article numbers and a status date, the mandatory content points, a template with `[[PLACEHOLDER]]` slots, and a `## Checkpoints` list.

If the `legal-eu` skill is installed, read it for the EU-level baseline; this skill covers the national layer on top of it.

- `references/intake.md` — questions to answer before the first text
- `references/mentions-legales.md` — LCEN articles 1-1 and 1-2, R123-237 code de commerce, regulated professions
- `references/donnees-personnelles.md` — RGPD articles 13/14 plus the loi 78-17 deviations, ages, post-mortem directives
- `references/rgpd-interne.md` — registre des traitements, sous-traitance, violations, DPO, CNIL référentiels
- `references/cookies.md` — article 82 loi 78-17, CNIL 2020-091 and 2020-092, cookie walls, audience measurement, enforcement
- `references/cgv-vente-distance.md` — L111-1, L221-5, L221-14, double clic, prices, product mentions
- `references/retractation.md` — L221-18 to L221-28, the annexe à l'article R221-1 model form
- `references/garantie-conformite.md` — L217-3 ff, the six-month repair extension, digital content, vices cachés
- `references/resiliation.md` — L215-1, L215-1-1, décret n° 2023-417 and articles D215-1 à D215-3
- `references/mediation.md` — L612-1, L616-1, L616-2, the CECMC list, the ODR shutdown
- `references/marketing.md` — L34-5 CPCE, CNIL prospection doctrine, loi n° 2023-451 influence commerciale
- `references/accessibilite.md` — article 47 loi 2005-102, RGAA, EAA under L412-13 du Code de la consommation
- `references/plateformes-sren-dsa.md` — DSA, LCEN article 6 as rewritten, loi SREN, ARCOM age verification
- `references/checklist.md` — pre-launch checklist with the article for each item
