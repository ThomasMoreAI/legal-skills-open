# Evals — Évaluation des skills Paperasse Lux

Suite d'évaluation pour mesurer la valeur ajoutée de chaque skill : on lance le même prompt **avec** et **sans** le `SKILL.md` chargé dans le contexte, puis un LLM-juge note les deux réponses sur des critères luxembourgeois précis (chiffres exacts, articles cités correctement, conformité au PCN/LIR/LCC).

## Prérequis

- Python ≥ 3.10
- [uv](https://docs.astral.sh/uv/) (`pip install uv`)
- Une clé API Anthropic dans `ANTHROPIC_API_KEY` (le runner appelle directement le SDK Python `anthropic`)

## Lancer les évaluations

```bash
# Toute la suite (~10-15 min)
uv run --project evals python evals/run_evals.py

# Un seul skill
uv run --project evals python evals/run_evals.py --skill notaire

# Garder le cache des runs précédents
uv run --project evals python evals/run_evals.py --reuse-cache

# Voir la review HTML
uv run --project evals python evals/generate_review.py evals-workspace/iteration-latest/

# Agréger les résultats sur plusieurs itérations
uv run --project evals python evals/aggregate_benchmark.py
```

## Format des tests

Chaque skill a son fichier dans `tests/` (ex. `tests/notaire.yaml`) :

```yaml
skill: notaire
cases:
  - id: bellegen-akt-2024
    prompt: "Acquisition d'un appartement à 650 000 € à Luxembourg-Ville. Acheteur célibataire, première résidence principale. Calcule les frais d'acte avec l'abattement Bëllegen Akt en vigueur depuis octobre 2024."
    must_contain:
      - "40 000"           # abattement par personne
      - "Bëllegen Akt"
      - "6 %"              # droit d'enregistrement
      - "1 %"              # droit de transcription
      - "3 %"              # surtaxe communale Lux-Ville
    must_not_contain:
      - "20 000"           # ancien abattement (2002-2024)
    rubric: |
      La réponse doit citer la loi du 27 juin 2024 portant introduction de mesures
      ciblées en matière de logement, calculer correctement la base imposable
      (650 000 - 40 000 = 610 000 €), et appliquer 6 % + 1 % + 3 % surtaxe Lux-Ville.
```

## Structure des résultats

```
evals-workspace/
├── iteration-2026-05-09T13-00/
│   ├── notaire/
│   │   ├── bellegen-akt-2024_with_skill.md
│   │   ├── bellegen-akt-2024_without_skill.md
│   │   └── grades.json
│   ├── results.json
│   └── review.html
└── cache/                # cache adressé par contenu
```

## Modèles utilisés

Configurés dans `config.yaml` :

- `subject_model` : modèle évalué (par défaut `claude-sonnet-4-5`)
- `judge_model` : juge LLM-as-judge (par défaut `claude-haiku-4-5`)

## Limites v0.1

- Pas de parallélisation (séquentiel — une suite complète prend ~15 min, pas 5).
- Cache adressé par contenu sur (prompt + skill + model + system_prompt + temperature + max_tokens) — change un de ces paramètres = re-run forcé.
- Pas de fallback `claude --bare`. Le runner appelle directement l'API Anthropic.
