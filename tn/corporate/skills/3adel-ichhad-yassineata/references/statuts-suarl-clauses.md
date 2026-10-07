# SUARL articles of association — standard clauses and template

> **Language note:** the explanatory prose in this file is in English (for the user). **The clause text itself stays in French** because it is the language used by the RNE clerk, the JORT publication notice, and Tunisian notaries. Do not translate the clauses — submit them in French.

## Preamble (for the drafter)

This file contains a **ready-to-fill SUARL articles-of-association template**, structured to pass the RNE clerk without friction.

> ⚠️ This template is a starting point. For specific object clauses, regulated activities, or complex setups (in-kind contributions, etc.), **consult a registered notary or lawyer**. The `3adel-ichhad` skill always appends a `[REQUIRES NOTAIRE SIGNATURE]` block at the end of any generated document.

Variables to replace (notation `{VAR}`):
- `{NOM_SOCIETE}`: e.g. "ATLAS DEV TUNIS"
- `{FORME_JURIDIQUE}`: SUARL
- `{CAPITAL_DT}`: e.g. 1000 (numeric) — legal SUARL minimum
- `{CAPITAL_LETTRES}`: e.g. "MILLE DINARS TUNISIENS"
- `{NB_PARTS}`: e.g. 100 or 1000
- `{VALEUR_PART}`: e.g. 10 or 1
- `{ADRESSE_SIEGE}`: full registered-office address
- `{GOUVERNORAT}`: e.g. Tunis, Sfax, Sousse
- `{ASSOCIE_NOM}`, `{ASSOCIE_CIN}`, `{ASSOCIE_ADRESSE}`, `{ASSOCIE_NATIONALITE}`
- `{OBJET_SOCIAL}`: precise activity description
- `{DUREE_ANNEES}`: e.g. 99 (default)
- `{DATE_CONSTITUTION}`: DD/MM/YYYY

---

## Template — STATUTS DE LA SOCIÉTÉ "{NOM_SOCIETE}" SUARL

### LE SOUSSIGNÉ

Monsieur / Madame {ASSOCIE_NOM}, titulaire de la CIN n° {ASSOCIE_CIN} délivrée le ___ à ___, demeurant à {ASSOCIE_ADRESSE}, de nationalité {ASSOCIE_NATIONALITE},

A établi ainsi qu'il suit les statuts de la société unipersonnelle à responsabilité limitée qu'il a décidé de constituer.

---

### TITRE I — FORME, DÉNOMINATION, OBJET, SIÈGE, DURÉE

**Article 1 — Forme**

Il est constitué une Société Unipersonnelle à Responsabilité Limitée (SUARL) régie par les dispositions du Code des Sociétés Commerciales tunisien (notamment articles 148 et suivants), les présents statuts, et toutes lois et règlements applicables.

**Article 2 — Dénomination**

La société prend la dénomination sociale : **« {NOM_SOCIETE} »**.

Cette dénomination doit être précédée ou suivie immédiatement, dans tous les actes, factures, annonces, publications et autres documents émanant de la société, des mots « Société Unipersonnelle à Responsabilité Limitée » ou des initiales « SUARL », ainsi que de l'énonciation du capital social.

**Article 3 — Objet**

La société a pour objet, tant en Tunisie qu'à l'étranger :

{OBJET_SOCIAL}

[Example object clause for a dev studio — **NAT codes inline**, see `nomenclature-nat.md`: *"Programmation informatique (NAT 62.01), conseil en systèmes informatiques (NAT 62.02), et toutes prestations connexes : développement, conception, maintenance et commercialisation de logiciels et solutions informatiques ; conseil et prestation de services dans le domaine des technologies de l'information ; formation technique associée ; et plus généralement toute opération industrielle, commerciale ou financière, mobilière ou immobilière, se rattachant directement ou indirectement à l'objet social ou susceptible d'en faciliter l'extension ou le développement."*]

[Example for an AI Automation Agency: *"Programmation informatique (NAT 62.01), autres activités informatiques incluant l'intégration de systèmes d'intelligence artificielle et l'automatisation des processus métier (NAT 62.09), conseil en gestion et en organisation (NAT 70.22)..."*]

[REQUIRES NOTAIRE SIGNATURE — specify if a regulated activity is included]
[NAT CODE MANDATORY — the RNE clerk needs the code on the registration form. Pick from `references/nomenclature-nat.md`. Marketing labels alone ("AI startup", "SaaS") will not pass.]

**Article 4 — Siège social**

Le siège social est fixé à : {ADRESSE_SIEGE}, gouvernorat de {GOUVERNORAT}, Tunisie.

Il pourra être transféré en tout autre lieu sur le territoire tunisien par décision de l'associé unique.

**Article 5 — Durée**

La durée de la société est fixée à {DUREE_ANNEES} années à compter de son immatriculation au Registre National des Entreprises (RNE), sauf cas de dissolution anticipée ou prorogation.

---

### TITRE II — CAPITAL SOCIAL, APPORTS, PARTS SOCIALES

**Article 6 — Apports**

L'associé unique apporte à la société, à titre d'apport en numéraire, la somme de **{CAPITAL_DT} dinars tunisiens ({CAPITAL_LETTRES})**, intégralement libérée et déposée auprès de la banque [NOM_BANQUE], comme l'atteste l'attestation de blocage du capital annexée aux présents statuts.

