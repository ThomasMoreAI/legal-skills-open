# Politique de confidentialité

The GDPR supplies the substance. The loi n° 78-17 du 6 janvier 1978 relative à l'informatique, aux fichiers et aux libertés (loi Informatique et Libertés, recodified by ordonnance n° 2018-1125 du 12 décembre 2018) supplies the French deviations. Depth belongs on the deviations; the GDPR articles are stated compactly so this file is usable alone.

## What RGPD articles 13 and 14 require, per processing

Identity and contact details of the responsable de traitement and of the DPO where appointed; purpose and **legal basis** for each processing, and the legitimate interests pursued where article 6(1)(f) is relied on; recipients or categories of recipients; transfers outside the EU with the safeguard relied on; retention period or the criteria determining it; the rights of access, rectification, erasure, restriction, portability and objection; the right to withdraw consent without affecting past processing; the right to lodge a complaint with the CNIL; whether provision of the data is a statutory or contractual requirement; the existence of automated decision-making including profiling. Article 14 adds the source of the data where it was not collected from the data subject.

A policy that lists services without stating a legal basis per purpose is defective under article 13(1)(c). Boilerplate "legitimate interest" without naming the interest is defective.

## Article 45 de la loi n° 78-17 — age of digital consent

Status as at 2026-08-05. Version en vigueur depuis le 1er juin 2019.

« En application du 1 de l'article 8 du règlement (UE) 2016/679 du 27 avril 2016, un mineur peut consentir seul à un traitement de données à caractère personnel en ce qui concerne l'offre directe de services de la société de l'information à compter de l'âge de quinze ans.

Lorsque le mineur est âgé de moins de quinze ans, le traitement n'est licite que si le consentement est donné conjointement par le mineur concerné et le ou les titulaires de l'autorité parentale à l'égard de ce mineur.

Le responsable de traitement rédige en des termes clairs et simples, aisément compréhensibles par le mineur, les informations et communications relatives au traitement qui le concerne. »

Three operational consequences. The threshold is **fifteen**, not sixteen. Below fifteen the consent is **joint** — the parent's consent alone is not enough, the minor must also consent. And the notice itself must be written in language a minor can understand, which means a second, plain-language version of the policy where the audience includes minors.

## Article 85 de la loi n° 78-17 — directives post mortem

Status as at 2026-08-05. Any person may lay down directives on the retention, erasure and communication of their personal data after their death. These directives may be general (registered with a certified digital trust provider) or specific to a given controller. A French privacy policy must state that the right exists and how to exercise it with this controller. No other member state has this right; a translated German or Irish policy will not contain it.

## Article 82 de la loi n° 78-17 — trackers

Cookies and any read or write on terminal equipment are governed by article 82, not by RGPD article 6. Detail in `cookies.md`. The privacy policy cross-refers; it does not replace the banner.

## Residual French formalities

