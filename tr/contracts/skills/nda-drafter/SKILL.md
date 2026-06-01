---
name: nda-drafter
title: NDA Drafter
description: Gizlilik sözleşmesi şablonları, ticari sır tanımı, süre ve cezai şartlar, üçüncü taraf clausing.
author: mikailustuner
author_url: https://github.com/mikailustuner/OmniRule/tree/main/skills/nda-drafter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: contracts
language: tr
---

# NDA Drafter

**Odağ Alanı:** Tek taraflı ve karşılıklı gizlilik sözleşmeleri (NDA/Mutabakat) taslak hazırlama, ticari sır tanımı kapsamlandırma, süre ve cezai şart belirleme, üçüncü taraf istisnaları düzenleme.

## Pattern 1: NDA Tipolojisi ve Seçim Kararı

```
1. NDA TİPİ SEÇİM AĞACI
├── TEK TARAFLI NDA (Unilateral NDA)
│   ├── Kim kullanır: Bilgi veren taraf (Disclosure)
│   ├── Kullanım senaryosu: Yatırımcı sunumu, iş görüşmesi,
│   │   tedarikçi değerlendirmesi, potansiyel satın alma
│   ├── Avantaj: Tek tarafa yükümlülük, basit süreç
│   └── Risk: Bilgi alan tarafın motivasyonu düşük
│
├── KARŞILIKLI NDA (Mutual/Bilateral NDA)
│   ├── Kim kullanır: Her iki taraf da bilgi paylaşır
│   ├── Kullanım senaryosu: Ortaklık müzakeresi, JV görüşmeleri,
│   │   lisanslama, R&D işbirliği, due diligence
│   ├── Avantaj: Simetrik koruma, karşılıklı bağlılık
│   └── Risk: Karmaşık müzakere, her iki taraf da taahhüt altında
│
├── ÇOK TARAFLI NDA (Multilateral NDA)
│   ├── Kim kullanır: 3+ taraf arasında bilgi paylaşımı
│   ├── Kullanım senaryosu: Konsorsiyum, platform katılımcıları
│   │   tedarikçi ağı, akreditasyon süreçleri
│   └── Risk: Zincirleme sorumluluk, boşluk riski
│
└── EMPLOYER NDA (Çalışan Gizlilik Sözleşmesi)
    ├── Kim kullanır: İşveren
    ├── Kullanım senaryosu: İşe girişte, görev değişikliğinde
    │   iş sözleşmesinin eki olarak
    └── Yasal özellik: İş hukuku kapsamında işçi koruması

2. HUKUKİ REJİM SEÇİMİ
├── Türk Hukuku (TBK m. 161-171 – Hapis sözleşmesi analog)
│   ├── Uygulanacak hükümler: TBK Genel Hükümler
│   ├── Yaptırım: Tazminat + manevi tatmin
│   └── İspat yükü: Gizli bilgiyi alan tarafta
│
├── İngiliz Hukuku (English law – common law NDA)
│   ├── Avantaj: Olgun içtihat, hızlı uygulama
│   └── Dikkat: English courts enforce "trade secrets" strictly
│
└── Seçim hukuku (Governing Law)
    └── Tarafların açıkça belirlediği hukuk sisteminin
        uygulanması esastır; aksi halde ilgili mahkeme
        kendi hukukunu uygular.
```

## Pattern 2: Ticari Sır Tanımı ve Kapsam

