---
name: clo-legal-kb
title: 📍 法务知识库
description: Captures and organizes reusable legal knowledge after each legal task, categorizing outputs into regulation summaries, contract templates, risk checklists, and CEO preferences for easy future retrieval.
author: Deepleaper
author_url: https://github.com/Deepleaper/leaper-agent/tree/master/skills/skills/L3-workstation/clo-legal-kb
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: zh
tags: [clo, knowledge]
---

# 📍 法务知识库

## 触发条件
- 每次法务工作完成后自动沉淀
- CEO 问"之前那个合同怎么处理的"
- 需要复用历史法务经验

## 输入要求
1. 法务工作输出（自动收集）
2. CEO 反馈和决策结果（可选）

## 执行步骤
1. 从本次法务工作中提取可复用知识
2. 分类归档：法规摘要/合同模板/风险清单/CEO偏好
3. 更新MEMORY知识库
4. 建立索引方便检索

## 输出模板

### 知识条目
- **类型**：法规/模板/风险清单/偏好
- **标题**：xxx
- **摘要**：xxx
- **来源**：xxx（日期+场景）
- **复用场景**：xxx

> ⚠️ AI 法律分析仅供参考，重大事项请咨询持牌律师

## 异常处理
- 法规已过时 → 标注失效日期，搜索更新版本
- 知识冲突 → 以最新法规为准，保留历史版本做对比

## 边界
- 不做：法规数据库的系统性建设（→ 专业法律数据库）
