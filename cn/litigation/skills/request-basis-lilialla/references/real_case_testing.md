# Real Case Testing

Use this reference when a user wants to test the skill on a live or past real matter.

## Operating Posture

Treat real case work as a pilot run, not as a final opinion. The goal is to produce a useful litigation map and expose skill defects.

## Input Gate

Before deep analysis, ask for or infer:

1. test goal: claim design, evidence mapping, defense scan, research queue, or full first-pass map;
2. material register: numbered contracts, pleadings, correspondence, payment records, chats, expert reports, or judgments;
3. party aliases: use roles or neutral labels where possible;
4. current procedural posture;
5. output depth and whether the user wants broad mapping or a focused claim.

If the user provides raw materials directly, continue with litigation mode but label all factual content carefully.

## Source Handling

- Do not put real matter materials into repository data, evals, or docs.
- Do not convert private case details into permanent examples.
- Convert reusable lessons into abstract failure patterns only.
- Keep party assertions, evidence content, evidence-supported facts, disputed facts, and model inferences separate.

## Required Real-Case Output Additions

In addition to the litigation mode skeleton, include:

```markdown
## 测试反馈记录

| 问题类型 | 观察到的问题 | 可能原因 | 建议修复位置 | 是否进入仓库 |
| --- | --- | --- | --- | --- |
```

Use this section to capture skill defects such as omitted request bases, evidence/fact confusion, cause-of-action overreach, missing verification tasks, or unusable output shape.

## Promotion Rule

Only promote a real-case lesson into repository files when it is:

- abstracted away from private facts;
- repeatable across cases;
- tied to a concrete repair location;
- not merely a disagreement over one possible legal strategy.
