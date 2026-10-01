# Succession au Luxembourg — guide notarial

## 1. Régime successoral

### Sources
- **Code civil luxembourgeois** (livre III, titre I — successions)
- **Loi du 27 décembre 1817** sur les successions
- **Règlement (UE) 650/2012** sur les successions internationales (depuis 17 août 2015)

### Principes
- Application de la loi du **dernier domicile habituel** du défunt (sauf option pour la loi nationale via testament)
- Réserve héréditaire au profit des descendants en ligne directe

## 2. Dévolution légale (sans testament)

### Ordre des héritiers
1. **Descendants** (enfants, petits-enfants par représentation)
2. **Ascendants privilégiés** (parents) + frères/sœurs et leurs descendants
3. Ascendants ordinaires (grands-parents, etc.)
4. Collatéraux ordinaires (oncles, tantes, cousins)

### Conjoint survivant
- En présence d'enfants : **usufruit** sur tous les biens OU **1/4 en pleine propriété** (au choix du conjoint)
- En présence des seuls parents/frères : usufruit OU pleine propriété sur quote-part
- Sans héritier : recueille toute la succession

### Partenaire (PACS lux)
- Régime depuis loi du 9 juillet 2004 (art. 14)
- **PAS d'héritier réservataire** par défaut
- Testament fortement recommandé pour léguer au partenaire
- Effet fiscal : assimilation au mariage (cf. droits de succession)

## 3. Réserve héréditaire

Quote-part du patrimoine **incompressible** revenant aux descendants :

| Nombre d'enfants | Réserve | Quotité disponible |
|---|---|---|
| 1 enfant | 1/2 | 1/2 |
| 2 enfants | 2/3 | 1/3 |
| 3 enfants ou plus | 3/4 | 1/4 |

**Quotité disponible** : part dont le défunt peut disposer librement par testament ou donation.

⚠️ Au Luxembourg, **pas de réserve pour le conjoint** ni pour les ascendants depuis 2007.

## 4. Testament

### Formes admises
1. **Testament olographe** : entièrement écrit, daté, signé de la main du testateur
2. **Testament authentique** : reçu par notaire en présence de 2 témoins
3. **Testament mystique** : remis cacheté au notaire

### Testament olographe — points d'attention
- **Aucune validité** sans :
  - Écriture entière de la main du testateur
  - Date complète (jour, mois, année)
  - Signature
- À déposer pour conservation chez un notaire (recommandé)
- Inscription au **Fichier Central des Dispositions de Dernières Volontés (FCDDV)**

### Donation entre époux (Hartwig)
- Acte notarié spécifique
- Permet d'augmenter les droits du conjoint au-delà du minimum légal
- Choix entre 3 options (1/4 PP + 3/4 usufruit, etc.)

## 5. Droits de succession

Cf. `data/abattements-succession.json` pour le détail complet.

### Principe phare lux : EXONÉRATION en ligne directe

✅ **Pas de droits de succession** entre :
- Parents ↔ enfants (sur la part légale)
- Époux/partenaires (sur la part légale)
- Grands-parents ↔ petits-enfants

→ Le Luxembourg est l'une des juridictions **les plus favorables d'Europe**.

