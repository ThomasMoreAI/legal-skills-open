---
name: entity-compliance-bossmann007
title: 'Entity compliance'
description: Tracker de compliance societário — inicializa, reporta prazos próximos, atualiza status, roda auditoria de saúde, exporta CSV. Mantém um compliance-tracker.yaml construído a partir da tabela de entidades, calcula prazos de arquivamento por entidade e Junta Comercial estadual, e mostra o que vence nos próximos 30/60/90 dias. Use quando o usuário disser "compliance societário", "prazos de arquivamento", "alteração contratual pendente", "tracker de entidades", "quais arquivamentos vencem", "saúde societária", ou "situação cadastral".
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/corporate-legal/skills/entity-compliance
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: br
practice: corporate
language: pt
---

# /entity-compliance

1. Carregar `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` → `## Entity Management` (tabela de entidades, jurisdições/Junta Comercial, responsável pelo registro).
2. Rotear pro modo correto conforme a flag:
   - Sem flag ou `--init`: Modo 1 — inicializa tracker a partir da tabela de entidades
   - `--report`: Modo 2 — mostra prazos próximos e itens vencidos
   - `--update`: Modo 3a (manual) ou 3b (upload de --from-report) — atualiza status
   - `--sweep`: Modo 3c — percorre itens unknown/overdue um a um
   - `--audit`: Modo 4 — auditoria de saúde completa
   - `--export`: Modo 5 — exporta CSV ou tabela
3. Ler/escrever `~/.claude/plugins/config/claude-for-legal/corporate-legal/entities/compliance-tracker.yaml`.
4. Após qualquer atualização: mostrar resumo das mudanças e próxima ação.

---

## Propósito

Alteração contratual não arquivada, CNPJ irregular perante a Receita Federal,
Formulário de Referência atrasado na CVM — toda entidade tem sua própria
agenda e sua própria consequência por perder o prazo. Essa skill mantém um
tracker YAML único que sabe o que vence, quando, e pra qual entidade. É leve
por design: o tracker é um arquivo seu, Claude atualiza sob comando, e você
exporta quando precisa compartilhar.

## Importante: ressalva sobre a referência de prazos

> Os prazos de arquivamento na tabela de referência dessa skill refletem exigências publicamente disponíveis na data de construção da skill. Exigências de arquivamento e datas de vencimento mudam — a Junta Comercial de cada estado tem seu próprio regimento interno, e a Receita Federal atualiza periodicamente prazos de obrigações acessórias (ECD, ECF, DCTFWeb). **Sempre confirme prazos com seu contador ou advogado responsável, ou diretamente com a Junta Comercial/Receita Federal, antes de confiar neles para fins de compliance.** Se sua empresa usa um escritório de contabilidade ou despachante que acompanha prazos societários, o calendário deles é autoritativo para suas entidades específicas — use esse tracker para organizar e mostrar os dados deles, não para substituí-los.

## Premissa de jurisdição

> Esse tracker calcula prazos contra o estado de registro (Junta Comercial) ou país de constituição/qualificação registrado por entidade. Regras de arquivamento, mecânica de vencimento e estrutura de taxas variam materialmente por jurisdição. Se a presença real de uma entidade difere do que está em `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` (filial não registrada, entidade dissolvida, mudança de sede/domicílio, arquivamentos internacionais geridos por agente local), a saída pode não se aplicar como escrito — confirme com o contador/advogado responsável ou consultor local daquela jurisdição.

## Desambiguação por tipo societário (Ltda. vs. S.A.)