```
TİCARİ SIR TANIMLAMA STRATEJİSİ
├── KAPSAYICI TANIM (Geniş Koruma)
│   └── "Gizli bilgi, taraflardan birinin veya bağlı şirketlerinin
│       ticari faaliyetleri sırasında edinilen, üçüncü kişilere
│       açıklanmamış, ekonomik değeri olan her türlü bilgi, belge,
│       veri, taslak, proje, know-how, formül, müşteri listesi,
│       fiyat politikası, strateji, yazılım kaynak kodu ve
│       pazar araştırması verilerini kapsar."
│   ├── Avantaj: Geniş koruma alanı
│   └── Risk: Mahkeme tarafından aşırı geniş bulunabilir
│
├── SINIRLI TANIM (Somut Koruma)
│   └── "Gizli bilgi, bu sözleşmenin Ek-A'sında listelenen
│       belgelerde açıkça 'GİZLİ' olarak işaretlenen bilgileri
│       ve aşağıdaki kategorilere giren bilgileri kapsar:
│       (a) Mali tablolar ve projeksiyonlar
│       (b) Müşteri ve tedarikçi ilişkileri
│       (c) Patent başvurusu yapılmamış teknik çözümler
│       (d) İş süreçleri ve operasyonel prosedürler"
│   ├── Avantaj: Net kapsam, ispat kolaylığı
│   └── Risk: Listede olmayan bilgiler korumasız kalır
│
└── HİBRİT TANIM (ÖNERİLEN)
    ├── Genel çerçeve + somut örnekler + istisnalar
    ├── "Gizli bilgi tanımı" + "Gizli bilgi olmayan bilgiler" listesi
    └── Üç katmanlı test (aşağıya bakınız)

ÜÇ KATMANLI TİCARİ SIR TESTİ (TRADE SECRET TRIAGE)
┌──────────────────────────────────────────────────────────────┐
│ 1. KATMAN: GİZLİLİK NİTELİĞİ                                   │
│    • Bilgi kamuya açık mı? (Patent, akademik yayın, web)        │
│    • Bilgi çalışanlar arasında sınırlı erişimli mi?              │
│    • "Gizli" veya "Özel" işaretlemesi var mı?                   │
│    → Tüm sorular EVET ise → Ticari sır niteliği güçlü           │
│                                                              │
│ 2. KATMAN: EKONOMİK DEĞER                                       │
│    • Bilgi rekabet avantajı sağlıyor mu?                        │
│    • Bilgi olmaksızın iş yapmak zorlaşıyor mu?                  │
│    • Bilginin edinilmesi için kaynak/ çaba harcanmış mı?         │
│    → Tüm sorular EVET ise → Ekonomik değer mevcut               │
│                                                              │
│ 3. KATMAN: KORUMA TEDBİRİ                                        │
│    • Erişim kontrolü (password, fiziksel güvenlik)?             │
│    • NDAlar imzalanmış mı?                                     │
│    • Çalışanlara gizlilik eğitimi verilmiş mi?                  │
│    → Tüm sorular EVET ise → Koruma tedbiri yeterli              │
└──────────────────────────────────────────────────────────────┘

Üç katmanlı testi geçen bilgi → Ticari sır olarak korunabilir
```

## Pattern 3: Süre, Kapsam ve Cezai Şartlar

