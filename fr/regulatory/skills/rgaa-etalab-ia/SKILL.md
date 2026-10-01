---
name: rgaa-etalab-ia
title: RGAA 4.1.2 — Outil d'audit de conformité
description: 'Outil d''audit de conformité RGAA 4.1.2 pour sites web et composants React/HTML. Utiliser cette skill pour auditer la conformité RGAA d''un site ou d''un composant : quand l''utilisateur demande un audit d''accessibilité, un rapport de conformité RGAA, quand il veut savoir si son code/site respecte le RGAA, quand il mentionne "audit RGAA", "conformité RGAA", "non-conformités", "déclaration d''accessibilité", ou quand il partage du code HTML/React pour vérification a posteriori.'
author: etalab-ia
author_url: https://github.com/etalab-ia/skills/tree/main/skills/rgaa
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: regulatory
language: fr
sources:
- title: Criteres Formulaires
  path: references/criteres-formulaires.md
- title: Criteres Images Cadres Couleurs
  path: references/criteres-images-cadres-couleurs.md
- title: Criteres Multimedia Tableaux Liens Scripts
  path: references/criteres-multimedia-tableaux-liens-scripts.md
- title: Criteres Navigation Consultation
  path: references/criteres-navigation-consultation.md
- title: Criteres Structure Presentation
  path: references/criteres-structure-presentation.md
---

# RGAA 4.1.2 — Outil d'audit de conformité

Référentiel d'accessibilité numérique français. 106 critères répartis en 13 thématiques. Basé sur WCAG 2.1 niveau AA.

Source : https://accessibilite.numerique.gouv.fr/

## Workflow d'audit

1. **Analyser le code fourni** (HTML, JSX, CSS)
2. **Parcourir les 13 thèmes RGAA** en consultant les fichiers de référence détaillés
3. **Pour chaque critère**, attribuer un statut :
   - **C** — Conforme : critère respecté
   - **NC** — Non conforme : critère violé (identifier l'élément et le problème)
   - **NA** — Non applicable : critère sans objet pour ce contenu (justifier)
4. **Produire le rapport structuré** selon le format ci-dessous
5. **Exporter le rapport** : écrire le rapport dans un fichier Markdown ET l'afficher dans la conversation

## Format du rapport de conformité

```markdown
## Audit RGAA 4.1.2 — Rapport de conformité

**Date :** JJ/MM/AAAA
**Périmètre audité :** [description du code / page / composant]
**Résultat global :** X% conforme
(X critères applicables — X conformes, X non conformes, X non applicables)

---

### Tableau de synthèse

| Thème | C | NC | NA |
|-------|---|----|----|
| 1. Images | | | |
| 2. Cadres | | | |
| 3. Couleurs | | | |
| 4. Multimédia | | | |
| 5. Tableaux | | | |
| 6. Liens | | | |
| 7. Scripts | | | |
| 8. Éléments obligatoires | | | |
| 9. Structuration | | | |
| 10. Présentation | | | |
| 11. Formulaires | | | |
| 12. Navigation | | | |
| 13. Consultation | | | |
| **Total** | | | |

---

### Non-conformités détectées

**[NC] {ID} — {Intitulé du critère}**
- **Élément concerné :** `<code>` ou description de l'endroit dans la page
- **Problème :** description précise de la violation
- **Correction :** action concrète à mener
- **Priorité :** 🔴 Bloquant / 🟠 Majeur / 🟡 Mineur

---

### Critères conformes

{ID1}, {ID2}, {ID3}... (liste compacte)

### Critères non applicables

- **{ID}** — {justification courte}
```

## Export du rapport

Après avoir produit le rapport, **toujours** :

1. Créer le dossier `audits/` à la racine du projet s'il n'existe pas
2. Écrire le rapport complet dans `audits/rgaa-AAAA-MM-JJ.md` (date du jour, format ISO)
3. Afficher également le rapport dans la conversation

Si un fichier du même nom existe déjà, ajouter un suffixe incrémental : `rgaa-2026-03-26-2.md`.

> Exemple : `audits/rgaa-2026-03-26.md`

## Grille de priorités

| Priorité | Définition | Exemples |
|----------|------------|---------|
| 🔴 **Bloquant** | Bloque l'accès au contenu ou à la fonctionnalité pour un utilisateur AT | Image sans `alt`, champ sans label, lien vide, piège au clavier |
| 🟠 **Majeur** | Impact fort sur l'expérience mais contournable par certains AT | Contraste insuffisant, focus non visible, hiérarchie de titres cassée, lien non explicite |
| 🟡 **Mineur** | Gêne légère, dégradation de l'expérience sans blocage | `autocomplete` manquant, `caption` de tableau absent, nouvelle fenêtre non signalée |

## Référence détaillée des critères

Chaque fichier de référence liste les critères avec leur condition, test de code, non-conformité type et priorité.

- **Images, Cadres, Couleurs** (thèmes 1–3, 14 critères) : [references/criteres-images-cadres-couleurs.md](references/criteres-images-cadres-couleurs.md)
- **Multimédia, Tableaux, Liens, Scripts** (thèmes 4–7, 28 critères) : [references/criteres-multimedia-tableaux-liens-scripts.md](references/criteres-multimedia-tableaux-liens-scripts.md)
- **Éléments obligatoires, Structure, Présentation** (thèmes 8–10, 28 critères) : [references/criteres-structure-presentation.md](references/criteres-structure-presentation.md)
- **Formulaires** (thème 11, 13 critères) : [references/criteres-formulaires.md](references/criteres-formulaires.md)
- **Navigation, Consultation** (thèmes 12–13, 23 critères) : [references/criteres-navigation-consultation.md](references/criteres-navigation-consultation.md)
