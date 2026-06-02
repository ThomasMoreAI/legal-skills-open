---
name: investigation-memo-zhou210712
title: /investigation-memo
description: 从调查日志起草或更新调查备忘录。当调查进展到可以撰写第一版备忘录时， 或当新数据已添加且现有草案需要更新时使用。
author: zhou210712
author_url: https://github.com/zhou210712/claude-for-legal-ZH/tree/main/employment-legal/skills/investigation-memo
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cn
practice: employment
language: zh
---

# /investigation-memo

从调查日志起草第一版调查备忘录，或当新数据已添加时更新现有草案。

## 指令

1. 加载调查日志并运行起草/更新模式。
2. 如为首次起草，警告证据来源清单中是否仍有高优先级来源未获取。
3. 如为更新，改写前显示变更内容。
4. 所有输出标注"保密 · 内部调查工作成果 —— 受律师保密义务保护"。

## 调查备忘录结构

```markdown
保密 · 内部调查工作成果

# 调查备忘录：[调查事项名称]

**调查期间：** [开始日期] — [日期]
**调查人员：** [姓名/角色]

---

## 一、投诉/举报概述

[投诉来源、时间、内容摘要]

## 二、调查过程

[取证情况、访谈人员及日期]

## 三、事实发现

[按时间线或争议焦点组织，每个发现附证据引用]

## 四、证据分析

[证据的三性审查——真实性、合法性、关联性]
[证据之间的矛盾和印证关系]

## 五、初步结论

[基于现有证据的事实认定]
[存在的证据缺口和不确定性]

## 六、建议

[处理建议及法律依据]
```

**保密说明（《律师法》第38条）。** 本备忘录包含律师在执业活动中知悉的保密信息，受《律师法》第38条保密义务保护。`[法条原文]` 在中国法下不存在独立的"attorney work product"保护制度，法院有权依法调取相关材料。建议将本备忘录与外部律师的法律意见书分开管理。

## 示例

```
/employment-legal:investigation-memo [调查事项名称]
```

```
/employment-legal:investigation-memo [调查事项名称]
（如已有草案则更新）
```
