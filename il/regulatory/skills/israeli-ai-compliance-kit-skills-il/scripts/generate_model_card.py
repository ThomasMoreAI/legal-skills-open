#!/usr/bin/env python3
"""Generate a markdown model card with Israeli-context fields from a JSON input.

Based on Mitchell et al. 2019 ("Model Cards for Model Reporting") with
additions for Israeli regulatory context: Privacy Protection Law database
registration status, Amendment 13 Data Protection Officer designation,
Ministry of Innovation 2023 ethical-principles alignment, and sector regulator
applicability.

Usage:
    python generate_model_card.py --input model.json --output MODEL_CARD.md
    python generate_model_card.py --example

Input JSON schema (all fields optional unless marked required):
    {
      "name": "My Model",                              # required
      "owner": "Acme Israel Ltd",                      # required
      "version": "1.0.0",
      "date": "2026-04-13",
      "contact": "ml-team@acme.co.il",
      "overview": "One-paragraph description",
      "intended_use": "Primary uses",
      "out_of_scope": "What not to use it for",
      "training_data": {
        "sources": ["Source 1", "Source 2"],
        "size": "100K rows",
        "languages": ["he", "en"],
        "lawful_basis": "Consent / legitimate interest / ..."
      },
      "evaluation": {
        "metrics": [{"name": "Accuracy", "value": "<your measured accuracy>"}],
        "datasets": ["Eval set A"],
        "fairness": "Summary of fairness tests"
      },
      "limitations": "Known limitations",
      "ethical_considerations": "Ethical analysis",
      "israeli_context": {
        "ppl_database_registered": true,
        "dpo_designated": true,
        "dpo_contact": "dpo@acme.co.il",
        "moi_2023_alignment": "Summary of alignment with 6 ethical principles",
        "sector_regulator": "None / BoI / MoH / CMISA / MoT / MoD",
        "eu_ai_act_scope": "Out of scope / Limited-risk / High-risk / GPAI"
      }
    }
"""

import argparse
import json
import sys
from datetime import date

EXAMPLE = {
    "name": "Hebrew Summarizer v1",
    "owner": "Example Israel Ltd",
    "version": "1.0.0",
    "date": str(date.today()),
    "contact": "ml@example.co.il",
    "overview": "Transformer-based abstractive summarizer for modern Hebrew news articles.",
    "intended_use": "Summarization of Israeli news articles for internal editorial workflow.",
    "out_of_scope": "Not for legal, medical, or financial document summarization.",
    "training_data": {
        "sources": ["Licensed Hebrew news corpus", "Publisher-approved archives"],
        "size": "250K articles",
        "languages": ["he"],
        "lawful_basis": "Contractual license from publishers"
    },
    "evaluation": {
        "metrics": [
            {"name": "ROUGE-L", "value": "38.5"},
            {"name": "Human preference", "value": "<your measured preference rate>"}
        ],
        "datasets": ["Held-out 5K articles"],
        "fairness": "No demographic disparity in summary quality across article categories"
    },
    "limitations": "May hallucinate quotes. Not validated on Mishnaic or classical Hebrew.",
    "ethical_considerations": "Outputs are verified by human editors before publication.",
    "israeli_context": {
        "ppl_database_registered": False,
        "dpo_designated": True,
        "dpo_contact": "dpo@example.co.il",
        "moi_2023_alignment": "Mapped to human-centric AI, transparency, reliability, accountability principles.",
        "sector_regulator": "None",
        "eu_ai_act_scope": "Out of scope (Israel-only deployment)"
    }
}


def render(data: dict) -> str:
    lines = []
    lines.append(f"# Model Card: {data.get('name', 'Untitled')}")
    lines.append("")
    lines.append(f"**Owner:** {data.get('owner', 'N/A')}")
    lines.append(f"**Version:** {data.get('version', 'N/A')}")
    lines.append(f"**Date:** {data.get('date', 'N/A')}")
    lines.append(f"**Contact:** {data.get('contact', 'N/A')}")
    lines.append("")

    lines.append("## Overview")
    lines.append(data.get("overview", "_Not provided._"))
    lines.append("")

    lines.append("## Intended Use")
    lines.append(data.get("intended_use", "_Not provided._"))
    lines.append("")

    lines.append("## Out of Scope")
    lines.append(data.get("out_of_scope", "_Not provided._"))
    lines.append("")

    td = data.get("training_data", {})
    lines.append("## Training Data")
    lines.append(f"- **Sources:** {', '.join(td.get('sources', [])) or 'N/A'}")
    lines.append(f"- **Size:** {td.get('size', 'N/A')}")
    lines.append(f"- **Languages:** {', '.join(td.get('languages', [])) or 'N/A'}")
    lines.append(f"- **Lawful basis (PPL):** {td.get('lawful_basis', 'N/A')}")
    lines.append("")

    ev = data.get("evaluation", {})
    lines.append("## Evaluation")
    metrics = ev.get("metrics", [])
    if metrics:
        lines.append("| Metric | Value |")
        lines.append("|--------|-------|")
        for m in metrics:
            lines.append(f"| {m.get('name', '')} | {m.get('value', '')} |")
    lines.append(f"- **Datasets:** {', '.join(ev.get('datasets', [])) or 'N/A'}")
    lines.append(f"- **Fairness:** {ev.get('fairness', 'N/A')}")
    lines.append("")

    lines.append("## Limitations")
    lines.append(data.get("limitations", "_Not provided._"))
    lines.append("")

    lines.append("## Ethical Considerations")
    lines.append(data.get("ethical_considerations", "_Not provided._"))
    lines.append("")

    ic = data.get("israeli_context", {})
    lines.append("## Israeli Regulatory Context")
    reg_status = "Yes" if ic.get("ppl_database_registered") else "No"
    dpo_status = "Yes" if ic.get("dpo_designated") else "No"
    lines.append(f"- **PPL database registered:** {reg_status}")
    lines.append(f"- **DPO designated (Amendment 13):** {dpo_status}")
    if ic.get("dpo_contact"):
        lines.append(f"- **DPO contact:** {ic['dpo_contact']}")
    lines.append(f"- **Sector regulator:** {ic.get('sector_regulator', 'None')}")
    lines.append(f"- **EU AI Act scope:** {ic.get('eu_ai_act_scope', 'Not assessed')}")
    lines.append("")
    lines.append("### Ministry of Innovation December 2023 Principles Alignment")
    lines.append(ic.get("moi_2023_alignment", "_Not provided._"))
    lines.append("")

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a markdown model card with Israeli-context fields.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--input", help="Path to JSON input file")
    parser.add_argument("--output", help="Path to output markdown file (stdout if omitted)")
    parser.add_argument("--example", action="store_true", help="Use built-in example data")
    args = parser.parse_args()

    if args.example:
        data = EXAMPLE
    elif args.input:
        try:
            with open(args.input, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            print(f"Error loading input: {e}", file=sys.stderr)
            return 1
    else:
        parser.print_help()
        return 1

    if not data.get("name") or not data.get("owner"):
        print("Error: 'name' and 'owner' are required fields", file=sys.stderr)
        return 1

    md = render(data)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"Model card written to {args.output}")
    else:
        print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
