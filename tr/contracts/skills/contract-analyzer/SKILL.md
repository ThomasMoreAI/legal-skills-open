---
name: contract-analyzer
title: Contract Analyzer
description: Sözleşme özetleme, risk tespiti, madde analizi, yükümlülük takibi ve çeviri desteği.
author: mikailustuner
author_url: https://github.com/mikailustuner/OmniRule/tree/main/skills/contract-analyzer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: contracts
language: tr
---

# Contract Analyzer

**Odağ Alanı:** Ticari sözleşmelerin yapısal analizi, risk tespiti, kritik madde belirleme ve tarafların yükümlülük takibi.

## Pattern 1: Sözleşme Okuma ve Sınıflandırma

```
1. SÖZLEŞME TIPI BELIRLEME
├── Satış Sözleşmesi (TBK m. 207)
│   ├── Mal satışı
│   ├── Hizmet satışı
│   └── Eser sözleşmesi
├── İş Sözleşmesi (TBK m. 393)
│   ├── Belirli süreli
│   ├── Belirsiz süreli
│   └── Çağrı üzerine çalışma
├── Kira Sözleşmesi (TBK m. 299)
│   ├── Konut Kira
│   ├── İşyeri Kira
│   └── Ürün Kira (leasing)
├── Temsilcilik/Multiği
│   ├── Acente sözleşmesi
│   ├── Distribütörlük
│   └── Franchise
├── Finansal Sözleşmeler
│   ├── Kredi sözleşmesi
│   ├── Factoring
│   ├── Forfaiting
│   └── Leasing
└── Dijital/Teknoloji Sözleşmeleri
    ├── SaaS anlaşması
    ├── Lisans sözleşmesi
    ├── Veri işleme anlaşması (DPA)
    └── SLA (Hizmet Seviyesi Anlaşması)

2. BELGE YAPISINI ÇÖZÜMLEME
├── Giriş bölümü (taraflar, tarih, tanımlar)
├── Ana hükümler (konu, kapsam, bedel)
├── Yükümlülükler bölümü
├── Ceza/teminat hükümleri
├── Fesih/iptal koşulları
├── Uyuşmazlık çözümü ( yetki/tespit)
└── Ekler ve protokoller
```

## Pattern 2: Risk Tespiti (Red Flag Analysis)

```
1. YÜKSEK RİSKLİ MADDELER
├── Tek taraflı değişiklik hakları
│   └── "Taraflardan biri bu sözleşmeyi tek taraflı olarak değiştirebilir"
├── Olağanüstü fesih hakları
│   └── 15 gün önceden fesih bildirimi ile sonlandırma
├── Aşırı ceza şartları
│   └── Gecikme halinde günlük %X cezai şart
├── Kısıtlayıcı rekabet yükümlülükleri
│   └── Sözleşme süresinin 2 katı boyunca rekabet yasağı
├── Veri ihlali yükümlülükleri
│   └── Sınırsız maddi sorumluluk
└── Yabancı hukuk/ tahkim kaydı
    └── Türk mahkemelerinin yetkisinin düşürülmesi

2. ORTA RİSKLİ MADDELER
├── Belirsiz tanımlar
│   └── "Makul süre", "olağan şartlar" gibi muğlak ifadeler
├── Otomatik yenileme mekanizmaları
│   └── Yenilenmeme bildirimi yapılmazsa otomatik uzatma
├── Sınırlı garanti süreleri
│   └── Ürün garantisi 6 aydan kısa
├── Eksik çekince hakları
│   └── Mücbir sebep tanımının darlığı
└── Katma değer vergisi hariç bedel
    └── "Bedel KDV hariçtir" kaydı

3. DÜŞÜK RİSKLİ MADDELER
├── Açık tanımlanmış konu ve kapsam
├── Dengeli fesih koşulları
├── Orantılı cezai şartlar
├── Makul ifa süreleri
└── Net uyuşmazlık çözüm mekanizması
```

## Pattern 3: Madde Analizi ve Kategorilendirme

```
HER MADDE İÇİN 5 BOYUTLU ANALIZ:
├── [1] HUKUKİ NITELIK
│   ├── CB (Ciddi Bağlayıcı) – Mutlak uyulması gereken
│   ├── KO (Koşullu) – Belirli şartlarda geçerli
│   ├── OP (Opsiyonel) – İsteğe bağlı uygulanabilir
│   └── TT (Tavsiye/Telif) – Yönlendirici nitelikte
│
├── [2] RİSK SEVİYESİ
│   ├── 🔴 KRITIK (>10 puan): Hukuki sonuç doğurabilir
│   ├── 🟡 YÜKSEK (5-10 puan): Ticari kayıp riski
│   ├── 🟢 DÜŞÜK (<5 puan): Operasyonel etki
│   └── ⚪ NÖTR: Standard madde
│
├── [3] MUHATAP TARAF ETKİSİ
│   ├── Sizin yükümlülüğünüz: +Puan
│   ├── Karşı tarafın yükümlülüğü: -Puan
│   └── Karşılıklı: 0 Puan
│
├── [4] PAZARLIK DURUMU
│   ├── TBD (Tartışılabilir) – Pazarlık edilebilir
│   ├── RZ (Reddedilemez) – Karşı taraf kabul etmez
│   └── KR (Kabul Edilebilir) – Mevcut haliyle makul
│
└── [5] ÖNERİ
    ├── "Olduğu gibi kabul et"
    ├── "Şu değişiklikle kabul et"
    └── "Müzakere et veya reddet"
```

