---
name: legal-translation-mikailustuner
title: Legal Translation
description: Hukuki çeviri, terminoloji doğruluğu, yeminli tercüme standartları ve Apostil işlemleri.
author: mikailustuner
author_url: https://github.com/mikailustuner/OmniRule/tree/main/skills/legal-translation
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: tr
---

# Legal Translation

**Odağ Alanı:** Hukuki dokümanların (sözleşmeler, mahkeme kararları, ticari belgeler, kimlik fotokopileri) Türkçe ↔ İngilizce ↔ Almanca ↔ Fransızca arasında doğru terminolojiyle çevirisi; yeminli tercüme standartları; Apostil ve tasdik işlemleri rehberliği.

## Pattern 1: Hukuki Çeviri Türleri ve Gereklilikler

```
1. ÇEVİRİ TİPİNE GÖRE GEREKLİLİKLER
├── YEMİNLİ TERCÜME (Sworn/Authorized Translation)
│   ├── Kim yapabilir: Yeminli tercüman ( noter onaylı )
│   ├── Kullanım: Yabancılıkla ilgili işlemler
│   │   (vize, oturma izni, şirket kuruluşu, dava dosyası)
│   ├── Şerh: "İşbu tercüme, aslının aynıdır" kaşesi + imza
│   ├── Hukuki geçerlilik: Noter onayı gerekli
│   ├── Önemli: Yargıtay, konsolosluk ve noterlikler
│   │   yeminli tercüman onaylı çeviri ister
│   └── Maliyet: Sayfa başına (2024: ortalama 100-250 TL/sayfa)
│
├── RESMİ ÇEVİRİ (Official Translation)
│   ├── Kim yapabilir: noter onaylı tercüman
│   ├── Kullanım: Şirket belgeleri, ticari sözleşmeler
│   ├── Şerh: Noter onayı gerekli
│   └── Hukuki geçerlilik: Noter onayı ile sağlanır
│
├── PROFESYONEL HUKUKİ ÇEVİRİ (Professional Legal Translation)
│   ├── Kim yapabilir: Hukuk alanında uzman çevirmen
│   ├── Kullanım: Due diligence, yatırımcı belgeleri,
│   │   hukuki danışmanlık amaçlı (resmi işlem dışı)
│   ├── Şerh: Yok (çeviri doğrudan kullanılamaz)
│   └── Hukuki geçerlilik: Resmi işlemde kullanılamaz
│
└── ORYANTAL / TEKNİK ÇEVİRİ (Technical Translation)
    ├── Kim yapabilir: Alan uzmanı (mühendis, doktor vb.)
    ├── Kullanım: Patent tercümesi, tıbbi raporlar
    ├── Şerh: Alan uzmanı imzası gerekebilir
    └── Hukuki geçerlilik: Kullanım amacına bağlı

2. TÜRKİYE'DE YEMİNLİ TERCÜMANLIK SİSTEMİ
├── Adalet Bakanlığı onaylı tercümanlar
│   └── Noterler Listesi'nde kayıtlı tercümanlar
├── Çevirmen Kayıt Sistemi (CKS) – e-Devlet üzerinden sorgulama
├── Her ilde noter onaylı tercüman listesi mevcut
└── İstanbul Barosu tercüman listesi: istanbulbarosu.org.tr
```

## Pattern 2: Hukuki Terminoloji Çeviri Rehberi