### Imposition de la part dépassant la réserve
Si testament avantage un héritier au-delà de sa réserve :
- **2,5 %** sur préciput (clause d'avantage matrimonial)
- **5 %** sur legs particuliers

### Lignes collatérales et étrangers
| Bénéficiaire | Taux base |
|---|---|
| Frères, sœurs | 6 % |
| Oncles, tantes, neveux, nièces | 9 % |
| Grands-oncles, grands-neveux | 10 % |
| Étrangers | 15 % |

+ **majoration progressive** selon montant de la part nette (jusqu'à 140 %).

### Exemple — neveu héritant 80 000 €
```
Taux base : 9 %
Majoration tranche 75-100k : 60 %
Taux effectif : 9 % × 1,60 = 14,4 %
Droits : 80 000 × 14,4 % = 11 520 €
```

## 6. Procédure de règlement

### Étape 1 — Décès et formalités initiales (J+0 à J+15)
- **Déclaration de décès** à la commune (≤ 24h)
- Obtention d'extraits d'acte de décès
- Recherche du **testament** (FCDDV via notaire)
- **Inventaire informel** des actifs/passifs
- **Blocage des comptes bancaires** du défunt (banque sur notification)

### Étape 2 — Acte de notoriété (1 à 2 mois)
- Établi par notaire
- Identifie les héritiers, leur lien de parenté, leur quote-part
- Permet de débloquer comptes bancaires, agir auprès des tiers
- Honoraires notaire : 300-600 € HT

### Étape 3 — Acceptation / renonciation
Chaque héritier peut :
- **Accepter purement et simplement** (devient propriétaire des biens ET responsable des dettes sur son patrimoine personnel)
- **Accepter sous bénéfice d'inventaire** (responsable seulement à hauteur de l'actif net) — déclaration au tribunal
- **Renoncer** à la succession (perd les biens, n'est pas tenu des dettes) — déclaration au greffe

Délai pour décision : pas de strict, mais usage = avant déclaration succession (6 mois).

### Étape 4 — Inventaire (le cas échéant)
- Obligatoire si :
  - Acceptation sous bénéfice d'inventaire
  - Héritier mineur ou incapable
  - Demande d'un héritier
- Réalisé par notaire — coût ~0,5 % de l'actif

### Étape 5 — Déclaration de succession (≤ 6 mois après décès)
- Dépôt au **bureau d'enregistrement de l'AED** compétent (résidence du défunt)
- Formulaire AED + annexes :
  - Acte de notoriété
  - Liste des actifs et passifs avec valeurs
  - Calcul des parts et droits dus
- **Prolongation possible** sur demande motivée (3-6 mois supplémentaires)

### Étape 6 — Paiement des droits
- À l'AED dans le délai de la déclaration
- Intérêts de retard 0,6 %/mois après échéance
- Possibilité de paiement différé / fractionné sur demande

### Étape 7 — Liquidation et partage
- **Partage amiable** entre héritiers (acte notarié si immobilier)
- OU **partage judiciaire** si désaccord (tribunal d'arrondissement)

## 7. Patrimoine et passif déductible

### Actifs taxables
- Immeubles
- Comptes bancaires, titres, espèces
- Véhicules, meubles, bijoux, œuvres d'art
- Créances sur tiers
- Parts sociales, actions
- Assurances-vie (sous conditions)

### Pour résidents : patrimoine mondial
### Pour non-résidents : seuls les **immeubles situés au Luxembourg**

### Passif déductible
- Dettes du défunt à la date du décès
- Frais funéraires raisonnables
- Frais de dernière maladie
- Impôts dus (IRPP année N)
- Honoraires notaire pour règlement succession

## 8. Spécificités assurance-vie

### Régime fiscal
- Capital décès versé au **bénéficiaire désigné** : généralement **hors succession**
- Exception : primes manifestement exagérées par rapport aux facultés du défunt → réintégration

### Recommandation
- Désignation claire du bénéficiaire dans le contrat
- Mise à jour en cas de changement de situation familiale
- Échange régulier avec assureur

## 9. Successions internationales

### Règlement UE 650/2012
- Loi applicable = loi du dernier **domicile habituel** du défunt
- Possibilité de choix de la **loi nationale** dans le testament
- **Certificat successoral européen (CSE)** délivré par le notaire — vaut acte de notoriété dans toute l'UE

### Conventions bilatérales
- Belgique-Luxembourg (1931) : éviter double imposition droits succession
- France-Luxembourg : pas de convention spécifique successions

### Cas du défunt résident lux avec biens à l'étranger
- Patrimoine mondial taxable au Lux (avec exonération immeubles étrangers)
- Mais vérifier convention applicable / risque double imposition

## 10. Donations du vivant et anticipation

### Donations notariées
- Soumises à droits de donation (cf. droits-enregistrement.json)
- **Ligne directe descendants : 1,8 %**
- Non rapportables après 12 mois précédant le décès

### Avantages
- Réduit la base de calcul des droits succession
- Permet de planifier la transmission
- Conserve l'usufruit (donation avec réserve d'usufruit)

### Donation-partage
- Acte notarié unique répartissant entre tous les enfants
- Évite contestations futures
- Évalue les biens au jour de la donation (gain en cas de plus-value ultérieure)

## 11. Liens utiles

- Chambre des Notaires : https://www.notariat.lu/
- AED — successions : https://pfi.public.lu/fr/professionnels/successions.html
- Guichet — décès et succession : https://guichet.public.lu/fr/citoyens/famille/deces-succession.html
- Code civil lux : https://eli.legilux.public.lu/eli/etat/code/code_civil
- Règlement UE 650/2012 : https://eur-lex.europa.eu/eli/reg/2012/650/oj
