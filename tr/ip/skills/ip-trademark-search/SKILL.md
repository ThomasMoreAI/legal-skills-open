---
name: ip-trademark-search
title: IP Trademark Search
description: Marka/patent araştırması, TürkPatent sorgusu, Nice sınıflandırması ve benzerlik analizi.
author: mikailustuner
author_url: https://github.com/mikailustuner/OmniRule/tree/main/skills/ip-trademark-search
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: ip
language: tr
---

# IP Trademark Search

**Odağ Alanı:** TürkPatent üzerinden marka ve patent araştırması, Nice sınıflandırma sistemine göre mal/hizmet kategorilendirme, görsel ve fonetik benzerlik analizi, uluslararası marka koruma stratejisi.

## Pattern 1: Marka Araştırma Protokolü

```
1. MARKA ARAŞTIRMA TÜRLERİ
├── ÖN İNCELEME (Preliminary Search)
│   ├── Amaç: Fikri mülkiyet hakkı başvurusu öncesi hızlı tarama
│   ├── Kapsam: Yalnızca tam eşleşme (exact match)
│   ├── Süre: < 1 saat
│   └── Kullanım: İlk karar verme (başvuruya değer mi?)
│
├── TAM DOSYALI ARAŞTIRMA (Full Search)
│   ├── Amaç: Başvuru öncesi kapsamlı risk analizi
│   ├── Kapsam: Tam + benzer + fonetik + görsel eşleşme
│   ├── Süre: 2-5 iş günü
│   └── Kullanım: Başvuru kararı öncesi nihai değerlendirme
│
├── İZLEME ARAŞTIRMASI (Watching)
│   ├── Amaç: Mevcut tescilli markanın takibi
│   ├── Kapsam: Benzer başvuruların periyodik taraması
│   ├── Süre: Sürekli (3/6/12 aylık periyotlar)
│   └── Kullanım: Mevcut markayı korumak için
│
└── KARŞI ARAŞTIRMA (Opposition Search)
    ├── Amaç: Rakip marka başvurularına itiraz hazırlığı
    ├── Kapsam: Belirli başvuru numarası veya tarih aralığı
    └── Süre: Başvuru yayın tarihinden itibaren 3 ay içinde

2. ARAŞTIRMA KAYNAKLARI
├── TÜRKİYE: TürkPatent (TPE)
│   └── tp.gov.tr – TürkPatent Sorgulama Sistemi
│
├── AB: EUIPO (Avrupa Birliği Fikri Mülkiyet Ofisi)
│   └── euipo.europa.eu – eSearch plus
│
├── ULUSLARARASI: WIPO (Dünya Fikri Mülkiyet Örgütü)
│   └── wipo.int – Madrid Monitor (marka) + PATENTSCOPE (patent)
│
├── AMERİKA: USPTO (ABD Patent ve Marka Ofisi)
│   └── uspto.gov – TESS ( trademark search system)
│
├── İNGİLTERE: IPO ( Intellectual Property Office)
│   └── gov.uk/government/organisations/intellectual-property-office
│
└── JAPONYA: JPO
    └── j-platpat.inpit.go.jp – Japonca/İngilizce sorgu
```

## Pattern 2: TürkPatent Sorgulama Adımları

