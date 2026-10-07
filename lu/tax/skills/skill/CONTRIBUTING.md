# Contribuer à Paperasse Lux

Merci de l'intérêt porté au projet ! Paperasse Lux est une collection de skills pour agents IA spécialisés dans la bureaucratie luxembourgeoise. Vos contributions — corrections, mises à jour de seuils légaux, nouveaux templates, retours d'expérience — sont les bienvenues.

## Types de contributions recherchées

1. **Mise à jour de données légales** (`*/data/*.json`) : taux TVA, barèmes IRPP, seuils PME, multiplicateurs ICC communaux, montants Bëllegen Akt, droits d'enregistrement.
2. **Nouvelles références** (`*/references/*.md`) : explications de mécanismes fiscaux, procédures ACD/AED, normes ISA-LUX, jurisprudence notable.
3. **Templates** (`*/templates/*` ou `templates/*`) : statuts, conventions, PV, courriers, mise en demeure, état daté.
4. **Scripts** (`*/scripts/*` ou `scripts/*`) : générateurs FAIA, validateurs Peppol, calculateurs IRPP.
5. **Corrections** : coquilles, liens morts, articles de loi mal cités, taux périmés.
6. **Nouveaux skills** : si un métier réglementé luxembourgeois manque (avocat, huissier, agent immobilier IFE, géomètre…).

## Règles éditoriales

### Source obligatoire

Chaque affirmation chiffrée ou juridique doit citer sa source primaire :
- **Loi** : *Loi du 4 décembre 1967 concernant l'impôt sur le revenu (LIR), art. X*
- **Règlement** : *Règlement grand-ducal du 12 septembre 2019, art. X*
- **Mémorial** : lien ELI vers `data.legilux.public.lu/eli/...`
- **Administration** : guichet.lu, impotsdirects.public.lu, aed.public.lu, lbr.lu, cssf.lu

Pas de source secondaire (PwC, KPMG, Deloitte) sans le texte primaire en parallèle.

### Date de dernière vérification

Tout fichier `data/*.json` doit contenir un champ `last_updated` (format `YYYY-MM-DD`) et `source`. Les fichiers `references/*.md` mentionnent la date en haut ou en bas.

### Veille via le flux JO

Avant toute mise à jour, consulter le flux RSS Légilux (`https://data.legilux.public.lu/api/rss-leg.xml`) ou la page **Veille JO** de l'app pour vérifier qu'aucune publication récente ne modifie le texte. Voir `references/legilux-flux-rss.md`.

### Style

- **Français** (langue principale du projet). Les termes luxembourgeois ou allemands sont conservés (Bëllegen Akt, Mémorial, ICC, RTS).
- **Markdown** GFM : tables, blocs de code avec langage, titres `##`/`###`.
- **Exemples chiffrés** : préférer des cas réalistes (CA 250 000 €, classe 1a avec 1 enfant, etc.) plutôt que `X € / Y €`.
- **Pas d'emoji** dans les SKILL.md (clarté pour parsing par les agents).

## Workflow de contribution

```bash
# 1. Forker puis cloner
git clone https://github.com/<votre-user>/paperasse-lux.git
cd paperasse-lux

# 2. Brancher
git checkout -b fix/tva-taux-2026

# 3. Modifier (ex. data/tva-taux.json)
# 4. Vérifier la source
# 5. Commit avec message clair
git commit -m "data(tva): mise à jour taux super-réduit 2026 (loi du DD/MM/AAAA)"

# 6. Pousser et ouvrir une PR
git push origin fix/tva-taux-2026
```

## Format de commit

Préfixes recommandés :
- `data(<skill>):` — mise à jour JSON
- `ref(<skill>):` — nouvelle référence ou correction
- `tpl:` — template
- `script:` — script utilitaire
- `skill(<nom>):` — modification d'un SKILL.md
- `doc:` — README, CONTRIBUTING, CHANGELOG
- `fix:` — correction de bug ou erreur factuelle

## Revue

Les PR sont revues sur 3 critères :
1. **Exactitude juridique** — la source primaire est-elle citée et toujours en vigueur ?
2. **Cohérence éditoriale** — respecte-t-elle le style et la structure du skill concerné ?
3. **Utilité opérationnelle** — un agent IA peut-il s'en servir directement (pas seulement lire) ?

## Code de conduite

Soyez courtois, factuel, et focalisé sur le contenu. Les désaccords sur l'interprétation d'un texte de loi sont bienvenus — citez vos sources et proposez une formulation neutre.

## Questions

Ouvrir une **issue** GitHub avec le label `question` ou `discussion`.
