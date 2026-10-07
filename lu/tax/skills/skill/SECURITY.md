# Politique de sécurité

## Versions supportées

Seule la dernière version mineure publiée est activement maintenue. Les
correctifs de sécurité sont appliqués sur la branche `main` et publiés dans
une release patch.

| Version | Supportée |
|---------|-----------|
| 0.7.x   | ✅        |
| < 0.7   | ❌        |

## Signaler une faille

**Ne créez pas d'issue publique pour signaler une faille de sécurité.**

Merci de signaler les vulnérabilités en privé via l'un de ces canaux :

1. **GitHub Security Advisories** — recommandé :
   https://github.com/gregherbe76/Luxembourg-Paperasse/security/advisories/new
2. **Email** : gregherbe76@users.noreply.github.com

Merci d'inclure dans votre signalement :

- Une description claire de la faille
- Les étapes pour la reproduire
- L'impact estimé (fuite de données, exécution de code, etc.)
- Si possible, une proposition de correctif

## Délai de réponse

- **Accusé de réception** : sous 72 heures.
- **Première analyse** : sous 7 jours.
- **Publication d'un correctif** : selon la sévérité (critique : <14 jours).

Les contributeurs ayant signalé une faille de manière responsable seront
crédités dans le CHANGELOG (sauf demande contraire).

## Périmètre

Ce projet contient :

- Du **code JavaScript** (parseurs bancaires, générateurs eCDF, calculateurs).
- Des **données réglementaires** (taux TVA, tarifs LBR, schémas) — les erreurs
  factuelles ne sont pas des failles de sécurité, signalez-les via une issue
  classique avec le template `data_update`.
- Des **skills Markdown** pour agents IA — les tentatives de prompt injection
  via les skills sont considérées comme des failles et doivent être signalées
  ici.

## Hors périmètre

- Les services tiers (Légilux, eCDF, RCS) — adressez-vous à leur éditeur.
- L'environnement d'exécution de votre agent IA (Claude, Codex, etc.).
