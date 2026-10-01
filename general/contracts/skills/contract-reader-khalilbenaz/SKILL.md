---
name: contract-reader-khalilbenaz
title: Contract Reader
description: Analyse un contrat en langage simple, identifie les clauses importantes et les points de vigilance. Se déclenche aussi avec "lire ce contrat", "analyser un contrat", "clause", "conditions générales", "CGV", "bail", ou toute demande de compréhension d'un document contractuel. Also triggers on "review this contract", "explain contract clauses", "what am I signing".
author: khalilbenaz
author_url: https://github.com/khalilbenaz/claude-skills-collection/tree/main/legal-skills/contract-reader
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: fr
---

# Contract Reader

> ⚠️ Cette analyse est informative et ne constitue pas un avis juridique. Pour tout contrat à enjeu significatif (bail commercial, CDI, cession, partenariat), consultez un avocat ou un juriste qualifié avant de signer.

---

## Étape 1 — Identification du type et du contexte

Avant toute analyse, préciser :

- **Type de contrat** : bail (habitation / commercial), contrat de travail (CDI/CDD/freelance), prestation de services, vente, licence logicielle, NDA, assurance, abonnement SaaS, CGV/CGU, cession de droits…
- **Parties** : qui signe quoi ? quelle est la partie la plus forte économiquement ?
- **Droit applicable** : droit français, OHADA, droit de l'UE, droit étranger ?
- **Enjeu** : montant, durée, réversibilité — cela calibre le niveau de vigilance nécessaire.

Si le document n'est pas fourni, demander de le coller en texte ou d'en partager les extraits clés.

---

## Étape 2 — Résumé exécutif (langage simple)

En 5 à 8 lignes maximum :

- Ce que chaque partie s'engage à faire
- La durée et la date d'entrée en vigueur
- Le prix / la contrepartie
- Les conditions de sortie en un mot

Exemple de sortie attendue :

> "Ce contrat vous engage à livrer une application mobile d'ici le 31 mars 2027 pour 40 000 € HT, en 3 jalons. La société X peut résilier à tout moment avec 15 jours de préavis, mais vous ne pouvez résilier qu'en cas de défaut de paiement prouvé. La propriété intellectuelle reste à X dès le paiement de chaque jalon."

---

## Étape 3 — Tableau d'analyse par clause

Analyser chaque section significative selon ce format :

| # | Clause / Article | Ce qu'elle dit (simple) | Favorable · Neutre · Défavorable | Point de vigilance |
|---|-----------------|------------------------|----------------------------------|--------------------|
| 1 | Durée et renouvellement | Contrat de 12 mois, renouvellement tacite si non-dénoncé 3 mois avant | Défavorable | Délai de préavis court — mettre un rappel agenda |
| 2 | Clause de confidentialité | NDA 5 ans post-contrat, périmètre très large | Défavorable | Vérifier si elle couvre vos projets personnels |
| 3 | Prix et révision | Prix fixe, pas d'indexation | Neutre | OK sur courte durée, risqué > 2 ans |

Colonnes à respecter — ne pas simplifier outre mesure ni inventer des données.

---

## Étape 4 — Points critiques à vérifier systématiquement

Passer en revue chaque point, même si non mentionné dans le contrat (l'absence est parfois un risque) :

### Obligations et responsabilités
- Obligations de résultat vs. obligations de moyens (différence juridique majeure)
- Garanties données et leur étendue
- Plafond de responsabilité — existe-t-il ? est-il raisonnable ?

### Durée et sortie
- Date de début effective (signature ? livraison ? paiement ?)
- Renouvellement tacite : **délai de préavis exact** et **mode de notification** (recommandé AR ?)
- Clause de résiliation anticipée : pénalités ? indemnités ? motifs acceptables ?

### Clauses financières
- Conditions de paiement et pénalités de retard (taux, délai)
- Clause de révision de prix ou d'indexation (ex. indice ICC, ILAT)
- Clause de remboursement ou d'avoir en cas de résiliation

### Propriété intellectuelle
- Qui détient les droits sur les livrables / créations ?
- Licence ou cession ? exclusive ou non ?
- Sort des éléments préexistants (code open source, outils internes)

### Clauses restrictives
- **Non-concurrence** : durée, périmètre géographique, secteur — est-elle contrepartie compensée ?
- **Non-sollicitation** : clients et/ou salariés ?
- **Exclusivité** : qui l'impose à qui ?

### Litige et juridiction
- Clause compromissoire (arbitrage) ou juridiction étatique ?
- Tribunal compétent : lieu, type (commercial, prud'hommes, civil)
- Droit applicable — quelle loi nationale ?

### Clauses souvent abusives (à signaler sans affirmer leur illégalité)
- Résiliation unilatérale sans motif en faveur d'une seule partie
- Limitation de responsabilité quasi-totale pour le prestataire dominant
- Modification unilatérale des tarifs sans préavis
- Cession de contrat sans accord de l'autre partie

---

## Étape 5 — Questions à poser avant de signer

Générer 5 à 8 questions concrètes adaptées au contrat analysé. Exemples de templates :

1. "Que se passe-t-il si je souhaite sortir du contrat après 6 mois — quels sont les frais exacts ?"
2. "La clause X (art. Y) signifie-t-elle que vous pouvez modifier le prix sans mon accord ?"
3. "Le renouvellement automatique peut-il être désactivé par email ou faut-il un courrier recommandé ?"
4. "Les droits sur les livrables me sont-ils transférés même en cas de litige en cours ?"
5. "La clause de non-concurrence s'applique-t-elle à mes activités actuelles chez d'autres clients ?"

---

## Étape 6 — Recommandation finale

Conclure par une synthèse à trois niveaux :

- **Signer tel quel** : si aucun point critique n'est identifié et l'enjeu est faible
- **Négocier les points suivants avant de signer** : liste des clauses à renégocier avec contre-proposition type
- **Consulter un avocat avant de signer** : si la valeur du contrat est élevée, si des clauses limitent fortement vos droits, ou si le droit applicable est incertain

---

## Garde-fous et anti-patterns

**Ne jamais faire :**
- Affirmer qu'une clause est illégale ou nulle — c'est une appréciation juridique qui nécessite un professionnel
- Analyser un contrat incomplet comme s'il était complet (signaler les lacunes)
- Ignorer les annexes et conditions générales — elles font partie du contrat

**Pièges fréquents :**
- Le "langage courant" d'un contrat peut avoir un sens technique différent (ex. "livraison" vs "mise à disposition")
- Un contrat "standard" peut inclure des clauses inhabituelles — lire chaque ligne
- Les renvois à d'autres documents (CGV, charte, politique de confidentialité) sont contractuels — demander ces documents

**Biais à éviter :**
- Ne pas rassurer excessivement : mieux vaut signaler un doute que minimiser un risque
- Ne pas sur-analyser un contrat simple (abonnement mensuel résiliable) au même niveau qu'un bail commercial

---

## Bonnes pratiques 2026

- **Contrats SaaS / IA** : vérifier les clauses d'utilisation des données pour entraînement de modèles et la portabilité des données
- **Contrats internationaux** : vérifier la conformité RGPD si transfert de données hors UE (clauses contractuelles types SCCs)
- **Contrats de prestation freelance** : depuis la loi PACTE et ses décrets, vérifier la présomption de salariat dans les secteurs réglementés
- **Baux commerciaux** : indexation ILAT ou ILC selon le secteur — bien vérifier l'indice contractualisé
- **Archivage** : conseiller de conserver le contrat signé + échanges email associés pendant toute la durée + 5 ans minimum
