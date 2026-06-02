---
name: legal-researcher
title: Legal Researcher
description: Hukuki araştırma, içtihat tarama, mevzuat takibi, Yargıtay kararları ve hukuki makale yazımı.
author: mikailustuner
author_url: https://github.com/mikailustuner/OmniRule/tree/main/skills/legal-researcher
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: general
language: tr
---

# Legal Researcher

**Odağ Alanı:** Türk hukuku kapsamında mevzuat araştırması, Yargıtay/Danıştay içtihatlarının taranması, karşılaştırmalı hukuk analizi ve hukuki makale yazımı.

## Pattern 1: Mevzuat Araştırma Protokolü

```
1. NORMATİF HİYERARŞİ ARAŞTIRMA
├── ANAYASA düzeyi
│   ├── Temel hak ve özgürlükler
│   ├── Devletin temel organları
│   └── Anayasa Mahkemesi kararları
│
├── YASA düzeyi
│   ├── 4721 sayılı Türk Medeni Kanunu
│   ├── 6098 sayılı Borçlar Kanunu (TBK)
│   ├── 6102 sayılı Türk Ticaret Kanunu (TTK)
│   ├── 6331 sayılı İş Sağlığı ve Güvenliği Kanunu
│   └── 6502 sayılı Tüketicinin Korunması Hakkında Kanun
│
├── YÖNETMELİK/TEBLİĞ düzeyi
│   ├── BDDK düzenlemeleri
│   ├── SPK tebliğleri
│   ├── BTK yönetmelikleri
│   └── İlgili sektör Bakanlık tebliğleri
│
└── GENELGELER VE YARGI KARARLARI
    ├── Yargıtay Genel Kurul içtihatları
    ├── Danıştay içtihatları
    ├── Anayasa Mahkemesi kararları
    └── Uyuşmazlık Mahkemesi kararları

2. HUKUK DALINA GÖRE ARAŞTIRMA AĞACI
├── Medeni Hukuk
│   ├── Şahıs varlıkları (kişilik, erişim hakkı)
│   ├── Aile hukuku (nişan, evlilik, boşanma)
│   ├── Miras hukuku (miras paylaşımı, vasiyet)
│   └── Eşya hukuku (mülkiyet, intifa, rehin)
│
├── Borçlar Hukuku
│   ├── Genel hükümler (borç kaynakları, ifa)
│   ├── Sözleşme hukuku (kurulma, hükümsüzlük)
│   ├── Haksız fiil sorumluluğu
│   └── Sebepsiz zenginleşme
│
├── Ticaret Hukuku
│   ├── Ticari işlem (müteselsil sorumluluk)
│   ├── Şirketler hukuku (anonim, limited)
│   ├── Kıymetli evrak (çek, bono, poliçe)
│   └── Sigorta hukuku
│
├── İş Hukuku
│   ├── Bireysel iş hukuku
│   ├── Toplu iş hukuku (sendika, toplu iş sözleşmesi)
│   ├── İş sağlığı ve güvenliği
│   └── Sosyal güvenlik hukuku
│
└── Kamu Hukuku
    ├── İdare hukuku (idari işlem, Kamu İhale Kanunu)
    ├── Ceza hukuku (maddi ceza hukuku, usul)
    ├── Anayasa hukuku
    └── Vergi hukuku
```

## Pattern 2: İçtihat Tarama Protokolü

