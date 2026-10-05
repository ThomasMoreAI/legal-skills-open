---
name: lawyer-minhlongs
title: '`mekong lawyer` — Vietnamese Legal Profession, Bar Association & Law Practice Suite'
description: Vietnamese Legal Profession, Bar Association & Law Practice Suite.
author: minhlongs
author_url: https://github.com/minhlongs/mekong-cli/tree/main/.agents/skills/lawyer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: vn
practice: general
language: en
---

# `mekong lawyer` — Vietnamese Legal Profession, Bar Association & Law Practice Suite

Governed by:
- **Law on Lawyers 2006 (Law No. 65/2006/QH11)** as amended by **Law No. 20/2012/QH13 (Luật Luật sư 2006/2012)**: Defines qualification, bar admission, rights and duties, forms of law practice, legal service contracts, and professional remuneration.
- **Decree No. 123/2013/NĐ-CP & Decree No. 137/2018/NĐ-CP**: Implementing regulations for law practice organizations, branches, and foreign law firms.
- **Code of Professional Ethics and Conduct of Vietnamese Lawyers (Bộ Quy tắc Đạo đức và Ứng xử nghề nghiệp luật sư Việt Nam - Decision No. 201/QĐ-HĐLSTQ)**: Governs conflict of interest rules, client confidentiality, pro bono legal aid duties, and professional standards.
- **Criminal Procedure Code 2015 (Law No. 101/2015/QH13)**: Articles 72-84 governing defense counsel registration (`Người bào chữa`), rights to visit detainees, and trial participation.
- **Civil Procedure Code 2015 & Law on Administrative Procedures 2015**: Articles governing litigation representatives and protection of lawful rights.

---

## 1. Capabilities & Core Subcommands

| Subcommand | Description | Key Parameters |
|---|---|---|
| `mekong lawyer` | Executive dashboard overview of Lawyers, Law Firms, Legal Contracts, Litigation Defense & Ethics | `--json` |
| `mekong lawyer attorney` | Register or update practicing lawyer admitted to the Bar under Law on Lawyers | `--card`, `--license`, `--name`, `--bar`, `--org`, `--form`, `--spec`, `--date`, `--status`, `--json` |
| `mekong lawyer firm` | Register or update Law Practice Organization licensed by Dept of Justice | `--reg-num`, `--name`, `--form`, `--partner`, `--dept`, `--address`, `--capital`, `--status`, `--json` |
| `mekong lawyer contract` | Execute mandatory statutory Legal Service Contract (Hợp đồng dịch vụ pháp lý) | `--contract-num`, `--client`, `--tax-id`, `--scope`, `--title`, `--lawyer`, `--fee`, `--date`, `--status`, `--json` |
| `mekong lawyer defense` | Record formal participation in court/investigation proceedings (Thông báo người bào chữa) | `--code`, `--case`, `--agency`, `--lawyer`, `--role`, `--date`, `--status`, `--notes`, `--json` |
| `mekong lawyer ethics` | Perform professional ethics, conflict of interest, and mandatory pro bono hours audit | `--code`, `--lawyer`, `--conflict/--no-conflict`, `--confidential/--no-confidential`, `--pro-bono`, `--verdict`, `--notes`, `--json` |
| `mekong lawyer list` | List records across lawyers, firms, contracts, litigation defense, and ethical audits | `category <lawyers\|firms\|contracts\|litigation\|ethics>`, `--limit <int>`, `--json` |
| `mekong lawyer status` | Display bar telemetry and legal practice operational status | `--json` |

---

## 2. MCP Tools Reference

The suite exposes 7 canonical MCP tools with dual-engine parity across FastMCP and JSON-RPC 2.0 stdio:

- `mekong_lawyer_attorney`: Register or update practicing lawyer card and bar association credentials.
- `mekong_lawyer_firm`: Register or update law firm / law office registration under Dept of Justice.
- `mekong_lawyer_contract`: Execute statutory legal service contract under Articles 54-56 Law on Lawyers.
- `mekong_lawyer_defense`: Record formal litigation defense / legal representation participation.
- `mekong_lawyer_ethics`: Perform professional ethics, conflict of interest, and pro bono legal aid audit.
- `mekong_lawyer_list`: Query legal profession records across categories.
- `mekong_lawyer_status`: Aggregate bar and law practice telemetry.
