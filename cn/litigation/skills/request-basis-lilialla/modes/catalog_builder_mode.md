# Catalog Builder Mode

Use for building and maintaining the request-basis data layer from local Markdown, OCR/MinerU JSON, tables, headings, manually marked excerpts, new academic materials, laws, judicial interpretations, court guidance, cases, user checklists, concept cards, and rule-obligation groups.

## Workflow

1. Identify extraction scope: file, heading, line range, JSON page/block, table.
2. Use the retrieval reference to locate snippets; do not load whole books.
3. Use catalog review batches to pick one cause-context batch when available; this is extraction context, not runtime case classification.
4. If the task adds a new source or updates an existing topic, follow the source-integration reference.
5. Extract atomic source assertions first; then map them to professional concepts, claim, request basis/norm basis, elements, defenses, evidence targets, and rule nodes.
6. If the material defines or distinguishes a professional term, build or update a concept card before using it in a rule-obligation group.
7. If the extracted material is reusable across claims or sources, build or update a rule-obligation group with `entry_mappings`.
8. Preserve source path, line/page/block id.
9. Mark extracted entries:
   - `source_status: source_extracted`
   - `verification_status: unverified`
   - `mcp_verification_required: true`
10. For current-law, judicial-interpretation, court guidance, special-law, minutes, or case-law questions, add verification tasks to the verification queue when available.
11. Mark OCR doubts and source conflicts as `needs_human_review` or `conflict_detected`.
12. Validate JSONL/YAML before committing.

## Output Skeleton

```markdown
# Catalog 抽取报告

## 1. 抽取范围

## 2. 新增条目

| id | 名称 | 案由 | 诉请 | 来源 | 状态 |
| --- | --- | --- | --- | --- | --- |

## 3. 字段缺口

## 4. 规则义务群更新

| group id | 请求目标 | 请求权基础 | 候选案由 | 规则节点 | 状态 |
| --- | --- | --- | --- | --- | --- |

## 5. 来源命题合并

## 5A. 专业概念卡更新

| concept id | term | trigger facts | adjacent concepts | source | status |
| --- | --- | --- | --- | --- | --- |

| assertion | source | merged into | conflict/verification |
| --- | --- | --- | --- |

## 6. OCR/表格/来源冲突疑点

## 7. MCP/权威核验任务

## 8. 人工审查任务
```

## Guardrails

- Do not upgrade local extraction to verified law.
- Do not invent article numbers.
- Do not merge distinct request bases for convenience.
- Do not merge same-looking propositions if their legal effect, trigger condition, time effect, or source authority differs.
- Do not put defenses into `claim_texts`; map defenses under `defenses`.
- Do not mark an entire rule-obligation group verified when only one rule node has been authority-checked.
