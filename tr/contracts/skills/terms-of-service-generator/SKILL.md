---
name: terms-of-service-generator
title: Terms of Service Generator
description: Kullanım şartları şablonu, sorumluluk sınırlaması, garanti hariç tutma ve fesih prosedürü.
author: mikailustuner
author_url: https://github.com/mikailustuner/OmniRule/tree/main/skills/terms-of-service-generator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: contracts
language: tr
---

# Terms of Service Generator

**Odağ Alanı:** Dijital platform, web sitesi, SaaS uygulaması ve mobil uygulama için kullanım şartları (Terms of Service / Terms & Conditions) şablonu hazırlama; sorumluluk sınırlaması, garanti hariç tutma, fesih prosedürü ve uyuşmazlık çözümü maddelerinin düzenlenmesi.

## Pattern 1: ToS Yapılandırma Rehberi

```
ZORUNLU BÖLÜMLER (Türkiye Yasal Gereklilikler)
├── 1. TARAFLAR VE KONU (Parties & Subject Matter)
│   ├── Satıcı/hizmet sağlayıcı bilgileri (unvan, adres, vergi no, iletişim)
│   ├── Müşteri/tüketici tanımı (gerçek kişi veya tüzel kişi)
│   ├── Sözleşmenin konusu ve kapsamı
│   └── Sürüm tarihi ve versiyon bilgisi
│
├── 2. HİZMET TANIMI VE KAPSAM (Description of Service)
│   ├── Sunulan hizmetin detaylı tanımı
│   ├── Hizmetin başlangıç ve bitiş koşulları
│   ├── Alt hizmet veya ek özellik tanımları
│   └── Hizmet dışı kalan unsurlar (dışlama listesi)
│
├── 3. KAYIT VE HESAP (Account Terms)
│   ├── Kayıt koşulları (yaş sınırı, gerçek bilgi yükümlülüğü)
│   ├── Hesap güvenliği (şifre sorumluluğu)
│   ├── Çoklu hesap yasağı
│   └── Hesabın askıya alınması/feshi koşulları
│
├── 4. ÖDEME VE FATURALAMA (Payment Terms)
│   ├── Ücretlendirme modeli (abonelik, kullanim bazlı, tek seferlik)
│   ├── Fiyat listesi ve güncelleme koşulları
│   ├── Ödeme yöntemleri ve para birimi
│   ├── Gecikme faizi ve temerrüt hükümleri
│   └── Otomatik yenileme ve iptal prosedürü
│
├── 5. FESİH VE İPTAL (Termination)
│   ├── Tarafların fesih hakları ( olağanüstü / olağan)
│   ├── Fesih bildirim süresi ve yöntemi
│   ├── Fesih sonrası veri işleme (silme / ihracat)
│   └── Hükümlerin fesh ötesi sürekliliği (devam eden hükümler)
│
├── 6. SORUMLULUK SINIRLAMASI (Limitation of Liability)
│   ├── Doğrudan zarar sınırlaması
│   ├── Dolaylı / dolaylı zararların hariç tutulması
│   ├── Maksimum sorumluluk tavanı
│   ├── Mücbir sebep tanımı ve etkileri
│   └── Zarar hesaplama yöntemi
│
├── 7. GARANTİ HARIÇ TUTMA (Warranty Disclaimer)
│   ├── Açık garanti yok (express warranty)
│   ├── Zımni garanti hariç tutma (implied warranty)
│   ├── "Service provided as-is" ifadesi
│   ├── Üçüncü taraf hizmetleri için garanti yok
│   └── Fit for particular purpose hariç tutma
│
├── 8. FİKRİ MÜLKİYET HAKLARI (Intellectual Property)
│   ├── Platform IP'si (marka, telif hakları, patent)
│   ├── Kullanıcı tarafından oluşturulan içerik (UGC)
│   ├── API ve veri kullanım hakları
│   └── Açık kaynak lisansları (üçüncü taraf bileşenler)
│
├── 9. GİZLİLİK VE VERİ (Privacy & Data)
│   ├── Veri toplama ve işleme kapsamı
│   ├── Cookie policy referansı
│   ├── Üçüncü taraf veri paylaşımı (3P hizmetler)
│   └── KVKK/GDPR uyumluluk referansı
│
├── 10. UYUŞMAZLIK ÇÖZÜMÜ (Dispute Resolution)
│   ├── Uygulanacak hukuk seçimi
│   ├── Yetkili mahkeme / tahkim kaydı
│   ├── Aracılık / uzlaştırma prosedürü
│   └── Toplu işlem yasağı (class action waiver)
│
└── 11. SON HÜKÜMLER
    ├── Sözleşme değişiklik prosedürü (bildirim + kabul)
    ├── Bölünebilirlik (severability)
    ├── Tam anlaşma (entire agreement)
    └── İhtar adresleri
```

