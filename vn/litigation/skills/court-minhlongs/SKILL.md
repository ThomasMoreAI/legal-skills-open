---
name: court-minhlongs
title: '`mekong court` — Vietnamese People''s Courts, Judicial Adjudication & Electronic Court Suite'
description: Vietnamese People's Courts, Judicial Adjudication & Electronic Court Suite.
author: minhlongs
author_url: https://github.com/minhlongs/mekong-cli/tree/main/.agents/skills/court
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: vn
practice: litigation
language: en
---

# `mekong court` — Vietnamese People's Courts, Judicial Adjudication & Electronic Court Suite

Governed by:
- **Law on Organization of People's Courts 2024 (Law No. 34/2024/QH15 — Luật Tổ chức Tòa án nhân dân 2024)**: Defines constitutional role, court system hierarchy, specialized courts, judicial ranks (Justices, Judges, People's Assessors, Clerks, Examiners), adjudication principles, and Chapter IX Electronic Courts (`Tòa án điện tử`).
- **Civil Procedure Code 2015 (Law No. 92/2015/QH13 — Bộ luật Tố tụng Dân sự 2015)**: Governs civil, commercial, labor, and family dispute resolution, first-instance trial, appellate review, and cassation/reopening.
- **Criminal Procedure Code 2015 (Law No. 101/2015/QH13 — Bộ luật Tố tụng Hình sự 2015)**: Governs criminal trial adjudication, trial panels, judgment pronouncements, and judicial appeals.
- **Law on Administrative Procedures 2015 (Law No. 93/2015/QH13 — Luật Tố tụng Hành chính 2015)**: Governs administrative lawsuits against state administrative acts and decisions.
- **Resolution No. 33/2021/QH15 on Online Court Hearings**: Legal basis for virtual, hybrid, and remote court hearings.
- **Circular No. 01/2017/TT-CA**: Standard for disclosing judicial judgments and rulings on the Supreme People's Court Electronic Portal.

---

## 1. Capabilities & Core Subcommands

| Subcommand | Description | Key Parameters |
|---|---|---|
| `mekong court` | Executive dashboard overview of Judicial Officers, Cases, Hearings, Judgments & Electronic Filings | `--json` |
| `mekong court officer` | Register/update a Judge, People's Assessor, Clerk, or Examiner under Law 34/2024/QH15 | `--code`, `--name`, `--role`, `--level`, `--court`, `--decision`, `--date`, `--term`, `--status`, `--json` |
| `mekong court case` | Docket and file a legal case under relevant procedure codes | `--number`, `--title`, `--type`, `--level`, `--court`, `--plaintiff`, `--defendant`, `--filing-date`, `--acceptance-date`, `--judge`, `--stage`, `--claim`, `--e-dossier/--paper-dossier`, `--json` |
| `mekong court hearing` | Schedule a trial hearing or online court session under Resolution 33/2021/QH15 | `--code`, `--case`, `--date`, `--type`, `--format`, `--member`, `--courtroom`, `--status`, `--notes`, `--json` |
| `mekong court judgment` | Issue formal court judgment/ruling, track appeal window & portal disclosure | `--number`, `--case`, `--type`, `--verdict`, `--remedy`, `--issue-date`, `--effective-date`, `--fee`, `--appeal-days`, `--public/--confidential`, `--json` |
| `mekong court filing` | Submit electronic filing, online claim, or e-evidence under Chapter IX Law 34/2024 | `--code`, `--name`, `--id-card`, `--title`, `--type`, `--case`, `--date`, `--payload`, `--status`, `--json` |
| `mekong court list` | List records across officers, cases, hearings, judgments, and electronic filings | `category <officers\|cases\|hearings\|judgments\|filings>`, `--limit <int>`, `--json` |
| `mekong court status` | Display court operations and digital transformation telemetry | `--json` |

---

## 2. MCP Tools Reference

The suite exposes 7 canonical MCP tools with dual-engine parity across FastMCP and JSON-RPC 2.0 stdio:

- `mekong_court_officer`: Register or update judicial officer (Judge, Assessor, Clerk, Examiner) under Law 34/2024/QH15.
- `mekong_court_case`: Docket and manage legal case under Civil, Criminal, or Administrative Procedure Code.
- `mekong_court_hearing`: Schedule physical, virtual (online), or hybrid court hearing under Resolution 33/2021/QH15.
- `mekong_court_judgment`: Issue formal court judgment or ruling and track statutory appeal deadlines.
- `mekong_court_filing`: Submit electronic filing or e-evidence with SHA-256 digital fingerprinting.
- `mekong_court_list`: Query court records across categories.
- `mekong_court_status`: Aggregate judicial operations and digital transformation telemetry.
