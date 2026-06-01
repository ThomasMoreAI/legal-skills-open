---
name: evidence-authenticity-review
title: 证据真实性审查技能
description: 用于审查证据真实性的执行技能。真实性是证据"三性"的基础，本技能提供书证、物证、电子数据、证人证言等各类证据的实质性审查方法，包括来源审查、载体审查、内容审查和对比审查等。适用于诉讼准备、证据质证阶段。
author: sungaoxiang-backend
author_url: https://github.com/sungaoxiang-backend/intelligent-evidence-platform/tree/main/skills/evidence-authenticity-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cn
practice: litigation
language: zh
---

# 证据真实性审查技能

## Overview

本技能提供一套系统化的证据真实性审查方法，涵盖书证、物证、电子数据、证人证言等各类证据类型的审查要点，帮助律师准确判断证据是否真实可靠，为质证提供有力依据。

## Background

根据《最高人民法院关于民事诉讼证据的若干规定》第八十七条，人民法院对单一证据审核认定的第一项即是"证据是否为原件、原物"。真实性是证据的"地基"，地基不牢，地动山摇。证据真实性审查分为形式审查（快速筛查）和实质审查（深度解剖）两个层次。

## Action

### 审查证据真实性

根据证据类型，采用相应的审查方法。

#### 审查框架

```
┌─────────────────────────────────────────────────────────────────┐
│                    证据真实性审查框架                              │
└─────────────────────────────────────────────────────────────────┘

                              输入：证据
                                │
                                ▼
                    ┌─────────────────────┐
                    │   第一步：形式审查   │
                    │   核对原件/完整性    │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
                有明显问题              通过初审
                    │                     │
                    ▼                     ▼
              ┌──────────┐      ┌─────────────────────┐
              │排除证据  │      │ 第二步：实质审查    │
              └──────────┘      │ (来源/载体/内容/对比)│
                               └──────────┬──────────┘
                                          │
                              ┌───────────┼───────────┐
                              │           │           │
                              ▼           ▼           ▼
                          来源审查    载体审查    内容/对比审查
```

#### 按证据类型的审查要点

**1. 书证审查**

| 审查项 | 审查方法 | 瑕疵表现 |
|-------|---------|---------|
| 原件核对 | 触摸印章凹凸感，检查纸张新旧 | 彩印冒充原件，纸张过于白净 |
| 笔迹鉴定 | 起笔、行笔、收笔特征分析 | 笔画抖动、不自然的断连 |
| 印章鉴定 | 印文形态、边框线条、微观瑕疵 | 印文边缘有锯齿、拼接痕迹 |
| 内容一致性 | 与已知事实对比验证 | 出现未启用地名、矛盾表述 |

**2. 电子数据审查**

| 审查项 | 审查方法 | 瑕疵表现 |
|-------|---------|---------|
| 元数据分析 | 创建时间、修改时间、设备信息 | 修改时间晚于声称形成时间 |
| 完整性验证 | 哈希值比对、数字签名验证 | 数据被篡改、不完整 |
| 来源追踪 | 发送者身份、传输路径 | 冒名发送、转发篡改 |
| 公证保全 | 检查公证书、时间戳 | 未经公证的易逝数据 |

**3. 证人证言审查**

| 审查项 | 审查方法 | 瑕疵表现 |
|-------|---------|---------|
| 感知能力 | 位置、光线、角度、视力条件 | 位置偏远、光线昏暗仍称看清 |
| 记忆情况 | 时间间隔、是否受干扰 | 证词前后矛盾、受媒体影响 |
| 利害关系 | 亲属、朋友、雇佣关系 | 存在利益关联或情感倾向 |
| 陈述一致性 | 与其他证据交叉印证 | 独自无佐证、与实物证据矛盾 |

**4. 物证审查**

| 审查项 | 审查方法 | 瑕疵表现 |
|-------|---------|---------|
| 原物核实 | 与记录描述对比 | 复制品与原物不符 |
| 保存状态 | 检查保存环境、链条 | 保管不善、污染损毁 |
| 专业鉴定 | 成分分析、痕迹鉴定 | 鉴定条件不具备 |