```
TÜRKPATENT MARKA ARAMA PROSEDÜRÜ (Adım Adım)

ADIM 1: GİRİŞ
├── URL: https://search. trademarks.tpe.gov.tr
├── Giriş: TC Kimlik No veya e-Devlet şifresi (başvuru sahibi)
└── Misafir sorgulama: Sınırlı sayıda sorgu (günlük 10 sorgu)

ADIM 2: TEMEL ARAMA KRİTERLERİ
├── Marka adı: Kelime veya kelime grubu
│   └── İpucu: Tire (-) veya bosluk kullanmadan her iki varyasyonu da dene
├── Sahip/başvuru sahibi: Şirket veya gerçek kişi adı
├── Başvuru/Tescil numarası: Biliyorsanız direkt erişim
├── Nice sınıfı: Belirli bir sınıftaki kayıtlar
└── Durum filtreleri: Başvuru / Tescil / Ret / İtiraz

ADIM 3: GELİŞMİŞ ARAMA (Boolean Operatörleri)
├── AND: "soft AND bank" → Her iki kelime de geçen sonuçlar
├── OR: "soft OR bank" → Herhangi bir kelime geçen sonuçlar
├── NOT: "soft NOT bank" → soft var, bank yok
├── Wildcard: "sof*" → sof ile başlayan tüm sonuçlar
└── Fonetik: "~" operatörü (sesbenzerlik araması, sınırlı)

ADIM 4: SONUÇ DEĞERLENDİRME KRİTERLERİ
┌────────────────┬─────────────────────────────────────────────────────────┐
│ Değerlendirme  │ Kriter                                                    │
│ Boyutu         │                                                          │
├────────────────┼─────────────────────────────────────────────────────────┤
│ Kayıtlılık     │ Aktif tescil mi? (Tescilsiz başvurular daha az riskli)│
│ Durumu         │ Ret / İtiraz / Yayın aşamasında / Terkin                │
├────────────────┼─────────────────────────────────────────────────────────┤
│ Nice sınıfı    │ Başvurduğunuz sınıfla aynı veya aşırı mı?               │
│                 │ Yakın sınıflar da çakışma yaratabilir                   │
├────────────────┼─────────────────────────────────────────────────────────┤
│ Mal/hizmet     │ Tam veya kısmi örtüşme mi?                               │
│ Kapsamı       │ Aynı kategoride mi farklı alt kategori mı?               │
├────────────────┼─────────────────────────────────────────────────────────┤
│ Benzerlik      │ Görsel benzerlik (logotype)?                             │
│                 │ Fonetik benzerlik (telaffuz)?                           │
│                 │ Kavramsal benzerlik (anlam)?                            │
├────────────────┼─────────────────────────────────────────────────────────┤
│ Coğrafi        │ Türkiye geneli mi, bölgesel mi?                          │
│ Kapsam         │ Uluslararası yayılma var mı? (WIPO Madrid)             │
├────────────────┼─────────────────────────────────────────────────────────┤
│ Sahip          │ Gerçek kişi mi, şirket mi?                                 │
│ profili        │ Aktif işletme mi, pasif mi?                               │
└────────────────┴─────────────────────────────────────────────────────────┘
```

## Pattern 3: Nice Sınıflandırma Sistemi

```
NICE SINIFLANDIRMASI – TEMEL YAPISI (11. Edisyon, 2024)

SINIFLAR 1-34: MAL SINIFLARI (ÜRÜNLER)
┌────────┬──────────────────────────────────────────┬──────────────────────────────────┐
│ Sınıf  │ Kapsam                                  │ Örnekler                          │
├────────┼──────────────────────────────────────────┼──────────────────────────────────┤
│ 1      │ Kimyasallar                             │ Endüstriyel kimyasallar, yapıştırıcı│
│ 3      │ Kozmetik, temizlik                       │ Şampuan, krem, parfüm, oje         │
│ 5      │ Eczacılık ürünleri                       │ İlaçlar, medikal plaster, besin    │
│ 9      │ Bilimsel/elektronik cihazlar             │ Yazılım, bilgisayar, telefon, CD   │
│ 14     │ Değerli metaller                        │ Takı, saat, mücevher              │
│ 16      │ Kağıt, basılı eserler                   │ Kitap, dergi, kırtasiye           │
│ 25      │ Giyim, ayakkabı                         │ Tişört, ayakkabı, şapka           │
│ 29      │ Gıda ürünleri (hayvansal/kaynaklı)     │ Et, süt ürünleri, konserve         │
│ 30      │ Gıda ürünleri (bitkisel/kaynaklı)      │ Un, ekmek, makarna, çikolata       │
│ 35      │ Reklam, iş yönetimi                     │ Perakende, franchising, pazarlama  │
│ 36      │ Finansal, sigorta                      │ Banka, sigorta, gayrimenkul        │
│ 37      │ İnşaat, onarım                         │ Bina yapımı, tamirat              │
│ 38      │ Telekomünikasyon                       │ İnternet, telefon, radyo          │
│ 41      │ Eğitim, eğlence                       │ Okul, spor, oyun, konser          │
│ 42      │ Bilim/teknoloji hizmetleri              │ Yazılım geliştirme, tasarım       │
│ 43      │ Yiyecek/içecek hizmetleri              │ Restoran, cafe, katering           │
│ 44      │ Tıbbi/hijyen hizmetleri                │ Hastane, eczane, veteriner         │
│ 45      │ Hukuki, güvenlik hizmetleri             │ Avukatlık, güvenlik danışmanlığı  │
└────────┴──────────────────────────────────────────┴──────────────────────────────────┘

SINIFLAR 35-45: HİZMET SINIFLARI
├── 35: Reklam, iş yönetimi, ofis işleri
├── 36: Sigortacılık, finans, gayrimenkul
├── 37: İnşaat, madencilik, onarım
├── 38: Telekomünikasyon
├── 39: Ulaşım, depolama, seyahat organizasyonu
├── 40: Malzeme işleme (üretim)
├── 41: Eğitim, eğlence, spor
├── 42: Bilim ve teknoloji hizmetleri, araştırma
├── 43: Yiyecek ve içecek hizmetleri, barınma
├── 44: Tıbbi/hijyen bakım, veterinerlik
└── 45: Hukuki, güvenlik hizmetleri, sosyal hizmetler

NICE SINIF SEÇİM STRATEJİSİ
├── Temel sınıf: Ana ürün/hizmet kategorisi
├── Koruma sınıfı: Rakip ürün/hizmetlerin bulunduğu sınıflar
├── Gelecek sınıfı: 5 yıllık iş planına göre olası genişleme sınıfları
└── Maliyet optimizasyonu: Her sınıf ayrı başvuru ücreti (TürkPatent 2024: ~850 TL/sınıf)
```

