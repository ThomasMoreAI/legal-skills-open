---
name: legal-ch-clemensjl
title: Swiss online legal texts
description: Use when writing, reviewing, or fixing legally required texts for a Swiss website, webshop, app, or newsletter — Impressum, Datenschutzerklärung, cookie notice, AGB, warranty and return terms, price display, accessibility statement — or when asked whether a Swiss online presence is legally compliant. Also use when a German, Austrian, or EU legal template is about to be reused for Switzerland, when personal data processing starts, or before a site goes live.
author: clemensjl
author_url: https://github.com/clemensjl/claude-skills/tree/main/skills/legal-ch
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: ch
practice: data-protection
language: en
sources:
- title: Agb Vertragsschluss
  path: references/agb-vertragsschluss.md
- title: Auslandsbezug Dsg
  path: references/auslandsbezug-dsg.md
- title: Barrierefreiheit
  path: references/barrierefreiheit.md
- title: Checklist
  path: references/checklist.md
- title: Cookies Tracking
  path: references/cookies-tracking.md
- title: Datenschutzerklaerung
  path: references/datenschutzerklaerung.md
- title: Dsg Intern
  path: references/dsg-intern.md
- title: Eu Crossborder
  path: references/eu-crossborder.md
- title: Gewaehrleistung Widerruf
  path: references/gewaehrleistung-widerruf.md
- title: Impressum
  path: references/impressum.md
- title: Intake
  path: references/intake.md
- title: Marketing
  path: references/marketing.md
- title: Plattform Streitbeilegung
  path: references/plattform-streitbeilegung.md
- title: Preisbekanntgabe
  path: references/preisbekanntgabe.md
---

# Swiss online legal texts

Mandatory texts for Swiss websites, webshops, apps and newsletters. The governing acts are UWG (Bundesgesetz gegen den unlauteren Wettbewerb, the unfair competition act, SR 241), DSG (Datenschutzgesetz, the data protection act, SR 235.1) with DSV (Datenschutzverordnung, SR 235.11), OR (Obligationenrecht, the code of obligations, SR 220), FMG (Fernmeldegesetz, the telecommunications act, SR 784.10), PBV (Preisbekanntgabeverordnung, the price disclosure ordinance, SR 942.211) and BehiG (Behindertengleichstellungsgesetz, the disability equality act, SR 151.3).

Switzerland is multilingual. Every text below must exist in the language in which the customer is actually addressed — German, French or Italian. A German-only Impressum on a French-language shop does not discharge the duty. The templates in this skill are German; translate rather than transplant.

**Core principle.** Switzerland is not in the EU and its consumer law is genuinely seller-friendly, which is exactly where imported templates do damage. There is **no general right of withdrawal for online purchases** — Art. 40a–40f OR cover doorstep, workplace, street, promotional-excursion and telephone sales, not e-commerce. Warranty can be excluded by agreement under Art. 199 OR. There is **no cookie consent requirement**; Art. 45c lit. b FMG imposes an information duty with a refusal option. Two things run the other way and get missed: the Impressum duty sits in an unfair-competition provision, **Art. 3 Abs. 1 lit. s UWG**, breach of which is a criminal offence on complaint under Art. 23 UWG; and DSG penalties are **criminal fines of up to CHF 250,000 against natural persons** (Art. 60–63 DSG), not administrative fines against companies. The revised DSG applies *alongside* the GDPR, not instead of it, wherever Art. 3(2) GDPR reaches the business.

## Not legal advice

This skill produces drafts and findings, not legal advice. Before go-live:

- Webshop, subscription, payment processing, children's data, health data or platform operation: **obtain sign-off from a Swiss lawyer.**
- Free first-line help: EDÖB (edoeb.admin.ch) for data protection interpretation questions; SECO (seco.admin.ch) and the cantonal enforcement bodies for price disclosure; Schweizerische Lauterkeitskommission (faire-werbung.ch) for advertising complaints; Stiftung für Konsumentenschutz (konsumentenschutz.ch), FRC (frc.ch), ACSI (acsi.ch) for consumer-side questions; the cantonal bar associations via sav-fsa.ch for lawyer referral.
- Every generated text carries a visible marker `<!-- ENTWURF – juristisch nicht freigegeben -->` as an HTML comment until legal sign-off is confirmed. Never remove the marker silently. For French use `<!-- BROUILLON – non validé juridiquement -->`, for Italian `<!-- BOZZA – non approvata legalmente -->`.

