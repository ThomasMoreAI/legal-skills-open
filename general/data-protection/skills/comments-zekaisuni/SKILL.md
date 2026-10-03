---
name: comments-zekaisuni
title: /comments
description: 'Türkiye''deki taslak düzenleme ve kamuoyu görüşü sürelerini takip eder; görüş verilecek/verilmeyecek kararlarını ve son tarihleri kaydeder. Kullanım: "açık görüş süreleri", "taslak takip", "comment tracker", "--decide CMT-ID".'
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/regulatory-legal/skills/comments
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: tr
---

# /comments

## Amaç

Taslak düzenleme ve kamuoyu görüşü çağrılarında asıl risk son tarihin kaçmasıdır. Bu skill karar vermez; kararın sahibini, son tarihi ve gerekçeyi görünür tutar.

## Bağlam

- `comment-tracker.yaml`: açık taslak/görüş kayıtları.
- `CLAUDE.md`: varsayılan karar sahibi, kurum listesi, çıktı kuralları.

## Varsayılan Görünüm

```markdown
[ROLE-BASED LEGAL REVIEW HEADER]

## Taslak / Görüş Takibi - [tarih]

### Son 14 gün içinde

| ID | Kurum | Konu | Son tarih | Kalan gün | Karar | Sahip |
|---|---|---|---|---|---|---|

### Açık

[aynı tablo]

### Yakın zamanda karara bağlananlar

| ID | Konu | Karar | Gerekçe |
|---|---|---|---|

---

**Açık kayıt:** [N]  **30 günden az ve kararsız:** [N]
```

## Karar Kaydetme

```
/regulatory-legal:comments --decide CMT-001
Karar: [gorus-verilecek / gorus-verilmeyecek / birlik-uzerinden / ertelendi / sunuldu]
Gerekçe: "[kısa gerekçe]"
```

Görüş verilecekse iç inceleme için son tarihten en az 5 iş günü önce çalışma takibi öner.

## Bildirimler

Slack veya başka bir mesajlaşma entegrasyonu varsa gönderimden önce mutlaka kullanıcıya önizleme göster ve açık onay al. Son tarih, kurum adı veya hukuki sonuç içeren mesajlar otomatik gönderilmez.

## Hukuki Sonuç Kapısı

Kurumlara görüş sunmak, şirketin/klientin pozisyonunu kayıt altına alan hukuki sonuç doğurabilecek bir işlemdir. `CLAUDE.md` rolü non-lawyer ise "görüş verilecek" kararı veya sunuma hazır metin üretmeden önce avukat incelemesi sorulur ve kısa briefing hazırlanır.

## Yapmadıkları

- Görüş mektubunu nihai olarak sunmaz.
- Kararı kendisi vermez.
- Taslak metni yürürlükte bağlayıcı düzenleme gibi değerlendirmez.
