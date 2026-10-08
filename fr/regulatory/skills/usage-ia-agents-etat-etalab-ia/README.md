# usage-ia-agents-etat

Skill pour assistants de code IA — cadre d'usage de l'**IA générative pour les agents publics de l'État**, d'après le [Guide d'usage de l'IA pour les agents publics de l'État](https://ia.numerique.gouv.fr/ressources/guide-dusage-de-lia/) publié par la **DINUM** (avec la DITP et la DGAFP).

## Ce que fait cette skill

Quand elle est activée, l'assistant IA peut :

- **Répondre aux questions** sur les règles d'usage de l'IA dans l'administration (5 principes, choix des outils, données autorisées, transparence, formation)
- **Alerter de façon proactive** quand l'utilisateur s'apprête à faire quelque chose de contraire au guide :
  - transmettre des données personnelles, sensibles, RH, médicales, internes, couvertes par le secret ou classifiées (IGI 1300) à un outil d'IA commercial grand public ;
  - utiliser un outil d'IA non autorisé par son administration ;
  - omettre de signaler un usage substantiel de l'IA (transparence) ;
  - lancer une action automatique sans validation humaine ;
  - recourir à l'IA pour un usage à haut risque au sens du règlement européen sur l'IA (tri de candidatures, RH, justice, santé, police).
- **Orienter vers l'outil adapté** : Assistant IA interministériel, Assistant Transcripts, Visio, ou l'outil de l'administration.

## Contenu

| Fichier | Description |
|---------|-------------|
| [`SKILL.md`](SKILL.md) | Les 5 principes, le conseil proactif (points de vigilance) et le choix de l'outil selon les données |
| [`references/comprendre-iag.md`](references/comprendre-iag.md) | Capacités, limites (hallucinations, biais) et conditions d'un usage réussi |
| [`references/outils-et-donnees.md`](references/outils-et-donnees.md) | Les 3 catégories d'outils, catégories de données, cadre juridique (RGPD, RIA, secret pro, SecNumCloud) |
| [`references/5-principes-fondamentaux.md`](references/5-principes-fondamentaux.md) | Détail des 5 principes fondamentaux |
| [`references/fiches-pratiques.md`](references/fiches-pratiques.md) | Les 5 règles d'or du prompt et les cas d'usage par famille de métier |

## Installation

```bash
# Avec Vercel Skills CLI (recommandé)
npx skills add etalab-ia/skills --skill usage-ia-agents-etat

# Claude Code
npx skills add etalab-ia/skills --skill usage-ia-agents-etat -a claude-code

# OpenCode
npx skills add etalab-ia/skills --skill usage-ia-agents-etat -a opencode
```

## Exemples d'utilisation

- *« Quelles sont les règles pour utiliser l'IA dans l'administration ? »*
- *« Je veux résumer ce compte-rendu de réunion interne avec ChatGPT, c'est ok ? »* → alerte : données internes → utiliser l'outil de l'administration
- *« Dois-je signaler que cette note a été rédigée avec l'IA ? »*
- *« Quel outil pour transcrire une réunion ? »* → Assistant Transcripts / Visio

## Liens utiles

- [Guide d'usage de l'IA pour les agents publics de l'État](https://ia.numerique.gouv.fr/ressources/guide-dusage-de-lia/)
- [IA dans l'État (DINUM)](https://ia.numerique.gouv.fr/)
- [Assistant IA interministériel](https://assistant.numerique.gouv.fr/)

## Licence

MIT