```
SÜRE BELİRLEME STRATEJİSİ
┌────────────────────────┬─────────────────┬────────────────────────────┐
│ Bilgi Türü             │ Önerilen Süre   │ Gerekçe                    │
├────────────────────────┼─────────────────┼────────────────────────────┤
│ Genel ticari bilgi     │ 2-3 yıl         │ Rekabet avantajinin süresi │
│ Müşteri listesi        │ 3-5 yıl         │ Müşteri bağımlılık süresi  │
│ Teknik know-how        │ 5 yıl - süresiz  │ Teknoloji ömrü + patent    │
│ Formül/recete          │ Süresiz         │ Sürekli ekonomik değer     │
│ Mali veriler           │ 3 yıl           │ Vergi denetim süresi        │
│ Personel bilgileri     │ İş ilişkisi +2yıl│ İş sözleşmesi sonrası taahhüt│
└────────────────────────┴─────────────────┴────────────────────────────┘

COĞRAFI KAPSAM (Coğrafi Scope)
├── Türkiye: Yalnızca Türkiye sınırları içinde koruma
├── Avrupa: AB üye devletleri + EEA
├── Global: Tüm ülkeler (en geniş, en zor uygulanabilir)
└── Hedef pazar: Belirli ülkeler listesi

CEZAİ ŞART MATRİSİ
┌───────────────────────┬──────────────────────┬────────────────────────┐
│ İhlal Türü           │ Önerilen Ceza        │ Uygulama Notu           │
├───────────────────────┼──────────────────────┼────────────────────────┤
│ Kasıtlı ifşa          │ 3× sözleşme bedeli   │ Kasti ihlal, ağır ihmal│
│                        │ veya sabit tutar     │                        │
├───────────────────────┼──────────────────────┼────────────────────────┤
│ İhmalden kaynaklanan  │ Gerçek zarar +       │ Basit ihmal, dikkat     │
│ ifşa                  │ olağan kazancın iades│ dikkatsizlik           │
├───────────────────────┼──────────────────────┼────────────────────────┤
│ Üçüncü taraf sızıntısı │ İhlal Eden tarafın   │ Bilgi alan taraf,       │
│                        │ tam sorumluluğu      │ üçüncü taraftan önce    │
│                        │                      │ sorumludur              │
└───────────────────────┴──────────────────────┴────────────────────────┘
```

## Pattern 4: Üçüncü Taraf İstisna Mekanizması

```
ÜÇÜNCÜ TARAF ISTISNALARI (Third-Party Exceptions)
├── İZİNSİZ AÇIKLAMA YASAĞI
│   └── "Taraflardan hiçbiri, karşı tarafın açık yazılı izni
│       olmaksızın, gizli bilgileri üçüncü taraflara doğrudan
│       veya dolaylı olarak açıklamayacaktır."
│
├── YASAL ZORUNLULUK İSTİSNASI
│   └── "Bu sözleşme kapsamındaki gizlilik yükümlülükleri,
│       yasal veya düzenleyici bir zorunluluktan kaynaklanan
│       ifşalar için geçerli değildir. Bu durumda, ifşa
│       yapmadan önce karşı tarafa yazılı bildirim yapılacak
│       ve mümkünse yasal olarak izin verilen ölçüde
│       gizlilik korunacaktır."
│
├── NİHAİ ALICI İSTİSNASI (Corporate Transaction)
│   └── "Bir taraf, birleşme, devir, satın alma veya iflas
│       durumlarında gizli bilgileri devir alan tarafa
│       aktarabilir. Bu aktarım, devralan tarafın da aynı
│       gizlilik yükümlülüklerine tabi olacağını taahhüt
│       etmesi koşuluna bağlıdır."
│
├── YETERLİ KORUMA ALTINDA TUTULAN BİLGİLER
│   └── "Karşı tarafa ifşa edilmeden önce, aşağıdaki
│       koşulların sağlandığı bilgiler gizli bilgi
│       kapsamından çıkarılır:
│       (a) Karşı tarafa ifşa edilmeden önce kamuya açık
│           hale gelmiş veya olmuş
│       (b) Karşı tarafa ifşa edilmeden önce, ifşa eden
│           tarafa herhangi bir gizlilik yükümlülüğü
│           olmaksızın meşru olarak biliniyordu
│       (c) Karşı tarafa ifşa edilmeden önce veya sonra
│           karşı tarafın kendi çabalarıyla, herhangi
│           bir gizlilik yükümlülüğünü ihlal etmeden
│           geliştirilmiştir
│       (d) Karşı taraftan bağımsız olarak geliştirilmiştir
│           ve gizli bilgi kullanılmamıştır"
│
└── KİŞİSEL VERİ İSTİSNASI (KVKK/GDPR uyumlu)
    └── "Bu sözleşme, kişisel verilerin işlenmesini
        düzenlemez. Kişisel veriler, ilgili veri koruma
        mevzuatına tabidir ve ayrı bir Veri İşleme
        Anlaşması (DPA) ile düzenlenecektir."
```

## Key Patterns (Özet)