```
1. YARGI KARARI ARAMA STRATEJİSİ
├── KARAR TİPİNİ BELİRLE
│   ├── Yargıtay Hukuk Genel Kurulu (en yüksek içtihat)
│   ├── Yargıtay Daire kararları (uygulama birliği)
│   ├── Yargıtay Genel Kurul kararları (içtihat birleştirme)
│   ├── Danıştay İdari Daireler Kurulu
│   └── Anayasa Mahkemesesi bireysel başvuru kararları
│
├── ANAHTAR KELİME STRATEJİSİ
│   ├── Fact: "Yargıtay 11. HD", "2020/3541 E.", "2021/1234 K."
│   ├── Konu: "haksız şart", "tek taraflı fesih", "mücbir sebep"
│   ├── Hukuki terim: "imkansızlık", "muvazaa", "hazine"
│   └── Karşılaştırmalı: "AB Directive", "CISG Article 7"
│
├── VERİ TABANI SEÇİMİ
│   ├── Lexpera (lexpera.com) – Türkçe içtihat veritabanı
│   ├── Legalbank (legalbank.net) – Yargıtay kararları
│   ├── Sayistay Kararları (sayistay.gov.tr)
│   ├── UYAP (uyap.gov.tr) – Resmi yargı veritabanı
│   ├── E-Justice EU (e-justice.europa.eu) – AB kararları
│   └── Westlaw / LexisNexis – Uluslararası kararlar
│
└── FİLTRELEME KRİTERLERİ
    ├── Tarih aralığı: Son 5 yıl (güncel içtihat) / Tümü (kök içtihat)
    ├── Karar sonucu: Kabul / Ret / Kısmi kabul
    ├── Dava değeri: Alt/üst sınır (mali yetki)
    └── Coğrafi: İstanbul / Ankara / İzmir (yerel mahkeme içtihatları)

2. İÇTİHAT DEĞERLENDİRME MATRİSİ
┌────────────────────┬──────────┬──────────┬──────────┬──────────┐
│ Karar               │ İçtihat │ Tarih    │ Daire   │ Sonuç    │
│                     │ Ağırlığı │          │         │          │
├────────────────────┼──────────┼──────────┼──────────┼──────────┤
│ Yargıtay HGK       │ ★★★★★   │ 2019     │ HGK     │ Bağlayıcı│
│ Yargıtay Daire     │ ★★★★    │ 2021-24  │ 11. HD  │ Yönlendir│
│ Danıştay DDK       │ ★★★★    │ 2020     │ DDK     │ Yönlendir│
│ Bölge Adliye       │ ★★★     │ 2023     │ 12. HD  │ Gösterge │
│ İlk Derece         │ ★★      │ 2024     │ İstanbul│ Bakınız  │
└────────────────────┴──────────┴──────────┴──────────┴──────────┘
```

## Pattern 3: Hukuki Makale Yazım Pattern

```
MAKALE YAZIM AKIŞI (5 Faz)

FAZ 1: KONU VE KAPSAM TANIMLAMA
├── Araştırma sorusu formüle etme
│   └── "Yapay zeka ürünlerinin tüketici hukuku kapsamında sorumluluğu nasıl belirlenir?"
├── Alt sorular belirleme (3-5 adet)
└── Ana tez hipotezini oluşturma

FAZ 2: ARAŞTIRMA VE ANALİZ
├── Mevzuat tarama (normatif çerçeve)
├── İçtihat tarama (Yargıtay/Danıştay)
├── Doktrin tarama (Türk/uluslararası hukukçular)
├── Karşılaştırmalı hukuk (ABD, AB, Almanya)
└── Saha araştırması (varsa istatistikler, anketler)

FAZ 3: YAPI VE TASLAK
├── I. GİRİŞ
│   ├── Konunun önemi ve güncelliği
│   ├── Araştırma sorusu ve hipotez
│   └── Metodoloji (kullanılan kaynaklar)
│
├── II. NORMATİF ÇERÇEVE
│   ├── İlgili mevzuat hükümleri
│   ├── Yönetmelik ve içtihat
│   └── Uluslararası düzenlemeler
│
├── III. DOKTRİN VE İÇTİHAT ANALİZİ
│   ├── Yazar görüşleri (farklı görüşler)
│   ├── Destekleyen ve aykırı içtihatlar
│   └── Tartışmalı noktalar
│
├── IV. DEĞERLENDİRME VE ÇÖZÜM ÖNERİSİ
│   ├── Mevcut durum analizi
│   ├── Eksiklik ve boşluklar
│   ├── Çözüm önerileri
│   └── Gelecek perspektifi
│
└── V. SONUÇ
    └── Kısa özet + sonuç + öneriler

FAZ 4: ATIF VE KAYNAKÇA
├── İç metin atfı (Chicago / Turabian / APA)
├── Kaynakça düzenleme
└── İntihal kontrolü

FAZ 5: GÖZDEN GEÇİRME
├── Hukuki terminoloji kontrolü
├── Mezmua kontrolü (varsa)
└── Akademik danışmanlık
```

