---
name: policy-redraft-zekaisuni
title: /policy-redraft
description: Policy-diff veya gaps sonucunda bulunan boşluğu kapatmak için Türkçe/İngilizce iç politika üzerinde öneri redraft üretir. Kaynak politika dosyasını değiştirmez; ayrı bir öneri memo'su yazar.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/regulatory-legal/skills/policy-redraft
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: tr
---

# /policy-redraft

## İlkeler

1. Bu bir **öneridir**, onaylı politika değişikliği değildir.
2. Kaynak politika dosyasının üzerine yazma.
3. Gap'i kapatma; kapanış, politika sahibi uygulayıp onayladıktan sonra yapılır.
4. Düzenleme statüsü doğrulanamıyorsa banner ekle.
5. En küçük gerekli değişikliği öner; stil/restyle yapma.
6. `[verify]` ve kaynak etiketlerini redraft içinde taşı.

## Gerekli Girdiler

- Gap: `GAP-ID`, policy-diff özeti veya kullanıcının açıklaması.
- Güncel onaylı politika metni: dosya yolu veya yapıştırılmış metin.
- Düzenleme metni: birincil kaynak, policy-diff çıktısı veya kullanıcı metni.

Politika metni dosyadan gelirse şu soruyu sor: "Bu politikanın en güncel ve onaylı versiyonu mu?" Yanıtı reviewer note'a yaz.

## Statü Kontrolü

Resmi Gazete, Mevzuat veya ilgili kurum sayfasından doğrulama yapılamıyorsa:

> `DÜZENLEME DURUMU DOĞRULANAMADI - Bu redraft önerisi uygulanmadan önce metin, yürürlük ve geçiş tarihi birincil kaynaktan teyit edilmelidir.`

## Redraft Formatı

- Silinen metin: `~~metin~~`
- Eklenen metin: **metin**
- Her değişiklik kısa gerekçe taşır: `[Değişiklik: KVKK Kurul rehberi/kaynak gereği ...]`
- Belirsiz tarih, eşik veya madde: `[verify]`

## Çıktı

```markdown
[ROLE-BASED LEGAL REVIEW HEADER]

> **Reviewer note**
> - Kaynaklar: [Resmi Gazete/Mevzuat/Kurum/user provided/verify]
> - İncelenen politika bölümleri: [liste]
> - Doğrulama durumu: [doğrulandı / doğrulanamadı]
> - Uygulamadan önce: politika sahibinin onayı, yürürlük kontrolü, değişiklik yönetimi ve gap tracker güncellemesi gerekir.

## Policy Redraft - [Politika adı]

**Gap:** [GAP-ID veya kısa açıklama]
**Düzenleme:** [ad, kaynak, tarih]
**Politika:** [ad, versiyon/tarih]
**Statü:** ÖNERİ - henüz onaylanmadı

### Kısa sonuç

[Boşluk ne, öneri neyi değiştiriyor, hangi konu insan incelemesi istiyor]

### İşaretli politika bölümü

[Sadece etkilenen bölüm]

### Değişiklik özeti

| # | Bölüm | Mevcut | Öneri | Neden | Kaynak |
|---|---|---|---|---|---|

### Uygulamadan önce

- [ ] Metnin en güncel onaylı politika olduğu teyit edildi.
- [ ] Düzenlemenin yürürlük/güncellik durumu doğrulandı.
- [ ] Politika sahibi ve gerekirse hukuk/compliance onayı alındı.
- [ ] Değişiklik yönetimi süreci işletildi.
- [ ] Gap ancak uygulama ve onaydan sonra kapatıldı.
```

Dosya adı: `[policy-name]-proposed-redraft-[YYYY-MM-DD].md`. Matter workspace aktifse oraya, değilse kullanıcının belirttiği çalışma alanına yaz.

## Yapmadıkları

- Kaynak politikaya doğrudan uygulamaz.
- Gap'i kendiliğinden kapatmaz.
- Birden çok politikayı tek seferde yeniden yazmaz.
