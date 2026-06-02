---
name: paper2patent
title: Paper2Patent
description: Convert academic papers into complete Chinese invention patent application deliverables, including DOCX/PDF application documents, claims, specifications, abstracts, drawing specifications, and fidelity reviews. Use when drafting patent text, generating Word or PDF patent applications, preparing patent drawings, or checking paper-to-patent fidelity.
author: gabrielmoreira
author_url: https://github.com/gabrielmoreira/agent-skills-mirror/tree/main/mirrors/repos/7toCR@paper2patent/.claude/skills/paper2patent
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cn
practice: ip
language: en
---

# Paper2Patent

## Purpose

Use this skill to convert an academic paper into a complete Chinese invention patent application deliverable. The default full-draft output is a Word document (`.docx`) and, when a converter is available, a PDF copy. Keep the work faithful to the supplied paper: do not invent technical features, embodiments, data, hardware, scenarios, or effects that are not present in the source material.

## Workflow

1. Determine the output mode. Use `direct` by default, `human-in-loop` when the user asks to review choices before generation, and `text-only` when the user explicitly wants no files.
2. Collect and assess the paper input. Read `references/input-requirements.md` when the user provides partial paper content, a PDF path, source paper figures, figure descriptions, or unclear source material.
3. Extract the patentable contribution. Build the closed chain of difference point, technical problem, technical solution, and technical effect.
4. Draft the structured patent content. Read `references/text-conversion-workflow.md` for the five-part content model and execution order. Treat the repository `reference_skills/meterial.md` prompt as the normative source for the five patent sections, claim rules, specification depth, and fidelity constraints.
5. Apply claim and specification rules. Read `references/claims-and-specification-rules.md` before writing or revising claims, background, invention content, or embodiments.
6. Prepare drawings. Read `references/drawing-generation.md`; first derive patent reference drawings from the source paper figures, captions, and method text when available, then align them with the claims and specification. Generate black-and-white SVG reference drawings, converter-compatible PNG fallbacks when possible, and Image2-style refinement prompts.
7. Generate files for full drafts. Read `references/document-generation.md`, then use `scripts/generate_patent_drawings.py` to create clean SVG/PNG drawings, `scripts/generate_patent_docx.py` to embed them in DOCX, and `scripts/export_patent_pdf.py` for PDF conversion when available.
8. Run the internal quality pass. Read `references/quality-checklist.md` before finalizing.

## Output Rules

- Default to Simplified Chinese for patent deliverables.
- For a full patent application request, default to generating source-faithful SVG reference drawings, PNG fallback drawings, Image2 refinement prompts, a `.docx` file with embedded visible drawings, and a `.pdf` copy when possible.
- Output only the requested artifact summary to the user: file paths, remaining placeholders, and any conversion limitation. Do not expose hidden analysis or internal checklist results.
- In `text-only` mode, output plain patent text with no Markdown headings, code fences, checklists, or hidden reasoning.
- Preserve one consistent invention name across the abstract, claims, specification, and drawing descriptions.
- Do not treat text-only drawing descriptions as a complete drawing deliverable when a full DOCX/PDF application is requested; either embed compliant drawings or report the drawing-generation limitation.
- Do not draw figure numbers or figure titles inside the image canvas. Keep figure captions outside the image in the patent document.
- Keep drawing canvases tight around the technical content: avoid excessive blank margins and reject outputs with unrelated titles, labels, watermarks, decorative elements, or unsupported modules.
- Keep claims definite. Avoid uncertain words such as "等", "大约", "优选", "可以", "比如", and "不限于" in claims.
- In `direct` mode, if source information is insufficient, generate explicit `【待补充：...】` placeholders and a material gap section instead of filling gaps with assumptions.
- In `human-in-loop` mode, ask for missing source material before generating final files when the gap would affect the technical solution or claim scope.
- Do not store user-provided papers, unpublished disclosures, generated drafts, API keys, tokens, local machine paths, or personal contact details in repository files.

## Common Requests

- "将这篇论文直接生成中国发明专利申请书 Word 和 PDF": draft the structured content, generate DOCX, and export PDF when available.
- "将这篇论文转换成中国发明专利申请文本": draft the five-part patent document, using text-only mode if no file is requested.
- "帮我写权利要求书": focus on claims and load the claim rules.
- "根据说明书生成专利附图": load the drawing rules and keep drawing terms aligned with claims and specification.
- "检查这份专利草稿是否忠实论文": use the quality checklist and report gaps or risky additions.
