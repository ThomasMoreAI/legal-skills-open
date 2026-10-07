#!/usr/bin/env python3
"""
run_evals.py — Lance les évaluations pour les skills Paperasse Lux.

Pour chaque cas de test :
  1. Demande au modèle SANS le skill chargé
  2. Demande au modèle AVEC le skill chargé
  3. Demande au modèle-juge de noter les deux réponses
  4. Écrit les résultats dans evals-workspace/iteration-<timestamp>/
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any

import yaml
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

try:
    from anthropic import Anthropic
except ImportError:
    print("[ERREUR] pip install anthropic — ou lancez via uv (uv run --project evals python ...)")
    sys.exit(1)

console = Console()
ROOT = Path(__file__).resolve().parent.parent
EVALS_DIR = ROOT / "evals"
WORKSPACE = ROOT / "evals-workspace"
CACHE_DIR = WORKSPACE / "cache"


def load_config() -> dict[str, Any]:
    return yaml.safe_load((EVALS_DIR / "config.yaml").read_text(encoding="utf-8"))


def load_test_cases(skill: str) -> dict[str, Any]:
    test_file = EVALS_DIR / "tests" / f"{skill}.yaml"
    if not test_file.exists():
        return {"skill": skill, "cases": []}
    return yaml.safe_load(test_file.read_text(encoding="utf-8"))


def load_skill_md(skill: str) -> str:
    skill_path = ROOT / skill / "SKILL.md"
    if not skill_path.exists():
        console.print(f"[yellow][WARN] {skill}/SKILL.md introuvable[/yellow]")
        return ""
    return skill_path.read_text(encoding="utf-8")


def cache_key(prompt: str, skill_content: str, model: str, system: str = "", temperature: float = 0.0, max_tokens: int = 0) -> str:
    """Hash incluant tous les paramètres qui influencent la sortie LLM, pour éviter
    les faux hits du cache lorsque system_prompt / température / tokens changent."""
    h = hashlib.sha256()
    for piece in (prompt, skill_content, model, system, f"{temperature}", f"{max_tokens}"):
        h.update(piece.encode())
        h.update(b"\x00")
    return h.hexdigest()[:16]


def cached_or_call(
    client: Anthropic,
    *,
    model: str,
    system: str,
    prompt: str,
    max_tokens: int,
    temperature: float,
    skill_content: str = "",
    use_cache: bool = False,
) -> str:
    full_system = system if not skill_content else f"{system}\n\n# Skill chargé\n\n{skill_content}"
    if use_cache:
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        key = cache_key(prompt, skill_content, model, full_system, temperature, max_tokens)
        cached = CACHE_DIR / f"{key}.txt"
        if cached.exists():
            return cached.read_text(encoding="utf-8")
    msg = client.messages.create(
        model=model,
        system=full_system,
        max_tokens=max_tokens,
        temperature=temperature,
        messages=[{"role": "user", "content": prompt}],
    )
    text = "".join(b.text for b in msg.content if hasattr(b, "text"))
    if use_cache:
        cached.write_text(text, encoding="utf-8")
    return text


JUDGE_PROMPT = """Tu es un expert luxembourgeois (comptabilité, fiscalité, droit notarial). Tu évalues une réponse d'IA selon la rubrique fournie.

# Cas à évaluer
{prompt}

# Rubrique
{rubric}

# Mots/chiffres qui DOIVENT figurer
{must_contain}

# Mots/chiffres qui NE DOIVENT PAS figurer
{must_not_contain}

# Réponse à noter
{answer}

# Instructions
- Vérifie que TOUS les éléments must_contain sont présents.
- Vérifie qu'AUCUN élément must_not_contain n'est présent.
- Évalue la rubrique de fond (citations légales, exactitude des calculs, contexte LU correct).
- Note de 0 à 100. Justifie en 2-3 phrases maximum.

