---
name: judicialassist-minhlongs
title: '`mekong judicialassist` (alias `mekong extradition`) — Vietnamese Mutual Legal Assistance, Extradition & Cross-Border Ju'
description: Vietnamese Mutual Legal Assistance, Extradition & Cross-Border Judicial Cooperation Suite.
author: minhlongs
author_url: https://github.com/minhlongs/mekong-cli/tree/main/.agents/skills/judicialassist
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: vn
practice: criminal
language: en
---

# `mekong judicialassist` (alias `mekong extradition`) — Vietnamese Mutual Legal Assistance, Extradition & Cross-Border Judicial Cooperation Suite

Governed by:
- **Law on Mutual Legal Assistance 2007 (Luật Tương trợ tư pháp - Law No. 08/2007/QH12)**: Regulates the principles, authority, conditions, and procedures for mutual legal assistance in civil matters (Chương II), mutual legal assistance in criminal matters (Chương III), extradition of offenders (Chương IV), and transfer of persons serving prison sentences (Chương V).
- **Criminal Procedure Code 2015 (Luật Tố tụng hình sự 2015 - Law No. 101/2015/QH13, Arts 491-508)**: Part Eight governing international judicial cooperation, criminal letters of request, extradition requests, and transfer of criminal proceedings.
- **Civil Procedure Code 2015 (Luật Tố tụng dân sự 2015 - Law No. 92/2015/QH13, Arts 474-481)**: Part Eight governing civil judicial letters of request, service of documents abroad, recognition and enforcement of foreign court judgments and arbitral awards.
- **Joint Circular No. 02/2016/TTLT-BCA-BQP-BTP-NHNNVN-VKSNDTC-TANDTC**: Joint circular guiding mutual legal assistance in criminal matters.
- **Joint Circular No. 12/2016/TTLT-BTP-BNG-TANDTC**: Joint circular guiding mutual legal assistance in civil matters.
- **United Nations Conventions**: UN Convention against Transnational Organized Crime (UNTOC), UN Convention against Corruption (UNCAC), and bilateral treaties on extradition and mutual legal assistance.

---

## 1. Capabilities & Core Subcommands

| Subcommand | Description | Key Parameters |
|---|---|---|
| `mekong judicialassist` | Executive dashboard overview of Civil MLA, Criminal MLA, Extradition, Sentence Transfer & Bilateral Treaties | `--json` |
| `mekong judicialassist civil` | Submit and record a Civil Mutual Legal Assistance Request under Articles 10-16 (focal point: Ministry of Justice / BTP) | `--case-code`, `--direction`, `--type`, `--requesting-body`, `--foreign-country`, `--target`, `--address`, `--basis`, `--costs-usd`, `--status`, `--json` |
| `mekong judicialassist criminal` | Submit and record a Criminal Mutual Legal Assistance Request under Articles 17-31 (focal point: Supreme People's Procuracy / VKSNDTC) | `--case-code`, `--direction`, `--type`, `--agency`, `--foreign-country`, `--offense`, `--dual-criminality`, `--basis`, `--asset-vnd`, `--status`, `--json` |
| `mekong judicialassist extradition` | Evaluate and record an Extradition Dossier according to statutory standards and refusal grounds under Articles 32-48 (focal point: Ministry of Public Security / BCA) | `--subject`, `--nationality`, `--direction`, `--country`, `--ground`, `--offense`, `--penalty-months`, `--remaining-months`, `--dual-criminality`, `--vietnamese-citizen`, `--expired-limitations`, `--torture-risk`, `--status`, `--json` |
| `mekong judicialassist transfer` | Process and record the Transfer of a Sentenced Person under Articles 49-64 (focal point: Ministry of Public Security / BCA) | `--prisoner`, `--nationality`, `--direction`, `--from-country`, `--to-country`, `--original-months`, `--served-months`, `--remaining-months`, `--consent`, `--dual-criminality`, `--compensation-cleared`, `--court-decision`, `--status`, `--json` |
| `mekong judicialassist treaty` | Register and track Bilateral Mutual Legal Assistance & Extradition Treaties | `--country`, `--title`, `--signing-date`, `--effective-date`, `--domain`, `--active`, `--json` |
| `mekong judicialassist list` | Query cross-border judicial assistance records by category (`civil`, `criminal`, `extradition`, `transfer`, `treaty`, `audit`) | `--category`, `--limit`, `--offset`, `--json` |
| `mekong judicialassist status` | Display cross-border judicial assistance telemetry and system status | `--json` |

---

## 2. Statutory Rules & Safeguards Enforced

1. **Vietnamese Citizen Non-Extradition Principle (Điều 35 Khoản 1 Điểm a Luật TTTP)**:
   - Vietnam **mandatorily refuses** to extradite Vietnamese citizens to foreign states. Vietnamese citizens who commit crimes abroad shall be prosecuted under Vietnamese criminal jurisdiction.
2. **Dual Criminality Principle (Nguyên tắc tội phạm kép - Điều 20 & 33 Luật TTTP)**:
   - Coercive criminal measures (search, seizure, freeze, confiscation) and extradition require the alleged act to constitute an offense under both Vietnamese criminal law and the foreign law.
3. **Statutory Penalties for Extradition (Điều 33 Luật TTTP)**:
   - For criminal prosecution: offense punishable by imprisonment of **at least 12 months** under both laws.
   - For sentence execution: remaining imprisonment of **at least 6 months**.
4. **Sentence Transfer Conditions (Điều 50-51 Luật TTTP)**:
   - Remaining imprisonment term must be **at least 12 months** (1 year).
   - Voluntary written consent of the sentenced person is mandatory.
   - Full clearance and satisfaction of all civil compensation and damages liabilities in the transferring state.
5. **Death Penalty Assurance (Điều 35 Khoản 2 Điểm a Luật TTTP)**:
   - Discretionary refusal if the requesting state provides no formal written assurance that the death penalty will not be imposed or executed.

---

## 3. Dual MCP Tools Parity

The suite exposes 7 canonical MCP tools with dual-engine parity across FastMCP and JSON-RPC 2.0 stdio:

- `mekong_judicialassist_civil`: Submit or update Civil Mutual Legal Assistance request.
- `mekong_judicialassist_criminal`: Submit or update Criminal Mutual Legal Assistance request.
- `mekong_judicialassist_extradition`: Evaluate and record Extradition Dossier with statutory refusal analysis.
- `mekong_judicialassist_transfer`: Process and record Transfer of Sentenced Persons.
- `mekong_judicialassist_treaty`: Register or update Bilateral Mutual Legal Assistance treaty.
- `mekong_judicialassist_list`: Query cross-border records across all categories.
- `mekong_judicialassist_status`: Aggregate cross-border judicial assistance telemetry and authority status.