Never omit or soften this section in output.

## Workflow

1. **Take the facts first.** Without answers no text is anything but guesswork. Questions in `references/intake.md`.
2. **Determine the obligation matrix** (below): which texts this specific project actually needs.
3. **Read the reference file for each obligation, then draft.** Never from memory — the article numbers are too specific.
4. **Run `references/checklist.md`** and report findings with the article and the location.
5. Emit the sign-off notice, leave the draft marker in place.

**Output shape.** Exactly four parts, in this order:

1. the legal text or finding itself, with the draft marker
2. the list of `[[MISSING: …]]` items the user must supply
3. adjacent open obligations in the same project, one sentence each
4. the sign-off notice

The norm sits next to the statement it belongs to. Reference-file names and paths belong in none of the four parts — they are working material, not deliverable.

## Obligation matrix

| Situation | Required texts, with the norm | Reference |
|---|---|---|
| Any site offering goods, works or services in electronic commerce | Impressum: identity and contact address including email (Art. 3 Abs. 1 lit. s Ziff. 1 UWG); company details for registered entities (Art. 954a OR) | `impressum.md` |
| Any processing of personal data, including server logs and contact forms | Datenschutzerklärung (Art. 19 DSG) | `datenschutzerklaerung.md` |
| Any processing of personal data | Register of processing activities, processor contracts, security, breach process (Art. 12, 8, 9, 24 DSG) — internal, not published | `dsg-intern.md` |
| Controller abroad processing Swiss data, or Swiss controller targeting the EU | Swiss representative (Art. 14 DSG) or EU representative (Art. 27 GDPR); transfer basis (Art. 16/17 DSG) | `auslandsbezug-dsg.md` |
| Non-essential cookies, analytics, pixels, embeds, fonts from third-party servers | Cookie information plus refusal option (Art. 45c lit. b FMG); explicit consent where processing is high-intensity (Art. 6 Abs. 7 DSG) | `cookies-tracking.md` |
| Online ordering process | Steps to contract, input-error correction, immediate order confirmation (Art. 3 Abs. 1 lit. s Ziff. 2–4 UWG); AGB | `agb-vertragsschluss.md` |
| Sale of goods or digital products | Warranty terms (Art. 197 ff. OR), guarantee if offered, return policy if granted voluntarily | `gewaehrleistung-widerruf.md` |
| Any price shown to consumers | Actual price payable in CHF including VAT and non-optional surcharges (Art. 3, 4 PBV) | `preisbekanntgabe.md` |
| Newsletter, email or SMS advertising, cold calling | Opt-in, correct sender, free refusal option (Art. 3 Abs. 1 lit. o UWG); directory marker (lit. u, v) | `marketing.md` |
| Public-sector, concession-holding or federally mandated services | Accessibility per Art. 14 Abs. 2 BehiG, Art. 10 BehiV, eCH-0059 | `barrierefreiheit.md` |
| Hosting, forum, comments, marketplace, UGC | No Swiss DSA equivalent; contractual moderation rules and Art. 28 ZGB / Art. 3 UWG exposure | `plattform-streitbeilegung.md` |
| Consumer sale | Conciliation before court (Art. 197 ZPO); no ODR link, ever | `plattform-streitbeilegung.md` |
| Shipping to or targeting EU customers | GDPR, EAA, GPSR responsible person, CRD withdrawal right in parallel | `eu-crossborder.md` |

## Hard rules

