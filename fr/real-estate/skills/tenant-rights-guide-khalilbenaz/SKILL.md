---
name: tenant-rights-guide-khalilbenaz
title: Tenant Rights Guide
description: Informe sur les droits du locataire dans une situation donnée. Se déclenche aussi avec "droits du locataire", "mon propriétaire", "augmentation de loyer", "état des lieux", "expulsion", "dépôt de garantie", ou toute question de droit locatif. Also triggers on "tenant rights", "landlord dispute", "rent increase rules".
author: khalilbenaz
author_url: https://github.com/khalilbenaz/claude-skills-collection/tree/main/legal-skills/tenant-rights-guide
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: real-estate
language: fr
---

# Tenant Rights Guide

> Ce guide fournit des informations générales à titre éducatif. Le droit locatif est territorial et évolue fréquemment. Pour toute action juridique, consultez un juriste, une ADIL (France), ou une association de locataires de votre région.

---

## Étape 1 — Qualifier la situation

Avant toute réponse, collecte les éléments essentiels :

| Information | Exemples |
|---|---|
| Pays / région | France (loi Alur), Belgique, Maroc, Tunisie… |
| Type de bail | Résidence principale, meublé, étudiant, commercial |
| Durée dans le logement | < 3 mois, 1 an, 5 ans… |
| Problème exact | Loyer, travaux, restitution caution, expulsion, nuisances… |
| Actions déjà tentées | Aucune, mail envoyé, courrier RAR, conciliation… |

Si l'utilisateur n'a pas donné ces éléments, pose les questions ciblées avant de continuer.

---

## Étape 2 — Identifier les droits applicables

### Thèmes fréquents (France — loi du 6 juillet 1989 et loi Alur 2014)

**Dépôt de garantie**
- Logement vide : 1 mois de loyer hors charges maximum.
- Meublé : 2 mois maximum.
- Délai de restitution : 1 mois si état des lieux de sortie conforme, 2 mois sinon.
- Sanction retard : majoration de 10 % du loyer mensuel par mois de retard.

**Augmentation de loyer**
- En zone tendue : encadrement strict (IRL + plafond légal).
- Hors zone tendue : révision annuelle possible uniquement si clause dans le bail, indexée sur l'IRL (Indice de Référence des Loyers).
- Augmentation abusive = refus motivé par écrit dans le mois suivant la notification.

**État des lieux**
- Obligatoire à l'entrée ET à la sortie, signé par les deux parties.
- Désaccord à l'entrée : possible de compléter dans les 10 jours suivant remise des clés.
- Absence d'état des lieux d'entrée : présomption de bon état en faveur du locataire.

**Travaux et décence**
- Le logement doit respecter les critères de décence (surface minimale 9 m², chauffage, étanchéité…).
- Travaux urgents (fuite, chauffage en hiver) : le propriétaire doit intervenir dans un délai raisonnable.
- Refus ou inaction : mise en demeure, puis saisine de la CAF ou du tribunal judiciaire.

**Expulsion**
- Aucune expulsion sans décision judiciaire.
- Trêve hivernale (France) : du 1er novembre au 31 mars — aucune expulsion possible.
- Coupure d'eau, de gaz ou d'électricité par le propriétaire = voie de fait, illégale.

---

## Étape 3 — Actions concrètes par escalade

Respecte cet ordre : chaque étape doit être tentée avant la suivante.

### 1. Contact amiable (oral puis écrit simple)
- Email avec accusé de lecture ou SMS : trace écrite légère.
- Délai raisonnable à donner : 8 à 15 jours selon l'urgence.

### 2. Mise en demeure par lettre recommandée avec AR (LRAR)
- Obligatoire avant tout recours juridique.
- Modèle type (voir Étape 4).
- Délai à fixer dans le courrier : 8 jours (urgent) à 1 mois.

### 3. Recours amiable / médiation
- **ADIL** (France) : consultation gratuite en ligne ou en présentiel.
- **Commission départementale de conciliation (CDC)** : saisie gratuitement, obligatoire avant certains tribunaux.
- **Conciliateur de justice** : gratuit, disponible en mairie.