The GDPR abolished most prior formalities, but not all. Processing of health data for research, processing of the **NIR** (numéro d'inscription au répertoire, the social security number) and certain state files remain subject to specific French regimes under loi 78-17 — authorisation, décret en Conseil d'État, or a declaration of conformity with a CNIL **référentiel** or **méthodologie de référence**. If the project touches health data, biometrics for access control, or the NIR, stop and check the applicable CNIL référentiel before drafting. [[UNVERIFIED: the specific article numbers of loi 78-17 governing health-data research authorisations and NIR processing — confirm against the consolidated text on Légifrance before citing them]]

## Transferts hors UE — le DPF après Trump v. Slaughter

Article 13(1)(f) RGPD requires the instrument to be named per recipient. For a US recipient the EU-US Data Privacy Framework — décision d'exécution (UE) 2023/1795 du 10.07.2023 — covers only an organisation actually listed on `dataprivacyframework.gov/list`, and only within its certified scope. Check the contracting entity on the invoice, not the brand.

On **29.06.2026** the US Supreme Court held in *Trump v. Slaughter* that the statutory protection against removal of FTC commissioners is unconstitutional. Décision 2023/1795 rests on that independence: the FTC is the body enforcing the DPF principles, and independent supervision is a component of the adequacy test in article 45(2)(b) RGPD. Status as at 05.08.2026: noyb wrote to the Commission on 29.06.2026 seeking an orderly repeal and announced an annulment action (no filing confirmed); the EDPB wrote to Commissioner McGrath on 31.07.2026 asking for a close assessment; the Commission has not acted.

- The decision **remains in force** until the Commission repeals it or the Court of Justice annuls it. Do not write that transfers to the US have become unlawful.
- **The DPF alone is no longer sufficient.** Put clauses contractuelles types under article 46(2)(c) RGPD in the same contract as a fallback and complete an **analyse d'impact du transfert** addressing oversight and redress specifically. The CNIL has consistently treated the availability of an effective remedy as the decisive point in its US transfer decisions, so this is the limb it will examine.
- The published politique de confidentialité still names recipient, country and instrument. The fallback belongs in the registre des activités de traitement and the contrat de sous-traitance.

## Supervisory authority

Commission nationale de l'informatique et des libertés (CNIL), 3 place de Fontenoy, TSA 80715, 75334 Paris Cedex 07. Complaints: `cnil.fr/fr/plaintes`. The CNIL is the only competent authority for a controller established only in France; naming a German or Irish authority is a defect.

## DPO

No French headcount threshold. RGPD article 37 applies unchanged: a DPO is mandatory for public authorities, where core activities require regular and systematic monitoring on a large scale, or where core activities consist of large-scale processing of article 9 or article 10 data. The German rule of a DPO from 20 employees has no French counterpart. If a DPO is appointed, publish the contact details and notify the CNIL.

## Template

```html
<!-- BROUILLON – non validé juridiquement -->
<h1>Politique de confidentialité</h1>

<h2>Responsable du traitement</h2>
<p>[[dénomination]], [[adresse]], [[courriel]]. Délégué à la protection des données :
[[nom et coordonnées ou : aucun délégué n'a été désigné]].</p>

<h2>Traitements mis en œuvre</h2>
<table>
  <tr><th>Finalité</th><th>Base légale (RGPD art. 6)</th><th>Données</th>
      <th>Durée de conservation</th><th>Destinataires</th></tr>
  <tr><td>[[finalité]]</td><td>[[base]]</td><td>[[catégories]]</td>
      <td>[[durée ou critère]]</td><td>[[destinataires]]</td></tr>
</table>

<h2>Transferts hors Union européenne</h2>
<p>[[destinataire, pays, garantie : décision d'adéquation / clauses contractuelles
types / dérogation art. 49]]</p>

<h2>Vos droits</h2>
<p>Vous disposez d'un droit d'accès, de rectification, d'effacement, de limitation,
d'opposition et de portabilité, ainsi que du droit de retirer votre consentement à
tout moment sans que cela n'affecte la licéité du traitement effectué auparavant.
Vous pouvez également définir des directives relatives au sort de vos données à
caractère personnel après votre décès, conformément à l'article 85 de la loi
n° 78-17 du 6 janvier 1978. Ces droits s'exercent auprès de [[contact]].</p>

<h2>Mineurs</h2>
<p>Conformément à l'article 45 de la loi n° 78-17 du 6 janvier 1978, un mineur de
moins de quinze ans ne peut consentir seul : le consentement est donné conjointement
par le mineur et le ou les titulaires de l'autorité parentale. [[décrire la
vérification mise en place]]</p>

<h2>Réclamation</h2>
<p>Vous pouvez introduire une réclamation auprès de la CNIL, 3 place de Fontenoy,
TSA 80715, 75334 Paris Cedex 07, ou sur www.cnil.fr.</p>

<h2>Cookies et traceurs</h2>
<p>Voir la page dédiée. Le dépôt et la lecture de traceurs sont régis par l'article 82
de la loi n° 78-17 du 6 janvier 1978.</p>
```

## Checkpoints

- [ ] Reachable without consent and without login
- [ ] Legal basis stated for every purpose, legitimate interests named concretely
- [ ] Every service actually loaded appears in the policy, checked against a network capture
- [ ] Retention period or criterion per category, not a single global sentence
- [ ] Third-country transfers listed individually with the safeguard relied on
- [ ] Directives post mortem mentioned (article 85 de la loi 78-17)
- [ ] Consent age handled as 15 with joint consent below (article 45)
- [ ] Plain-language version where the audience includes minors
- [ ] CNIL named as supervisory authority with the correct address
- [ ] DPO contact published where a DPO is appointed, and notified to the CNIL
- [ ] No reference to BDSG, to a German Landesdatenschutzbehörde, or to a consent age of 16
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
