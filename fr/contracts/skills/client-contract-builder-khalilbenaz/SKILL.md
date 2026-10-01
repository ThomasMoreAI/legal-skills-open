---
name: client-contract-builder-khalilbenaz
title: Client Contract Builder
description: Aide à rédiger des contrats de prestation freelance avec les clauses essentielles, CGV et protection de la propriété intellectuelle. Se déclenche avec "contrat freelance", "CGV freelance", "clause", "propriété intellectuelle", "contrat prestation". Also triggers on "freelance contract", "client agreement", "terms and conditions".
author: khalilbenaz
author_url: https://github.com/khalilbenaz/claude-skills-collection/tree/main/freelance-skills/client-contract-builder
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: contracts
language: fr
---

# Client Contract Builder

## Critères de choix du type de contrat

| Situation | Type recommandé |
|---|---|
| Mission courte, scope figé | Contrat au forfait |
| Mission longue / incertaine | Régie (TJM) + bon de commande mensuel |
| Plusieurs missions récurrentes | Contrat-cadre + bons de commande |
| Partage d'informations confidentielles avant signature | NDA préalable |
| Sous-traitance pour un client final tiers | Contrat de sous-traitance (mentionner le donneur d'ordre) |

---

## Workflow en 8 étapes

### 1. Collecter les informations préalables

Demander systématiquement :
- Identité juridique complète des deux parties (raison sociale, forme juridique, SIRET/RC, adresse)
- Type et durée estimée de la mission
- TJM ou montant forfaitaire, devise
- Date de début et jalons prévus
- Livrables attendus et critères d'acceptation
- Existence d'un NDA ou d'un contrat-cadre déjà signé

### 2. Rédiger l'objet et le périmètre

L'objet doit être précis et délimité. Exemple :

```
OBJET : Développement d'une API REST Node.js permettant la gestion des paiements en ligne
pour le compte du Client. Inclus : conception, développement, tests unitaires, livraison
d'un code source documenté. Exclus : hébergement, maintenance corrective post-livraison,
migrations de données.
```

Toujours lister explicitement ce qui est **exclu** pour éviter le scope creep.

### 3. Clauses financières

Modèle de section paiement (forfait) :

```
PRIX : Le montant total de la prestation est fixé à [X] € HT.
FACTURATION : Facture émise à la signature (30%), à mi-parcours (40%), à la livraison (30%).
PAIEMENT : 30 jours net date de facture.
PÉNALITÉS : Tout retard de paiement entraîne l'application de pénalités au taux de 3× le
taux légal en vigueur, exigibles sans mise en demeure préalable. Indemnité forfaitaire pour
frais de recouvrement : 40 € (art. L441-10 C.Com.).
```

Pour la régie (TJM) :

```
TJM : [X] € HT/jour ouvré. Le nombre de jours est validé mensuellement via bon de commande.
DÉPASSEMENT : Tout jour supplémentaire fait l'objet d'un avenant ou d'un bon de commande
complémentaire signé avant exécution.
```

### 4. Livrables, jalons et PV de recette

- Définir chaque livrable avec son format de sortie (ex: repo Git privé, dossier ZIP, accès Figma).
- Préciser le délai de validation client (ex: **10 jours ouvrés**) — passé ce délai, la validation est réputée acquise.
- Joindre un modèle de PV de recette minimaliste :

```
PV DE RECETTE — [Nom du livrable] — [Date]
Prestataire : [Nom]  /  Client : [Nom]
Le Client déclare avoir reçu et validé les livrables définis à l'article X.
Signature : ___________  Date : ___________
```

### 5. Propriété intellectuelle

Clause recommandée (cession conditionnelle au paiement) :

```
PROPRIÉTÉ INTELLECTUELLE : Le Prestataire conserve tous les droits de propriété intellectuelle
sur les développements réalisés jusqu'au paiement intégral de la prestation. À compter du
paiement complet, il cède au Client, à titre exclusif, les droits patrimoniaux d'exploitation
(reproduction, représentation, adaptation) pour tout territoire et toute la durée légale de
protection.

RÉSERVE : Le Prestataire conserve ses droits sur les briques génériques (bibliothèques internes,
snippets réutilisables, frameworks maison) préexistantes au contrat. Une licence d'utilisation
non-exclusive et irrévocable est accordée au Client sur ces composants dans le cadre de la
prestation.
```

### 6. Clauses de protection obligatoires

**Limitation de responsabilité :**
```
Le Prestataire ne peut être tenu responsable de dommages indirects ou immatériels (perte
de chiffre d'affaires, perte de données). Sa responsabilité directe est plafonnée au montant
total HT facturé au titre du présent contrat.
```

**Confidentialité :**
```
Chaque partie s'engage à garder strictement confidentiels les informations échangées pendant
et 3 ans après la fin du contrat. Exception : informations déjà publiques ou reçues d'un tiers.
```

**Non-sollicitation :**
```
Pendant la mission et 12 mois après, le Client s'interdit de recruter ou solliciter directement
les collaborateurs du Prestataire ayant participé à la mission. En cas de violation : indemnité
forfaitaire = 6 mois de TJM du collaborateur concerné.
```

**Résiliation :**
```
Chaque partie peut résilier le contrat avec un préavis de [15/30] jours calendaires par écrit.
En cas de résiliation à l'initiative du Client, les travaux réalisés et validés sont facturés
au prorata. Les livrables en cours restent la propriété du Prestataire jusqu'au paiement.
```

### 7. CGV — structure minimale

Les CGV doivent être annexées et acceptées **avant** la signature du contrat principal :

1. Identification du prestataire (SIRET, TVA intracommunautaire, RCS)
2. Champ d'application
3. Conditions de commande et de devis
4. Prix et conditions de paiement
5. Modalités de livraison et d'acceptation
6. Propriété intellectuelle (renvoie au contrat si spécifique)
7. Garanties et responsabilités
8. Données personnelles (RGPD — responsable de traitement, durée de conservation)
9. Médiation et droit applicable (droit français, tribunal compétent)

### 8. Relecture et envoi

- Utiliser [DocuSign](https://www.docusign.com), [Yousign](https://yousign.com) ou [Signaturit](https://www.signaturit.com) pour signature électronique (valeur légale en France).
- Conserver une copie signée au format PDF archivé ≥ 5 ans.
- Pour les contrats > 5 000 € ou avec clause d'exclusivité, recommander une relecture par avocat spécialisé IT/PI.

---

## Garde-fous et anti-patterns

| Anti-pattern | Conséquence | Correction |
|---|---|---|
| Commencer la mission sans contrat signé | Zéro protection, litige impossible à prouver | Toujours bloquer le démarrage jusqu'à signature |
| Cession de PI sans paiement garanti | Le client utilise les livrables sans payer | Conditionner explicitement la cession au paiement intégral |
| Délai de validation client indéfini | Validation qui traîne, projet bloqué | Indiquer un délai limite (10 j ouvrés) + acceptation tacite |
| Pas de plafond de responsabilité | Exposition à des dommages dépassant le CA | Plafonner à 100% du montant HT facturé |
| CGV non transmises avant commande | CGV inopposables au client | Transmettre + obtenir un accusé de réception écrit |
| NDA après échange d'informations sensibles | Informations déjà divulguées, NDA sans effet | Signer le NDA avant tout briefing technique |
| Clause de non-concurrence trop large | Clause nulle (déséquilibre significatif) | Limiter à 12 mois, zone géographique ou secteur précis |

---

## Bonnes pratiques 2026

- **Signature électronique qualifiée eIDAS** : préférer ce niveau pour les contrats > 10 000 € (Yousign qualifié, DocuSign Advanced).
- **RGPD / DPA** : si la mission implique un accès à des données personnelles du client, annexer un DPA (Data Processing Agreement) — obligation légale depuis 2018, encore souvent oubliée.
- **IA et droits d'auteur** : si des livrables sont générés ou assistés par IA, préciser explicitement dans le contrat à qui appartiennent ces éléments et les outils utilisés (risque de contestation de la cession PI).
- **Indexation tarifaire** : intégrer une clause d'indexation annuelle sur l'indice SYNTEC pour les contrats longue durée.
- **Assurance RC Pro** : mentionner que le prestataire est couvert par une RC Pro et joindre une attestation d'assurance en annexe.
