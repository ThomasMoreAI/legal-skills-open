---
name: matter-workspace-25
title: /matter-workspace
description: Birden çok müvekkil/iş/regülasyon projesi için ayrı matter workspace oluşturur, listeler, aktif hale getirir veya arşivler.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/regulatory-legal/skills/matter-workspace
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: tr
---

# /matter-workspace

## Komutlar

- `/regulatory-legal:matter-workspace new <slug>` - yeni matter oluşturur.
- `/regulatory-legal:matter-workspace list` - matter listesini gösterir.
- `/regulatory-legal:matter-workspace switch <slug>` - aktif matter seçer.
- `/regulatory-legal:matter-workspace close <slug>` - matter'ı arşivler, silmez.
- `/regulatory-legal:matter-workspace none` - practice-level bağlama döner.

## Talimat

1. `CLAUDE.md -> Matter workspaces` bölümünü oku.
2. `Enabled` kapalıysa kullanıcıya bunun in-house/practice-level varsayılan olduğunu söyle; hata verme.
3. Yazmadan önce değişikliği göster ve onay al.
4. Cross-matter context kapalıysa başka matter klasörü okuma.

## Depolama

```text
~/.claude/plugins/config/claude-for-legal/regulatory-legal/
├── CLAUDE.md
└── matters/
    ├── <slug>/
    │   ├── matter.md
    │   ├── history.md
    │   ├── notes.md
    │   └── outputs/
    └── _archived/
```

Slug küçük harf ve tire kullanır: `kvkk-ihlal-2026`, `spk-teblig-gap`, `rekabet-sorusturma`.

## Intake

Yeni matter için kısa bilgiler:

- Müvekkil / iç iş birimi.
- Karşı taraf veya ilgili kurum.
- Matter türü: düzenleme takibi, görüş süreci, gap remediation, kurum incelemesi, yaptırım/soruşturma yanıtı, sürekli izleme, diğer.
- Gizlilik seviyesi: standart, heightened, clean-team.
- Temel olgular: 2-5 cümle.
- Practice playbook'tan sapmalar.
- İlgili matter'lar.

## matter.md Şablonu

```markdown
[ROLE-BASED LEGAL REVIEW HEADER]

# Matter: [Müvekkil / iş birimi] - [kısa açıklama]

**Slug:** [slug]
**Açılış:** [YYYY-MM-DD]
**Durum:** active
**Gizlilik:** [standard / heightened / clean-team]

## Taraflar / kurumlar

**Müvekkil / iş birimi:** [ad]
**İlgili kurum / karşı taraf:** [ad]

## Matter türü

[düzenleme takibi | görüş süreci | gap remediation | kurum incelemesi | yaptırım yanıtı | diğer]

## Temel olgular

[2-5 cümle]

## Matter'a özel notlar

- [özel eşik, zamanlama, gizlilik veya escalation notu]

## İlgili matter'lar

- [slug - neden ilgili]
```

## Yapmadıkları

- Çıkar çatışması kontrolü yapmaz.
- Retention politikası uygulamaz.
- Matter arşivini silmez.