## Pattern 4: Yükümlülük Takip Matrisi

```
TARAF YÜKÜMLÜLÜK MATRİSİ (Obligation Tracker)
┌──────────────┬─────────────────────────────┬────────────┬────────────┬──────────────┐
│ Yükümlülük   │ Madde Referansı            │ Başlangıç  │ Bitiş       │ Ceza/Sanki  │
├──────────────┼─────────────────────────────┼────────────┼────────────┼──────────────┤
│ Teslimat     │ madde 4.1, 4.2             │ imza tarihi│ +60 gün    │ Gecikme     │
│              │                             │            │            │ bedeli %0.5/ │
│              │                             │            │            │ gün          │
├──────────────┼─────────────────────────────┼────────────┼────────────┼──────────────┤
│ Ödeme        │ madde 5.1, 5.2, 5.3        │ mal kabulı │ +30 gün    │ Temerrüt    │
│              │                             │            │            │ faizi %3/ay │
├──────────────┼─────────────────────────────┼────────────┼────────────┼──────────────┤
│ Garanti      │ madde 6.1                   │ teslimat    │ +24 ay     │ Onarım/     │
│              │                             │            │            │ değişim     │
├──────────────┼─────────────────────────────┼────────────┼────────────┼──────────────┤
│ Rekabet      │ madde 8.1, 8.2              │ imza tarihi│ sözleşme   │ Tazminat    │
│ yasağı       │                             │            │ sonu +12ay │ bedeli x 3   │
└──────────────┴─────────────────────────────┴────────────┴────────────┴──────────────┘
```

## Key Patterns (Özet)

| Adım | Eylem | Çıktı |
|---|---|---|
| 1 | Sözleşme tipi sınıflandırması | Kategori + ilgili mevzuat referansı |
| 2 | Geliş yapısını haritalama | Bölüm-madde endeksi |
| 3 | Riskli maddeleri tarama | Red flag listesi (kritik öncelik sırası) |
| 4 | Her maddeyi 5 boyutta analiz etme | Puanlama matrisi |
| 5 | Yükümlülük takip tablosu oluşturma | Deadline + ceza takibi |
| 6 | Özet rapor hazırlama | Yönetici özeti + detaylı bulgular |

## Anti-Patterns

```
❌ SÖZLEŞME METNİNİ OLDUĞU GİBİ KABUL ETME
   Karşı tarafın hukuk danışmanı sizin için sürpriz maddeleri gizlemiştir.
   → Her "ve benzeri", "makul", "gerekli gördüğü" ifadesini sorun.

❌ YALNIZCA BEDEL MADDESİNE BAKMA
   Bedel yanında cezai şartlar, garantiler ve fesih koşulları eşit derecede kritiktir.
   → Tüm kritik maddeleri ayrı ayrı analiz edin.

❌ KAYNAKSIZ YORUM YAPMA
   "Bu madde Yargıtay içtihadına göre geçersizdir" demek, kaynak göstermeden hatalı olabilir.
   → Her hukuki yorum için mevzuat/ içtihat referansı ekleyin.

❌ TÜM RİSKLERİ EŞİT GÖRME
   Kısıtlayıcı rekabet maddesi ile yazım hatası aynı önemde değildir.
   → Risk puanlaması ile öncelik sırası belirleyin.

✅ DOĞRU ANALIZ
   Önce sözleşme tipini tespit et → İlgili mevzuat çerçevesini belirle →
   Red flag taraması yap → Her maddeyi 5 boyutta puanla →
   Yükümlülük matrisini çıkar → Hukuki görüş taslağı hazırla

✅ AÇIK KAYNAK REFERANSI
   "TBK m. 112 – Borç ifasının temerrüdü" veya "Yargıtay 11. HD 2019/4078 E. kararı"
   Her yorumu normatif metin veya içtihat ile destekle.
```

## Quick Reference

| Durum | Araç/Kaynak | Kullanım |
|---|---|---|
| Sözleşme tarama | Red Flag Checklist | Kritik maddeleri işaretle |
| Risk puanlama | 5-Boyut Analiz Matrisi | Her maddeyi 0-10 arası puanla |
| Yükümlülük takibi | Obligation Tracker | Deadline + ceza matrisini çıkar |
| Hukuki referans | TBK, TTK, İş Kanunu | İlgili mevzuat hükümlerini eşleştir |
| İçtihat araştırma | Yargıtay Kararları (lexpera, legalbank) | Tartışmalı maddeleri doğrula |
| Çeviri desteği | Yeminli tercüman onayı | Resmi belgeler için zorunlu |
| Özet rapor | 1 sayfa exec summary + detay | Yönetici ve hukuk ekibi için ayrı çıktı |
| Karşılaştırma | Benchmark sözleşmeler | Sektör standardı ile kıyasla |

---

*Kritik uyarı: Bu analiz hukuki danışmanlık yerine geçmez. Ticari kararlar için mutlaka yetkili hukuk danışmanına danışılmalıdır.*


## 🌍 Universal Language Support
- **Turkish Native:** This skill natively supports Turkish. If the user prompt is in Turkish, all analysis, formatting, and output MUST be entirely in Turkish. You do not need explicit "write in Turkish" instructions.
