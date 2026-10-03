---
name: legal-it
title: Italian mandatory online legal texts
description: Use when writing, reviewing, or fixing legally required texts for an Italian website, webshop, app, or newsletter — informazioni sul sito, informativa privacy, cookie policy and banner, condizioni generali di vendita, informativa sul recesso, modulo di recesso, garanzia di conformità, dichiarazione di accessibilità — or when asked whether an Italian online presence is compliant. Also use when a German, US or generic-EU legal template is about to be reused for Italy, when personal data processing starts, or before a site goes live.
author: clemensjl
author_url: https://github.com/clemensjl/claude-skills/tree/main/skills/legal-it
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
sources:
- title: Accessibilita
  path: references/accessibilita.md
- title: Checklist
  path: references/checklist.md
- title: Cookie tracker
  path: references/cookie-tracker.md
- title: Garanzia conformita
  path: references/garanzia-conformita.md
- title: Identificazione sito
  path: references/identificazione-sito.md
- title: Influencer pubblicita
  path: references/influencer-pubblicita.md
- title: Informativa privacy
  path: references/informativa-privacy.md
- title: Intake
  path: references/intake.md
- title: Marketing diretto
  path: references/marketing-diretto.md
- title: Piattaforme dsa
  path: references/piattaforme-dsa.md
- title: Privacy interna
  path: references/privacy-interna.md
- title: Recesso
  path: references/recesso.md
- title: Risoluzione controversie
  path: references/risoluzione-controversie.md
- title: Vendita online
  path: references/vendita-online.md
---

# Italian mandatory online legal texts

Mandatory texts for Italian websites, webshops, apps and newsletters. The governing instruments are D.Lgs 70/2003 (e-commerce), the Codice Civile, DPR 633/1972 (VAT), the Codice Privacy D.Lgs 196/2003 as amended by D.Lgs 101/2018, the Garante's binding provvedimenti, the Codice del Consumo D.Lgs 206/2005 as amended by D.Lgs 26/2023, 170/2021, 173/2021, 209/2025 and 30/2026, Legge 4/2004 and D.Lgs 82/2022 for accessibility, and the directly applicable GDPR and DSA. Explanations here are in English; every template text is in Italian, because that is the language it must be published in.

**Core principle.** Italy stacks *identification and formality* duties on top of the EU baseline that no other member state imposes in the same shape. The **partita IVA must appear on the home page itself** (art. 35 comma 1 DPR 633/1972), the **REA number is owed by every provider including a sole trader** (art. 7 lett. d D.Lgs 70/2003), companies must hold a **domicilio digitale registered in INI-PEC** and, since 31.12.2025, so must their **amministratore unico or delegato, with a different PEC from the company's** (art. 5 comma 1 D.L. 179/2012), online retail of goods still needs a **SCIA to the comune's SUAP** (art. 68 comma 1 D.Lgs 59/2010), the Garante's **cookie guidelines of 10.06.2021** are more prescriptive than the EDPB's, and the **age of digital consent is 14** (art. 2-quinquies Codice Privacy). A generic EU template satisfies none of these.

## Not legal advice

This skill produces drafts and findings, not legal advice. Before go-live:

- Webshop, subscription, payment processing, children's data, health data or platform operation: **obtain sign-off from an Italian lawyer.**
- First-line help without cost: the **Garante per la protezione dei dati personali** (garanteprivacy.it, Piazza Venezia n. 11, 00187 Roma, protocollo@gpdp.it) for data protection questions; **AGCM** (agcm.it) for consumer practices; **AGCOM** (agcom.it) as Digital Services Coordinator; the local **Camera di Commercio** for registro delle imprese, REA and SCIA questions; **AgID** (agid.gov.it) for accessibility.
- Every generated text carries a visible `<!-- BOZZA – non approvata legalmente -->` HTML comment until a lawyer has signed off. Never remove the marker silently.

Never omit this section from an output and never soften it.

## Workflow

