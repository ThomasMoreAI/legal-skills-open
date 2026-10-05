---
name: legalaid-minhlongs
title: '`mekong legalaid` — Vietnamese State Legal Aid, Vulnerable Population Representation & Justice Access Suite'
description: Vietnamese State Legal Aid, Vulnerable Population Representation & Justice Access Suite.
author: minhlongs
author_url: https://github.com/minhlongs/mekong-cli/tree/main/.agents/skills/legalaid
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: vn
practice: administrative
language: en
---

# `mekong legalaid` — Vietnamese State Legal Aid, Vulnerable Population Representation & Justice Access Suite

Governed by:
- **Law on Legal Aid 2017 (Luật Trợ giúp pháp lý - Law No. 11/2017/QH14)**: Defines eligibility criteria for beneficiaries (Điều 7: Người có công, hộ nghèo, trẻ em, người khuyết tật, đồng bào dân tộc thiểu số, người bị buộc tội từ 16 đến dưới 18 tuổi, nạn nhân bạo lực gia đình), legal aid organizations, officers, rights, duties, and operational procedures.
- **Decree No. 144/2017/NĐ-CP**: Detailed regulations implementing the Law on Legal Aid, financial remuneration, and collaborating lawyer contracts.
- **Circular No. 08/2017/TT-BTP**: Quality standards, criteria, and case file evaluation protocol for legal aid cases (Đánh giá chất lượng vụ việc trợ giúp pháp lý: Xuất sắc, Tốt, Đạt, Không đạt).
- **Criminal Procedure Code 2015 & Civil Procedure Code 2015**: Procedural defense counsel and lawful representation for vulnerable and indigent litigants.

---

## 1. Capabilities & Core Subcommands

| Subcommand | Description | Key Parameters |
|---|---|---|
| `mekong legalaid` | Executive dashboard overview of Beneficiaries, Officers, Requests, Proceedings & Quality Evals | `--json` |
| `mekong legalaid beneficiary` | Register or update eligible legal aid beneficiary under Article 7 Law on Legal Aid | `--code`, `--name`, `--citizen-id`, `--category`, `--province`, `--proof`, `--status`, `--json` |
| `mekong legalaid officer` | Register or update State Legal Aid Officer (TGV) or contracted lawyer | `--code`, `--name`, `--type`, `--card`, `--org`, `--dept`, `--status`, `--json` |
| `mekong legalaid request` | File or update legal aid application or case docket under Articles 29-33 | `--code`, `--beneficiary`, `--form`, `--field`, `--title`, `--date`, `--officer`, `--status`, `--json` |
| `mekong legalaid proceeding` | Issue appointment decision for officer to participate in court proceedings under Article 31 | `--code`, `--request`, `--case`, `--agency`, `--role`, `--date`, `--status`, `--notes`, `--json` |
| `mekong legalaid eval` | Evaluate legal aid case quality under Circular 08/2017/TT-BTP (0-100 score & rating) | `--code`, `--request`, `--evaluator`, `--score`, `--rating`, `--date`, `--notes`, `--json` |
| `mekong legalaid list` | List records across beneficiaries, officers, requests, proceedings, and evaluations | `category <beneficiaries\|officers\|requests\|proceedings\|evaluations>`, `--limit <int>`, `--json` |
| `mekong legalaid status` | Display State Legal Aid operational telemetry and justice access metrics | `--json` |

---

## 2. MCP Tools Reference

The suite exposes 7 canonical MCP tools with dual-engine parity across FastMCP and JSON-RPC 2.0 stdio:

- `mekong_legalaid_beneficiary`: Register or verify eligible legal aid beneficiary under Article 7.
- `mekong_legalaid_officer`: Register or update State Legal Aid Officer or collaborating lawyer.
- `mekong_legalaid_request`: File or update legal aid case docket (litigation, counseling, out-of-court representation).
- `mekong_legalaid_proceeding`: Issue appointment decision for court or investigation proceeding defense.
- `mekong_legalaid_eval`: Evaluate case quality and file standards under Circular 08/2017/TT-BTP.
- `mekong_legalaid_list`: Query legal aid records across categories.
- `mekong_legalaid_status`: Aggregate national legal aid operations and vulnerable protection telemetry.