## Pattern 2: Sorumluluk Sınırlaması Kalıbı

```
SORUMLULUK SINIRLAMASI – HUKUKİ ÇERÇEVE
├── TÜRKİYE'DEKİ YASAL SINIRLAR
│   ├── Türk Borçlar Kanunu m. 115 – Haksız şart yasağı
│   │   └── Tüketici sözleşmelerinde haksız şartlar geçersizdir
│   │   (TBK m. 25 – Mutlak butlan)
│   ├── 6502 Tüketicinin Korunması Hakkında Kanun
│   │   └── Yaniltici veya muğlak hükümler tüketici lehine yorumlanır
│   └── TMK m. 2 – İyiniyet kuralı (genel ilke)
│
└── HUKUKİ OLARAK KABUL EDİLEBİLİR SINIRLAMALAR
    ├── Kazanılmış haklar hariç tutulamaz
    ├── Ceza koşulu orantısız olamaz
    ├── Asgari özen yükümlülüğü kaldırılamaz
    ├── Kasıt ve ağır ihmal için sorumluluk sınırı konulamaz
    └── Can beden bütünlüğü zararları için sınır uygulanamaz

SORUMLULUK MATRİSİ ŞABLONU
┌───────────────────────────────┬───────────────────────┬────────────────────────┐
│ Zarar Türü                    │ Sorumluluk Durumu     │ Açıklama               │
├───────────────────────────────┼───────────────────────┼────────────────────────┤
│ Doğrudan maddi zarar          │ Sınırlanabilir        │ Makul tavan belirlenebilir │
├───────────────────────────────┼───────────────────────┼────────────────────────┤
│ Dolaylı (consequential) zarar │ Hariç tutulabilir     │ Kar kaybı, veri kaybı   │
├───────────────────────────────┼───────────────────────┼────────────────────────┤
│ Beklenen (anticipatory) zarar │ Hariç tutulabilir     │ Kâr kaybı, fırsat kaybı │
├───────────────────────────────┼───────────────────────┼────────────────────────┤
│ Casus bölge zararları         │ Hariç tutulabilir     │ Özel, arızi veya cezai   │
│                               │                       │ zararlar                 │
├───────────────────────────────┼───────────────────────┼────────────────────────┤
│ Kasıt                        │ SINIRLANAMAZ          │ Tam sorumluluk           │
├───────────────────────────────┼───────────────────────┼────────────────────────┤
│ Ağır ihmal                   │ SINIRLANAMAZ (TMK m.2)│ Asgari özen yükümlülüğü  │
├───────────────────────────────┼───────────────────────┼────────────────────────┤
│ Basit ihmal                  │ Sınırlanabilir        │ Hizmet bedeli ile sınırlı │
└───────────────────────────────┴───────────────────────┴────────────────────────┘
```

## Pattern 3: Garantilerin Hariç Tutulması