| Adım | Eylem | Çıktı |
|---|---|---|
| 1 | NDA tipi seçimi | Tek taraflı / Karşılıklı / Çok taraflı |
| 2 | Ticari sır tanımı | Hibrit tanım + istisna listesi |
| 3 | Süre ve coğrafi kapsam | Süre tablosu + kapsam tanımı |
| 4 | Cezai şart belirleme | Ceza matrisi + tazminat koşulları |
| 5 | Üçüncü taraf istisnaları | İstisna maddeleri seti |
| 6 | Uygulama hükümleri | Federasyon yetkisi / Tahkim kaydı |

## Anti-Patterns

```
❌ "HER TÜRLÜ BİLGİ GİZLİDİR" GİBİ GENİŞ TANIM
   Mahkemeler bu tip tanımları "belirsiz" bularak sözleşmeyi
   kısmi geçersiz sayabilir. Tanım somutlaştırılmalıdır.
   → "Gizli Bilgi" tanımına somut örnekler ve istisnalar ekle.

❌ SÜRESİZ GİZLİLİK YÜKÜMLÜLÜĞÜ
   Süresiz yükümlülük İngiliz hukukunda kısmen geçersiz kabul edilir.
   Belirli bilgi kategorileri için makul süre belirle.
   → Her bilgi kategorisi için ayrı süre belirle.

❌ CEZAİ ŞARTI BELİRSİZ BIRAKMA
   "Ciddi tazminat" gibi bir ifade ispat zorluğu yaratır.
   → Net sayısal tutar veya hesaplama formülü belirle.

❌ ÜÇÜNCÜ TARAF İSTİSNASINI YAZILI İZİNE BAĞLAMAMA
   Sözlü onay ispatlanamaz.
   → Tüm istisna talepleri yazılı ve tarihli olmalı.

❌ KİŞİSEL VERİLERİ AYRI DÜZENLEMEME
   NDA'lar kişisel veri işleme için uygun sözleşme türü değildir.
   → KVKK/GDPR uyumlu ayrı bir DPA (Veri İşleme Anlaşması) ekle.

✅ DOĞRU YAPI
   NDA tipi seç → Ticari sır tanımı (hibrit) → Kapsam belirle →
   Süre/kapsam/cza matrisini oluştur → İstisnaları düzenle →
   Uygulama hükümleri ekle → KVKK uyumluluk kontrolü
```

## Quick Reference

| Öğe | Standart Değer | Açıklama |
|---|---|---|
| NDA tipi | Karşılıklı (bilateral) | Her iki taraf da bilgi paylaşacaksa |
| Süre – genel | 2-3 yıl | Standart ticari bilgiler |
| Süre – know-how | 5 yıl - süresiz | Teknik bilgiler |
| Coğrafi kapsam | Türkiye + hedef pazar | Ticari hedeflerle sınırlı tut |
| Cezai şart | 3× sözleşme bedeli | Kasıtlı ihlal durumunda |
| İstisna – yasal | Yazılı bildirim + mümkünse gizlilik koruma | Zorunlu ifşa öncesi bildirim |
| İstisna – üçüncü taraf | Yazılı devir anlaşması | Devir alan da aynı yükümlülüğe tabi |
| Kişisel veri | Ayrı DPA şart | KVKK m. 28 uyarınca |
| Uygulama | Tahkim (ICC/ISTAC) | Hızlı, gizli çözüm |
| Hukuk seçimi | Türk Hukuku | Tarafların açık seçimi |

---

*Uyarı: Bu şablonlar genel rehberlik amaçlıdır. Ticari veya yatırımcı görüşmeleri için mutlaka yetkili hukuk danışmanına danışılmalıdır.*


## 🌍 Universal Language Support
- **Turkish Native:** This skill natively supports Turkish. If the user prompt is in Turkish, all analysis, formatting, and output MUST be entirely in Turkish. You do not need explicit "write in Turkish" instructions.
