# ACTE DE DONATION ENTRE VIFS

> Modèle pour acte notarié — à adapter par le notaire instrumentant

L'an DEUX MILLE {{ANNEE_LETTRES}},
Le {{JOUR_LETTRES}} {{MOIS_LETTRES}}.

Par-devant **Maître {{NOM_NOTAIRE}}**, notaire de résidence à {{RESIDENCE_NOTAIRE}}, soussigné.

---

## ONT COMPARU

### LE DONATEUR

**Monsieur / Madame {{NOM_PRENOM_DONATEUR}}**
Né(e) le {{DATE_NAISSANCE_DONATEUR}} à {{LIEU_NAISSANCE_DONATEUR}}
De nationalité {{NATIONALITE_DONATEUR}}
Demeurant : {{ADRESSE_DONATEUR}}
N° matricule : {{MATRICULE_DONATEUR}}

{{#SI_MARIE_DONATEUR}}Marié(e) sous le régime de {{REGIME_MATRIMONIAL}} avec {{NOM_CONJOINT}}{{/SI_MARIE_DONATEUR}}

### LE DONATAIRE

**Monsieur / Madame {{NOM_PRENOM_DONATAIRE}}**
Né(e) le {{DATE_NAISSANCE_DONATAIRE}} à {{LIEU_NAISSANCE_DONATAIRE}}
De nationalité {{NATIONALITE_DONATAIRE}}
Demeurant : {{ADRESSE_DONATAIRE}}
N° matricule : {{MATRICULE_DONATAIRE}}

**Lien de parenté avec le donateur** : {{LIEN_PARENTE}}
(exemples : enfant, petit-enfant, conjoint, neveu, étranger)

---

## LE DONATEUR DÉCLARE FAIRE DONATION ENTRE VIFS

### Au DONATAIRE qui accepte expressément du bien suivant :

#### Désignation du bien donné

{{#SI_BIEN_IMMOBILIER}}

**Bien immobilier**

Désignation cadastrale :
- Commune : {{COMMUNE}}
- Section : {{SECTION_CADASTRALE}}
- N° : {{NUMERO_CADASTRAL}}
- Contenance : {{SURFACE}} m²

Description : {{DESCRIPTION_BIEN}}

Origine de propriété : acquis par le donateur suivant {{ORIGINE_PROPRIETE}}

{{/SI_BIEN_IMMOBILIER}}

{{#SI_PARTS_SOCIALES}}

**Parts sociales / Actions**

- Société : {{NOM_SOCIETE}}
- Forme juridique : {{FORME_SOCIALE}}
- N° RCS : B {{RCS_SOCIETE}}
- Nombre de parts/actions : {{NOMBRE_PARTS}}
- Valeur nominale unitaire : {{VALEUR_NOMINALE}} €

{{/SI_PARTS_SOCIALES}}

{{#SI_SOMME_ARGENT}}

**Somme d'argent**

- Montant : **{{MONTANT_DON_LETTRES}} EUROS** ({{MONTANT_DON_CHIFFRES}} €)
- Origine : {{ORIGINE_FONDS}}
- Mode de remise : virement bancaire / espèces / chèque
{{/SI_SOMME_ARGENT}}

---

## ARTICLE 1 — VALEUR ET ÉVALUATION

Le bien donné est évalué à : **{{VALEUR_LETTRES}} EUROS** ({{VALEUR_CHIFFRES}} €).

---

## ARTICLE 2 — CONDITIONS DE LA DONATION

{{#SI_AVEC_USUFRUIT}}
### Réserve d'usufruit
Le DONATEUR se réserve l'**usufruit** du bien donné jusqu'à son décès.
Le DONATAIRE n'acquiert que la **nue-propriété**.
À l'extinction de l'usufruit (décès du donateur), la pleine propriété sera reconstituée au profit du donataire **sans nouveaux droits** à payer.

Évaluation usufruit selon barème art. 13 loi succession :
- Âge du donateur : {{AGE_DONATEUR}} ans
- Valeur usufruit : {{VALEUR_USUFRUIT}} €
- Valeur nue-propriété : {{VALEUR_NUE_PROPRIETE}} €
{{/SI_AVEC_USUFRUIT}}

{{#SI_DONATION_RAPPORTABLE}}
### Donation rapportable
La présente donation est consentie **en avancement de part successorale**, le donataire devant en faire le rapport à la succession du donateur.
{{/SI_DONATION_RAPPORTABLE}}

{{#SI_DONATION_HORS_PART}}
### Donation hors part / par préciput
La présente donation est consentie **hors part successorale**, sur la quotité disponible du donateur. Elle ne sera pas rapportable à la succession.
{{/SI_DONATION_HORS_PART}}

{{#SI_AVEC_CHARGE}}
### Charges imposées au donataire
Le donataire s'engage à : {{DETAIL_CHARGE}}

(exemples : verser une rente viagère au donateur, prendre soin du donateur, conserver le bien dans la famille pendant X ans)
{{/SI_AVEC_CHARGE}}

---

## ARTICLE 3 — DROITS D'ENREGISTREMENT

Conformément à la loi modifiée du 7 août 1920 :

| Lien | Taux | Calcul |
|---|---|---|
| {{LIEN_PARENTE}} | {{TAUX_DROITS}} % | {{VALEUR_CHIFFRES}} × {{TAUX_DROITS}} % = {{DROITS_DUS}} € |

{{#SI_BIEN_IMMOBILIER}}
+ Droit de transcription : {{VALEUR_CHIFFRES}} × 1 % = {{TRANSCRIPTION}} €
{{#SI_LUX_VILLE}}+ Surtaxe communale Luxembourg-Ville : 50 % du droit d'enregistrement = {{SURTAXE}} €{{/SI_LUX_VILLE}}
{{/SI_BIEN_IMMOBILIER}}

**Total droits dus** : {{TOTAL_DROITS}} €

Les droits sont à la charge du **{{QUI_PAIE_DROITS}}** (par défaut : donataire).

---

## ARTICLE 4 — IRRÉVOCABILITÉ

La présente donation est, conformément à l'art. 894 du Code civil, **irrévocable** entre les parties (sauf cas légaux limités : ingratitude, inexécution des charges, naissance d'enfant postérieure pour donation entre époux).

---

## ARTICLE 5 — ACCEPTATION

Le DONATAIRE déclare **accepter** la présente donation conformément à l'art. 932 du Code civil.

---

## ARTICLE 6 — FRAIS

Les frais, droits et émoluments du présent acte seront supportés par : **{{QUI_PAIE_FRAIS}}**.

---

## ARTICLE 7 — DÉCLARATIONS FISCALES

Les parties déclarent avoir été informées :
- Des conséquences fiscales de la donation (droits dus, rapport éventuel à succession)
- De la règle des 12 mois (donations dans l'année précédant le décès rapportées)
- De l'irrévocabilité de l'acte

---

## DONT ACTE

Lecture faite, les comparants ont signé avec le notaire le présent acte.

Fait et passé à {{LIEU}}, à l'étude du notaire instrumentant, l'an et jour ci-dessus.

| Le DONATEUR | Le DONATAIRE | Le NOTAIRE |
|---|---|---|
| | | |
| {{NOM_DONATEUR}} | {{NOM_DONATAIRE}} | Maître {{NOM_NOTAIRE}} |

---

> **⚠️ MODÈLE INDICATIF** — Tout acte de donation doit être rédigé par un notaire qui adapte les clauses à la situation patrimoniale et familiale du donateur. Modèle non opposable aux tiers.
