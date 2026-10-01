# Médiation de la consommation

Every trader dealing with consumers in France must give the consumer free access to a **médiateur de la consommation** and publish that médiateur's contact details. This is a French-specific compliance cost — the trader contracts with, and pays, a médiateur referenced by the CECMC — and it is the duty foreign templates most reliably omit.

## Article L612-1 du Code de la consommation

Status as at 2026-08-05. Version en vigueur depuis le 1er juillet 2016.

« Tout consommateur a le droit de recourir gratuitement à un médiateur de la consommation en vue de la résolution amiable du litige qui l'oppose à un professionnel. »

Free **for the consumer**. The trader bears the cost of the mediation scheme it joins. Article L612-2 sets out when a médiateur may decline a request: no prior written complaint to the trader, manifestly unfounded or abusive requests, a dispute already examined by another médiateur or a court, a request brought more than one year after the written complaint, and disputes outside the médiateur's competence.

## Article L616-1 — the publication duty

Status as at 2026-08-05. Version en vigueur depuis le 1er juillet 2016.

« Tout professionnel communique au consommateur les coordonnées du ou des médiateurs compétents dont il relève. »

In practice the details go in the **CGV**, on the **mentions légales** page, on order forms, and in the response to a complaint that could not be settled. Naming the scheme is not enough: the médiateur's name, postal address and website must be given, and the trader must actually be a member.

## Article L616-2 and the ODR platform

Article L616-2 is still formally in force in the version of 1 July 2016 and reads: the trader informs the consumer, where applicable, of the measures taken to implement **article 14 du règlement (UE) n° 524/2013** on online consumer dispute resolution.

That regulation was **repealed with effect from 20 July 2025 by règlement (UE) 2024/3228**. The ODR platform stopped accepting complaints on 20 March 2025 and was shut down on 20 July 2025. Article L616-2 therefore has no object: there are no measures to implement and there is no platform to link to.

Operational consequence: **never emit an ODR link.** A link to `ec.europa.eu/consumers/odr` is a dead link and, on a commercial page, a potentially misleading commercial practice. If a legacy CGV, mentions légales, order confirmation or email template contains one, delete it and replace it with the named médiateur. Do not reintroduce it because a template, a shop plugin or a marketplace checklist still asks for it.

[[UNVERIFIED: whether article L616-2 du Code de la consommation has since been formally repealed or amended to remove the reference to règlement (UE) n° 524/2013 — check Légifrance; the practical instruction above does not depend on the answer]]

## Article L641-1 — sanction

Failure to comply with the information duties of articles L616-1 and L616-2 is punishable by an administrative fine of up to **3 000 € for a natural person and 15 000 € for a legal person**. Imposed by the DGCCRF.

## Choosing a médiateur

The **Commission d'évaluation et de contrôle de la médiation de la consommation (CECMC)** maintains the official list of referenced médiateurs, published on `economie.gouv.fr/mediation-conso`. A médiateur not on that list does not satisfy article L612-1. Some sectors have a statutory médiateur (energy, telecoms, banking, insurance, travel); where one exists, the trader falls under it rather than choosing freely. Verify against the CECMC list before naming anyone, and never invent a name — an unnamed obligation reported as `[[MISSING: …]]` is far better than a fictitious médiateur in published CGV.

## Cross-border disputes

Article L616-3 provides assistance for consumers in cross-border disputes, directing them to the competent entity in another member state. The European Consumer Centre France (`europe-consommateurs.eu`) remains the practical contact point for cross-border consumer disputes now that the ODR platform is gone.

## The complaint step that must exist first

Mediation is only open once the consumer has made a written complaint to the trader and either received no answer or an unsatisfactory one (article L612-2). That means the trader needs a documented complaint route before it can validly point at a médiateur: a named address, an acknowledgement, and a response deadline stated in the CGV. A CGV that names a médiateur but gives no complaint address sends the consumer to a médiateur who will decline the request.

State the internal deadline explicitly — commonly one or two months — and hold to it. The one-year window for seising the médiateur runs from the written complaint, not from the incident.

## Remediating a legacy text

Legacy French CGV almost always contain the same two defects. Fix both in one pass:

1. A paragraph pointing at the European ODR platform, often with a live hyperlink. Delete the paragraph entirely. Do not replace it with "the platform is no longer available" — that sentence has no legal function and invites questions.
2. A generic sentence such as « le consommateur peut recourir à une médiation conventionnelle » with no médiateur named. This does not satisfy article L616-1. Replace it with the actual name, postal address and website of the contracted médiateur, or with `[[MISSING: médiateur de la consommation contracté et référencé par la CECMC]]` if none is contracted yet, and report it as a blocking item.

Check the same two defects in order confirmation emails, PDF invoices, the shop plugin's default legal strings, and any marketplace shop description, not only in the CGV page.

## Template

```html
<!-- BROUILLON – non validé juridiquement -->
<h2>Médiation de la consommation</h2>
<p>Conformément aux articles L. 612-1 et L. 616-1 du code de la consommation, vous
pouvez recourir gratuitement au service de médiation de la consommation ci-dessous,
en vue de la résolution amiable d'un litige nous opposant, après avoir adressé une
réclamation écrite à nos services et à défaut de réponse satisfaisante dans un délai
de [[délai]].</p>
<p>
  [[Nom du médiateur ou de l'entité de médiation]]<br>
  [[Adresse postale complète]]<br>
  [[Site internet]]
</p>
<p>La saisine du médiateur doit intervenir dans un délai d'un an à compter de votre
réclamation écrite.</p>
<p>Pour les litiges transfrontaliers, vous pouvez également contacter le Centre
européen des consommateurs France.</p>
```

## Checkpoints

- [ ] A médiateur is actually contracted and appears on the CECMC list
- [ ] Sector-specific statutory médiateur checked before choosing freely
- [ ] Name, postal address and website published, not just a scheme name
- [ ] Details present in the CGV **and** reachable from the mentions légales
- [ ] The prior written complaint step and the one-year time limit are explained
- [ ] No ODR link anywhere in the project, including order confirmations, invoices, transactional emails, shop plugin defaults and marketplace listings
- [ ] Full-text search over the project for `odr`, `ec.europa.eu/consumers`, `règlement en ligne des litiges`, `RLL`, `plateforme européenne` returns nothing
- [ ] Cross-border route mentioned via the Centre européen des consommateurs
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