## Key Patterns (Özet)

| Adım | Eylem | Çıktı |
|---|---|---|
| 1 | Hukuk dalı ve alt konu tespiti | Araştırma çerçevesi |
| 2 | Mevzuat hiyerarşisine göre tarama | Normatif referans listesi |
| 3 | Yargıtay/Danıştay karar taraması | İçtihat özetleri (10-20 adet) |
| 4 | İçtihat değerlendirme matrisi | İçtihat ağırlık puanlaması |
| 5 | Doktrin ve karşılaştırmalı analiz | Teorik çerçeve |
| 6 | Makale yazımı / özet rapor | Tamamlanmış hukuki belge |

## Anti-Patterns

```
❌ YALNIZCA GOOGLE ARAMA
   Google sonuçları kaynak doğrulaması yapılmamış içeriklerle doludur.
   → Resmi veritabanları (Lexpera, UYAP, Sayistay) birincil kaynak olmalı.

❌ GÜNCEL OLMAYAN MEVZUATA ATIF
   2001 tarihli TBK yürürlükte olmayan maddelerine atıf yapılabilir.
   → "Son güncelleme: [tarih]" notu düşülmeli ve mevzuat değişiklikleri kontrol edilmeli.

❌ FARKLI YARGI DAİRELERİNİ KARIŞTIRMA
   Yargıtay 11. HD ile 15. HD'nin içtihatları farklı olabilir.
   → Hangi dairenin kararı olduğu mutlaka belirtilmeli.

❌ TEK KARARA DAYALI GENELLEME
   Bir Yargıtay kararı "içtihat" anlamına gelmez.
   → En az 3 kararlık bir tutarlılık aranmalı.

❌ KARŞILAŞTIRMALI HUKUKU YÜZEYSEL YAPMA
   "Almanya'da da böyle" demek yeterli değildir.
   → Kaynak kanun maddesi, karar tarihi ve veri tabanı belirtilmeli.

✅ DOĞRU YAPI
   Hukuk dalı belirle → Normatif hiyerarşi oluştur →
   Birincil kaynaklarda araştır → İçtihat matrisini doldur →
   Doktrin sentezi yap → Makaleyi yapılandır → Kaynakça derle
```

## Quick Reference

| Görev | Kaynak | URL / Araç |
|---|---|---|
| Yargıtay kararları | Lexpera / Legalbank | lexfera.com, legalbank.net |
| Danıştay kararları | Danıştay resmi sitesi | danistay.gov.tr |
| Mevzuat araştırma | Resmi Gazete / Mevzuat Bilgi Sistemi | resmigazete.gov.tr, mevzuat.gov.tr |
| Sayıştay kararları | Sayıştay Başkanlığı | sayistay.gov.tr |
| AB mevzuatı | EUR-Lex | eur-lex.europa.eu |
| Uluslararası sözleşmeler | Birleşmiş Milletler | treaties.un.org |
| Atıf formatı | Chicago Manual of Style | chicagomanualofstyle.org |
| İntihal kontrolü | Turnitin / İthenticate | turnitin.com |
| Türk Medeni Kanunu | Kazancı Mevzuat | kazanci.com |
| Karşılaştırmalı hukuk | Max Planck Encyclopedia | mopilaw.mprg.de |

---

*Uyarı: Bu araştırma rehberi akademik ve profesyonel kullanım içindir. Hukuki danışmanlık yerine geçmez.*


## 🌍 Universal Language Support
- **Turkish Native:** This skill natively supports Turkish. If the user prompt is in Turkish, all analysis, formatting, and output MUST be entirely in Turkish. You do not need explicit "write in Turkish" instructions.
