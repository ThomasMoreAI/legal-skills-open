#!/usr/bin/env python3
"""
generate_review.py — Génère un review.html pour parcourir les résultats
d'une itération côte-à-côte (sans skill | avec skill | notation).

Usage : python evals/generate_review.py evals-workspace/iteration-XXX/
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jinja2 import Template

TPL = Template("""<!doctype html><html lang="fr"><head><meta charset="utf-8">
<title>Review {{ iter }}</title>
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; max-width: 1400px; margin: 2rem auto; padding: 0 1rem; color: #222; }
  h1 { color: #ED2939; }
  h2 { color: #00A1DE; border-bottom: 1px solid #eee; padding-bottom: 0.3rem; }
  .case { border: 1px solid #ddd; border-radius: 6px; margin: 1rem 0; padding: 1rem; }
  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1rem; }
  .col { border: 1px solid #eee; padding: 1rem; border-radius: 4px; max-height: 400px; overflow: auto; white-space: pre-wrap; font-family: ui-monospace, monospace; font-size: 12px; }
  .with { background: #f0fdf4; }
  .without { background: #fef2f2; }
  .score { font-size: 1.5rem; font-weight: bold; }
  .delta-pos { color: #16a34a; }
  .delta-neg { color: #dc2626; }
  .prompt { background: #f9fafb; padding: 0.7rem; border-left: 3px solid #00A1DE; }
  table { border-collapse: collapse; width: 100%; }
  th, td { border: 1px solid #ddd; padding: 6px 10px; text-align: left; }
  th { background: #f5f5f5; }
</style></head><body>
<h1>Paperasse Lux — Review {{ iter }}</h1>
<p>Sujet : <code>{{ subject_model }}</code> — Juge : <code>{{ judge_model }}</code></p>

<h2>Synthèse</h2>
<table>
  <tr><th>Skill</th><th>With</th><th>Without</th><th>Delta</th></tr>
  {% for s in skills %}
  <tr><td><b>{{ s.skill }}</b></td><td>{{ "%.0f"|format(s.avg_with) }}%</td><td>{{ "%.0f"|format(s.avg_without) }}%</td><td class="{{ 'delta-pos' if s.delta >= 0 else 'delta-neg' }}">{{ "%+.0f"|format(s.delta) }}%</td></tr>
  {% endfor %}
</table>

{% for s in skills %}
<h2>{{ s.skill }}</h2>
{% for c in s.cases %}
<div class="case">
  <h3>{{ c.id }} — <span class="score {{ 'delta-pos' if c.delta >= 0 else 'delta-neg' }}">Δ {{ "%+d"|format(c.delta) }}</span></h3>
  <div class="prompt">{{ c.prompt }}</div>
  <div class="grid">
    <div>
      <div class="score delta-neg">Sans skill : {{ c.without.score }}/100</div>
      <p><i>{{ c.without.justification }}</i></p>
      <div class="col without">{{ c.without_text }}</div>
    </div>
    <div>
      <div class="score delta-pos">Avec skill : {{ c.with.score }}/100</div>
      <p><i>{{ c["with"].justification }}</i></p>
      <div class="col with">{{ c.with_text }}</div>
    </div>
  </div>
</div>
{% endfor %}
{% endfor %}
</body></html>
""")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage : python evals/generate_review.py evals-workspace/iteration-XXX/")
        sys.exit(1)
    iter_dir = Path(sys.argv[1]).resolve()
    results = json.loads((iter_dir / "results.json").read_text(encoding="utf-8"))

    skills_view = []
    for s in results["skills"]:
        if not s["cases"]:
            continue
        cases_view = []
        for c in s["cases"]:
            with_text = (iter_dir / s["skill"] / f"{c['id']}_with_skill.md").read_text(encoding="utf-8")
            without_text = (iter_dir / s["skill"] / f"{c['id']}_without_skill.md").read_text(encoding="utf-8")
            cases_view.append({**c, "with_text": with_text, "without_text": without_text})
        avg_w = sum(c["with"]["score"] for c in s["cases"]) / len(s["cases"])
        avg_wo = sum(c["without"]["score"] for c in s["cases"]) / len(s["cases"])
        skills_view.append({"skill": s["skill"], "cases": cases_view, "avg_with": avg_w, "avg_without": avg_wo, "delta": avg_w - avg_wo})

    html = TPL.render(iter=results["iteration"], subject_model=results["subject_model"], judge_model=results["judge_model"], skills=skills_view)
    out = iter_dir / "review.html"
    out.write_text(html, encoding="utf-8")
    print(f"[OK] {out}")


if __name__ == "__main__":
    main()
