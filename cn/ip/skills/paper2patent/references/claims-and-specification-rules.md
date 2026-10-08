# Claims and Specification Rules

## Claim Rules

- Keep the invention name identical to the name used in the abstract.
- Use "其特征在于" to introduce technical features.
- Every claim must have one final Chinese period only. Use semicolons or commas inside the claim.
- Avoid uncertain claim words: "等", "大约", "可能", "也许", "例如", "比如", "优选", "可以", "不限于", "部分", "某些", "若干", "某种程度上", and "基本".
- Dependent claims must cite an earlier claim that actually contains the referenced feature.
- Multi-dependent claims must not depend on other multi-dependent claims.
- Do not copy paper sentences directly. Rewrite into patent step or module language.

## Independent Claims

For a method invention, use a step structure:

```text
1.一种[发明名称]方法，其特征在于，包括：
[步骤A]；
[步骤B]；
[步骤C]。
```

For a system invention, use a module structure:

```text
2.一种[发明名称]系统，其特征在于，包括：
[模块A]，配置为...；
[模块B]，配置为...；
[模块C]。
```

Only include a system claim when the paper supports a system, architecture, device, or module arrangement.

## Specification Structure

Use these subsections:

- 技术领域: state the technical field in one concise paragraph.
- 技术背景: explain technical definitions, existing methods, existing problems, why the problems occur, and their consequences.
- 发明内容: summarize the solution, detail the technical means, and explain source-supported technical effects.
- 附图说明: list each figure in one sentence.
- 具体实施方式: describe each important step or module in enough detail for implementation.

The structure and depth should follow `reference_skills/meterial.md`: technical background must include definitions, existing technology, and existing problems; invention content must include a summary, detailed technical solution, and technical effects; embodiments must explain what each key step is, what problem it solves, how it operates, and what result it produces.

## Embodiment Depth

For each important step, answer in patent language:

- What the step or module is.
- What problem it addresses.
- How it operates using source-supported information.
- What output or technical effect it produces.

## Common Failures

- Claim scope is broader than the paper supports.
- Claims include "等" or other indefinite language.
- The background states problems not identified by the paper.
- The embodiment reads like a paper translation rather than a patent implementation.
- Drawings introduce modules or connections absent from the claims or specification.
- Drawings or captions use terms that differ from the claims, specification, or source paper figure descriptions.
