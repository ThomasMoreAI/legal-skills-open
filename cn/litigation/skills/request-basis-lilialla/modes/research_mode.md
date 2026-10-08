# Research Mode

Use for current law and case-law verification. The local repository frames questions; MCP or another authoritative source verifies law and court practice.

## Mandatory MCP/Authority Search

Required when answering:

- current law or judicial interpretation;
- validity, amendment, repeal, or time effect;
- court practice, usual holdings, judicial tendency;
- local/departmental rules;
- case-law paths for a dispute issue.

## Workflow

1. State research question.
2. If available, use a rule-obligation group to frame request bases, elements, defenses, and candidate causes of action.
3. If local materials are useful for framing, use the retrieval reference to retrieve only targeted snippets.
4. Define scope: jurisdiction, time range, court level, keywords.
5. Retrieve current law and record validity.
6. Retrieve case-law and build a path matrix.
7. Score comparability: fact, claim, norm, evidence, time, region/court level.
8. Distinguish support paths, contrary paths, and open questions.
9. Compare with local scholarly/reference material if useful.
10. Update or create verification-queue tasks for unresolved law, judicial interpretation, or case-law questions when the package has a queue.

## Output Skeleton

```markdown
# 法规与类案研究校验

## 1. 研究问题

## 2. 检索范围

## 3. 本地规则义务群框架

| 规则义务群 | 请求权基础 | 要件/抗辩提示 | 候选案由/关键词 | 核验状态 |
| --- | --- | --- | --- | --- |

## 4. 现行规范

| 规范 | 条文 | 效力状态 | 适用范围 | 来源 |
| --- | --- | --- | --- | --- |

## 5. 类案裁判路径

| 案件 | 法院 | 日期 | 争点 | 裁判要点 | 可比性 |
| --- | --- | --- | --- | --- | --- |

## 6. 分歧与边界

## 7. 结论等级

## 8. 回填建议

| target | status update | source | still open |
| --- | --- | --- | --- |
```

## Guardrails

- Avoid “法院通常认为” unless sample scope and contrary cases are addressed.
- Do not treat scholarly material as verified law.
- Record retrieval metadata whenever available.
- If verification is partial, update only the verified rule node or source assertion; do not mark the whole rule-obligation group as verified.
