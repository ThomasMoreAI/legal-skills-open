---
name: review
title: /review
description: 根据审查指引审查供应商协议、保密协议或SaaS订阅。从标题识别协议结构， 路由至正确的审查技能，并将输出整合为单一备忘录。当用户说"审查这个合同" "检查这个主协议""这个保密协议可以吗""看看这个SaaS协议"或附上接收方协议供审查时使用。
author: zhou210712
author_url: https://github.com/zhou210712/claude-for-legal-ZH/tree/main/commercial-legal/skills/review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: zh
---

# /review

根据审查指引审查接收方协议。从标题识别协议结构，选择合适的技能，如 `confirm_routing` 启用则在继续前与用户确认。

## 指令

1. **加载审查指引。** 如果存在占位符，停止并提示运行 `/commercial-legal:cold-start-interview`。同时读取 `## 审查偏好` → `confirm_routing`。

2. **获取协议：** 从文件路径、云文档链接、合同管理系统ID或粘贴文本获取。

3. **读取文件结构——先看标题。** 提取主协议标题和全部展示件/附件标题。这是路由信号。

4. **根据文件结构选择技能。**

   | 文件/条款标题包含 | 技能 |
   |---|---|
   | 保密协议、NDA、保密协议书（作为*主*协议） | **保密协议审查** |
   | 主服务协议、专业服务、工作说明书、咨询服务协议 | **供应商协议审查** |
   | 订阅、SaaS、云服务、带自动续约的订单、带周期性费用的软件许可 | **SaaS审查**（叠加于供应商协议审查之上） |
   | 数据处理协议、DPA（作为展示件或独立文件） | 注记供**供应商协议审查**→数据保护部分 |

   多个技能可适用。常见组合：MSA + DPA展示件 → 供应商协议审查，附DPA注记。

5. **如果启用，确认路由。** 如果 `confirm_routing` 为 `true`：

   ```
   我将按以下方式审查：[协议类型]。
   
   已识别文件：
   - [主协议标题] → [技能]
   - [展示件A标题] → [如何处理]
   
   是否正确？（是/否——或告诉我哪里不对）
   ```

   等待确认。如果 `confirm_routing` 为 `false`：无声继续。

6. **运行技能。** 完全执行每个技能的工作流。如多个技能适用，依次运行并将输出整合为单一备忘录。

7. **检查上报：** 如果任何问题超出审查者权限，调用**上报标注器**路由并起草上报说明。

8. **提供后续操作：** 给业务负责人的利益方摘要、带修订痕迹的.docx、合同管理系统记录创建、加入续约登记册。

## 示例

```
/commercial-legal:review vendor-msa.pdf
/commercial-legal:review https://drive.google.com/file/d/ABC123
/commercial-legal:review
[粘贴协议文本]
```

## 输出

按技能格式的完整审查备忘录。路由决定记录在顶部。逐条偏离、具体修订语言、具名审批人。
