---
name: nationality-minhlongs
title: '`mekong nationality` (alias `mekong citizenship`) — Vietnamese Nationality, Naturalization, Renunciation & Dual Citizens'
description: Vietnamese Nationality, Naturalization, Renunciation & Dual Citizenship Suite.
author: minhlongs
author_url: https://github.com/minhlongs/mekong-cli/tree/main/.agents/skills/nationality
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: vn
practice: immigration
language: en
---

# `mekong nationality` (alias `mekong citizenship`) — Vietnamese Nationality, Naturalization, Renunciation & Dual Citizenship Suite

Governed by:
- **Law on Vietnamese Nationality 2008 (Luật Quốc tịch Việt Nam - Law No. 24/2008/QH12)**: Regulates principles of Vietnamese nationality (single nationality principle with exceptions under Article 4), relations between the State and citizens, acquisition of nationality (naturalization under Article 19), loss of nationality (renunciation under Article 27, deprivation under Article 31), restoration of nationality (Article 23), and state management of nationality.
- **Law Amending and Supplementing Law on Vietnamese Nationality 2014 (Law No. 56/2014/QH13)**: Extended registration provisions and dual nationality protections for overseas Vietnamese (Người Việt Nam định cư ở nước ngoài).
- **Decree No. 16/2020/ND-CP**: Detailing statutory conditions, procedures, dossiers, and issuance of Certificate of Vietnamese Nationality (Giấy xác nhận có quốc tịch Việt Nam) and Certificate of Being of Vietnamese Origin (Giấy xác nhận là người gốc Việt Nam).
- **Circular No. 02/2020/TT-BTP**: Ministry of Justice instructions on nationality registers and forms.

---

## 1. Capabilities & Core Subcommands

| Subcommand | Description | Key Parameters |
|---|---|---|
| `mekong nationality` | Executive dashboard overview of naturalizations, renunciations, restorations & nationality certificates | `--json` |
| `mekong nationality naturalize` | Process and evaluate Naturalization in Vietnam under Article 19 | `--applicant`, `--chosen-name`, `--birth-date`, `--nationality`, `--residence-years`, `--proficiency`, `--livelihood`, `--exemption`, `--dual-permit`, `--decision-no`, `--status`, `--json` |
| `mekong nationality renounce` | Process and evaluate Renunciation of Vietnamese Nationality under Article 27 (statutory bars: tax debt, prosecution, court judgment, national security) | `--applicant`, `--birth-date`, `--target-country`, `--tax-cleared`, `--criminal-pending`, `--judgment-pending`, `--security-cleared`, `--decision-no`, `--status`, `--json` |
| `mekong nationality restore` | Process Restoration of Vietnamese Nationality under Article 23 | `--applicant`, `--birth-date`, `--former-status`, `--ground`, `--nationality`, `--decision-no`, `--status`, `--json` |
| `mekong nationality certificate` | Issue or record Certificate of Vietnamese Nationality under Decree 16/2020/ND-CP | `--applicant`, `--id-type`, `--id-number`, `--residence`, `--authority`, `--cert-no`, `--issue-date`, `--status`, `--json` |
| `mekong nationality list` | Query nationality records by category (`naturalization`, `renunciation`, `restoration`, `certificate`, `audit`) | `--category`, `--limit`, `--offset`, `--json` |
| `mekong nationality status` | Display nationality affairs telemetry and system status | `--json` |

---

## 2. Statutory Rules & Safeguards Enforced

1. **Vietnamese Naming Mandate (Điều 19 Khoản 3 Luật Quốc tịch)**:
   - Naturalized citizens must have a Vietnamese chosen name.
2. **5-Year Residence & Integration Baseline (Điều 19 Khoản 1)**:
   - Standard naturalization requires $\ge$ 5 years permanent residence in Vietnam, adequate Vietnamese proficiency, and assured livelihood.
3. **Statutory Naturalization Exemptions (Điều 19 Khoản 2)**:
   - Exemption from 5-year residence, language, and livelihood for:
     * Spouse, parent, or natural child of a Vietnamese citizen (`SPOUSE_PARENT_CHILD`).
     * Person with special merits contributed to the building and defending of Vietnam (`SPECIAL_MERIT`).
     * Person whose naturalization is beneficial to the State of Vietnam (`BENEFICIAL_TO_STATE`).
4. **Renunciation of Foreign Citizenship vs Dual Nationality (Điều 19 Khoản 3)**:
   - Foreign citizenship must be renounced upon naturalization unless granted a **Special Presidential Permit** (`SPECIAL_PRESIDENTIAL_PERMIT`) by the State President.
5. **Mandatory Bars to Renouncing Vietnamese Nationality (Điều 27 Khoản 2 & 3)**:
   - Renunciation is prohibited if the person:
     * Owes taxes or property liabilities to the State, organizations, or citizens in Vietnam.
     * Is undergoing criminal prosecution or executing a court judgment.
     * Poses prejudice to national security.

---

## 3. Dual MCP Tools Parity

The suite exposes 6 canonical MCP tools with dual-engine parity across FastMCP and JSON-RPC 2.0 stdio:

- `mekong_nationality_naturalize`: Process or update naturalization dossier.
- `mekong_nationality_renounce`: Process or update renunciation dossier with statutory bar checks.
- `mekong_nationality_restore`: Process or update restoration of Vietnamese nationality.
- `mekong_nationality_certificate`: Issue or record Certificate of Vietnamese Nationality.
- `mekong_nationality_list`: Query nationality affairs records across categories.
- `mekong_nationality_status`: Aggregate Vietnamese nationality affairs telemetry.
