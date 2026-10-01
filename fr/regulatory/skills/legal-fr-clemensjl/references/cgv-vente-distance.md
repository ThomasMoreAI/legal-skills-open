# CGV et vente à distance

CGV are the contract. CGU are the rules of use of the service. They are different documents with different mandatory content; see `plateformes-sren-dsa.md` for CGU. Nothing here cites a directive: the binding text is the Code de la consommation.

## Article L111-1 du Code de la consommation — precontractual information

Status as at 2026-08-05. Version en vigueur depuis le 1er octobre 2021; applies to contracts concluded from 1 January 2022. Before the consumer is bound by an onerous contract, the trader communicates, **de manière lisible et compréhensible**:

1. « Les caractéristiques essentielles du bien ou du service, ainsi que celles du service numérique ou du contenu numérique » ;
2. « Le prix ou tout autre avantage procuré au lieu ou en complément du paiement d'un prix » ;
3. « En l'absence d'exécution immédiate du contrat, la date ou le délai auquel le professionnel s'engage à délivrer le bien ou à exécuter le service » ;
4. « Les informations relatives à l'identité du professionnel, à ses coordonnées postales, téléphoniques et électroniques » ;
5. « L'existence et les modalités de mise en œuvre des garanties légales, notamment la garantie légale de conformité » ;
6. « La possibilité de recourir à un médiateur de la consommation ».

Point 6 is the one foreign templates never carry. Point 2 is broader than "price": any advantage obtained instead of or in addition to payment — data-for-service arrangements included.

## Article L221-5 — distance and off-premises contracts

Adds, before conclusion: the information of L111-1 plus, where the right of withdrawal exists, the conditions, time limit and procedure for exercising it **and the formulaire type de rétractation**; where it does not exist or may be lost, that fact; the cost of returning the goods where the consumer bears it; the existence of applicable codes of conduct, deposits and financial guarantees; the duration of the contract and the conditions for terminating an open-ended or automatically renewed contract. Amended by ordonnance n° 2021-1734 du 22 décembre 2021 transposing directive (EU) 2019/2161, applicable to contracts concluded from 28 May 2022. [[UNVERIFIED: the full numbered enumeration of article L221-5 in its current version — confirm against Légifrance before reproducing it verbatim in a document]]

## Article L221-14 — the order process and the payment button

Status as at 2026-08-05. Version en vigueur depuis le 1er juillet 2016. Three duties:

1. Before the contract is concluded electronically, the trader reminds the consumer, legibly and comprehensibly, of the essential characteristics of the goods or services, their price, the duration of the contract, and any minimum commitment period, by reference to the information of article L221-5.
2. The trader ensures the consumer **explicitly acknowledges the payment obligation**. The function used to validate the order carries, **à peine de nullité**, the clear and legible wording « **commande avec obligation de paiement** » or an analogous formula, free of any ambiguity, indicating that placing the order entails payment.
3. Online trading sites indicate **at the latest at the beginning of the ordering process**, clearly and legibly, the accepted means of payment and any restrictions on delivery.

"Valider ma commande", "Continuer", "Payer" alone do not satisfy point 2. À peine de nullité means the consumer is not bound: this is not a cosmetic defect.

## Double clic — article 1127-2 du code civil

The contract is validly concluded only where the recipient has been able to check the detail of the order and its total price, and to correct errors, **before confirming it to express acceptance**. In practice: a summary page listing items, quantities, unit prices, shipping and total, an obvious route back to correct, then the payment-obligation button. The summary must sit immediately above the button, not on an earlier step. [[UNVERIFIED: exact current wording of article 1127-2 du code civil — the substance is settled but confirm the text before quoting it]]

## Price display

Prices shown to consumers are **TTC** — inclusive of VAT and all charges. Delivery costs are stated separately and before the order is placed (article L221-14 third paragraph for restrictions and means of payment; article L112-1 for the general price-marking duty). A trader under the **franchise en base de TVA** shows no VAT and must display « TVA non applicable, article 293 B du CGI » on invoices. Reference-price and discount claims are subject to the lowest price applied in the 30 days preceding the reduction.

