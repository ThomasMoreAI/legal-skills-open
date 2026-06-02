---
name: ai-intelligent-contract-review
title: AI 智能合同审查系统
description: Automates contract review by identifying clause risks, comparing against standard contracts, and managing contract lifecycles including expiry reminders and archiving. Best used by legal, procurement, sales, and HR teams handling high volumes of contracts.
author: luokai0
author_url: https://github.com/luokai0/ai-agent-skills-by-luo-kai/tree/main/ai-agent-skills/22-clawhub-skills/ai-intelligent-contract-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: zh
---

# AI 智能合同审查系统

## 描述
自动化合同审查，风险识别 + 条款分析。

## 功能
- 风险识别（条款风险标注）
- 条款对比（标准合同对比）
- 合同生成（智能填充）
- 到期提醒（自动续约提醒）
- 合同归档（电子化管理）

## 定价
- 基础版：¥299/月（50 份合同/月）
- 专业版：¥1499/月（300 份合同/月）
- 企业版：¥4999/月（无限合同）

## 适用场景
- 法务部门
- 采购合同
- 销售合同
- 劳动合同

## 技术栈
- Python + FastAPI
- NLP（合同解析）
- 风险识别模型
- 文档管理

## 安装
```bash
git clone https://github.com/openclaw-skills/ai-intelligent-contract-review
cd ai-intelligent-contract-review
pip install -r requirements.txt
python app.py
```

---
创建：2026-03-13
作者：OpenClaw Skills Team
