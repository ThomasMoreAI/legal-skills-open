# Accessibilité numérique

Two French regimes apply, with different triggers, different obligations and different enforcers. Confusing them is the usual failure: a small B2C shop concludes it is exempt because it is far below 250 million € turnover, and misses the European Accessibility Act layer that has applied since 28 June 2025.

## Regime 1 — article 47 de la loi n° 2005-102 du 11 février 2005

Status as at 2026-08-05. Version en vigueur depuis le 8 septembre 2023, amended by **ordonnance n° 2023-859 du 6 septembre 2023**, article 1.

**Who is covered**: online public communication services of public bodies, of private bodies entrusted with a public service mission, of private bodies created to meet needs in the general interest, and of **undertakings whose turnover exceeds a threshold set by décret**. That threshold is fixed at **250 million €** by article 2 du décret n° 2019-768 du 24 juillet 2019.

**What is owed**:

- publication of a **déclaration d'accessibilité**;
- a **schéma pluriannuel de mise en accessibilité** covering no more than three years, with annual action plans made public;
- on the **home page**, a clearly visible mention of the conformity status, giving easy access to the accessibility declaration and the action plans.

**Enforcement**: the **Autorité de régulation de la communication audiovisuelle et numérique (ARCOM)**, with fines of up to **50 000 €** for failing the accessibility requirements and up to **25 000 €** for failing the declaration and home-page mention duties.

**The technical reference** is the **RGAA — Référentiel général d'amélioration de l'accessibilité**, current published version **4.1.2**, established jointly by the ministers responsible for disability and for digital affairs by arrêté of 20 September 2019 and maintained at `accessibilite.numerique.gouv.fr`. RGAA 4 is aligned with WCAG 2.1 level AA via EN 301 549.

**The home-page mention** takes one of exactly three forms:

- « Accessibilité : totalement conforme » — all applicable criteria met;
- « Accessibilité : partiellement conforme » — at least 50 % of applicable criteria met;
- « Accessibilité : non conforme » — under 50 %, or no valid audit.

It may be a link to the accessibility page. There is no fourth option, and omitting the mention because the result is embarrassing is itself the sanctioned breach.

The accessibility page must be reachable from the home page and from every other page, and must carry the declaration, the schéma pluriannuel or a link to it, and the annual action plan or a link to it.

## Regime 2 — European Accessibility Act, article L412-13 du Code de la consommation

Status as at 2026-08-05. Introduced by **loi n° 2023-171 du 9 mars 2023**, with implementing texts including ordonnance n° 2023-859 du 6 septembre 2023 and its décrets.

**Scope**: products placed on the market and services **provided after 28 June 2025**, in the categories listed by décret — which include e-commerce services, consumer banking, e-books, electronic communications services, and transport services. The trigger is the nature of the service to consumers, not turnover.

**Microenterprise exemption**: undertakings employing **fewer than ten persons** and whose **annual turnover does not exceed two million €** or whose **balance sheet total does not exceed two million €** are exempt in respect of services. The exemption is for services; a business that manufactures, imports or distributes covered products does not get it for those products.

**Disproportionate burden**: an economic operator may assess whether compliance would require a fundamental alteration or impose a disproportionate burden. This is an assessment to be documented and kept, not a declaration to be asserted. An undocumented claim of disproportionate burden fails on inspection.

[[UNVERIFIED: the précis list of services covered by the décret adopted under article L412-13, the enforcing authority for the private-sector EAA layer, and the applicable sanctions — confirm on Légifrance and economie.gouv.fr before telling a client which category they fall into]]

## Deciding which regime applies

| Situation | Regime 1 (art. 47) | Regime 2 (L412-13) |
|---|---|---|
| Public body or public service mission | Yes | Depends on the service |
| Private company, turnover in France above 250 M€ | Yes | Yes if the service is covered |
| B2C e-commerce, 12 employees, 4 M€ turnover | No | Yes |
| B2C e-commerce, 6 employees, 900 k€ turnover | No | Exempt as a microenterprise for its services |
| B2B-only SaaS | No | Generally no; check the décret list |

A business outside both regimes still faces the general prohibition of discrimination and the reputational and commercial cost of an unusable site. Say so once; do not turn it into a compliance claim.

## Template — déclaration d'accessibilité skeleton

```html
<!-- BROUILLON – non validé juridiquement -->
<h1>Déclaration d'accessibilité</h1>
<p>[[dénomination]] s'engage à rendre son site accessible conformément à l'article 47
de la loi n° 2005-102 du 11 février 2005.</p>
<p>Cette déclaration s'applique à [[URL du site]].</p>

<h2>État de conformité</h2>
<p>[[URL]] est <strong>[[non conforme / partiellement conforme / totalement
conforme]]</strong> avec le référentiel général d'amélioration de l'accessibilité
(RGAA), version 4.1.2, [[taux de conformité]] % des critères étant respectés.</p>

<h2>Résultats des tests</h2>
<p>L'audit de conformité réalisé le [[date]] par [[auditeur]] révèle que
[[pourcentage]] % des critères du RGAA 4.1.2 sont respectés.</p>

<h2>Contenus non accessibles</h2>
<p>[[liste des non-conformités, des dérogations pour charge disproportionnée avec leur
justification, et des contenus non soumis]]</p>

<h2>Amélioration et contact</h2>
<p>Schéma pluriannuel : [[lien]]. Plan d'action [[année]] : [[lien]].<br>
Contact : [[courriel]], [[adresse postale]].</p>

<h2>Voie de recours</h2>
<p>Si vous n'obtenez pas de réponse, vous pouvez adresser un signalement au Défenseur
des droits, saisir son délégué dans votre région ou lui écrire par voie postale.</p>
```

Home-page mention, verbatim, one of the three:

```html
<a href="/accessibilite">Accessibilité : partiellement conforme</a>
```

## Checkpoints

- [ ] Applicability of both regimes assessed and the reasoning recorded
- [ ] Microenterprise status documented with headcount and turnover or balance sheet, if relied on
- [ ] Home page carries one of the three exact mentions, visible and linked
- [ ] Accessibility page reachable from the home page and from every page
- [ ] Déclaration d'accessibilité published, following the RGAA model
- [ ] Schéma pluriannuel of no more than three years, plus the annual action plan, published
- [ ] Audit against RGAA 4.1.2 performed and dated, conformity rate stated honestly
- [ ] Keyboard-only pass through the main flows succeeds, focus visible
- [ ] Contrast measured, form labels associated, error messages textual
- [ ] Screen-reader pass through checkout or signup
- [ ] Any disproportionate-burden claim documented with the assessment, not merely asserted
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