1. **Take intake before any text exists.** Without the answers every text is guesswork. Questions in `references/intake.md`.
2. **Determine the obligation matrix** below: which texts this specific project actually needs.
3. **Read the reference file for each obligation before drafting.** Never from memory — the article numbers and the dated cut-overs are too specific.
4. **Run `references/checklist.md`**, reporting each finding with its article.
5. Output the approval notice, leave the draft marker in place.

**Output shape.** Exactly four parts, in this order:

1. the legal text or the finding itself, carrying the draft marker
2. the list of `[[MISSING: …]]` items the user must supply
3. adjacent open obligations in the same project, one sentence each
4. the approval notice

The norm sits directly next to the statement it supports. Reference file names and paths belong in none of the four parts — they are working material, not part of the delivery.

## Obligation matrix

| Situation | Required texts, with the norm | Reference |
|---|---|---|
| Any website run for economic purposes | Informazioni sul sito (art. 7 D.Lgs 70/2003), partita IVA on the home page (art. 35 DPR 633/1972) | `identificazione-sito.md` |
| S.p.A., S.a.p.a. or S.r.l. with a website | Additionally sede, registro imprese, capitale versato, socio unico, liquidazione (art. 2250 comma 7 c.c.) | `identificazione-sito.md` |
| Any processing of personal data, even server logs | Informativa (Artt. 13/14 GDPR) plus the Codice Privacy deviations | `informativa-privacy.md` |
| Non-technical cookies, analytics, pixels, embeds, third-party fonts | Consent banner and cookie policy (art. 122 Codice Privacy; Garante provv. 231/2021) | `cookie-tracker.md` |
| Email open tracking | Separate consent and granular opt-out (Garante provv. 284/2026, deadline 29.10.2026) | `cookie-tracker.md` |
| Selling to consumers online | Pre-contractual information (art. 49), order button wording (art. 51 comma 2), condizioni generali di vendita | `vendita-online.md` |
| Selling to consumers online | Withdrawal information, modulo tipo (Allegato I parte B) and the **online withdrawal function** (art. 54-bis) | `recesso.md` |
| Selling goods, digital content or digital services | Garanzia legale di conformità (artt. 128 ff / 135-octies ff) | `garanzia-conformita.md` |
| Newsletter, SMS or telephone marketing | Consent, soft-spam conditions, RPO checks (art. 130 Codice Privacy) | `marketing-diretto.md` |
| Influencer, affiliate or sponsored content | Disclosure per the Digital Chart; AGCOM regime above the thresholds | `influencer-pubblicita.md` |
| B2C digital service, not a microenterprise | Accessibility conformity and declaration (D.Lgs 82/2022; L. 4/2004) | `accessibilita.md` |
| Hosting, forum, comments, reviews, marketplace | DSA contact point, notice and action, statement of reasons | `piattaforme-dsa.md` |
| Any consumer contract | ADR position stated honestly; **no ODR reference** | `risoluzione-controversie.md` |
| Personal data in any form | Registro dei trattamenti, Art 28 contracts, breach process, employee monitoring under art. 4 L. 300/1970 | `privacy-interna.md` |

## Hard rules

