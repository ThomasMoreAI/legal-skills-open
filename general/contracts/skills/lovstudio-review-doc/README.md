# 合同精修 · Contract Polish

![Version](https://img.shields.io/badge/version-1.1.1-CC785C) ![Category](https://img.shields.io/badge/category-business-blue)

合同专家审阅：分析交易结构与法律风险，输出逐条批注、红线修订、替代条款、谈判方案和签署建议。

## 核心能力

- 七轮审阅：交易结构、定义一致性、权利义务、风险分配、合同生命周期、合规争议、可操作与可举证。
- 双维度分级：风险分为致命、高、中、低、提示；谈判分为必须坚持、优先争取、可交换、可接受。
- 真人律师式批注：每条说明问题、原因、实际后果、首选修改与退让方案。
- DOCX 原位批注和修订，覆盖正文、表格、页眉与页脚。
- 写入前校验原文定位和修订安全性，拒绝可能破坏格式的跨运行替换。
- 中国大陆默认法律基线，并要求在交付日重新核验官方现行文本。

## 安装

```bash
npx skills add review-doc -g -y
python3 -m pip install "python-docx>=1.0" "lxml>=4.9"
```

## 使用

```text
$lov-review-doc 审阅这份合同，站在乙方立场，给出批注、红线修订和谈判底线。
```

默认交付：

1. 带批注和修订痕迹的 DOCX。
2. 合同审阅报告 Markdown。
3. 可复核的结构化审阅 JSON。

## 新版 DOCX 命令

```bash
python3 scripts/contract_docx.py extract \
  --input contract.docx \
  --output contract-blocks.json

python3 scripts/contract_docx.py validate \
  --input contract.docx \
  --annotations review.json

python3 scripts/contract_docx.py annotate \
  --input contract.docx \
  --annotations review.json \
  --output contract-reviewed.docx
```

完整 JSON 字段见 [`references/annotation-schema.md`](references/annotation-schema.md)。

## 0.x 兼容入口

原有段落编号命令仍可使用，并会自动转换为 1.0 稳定锚点：

```bash
python3 scripts/annotate_docx.py extract --input contract.docx
python3 scripts/annotate_docx.py annotate \
  --input contract.docx \
  --annotations legacy-review.json \
  --output contract-reviewed.docx
```

## 重要边界

本 Skill 提供实质合同审阅，但不冒充律师事务所正式法律意见。涉及高额交易、控制权、担保、破产、刑事、制裁、跨境数据或迫近诉讼时，应由对应法域执业律师复核。

## License

MIT
