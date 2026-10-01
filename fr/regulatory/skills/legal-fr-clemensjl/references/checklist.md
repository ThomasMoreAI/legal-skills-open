# Pre-launch checklist

Work through before going live. Every finding is reported with its article and its location, not as a general remark. Anything that can be tested technically is tested, not judged from intent.

## Technical pass first

These four steps produce half the findings and take minutes:

1. Load the site in a fresh browser profile with the network tab recording. List every third-party domain contacted **before** any consent decision.
2. Application tab: capture every cookie, localStorage and IndexedDB entry present before the decision.
3. Full-text search across the whole project — including shop system strings, PDF invoices, transactional email templates and plugin defaults — for: `odr`, `ec.europa.eu/consumers`, `règlement en ligne des litiges`, `RLL`, `article 6-III`, `article 6-I`, `TMG`, `DDG`, `Impressum`, `Widerruf`, `BDSG`, `Amtsgericht`, `Handelsregister`.
4. Run the ordering flow and the cancellation flow once with the keyboard only, no mouse.

## Mentions légales

- [ ] One click from every page, labelled « Mentions légales », no login and no consent gate
- [ ] Name or denomination, siège social, telephone number, email (art. 1-1 I LCEN)
- [ ] SIREN or RNE registration number where the trader is registered (art. 1-1 I 1° et 2°)
- [ ] Capital social for companies (art. 1-1 I 2°)
- [ ] Directeur de la publication named (art. 1-1 I 3°)
- [ ] **Hébergeur** with denomination, address and telephone (art. 1-1 I 4°)
- [ ] Third-party data storage providers named where applicable (art. 1-1 I 5°)
- [ ] « RCS » plus the city of the greffe, and the R123-237 items, on the site (C. com. art. R123-237)
- [ ] TVA intracommunautaire number where VAT-registered
- [ ] Regulated activity: title, ordre, applicable rules with access, insurance (C. conso art. L111-2)
- [ ] No citation of article 6-III LCEN, § 5 TMG, § 5 DDG or § 5 ECG

## Données personnelles

- [ ] Privacy policy reachable without consent and without login
- [ ] Purpose, legal basis, recipients and retention stated per processing (RGPD art. 13)
- [ ] Legitimate interests named concretely
- [ ] Every service actually loaded appears in the policy, checked against the network capture
- [ ] Third-country transfers listed individually with the safeguard
- [ ] Directives post mortem mentioned (art. 85 loi 78-17)
- [ ] Consent age handled as 15 with joint consent below (art. 45 loi 78-17)
- [ ] CNIL named as supervisory authority with the correct address
- [ ] Register, processor contracts, security measures and breach procedure exist internally

## Cookies et traceurs

- [ ] No non-exempt request and no non-exempt storage before a decision (art. 82 loi 78-17)
- [ ] « Tout refuser » on the first layer, equally prominent as « Tout accepter »
- [ ] Purposes on the first layer, granular choice, no pre-ticked categories
- [ ] Closing the banner is not treated as acceptance
- [ ] Withdrawal control permanently in the footer
- [ ] Cookie table matches the network capture
- [ ] Consent log records timestamp, purposes, banner version and mechanism
- [ ] Fonts local or behind consent; maps, video and captcha behind consent or click-to-load
- [ ] Any tracker claimed exempt meets all CNIL audience-measurement criteria, including 13 and 25 months

## Boutique et vente à distance

- [ ] Order button reads « commande avec obligation de paiement » or an unambiguous equivalent (art. L221-14)
- [ ] Order summary immediately above the button, with a route back to correct
- [ ] Means of payment and delivery restrictions shown at the latest at the start of the ordering process
- [ ] Prices TTC, delivery costs separate and shown before validation
- [ ] All six items of article L111-1 present, including the médiateur
- [ ] Delivery date or period stated concretely
- [ ] No pre-ticked optional extras
- [ ] Order confirmation on a durable medium
- [ ] Discount claims backed by the lowest price of the preceding 30 days
- [ ] Indice de réparabilité or de durabilité, spare-parts availability, Triman and info-tri where applicable
- [ ] CGV and CGU are separate documents with separate content

## Rétractation

