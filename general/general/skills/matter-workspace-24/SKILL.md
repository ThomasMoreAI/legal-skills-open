---
name: matter-workspace-24
title: /matter-workspace
description: 'Cok muvekkilli veya cok urunlu kullanimda product matter workspace yonetir: new, list, switch, close, none. Context sizintisini onlemek icindir.'
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/product-legal/skills/matter-workspace
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: tr
---

# /matter-workspace

## Amac

Tek bir sirket ici product counsel kullaniminda genellikle kapali kalir. Ozel hukuk burosu, cok muvekkilli danismanlik veya ayrilmasi gereken urun/muvekkil dosyalari varsa matter workspace her dosyanin context'ini ayri tutar.

## Subcommands

- `/product-legal:matter-workspace new <slug>` - yeni matter ac, kisa intake yap, `matter.md` yaz.
- `/product-legal:matter-workspace list` - matter'lari listele.
- `/product-legal:matter-workspace switch <slug>` - aktif matter'i degistir.
- `/product-legal:matter-workspace close <slug>` - matter'i arsivle, silme.
- `/product-legal:matter-workspace none` - practice-level context'e don.

## Depolama

```text
~/.claude/plugins/config/claude-for-legal/product-legal/
├── CLAUDE.md
└── matters/
    ├── <slug>/
    │   ├── matter.md
    │   ├── history.md
    │   ├── notes.md
    │   └── outputs/
    └── _archived/
```

## Intake

Yeni matter icin sor:

- Muvekkil veya internal business unit,
- urun/ozellik/kampanya adi,
- matter turu: lansman, reklam claim, abonelik/checkout, KVKK/data, AI, sektor risk, diger,
- hedef pazarlar,
- gizlilik seviyesi,
- temel olgular,
- practice profilinden sapmalar,
- ilgili dosyalar/ticket'lar.

## `matter.md` Sablonu

```markdown
# Matter: [Client/BU] - [short description]

**Slug:** [slug]
**Opened:** [YYYY-MM-DD]
**Status:** active
**Confidentiality:** [standard / heightened / clean-team]

## Taraflar ve ekip

**Muvekkil / BU:** [name]
**Urun sahipleri:** [names]
**Hukuk sahibi:** [name]

## Matter turu

[lansman | reklam claim | abonelik/checkout | KVKK/data | AI | sektor risk | diger]

## Temel olgular

[2-5 cumle]

## Matter'a ozel override

- [practice profilinden sapma]

## Ilgili dokumanlar

- [path/link]
```

## Guardrail

- `Cross-matter context: off` ise baska matter dosyasi okunmaz.
- `close` arsivler, silmez.
- Bu skill conflicts check yapmaz; yalnizca kullanicinin beyan ettigi ayrimlari kaydeder.
