# Text Conversion Workflow

## Internal Execution Order

1. Read the paper and extract only source-supported technical content.
2. Identify the difference point, technical problem, technical solution, and technical effect.
3. Choose a consistent invention name.
4. Draft the five patent sections in order as structured content, following the detailed structure and hard constraints from `reference_skills/meterial.md`.
5. Add explicit `【待补充：...】` placeholders for required content that the paper does not support.
6. Run the quality checklist and revise silently.
7. Output the requested artifact: DOCX/PDF for full direct generation, or plain text only in `text-only` mode.

Do not expose chain-of-thought, hidden analysis, self-reflection, or checklist results in the final draft.

## Five-Part Patent Structure

For a full Chinese invention patent draft, assemble these sections:

1. 说明书摘要
2. 摘要附图
3. 权利要求书
4. 说明书
5. 说明书附图

Use this structure as the content model for Word/PDF generation. In `text-only` mode, the default final format is:

```text
一、说明书摘要
...

二、摘要附图
...

三、权利要求书
1.一种[发明名称]，其特征在于，包括：
...

四、说明书
技术领域
...

五、说明书附图
...
```

## Section Guidance

- 说明书摘要: no more than 300 Chinese characters when possible. Include name, field, core solution, and technical effect. If drawings are present, reference the selected abstract drawing.
- 摘要附图: select the drawing that best represents the core method or architecture. If none exists, state that there is no abstract drawing.
- 权利要求书: normally 6-10 claims. Include 1-2 independent claims and supported dependent claims.
- 说明书: include technical field, background, invention content, drawing descriptions, and detailed embodiments. The background must cover technical definitions, existing methods, existing problems, causes, and consequences. The invention content must cover summary, technical-solution details, and source-supported technical effects.
- 说明书附图: describe and, for full documents, generate black-and-white flowcharts, system block diagrams, or data flow diagrams that match the source paper, claims, and specification.

## Source-Figure First Drawing Order

When drawings are requested, build them before final DOCX assembly:

1. Extract candidate source figures from the paper PDF, screenshots, figure captions, or architecture descriptions.
2. Identify the source-supported steps, modules, data nodes, arrows, and figure purpose.
3. Redraw the source figure as a clean patent reference drawing; do not copy visual styling, colors, titles, or paper layout artifacts.
4. Use the generated patent text only to normalize terminology, step numbering, component labels, and captions.
5. If the source figure and patent text conflict, report a material gap instead of inventing a reconciled structure.

## Fidelity Principle

Patent-style abstraction is allowed; technical invention is not. A claim may generalize a paper-supported step, but must not add new modules, deployment environments, hardware limits, application scenarios, metrics, or causal effects absent from the paper.

## File-Generation Content Model

For full document generation, convert the five-part draft into the JSON contract in `document-generation.md`. Keep section labels stable so the DOCX generator can render:

- `abstract` for 说明书摘要.
- `abstract_drawing` for 摘要附图.
- `claims` as an ordered list.
- `description` with `technical_field`, `background`, `invention_content`, `drawing_description`, and `embodiments`.
- `drawings` as the 说明书附图 specifications.
- `source_figures` for source-paper figure metadata when available.
- `drawing_assets` for generated SVG/PNG reference drawing metadata.
- `image_model_prompts` for Image2-style refinement prompts.
- `drawing_validation` for title-pollution, whitespace, and line-drawing checks.
- `gaps` for all remaining placeholders or missing source material.
