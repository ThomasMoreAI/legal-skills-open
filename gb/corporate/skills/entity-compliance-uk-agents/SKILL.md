---
name: entity-compliance-uk-agents
title: /entity-compliance
description: Entity compliance tracker — initialise, report upcoming deadlines, update status, run health audit, export to CSV. Maintains a compliance-tracker.yaml built from the entity table, calculates Companies House filing deadlines by entity and nation (England & Wales / Scotland / Northern Ireland), and surfaces what's due in the next 30/60/90 days. Covers Confirmation Statements (CS01), annual accounts, PSC register updates, and charge registration (21-day window). Use when user says "entity compliance", "Companies House deadlines", "Confirmation Statement due", "accounts filing", "entity tracker", "what filings are due", "entity health", or "good standing".
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/corporate-legal-uk/skills/entity-compliance
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: corporate
language: en
---

# /entity-compliance

1. Load `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md` → `## Entity Management` (entity table, jurisdictions, company secretary / registered office).
2. Route to the correct mode below based on flag:
   - No flag or `--init`: Mode 1 — initialise tracker from entity table
   - `--report`: Mode 2 — surface upcoming deadlines and overdue items
   - `--update`: Mode 3a (manual) or 3b (--from-report upload) — update status
   - `--sweep`: Mode 3c — walk through unknown/overdue items one by one
   - `--audit`: Mode 4 — full health audit
   - `--export`: Mode 5 — produce CSV or table export
3. Read/write `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/entities/compliance-tracker.yaml`.
4. After any update: show summary of changes and next action.

---

## Purpose

Confirmation Statements, accounts filings, PSC register updates, charge registrations — every UK entity has its own schedule and its own consequences for missing the deadline (fines, strike-off, unenforceable charges). This skill maintains a single YAML tracker that knows what's due, when, and for which entity. It's lightweight by design: the tracker is a file you own, Claude updates it on command, and you export it when you need to share it.

## Important: deadline reference caveat

> The filing deadlines in this skill's reference table reflect UK Companies Act 2006 requirements and Companies House guidance as understood at the skill's build date. Filing requirements, due dates, and fee structures can change. **Always confirm deadlines directly with Companies House (companieshouse.gov.uk) or your company secretarial service before relying on them for compliance purposes.** If you use a professional company secretarial service, their compliance calendar is authoritative for your specific entities — use this tracker to organise and surface their data, not to replace it.

## Jurisdiction assumption

> This tracker computes deadlines against the nation of incorporation and qualification recorded per entity. Filing rules, due-date mechanics, and fee structures vary between England & Wales, Scotland, and Northern Ireland. For Scottish entities, some CA2006 provisions and registration requirements differ (charges over Scottish property require registration at the Register of Sasines / Land Register of Scotland in addition to Companies House). If an entity's actual footprint differs from what's in the config, the output may not apply as written — confirm with Companies House or a company secretarial specialist.

## Entity-type disambiguation (UK)

> The filing calendar depends on **entity type** and whether the company is **private or public**. Treating a "UK entity" as a single bucket is a common and consequential error. Key distinctions:
>
> - **Private company (Ltd):** Annual accounts due 9 months after financial year end. Confirmation Statement: due within 14 days after the review period end (anniversary of incorporation or last CS01). First accounts: if the period is more than 12 months, the filing deadline is different.
> - **Public company (plc):** Annual accounts due 6 months after financial year end. AGM required within 6 months of financial year end.
> - **Dormant company:** May file dormant accounts (CA2006 s.480) if eligible; check eligibility (small company criteria + dormant throughout the period).
> - **LLP:** Different filing regime under LLP Act 2000 and LLP (Accounts and Audit) Regulations.
> - **Single-member company:** Same CA2006 rules as other private companies; note that if sole member also sole director, succession planning is important.
>
> Never copy a deadline from one entity type to another. Confirm entity type from the entity table before computing or reporting a deadline.

---

## Tracker file

Lives at `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/entities/compliance-tracker.yaml`. Structure:

```yaml
# Entity Compliance Tracker (UK)
# Generated: [date]
# Last updated: [date]
# Disclaimer: deadlines are reference only — confirm with Companies House or company secretarial service

metadata:
  company: "[Company Name]"
  generated: "[date]"
  last_updated: "[date]"
  last_audit: "[date or null]"

custom_jurisdictions:   # manually added — non-UK jurisdictions not in built-in reference table
  []

entities:
  - name: "[Entity Name]"
    registered_number: "[XXXXXXXX]"
    type: "[Ltd / plc / LLP / LP / unlimited / other]"
    nation: "[England and Wales / Scotland / Northern Ireland]"
    formation_date: "[date or null]"
    financial_year_end: "[MM-DD or null]"
    status: "[active / dormant / dissolving]"
    company_secretary: "[name / outsourced to [firm] / none]"
    registered_office: "[address]"
    notes: ""

    jurisdictions:
      - nation: "[England and Wales / Scotland / Northern Ireland]"
        qualification: "[domestic / foreign / branch]"
        qualified_date: "[date or null]"
        agent_managed: false
        local_agent: "[name or null]"
        filings:
          - type: "[Confirmation Statement (CS01) / Annual Accounts / Dormant Accounts / Charge Registration / PSC Update / other]"
            due_date: "[YYYY-MM-DD]"
            due_basis: "[anniversary: YYYY-MM-DD / fixed: MM-DD / event-triggered / other]"
            last_filed: "[date or null]"
            last_fee: "[amount or null]"
            status: "[current / due_soon / overdue / unknown]"
            confirmed_good_standing: "[date or null]"
            notes: ""
```

Status values:
- `current` — filed for current period, nothing due within 90 days
- `due_soon` — due within 90 days
- `overdue` — past due date with no filed date recorded
- `unknown` — no information; needs manual confirmation

---

## Mode 1: Initialise

Run when no tracker exists, or with `--rebuild` to regenerate from scratch.

### Step 1: Load entity table

Read `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md` → `## Entity Management` → Entity table. If the entity table is populated (from org chart upload at cold-start), use it directly. If not, ask the user to either run the cold-start module or provide the entity list.

### Step 2: For each entity, confirm filing requirements

**UK Companies House — key filing types:**

**Confirmation Statement (CS01):**
- Every UK company must file at least one CS01 per 12-month review period.
- Due date: within 14 days after the review period end (which is the anniversary of incorporation or the anniversary of the last CS01 filing date, whichever is later).
- Fee: £13 (online) / £40 (paper) `[verify current fee]`.
- Failure to file: company may be struck off the register and dissolved.
- Content: confirms or updates company information (registered office, SIC codes, share capital, shareholders, PSC register information, officer details).

**Annual Accounts:**
- Private company (Ltd): due 9 months after financial year end.
- Public company (plc): due 6 months after financial year end.
- First accounts: if the accounting reference period is more than 12 months, the deadline is 21 months from incorporation date (for private companies). `[verify]`
- Dormant company accounts (CA2006 s.480): eligible if company has been dormant throughout the period AND is a small company. File Form AA02 (dormant company accounts).
- Failure to file: automatic civil penalties starting at £150 (private) / £750 (public) up to £1,500 / £7,500 for accounts more than 6 months late. `[verify current penalty levels]`

**PSC Register update:**
- Must be updated within 14 days of becoming aware of a registrable change.
- File Form PSC01–PSC09 at Companies House depending on the type of change.
- This is an ongoing obligation — not just an annual filing.

**Charge registration (CA2006 Part 25):**
- Must register a charge at Companies House within 21 days of creation.
- File Form MR01 (mortgage or charge created by a UK company).
- Failure to register: charge is void against liquidator/administrator and secured creditors — the debt remains due but the security is lost.
- **Scottish companies / Scottish property:** charges over Scottish property also require registration at the Register of Sasines or the Land Register of Scotland. Confirm with Scottish solicitors.

**For each entity × filing type, ask the user:**
1. Do you have a current CS01 / accounts filing confirmation from Companies House?
2. What is the last filed date for each filing type?
3. What is the financial year end?
4. Is the entity dormant (CA2006 s.1169 — no significant accounting transactions during the period)?

For anything the user does not know, flag the entity × filing type entry as `unknown`.

**Companies House verification via uk-due-diligence MCP:**
If the uk-due-diligence MCP is connected, query Companies House for the company's filing history to verify last filed dates and next due dates. Report ✓ if retrieved from Companies House directly; `[model knowledge — verify]` if calculated from user-provided data. Always prefer live Companies House data over estimates.

### Step 3: Write the tracker

Generate `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/entities/compliance-tracker.yaml` with all entities and their filing requirements. Set initial status:
- `current` if last_filed is within the current filing period
- `due_soon` if due within 90 days and no last_filed for current period
- `overdue` if due date has passed and no last_filed for current period
- `unknown` if formation_date is missing or due date cannot be calculated

Show a summary after generating:

```
Entity compliance tracker initialised.

Entities: [N]
Total filing obligations tracked: [N]

Status summary:
  ✅ Current:   [N]
  ⏰ Due soon:  [N] (next 90 days)
  🔴 Overdue:   [N]
  ❓ Unknown:   [N] (confirm with Companies House or company secretarial service)

Run /corporate-legal-uk:entity-compliance --report to see what's due.
```

---

## Mode 2: Report

Surfaces upcoming deadlines and flags overdue items. Default: next 90 days.

```
/corporate-legal-uk:entity-compliance --report [--days 30|60|90|180]
```

Output format:

```
ENTITY COMPLIANCE REPORT (UK COMPANIES HOUSE) — [date]
[Company Name]

🔴 OVERDUE ([N]):
  [Entity] / [Nation] / [Filing type] — was due [date]

⏰ DUE WITHIN [N] DAYS ([N]):
  [Entity] / [Nation] / [Filing type] — due [date]  [company secretary / self-filing]
  [Entity] / [Nation] / [Filing type] — due [date]

✅ RECENTLY FILED ([N] in last 90 days):
  [Entity] / [Nation] / [Filing type] — filed [date]

❓ UNKNOWN STATUS ([N]):
  [Entity] / [Nation] / [Filing type] — no information; verify with Companies House

🌐 AGENT-MANAGED ([N]):
  [Entity] / [Country] / [Filing type] — managed by [local agent]; confirm status directly

PSC REGISTER STATUS:
  Last reviewed: [date]
  Entities with PSC register confirmed up to date: [N] of [total]
  Entities where PSC review outstanding: [list]

CHARGES:
  Charges registered in last 30 days: [N]
  Charges due for registration within 21-day window: [N] [🔴 if any — time-sensitive]
```

If the tracker covers more than ~10 entities, or any time the user asks: offer the dashboard (see CLAUDE.md `## Outputs → Dashboard offer for data-heavy outputs`). Shape the offer for this output — counts by filing status, a sortable entity table with nation, filing type, and next due date.

---

## Mode 3: Update

Updates one or more entities in the tracker. Three sub-modes:

### Consequential-action gate (file at Companies House)

**Before directing or confirming a filing:** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md`. If the Role is **Non-lawyer**:

> Filing a Confirmation Statement, annual accounts, or PSC update at Companies House has legal consequences — it's a formal statement from the company, it carries fees, and missed or incorrect filings can cause penalties, loss of good standing, or strike-off. Have you reviewed this with a solicitor or company secretary before filing? If yes, proceed to record the filing. If no, here's a brief to bring to them:
>
> - Entity, filing type, and due date
> - What the tracker says about the last filing (date, officer/director information last reported)
> - Open questions (is the information still accurate; has the registered office changed; has the company secretary changed; are there any PSC register updates outstanding)
> - What could go wrong (out-of-date PSC information, missed deadline triggering penalties or strike-off, wrong information filed)
> - What to ask the solicitor/company secretary (is a filing actually needed now; are there any changes to be reflected; who should authorise)
>
> If you need to find a solicitor: contact the SRA at sra.org.uk.

Do not record a new `last_filed` date past this gate without an explicit yes. Tracker reads, deadline reports, and "what's due soon" output do not require the gate.

### 3a: Manual update

```
/corporate-legal-uk:entity-compliance --update
```

Attorney/company secretary tells Claude what was filed:
> "We filed the Confirmation Statement for [Entity] on [date]. Filed online."

Claude updates:
- `last_filed` → filed date
- `status` → `current`
- `last_updated` in metadata

### 3b: Companies House confirmation upload

```
/corporate-legal-uk:entity-compliance --update --from-report
```

User uploads a Companies House confirmation email, a company secretarial service compliance report (PDF, CSV, or Excel), or a bulk export from Companies House WebFiling. Claude reads it and updates matching entities.

After processing:
```
Updated [N] entities from report.