```
GARANTİ HARIÇ TUTMA MADDESİ (Warranty Disclaimer)
├── TEMEL UNSURLAR
│   ├── "HİZMETLER 'OLDUĞU GİBİ' (AS-IS) SUNULMAKTADIR"
│   ├── "SAĞLANMIŞTIR" altında hiçbir açık veya zımni garanti yoktur
│   ├── "BELİRLİ BİR AMACA UYGUNLUK" garantisi yoktur
│   └── "DEVamlılık" ve "HATASIZLIK" garantisi yoktur
│
├── EK GARANTİ HARIÇ TUTMALARI
│   ├── Üçüncü taraf içerik/hizmetleri (API, LinkedIn, Google Maps)
│   ├── Kullanıcı tarafından yüklenen verilerin doğruluğu
│   ├── Üçüncü taraf reklamları veya sponsorlu içerik
│   ├── İnternet bağlantısı ve alt yapı kesintileri
│   └── Force majeure olayları
│
└── ÖRNEK MADDE METNİ (Türkçe – Tüketici Uyumlu)
    "Hizmet Sağlayıcı, hizmetlerin hatasız, kesintisiz,
    güvenli veya belirli bir sonuç vereceğine dair hiçbir
    garanti vermemektedir. Hizmet Sağlayıcı, hizmetlerin
    belirli bir amaca uygunluğu ve mülkiyet garantisi dahil
    olmak üzere tüm zımni garantileri açıkça hariç tutar.
    Bu hariç tutma, tüketiciyi koruyan mevzuat hükümlerinin
    uygulanabileceği durumlarda geçerliliğini kaybeder."

NOT: Tüketici sözleşmelerinde TBK m. 25 kapsamında
"haksız şart" addedilebilecek garantisizlik hükümleri
mahkeme tarafından geçersiz sayılabilir. Dikkat!
```

## Pattern 4: Fesih Prosedürü ve Koşulları

```
FESİH TÜRLERİ VE KOŞULLARI
├── [A] OLAĞAN FESİH (Ordinary Termination)
│   ├── Satıcı tarafından: İşbu sözleşme, [X] gün önceden
│   │   yazılı bildirimle fesh edilebilir
│   ├── Müşteri tarafından: Hesap ayarlarından veya yazılı
│   │   bildirimle [X] gün önceden iptal
│   └── Otomatik yenileme: [X] gün önceden iptal edilmezse
│       otomatik yenileme (opt-out model)
│
├── [B] TAZARİ FESİH (Immediate Termination)
│   ├── Taraflardan biri, karşı tarafın aşağıdaki hallerden
│   │   herhangi birini gerçekleştirmesi halinde sözleşmeyi
│   │   derhal ve tazminatsız fesh edebilir:
│   │   (a) İşbu sözleşmeyi veya kanunu açıkça ihlal etmesi
│   │   (b) Mücbir sebep dışı 30 gün sürekli hizmet kesintisi
│   │   (c) iflas, konkordato veya ödeme aczi durumu
│   │   (d) Güveni suistimal, dolandırıcılık veya yasadışı faaliyet
│   │   (e) Hesabın üçüncü kişilerce yetkisiz kullanımı
│   │       (güvenlik ihlali durumunda)
│   └── Etki: Fesih anından itibaren tüm yükümlülükler sona erer
│
├── [C] İKİZ FESİH HAKKI (Termination for Convenience)
│   ├── Her iki taraf da herhangi bir gerekçe göstermeksizin
│   │   sözleşmeyi fesh edebilir
│   └── Koşul: [X] gün önceden yazılı bildirim
│
└── FESH SONRASI YÜKÜMLÜLÜKLER
    ├── Veri silme / ihracat (data portage): [X] gün içinde
    ├── Kullanılmayan avansların iadesi: [X] gün içinde
    ├── Fesih sonrası gizlilik yükümlülüğü: [X] yıl devam eder
    └── Devam eden hükümler: Fikri mülkiyet, garanti, sorumluluk
        sınırlaması, gizlilik hükümleri fesih sonrası da geçerlidir

FESİH İŞ AKIŞI
Tetikleyici olay
       ↓
[X] gün önceden bildirim (olağan fesih)
       ↓
Hesap/Hizmet askıya alma (isteğe bağlı)
       ↓
Fesih tarihi – hizmet kesimi
       ↓
Veri ihracatı (müşteriye [X] gün süre)
       ↓
Veri imhası (KVKK/GDPR m. 17)
       ↓
Fatura düzenleme / avans iadesi
       ↓
Fesih onayı + kayıt arşivleme
```

## Key Patterns (Özet)

| Bölüm | İçerik | Zorunluluk |
|---|---|---|
| 1 | Taraflar ve konu | ✅ Zorunlu |
| 2 | Hizmet tanımı | ✅ Zorunlu |
| 3 | Kayıt ve hesap | ✅ Zorunlu |
| 4 | Ödeme ve faturalama | ✅ Zorunlu |
| 5 | Fesih ve iptal | ✅ Zorunlu |
| 6 | Sorumluluk sınırlaması | ✅ Zorunlu |
| 7 | Garanti hariç tutma | ✅ Zorunlu |
| 8 | Fikri mülkiyet | ✅ Zorunlu |
| 9 | Gizlilik ve veri | ✅ Zorunlu |
| 10 | Uyuşmazlık çözümü | ✅ Zorunlu |
| 11 | Son hükümler | ✅ Zorunlu |