## Pattern 4: Benzerlik Analizi

```
BENZERLIK ANALİZİ MATRİSİ

3 BOYUTLU DEĞERLENDİRME:
├── [1] FONETİK BENZERLİK (Söyleniş)
│   ├── Tam benzer: "Kargo" vs "Kargo" → %100
│   ├── Yakın fonetik: "Kargo" vs "Kargo" (yazım farkı) → %70-80
│   ├── Kısmi benzer: "Kargo" vs "KarGOTur" → %50-60
│   └── Farklı fonetik: "Kargo" vs "Cargo" → %30-40
│
├── [2] GÖRSEL BENZERLİK (Yazım/Görüntü)
│   ├── Aynı harf dizisi: "Kargo" vs "Kargo" → %100
│   ├── Harf değişimi: "Kargo" vs "Kırgo" → %60-70
│   ├── Ek/eksiltme: "Kargo" vs "KargoX" → %70
│   ├── Görsel logo: Renk/şekil/font benzerliği ayrıca değerlendirilir
│   └── Farklı görsel: "Kargo" vs "Cargo" → %20-30
│
└── [3] KAVRAMSAL BENZERLİK (Anlam)
    ├── Aynı kavram: "Kargo" vs "Kargo" → %100
    ├── İlişkili kavram: "Kargo" vs "Nakliye" → %60
    ├── Benzer çağrışım: "Kargo" vs "Hızlı Teslimat" → %50
    └── Farklı kavram: "Kargo" vs "Banka" → %0-10

GENEL BENZERLİK SKORU = (Fonetik × 0.4) + (Görsel × 0.3) + (Kavramsal × 0.3)

┌────────────────┬───────────────────────────────────────────────────────────┐
│ Toplam Skor    │ Yorum ve Aksiyon                                            │
├────────────────┼───────────────────────────────────────────────────────────┤
│ %80-100        │ 🔴 Yüksek risk – Aynı sınıfta başvuru muhtemelen ret  │
│                │ edilir veya itiraz yükseltilir. Başvuru dan kaçınılmalı. │
├────────────────┼───────────────────────────────────────────────────────────┤
│ %50-79         │ 🟡 Orta risk – Başvuru kabul edilebilir ancak mevcut    │
│                │ marka sahibi itiraz edebilir. Farklılaştırma önerilir.   │
├────────────────┼───────────────────────────────────────────────────────────┤
│ %20-49         │ 🟢 Düşük risk – Başvuru kabul edilebilir görünüyor.     │
│                │ Yine de Nice sınıf örtüşmesi kontrol edilmelidir.        │
├────────────────┼───────────────────────────────────────────────────────────┤
│ %0-19          │ ✅ Minimal risk – Genel benzerlik yok.                     │
│                │ Başvuru için yeşil ışık.                                   │
└────────────────┴───────────────────────────────────────────────────────────┘
```