Réponds UNIQUEMENT avec un objet JSON :
{{"score": <0-100>, "justification": "<2-3 phrases>", "must_contain_ok": true/false, "must_not_contain_ok": true/false}}
"""


def grade(client: Anthropic, cfg: dict, case: dict, answer: str) -> dict:
    prompt = JUDGE_PROMPT.format(
        prompt=case["prompt"],
        rubric=case.get("rubric", "(pas de rubrique fournie — évalue l'exactitude générale)"),
        must_contain="\n".join(f"- {m}" for m in case.get("must_contain", [])) or "(aucun)",
        must_not_contain="\n".join(f"- {m}" for m in case.get("must_not_contain", [])) or "(aucun)",
        answer=answer,
    )
    text = cached_or_call(
        client,
        model=cfg["judge_model"],
        system="Tu notes des réponses d'IA. Réponds UNIQUEMENT en JSON valide.",
        prompt=prompt,
        max_tokens=cfg["judge_max_tokens"],
        temperature=cfg["judge_temperature"],
    )
    # Parse JSON robuste
    try:
        start = text.find("{")
        end = text.rfind("}") + 1
        return json.loads(text[start:end])
    except (ValueError, json.JSONDecodeError):
        return {"score": 0, "justification": f"[Parsing échoué : {text[:200]}]", "must_contain_ok": False, "must_not_contain_ok": False}


def run_skill(skill: str, cfg: dict, client: Anthropic, iter_dir: Path, use_cache: bool) -> dict:
    cases_data = load_test_cases(skill)
    cases = cases_data.get("cases", [])
    if not cases:
        console.print(f"[yellow]Aucun cas pour {skill}[/yellow]")
        return {"skill": skill, "cases": []}
    skill_content = load_skill_md(skill)
    skill_dir = iter_dir / skill
    skill_dir.mkdir(parents=True, exist_ok=True)
    results = []

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console) as bar:
        for case in cases:
            t = bar.add_task(f"  {skill}/{case['id']}", total=None)

            # Sans skill
            without = cached_or_call(client, model=cfg["subject_model"], system=cfg["system_prompt"],
                                      prompt=case["prompt"], max_tokens=cfg["subject_max_tokens"],
                                      temperature=cfg["subject_temperature"], use_cache=use_cache)
            (skill_dir / f"{case['id']}_without_skill.md").write_text(without, encoding="utf-8")

            # Avec skill
            with_ = cached_or_call(client, model=cfg["subject_model"], system=cfg["system_prompt"],
                                    prompt=case["prompt"], max_tokens=cfg["subject_max_tokens"],
                                    temperature=cfg["subject_temperature"],
                                    skill_content=skill_content, use_cache=use_cache)
            (skill_dir / f"{case['id']}_with_skill.md").write_text(with_, encoding="utf-8")

            # Notation
            grade_without = grade(client, cfg, case, without)
            grade_with = grade(client, cfg, case, with_)
            results.append({
                "id": case["id"],
                "prompt": case["prompt"],
                "without": grade_without,
                "with": grade_with,
                "delta": grade_with["score"] - grade_without["score"],
            })
            bar.update(t, completed=True, description=f"  {skill}/{case['id']}: with={grade_with['score']} without={grade_without['score']} Δ={grade_with['score']-grade_without['score']:+d}")

    out = {"skill": skill, "cases": results}
    (skill_dir / "grades.json").write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill", help="Évalue un seul skill")
    parser.add_argument("--reuse-cache", action="store_true", help="Réutilise les runs précédents")
    args = parser.parse_args()

    cfg = load_config()
    if not os.environ.get("ANTHROPIC_API_KEY"):
        console.print("[red][ERREUR] ANTHROPIC_API_KEY manquant.[/red]")
        sys.exit(1)

    client = Anthropic()
    skills = [args.skill] if args.skill else cfg["skills"]
    stamp = dt.datetime.now().strftime("%Y-%m-%dT%H-%M")
    iter_dir = WORKSPACE / f"iteration-{stamp}"
    iter_dir.mkdir(parents=True, exist_ok=True)
    console.print(f"[bold cyan]Itération : {iter_dir}[/bold cyan]")

    all_results = []
    for skill in skills:
        console.print(f"\n[bold]== {skill} ==[/bold]")
        all_results.append(run_skill(skill, cfg, client, iter_dir, args.reuse_cache))

    summary = {
        "iteration": stamp,
        "subject_model": cfg["subject_model"],
        "judge_model": cfg["judge_model"],
        "skills": all_results,
    }
    (iter_dir / "results.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    # Mise à jour du raccourci "latest"
    latest = WORKSPACE / "iteration-latest"
    if latest.exists() or latest.is_symlink():
        latest.unlink()
    latest.symlink_to(iter_dir.name)

    console.print("\n[bold green]== Résumé ==[/bold green]")
    for s in all_results:
        if not s["cases"]:
            continue
        avg_w = sum(c["with"]["score"] for c in s["cases"]) / len(s["cases"])
        avg_wo = sum(c["without"]["score"] for c in s["cases"]) / len(s["cases"])
        console.print(f"  {s['skill']:25s}  with={avg_w:.0f}%  without={avg_wo:.0f}%  Δ={avg_w-avg_wo:+.0f}%")


if __name__ == "__main__":
    main()
