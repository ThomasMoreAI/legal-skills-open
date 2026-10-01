# Mentions légales

Two regimes apply in parallel. The LCEN covers every publisher of an online public communication service; the Code de commerce adds the commercial-register mentions for registered traders. One page can satisfy both, but neither may be omitted.

Accessibility: permanently available, no login, no consent gate in front of it. In practice a footer link on every page, labelled **Mentions légales**, reachable in one click.

## Article 1-1 de la loi n° 2004-575 (LCEN)

Status as at 2026-08-05. Version en vigueur depuis le 23 mai 2024, inserted by loi n° 2024-449 du 21 mai 2024 (loi SREN, which restructured the LCEN to align it with règlement (UE) 2022/2065). The old article 6-III no longer carries these duties.

Paragraph I, verbatim: « Les personnes dont l'activité est d'éditer un service de communication au public en ligne mettent à la disposition du public, dans un standard ouvert :

1° S'il s'agit de personnes physiques, leurs nom, prénoms, domicile et numéro de téléphone et, si elles sont assujetties aux formalités d'inscription au registre du commerce et des sociétés ou au registre national des entreprises en tant qu'entreprise du secteur des métiers et de l'artisanat, le numéro de leur inscription ;

2° S'il s'agit de personnes morales, leur dénomination ou leur raison sociale et leur siège social, leur numéro de téléphone et, s'il s'agit d'entreprises assujetties aux formalités d'inscription au registre du commerce et des sociétés ou au registre national des entreprises en tant qu'entreprise du secteur des métiers et de l'artisanat, le numéro de leur inscription, leur capital social et l'adresse de leur siège social ;

3° Le nom du directeur ou du codirecteur de la publication, au sens de l'article 93-2 de la loi n° 82-652 du 29 juillet 1982 sur la communication audiovisuelle et, le cas échéant, celui du responsable de la rédaction ;

4° Le nom, la dénomination ou la raison sociale, l'adresse et le numéro de téléphone du fournisseur de services d'hébergement ;

5° Le cas échéant, le nom, la dénomination ou la raison sociale et l'adresse des personnes physiques ou morales qui assurent, même à titre gratuit, le stockage de données traitées directement par elles dans le cadre de l'édition du service. »

Three consequences that foreign templates miss: the **telephone number** is mandatory, not optional; the **hébergeur** must be named with address and telephone; and a **directeur de la publication** must be designated by name.

Paragraph II: a person publishing **à titre non professionnel** may publish only the host's name, denomination or company name and address, to preserve anonymity, provided the identification data listed in I has been given to the host. The host is then bound by professional secrecy under articles 226-13 and 226-14 du code pénal, which is not opposable to the judicial authority. A commercial site, a site carrying advertising, and a site selling anything are professional and cannot use this option.

Paragraph III: right of reply, to be inserted within three days of receipt, on pain of a 3 750 € fine.

## Article 1-2 de la LCEN — the offence

Status as at 2026-08-05. « Est puni d'un an d'emprisonnement et de 75 000 euros d'amende le fait, pour une personne physique ou le dirigeant de droit ou de fait d'une personne morale dont l'activité est d'éditer un service de communication au public en ligne, de ne pas respecter les I et II de l'article 1er-1. » 375 000 € for a legal person. This is a criminal offence, not an administrative irregularity.

## Article R123-237 du code de commerce

Status as at 2026-08-05. Version en vigueur depuis le 15 mai 2022 (décret n° 2022-725 du 28 avril 2022). A person registered in the RCS must show on **its website**: the mention « RCS » followed by the city where the greffe sits, plus the items at 1°, 3°, 5°, 8° and 9° — the numéro unique d'identification (SIREN), the location of the siège social, for a foreign company its denomination, legal form and home registration number, the EIRL wording where applicable, and the « entrepreneur individuel » wording where applicable. Companies also state whether they are en liquidation. Breach is a contravention de la 4e classe.

The **numéro de TVA intracommunautaire** is required on invoices under the Code général des impôts; publishing it in the mentions légales is standard practice and avoids a separate defect on invoices. Format: FR, two characters, then the SIREN.

## Regulated professions and services

Article L111-2 du Code de la consommation adds, for a service provider, the professional title and the professional body granting it, the applicable professional rules and how to access them, and the details of any mandatory professional liability insurance including the geographic coverage. Article 1-1 I LCEN does not carry these; they are a Code de la consommation duty and must be added for avocats, experts-comptables, architectes, agents immobiliers, professions de santé and the like.

## Template

```html
<!-- BROUILLON – non validé juridiquement -->
<h1>Mentions légales</h1>
<p>Conformément à l'article 1-1 de la loi n° 2004-575 du 21 juin 2004 pour la confiance
dans l'économie numérique et à l'article R. 123-237 du code de commerce.</p>

<h2>Éditeur du site</h2>
<p>
  [[Dénomination sociale ou nom et prénoms]]<br>
  Forme juridique : [[forme juridique]]<br>
  Capital social : [[montant]] euros<br>
  Siège social : [[adresse complète, code postal, commune, France]]<br>
  Numéro unique d'identification (SIREN) : [[SIREN]]<br>
  Immatriculée au RCS de [[ville du greffe]]<br>
  SIRET : [[SIRET]]<br>
  Numéro de TVA intracommunautaire : [[FR……]]<br>
  Téléphone : [[numéro]]<br>
  Courriel : <a href="mailto:[[adresse]]">[[adresse]]</a>
</p>

<h2>Directeur de la publication</h2>
<p>[[Nom et prénom]], en qualité de [[fonction]].<br>
Responsable de la rédaction : [[nom ou : sans objet]]</p>

<h2>Hébergeur</h2>
<p>
  [[Dénomination de l'hébergeur]]<br>
  [[Adresse complète]]<br>
  Téléphone : [[numéro]]
</p>

<h2>Activité réglementée</h2>
<p>
  Titre professionnel : [[titre]] — délivré en [[État membre]]<br>
  Ordre ou organisme professionnel : [[nom]]<br>
  Règles professionnelles applicables : [[référence]], consultables sur [[URL]]<br>
  Assurance de responsabilité civile professionnelle : [[assureur, adresse,
  couverture géographique]]<br>
  Autorité de contrôle : [[autorité ou : sans objet]]
</p>

<h2>Médiation de la consommation</h2>
<p>[[voir mediation.md — aucun lien vers la plateforme RLL]]</p>

<h2>Propriété intellectuelle et crédits</h2>
<p>
  Les contenus de ce site sont protégés par le code de la propriété intellectuelle.<br>
  Crédits photographiques : [[auteur / banque d'images / licence]]
</p>
```

## Checkpoints

- [ ] Reachable in one click from every page, without login and without a consent gate
- [ ] Link labelled « Mentions légales », not « À propos », « Legal » or « Impressum »
- [ ] Telephone number present (article 1-1 I 1° et 2° LCEN)
- [ ] Hébergeur named with denomination, full address and telephone (article 1-1 I 4°)
- [ ] Third-party data storage providers named where applicable (article 1-1 I 5°)
- [ ] Directeur de la publication named (article 1-1 I 3°)
- [ ] SIREN, « RCS » plus the city of the greffe, capital social, siège social (article R123-237)
- [ ] TVA intracommunautaire number, if VAT-registered
- [ ] Professional title, body, rules and insurance for regulated activities (article L111-2 C. conso)
- [ ] No citation of « article 6-III de la LCEN », « § 5 TMG », « § 5 DDG » or « § 5 ECG »
- [ ] No ODR link
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
