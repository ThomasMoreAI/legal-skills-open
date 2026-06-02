---
name: matter-workspace-23
title: /matter-workspace
description: 'Privacy/KVKK matter workspace''lerini yönetir: yeni dosya açma, listeleme, aktif dosya değiştirme, arşivleme veya practice-level çalışmaya dönme. Çok müvekkilli veya çok dosyalı KVKK çalışmalarında bağlam ayrımını korur.'
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/privacy-legal/skills/matter-workspace
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: data-protection
language: tr
---

# /matter-workspace

## Komutlar

- `/privacy-legal:matter-workspace new <slug>` - yeni KVKK matter klasörü açar.
- `/privacy-legal:matter-workspace list` - aktif ve arşiv matter'ları listeler.
- `/privacy-legal:matter-workspace switch <slug>` - aktif matter'ı değiştirir.
- `/privacy-legal:matter-workspace close <slug>` - matter'ı arşivler; silmez.
- `/privacy-legal:matter-workspace none` - practice-level bağlama döner.

## Başlamadan

1. `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` dosyasını oku.
2. `## Matter Workspaces` bölümünü kontrol et.
3. `Enabled` kapalıysa kullanıcıya şunu söyle:

   > Matter workspace kapalı. In-house / tek müvekkil kullanımında privacy plugin practice-level bağlamla çalışır. Çok müvekkilli çalışıyorsanız `/privacy-legal:cold-start-interview --redo` ile matter workspace'i açabilirsiniz.

4. Yazmadan önce yapılacak değişikliği göster ve onay al.

## Saklama Yapısı

```text
~/.claude/plugins/config/claude-for-legal/privacy-legal/
├── CLAUDE.md
└── matters/
    ├── <slug>/
    │   ├── matter.md
    │   ├── history.md
    │   ├── notes.md
    │   └── outputs/
    └── _archived/
        └── <slug>/
```

Slug küçük harf, rakam ve tire kullanır: `abc-vendor-dpa-2026`, `calisan-izleme-vked`, `kurul-incelemesi`.

## `new <slug>`

1. Slug aktif veya arşivde kullanılıyor mu kontrol et.
2. Kısa intake yap:
   - Müvekkil / iç iş birimi,
   - karşı taraf / tedarikçi / regülatör,
   - matter türü: use-case triage, VKED, DPA review, ilgili kişi başvurusu, veri ihlali, Kurul incelemesi, yurt dışı aktarım, politika güncellemesi, diğer,
   - veri kategorileri ve veri sahibi grupları,
   - yurt dışı aktarım veya özel nitelikli veri var mı,
   - gizlilik seviyesi: standart / hassas / clean-team,
   - matter'a özel playbook sapması,
   - ilişkili matter'lar.
3. `matter.md`, `history.md`, `notes.md` ve `outputs/` oluştur.
4. Otomatik switch yapma; kullanıcıya switch isteyip istemediğini sor.

## `matter.md` Şablonu

```markdown
GİZLİ HUKUKİ / KVKK ÇALIŞMA TASLAĞI - HUKUKÇU İNCELEMESİNE TABİDİR

# Matter: [Müvekkil/İş Birimi] - [kısa açıklama]

**Slug:** [slug]
**Açılış:** [YYYY-MM-DD]
**Durum:** aktif
**Gizlilik:** standart / hassas / clean-team

## Taraflar

**Müvekkil / iş birimi:** [ad]
**Karşı taraf / tedarikçi / regülatör:** [ad]

## Matter Türü

[use-case triage | VKED | DPA review | ilgili kişi başvurusu | veri ihlali | Kurul incelemesi | yurt dışı aktarım | politika güncellemesi | diğer]

## Kilit Olgular

[2-5 cümle]

## KVKK Kapsamı

- Veri sahibi grupları:
- Veri kategorileri:
- Özel nitelikli veri:
- Yurt dışı aktarım:
- Veri sorumlusu/veri işleyen rolü:

## Matter'a Özel Sapmalar

- [practice-level playbook'tan sapma ve nedeni]

## İlişkili Matter'lar

- [slug - neden ilişkili]

## Gizlilik Notu

[Hassas veya clean-team ise kimler görebilir, cross-matter kapalı mı?]
```

## `list`

`matters/*/matter.md` dosyalarını oku ve tablo üret:

| Slug | Müvekkil/İş birimi | Tür | Durum | Açılış | Aktif |
|---|---|---|---|---|---|

Arşiv matter'ları ayrı başlık altında göster.

## `switch <slug>`

1. `matters/<slug>/matter.md` var mı kontrol et.
2. Practice `CLAUDE.md` içindeki `Active matter:` satırını güncelle.
3. Matter özetini göster.

## `close <slug>`

1. Matter var mı kontrol et.
2. `history.md` dosyasına kapanış kaydı ekle.
3. Klasörü `matters/_archived/<slug>/` altına taşı.
4. Aktif matter kapanıyorsa `Active matter: none - practice-level context only` yaz.

## `none`

Practice `CLAUDE.md` içindeki `Active matter:` satırını `none - practice-level context only` yap.

## Cross-Matter Kuralı

`Cross-matter context` kapalıysa başka matter klasörü okunmaz. Açık olsa bile başka matter ancak kullanıcı açıkça "karşılaştır" veya "önceki dosyalara bak" derse okunur.

## Bu Skill Ne Yapmaz

- Çıkar çatışması kontrolü yapmaz.
- Arşivi silmez.
- Retention/imha kararı vermez.
- Substantive KVKK analizini yapmaz; sadece bağlam klasörünü yönetir.