```
TEMEL HUKUKİ TERİM ÇEVİRİ MATRİSİ (TR → EN)
┌────────────────────────────────┬────────────────────────────────┬──────────────────────────────────┐
│ Türkçe Terim                    │ İngilizce Karşılığı             │ Açıklama                          │
├────────────────────────────────┼────────────────────────────────┼──────────────────────────────────┤
│ İfa                            │ Performance                    │ Borcun yerine getirilmesi         │
│ Mücbir sebep                   │ Force majeure                  │ Olağanüstü durum                   │
│ Borçlar Kanunu                 │ Code of Obligations            │ 6098 sayılı TBK                   │
│ Türk Ticaret Kanunu            │ Turkish Commercial Code        │ 6102 sayılı TTK                   │
│ Haksız fiil                    │ Tort / Unlawful act            │ Hukuka aykırı zarar verme          │
│ Sebepsiz zenginleşme           │ Unjust enrichment              │ Haksız kazanç                       │
│ Muvazaa                        │ Sham transaction / Simulation   │ Gerçek iradeyi gizleme            │
│ Muaccel                        │ Due and payable                │ Vadesi gelmiş, ödenmesi gereken   │
│ Müeccel                        │ Not yet due                    │ Vadesi gelmemiş                    │
│ Ceza şartı                     │ Penalty clause                 │ Sözleşme cezası                   │
│ Mütemerrit                     │ Defaulting party               │ Borcunu ödemeyen taraf            │
│ Talik                          │ Suspension                      │ Bir süre erteleme                  │
│ Terkin                         │ Deletion / Cancellation        │ Kayıttan silme                    │
│ İşlemiş faiz                   │ Accrued interest              │ Hesaplanmış faiz                   │
│ İradi                           │ Voluntary                      │ İsteğe bağlı                      │
│ Def'i                          │ Defense                        │ Davalının itiraz hakkı            │
│ Fer'i müdahale                 │ Intervention                   │ Davaya katılma                     │
│ Kıymetli evrak                 │ Negotiable instruments         │ Çek, bono, poliçe                  │
│ Kambiyo senetleri              │ Commercial papers             │ Para yerine geçen belgeler         │
│ Vekaletname                    │ Power of attorney              │ Yetki belgesi                      │
│ Yetki belgesi                   │ Certificate of authority      │ Şirket yetkilisi belgesi          │
│ Müddeti bilirkişi               │ Court-appointed expert        │ Mahkeme tarafından atanan uzman   │
│ Keşif                           │ Site inspection                │ Yerinde inceleme                   │
│ Tensip                           │ Decision / Ruling             │ Mahkeme kararı                    │
│ Tevhid-i ihtilaf               │ Consolidation of disputes     │ Birden fazla davanın birleştirilmesi│
│ Tenfiz                           │ Enforcement of judgment       │ Mahkeme kararının icrası           │
│ Nafaka                          │ Alimony / Maintenance          │ Düzenli ödeme yükümlülüğü         │
│ Tenzil                           │ Reduction / Decrease          │ İndirim                           │
│ İlâm                            │ Certified copy of judgment    │ Mahkeme kararının onaylı sureti   │
└────────────────────────────────┴────────────────────────────────┴──────────────────────────────────┘

YARGI KURULUŞU ÇEVİRİLERİ
┌──────────────────────┬─────────────────────────────┬──────────────────────────────────┐
│ Türk Kurum            │ İngilizce Karşılığı          │ Kısaltma                        │
├──────────────────────┼─────────────────────────────┼──────────────────────────────────┤
│ Yargıtay             │ Court of Cassation           │ Yarg.                           │
│ Danıştay             │ Council of State             │ D-                              │
│ Anayasa Mahkemesi    │ Constitutional Court          │ AYM                             │
│ Bölge Adliye Mah.    │ Regional Court of Appeal     │ BAM                             │
│ Asliye Hukuk Mah.    │ Court of First Instance      │ AHM                             │
│ Asliye Ticaret Mah.  │ Commercial Court             │ ATM                             │
│ İcra Mahkemesi       │ Enforcement Court           │ iM                              │
│ Sulh Hukuk Mahkemesi │ Magistrate Court             │ SHM                             │
│ Tüketici Hakem Heyeti │ Consumer Arbitration Board  │ THH                             │
│ Noter                │ Notary Public                │                                 │
│ Baro                │ Bar Association               │                                 │
└──────────────────────┴─────────────────────────────┴──────────────────────────────────┘
```

