# Retrieval

Use this reference when a task needs local books, lecture materials, catalog candidates, or case-training examples.

## Default Order

1. Start from the current claim goal, request-basis name, rule-obligation group id, article number, or candidate cause of action.
2. Search the source registry for source scope and source status.
3. Search the source locator index or use the local retrieval tool when available.
4. Read only the source lines returned by the match.
5. Label the result as `source_extracted`, `scholarly_reference`, `case_training_sample`, or another source label. Do not upgrade it to verified law.

## Local Search

When a local retrieval tool is available, prefer targeted queries by layer, for example:

```bash
<retrieval_search> "关键词" --layer core_reference
<retrieval_search> "关键词" --layer case_training
```

Useful queries include:

- claim goal: `支付价款`, `返还原物`, `赔偿损失`, `停止侵害`;
- request-basis name: `价款支付请求权`, `不当得利返还请求权`;
- structure terms: `构成要件`, `抗辩`, `检视顺序`, `请求权基础`;
- article or instrument: `第145条`, `合同编通则解释`;
- court guidance or minutes: `九民纪要`, `会议纪要`, `审判会议纪要`;
- cause of action: `买卖合同纠纷`, `医疗损害责任纠纷`.

## Reading Limits

- Do not load any whole large source material file.
- Do not load the source locator index wholesale unless the task is index maintenance.
- For catalog work, review one row or one batch at a time.
- For litigation work, retrieve local materials only after the claim goals and proof issues are identified.

## Source Priority

- `core_reference`: method, catalog seeds, legal-system scaffolding.
- `case_training`: examples, exam style, issue spotting, modified facts.
- `conversion_artifact`: OCR traceability only.
- statutes, judicial interpretations, court guidance, minutes, papers, and cases added later must first be indexed, then integrated through the source-integration reference.
- MCP or other authority source: required before stating current law, judicial interpretation status, or court practice.
