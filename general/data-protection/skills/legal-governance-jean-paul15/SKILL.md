---
name: legal-governance-jean-paul15
title: Légal & gouvernance — ne jamais l'oublier, ne jamais trancher seul
description: Dimension légale et gouvernance du développement — licences du projet et des dépendances, données personnelles (RGPD/CCPA — minimisation, base légale, consentement, conservation, sous-traitants), accessibilité légale, réglementation IA, traçabilité des décisions, propriété du code, approbations. À utiliser dès qu'on ajoute une dépendance, collecte ou transmet des données personnelles, intègre un tiers, ajoute une fonction IA, ou prend une décision qui engage le projet.
author: Jean-Paul15
author_url: https://github.com/Jean-Paul15/claude-eng-framework/tree/main/core/skills/legal-governance
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: fr
---

# Légal & gouvernance — ne jamais l'oublier, ne jamais trancher seul

L'agent n'est pas juriste : il **détecte, documente et escalade**. Les décisions légales appartiennent à l'humain
(catégorie « approbation humaine » du framework).

## Licences
- Le projet a-t-il une licence déclarée ? Sinon : le signaler une fois (décision humaine : propriétaire vs open source).
- **Nouvelle dépendance** : vérifier sa licence avant l'ajout. Copyleft fort (GPL, AGPL, SSPL, EUPL) dans un projet
  non-GPL ou distribué/SaaS → **approbation humaine**. Copyleft faible (LGPL, MPL) : vérifier les obligations.
  Licence absente ou « source-available » (BUSL…) : le signaler. La gate `compliance` fait un contrôle npm automatique.
- Ne pas copier de code d'une source dont la licence est incompatible ou inconnue ; attribution quand elle est requise
  (fichier NOTICE / THIRD_PARTY).

## Données personnelles (RGPD et équivalents)
Pour toute nouvelle donnée personnelle collectée, stockée ou transmise :
- **Minimisation** : est-elle nécessaire ? **Base légale / consentement** (cookies et analytics : consentement préalable en UE).
- **Conservation** : durée définie et suppression effective ; droits d'accès, rectification, effacement, portabilité.
- **Sous-traitants / transferts** : envoi à un tiers (analytics, email, IA, paiement) → le lister ; transfert hors UE à signaler.
- **Sécurité** : chiffrement en transit, accès restreint, pas de données personnelles dans les logs.
- Nouvelle catégorie de données ou nouveau sous-traitant → **approbation humaine** + mise à jour de la politique de confidentialité.

## Autres obligations à signaler (pas à interpréter)
- Accessibilité : WCAG 2.2 AA est aussi une obligation légale dans de nombreux contextes (ex. European Accessibility Act).
- IA : transparence envers l'utilisateur, données envoyées au fournisseur, conditions d'usage du fournisseur, EU AI Act selon l'usage.
- Paiements : PCI DSS (ne jamais stocker de numéros de carte ; utiliser les solutions hébergées du prestataire).
- Santé, finance, mineurs, export de cryptographie : domaines réglementés → signaler systématiquement.

## Gouvernance
- **Traçabilité** : décision structurante → ADR (`node .ceng/runtime/cli.js decision add …`) ; dérogation de gate → justifiée.
- **Propriété** : respecter CODEOWNERS ; ne pas modifier LICENSE, CODEOWNERS, SECURITY.md, ni les garde-fous sans approbation.
- **Audit** : le journal `.ceng/logs/events.jsonl` et les rapports permettent de reconstituer qui a fait quoi et pourquoi.
- **Approbations** : déploiement, données, infra, secrets, licences → humain, quelle que soit l'autonomie configurée.
