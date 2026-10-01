# rgaa

Skill pour assistants de code IA — auditer la conformité [RGAA 4.1.2](https://accessibilite.numerique.gouv.fr/) de sites web et composants React/HTML.

## Ce que fait cette skill

Quand elle est activée, l'assistant IA peut :

- **Auditer du code** HTML/React selon les 106 critères RGAA 4.1.2 (basés sur WCAG 2.1 niveau AA)
- **Produire un rapport structuré** avec statut C/NC/NA par critère, non-conformités détaillées et corrections priorisées (🔴 Bloquant, 🟠 Majeur, 🟡 Mineur)
- **Exporter le rapport** dans `audits/rgaa-YYYY-MM-DD.md`

C'est un outil d'**audit a posteriori** : on lui fournit du code à analyser, il produit un rapport. Ce n'est pas un outil de génération de code.

## Contenu

| Fichier | Description |
|---------|-------------|
| [`SKILL.md`](SKILL.md) | Workflow d'audit en 4 étapes et format de rapport standardisé |
| [`references/criteres-images-cadres-couleurs.md`](references/criteres-images-cadres-couleurs.md) | Thèmes 1 à 3 : Images, Cadres, Couleurs |
| [`references/criteres-multimedia-tableaux-liens-scripts.md`](references/criteres-multimedia-tableaux-liens-scripts.md) | Thèmes 4 à 7 : Multimédia, Tableaux, Liens, Scripts |
| [`references/criteres-structure-presentation.md`](references/criteres-structure-presentation.md) | Thèmes 8 à 10 : Éléments obligatoires, Structure, Présentation |
| [`references/criteres-formulaires.md`](references/criteres-formulaires.md) | Thème 11 : Formulaires (13 critères) |
| [`references/criteres-navigation-consultation.md`](references/criteres-navigation-consultation.md) | Thèmes 12 à 13 : Navigation, Consultation |

## Installation

```bash
# Avec Vercel Skills CLI (recommandé)
npx skills add etalab-ia/skills --skill rgaa

# Claude Code
npx skills add etalab-ia/skills --skill rgaa -a claude-code

# OpenCode
npx skills add etalab-ia/skills --skill rgaa -a opencode
```

## Exemples d'utilisation

Une fois la skill installée, l'assistant IA peut répondre à des demandes comme :

- *"Audite l'accessibilité de ce composant formulaire"*
- *"Mon site est-il conforme RGAA ? Voici le code de la page d'accueil"*
- *"Génère un rapport de conformité RGAA pour ces composants React"*
- *"Quelles sont les non-conformités RGAA de ce HTML ?"*

## Liens utiles

- [Référentiel RGAA 4.1.2](https://accessibilite.numerique.gouv.fr/)
- [WCAG 2.1](https://www.w3.org/TR/WCAG21/)
- [Critères et tests RGAA](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)

## Licence

MIT