## Product-page mentions that catch French shops

| Mention | When | Norm |
|---|---|---|
| Indice de réparabilité, 1 to 10 | Listed electrical and electronic equipment | art. L541-9-2 du code de l'environnement |
| Indice de durabilité, 1 to 10 | Televisions since 8 January 2025, washing machines since 8 April 2025, replacing the indice de réparabilité for those categories | art. L541-9-2 code env., décret n° 2024-316 du 5 avril 2024 |
| Availability of spare parts, with the period | Goods where the duty applies | art. L111-4 du Code de la consommation |
| Logo Triman and info-tri | Household products subject to an extended producer responsibility scheme, glass drink packaging excluded | art. L541-9-3 du code de l'environnement |
| Textile composition, care and origin claims | Textiles | EU regulation 1007/2011 and French implementing rules |

[[UNVERIFIED: whether the Triman and info-tri signage may be shown in dematerialised form on the product page rather than on the packaging for distance sales, and the exact décret governing that — confirm against ecologie.gouv.fr before advising a shop]]

## Template — CGV skeleton

```html
<!-- BROUILLON – non validé juridiquement -->
<h1>Conditions générales de vente</h1>
<p>Applicables aux ventes conclues à distance entre [[dénomination]], [[adresse]],
SIREN [[SIREN]], et tout consommateur au sens du code de la consommation.</p>

<h2>1. Objet et champ d'application</h2>
<h2>2. Caractéristiques essentielles des produits et services</h2>
<h2>3. Prix</h2>
<p>Les prix sont indiqués en euros toutes taxes comprises. Les frais de livraison
sont indiqués séparément avant la validation de la commande. [[franchise en base de
TVA : mention « TVA non applicable, article 293 B du CGI »]]</p>
<h2>4. Commande</h2>
<p>La validation de la commande s'effectue par une fonction portant la mention
« commande avec obligation de paiement ». Le consommateur peut vérifier le détail de
sa commande et son prix total et corriger d'éventuelles erreurs avant de la
confirmer.</p>
<h2>5. Paiement</h2>
<h2>6. Livraison</h2>
<p>Délai de livraison : [[délai]]. Restrictions de livraison : [[zones]].</p>
<h2>7. Droit de rétractation</h2>
<p>[[voir retractation.md — délai, exceptions, formulaire type]]</p>
<h2>8. Garantie légale de conformité et vices cachés</h2>
<p>[[voir garantie-conformite.md — encadré obligatoire]]</p>
<h2>9. Résiliation</h2>
<p>[[voir resiliation.md, pour les contrats à durée déterminée ou reconductibles]]</p>
<h2>10. Données personnelles</h2>
<h2>11. Médiation de la consommation</h2>
<p>[[voir mediation.md — nom, adresse postale et site du médiateur, aucun lien RLL]]</p>
<h2>12. Droit applicable</h2>
<p>Droit français, sans préjudice des dispositions impératives plus protectrices du
pays de résidence habituelle du consommateur.</p>
```

## Checkpoints

- [ ] Order button reads « commande avec obligation de paiement » or an unambiguous equivalent (art. L221-14)
- [ ] Order summary with items, prices, shipping and total sits immediately above the button, with a route back to correct
- [ ] Accepted means of payment and delivery restrictions shown at the latest at the start of the ordering process
- [ ] Prices TTC, delivery costs separate and shown before validation
- [ ] All six items of article L111-1 present, including the médiateur
- [ ] Withdrawal information and the model form provided before the contract (art. L221-5)
- [ ] Delivery date or period stated concretely, not "dès que possible"
- [ ] Legal guarantees described, not replaced by a commercial guarantee
- [ ] No pre-ticked optional extras
- [ ] Order confirmation sent on a durable medium
- [ ] Discount claims backed by the lowest price of the preceding 30 days
- [ ] Indice de réparabilité or de durabilité, spare-parts availability, Triman and info-tri shown where applicable
- [ ] CGV and CGU are separate documents
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