### 4. Recours administratif / organismes
- **CAF** : signalement logement indécent (peut suspendre APL au propriétaire).
- **DDETS / préfecture** : pour les manquements graves (décence, insalubrité).
- **Défenseur des droits** : discrimination dans l'accès au logement.

### 5. Recours judiciaire
- **Tribunal judiciaire** (ex-TI) pour litiges locatifs.
- En ligne via [justice.fr](https://www.justice.fr) pour saisine sans avocat jusqu'à 10 000 €.
- Aide juridictionnelle possible sous conditions de ressources.

---

## Étape 4 — Modèles de courriers

### Mise en demeure — non-restitution du dépôt de garantie

```
[Prénom Nom Locataire]
[Adresse]
[Ville, Date]

Madame, Monsieur [Nom propriétaire],
[Adresse propriétaire]

Lettre recommandée avec accusé de réception

Objet : Mise en demeure — Restitution du dépôt de garantie

Madame, Monsieur,

J'ai quitté le logement situé [adresse] le [date], après remise des clés et réalisation de
l'état des lieux de sortie. À ce jour, soit plus de [1 ou 2] mois après mon départ, vous
n'avez pas restitué le dépôt de garantie d'un montant de [montant] €.

Conformément à l'article 22 de la loi du 6 juillet 1989, je vous mets en demeure de me
restituer cette somme dans un délai de 8 jours à compter de la réception de ce courrier.

Passé ce délai, je me réserve le droit de saisir la commission de conciliation compétente
ou le tribunal judiciaire, et de réclamer une majoration de 10 % par mois de retard.

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées.

[Signature]
```

### Mise en demeure — travaux urgents non réalisés

```
Objet : Mise en demeure — Réalisation de travaux urgents

Je vous informe qu'un problème de [description : fuite, chauffage défaillant…] affecte le
logement depuis le [date du signalement]. Malgré mes relances du [dates], aucune
intervention n'a été effectuée.

Je vous mets en demeure de faire réaliser ces travaux dans un délai de 8 jours.

À défaut, je saisirai le tribunal judiciaire pour obtenir leur exécution sous astreinte, et
réclamerai une réduction de loyer proportionnelle à la période de trouble de jouissance.
```

---

## Étape 5 — Ressources et organismes

| Organisme | Usage | Accès |
|---|---|---|
| ADIL (France) | Conseil juridique gratuit | adil.org |
| CNL / CLCV | Associations de locataires | cnl.asso.fr |
| Service-Public.fr | Fiches pratiques officielles | service-public.fr |
| justice.fr | Saisine en ligne tribunal | justice.fr |
| CAF | Logement indécent, APL | caf.fr |
| Maison de Justice | Aide gratuite de proximité | Via mairie |

---

## Garde-fous et pièges fréquents

- **Ne pas envoyer de SMS comme seule preuve** : le propriétaire peut les nier. Toujours doubler d'un email ou d'un LRAR.
- **Ne pas quitter le logement sans état des lieux de sortie** : sans lui, le propriétaire peut retenir toute la caution.
- **Ne pas accepter de paiement partiel sans réserves écrites** : cela peut valoir quittance.
- **Ne pas confondre charges récupérables et charges non récupérables** : le décret du 26 août 1987 liste ce qui est imputable au locataire.
- **Ne jamais cesser de payer le loyer sans décision judiciaire** : même en cas de litige, l'impayé crée un motif d'expulsion valable.
- **Attention aux délais de prescription** : 3 ans pour les loyers impayés, 3 ans pour la restitution du dépôt de garantie (à compter de la date de restitution théorique).

---

## Bonnes pratiques 2026

- Conserver une copie numérique datée de tout document (bail, états des lieux, quittances) dans un cloud personnel.
- Photographier le logement à l'entrée ET à la sortie avec horodatage automatique.
- Pour les échanges sensibles, utiliser un service d'email certifié (ex : AR24, LRE) qui a valeur légale équivalente au LRAR papier.
- En cas de bail numérique, vérifier la conformité de la signature électronique (eIDAS niveau avancé minimum).
- Consulter l'ADIL locale avant d'agir : 30 minutes gratuites évitent souvent des erreurs coûteuses.
