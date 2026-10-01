---
name: legal-complaint-letter-writer-khalilbenaz
title: Complaint Letter Writer
description: Rédige une lettre de réclamation formelle pour un litige consommateur, administratif ou professionnel. Se déclenche aussi avec "lettre de réclamation", "plainte", "mise en demeure", "je veux me plaindre", "courrier formel", ou toute rédaction de contestation officielle. Also triggers on "complaint letter", "formal letter of dispute", "write to customer service".
author: khalilbenaz
author_url: https://github.com/khalilbenaz/claude-skills-collection/tree/main/skills/legal-complaint-letter-writer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: consumer
language: fr
---

# Complaint Letter Writer

> Ce skill génère des modèles de courriers. Pour les litiges importants (montants élevés, licenciement, procédure judiciaire), faites relire par un avocat ou une association de consommateurs avant envoi.

---

## Étape 1 — Collecter les informations nécessaires

Demande systématiquement :

| Information | Pourquoi |
|---|---|
| Destinataire exact (nom, adresse, service) | Cibler la bonne entité juridique |
| Objet du litige (produit, prestation, décision) | Cadrer la réclamation |
| Chronologie des faits (dates précises) | Établir la preuve |
| Démarches déjà effectuées (appels, emails) | Montrer la bonne foi |
| Références disponibles (n° de commande, contrat, facture) | Identifier le dossier |
| Résultat attendu (remboursement, remplacement, annulation) | Formuler une demande précise |
| Pays / juridiction | Adapter la base légale |

---

## Étape 2 — Choisir le niveau de la lettre

### Niveau 1 — Réclamation amiable (premier contact)
Ton poli mais ferme. Pas de mention de recours judiciaires. Délai de réponse suggéré : **15 jours**.

Utiliser quand :
- Aucune démarche préalable n'a été faite
- La relation commerciale peut être préservée
- Le litige est simple (erreur de facturation, retard de livraison)

### Niveau 2 — Lettre formelle de réclamation
Ton formel. Mention des droits légaux et d'une escalade possible. Délai : **8 jours**.

Utiliser quand :
- Une réclamation amiable est restée sans réponse
- Le préjudice est établi et documenté

### Niveau 3 — Mise en demeure
Ton juridique. Mention explicite des recours (tribunal, médiateur, signalement DGCCRF). Délai : **8 jours francs**.

Utiliser quand :
- Les deux premiers niveaux ont échoué
- Le montant ou le préjudice justifie une procédure
- Document qui peut servir de pièce en justice

---

## Étape 3 — Structure de la lettre (template)

```
[Prénom NOM]
[Adresse complète]
[Email / Téléphone]

[Ville], le [date]

À l'attention de [Service concerné]
[Entreprise / Organisme]
[Adresse]

Lettre recommandée avec accusé de réception

Objet : Réclamation relative à [objet précis] — Réf. [n° dossier/commande]

Madame, Monsieur,

**Rappel des faits**
[Chronologie factuelle : date d'achat/contrat, description du problème, date de survenance]

**Démarches déjà effectuées**
[Contact du [date] par [moyen] — sans réponse / réponse insatisfaisante]

**Fondement de ma demande**
[Base légale : article L217-4 du Code de la consommation (garantie légale), article 1231-1 du Code civil (responsabilité contractuelle), clause X du contrat, etc.]

**Ma demande**
Je vous demande, dans un délai de [X] jours à compter de la réception de ce courrier :
- [Action précise : remboursement de X €, remplacement, correction, etc.]

À défaut de réponse satisfaisante dans ce délai, je me réserve le droit de saisir [médiateur compétent / tribunal judiciaire / autorité de contrôle].

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées.

[Signature]
[Pièces jointes : liste]
```

---

## Étape 4 — Bases légales fréquentes (France, 2026)

| Situation | Texte applicable |
|---|---|
| Produit défectueux | Art. L217-4 à L217-14 Code conso — garantie légale 2 ans |
| Prestation non conforme | Art. 1217 et 1231-1 Code civil — inexécution contractuelle |
| Remboursement refusé | Art. L224-25-22 Code conso (e-commerce), 14 jours légaux |
| Litige bancaire | Art. L316-1 Code monétaire et financier — médiation obligatoire |
| Employeur / travail | Art. L1237-19 Code du travail (rupture), lettres LRAR |
| Copropriété | Art. 42 loi du 10 juillet 1965 |
| Assurance | Art. L113-12 Code des assurances (résiliation), L133-2 |

---

## Étape 5 — Envoi et suivi

**Format papier :**
- Lettre recommandée avec avis de réception (LRAR) — preuve légale de réception
- Conserver une copie signée + le récépissé La Poste

**Format numérique :**
- Email avec demande d'accusé de lecture + confirmation de réception
- Service type "AR24" ou "Maileva" pour recommandé électronique (valeur juridique équivalente depuis 2022)

**Délais à surveiller :**
- Noter la date de réception (AR) — le délai court à partir de ce jour
- Sans réponse : passer au niveau supérieur ou saisir le médiateur sectoriel

**Recours si pas de réponse :**
1. Médiateur sectoriel (médiation de la consommation obligatoire pour les pros)
2. Signalement sur SignalConso (DGCCRF)
3. Justice de proximité (< 5 000 €) ou tribunal judiciaire
4. Associations : UFC-Que Choisir, 60 Millions de consommateurs

---

## Garde-fous et pièges courants

- **Ne jamais menacer sans intention** : "je vais poursuivre" sans suite affaiblit la position.
- **Éviter le ton agressif ou émotionnel** : les faits seuls sont convaincants ; les insultes invalident la lettre.
- **Pas de fausses références légales** : vérifier l'article cité avant de l'inclure.
- **Ne pas demander plusieurs choses contradictoires** : une demande principale, une alternative.
- **Délai trop court** : moins de 8 jours est rarement considéré comme raisonnable par les tribunaux.
- **Pièces jointes non citées** : lister chaque document joint dans le corps de la lettre.
- **Signature manquante** : une lettre non signée n'a pas de valeur probante.
- **Mise en demeure trop tôt** : pour les petits litiges, un premier contact amiable évite l'escalade inutile.


## Communication Rules

- Clear and concise; skip filler, but never at the cost of warmth.
- Warm, respectful, non-judgmental tone — meet the person where they are.
- Lead with what matters to the user; avoid unnecessary preamble.
- Plain language; explain only what genuinely helps.
- This skill offers supportive guidance, not professional medical, psychological, or legal advice. Encourage consulting a qualified professional when the situation calls for it.
- No emoji unless the user uses them first.