## Pattern 3: Sözleşme Çeviri Standartları

```
SÖZLEŞME ÇEVİRİ KURALLARI
├── GENEL İLKELER
│   ├── Resmiyet derecesine uygun dil stili kullan
│   ├── Kısaltmalar ilk kullanımda açık olarak yazılmalı
│   │   └── "Yargıtay (Yargıtay), 11. Hukuk Dairesi (11. HD)"
│   ├── Para birimleri açık yazılmalı (USD – ABD Doları)
│   ├── Tarihler: Gün.Ay.Yıl formatında (15.04.2025)
│   └── Sayılar: Hem rakam hem yazıyla (TL 1.000.000 / Bir milyon Türk Lirası)
│
├── MADDE ÇEVİRİSİ STANDART FORMAT
│   │
│   ARTICLE 5 – CONFIDENTIALITY
│   │
│   ├── Madde başlığı: Büyük harf + bold
│   │   └── ARTICLE 5 – GİZLİLİK
│   │
│   ├── Numara: Arap rakamı (5.) – Türkçe'de de Arap rakamı kullanılabilir
│   │
│   ├── Alt bentler: (a), (b), (c) veya (i), (ii), (iii)
│   │   └── (a) The Receiving Party shall...
│   │       (b) Confidential Information includes...
│   │
│   └── Atıflar: "Article 3(2)" → "Madde 3(fıkra 2)"
│       "Section 1.2" → "Bölüm 1.2"
│
├── MADDE NUMARALANDIRMA UYUMSUZLUĞU
│   ├── Türkçe: MADDE 5 / madde 5 / md. 5
│   ├── İngilizce: ARTICLE 5 / Section 5 / Clause 5 / Article 5
│   └── Not: Çeviride tutarlılık şart; kaynak metindeki numaralama korunmalı
│
├── KELİME SEVİYESİ HASSASİYET
│   ├── "shall" = "yükümlüdür" / "gerekir" (zorunluluk)
│   ├── "may" = "yetkilidir" / "izindir" ( izin)
│   ├── "must" = "zorundadır" (mutlak gereklilik)
│   ├── "will" = "edecektir" (gelecek zaman, taahhüt)
│   ├── "should" = "olmalıdır" ( tavsiye)
│   └── "may not" = "yetkili değildir" ( yasak)
│
└── UYUŞMAZLIK ÇÖZÜM ÇEVİRİLERİ
    ├── "Arbitration" = "Tahkim" ( ICC, ISTAC, UNCITRAL Kuralları)
    ├── "Litigation" = "Mücadelе / Mahkeme yargılaması"
    ├── "Mediation" = "Arabuluculuk"
    ├── "Governing Law" = "Uygulanacak Hukuk"
    └── "Jurisdiction" = "Yargı Yetkisi / Mhkeme Yetkisi"
```

## Pattern 4: Apostil Süreci ve Belge Türleri

