# Prospection, newsletter et influence commerciale

Two distinct regimes. Electronic direct marketing runs on **article L34-5 du code des postes et des communications électroniques (CPCE)**, enforced by the CNIL and the DGCCRF. Paid influencer content runs on **loi n° 2023-451 du 9 juin 2023**, as amended by **ordonnance n° 2024-978 du 6 novembre 2024**.

## Article L34-5 CPCE — email, SMS and automated calling

Status as at 2026-08-05. Version en vigueur depuis le 26 juillet 2020.

Direct marketing by automated calling systems, fax or electronic mail using the contact details of a **natural person** is prohibited without that person's prior consent. Consent is defined as any free, specific and informed indication of wishes by which a person accepts that personal data concerning them be used for direct marketing.

Direct marketing covers any message promoting goods, services or the image of a person, including calls inviting the recipient to dial a premium-rate number.

**Exception for existing customers**: marketing by electronic mail is permitted where the contact details were obtained directly from the recipient in the course of a sale or the provision of a service, the marketing concerns **similar** products or services supplied by the same person, and the recipient is offered, expressly and unambiguously, the possibility to object free of charge and simply at the time the details are collected and in every subsequent message.

Every message must state valid contact details to which the recipient can send a request to stop, must not conceal the sender's identity, and must not use a misleading subject line.

The CNIL supervises compliance and receives complaints. Breaches are established by DGCCRF officers and sanctioned by an administrative fine of up to **75 000 € for a natural person and 375 000 € for a legal person**.

## Practical consequences

- **Double opt-in** is not required by the text but is the only realistic way to discharge the burden of proving consent (RGPD article 7(1)). Store timestamp, IP, the form text version and the confirmation click.
- The confirmation email must contain no advertising; a promotional confirmation email is itself unsolicited marketing.
- An unsubscribe link in every message, working in one click, with no login and no reason required.
- Separate, non-pre-ticked consent for the newsletter, distinct from acceptance of the CGV.
- The existing-customer exception is narrow: same trader, similar products, opportunity to object at collection. It does not cover a purchased list, a partner's list, or a new product line unrelated to the purchase.

## B2B nuance

Marketing to a professional at their professional address is treated differently: the CNIL accepts that prospection addressed to a professional, at a professional address, may rest on legitimate interest rather than consent, provided the message relates to the recipient's professional function and an opt-out is offered at collection and in every message. A nominative professional address of the form `prenom.nom@entreprise.fr` is still personal data and the person must be informed and able to object. Generic addresses (`contact@`, `info@`) are the least exposed case. [[UNVERIFIED: the exact current CNIL page and wording on B2B prospection — confirm on cnil.fr before advising a client that a given B2B list may be mailed without consent]]

## Telephone canvassing

Démarchage téléphonique is a separate regime with its own rules on permitted days and hours, the Bloctel opposition list, and mandatory identification at the start of the call. [[UNVERIFIED: whether the shift from an opposition regime to a prior-consent regime for telephone canvassing has taken effect, and the statute and date — this was legislated recently and must be checked before advising on outbound calling]]

## Influence commerciale — loi n° 2023-451

Status as at 2026-08-05. The law defines commercial influence carried out for consideration by electronic means as the activity of natural or legal persons who mobilise their notoriety **à titre onéreux** to promote, directly or indirectly, goods, services or any cause. Article 1 and articles 5, 5-1 and 5-2 were rewritten by **ordonnance n° 2024-978 du 6 novembre 2024**, adopted to bring the law into line with EU law after the notification procedure under directive (EU) 2015/1535 was not followed at adoption.

Mandatory mentions, which must be clear, legible and comprehensible on every medium used:

| Situation | Mention |
|---|---|
| Content promoting goods, services or a cause for consideration | « **Publicité** » or « **Collaboration commerciale** », or an equivalent adapted to the format |
| Images where a silhouette or a face has been retouched | « **Images retouchées** » |
| Images produced by artificial intelligence | « **Images virtuelles** » |

Failure to indicate the commercial intent is treated as a misleading commercial practice under article 5-2 as created by the ordonnance. Failure to carry the « Images retouchées » or « Images virtuelles » mention is punishable by **one year's imprisonment and a 4 500 € fine**.

Article 8 requires a **written contract** between advertiser and influencer, on pain of nullity, stating the parties' identities, the nature of the mission, the remuneration in cash or in kind, the rights and obligations of each party, and submission to French law. The obligation applies above a remuneration threshold fixed by décret. Advertiser, agent and influencer are jointly liable for damage caused to third parties. [[UNVERIFIED: the number and date of the décret fixing the remuneration threshold for the mandatory written contract, and the current threshold amount]]

Affiliate links, gifted products and ambassador programmes fall within the definition where anything of value is given: the disclosure duty is triggered by consideration, not by a payment in cash.

## Template — newsletter consent and unsubscribe

```html
<!-- BROUILLON – non validé juridiquement -->
<label>
  <input type="checkbox" name="newsletter" value="1">
  J'accepte de recevoir la lettre d'information de [[dénomination]] par courrier
  électronique, portant sur [[objet précis : nouveautés, offres, contenus]].
  Je peux retirer mon consentement à tout moment via le lien de désinscription
  présent dans chaque message. [[lien vers la politique de confidentialité]]
</label>
```

```html
<!-- pied de chaque envoi -->
<p>Vous recevez ce message parce que vous vous êtes inscrit le [[date]] sur
[[domaine]]. <a href="[[lien]]">Se désinscrire en un clic</a>.<br>
[[dénomination]], [[adresse postale]], [[courriel]].</p>
```

## Checkpoints

- [ ] Separate, non-pre-ticked consent for marketing, distinct from CGV acceptance
- [ ] Double opt-in active, confirmation email free of advertising
- [ ] Consent record kept: timestamp, IP, form text version, confirmation
- [ ] One-click unsubscribe in every message, no login, no reason required
- [ ] Sender identity and valid reply address in every message, no misleading subject line (art. L34-5 CPCE)
- [ ] Existing-customer exception used only for similar products of the same trader, with an objection route offered at collection
- [ ] Purchased or partner lists not mailed to natural persons
- [ ] Mentions légales or an equivalent identification block in every mailing
- [ ] Influencer and affiliate content carries « Publicité » or « Collaboration commerciale » throughout the content
- [ ] « Images retouchées » and « Images virtuelles » applied where relevant
- [ ] Written contract in place with every paid influencer above the décret threshold
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
