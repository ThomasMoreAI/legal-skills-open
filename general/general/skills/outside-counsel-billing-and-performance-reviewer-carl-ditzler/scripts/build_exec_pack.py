#!/usr/bin/env python3
"""Build a markdown report, PDF-friendly HTML report, or PowerPoint-ready outline from structured JSON input"""
"""Codex created this script"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_payload(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def bullet_lines(items: list[str], indent: str = "- ") -> list[str]:
    return [f"{indent}{item}" for item in items if item]


def render_markdown(data: dict) -> str:
    lines = [f"# {data.get('title', 'Executive Review')}"]
    if data.get("period"):
        lines.append("")
        lines.append(f"**Period:** {data['period']}")
    if data.get("audience"):
        lines.append(f"**Audience:** {data['audience']}")
    if data.get("summary"):
        lines.extend(["", "## Summary", data["summary"]])
    metrics = data.get("metrics", {})
    if metrics:
        lines.extend(["", "## Key Metrics"])
        for key, value in metrics.items():
            lines.append(f"- {key}: {value}")
    findings = data.get("findings", [])
    if findings:
        lines.extend(["", "## Headline Findings"])
        for finding in findings:
            confidence = f" ({finding.get('confidence')})" if finding.get("confidence") else ""
            lines.append(f"- {finding.get('title', 'Finding')}{confidence}: {finding.get('detail', '')}".rstrip())
    recommendations = data.get("recommendations", [])
    if recommendations:
        lines.extend(["", "## Recommended Actions"])
        lines.extend(bullet_lines(recommendations))
    return "\n".join(lines).strip() + "\n"


def render_html(data: dict) -> str:
    import html

    def esc(value: object) -> str:
        return html.escape("" if value is None else str(value))

    findings = data.get("findings", [])
    metrics = data.get("metrics", {})
    recommendations = data.get("recommendations", [])
    metric_rows = "".join(
        f"<tr><th>{esc(key)}</th><td>{esc(value)}</td></tr>" for key, value in metrics.items()
    )
    finding_cards = "".join(
        (
            "<section class='issue-card'>"
            f"<div class='issue-head'><h3>{esc(finding.get('title', 'Finding'))}</h3>"
            f"<span class='pill'>{esc(finding.get('label', finding.get('title', 'Finding')))}</span>"
            f"<span class='confidence'>{esc(finding.get('confidence', ''))}</span></div>"
            f"<p>{esc(finding.get('detail', ''))}</p>"
            "</section>"
        )
        for finding in findings
    )
    rec_list = "".join(f"<li>{esc(item)}</li>" for item in recommendations if item)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>{esc(data.get('title', 'Executive Review'))}</title>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      margin: 36px;
      color: #1d2433;
      line-height: 1.4;
    }}
    h1, h2, h3 {{
      color: #24385b;
      margin: 0 0 12px 0;
    }}
    .meta {{
      margin: 0 0 20px 0;
      color: #4b5a73;
      font-size: 14px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      table-layout: fixed;
      margin: 12px 0 20px 0;
    }}
    th, td {{
      border: 1px solid #d3d9e3;
      padding: 10px 12px;
      text-align: left;
      vertical-align: top;
      white-space: normal;
      overflow-wrap: anywhere;
      word-break: break-word;
    }}
    th {{
      background: #eef3fa;
      width: 36%;
      color: #24385b;
    }}
    .issue-card {{
      border: 1px solid #cfd7e6;
      border-radius: 10px;
      padding: 14px 16px;
      margin: 0 0 14px 0;
      break-inside: avoid;
      page-break-inside: avoid;
    }}
    .issue-head {{
      display: grid;
      grid-template-columns: minmax(0, 1fr) auto auto;
      gap: 10px;
      align-items: start;
      margin-bottom: 8px;
    }}
    .issue-head h3 {{
      margin: 0;
      overflow-wrap: anywhere;
      word-break: break-word;
    }}
    .pill {{
      display: inline-block;
      max-width: 220px;
      padding: 6px 10px;
      border-radius: 999px;
      background: #d68400;
      color: white;
      font-weight: 700;
      font-size: 13px;
      text-align: center;
      white-space: normal;
      overflow-wrap: anywhere;
      word-break: break-word;
    }}
    .confidence {{
      font-weight: 600;
      color: #4b5a73;
      white-space: nowrap;
    }}
    p, li {{
      overflow-wrap: anywhere;
      word-break: break-word;
    }}
  </style>
</head>
<body>
  <h1>{esc(data.get('title', 'Executive Review'))}</h1>
  <div class="meta">
    {'<div><strong>Period:</strong> ' + esc(data.get('period')) + '</div>' if data.get('period') else ''}
    {'<div><strong>Audience:</strong> ' + esc(data.get('audience')) + '</div>' if data.get('audience') else ''}
  </div>
  {'<h2>Summary</h2><p>' + esc(data.get('summary')) + '</p>' if data.get('summary') else ''}
  {'<h2>Key Metrics</h2><table>' + metric_rows + '</table>' if metrics else ''}
  {'<h2>Headline Findings</h2>' + finding_cards if findings else ''}
  {'<h2>Recommended Actions</h2><ul>' + rec_list + '</ul>' if recommendations else ''}
</body>
</html>
"""


def render_ppt_outline(data: dict) -> str:
    slides = data.get("slides")
    if not slides:
        slides = [
            {"title": data.get("title", "Executive Review"), "bullets": [data.get("summary", "")]},
            {"title": "Headline Findings", "bullets": [f.get("title", "") + (f": {f.get('detail', '')}" if f.get("detail") else "") for f in data.get("findings", [])]},
            {"title": "Recommended Actions", "bullets": data.get("recommendations", [])},
        ]
    blocks = []
    for index, slide in enumerate(slides, start=1):
        blocks.append(f"## Slide {index}: {slide.get('title', 'Untitled')}")
        for bullet in slide.get("bullets", []):
            if bullet:
                blocks.append(f"- {bullet}")
        blocks.append("")
    return "\n".join(blocks).strip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--format", choices=["report-md", "report-html", "ppt-outline"], required=True)
    args = parser.parse_args()

    data = load_payload(Path(args.input))
    if args.format == "report-md":
        output = render_markdown(data)
    elif args.format == "report-html":
        output = render_html(data)
    else:
        output = render_ppt_outline(data)
    Path(args.output).write_text(output, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