```
APOSTİL SÜRECİ – ADIM ADIM REHBER

1. APOSTİL NEDİR?
├── 1961 Lahey Apostil Sözleşmesi
├── Yabancı ülkede kullanılacak belgelerin tasdiki
├── "Lahey Apostil" = Belgenin orijinal olduğunun resmi onayı
└── Hedef ülke Apostil Sözleşmesi'ne taraf olmalı

2. TÜRKİYE'DEKİ APOSTİL YETKİLİ KURUMLAR
┌──────────────────────┬──────────────────────────────────────────────────┐
│ Belge Türü           │ Apostil Yetkili Kurumu                           │
├──────────────────────┼──────────────────────────────────────────────────┤
│ Adli belgeler         │ Cumhuriyet başsavcılıkları (Asliye / Sulh)       │
│ (mahkeme kararları,   │                                                   │
│  ifade tutanakları)   │                                                   │
├──────────────────────┼──────────────────────────────────────────────────┤
│ Resmi belgeler        │ Valilikler / Kaymakamlıklar                     │
│ (nüfus kayıt örneği,  │                                                   │
│  diploma, sertifika)  │                                                   │
├──────────────────────┼──────────────────────────────────────────────────┤
│ Ticari belgeler       │ Türkiye Ticaret Odaları Birliği (TTO)           │
│ (sicil kaydı,         │                                                   │
│  faaliyet belgesi)    │                                                   │
├──────────────────────┼──────────────────────────────────────────────────┤
│ Noter onaylı belgeler │ Noterlikler                                      │
│                       │                                                   │
├──────────────────────┼──────────────────────────────────────────────────┤
│ Yeminli tercüme       │ Önce noter onayı → sonra Apostil (eğer hedef    │
│                       │ ülke gerektiriyorsa)                             │
└──────────────────────┴──────────────────────────────────────────────────┘

3. APOSTİL SÜRECİ (Adım Adım)
├── ADIM 1: Belge temini
│   └── Gerekli belge (orijinal veya noter onaylı suret)
│
├── ADIM 2: Apostil başvurusu
│   └── İlgili kuruma başvuru (fizik veya e-Başvuru)
│
├── ADIM 3: Apostil tasdiki
│   └── Kurum, belgenin orijinal olduğunu Apostil ile tasdik eder
│
├── ADIM 4: tercüme (gerekirse)
│   └── Hedef ülke dilinde yeminli tercüme
│
└── ADIM 5: Konsolosluk vizesi (opsiyonel)
    └── Bazı ülkeler apostil'e ek olarak konsolosluk vizesi ister

4. APOSTİL GEREKTİREN BELGE TÜRLERİ MATRİSİ
┌──────────────────────┬─────────────────┬──────────────┬──────────────────┐
│ Belge                │ Apostil Gerekli │ Tercüme     │ Konsolosluk Vizesi│
├──────────────────────┼─────────────────┼──────────────┼──────────────────┤
│ Doğum/kimlik belgesi │ ✅ Evet         │ ✅ Evet      │ Ülkeye göre      │
├──────────────────────┼─────────────────┼──────────────┼──────────────────┤
│ Evlilik cüzdanı     │ ✅ Evet         │ ✅ Evet      │ Ülkeye göre      │
├──────────────────────┼─────────────────┼──────────────┼──────────────────┤
│ Diploma              │ ✅ Evet         │ ✅ Evet      │ Eğitim vizesi ise │
├──────────────────────┼─────────────────┼──────────────┼──────────────────┤
│ Mahkeme kararı       │ ✅ Evet         │ ✅ Evet      │ Genellikle hayır   │
├──────────────────────┼─────────────────┼──────────────┼──────────────────┤
│ Ticari şirket belgesi│ ✅ Evet         │ ✅ Evet      │ İş vizesi ise     │
├──────────────────────┼─────────────────┼──────────────┼──────────────────┤
│ Yeminli tercüme      │ Noter onayına bağlı │ —        │ Ülkeye göre      │
└──────────────────────┴─────────────────┴──────────────┴──────────────────┘
```

## Key Patterns (Özet)

| Görev | Standart | Dikkat |
|---|---|---|
| Yeminli tercüme | Noter onaylı + ıslak imza | Her sayfada ayrı onay gerekli |
| Para birimi | Hem rakam hem yazıyla | "TL 500.000 / Beşyüz Bin Türk Lirası" |
| Tarih formatı | Gün.Ay.Yıl | "15.04.2025" |
| "Shall" çevirisi | "yükümlüdür" / "gerekir" | Zorunluluk ifade eder |
| "May" çevirisi | "yetkilidir" / "izindir" | İzin ifade eder |
| Para birimi dönüşümü | Resmi kur kuru kullan | Çeviri tarihindeki kur belirtilmeli |
| Apostil | Lahey Sözleşmesi | Hedef ülke taraf olmalı |
| Apostil + tercüme | Önce tercüme, sonra Apostil | Sıralama önemli |
| Kurum isimleri | Resmi İngilizce çevirileri kullan | Çeviri kaynaklarında kontrol et |
| Sayfa numaralama | "Sayfa X / Y" formatı | Toplam sayfa belirtilmeli |