## Parameters

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Evidence Authenticity Review",
  "type": "object",
  "properties": {
    "evidence_type": {
      "type": "string",
      "enum": ["document", "digital", "testimony", "object", "audio_visual"],
      "description": "证据类型"
    },
    "has_original": {
      "type": "boolean",
      "description": "是否有原件"
    },
    "provided_by": {
      "type": "string",
      "enum": ["party", "third_party", "court"],
      "description": "证据提供方"
    },
    "review_focus": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": ["source", "carrier", "content", "comparison", "metadata"]
      },
      "description": "审查重点"
    },
    "party_position": {
      "type": "string",
      "description": "己方当事人立场（原告/被告）"
    }
  },
  "required": ["evidence_type", "has_original"]
}
```

## Output Schema

```json
{
  "authenticity_review": {
    "overall_assessment": {
      "authenticity": "verified|questionable|unverified",
      "confidence": "high|medium|low",
      "recommendation": "accept|challenge|exclude"
    },
    "detailed_findings": {
      "original_check": "passed|failed|not_applicable",
      "carrier_analysis": "详细发现",
      "content_analysis": "内容真实性评估",
      "comparison_result": "与其他证据对比结果"
    },
    "challenge_points": [
      "可质疑的具体问题点"
    ],
    "cross_examination_suggestions": [
      "质证意见建议"
    ]
  }
}
```

## Legal Guardrails

**风险提示：**
- 无原件的证据，真实性存疑，可不予认可
- 电子证据易被篡改，需验证元数据和完整性
- 证人证言主观性强，需交叉询问验证
- 书证需注意是否为套打、空白盖章后添加内容

**质证策略：**
- 对己方不利证据：严格审查真实性，发现问题坚决不认
- 对己方有利证据：提前核实原件，避免庭上被动
- 对案外人出具证据：可认可形式真实但不认内容真实

**合规要求：**
- 真实性质证意见应基于客观审查结果
- 不得恶意质疑真实证据损害诚信
- 庭前应让委托人确认签字印章真实性

## Metadata

| 属性 | 值 |
|-----|-----|
| `logic_origin` | 《诉讼律师证据工作实战指引》《各类证据的真实性审查要点》《实务技能质证技巧》 |
| `evolution_value` | 系统化真实性审查方法，避免虚假证据被采信，保护当事人权益 |
| `execution_context` | 诉前证据审查、庭审质证阶段 |

## Test Cases

### 测试用例 1：书证真实性审查（有原件）

**输入：**
```json
{
  "evidence_type": "document",
  "has_original": true,
  "provided_by": "party",
  "review_focus": ["source", "carrier", "content"],
  "party_position": "被告"
}
```

**期望输出：**
```json
{
  "authenticity_review": {
    "overall_assessment": {
      "authenticity": "questionable",
      "confidence": "medium",
      "recommendation": "challenge"
    },
    "detailed_findings": {
      "original_check": "passed",
      "carrier_analysis": "纸张过于白净，声称签订于三年前但纸张崭新，存在伪造嫌疑",
      "content_analysis": "合同中出现了五年前才启用的新地名，内容真实性存疑",
      "comparison_result": "与双方其他交易习惯存在不一致"
    },
    "challenge_points": [
      "纸张形成时间与声称签订时间不符",
      "内容包含时代错误信息",
      "建议申请笔迹和印章鉴定"
    ],
    "cross_examination_suggestions": [
      "对该证据的真实性不予认可",
      "纸张过于白净，与声称形成时间严重不符",
      "内容中出现的地名在声称签订时并不存在",
      "申请对笔迹、印章形成时间进行司法鉴定"
    ]
  }
}
```

### 测试用例 2：电子数据审查（微信聊天记录）

**输入：**
```json
{
  "evidence_type": "digital",
  "has_original": false,
  "provided_by": "party",
  "review_focus": ["metadata", "source", "content"],
  "party_position": "原告"
}
```

**期望输出：**
```json
{
  "authenticity_review": {
    "overall_assessment": {
      "authenticity": "unverified",
      "confidence": "low",
      "recommendation": "challenge"
    },
    "detailed_findings": {
      "original_check": "failed",
      "carrier_analysis": "未提供原始载体，仅有截图，无法验证完整性",
      "content_analysis": "截图存在编辑痕迹，部分内容模糊不清",
      "comparison_result": "与对方当事人陈述存在重大矛盾"
    },
    "challenge_points": [
      "未提供原始载体，仅提供截图",
      "截图可能经过编辑、删减",
      "无法验证电子数据的完整性和真实性"
    ],
    "cross_examination_suggestions": [
      "该证据没有原件，对真实性无法核实，故对真实性不予认可",
      "根据《最高人民法院关于民事诉讼证据的若干规定》第十五条，电子数据应当提供原件",
      "请法庭责令对方提供原始载体或经过公证的电子数据"
    ]
  }
}
```

### 测试用例 3：证人证言审查

**输入：**
```json
{
  "evidence_type": "testimony",
  "has_original": true,
  "provided_by": "witness",
  "review_focus": ["source", "content", "comparison"],
  "party_position": "被告"
}
```

**期望输出：**
```json
{
  "authenticity_review": {
    "overall_assessment": {
      "authenticity": "questionable",
      "confidence": "medium",
      "recommendation": "challenge"
    },
    "detailed_findings": {
      "original_check": "passed",
      "carrier_analysis": "证人与原告系多年好友关系",
      "content_analysis": "证人声称在昏暗光线下清晰辨认被告面孔，违背常理",
      "comparison_result": "证言与监控视频记录存在矛盾"
    },
    "challenge_points": [
      "证人与原告存在利害关系",
      "感知条件不足（光线昏暗）",
      "证言与客观证据（监控）矛盾"
    ],
    "cross_examination_suggestions": [
      "证人与原告系多年好友关系，存在利害关系",
      "证人作证时光线条件不足，不可能清晰辨认",
      "证言内容与监控视频记录相互矛盾",
      "建议法庭对该证人证言的证明力不予采信"
    ]
  }
}
```

## Related Skills

- `evidence-cross-examination`: 庭审质证技巧（三性完整质证）
- `evidence-admissibility-check`: 证据可采性综合判断
- `evidence-list-compilation`: 证据清单一览表制作
- `evidence-review-methodology`: 证据审查四法则