> O calendário de arquivamento depende do **tipo societário**, não só da Junta Comercial. Tratar "entidade brasileira" como um balde único é um erro comum e consequente — Ltda., S.A. fechada e S.A. de capital aberto têm arquivamentos diferentes, prazos diferentes, e consequências diferentes por perder o prazo. Confirme o tipo societário na tabela de entidades antes de calcular ou reportar um prazo, e nunca copie um prazo de um tipo societário pra outro na mesma Junta Comercial.
>
> **Brasil — a divisão que importa:**
>
> - **Sociedade Limitada (Ltda.):** Toda alteração contratual (mudança de sócio, capital social, objeto social, endereço) deve ser arquivada na Junta Comercial do estado em até **30 dias** da assinatura para retroagir os efeitos à data do ato — passado esse prazo, os efeitos só valem da data do arquivamento em diante (Art. 36, Lei 8.934/1994; Art. 1.151, §§1º-3º, Código Civil). Não há "annual report" nem "franchise tax" — a obrigação recorrente é fiscal (CNPJ ativo perante Receita Federal, obrigações acessórias conforme regime tributário: Simples Nacional, Lucro Presumido ou Lucro Real).
> - **Sociedade Anônima fechada (S.A. capital fechado):** Assembleia Geral Ordinária (AGO) obrigatória em até **4 meses após o encerramento do exercício social** para aprovar contas, eleger administradores e destinar resultado (Art. 132, Lei 6.404/1976). Ata da AGO deve ser arquivada na Junta Comercial. Sem obrigações de CVM. [verified: https://www.planalto.gov.br/ccivil_03/leis/l6404consol.htm]
> - **Sociedade Anônima de capital aberto (S.A. aberta — CVM):** Além da AGO (Art. 132), obrigações recorrentes perante a CVM: Formulário de Referência (atualização anual, Instrução CVM 480/2009), Demonstrações Financeiras Padronizadas (DFP) anuais e Informações Trimestrais (ITR), ambas via sistema CVM/B3. Prazo de entrega da DFP: até o dia seguinte à disponibilização das demonstrações financeiras aos acionistas, ou até o dia seguinte à publicação, o que ocorrer primeiro — nunca depois de 3 meses do encerramento do exercício.
>
> Uma Ltda. NÃO tem "annual report" no sentido americano — escrever esse prazo pra uma Ltda. carrega risco real (flags espúrias de "overdue" que mascaram a real exposição em arquivamento de alteração contratual, ou o inverso: tratar a regra de AGO de S.A. como universal e perder o prazo real de 30 dias de arquivamento de alteração da Ltda.). Se a tabela de entidades registra uma entidade brasileira sem tipo definido, marque como `type_unknown` e peça confirmação ao usuário antes de calcular qualquer prazo.
>
> A mesma disciplina de tipo societário se aplica a filiais de entidades brasileiras em outros países e a subsidiárias estrangeiras de holding brasileira — cada uma segue o regime de arquivamento do seu próprio país de constituição. Quando a tabela de referência de uma jurisdição estiver populada, garanta que está indexada por tipo societário, não só por estado/país.

---

## Tracker file

Lives at `~/.claude/plugins/config/claude-for-legal/corporate-legal/entities/compliance-tracker.yaml`. Structure:

```yaml
# Entity Compliance Tracker
# Generated: [date]
# Last updated: [date]
# Disclaimer: deadlines are reference only — confirm with contador/administrador responsável or Junta Comercial

metadata:
  company: "[Company Name]"
  generated: "[date]"
  last_updated: "[date]"
  last_audit: "[date or null]"

custom_jurisdictions:   # manually added — US states or countries not in built-in reference table
  []                    # populated when a new jurisdiction is encountered

entities:
  - name: "[Nome da Entidade]"
    type: "[Ltda. / S.A. fechada / S.A. aberta / outro]"
    state_of_formation: "[estado — Junta Comercial de registro]"
    cnpj: "[CNPJ ou null]"
    formation_date: "[data ou null]"
    status: "[ativa / dormant / em dissolução]"
    registered_agent: "[contador/administrador responsável / escritório / interno / outro]"
    notes: ""

    jurisdictions:
      - state: "[estado]"
        qualification: "[matriz / filial]"
        qualified_date: "[data ou null]"
        agent_managed: false   # true para entidades internacionais onde agente local cuida do compliance
        local_agent: "[nome ou null]"
        filings:
          - type: "[Alteração Contratual / AGO / DFP / ITR / Formulário de Referência / obrigação acessória / outro]"
            due_date: "[YYYY-MM-DD]"
            due_basis: "[fixed date / anniversary month / other]"
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

Read `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` → `## Entity Management` → Entity table. If the entity table
is populated (from org chart upload at cold-start), use it directly. If not,
ask the user to either run the cold-start module or provide the entity list.

### Step 2: For each entity × jurisdiction, confirm the filing requirements

For each entity, confirm the current filing schedule with the contador/administrador responsável or the relevant Junta Comercial. Filing schedules change (some jurisdictions move from fixed dates to anniversary-based schedules and back, fee structures are revised, filing categories are reclassified). Do not rely on a cached schedule. The tracker below records the dates you confirm; update them when your contador/administrador sends reminders.

For each jurisdiction where the entity is registered (domestic or foreign):

1. Ask the user whether they have a current compliance report from the contador/administrador responsável — that's the most authoritative source.
2. If not, ask the user what they know (filing type, due-date basis, last filed date, typical fee). Record what they provide.
3. For anything the user does not know, flag the entity × jurisdiction entry as `unknown` — do not populate dates from a cached reference. The user's next step is to confirm with the contador/administrador responsável or Junta Comercial.

**Capture details in the tracker rather than a reference table:**

> I don't have filing requirements for [Jurisdiction] in the reference table.
> Let me capture them so we can track this going forward.
>
> For [Entity] in [Jurisdiction]:
> 1. What type of filing is required? (Declarações à Junta Comercial, Alteração Contratual, AGO, DEFIS, DFP/ITR, Formulário de Referência, ou outro?)
> 2. When is it due? (Fixed date like May 1, anniversary month, or other?)
> 3. What's the typical fee? (Approximate is fine — or "unknown".)
> 4. Who is your contador/administrador responsável or local filing agent there?

Store the answer in a `custom_jurisdictions` block in the tracker:

```yaml
custom_jurisdictions:
  - jurisdiction: "[State / Country]"
    jurisdiction_type: "[US state / Canada province / EU member state / other]"
    filings:
      - type: "[filing type]"
        due_basis: "[fixed: MM-DD / anniversary month / other description]"
        typical_fee: "[amount or unknown]"
        notes: "[any other relevant information — e.g., local agent required, filing in local language]"
    added_by: "manual"
    added_date: "[date]"
```

This custom definition is then applied to all entities in that jurisdiction.
Future `--init` runs and entity additions will use it automatically.

**International jurisdictions specifically:**

International filings vary enormously by jurisdiction. Always go through the
custom definition flow above — confirm the filing type, cadence, and fee with
the local filing agent or registered office agent before populating the tracker.

For international entities, also ask:
- Is there a local filing agent or registered office agent handling compliance?
  If yes, note the agent name — the tracker can flag when to follow up with them
  rather than calculating due dates independently.
- Is the entity required to file any group-level reports in this jurisdiction
  (e.g., country-by-country reporting, beneficial ownership registers,
  economic substance filings)?

Flag international entities with a local agent as `agent_managed: true` in the
tracker. The report mode will list them separately with a note to confirm status
with the local agent rather than showing a calculated due date.

For anniversary-based filings: calculate from the formation_date in the tracker.
If formation_date is null: set status to `unknown` and flag for confirmation.

### Step 3: Write the tracker

Generate `~/.claude/plugins/config/claude-for-legal/corporate-legal/entities/compliance-tracker.yaml` with all entities and their
calculated filing requirements. Set initial status:
- `current` if last_filed is within the current filing period
- `due_soon` if due within 90 days and no last_filed for current period
- `overdue` if due date has passed and no last_filed for current period
- `unknown` if formation_date is missing or state is not in reference table

Show a summary after generating:

```
Entity compliance tracker initialized.

Entities: [N]
Total jurisdictions: [N]
Filings tracked: [N]

Status summary:
  ✅ Current:   [N]
  ⏰ Due soon:  [N] (next 90 days)
  🔴 Overdue:   [N]
  ❓ Unknown:   [N] (confirm with registered agent)

Run /corporate-legal:entity-compliance --report to see what's due.
```

---

## Mode 2: Report

Surfaces upcoming deadlines and flags overdue items. Default: next 90 days.

```
/corporate-legal:entity-compliance --report [--days 30|60|90|180]
```

Output format:

```
ENTITY COMPLIANCE REPORT — [date]
[Company Name]

🔴 OVERDUE ([N]):
  [Entity] / [State] / [Filing type] — was due [date]

⏰ DUE WITHIN [N] DAYS ([N]):
  [Entity] / [State] / [Filing type] — due [date]  [registered agent]
  [Entity] / [State] / [Filing type] — due [date]

✅ RECENTLY FILED ([N] in last 90 days):
  [Entity] / [State] / [Filing type] — filed [date]

❓ UNKNOWN STATUS ([N]):
  [Entity] / [State] / [Filing type] — no information; confirm with registered agent

🌐 AGENT-MANAGED ([N]):
  [Entity] / [Country] / [Filing type] — managed by [local agent]; confirm status directly
  [Entity] / [Country] — no local agent recorded; add one with --update

GOOD STANDING:
  Last confirmed: [date]
  Entities with confirmed good standing: [N] of [total]
  Entities not confirmed in last 12 months: [list]
```

If the tracker covers more than ~10 entities, or any time the user asks: offer the dashboard (see CLAUDE.md `## Outputs → Dashboard offer for data-heavy outputs`). Shape the offer for this output — counts by filing status (overdue / due soon / filed / unknown), counts by good-standing state, and a sortable entity table with jurisdiction, filing type, and next due date.

---

## Mode 3: Update

Updates one or more entities in the tracker. Three sub-modes:

### Consequential-action gate (file SOI / annual report)

**Before directing or confirming a filing:** Read `## Who's using this` in `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md`. If the Role is **Non-lawyer**:

> Filing declarations with the Junta Comercial, alterações contratuais, or tax obligations (DEFIS, ECF, DFP) has legal consequences — it's a formal representation from the entity, it carries fees, and missed or incorrect filings can cause loss of good standing or penalties from the tax authorities and registrar. Have you reviewed this with an attorney (or a qualified contador/advogado responsável) before filing? If yes, proceed to record the filing. If no, here's a brief to bring to them:
>
> - Entity, jurisdiction, filing type, and due date
> - What the tracker says about the last filing (date, fee, officer/partner information last reported)
> - Open questions (is the officer/partner information still accurate; has the registered agent/contador changed; has the registered office changed)
> - What could go wrong (out-of-date partner/officer information, missed 30-day deadline for alteração causing loss of retroactivity, registration or tax compliance failures)
> - What to ask the attorney (is a filing actually needed this year; are there any contract amendments or partner/officer changes that need to be reflected; who should sign)
>
> If you need to find an attorney, solicitor, barrister, or other authorised legal professional: contact your professional regulator (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent) for a referral service.

Do not record a new `last_filed` date past this gate without an explicit yes. Tracker reads, deadline reports, and "what's due soon" output do not require the gate.

### 3a: Manual update

```
/corporate-legal:entity-compliance --update
```

Attorney tells Claude what was filed:
> "Registramos a ata da AGO na Junta Comercial (JUCESP) para [Entity] em 1º de março. Taxa de R$ 150,00."

Claude updates:
- `last_filed` → March 1 date
- `last_fee` → R$ 150,00
- `status` → `current`
- `last_updated` in metadata

### 3b: Registered agent report upload

```
/corporate-legal:entity-compliance --update --from-report
```

User uploads a CT Corp, National Registered Agents, or similar compliance
report (PDF, CSV, or Excel). Claude reads it and updates matching entities:

From the report, extract for each entity:
- Filing type and due date
- Last filed date (if present)
- Good standing status and date confirmed
- Any flags or warnings from the agent

Match report entities to tracker entities by name (flag near-matches for
confirmation — "Acme Holdings LLC" vs. "Acme Holdings, LLC" are probably
the same entity).

After processing:
```
Updated [N] entities from report.

Matched: [N]
Unmatched (in report, not in tracker): [list — may need to add to entity table]
Not in report (in tracker, no update): [list — status unchanged]
```

### 3c: Bulk status sweep

```
/corporate-legal:entity-compliance --sweep
```

Walks through each entity with `unknown` or `overdue` status and asks for
current information one at a time:

> [Entity] / [State] / [Filing type] — currently showing as [status].
> Has this been filed? If yes, when and what was the fee?

Updates tracker after each confirmation. Produces a completion summary.

---

## Mode 4: Health audit

```
/corporate-legal:entity-compliance --audit
```

Broader review beyond just filing status. Surfaces:

**Filing compliance:**
- Overdue items (from report mode)
- Unknown status items

**Entity health:**
- Entities marked as `dormant` — flag for review: should these be dissolved?
  Carrying dormant entities costs money (annual fees, registered agent fees)
  and creates ongoing compliance obligations.
- Entities with formation_date older than 5 years and status `dormant` — flag
  as dissolution candidates.
- Entities missing formation_date — flag as data gap.

**Good standing gaps:**
- Entities with no `confirmed_good_standing` date — unknown whether in good
  standing; risk if a transaction requires a certificate on short notice.
- Entities with `confirmed_good_standing` older than 12 months — stale; worth
  refreshing, especially if M&A or financing is anticipated.

**Foreign qualification gaps:**
- Based on `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` entity table: are there states in the company's
  operational footprint (offices, employees) where entities are not foreign
  qualified? This requires the attorney to confirm operational presence —
  Claude can flag the question but cannot determine presence independently.

**Intercompany agreement gaps:**
- From `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md`: if intercompany agreements are marked as partial or no,
  flag which entity relationships likely need agreements (parent-subsidiary
  services, IP licenses, loans).

Output format:

```
ENTITY HEALTH AUDIT — [date]

FILING COMPLIANCE
  Overdue: [N]
  Unknown status: [N]
  Action: run --sweep to confirm unknown items

DORMANT ENTITIES ([N])
  [List of dormant entities with age and annual carrying cost if known]
  Dissolution candidates (>5 years dormant): [list]

GOOD STANDING
  No record: [N] entities
  Stale (>12 months): [N] entities
  Consider refreshing before: [any upcoming transactions or contract renewals if known]

POTENTIAL GAPS
  Foreign qualification: [flag question — confirm operational presence in:]
    [list of states from `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` footprint not in tracker as qualified]
  Intercompany agreements: [status from `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md`]

RECOMMENDED ACTIONS
  1. [Highest priority action]
  2. [etc.]
```

---

## Mode 5: Export

```
/corporate-legal:entity-compliance --export [--format csv|table]
```

Produces a flat export suitable for sharing with finance, legal ops, or
outside registered agent. Default: CSV.

CSV columns:
`Entity Name, Entity Type, State of Formation, Formation Date, Status,
Registered Agent, Jurisdiction, Qualification Type, Filing Type, Due Date,
Last Filed, Last Fee, Good Standing Confirmed, Notes`

One row per filing per jurisdiction. Multiple rows per entity (one per
jurisdiction × filing type combination).

If `--format table`: produce a markdown table suitable for pasting into
a report or Slack message, showing only the next 90 days of filings.

---

## What this skill does not do

- It does not file anything. Output is a tracker and a to-do list; filing
  is done by the attorney, outside counsel, or registered agent.
- It does not pull good standing certificates. It tracks when certificates
  were last confirmed; obtaining them is manual or via registered agent.
- It does not determine whether foreign qualification is required in a given
  state. That analysis depends on facts about business activity that the
  attorney must confirm.
- It does not replace a registered agent service for companies with complex
  multi-entity structures. CT Corp, National Registered Agents, and similar
  services have dedicated compliance teams and direct state relationships.
  This skill is best suited for smaller organizations without agent support,
  or as a lightweight layer on top of agent data for organizations that do
  have support.
- The filing deadline reference table is not legal advice and may not reflect
  current requirements. Confirm all deadlines before relying on them.


## Formula injection defense

Before writing any cell in Excel, Sheets, or CSV output, neutralize formula injection. Counterparty-sourced text (contract quotes, party names, registered agent data, CLM exports) is attacker-controlled. A cell starting with `=`, `+`, `-`, `@`, `	`, `
`, or `
` will be interpreted as a formula or break the row structure.

- **Prefix with a single quote:** `'=SUM(A1:A10)` → `=SUM(A1:A10)` (displayed as text, not executed)
- **Applies to every cell that contains text sourced from a document, a tool result, or a user paste.** Column headers you control and computed values you produce are safe.
- **CSV: also escape embedded commas, double quotes, newlines** (RFC 4180 quoting).
- This is not optional. A spreadsheet your user opens in Excel that triggers a macro or exfiltrates data via DDE is a supply-chain attack on your user.