## Anti-Patterns

```
❌ GOOGLE TRANSLATE VEYA OTOMATİK ÇEVİRİYE GÜVENME
   Hukuki belgelerde anlam kayması kritik sonuçlar doğurabilir.
   "Müeccel" ile "muaccel" karıştırılırsa yükümlülükler değişir.
   → Mutlaka insan tercüman ve terminoloji kontrolü kullan.

❌ YEMİNLİ TERCÜMAN OLMADAN RESMİ İŞLEM YAPTIRMA
   Konsolosluk, noter veya yargı organları yeminli tercüman
   onayı olmadan çeviri kabul etmez.
   → Resmi işlem için noter onaylı çeviri şart.

❌ APOSTİLİN YETERLİ OLDUĞUNU DÜŞÜNME
   Bazı ülkeler apostil'e ek olarak konsolosluk vizesi ister.
   → Hedef ülkenin Lahey Apostil Sözleşmesi'ne taraf olup olmadığını
      kontrol et + konsolosluk gerekliliklerini araştır.

❌ KURUM İSİMLERİNİ ÇEVİRMEDEN BIRAKMA
   "Yargıtay" → "Yargitay" veya "Yargi-tay" yazılırsa anlaşılmaz.
   → Resmi İngilizce çevirileri kullan: "Court of Cassation"

❌ SÖZLEŞME ÇEVİRİSİNDE NUMARALANDIRMA BOZULMASI
   Kaynak metindeki "madde" → "article" dönüşümünde tutarsızlık
   sonraki atıfların çalışmamasına yol açar.
   → Kaynak metin numaralama formatını koru + tutarlılık kontrolü yap.

✅ DOĞRU YAPI
   Belge türü tespit → Gereken tercüme türü belirle →
   Terminoloji listesi hazırla → Çeviri yap →
   Hukuki kontrol (terim doğruluğu) → Sayfa düzeni →
   Yeminli tercüman onayı (gerekirse) → Apostil (gerekirse)
```

## Quick Reference

| Görev | Kaynak | Not |
|---|---|---|
| Yeminli tercüman bulma | Türkiye Noterler Birliği | noterlerbirlik.org.tr |
| Yeminli tercüman sorgulama | e-Devlet / CKS | CeBIS kayıt sistemi |
| Apostil başvurusu | Valilikler / Başsavcılıklar | Fiziksel veya e-Başvuru |
| Apostil sorgulama | Lahey Konferansı | hcch.net |
| Apostil taraf ülkeleri | Lahey Apostil Atlası | hcch.net/tools/apostille |
| Ticari belge Apostil | TTO (Ticaret Odaları) | tobb.org.tr |
| Hukuki terminoloji | UYAP sözlük / EU lexicon | Resmi terimler |
| Konsolosluk gereklilikleri | Konsolosluk.gov.tr | Ülke bazlı bilgi |
| Çeviri fiyatları (2024) | Noter ücret tarifesi | Sayfa başına ortalama |
| Apostil ücreti | Kurumdan kuruma değişir | 2024: 150-500 TL |

---

*Uyarı: Bu rehber hukuki çeviri süreçlerinde genel bilgilendirme amaçlıdır. Resmi işlemlerde her zaman yetkili kurumların güncel gerekliliklerini kontrol edin. Hukuki belgelerin çevirisi için her zaman profesyonel ve yeminli tercüman ile çalışılmalıdır.*


## 🌍 Universal Language Support
- **Turkish Native:** This skill natively supports Turkish. If the user prompt is in Turkish, all analysis, formatting, and output MUST be entirely in Turkish. You do not need explicit "write in Turkish" instructions.