**Article 7 — Capital social**

Le capital social est fixé à la somme de **{CAPITAL_DT} dinars tunisiens ({CAPITAL_LETTRES})**, divisé en **{NB_PARTS} parts sociales** de **{VALEUR_PART} dinars** chacune, intégralement souscrites et libérées par l'associé unique.

**Article 8 — Augmentation et réduction du capital**

Le capital social peut être augmenté ou réduit en vertu d'une décision de l'associé unique, conformément aux articles 116 et suivants du Code des Sociétés Commerciales.

**Article 9 — Parts sociales**

Les parts sociales ne peuvent être représentées par des titres négociables. Elles sont indivisibles à l'égard de la société. Toute cession éventuelle suite à transmission ou décès est régie par les articles applicables du CSC et entraîne, le cas échéant, transformation en SARL.

---

### TITRE III — GÉRANCE

**Article 10 — Désignation du gérant**

La société est gérée par un ou plusieurs gérants, personnes physiques, désignés par l'associé unique. Le premier gérant désigné est : **{ASSOCIE_NOM}** (associé unique lui-même), pour une durée indéterminée.

**Article 11 — Pouvoirs du gérant**

Le gérant dispose des pouvoirs les plus étendus pour agir en toutes circonstances au nom de la société, dans la limite de l'objet social et sous réserve des pouvoirs expressément réservés par la loi à l'associé unique.

**Article 12 — Rémunération**

La rémunération éventuelle du gérant est fixée par décision de l'associé unique.

**Article 13 — Responsabilité**

Le gérant est responsable envers la société et envers les tiers dans les conditions prévues par les articles 116 à 127 du Code des Sociétés Commerciales.

---

### TITRE IV — DÉCISIONS DE L'ASSOCIÉ UNIQUE

**Article 14 — Pouvoirs**

L'associé unique exerce les pouvoirs dévolus à l'assemblée des associés par le Code des Sociétés Commerciales.

**Article 15 — Modalités**

Toutes les décisions de l'associé unique sont consignées dans un registre spécial tenu au siège social, avec date, objet et signature de l'associé.

---

### TITRE V — EXERCICE SOCIAL, COMPTES, RÉSULTATS

**Article 16 — Exercice social**

L'exercice social commence le 1er janvier et se termine le 31 décembre de chaque année.

Par exception, le premier exercice commence à la date d'immatriculation au RNE et se termine le 31 décembre {ANNEE_PREMIER_EXERCICE}.

**Article 17 — Comptes annuels**

À la clôture de chaque exercice, le gérant établit l'inventaire, les comptes annuels et le rapport de gestion conformément à la législation en vigueur.

**Article 18 — Affectation des résultats**

Le bénéfice distribuable est attribué à l'associé unique selon décision, sous réserve de l'affectation à la réserve légale (5% du bénéfice annuel jusqu'à ce que la réserve atteigne 10% du capital social).

---

### TITRE VI — DISSOLUTION, LIQUIDATION

**Article 19 — Dissolution**

La société est dissoute dans les cas prévus par la loi et le présent acte. La dissolution entraîne la liquidation conformément aux dispositions du Code des Sociétés Commerciales.

---

### TITRE VII — DISPOSITIONS DIVERSES

**Article 20 — Frais de constitution**

Les frais et droits de constitution sont à la charge de la société, qui les amortira sur les premiers exercices.

**Article 21 — Élection de domicile**

Pour l'exécution des présents statuts, élection de domicile est faite au siège social.

**Article 22 — Loi applicable et juridiction**

Les présents statuts sont régis par la loi tunisienne. Tout litige sera soumis aux tribunaux compétents de {GOUVERNORAT}.

---

**Fait à {GOUVERNORAT}, le {DATE_CONSTITUTION}, en trois exemplaires originaux.**

L'associé unique :

{ASSOCIE_NOM}

(signature)

---

## [REQUIRES NOTAIRE SIGNATURE]

> This articles-of-association template must be **read one final time by a registered notary or lawyer** before signing and filing with the RNE. The `3adel-ichhad` skill is not a replacement for the notarial signature — it optimises the drafting to minimise clerk friction but does not cover every edge case.

## Annexes to attach to the RNE dossier

1. Capital blocking certificate (depositary bank)
2. Proof of registered-office domiciliation
3. Certified copy of the sole shareholder's national ID card (CIN)
4. RNE registration form, fully completed
5. Receipt of fees and fiscal stamps
6. Receipt of the declaration of existence at the BCI (tax ID pending)

## RNE clerk anti-friction checklist

- [ ] Company name verified as available (RNE non-similarity certificate)
- [ ] Capital matches the value on the bank certificate (exact, to the dinar)
- [ ] Registered-office address = address on the lease / domiciliation contract (identical spelling)
- [ ] CIN reproduced identically everywhere (number, date, place of issue)
- [ ] Object clause does not contain an unlicensed regulated activity
- [ ] All copies hand-signed (ink, not scanned)
- [ ] Pages numbered
- [ ] Constitution date = signature date, not a projected date

## Sources

- `code-societes.md` (legal framework)
- `rne.md` (registration procedure)
- `data/sources.json` → `code-societes-commerciales`