## Anti-Patterns

```
❌ "BİLDİRİMSİZ FESHİ" İZİN VEREN HÜKÜM
   Türk Borçlar Kanunu, ihbarsız feshi ancak mücbir sebep
   veya haklı nedenle kabul eder. Bildirimsiz fesih hükmü
   TBK m. 25 kapsamında haksız şart addedilebilir.
   → Minimum bildirim süresi belirle (14-30 gün önerilir).

❌ SORUMLULUK TAVANINI HİZMET BEDELİNİN 1 KATIYA İNDİRME
   Kasıt ve ağır ihmal durumlarında tavan uygulanamaz.
   Basit ihmal için bile 1 kat, hizmet bedelinin çok altında
   kalabilir ve müşteriye yetersiz koruma sağlar.
   → 3-12 aylık hizmet bedeli arasında makul tavan belirle.

❌ GARANTİ HARIÇ TUTMASINI MUTLAK YAPMA
   Tüketici Kanunu kapsamındaki sözleşmelerde kanuni
   garantiler (malın ayıpsız olması gibi) hariç tutulamaz.
   → "Kanuni haklar saklıdır" çekincesi ekle.

❌ FESİH SONRASI VERİ İŞLEMEYİ DÜZENLEMEME
   KVKK m. 7 uyarınca verilerin işlenmesi için ya rıza
   ya da hukuki sebep gerekir. Fesih sonrası veri saklama
   ayrıca düzenlenmemişse hukuka aykırı olabilir.
   → "Fesih sonrası [X] gün saklama" + "sonrası imha" hükmü ekle.

❌ TOPLU İŞLEM YASAĞINI KABUL ETTİRME
   Türkiye'de toplu işlem (class action) kurumu aktif değildir;
   ancak bu madde yanlış algılanabilir ve tüketici güvenini sarsar.
   → Bu madde Türkiye için opsiyoneldir; eklenirse açıkça belirtilmelidir.

✅ DOĞRU YAPI
   Zorunlu bölümleri tespit et → Sektöre uygun ekler ekle →
   Sorumluluk sınırlaması matrisini doldur → Garanti kalıbını
   yerleştir → Fesih prosedürünü detaylandır → KVKK uyum kontrolü →
   Tüketici mevzuatı uyumluluğu → Güncelleme prosedürü ekle
```

## Quick Reference

| Öğe | Standart Değer | Not |
|---|---|---|
| Olağan fesih bildirimi | 14-30 gün | Tek taraflı fesih için |
| Otomatik yenileme periyodu | Aylık / Yıllık | İptal süresi: 7-14 gün önce |
| Sorumluluk tavanı | 3-12 × aylık bedel | Kasıt/ağır ihmal hariç |
| Fesih sonrası veri ihracatı | 7-30 gün | KVKK m. 7 uyumlu |
| Fesih sonrası veri imhası | 30-90 gün | KVKK m. 17 |
| Garanti hariç tutma | "Olduğu gibi" (as-is) | + "belirli amaç" hariç tutma |
| Uygulanacak hukuk | Türk Hukuku | Tarafların açık seçimi |
| Yetkili mahkeme | Tüketici Hakem Heyeti / Tüketici Mahkemesi | TL eşik değerine göre |
| Değişiklik bildirimi | 15-30 gün önceden | Kullanıcının onay alması gerekir |
| Ulaşılabilirlik | support@domain.com + form | İletişim bilgisi zorunlu |

---

*Uyarı: Bu şablonlar genel rehberlik amaçlıdır. Dijital platform ToS taslağı için mutlaka teknoloji hukuku alanında uzmanlaşmış avukata danışılmalıdır. 6502 sayılı Tüketicinin Korunması Hakkında Kanun kapsamındaki zorunlu hükümler dikkate alınmalıdır.*


## 🌍 Universal Language Support
- **Turkish Native:** This skill natively supports Turkish. If the user prompt is in Turkish, all analysis, formatting, and output MUST be entirely in Turkish. You do not need explicit "write in Turkish" instructions.