- **The ODR platform is dead.** Regulation (EU) 2024/3228 shut it down; operation ended 20 July 2025. A link to it is a dead link presented as a consumer right. Found in an existing text, it is removed, not rewritten, and never re-added, whatever a shop template says.
- **Artt. 14 to 17 D.Lgs 70/2003 are abrogated.** D.Lgs 25 marzo 2024 n. 50 repealed the Italian mere-conduit, caching, hosting and no-general-monitoring articles with effect from 2 May 2024. Intermediary liability is now artt. 4 to 8 of Regulation (EU) 2022/2065 directly. Any text citing "art. 16 D.Lgs 70/2003" for hosting is citing a repealed provision.
- **The online withdrawal function is mandatory.** Art. 54-bis Codice del Consumo, inserted by D.Lgs 209/2025, applies to distance contracts concluded through an online interface from 19 June 2026. The control reads *recedere dal contratto qui*, the confirmation reads *conferma recesso*, and receipt must be acknowledged on a durable medium with the content, date and time of transmission.
- **The order button must carry only the payment wording.** Art. 51 comma 2 requires *soltanto le parole «ordine con obbligo di pagare»* or an unambiguous equivalent. The sanction is not a fine: *il consumatore non è vincolato dal contratto o dall'ordine*.
- **Burden of proof reverses for one year, not six months.** Art. 135 comma 1 Codice del Consumo, as replaced by D.Lgs 170/2021. Six months is repealed law. The two-month *denuncia* was abolished by the same decree — a template that still contains it is pre-2022.
- **Consent age is 14.** Art. 2-quinquies Codice Privacy. Below 14 the consent must be given by the holder of parental responsibility. Never write 16 for an Italian service.
- **No tracker before consent, and the X is the requirement.** The Garante's linee guida (provv. 231 del 10.06.2021) require an X inside the banner, top right, with graphic prominence equal to the accept command, all granular options preset to refusal, and no re-prompting for at least six months after a recorded choice.
- **Informativa is not consenso.** The Art 13 notice is owed for every processing whatever the basis. Consent is one basis among six and the weakest. Never attach consent to order handling, invoicing or logs — Italian templates do this routinely and it makes the processing more fragile, not safer.
- **Never invent identifying data.** Partita IVA, codice fiscale, REA number, registro delle imprese office, capitale sociale, PEC, supervisory authority, registered office: if unknown it becomes `[[MISSING: numero REA]]` in the text and in the report back to the user.
- **A geographic address, never a PO box.** Art. 7 lett. b D.Lgs 70/2003 requires the *domicilio o sede legale*. For a sole trader without business premises that is the home address — if the user does not want that published, it is a business decision (registered office service, coworking address), not a drafting question. Raise it immediately instead of working around it.

## False friends

Imported assumptions that look plausible and are wrong. If one is asserted, strike it and substitute the Italian position, where one exists.

| Imported assumption | Position in Italy |
|---|---|
| § 5 TMG / § 5 DDG *Impressum* | Art. 7 D.Lgs 70/2003, plus art. 2250 c.c. for S.p.A./S.r.l. and art. 35 DPR 633/1972 for the partita IVA on the home page |
| *Widerrufsrecht*, *Widerrufsbelehrung* | **Recesso**, informativa sul recesso. Only the annexed form is a *modulo*, because the annex comes from the directive |
| Kündigungsbutton under § 312k BGB | Does not exist. What exists is the **funzione di recesso** under art. 54-bis Codice del Consumo, which is about exercising withdrawal, not terminating a continuing contract |
| BDSG, works-council thresholds by headcount | Codice Privacy D.Lgs 196/2003; employee monitoring runs through **art. 4 L. 300/1970**, with an accordo sindacale or Ispettorato nazionale del lavoro authorisation |
| Age of consent 16 | **14**, art. 2-quinquies Codice Privacy |
| Amtsgericht, Handelsregister, HRB | Tribunale, **Registro delle imprese**, numero **REA** |
| USt-IdNr. under § 27a UStG | **Partita IVA**, format IT + 11 digits, and it must be on the **home page** |
| Six-month reversal of the burden of proof | **One year**, art. 135 comma 1 Codice del Consumo |
| "Notify the defect within two months" | Abolished by D.Lgs 170/2021 |
| Generic-EU template citing Directive 2011/83/EU or 2019/771 | Cite the **Codice del Consumo articles**. Italian authorities enforce the transposition, not the directive |
| "Reject all button" as the Italian banner rule | The Italian rule is the **X**, top right, inside the banner, of equal graphic prominence. A reject button is good practice, not the literal requirement |
| Link to the EU ODR platform | Shut down 20 July 2025 |
| D.Lgs 145/2007 as the consumer advertising law | It protects **professionisti** (B2B). B2C unfair practices are artt. 18-27 Codice del Consumo |
| "In collaborazione con" / "#suppliedby" as influencer disclosure | Not in the Digital Chart of 30 ottobre 2024. Use *pubblicità*, *advertising*, *sponsorizzato da …*, or *prodotto inviato da …* |