Matched: [N]
Unmatched (in report, not in tracker): [list — may need to add to entity table]
Not in report (in tracker, no update): [list — status unchanged]
```

### 3c: Bulk status sweep

```
/corporate-legal-uk:entity-compliance --sweep
```

Walks through each entity with `unknown` or `overdue` status and asks for current information one at a time.

---

## Mode 4: Health audit

```
/corporate-legal-uk:entity-compliance --audit
```

Broader review beyond just filing status. Surfaces:

**Filing compliance:**
- Overdue items (from report mode)
- Unknown status items

**Entity health:**
- Entities marked as `dormant` — flag for review: should these be dissolved? Carrying dormant entities costs money (annual fees, company secretarial fees) and creates ongoing Companies House obligations.
- Entities with formation_date older than 5 years and status `dormant` — flag as dissolution candidates. Voluntary striking off (CA2006 s.1003) or Members' Voluntary Liquidation if solvent and assets to distribute.
- Entities missing formation_date or Companies House registration number — flag as data gap.

**Good standing gaps:**
- Entities with no confirmed filing up to date — unknown whether in good standing with Companies House.
- Entities where accounts or CS01 filings are more than 6 months outstanding — risk of automatic penalties or compulsory strike-off.

**PSC register gaps:**
- Entities where PSC register has not been reviewed in the last 12 months — flag for review. PSC register is a live obligation; changes must be reported within 14 days.
- Any PSC holding >50% shares or voting rights — confirm whether any notification obligations to Companies House or HMRC are triggered by recent changes.

**Charge registration gaps:**
- Any charges created in the last 30 days — confirm registered within 21-day window.
- Any charges on the register where the debt has been discharged — confirm MR04 (satisfaction/release) filed.

**Scottish company charges:**
- For Scottish entities: confirm whether any property charges have been registered at both Companies House AND the Scottish Registers (Register of Sasines / Land Register of Scotland).

**Intercompany agreement gaps:**
- From `~/.claude/plugins/config/uk-legal-plugins/corporate-legal-uk/CLAUDE.md`: if intercompany agreements are marked as partial or no, flag which entity relationships likely need agreements (parent-subsidiary services, IP licences, loans — note transfer pricing implications for HMRC).

Output format:

```
ENTITY HEALTH AUDIT (UK) — [date]

FILING COMPLIANCE
  Overdue: [N]
  Unknown status: [N]
  Action: run --sweep to confirm unknown items

DORMANT ENTITIES ([N])
  [List of dormant entities with age and annual carrying cost if known]
  Dissolution candidates (>5 years dormant): [list]
  Consider: voluntary striking off (CA2006 s.1003) or MVL

GOOD STANDING / COMPANIES HOUSE STATUS
  No confirmed filing: [N] entities
  Penalty risk (>6 months overdue): [N] entities
  Consider refreshing before: [any upcoming transactions or financings if known]

PSC REGISTER
  Not reviewed in last 12 months: [N] entities
  Action: review and file any changes within 14 days of becoming aware

CHARGES
  Pending 21-day registration window: [N]
  Discharged charges without MR04: [flag if any]
  Scottish entities — dual registration required: [flag if applicable]

POTENTIAL GAPS
  Intercompany agreements: [status from config]

RECOMMENDED ACTIONS
  1. [Highest priority action]
  2. [etc.]
```

---

## Mode 5: Export

```
/corporate-legal-uk:entity-compliance --export [--format csv|table]
```

Produces a flat export suitable for sharing with finance, legal ops, or the company secretarial service. Default: CSV.

CSV columns:
`Entity Name, Registered Number, Entity Type, Nation, Formation Date, Financial Year End, Status, Company Secretary, Filing Type, Due Date, Last Filed, Last Fee, Good Standing Confirmed, Notes`

One row per filing per entity. Multiple rows per entity (one per filing type).

If `--format table`: produce a markdown table suitable for pasting into a report or Slack message, showing only the next 90 days of filings.

---

## What this skill does not do

- It does not file anything at Companies House. Output is a tracker and a to-do list; filing is done by the solicitor, company secretary, or registered agent.
- It does not pull live Companies House data independently — it uses the uk-due-diligence MCP if connected, or relies on user-provided data.
- It does not determine whether foreign qualification is required in a given jurisdiction (UK nations). That analysis depends on facts about operational presence that the solicitor must confirm.
- It does not replace a company secretarial service for groups with complex multi-entity structures.
- The filing deadline reference table is not legal advice and may not reflect current requirements. Confirm all deadlines with Companies House before relying on them.


## Formula injection defense

Before writing any cell in Excel, Sheets, or CSV output, neutralize formula injection. Counterparty-sourced text (contract quotes, party names, Companies House data, company secretarial exports) is attacker-controlled. A cell starting with `=`, `+`, `-`, `@`, tab, or carriage return will be interpreted as a formula or break the row structure.

- **Prefix with a single quote:** `'=SUM(A1:A10)` → `=SUM(A1:A10)` (displayed as text, not executed)
- **Applies to every cell that contains text sourced from a document, a tool result, or a user paste.** Column headers you control and computed values you produce are safe.
- **CSV: also escape embedded commas, double quotes, newlines** (RFC 4180 quoting).
- This is not optional. A spreadsheet your user opens in Excel that triggers a macro or exfiltrates data via DDE is a supply-chain attack on your user.
