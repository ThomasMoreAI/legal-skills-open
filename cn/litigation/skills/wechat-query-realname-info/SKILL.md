---
name: wechat-query-realname-info
title: 微信实名认证信息调取技能
description: 用于调取微信实名认证信息的执行技能。通过法院发协助函或律师持调查令向财付通支付科技有限公司申请调取目标微信号的实名认证信息，获取真实姓名、身份证号等权威身份证明。此技能仅适用于已确认实名认证的微信号。
author: sungaoxiang-backend
author_url: https://github.com/sungaoxiang-backend/intelligent-evidence-platform/tree/main/skills/wechat-query-realname-info
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cn
practice: litigation
language: zh
---

# 微信实名认证信息调取技能

## Overview

本技能指导律师或法院工作人员通过合法程序向财付通（微信支付运营主体）调取微信号实名认证信息，获取包含真实姓名、身份证号码、微信号等信息的权威复函，是证明微信使用者身份的最有力证据。

## Background

根据调研文章，对于已实名认证的微信号，可以通过法院发协助函或律师持调查令的方式，向财付通支付科技有限公司申请调取实名认证信息。财付通的复函中会清晰显示认证者的真实姓名、身份证号码、微信号等信息，其法律效力极高。

## Action

### 调取微信实名认证信息

通过法院或律师渠道向财付通申请调取实名认证信息。

**执行路径：**

| 申请人类型 | 所需文件 | 申请对象 |
|-----------|---------|---------|
| 法院 | 协助执行函/调查函 | 财付通支付科技有限公司 |
| 律师 | 律师调查令（法院签发） | 财付通支付科技有限公司 |

**调取信息内容：**
- 真实姓名（完整）
- 身份证号码（完整）
- 微信号
- 实名认证状态
- 认证时间等

**财付通联系信息：**
- 公司名称：财付通支付科技有限公司
- 地址：深圳市南山区科技园
- 注：具体联系地址和流程可能需要通过法院渠道获取最新信息

## Parameters

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "WeChat Realname Info Query",
  "type": "object",
  "properties": {
    "applicant_type": {
      "type": "string",
      "enum": ["court", "lawyer"],
      "description": "申请人类型"
    },
    "case_info": {
      "type": "object",
      "properties": {
        "case_number": {"type": "string", "description": "案号"},
        "court_name": {"type": "string", "description": "受理法院"},
        "case_type": {"type": "string", "description": "案件类型"}
      },
      "required": ["case_number", "court_name"]
    },
    "target_wechat_id": {
      "type": "string",
      "description": "目标微信号"
    },
    "target_user_alias": {
      "type": "string",
      "description": "目标用户的推测/已知姓名（如有）"
    },
    "application_purpose": {
      "type": "string",
      "description": "申请目的/证明事项"
    }
  },
  "required": ["applicant_type", "case_info", "target_wechat_id"]
}
```

## Output Schema

```json
{
  "query_result": {
    "status": "success|pending|rejected",
    "tenpay_response": {
      "response_date": "ISO 8601 date",
      "response_reference": "复函编号",
      "realname": "真实姓名",
      "id_number": "身份证号",
      "wechat_id": "微信号",
      "verification_status": "verified|unverified"
    },
    "evidence_usability": {
      "has_official_seal": true,
      "legal_validity": "high|medium|low",
      "recommended_usage": "direct_evidence|supporting_evidence"
    }
  }
}
```

## Legal Guardrails

**风险提示：**
- 本技能仅适用于已实名认证的微信号，未实名账号无法通过此途径获取信息
- 调取过程必须通过合法的司法程序，不得通过非法渠道购买
- 财付通复函的获取周期视具体流程而定，可能需要数周时间

**合规要求：**
- 必须持有法院签发的协助函或律师调查令
- 调取的信息仅用于本案诉讼活动，不得用于其他目的
- 应妥善保管复函原件，庭审时需出示原件

**证据效力：**
- 财付通复函属于第三方权威机构出具的证明，证据效力极高
- 复函需加盖财付通公司公章方具有完整法律效力

## Metadata

| 属性 | 值 |
|-----|-----|
| `logic_origin` | 《如何在法庭上证明微信使用者的真实身份》第02节 |
| `evolution_value` | 获取最权威的身份证明材料，直接证明微信使用者的真实身份，显著提升证据效力 |
| `execution_context` | 诉讼中、诉前调查阶段 |

## Test Cases

### 测试用例 1：律师持调查令调取信息

**输入：**
```json
{
  "applicant_type": "lawyer",
  "case_info": {
    "case_number": "（2025）粤0305民初1234号",
    "court_name": "深圳市南山区人民法院",
    "case_type": "民间借贷纠纷"
  },
  "target_wechat_id": "wxid_debtor2025",
  "target_user_alias": "张三",
  "application_purpose": "证明微信号 wxid_debtor2025 的使用者真实身份，用于确认借贷关系当事人"
}
```

**期望输出：**
```json
{
  "query_result": {
    "status": "success",
    "tenpay_response": {
      "response_date": "2025-03-15",
      "response_reference": "财付通复函〔2025〕第XXX号",
      "realname": "张某三",
      "id_number": "440***********1234",
      "wechat_id": "wxid_debtor2025",
      "verification_status": "verified"
    },
    "evidence_usability": {
      "has_official_seal": true,
      "legal_validity": "high",
      "recommended_usage": "direct_evidence"
    }
  }
}
```

### 测试用例 2：法院发函调取信息

**输入：**
```json
{
  "applicant_type": "court",
  "case_info": {
    "case_number": "（2025）京0108民初5678号",
    "court_name": "北京市海淀区人民法院",
    "case_type": "买卖合同纠纷"
  },
  "target_wechat_id": "seller_wxid888",
  "application_purpose": "核实交易对方身份，确认合同相对方"
}
```

**期望输出：**
```json
{
  "query_result": {
    "status": "success",
    "tenpay_response": {
      "response_date": "2025-02-20",
      "response_reference": "协查函复〔2025〕第XXX号",
      "realname": "李某四",
      "id_number": "110***********5678",
      "wechat_id": "seller_wxid888",
      "verification_status": "verified"
    },
    "evidence_usability": {
      "has_official_seal": true,
      "legal_validity": "high",
      "recommended_usage": "direct_evidence"
    }
  }
}
```

## Related Skills

- `wechat-verify-realname`: 调取前先确认微信号是否已实名认证
- `wechat-apply-transfer-proof`: 如存在转账记录，可同时申请电子回单作为补充证据
- `wechat-present-evidence`: 获取复函后在法庭上展示证据的规范流程