- **No general right of withdrawal for online orders.** Art. 40b OR lists the covered situations exhaustively: offers at the workplace or in living quarters, in public transport or on public streets and squares, at a promotional event tied to an excursion, and by telephone or comparable simultaneous oral telecommunication. E-commerce is not among them, and Art. 40a Abs. 1 lit. b OR sets a CHF 100 floor. If a shop grants returns anyway, label it a **voluntary return policy**, never a statutory right and never "Widerrufsrecht".
- **The Impressum duty is criminal.** Art. 3 Abs. 1 lit. s Ziff. 1 UWG requires clear and complete information about identity and contact address including email. Intentional breach is punishable on complaint with custodial sentence up to three years or a monetary penalty (Art. 23 Abs. 1 UWG). Never present it as a formality.
- **No cookie consent banner is required by Swiss law.** Art. 45c lit. b FMG requires that users be informed about the processing and its purpose and told they can refuse it. A prior explicit opt-in is required only where the processing involves besonders schützenswerte Personendaten or Profiling mit hohem Risiko (Art. 6 Abs. 7 DSG). Do not import ePrivacy consent logic as if it were Swiss law, and do not claim Swiss law forbids a banner either.
- **DSG fines hit individuals, not companies.** Art. 60–63 DSG punish *private Personen* with a fine of up to CHF 250,000, mostly on complaint. Only where a fine of at most CHF 50,000 is in play and identifying the responsible individual would be disproportionate may the business be fined instead (Art. 64 Abs. 2 DSG in conjunction with Art. 7 VStrR). Never describe DSG sanctions as GDPR-style percentage-of-turnover corporate fines.
- **State both halves of the warranty rule or neither.** Art. 199 OR permits exclusion or restriction of warranty by agreement, void only where the seller fraudulently concealed the defect. Art. 210 Abs. 4 OR separately makes it invalid to shorten the limitation period below two years, or below one year for used goods, where the item is for the buyer's personal or family use and the seller acts professionally. A blanket exclusion in consumer AGB remains exposed to Art. 8 UWG.
- **Never invent company data.** Handelsregister entry, UID/CHE number, MWST number, legal form, registered office, representative bodies: if unknown it becomes `[[MISSING: UID/CHE number]]` in the text and in the report back to the user.
- **No German or Austrian provisions.** If a text contains § 5 TMG or § 5 DDG, § 55 RStV, BDSG, "Widerrufsbelehrung", "Kündigungsbutton nach § 312k BGB", "Amtsgericht", ECG, FAGG or "Rücktrittsrecht nach FAGG", it came from a foreign template and is rewritten in full, not patched.
- **Delete every ODR link.** Regulation (EU) No 524/2013 was repealed with effect from 20 July 2025 by Regulation (EU) 2024/3228, and the platform never covered Switzerland in the first place. A link to it is a dead link and a potentially misleading commercial statement. Remove without replacement; point to the cantonal Schlichtungsbehörde instead.
- **Prices are gross, in Swiss francs, and complete.** Art. 3 Abs. 1 PBV requires the actual price payable in Swiss francs. Art. 4 Abs. 1 PBV requires passed-on public levies, copyright levies, advance disposal fees and all further non-optional surcharges of any kind — reservation, service, processing — to be included; shipping costs may be shown separately. Crossed-out comparison prices require Art. 16 PBV compliance.
- **The GDPR applies in parallel when Art. 3(2) GDPR is met.** Offering goods or services to people in the EU, or monitoring their behaviour there, triggers the GDPR regardless of Swiss law. Then a genuine consent banner, an Art. 27 GDPR representative and GDPR-standard information duties apply on top of the DSG.

## False friends

| Imported assumption | Position in Switzerland |
|---|---|
| § 5 TMG / § 5 DDG Impressum (Germany) | Art. 3 Abs. 1 lit. s Ziff. 1 UWG, an unfair-competition provision; plus Art. 954a OR for registered entities |
| § 5 ECG, §§ 24/25 MedienG Offenlegung (Austria) | No media-law disclosure duty exists. There is no Swiss Offenlegung, no Blattlinie, no Medieninhaber |
| Widerrufsrecht / Rücktrittsrecht of 14 days for online orders (DE/AT/EU) | Does not exist. Art. 40b OR does not cover e-commerce. Voluntary return policies only |
| Kündigungsbutton § 312k BGB, Widerrufsbutton § 13a FAGG | No Swiss equivalent of either |
| Cookie consent under Art. 5(3) ePrivacy Directive | Art. 45c lit. b FMG: information plus refusal option. Explicit consent only under Art. 6 Abs. 7 DSG |
| GDPR fines up to 4 % of global turnover | Criminal fines up to CHF 250,000 against natural persons, Art. 60–63 DSG |
| Breach notification within 72 hours (Art. 33 GDPR) | "So rasch als möglich" and only where high risk is likely, Art. 24 Abs. 1 DSG |
| DPO mandatory above a headcount threshold (BDSG § 38) | Art. 10 DSG Datenschutzberater is voluntary for private controllers; appointing one unlocks the Art. 23 Abs. 4 DSG consultation exemption |
| Register of processing exempt below 250 employees (Art. 30(5) GDPR) | Art. 24 DSV: exempt below 250 employees *unless* besonders schützenswerte Personendaten are processed at large scale or high-risk profiling is carried out |
| EU accessibility duty for private e-commerce (EAA) | BehiG binds authorities and concession holders; private providers only owe non-discrimination under Art. 6 BehiG, remedy capped at CHF 5,000 (Art. 11 Abs. 2 BehiG) |
| DSA notice-and-action, trusted flaggers, statement of reasons | No DSA equivalent in Swiss law as at 2026-08-05 |
| Link to the EU ODR platform | Never applied to Switzerland; platform shut down 20 July 2025. Delete |
| Handelsregister HRB, Amtsgericht, USt-IdNr. | Handelsregister with UID in the format CHE-###.###.###, cantonal courts, MWST number |

