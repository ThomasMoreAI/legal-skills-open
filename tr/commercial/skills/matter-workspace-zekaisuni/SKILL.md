---
name: matter-workspace-zekaisuni
title: /matter-workspace
description: 'Manage matter workspaces: new, list, switch, close, or detach to practice-level. Turkish-law adaptation preserves the original matter isolation function while adding client, vekalet, UYAP-if-applicable, mediation, confidentiality, and conflicts-status fields.'
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/commercial-legal/skills/matter-workspace
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: commercial
language: tr
---

# /matter-workspace

Birden fazla müvekkil veya dosyada çalışan kullanıcılar için bağlam izolasyonu sağlar. Bu skill hukuki strateji üretmez; diğer skill'lere hangi dosya bağlamında çalıştıklarını söyler.

## Subcommands

- `/commercial-legal:matter-workspace new <slug>` - create a matter workspace.
- `/commercial-legal:matter-workspace list` - list active and archived matters.
- `/commercial-legal:matter-workspace switch <slug>` - set active matter.
- `/commercial-legal:matter-workspace close <slug>` - archive, never delete.
- `/commercial-legal:matter-workspace none` - detach to practice-level context.

## Instructions

1. Read `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` and confirm `## Matter workspaces`.
2. If disabled, explain that in-house users normally work at practice-level:

   > Dosya çalışma alanları kapalı. Kurum içi hukuk müşavirliği olarak yapılandırıldığınız için eklenti genel pratik bağlamında çalışır. Birden fazla müvekkil veya şirketle çalışıyorsanız `/commercial-legal:cold-start-interview --redo` ile özel/pratik ayarını güncelleyin.

3. Dispatch on `$ARGUMENTS`.
4. Show proposed changes and confirm before writing.

## Storage Layout

```
~/.claude/plugins/config/claude-for-legal/commercial-legal/
├── CLAUDE.md
└── matters/
    ├── <slug>/
    │   ├── matter.md
    │   ├── history.md
    │   ├── notes.md
    │   └── outputs/
    └── _archived/
```

Keep repo paths in English unless the full plugin has been renamed.

## `new <slug>`

1. Confirm slug is lowercase with hyphens and does not exist in active or archived matters.
2. Run intake:
   - Client / müvekkil.
   - Counterparty / karşı taraf.
   - Matter type: vendor MSA | customer agreement | NDA | SaaS subscription | amendment | renewal | dispute-linked | other.
   - UYAP No: only if a court/enforcement file exists.
   - Vekalet durumu: verildi | beklemede | yok | kurum içi.
   - Conflicts status: yapıldı | beklemede | kapsam dışı.
   - Arabuluculuk dava şartı: true | false | belirsiz.
   - Confidentiality: standard | heightened | mesleki-sır-kısıtlı | clean-team.
   - Key facts: 2-5 sentences.
   - Matter-specific playbook overrides.
   - Related matters.
3. Write `matter.md`.
4. Seed `history.md`.
5. Create empty `notes.md`.
6. Do not auto-switch; ask if the user wants to switch.

## `matter.md` Template

```markdown
[WORK-PRODUCT HEADER - per plugin config]

# Matter: [Client] - [short description]

**Slug:** [slug]
**Opened:** [YYYY-MM-DD]
**Status:** active
**Confidentiality:** [standard / heightened / mesleki-sır-kısıtlı / clean-team]

## Parties

**Client:** [name]
**Counterparty:** [name(s)]
**Vekalet durumu:** [verildi | beklemede | yok | kurum içi]
**Conflicts status:** [yapıldı | beklemede | kapsam dışı]

## Matter Type

[type and one-line rationale]

## UYAP / Dispute Link

**UYAP No:** [if any; otherwise "dava/icra bağlantısı yok"]
**Arabuluculuk:** [dava şartı / değil / belirsiz]

## Key Facts

[2-5 sentences]

## Matter-Specific Overrides

- [override]

## Related Matters

- [slug - reason]

## Confidentiality Notes

[who may see this file; whether cross-matter context is permitted]
```

## `history.md` Seed

```markdown
# History: [Client] - [short description]

Append-only event log. Most recent at top.

## [YYYY-MM-DD] - Matter opened

Intake completed. Slug: `[slug]`. Status: active.
```

## Cross-Matter Context

When `Cross-matter context` is off, no skill may read another matter folder. When on, cross-matter files may be read only if the user explicitly asks for comparison or portfolio analysis.

## What this skill does not do

- It does not run a conflicts check; it records the declared status.
- It does not enforce retention or destruction.
- It does not delete matters.
- It does not decide litigation or negotiation strategy.
- It does not decide whether cross-matter access is appropriate; it obeys the flag and user instruction.