## Key Patterns (Özet)

| Adım | Eylem | Çıktı |
|---|---|---|
| 1 | Marka araştırma türü seçimi | Ön/tam/izleme/karşı araştırma |
| 2 | TürkPatent + EUIPO + WIPO sorgusu | Kayıtlı/bekleyen kayıt listesi |
| 3 | Nice sınıfı belirleme | Mal/hizmet sınıf listesi |
| 4 | Benzerlik analizi | 3 boyutlu skor (fonetik/görsel/kavramsal) |
| 5 | Risk değerlendirmesi | Düşük/orta/yüksek risk sınıflandırması |
| 6 | Başvuru stratejisi | Tek marka/marka portföyü önerisi |

## Anti-Patterns

```
❌ YALNIZCA TÜRKİYE'DE ARAMA
   Uluslararası markalar Türkiye'de tescil edilmiş olmasa da
   Madrid Protokolü ile 6 ay içinde koruma talep edebilir.
   → EUIPO ve WIPO veritabanlarını da tara.

❌ YALNIZCA TAM EŞLEŞMEYE BAKMA
   "Kargo" markası için "KarGo", "Kırgo", "Cargo" gibi
   benzer varyasyonlar da aynı korumayı ihlal eder.
   → Fonetik ve görsel benzerlikleri de araştır.

❌ SAYI BAZLI BENZERLİĞE GÜVENME
   Sayısal skor tek başına yeterli değildir.
   "Fonetic: %90, Gorsel: %20, Kavramsal: %10" → Toplam %48 (düşük görünebilir)
   Ancak fonetik %90 tek başına yeterli çakışma yaratabilir.
   → Her boyutu ayrı değerlendir.

❌ SİYAH-BEYAZ LOGO İLE BAŞVURUP RENKLİ İSTEME
   Başvuru sırasında siyah-beyaz tescil edilir, sonradan renk eklenemez.
   → Markanın nihai görsel formuyla başvuru yap.

❌ DÜŞÜK MALİYETLİ TEK SINIFLA KALMA
   İleride iş modeli değişince yeni sınıflarda başvuru yapılamayabilir.
   → 5 yıllık iş planına göre stratejik sınıf seçimi yap.

✅ DOĞRU YAPI
   Araştırma türü belirle → Kaynaklarda kapsamlı tarama →
   Nice sınıfı seç → Benzerlik analizi → Risk değerlendirmesi →
   Başvuru stratejisi → İzleme planı
```

## Quick Reference

| Görev | Kaynak | URL |
|---|---|---|
| Türkiye marka sorgusu | TürkPatent | search.trademarks.tpe.gov.tr |
| AB marka sorgusu | EUIPO | euipo.europa.eu/eSearch |
| Uluslararası marka | WIPO Madrid | branddb.wipo.int |
| ABD marka sorgusu | USPTO | tmsearch.uspto.gov |
| Patent sorgusu | TürkPatent | patents.tpe.gov.tr |
| Patent (uluslararası) | WIPO PATENTSCOPE | patentscope.wipo.int |
| Nice sınıf listesi | WIPO resmi | wipo.int/treaties/en/classification/nice |
| TürkPatent ücretler | TürkPatent web | tp.gov.tr/uecretler |
| Madrid Protokolü | WIPO Madrid | wipo.int/madrid |
| Marka izleme servisi | Trademarkwatch | trademarkwatch.com |

---

*Uyarı: Bu araştırma rehberi Fikri Mülkiyet alanında genel bilgilendirme amaçlıdır. Marka tescili veya patent başvurusu için mutlaka kalifiye patent vekilinden (marka vekili) profesyonel destek alınmalıdır.*


## 🌍 Universal Language Support
- **Turkish Native:** This skill natively supports Turkish. If the user prompt is in Turkish, all analysis, formatting, and output MUST be entirely in Turkish. You do not need explicit "write in Turkish" instructions.
