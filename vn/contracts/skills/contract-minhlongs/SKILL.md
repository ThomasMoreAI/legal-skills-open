---
name: contract-minhlongs
title: /contract — Autonomous Commercial Contract, E-Sign & Legal Risk Assessment Engine
description: Commercial contracts, electronic signatures (E-Sign), statutory risk assessment, penalty limits, and legal redlines under Vietnamese law.
author: minhlongs
author_url: https://github.com/minhlongs/mekong-cli/tree/main/.agents/skills/contract
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: vn
practice: contracts
language: en
---

# /contract — Autonomous Commercial Contract, E-Sign & Legal Risk Assessment Engine

Autonomous Vietnamese Commercial Contract Management, E-Signatures, and Legal Risk Auditing conforming to:
- **Bộ luật Dân sự 2015 (Luật số 91/2015/QH13)**: Hợp đồng dân sự, điều kiện có hiệu lực, bồi thường thiệt hại.
- **Luật Thương mại 2005 (Luật số 36/2005/QH11)**:
  - **Điều 301**: Giới hạn trần mức phạt vi phạm hợp đồng tối đa 8% giá trị phần nghĩa vụ bị vi phạm.
  - **Điều 302**: Bồi thường thiệt hại thực tế, trực tiếp.
  - **Điều 294**: Miễn trách nhiệm trong sự kiện bất khả kháng (Force Majeure).
- **Luật Giao dịch điện tử 2023 (Luật số 20/2023/QH15) & Nghị định 130/2018/NĐ-CP**:
  - Giá trị pháp lý của văn bản và chữ ký điện tử an toàn.
  - Mã băm chữ ký số điện tử SHA-256 kết hợp dấu thời gian tin cậy (Timestamp Authority - TSA).
- **Nghị định 13/2023/NĐ-CP**: Cam kết bảo vệ dữ liệu cá nhân (PDPD) trong các thỏa thuận thương mại công nghệ.

## Architecture

```
mekong contract
     │
     ├── (overview)         ── Commercial contract dashboard, risk breakdown, and active e-signatures
     ├── draft              ── Synthesize standard commercial contract (SOFTWARE_DEV, COMMERCIAL_SALE, NDA, DISTRIBUTION)
     ├── risk-check         ── Scan clauses for statutory conflicts, penalty breach (>8%), and missing safeguards
     ├── sign               ── Execute cryptographic electronic signature (SHA-256 + TSA)
     ├── verify             ── Verify integrity and authenticity of electronic signatures
     ├── list               ── Query historical commercial contracts and execution status
     └── status             ── Contract engine regulatory telemetry in .mekong/contracts.db
```

## CLI Usage

```bash
// turbo
mekong contract [OPTIONS]
```

### Subcommands

| Command | Arguments / Flags | Description |
|---------|-------------------|-------------|
| `mekong contract` | `[--json]` | Overview contracts dashboard, risk metrics, and e-signatures |
| `mekong contract draft` | `<template> <party_a> <party_b> [--value N] [--scope S] [--penalty P] [--json]` | Draft statutory commercial contract |
| `mekong contract risk-check` | `<text> [--penalty P] [--json]` | Scan contract text for illegal penalties, missing force majeure |
| `mekong contract sign` | `<contract_id> <name> [--title T] [--tax TAX] [--org ORG] [--json]` | Sign contract electronically with TSA SHA-256 |
| `mekong contract verify` | `<signature_id> [--json]` | Verify e-signature integrity and legal validity |
| `mekong contract list` | `[--status S] [--limit N] [--json]` | Query registered commercial contracts |
| `mekong contract status` | `[--json]` | Contract engine status and database telemetry |

## MCP Tools Integration

- `mekong_contract_draft(template_type, party_a_name, party_b_name, contract_value_vnd=0.0, party_a_tax_id="0100000001", party_b_tax_id="0300000002", scope_summary="", penalty_rate_pct=8.0, dispute_forum="VIAC")`: Synthesize standard commercial contract.
- `mekong_contract_risk_check(contract_text, penalty_pct=None)`: Scan contract clauses for legal risks and redlines.
- `mekong_contract_sign(contract_id, signer_name, signer_title="Giám đốc điều hành", signer_tax_id="0100000001", organization_name="")`: Sign contract electronically.
- `mekong_contract_verify(signature_id)`: Verify cryptographic electronic signature validity.
- `mekong_contract_status()`: Retrieve contract engine telemetry and metrics.
