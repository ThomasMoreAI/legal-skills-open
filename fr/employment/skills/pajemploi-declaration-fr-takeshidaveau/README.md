# Skill pajemploi-declaration-fr

Assistant de préparation de la déclaration mensuelle Pajemploi pour un parent
employeur d'une assistante maternelle agréée (IDCC 2395).

## Installation

Copier `skills/pajemploi-declaration-fr/` dans `~/.claude/skills/` pour un
skill personnel, ou laisser dans ce dépôt pour un skill projet.

## Utilisation

Depuis Claude Code :

> "Aide-moi à préparer ma déclaration Pajemploi du mois"

Le skill détecte automatiquement le mode :
- **Mode A** (setup) si aucun contrat dans `./pajemploi/` — il ingère le
  contrat et écrit `contrat-<prenom>.md`.
- **Mode B** (mensuel) si le contrat existe — il te pose les questions du
  mois et écrit `YYYY-MM.md`.
- **Mode C** (info attestation fiscale) sur demande explicite en fin d'année.

## Artefacts produits

Dans `./pajemploi/` :
- `contrat-<prenom-enfant>.md` — résumé du contrat (écrit une fois).
- `YYYY-MM.md` — déclaration mensuelle (une par mois) avec tableau des cases
  à saisir sur pajemploi.urssaf.fr, hypothèses retenues, checklist à vérifier.

Format stable de `monthly.md` pour consommation future par un skill
compagnon d'automatisation navigateur (hors v1).

## Limitations

Le skill refuse de traiter les cas R-01 à R-04 (fin de contrat / rupture, garde partagée, CDD particulier, activité partielle de l'assmat). Voir `references/pitfalls.md` pour le détail. Pour ces cas, consulter un conseiller Pajemploi ou un expert paie.

## Structure

```
skills/pajemploi-declaration-fr/
├── SKILL.md                            # point d'entrée, 3 modes
├── references/
│   ├── contract-schema.md              # mode A
│   ├── monthly-fields.md               # mode B (champs + règles)
│   └── pitfalls.md                     # P-01..P-08 + R-01..R-04
├── templates/
│   ├── contrat.md
│   └── monthly.md
└── tests/
    └── fixtures/
        ├── fixture-01-mensualise-standard/
        ├── fixture-02-heures-complementaires/
        └── fixture-03-cp-juin/
```

## Lien avec `declaration-impot-fr`

L'attestation fiscale annuelle Pajemploi alimente la case **7GA** de la
déclaration d'impôt. Le piège P-07 de ce skill renvoie vers le piège P-08 du
skill `declaration-impot-fr` : montant 7GA = total attestation − aides CMG
CAF perçues.

## Documents de conception

- Spec : `docs/superpowers/specs/2026-04-24-skill-pajemploi-declaration-fr-design.md`
- Plan d'implémentation : `docs/superpowers/plans/2026-04-24-skill-pajemploi-declaration-fr.md`

## Évolutions prévues

- Skill compagnon d'automatisation navigateur consommant `monthly.md`.
- Extension fin de contrat (R-01).
- Intégration CMG via CAF pour le calcul case 7GA.

## État v1

- Workflow 3 modes (A/B/C).
- 3 fixtures de test avec expected-monthly.md.
- Points à confirmer lors de la première utilisation réelle : format exact
  des champs sur pajemploi.urssaf.fr (décimales, libellés).