If an obligation comes to mind that cannot be traced to a specific Italian norm, it is reported as an open question, not asserted.

## Common mistakes

| Mistake | Why it is wrong |
|---|---|
| Partita IVA only on the legal-information page | Art. 35 comma 1 DPR 633/1972 says *nella home-page* |
| Art. 2250 c.c. data claimed for an s.n.c. or a sole trader | Comma 7 binds only S.p.A., S.a.p.a. and S.r.l. |
| "Questo sito usa i cookie. OK" | No consent under art. 122; no X, no granularity, no reject of equal weight |
| Banner shown on every visit | Prohibited for at least six months after a recorded choice |
| Consent box for order processing | Art 6(1)(b) GDPR applies; a consent that blocks the order is not free |
| "Garanzia 12 mesi" on new goods | Two years under art. 133; any pre-notification limitation is null under art. 135-sexies |
| Paid extended warranty promoted without the free legal guarantee | The AGCM Apple precedent, PS7256, EUR 900,000 plus EUR 200,000 |
| "Solo se non aperto", "esclusi i saldi" as withdrawal exclusions | Art. 59 is a closed list; invented restrictions are unenforceable |
| Withdrawal instructions without the Allegato I parte B form | It is a mandatory component under art. 49 comma 1 lett. h |
| Discount claim without a 30-day price history | Art. 17-bis comma 2 defines the previous price as the lowest in the last 30 days |
| Reviews displayed with no statement about verification | Art. 22 comma 5-bis; unverified claims are always misleading under art. 23 comma 1 lett. bb-ter |
| Soft spam by SMS or to a postal-only customer | Art. 130 comma 4 covers *coordinate di posta elettronica* only |
| Telephone list scrubbed against the RPO once a quarter | The duty is monthly and again before each campaign |
| Accessibility ignored because turnover is under EUR 500 million | That threshold is Legge Stanca. The EAA regime under D.Lgs 82/2022 has no turnover threshold |
| Images used without a licence record | The record belongs in the project, not in the legal text |

## Reference files

Each contains the article numbers with a status date, the mandatory content, a template with `[[PLACEHOLDER]]` slots, and a checkpoint list.

- `references/intake.md` — questions to answer before the first text
- `references/identificazione-sito.md` — art. 7 D.Lgs 70/2003, art. 2250 c.c., art. 35 DPR 633/1972, PEC and INI-PEC, SCIA, sanctions
- `references/informativa-privacy.md` — Artt. 13/14 GDPR, Codice Privacy deviations, age 14, the informativa/consenso distinction
- `references/privacy-interna.md` — registro dei trattamenti, designations, DPO notification, breach, art. 4 L. 300/1970, email metadata
- `references/cookie-tracker.md` — art. 122, Garante provv. 231/2021, tracking pixels provv. 284/2026, Google Analytics, enforcement
- `references/vendita-online.md` — artt. 49 and 51, price reductions, reviews, marketplaces, sanctions, condizioni generali di vendita
- `references/recesso.md` — artt. 52 to 59, art. 54-bis withdrawal function, Allegato I parte B verbatim
- `references/garanzia-conformita.md` — artt. 128 ff and 135-octies ff, two years, one-year reversal, updates, commercial guarantee
- `references/marketing-diretto.md` — art. 130 verbatim, soft spam conditions, RPO, double opt-in, telemarketing code
- `references/influencer-pubblicita.md` — AGCOM delibere 7/24/CONS and 197/25/CONS, AGCM, IAP Digital Chart 2024
- `references/accessibilita.md` — Legge Stanca and the EUR 500 million threshold, EAA D.Lgs 82/2022, declaration
- `references/piattaforme-dsa.md` — DSA categories, AGCOM as Digital Services Coordinator, the abrogation of artt. 14-17 D.Lgs 70/2003
- `references/risoluzione-controversie.md` — artt. 141 to 141-decies, ADR registers, ODR removal, consumer forum
- `references/checklist.md` — pre-launch checklist mapped to articles

If the legal-eu skill is installed, read it for the EU-level baseline; this skill covers the national layer on top of it.