- [ ] The word « rétractation » is used, never « Widerruf » or « rétraction »
- [ ] Fourteen days with the correct starting point per contract type (art. L221-18)
- [ ] Model form from the annexe à l'article R221-1 supplied, saveable and printable
- [ ] Trader's postal address, email and telephone in the notice
- [ ] Return costs stated where the consumer bears them
- [ ] Refund within fourteen days, same means of payment
- [ ] Exceptions listed only where they genuinely apply (art. L221-28), no invented restrictions
- [ ] Immediate digital content: two separate, non-pre-ticked declarations, stored with a timestamp
- [ ] **Fonctionnalité de rétractation built** (art. L221-21 al. 3, in force 19.06.2026): free, permanently and directly accessible on the online interface
- [ ] Control labelled « renoncer au contrat ici », displayed visibly (art. D221-5)
- [ ] Declaration collects nom et prénom, details identifying the contract, and the electronic means for the reply
- [ ] Separate confirmation control labelled « confirmer la rétractation »
- [ ] Accusé de réception on a durable medium within a reasonable time, stating the content of the declaration and the **date and heure** it was sent

## Garanties

- [ ] Two years for new goods, twelve-month presumption for second-hand (art. L217-3, L217-7)
- [ ] Six-month extension after repair stated (art. L217-13)
- [ ] New guarantee period after replacement following a failed repair stated
- [ ] Thirty-day limit for restoring conformity stated (art. L217-10)
- [ ] Vices cachés mentioned with the two-year limit from discovery (C. civ. art. 1648)
- [ ] Commercial guarantee, if any, described as additional and not substitutive
- [ ] Warranty end dates in support tooling reflect the +6 months

## Résiliation

- [ ] Entry point « résilier votre contrat » or an unambiguous equivalent (art. D215-1)
- [ ] Direct, easy and permanent access from the online interface
- [ ] Available even for contracts concluded offline, if electronic conclusion is offered today
- [ ] D215-2 fields present, including the desired cancellation date
- [ ] Summary page with correction, then « notification de la résiliation » (art. D215-3)
- [ ] Acknowledgement plus end date and effects on a durable medium (art. L215-1-1)
- [ ] Tacit-renewal reminder between three months and one month before the deadline (art. L215-1)

## Médiation

- [ ] A CECMC-referenced médiateur is actually contracted
- [ ] Name, postal address and website in the CGV and reachable from the mentions légales
- [ ] Prior written complaint step and the one-year limit explained
- [ ] **No ODR link anywhere**, including invoices, transactional emails and plugin defaults

## Marketing

- [ ] Separate, non-pre-ticked marketing consent, distinct from CGV acceptance
- [ ] Double opt-in active, confirmation email free of advertising
- [ ] Consent record with timestamp, IP and form text version
- [ ] One-click unsubscribe in every message, no login
- [ ] Sender identity and valid reply address, no misleading subject line (art. L34-5 CPCE)
- [ ] Existing-customer exception used only for similar products of the same trader
- [ ] Influencer and affiliate content carries « Publicité » or « Collaboration commerciale »
- [ ] « Images retouchées » and « Images virtuelles » where applicable
- [ ] Written contract with every paid influencer above the décret threshold

## Accessibilité

- [ ] Applicability of article 47 loi 2005-102 and of article L412-13 C. conso both assessed and recorded
- [ ] Microenterprise status documented where relied on
- [ ] Home page carries one of the three exact conformity mentions
- [ ] Déclaration d'accessibilité, schéma pluriannuel and annual action plan published
- [ ] RGAA 4.1.2 audit dated, conformity rate stated honestly
- [ ] Keyboard pass succeeds, focus visible, contrasts measured, labels associated

## Plateforme

- [ ] DSA classification recorded
- [ ] Point of contact published with accepted languages; EU representative if established outside the EU
- [ ] Notice and action mechanism live; statements of reasons issued on restriction
- [ ] Moderation rules disclosed in the CGU
- [ ] Marketplace: trader traceability collected before listing
- [ ] Adult content: ARCOM age-verification référentiel addressed

## Cross-cutting

- [ ] No German or Austrian provisions and no German authorities anywhere in the text
- [ ] No directive cited where a Code de la consommation article binds
- [ ] Image rights and licences documented
- [ ] Third-party marks and logos used only with authorisation
- [ ] Every `[[…]]` placeholder resolved or explicitly reported as open
- [ ] Draft marker `<!-- BROUILLON – non validé juridiquement -->` still present while legal sign-off is outstanding

## Result format

Report findings as a table, most severe first:

| Severity | Location | Norm | Finding | Fix |
|---|---|---|---|---|
| critique / élevé / moyen | file:line or URL | article | what is missing or wrong | concrete step |

**Critique** means criminal exposure, an administrative fine, or an unenforceable contract. That covers missing mentions légales (art. 1-2 LCEN, one year and 75 000 €), tracking before consent (art. 82 loi 78-17), a wrongly labelled order button (art. L221-14, à peine de nullité), a missing withdrawal notice, no named médiateur (art. L641-1), and a missing electronic cancellation functionality (art. L215-1-1).
