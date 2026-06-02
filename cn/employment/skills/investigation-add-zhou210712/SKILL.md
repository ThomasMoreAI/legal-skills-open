---
name: investigation-add-zhou210712
title: /investigation-add
description: 向进行中的调查添加数据——文件、访谈记录或观察意见。 按已记录的筛选标准批量处理，浮现重要事项，记录所有已审查内容 以供覆盖验证。当新的证据、访谈记录或文件材料进入进行中的调查时使用。
author: zhou210712
author_url: https://github.com/zhou210712/claude-for-legal-ZH/tree/main/employment-legal/skills/investigation-add
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cn
practice: employment
language: zh
---

# /investigation-add

向进行中的调查日志添加数据。使用已记录的筛选标准处理文件批次，浮现重要事项，记录所有已审查内容以供覆盖验证。

## 指令

1. 加载 `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`。
2. 运行添加数据模式：
   - 将新数据追加到调查日志
   - 按筛选标准评估：是否与调查要点相关？是否重要？
   - 输出浮现比例和已浮现事项列表
3. 处理完成后，显示浮现比例和已浮现事项列表。
4. 如果数据覆盖了证据来源清单中的某项，提示更新清单。

## 证据筛选标准

添加数据时，按以下维度评估：

| 维度 | 检查 |
|---|---|
| 相关性 | 该证据是否与待证事实相关？ |
| 真实性 | 该证据是否可核验来源和真实性？ |
| 合法性 | 该证据的获取方式是否合法？（《劳动争议司法解释（一）》关于证据合法性） |
| 重要性 | 该证据是否会影响调查结论？ |

## 保密要求

所有添加的数据受《律师法》第38条保密义务保护。`[法条原文]` 注意区分：
- 原始材料（投诉信、聊天记录、邮件等）——保持原样，不修改
- 调查分析意见——属于律师工作成果，标注保密
- 日志条目——记录处理过程，不替代调查分析

## 示例

```
/employment-legal:investigation-add [调查事项名称]
[粘贴访谈记录]
```

```
/employment-legal:investigation-add [调查事项名称]
[附上邮件导出文件]
```