If a duty comes to mind that cannot be traced to a concrete Swiss provision, it is reported as an open question, not asserted.

## Common mistakes

| Mistake | Why it is wrong |
|---|---|
| "14 Tage Widerrufsrecht" in a Swiss shop's terms | Asserts a statutory right that does not exist; also misleading under Art. 3 Abs. 1 lit. b UWG |
| Cookie banner with only an "OK" button | Art. 45c lit. b FMG requires a refusal option, not just an acknowledgement |
| Blocking the whole site behind a consent wall | Impressum and Datenschutzerklärung must be reachable without consent and without login |
| Datenschutzerklärung copied from a German template | Names the wrong authority, wrong articles, wrong legal bases; Art. 19 Abs. 4 DSG requires the recipient state and the safeguard, which Art. 13 GDPR does not |
| Prices excluding VAT on a consumer-facing page | Art. 3, 4 PBV; criminal under Art. 24 Abs. 1 lit. a UWG, fine up to CHF 20,000 |
| "Statt CHF 199" without a qualifying reference period | Art. 16 Abs. 1 lit. a PBV: the comparison price must have applied immediately before, or for at least 30 consecutive days |
| Newsletter sent to purchased address lists | Art. 3 Abs. 1 lit. o UWG requires prior consent outside the existing-customer exception |
| Guarantee described as if it replaced warranty | Garantie is voluntary and additional; Art. 197 ff. OR applies independently unless validly excluded |
| Warranty shortened to one year for new consumer goods | Art. 210 Abs. 4 OR invalidates the shortening |
| Assuming the DSG is "GDPR-lite" and one text covers both | Different information duties, different penalties, different transfer regime; where both apply, the stricter obligation governs each point |

## Reference files

Each contains the article numbers with status date, the mandatory content points, a template with `[[PLACEHOLDER]]` slots, and a checkpoint list.

- `references/intake.md` — questions to answer before the first text
- `references/impressum.md` — Art. 3 Abs. 1 lit. s UWG, Art. 954a/931 OR, UID, MWST number
- `references/datenschutzerklaerung.md` — Art. 19–21 DSG, German template, GDPR delta
- `references/dsg-intern.md` — register, security, processors, DSFA, breach notification, criminal liability
- `references/auslandsbezug-dsg.md` — Art. 14 DSG representative, Art. 27 GDPR representative, Art. 16/17 DSG transfers, adequacy list, Swiss-US DPF
- `references/cookies-tracking.md` — Art. 45c FMG, EDÖB Leitfaden, when opt-in becomes mandatory
- `references/agb-vertragsschluss.md` — Art. 1–10 OR, Art. 3 Abs. 1 lit. s Ziff. 2–4 UWG, Art. 8 UWG, Ungewöhnlichkeitsregel, Art. 3a UWG geoblocking
- `references/gewaehrleistung-widerruf.md` — Art. 197–210 OR, Garantie, Art. 40a–40f OR and its real scope
- `references/preisbekanntgabe.md` — PBV, Art. 16–18 and 24 UWG, comparison prices
- `references/marketing.md` — Art. 3 Abs. 1 lit. o, u, v, w, x UWG, Art. 45a FMG, Sterneintrag
- `references/barrierefreiheit.md` — BehiG, BehiV, eCH-0059, and the EAA trap for EU-facing shops
- `references/plattform-streitbeilegung.md` — absence of a DSA, moderation, ZPO conciliation, ombudsman bodies, ODR deletion
- `references/eu-crossborder.md` — GDPR, EAA, GPSR, CRD withdrawal right, Rome I and Lugano
- `references/checklist.md` — pre-launch checklist mapped to articles
