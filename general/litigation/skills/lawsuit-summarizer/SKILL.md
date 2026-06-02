---
name: lawsuit-summarizer
title: Lawsuit Summarizer
description: Dava özetleme, taraf analizi, talep ve savunma özeti, karar sonuçları.
author: mikailustuner
author_url: https://github.com/mikailustuner/OmniRule/tree/main/skills/lawsuit-summarizer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: tr
---

# Lawsuit Summarizer

**Odağ Alanı:** Hukuki dava dosyalarının, mahkeme kararlarının, dilekçelerin ve yargılama tutanaklarının yapısal özetlenmesi; tarafların hukuki konumlarının analizi; talep ve savunma unsurlarının çıkarılması; karar sonuçlarının tespiti.

## Pattern 1: Dava Özetleme Protokolü

```
1. DAVA DOSYASI YAPISI
├── A. GENEL BİLGİLER (Case Header)
│   ├── Dava numarası (Esas No / Karar No)
│   ├── Mahkeme / Yargılama Dairesi
│   ├── Dava türü (Asliye Hukuk, Asliye Ticaret, İş, Ceza)
│   ├── Karar tarihi
│   ├── Davacı ve davalı (ad/soyad veya unvan)
│   ├── Avukatlar listesi
│   └── Davanın konusu (kısa tanım: 1-2 cümle)
│
├── B. OLGUSAL ZEMİN (Fact Pattern)
│   ├── Taraflar arasındaki ilişki (müşteri, tedarikçi, işveren...)
│   ├── Olayların kronolojisi (tarihleriyle birlikte)
│   ├── Uyuşmazlığın doğmasına yol açan olay
│   ├── Tarafların daha önceki eylemleri
│   └── Mücbir sebep veya özel koşullar (varsa)
│
├── C. TALEP VE İDDİA (Claims)
│   ├── Davacının talepleri (maddi + manevi)
│   ├── Hukuki nitelendirme (haksız fiil, sözleşme违an, vb.)
│   ├── Dayanılan normatif hükümler
│   ├── Talep miktarı (varsa)
│   └── İspat vasıtaları (tanık, bilirkişi, fiziki delil)
│
├── D. SAVUNMA (Defenses)
│   ├── Davalının savunmaları (itiraz + karşı iddia)
│   ├── Davalının dayandığı hukuki gerekçeler
│   ├── İspat vasıtaları (karşı deliller)
│   ├── Davanın süresizliğine/itirazına ilişkin savunmalar
│   └── Karşı talep (reconvention) varsa detayları
│
├── E. TARAFLARIN DELİL İNCELEMESİ (Evidence Review)
│   ├── Davacı delilleri
│   ├── Davalı delilleri
│   ├── Bilirkişi raporu (varsa – tarih ve bulguları)
│   └── Keşif / yerinde inceleme (varsa)
│
├── F. MAHKEME DEĞERLENDİRMESİ (Court Analysis)
│   ├── Uyuşmazlık konusu hukuki sorunlar
│   ├── Tarafların hukuki argümanlarının değerlendirilmesi
│   ├── Delillerin ve ispatın değerlendirilmesi
│   ├── Bilirkişi raporunun değerlendirilmesi
│   └── Uygulanan içtihat ve normatif hükümler
│
└── G. HÜKÜM (Judgment)
    ├── Kabul / Ret / Kısmi kabul / Kısmi ret
    ├── Verilen hüküm (maddi tazminat, ifa, ceza vb.)
    ├── Manevi tazminat (varsa)
    ├── Yargılama giderleri (harç, vekalet ücreti, bilirkişi ücreti)
    ├── İstinaf / temyiz süresi ve yolu
    └── Kararın gerekçesi (kısa özet)

2. ÖZETLEME FORMATLARI
├── FORMAT A: YÖNETİCİ ÖZETİ (1 sayfa)
│   ├── Dava özeti: 3-5 cümle
│   ├── Sonuç: Kabul/Ret + temel gerekçe
│   ├── Risk analizi: Düşük/Orta/Yüksek
│   └── Öneri: Takip edilecek adımlar
│
├── FORMAT B: DETAYLI ANALİZ RAPORU (3-5 sayfa)
│   ├── Olgusal zemin (kronolojik)
│   ├── Tarafların hukuki pozisyonları (karşılaştırmalı)
│   ├── Delil değerlendirmesi
│   ├── Hukuki çerçeve ve içtihat
│   └── Karar analizi + gelecek perspektifi
│
└── FORMAT C: PRECEDENT CARD (içtihat kartı)
    ├── Davanın özeti (50 kelime)
    ├── Uygulanan kural (kısa)
    ├── Temel gerekçe (2-3 cümle)
    └── İçtihat değeri: Yüksek/Orta/Düşük
```

## Pattern 2: Taraf Analizi Matrisi

```
TARAFLARIN HUKUKİ POZİSYON ANALİZİ MATRİSİ
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ DAVA TARAFLARI ANALİZİ                                                          │
├──────────────────┬──────────────────────────────────────────────────────────────┤
│ DAVACI (Plaintiff)                                                              │
│ Hukuki pozisyonu │ Haksız fiil / Sözleşme违an / Mülkiyet hakkı ihlali            │
│ Dayandığı hükümler│ TBK m. 112 (borcun ifası), TBK m. 529 (haksız fiil)          │
│ Talep miktarı    │ [TL tutarı] + faiz + yargılama giderleri                      │
│ İspat stratejisi │ [Delil listesi: belgeler, tanıklar, bilirkişi]               │
│ Güçlü yönler     │ • Somut zarar ispatı                                           │
│                   │ • Tanık ifadesı mevcut                                        │
│ Zayıf yönler     │ • Nedensellik bağı zayıf                                       │
│                   │ • Karşı tarafın kusursuzlik ispatı olasılığı                  │
├──────────────────┼──────────────────────────────────────────────────────────────┤
│ DAVALI (Defendant)                                                              │
│ Hukuki pozisyonu │ Sorumluluk reddi / Mücbir sebep / Hasarın paylaştırılması     │
│ Dayandığı hükümler│ TBK m. 114 (ifa imkansızlığı), TBK m. 115 (mücbir sebep)      │
│ Savunma argümanları│ • Davalı kusursuzdur / olayda sorumluluk yok                 │
│                    │ • Davacının ihmali sonucu oluşan hasar                        │
│                    │ • Mücbir sebep mevcuttur                                    │
│ İspat stratejisi │ [Karşı deliller: belgeler, uzman görüşü]                     │
│ Güçlü yönler     │ • Mücbir sebep iddiası destekleyici belgeler                   │
│                   │ • Davalının kusursuzluk ispatı güçlü                          │
│ Zayıf yönler     │ • Sözleşmede açık hüküm aleyhte                                │
│                   │ • Önceki içtihat davacı lehine                                │
└──────────────────┴──────────────────────────────────────────────────────────────┘

KARŞILAŞTIRMALI DEĞERLENDİRME:
├── Hukuki açıdan güçlü taraf: Delillerin ve normatif hükmün netliği
├── Ekonomik açıdan avantajlı taraf: Yargılama masrafları + vekalet ücreti riski
└── Stratejik avantaj: Zamanaşımı süresi / delil durumu / tanık güvenilirliği
```

## Pattern 3: Talep ve Savunma Özetleme

```
TALEP ANALİZİ ŞABLONU
┌─────────────┬─────────────┬─────────────┬─────────────┬─────────────┬──────────────┐
│ Talep No    │ Talep       │ Hukuki      │ Dayanak     │ İspat       │ Değerlendirme│
│             │ İçeriği     │ Nitelik     │ Hüküm       │ Vasıtası    │ (Güç/İmkansız)│
├─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼──────────────┤
│ T.1        │ Maddi       │ Alacak      │ TBK m. 112  │ Sözleşme    │ Güçlü         │
│             │ tazminat    │             │ Sözleşme ifası │ belgeleri,│ (fatura,     │
│             │ TL 500.000  │             │             │ banka       │ sevkiyat     │
│             │ + işlemiş   │             │             │ dekontları  │ belgeleri)   │
│             │ faiz       │             │             │             │              │
├─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼──────────────┤
│ T.2        │ Manevi      │ Haksız fiil │ TBK m. 58    │ Tıbbi       │ Orta         │
│             │ tazminat    │ tazminatı   │ Manevi       │ rapor,      │ (manevi      │
│             │ TL 50.000   │             │ tazminat    │ iş kaybı    │ tazminat     │
│             │             │             │             │ belgesi     │ ispatı zor)  │
├─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼──────────────┤
│ T.3        │ Yargılama   │ Gider       │ HMK m. 323   │ Mahkeme     │ Otomatik     │
│             │ giderleri   │ istemi      │ Giderler     │ kararı      │ (kanunen     │
│             │             │             │ haksız çıkan│             │ düzenlenmiş) │
│             │             │             │ taraftan alınır│           │             │
└─────────────┴─────────────┴─────────────┴─────────────┴─────────────┴──────────────┘

SAVUNMA ANALİZİ ŞABLONU
┌─────────────┬─────────────┬─────────────┬─────────────┬─────────────┬──────────────┐
│ Savunma No  │ Savunma    │ Hukuki     │ Dayanak     │ İspat       │ Değerlendirme│
│             │ İçeriği     │ Nitelik     │ Hüküm       │ Vasıtası    │              │
├─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼──────────────┤
│ S.1        │ Davalı     │ İspat      │ TBK m. 114  │ Hasar      │ Zor          │
│             │ kusursuzdur │ (davalı    │ Kusursuzluk  │ raporu,     │ (davalının   │
│             │             │ kusursuzluk│ ispatı      │ tanık       │ kusursuzluk   │
│             │             │ ispatı     │ davalıya    │ ifadesi,    │ ispatı çok   │
│             │             │ düşer)     │ düşer      │ uzman       │ zordur)      │
├─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼──────────────┤
│ S.2        │ Mücbir      │ Mücbir     │ TBK m. 115  │ OHAL       │ Orta         │
│             │ sebep      │ sebep      │ Mücbir      │ kararnamesi,│ (pandemi     │
│             │ (pandemi)   │             │ sebep       │ resmi       │ ispatı       │
│             │             │             │             │ gazete      │ görece       │
│             │             │             │             │ kayıtları   │ kolaylaşmış) │
├─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼──────────────┤
│ S.3        │ Karşı alacak│ Takas       │ TBK m. 133  │ Carı hesap  │ Güçlü        │
│             │ takası     │             │ Takas       │ özeti,      │ (belgeli     │
│             │ TL 200.000  │             │             │ faturalar   │ karşı        │
│             │             │             │             │             │ alacak varsa)│
└─────────────┴─────────────┴─────────────┴─────────────┴─────────────┴──────────────┘
```

## Pattern 4: Karar Sonuçları ve Sonraki Adımlar

```
KARAR DEĞERLENDİRME ŞABLONU
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ KARAR ANALİZİ                                                                    │
├──────────────────────────────────────────┬────────────────────────────────────────┤
│ Mahkeme                                │ İstanbul 7. Asliye Hukuk Mahkemesi         │
│ Dava No                                │ 2024/2341 E. – 2025/1122 K.                │
│ Karar Tarihi                           │ 2025-04-15                                │
│ Sonuç                                  │ Kısmi kabul (T.1 tam, T.2 kısmi)           │
├──────────────────────────────────────────┼────────────────────────────────────────┤
│ HÜKÜM DETAYI                                                                         │
│ Maddi tazminat                          │ TL 500.000 + işlemiş faiz (d.d. 2023-01-15)│
│ Manevi tazminat                         │ TL 25.000 (T.2'nin yarısı)                │
│ Vekalet ücreti (davacı lehine)          │ TL 35.000                                 │
│ Vekalet ücreti (davalı lehine)          │ Reddedildi                                │
│ Yargılama giderleri                     │ Davalı tarafından alınacak (2/3 davacı, 1/3 davalı)│
│ Bilirkişi ücreti                        │ TL 15.000 (davalı tarafından)            │
├──────────────────────────────────────────┴────────────────────────────────────────┤
│ İÇTİHAT DEĞERİ                                                                         │
│ Karar içtihat niteliğinde mi?          │ Evet – Yargıtay 11. HD içtihadı ile uyumlu │
│ Benzer davalarda emsal niteliği         │ Yüksek – Sözleşmenin mücbir sebep yorumu   │
│                                        │ konusundaki HGK kararı ile tutarlı         │
├──────────────────────────────────────────┬────────────────────────────────────────┤
│ KARŞI OLANAKLAR                                                                         │
│ İstinaf süresi                          │ 2 hafta (HMK m. 341)                      │
│ Temyiz potansiyeli                      │ Yüksek – davalı temyiz edebilir           │
│ Uzlaşma olasılığı                       │ Orta – miktar düşük kalırsa taraflar      │
│                                        │ uzlaşabilir                               │
├──────────────────────────────────────────┴────────────────────────────────────────┤
│ STRATEJİ ÖNERİ                                                                          │
│ Davalı açısından:                     │ İstinaf düşünülmeli; önce uzlaşma teklifi  │
│                                         │ yapılabilir. Temyiz için süre kaçırılmamalı│
│                                         │                                             │
│ Davacı açısından:                      │ Karar olumlu; icra takibine başlanabilir.  │
│                                         │ İstinaf riski varsa karşı istinaf        │
│                                         │ hazırlığı yapılmalı.                      │
└──────────────────────────────────────────┴────────────────────────────────────────┘
```

## Key Patterns (Özet)

| Bölüm | İçerik | Kullanım |
|---|---|---|
| A | Dava genel bilgileri | Hızlı tanımlama |
| B | Olgusal zemin | Kronoloji ve bağlam |
| C | Talep analizi | Davacının iddiaları |
| D | Savunma analizi | Davalının argümanları |
| E | Delil değerlendirmesi | İspat gücü analizi |
| F | Mahkeme değerlendirmesi | Hukuki gerekçe |
| G | Karar ve sonuçlar | Hüküm + içtihat değeri |
| H | Strateji önerisi | Sonraki adımlar |

## Anti-Patterns

```
❌ YALNIZCA DAVA KONUSUNU AKTARMA
   "X şirketi Y şirketine dava açtı" bilgisi yetersizdir.
   → Olayların kronolojisi, hukuki nitelendirme ve deliller dahil edilmelidir.

❌ TARAFLARIN POZİSYONLARINI EŞİT ÖLÇÜDE SUNMA
   Mahkemeler tarafsız değerlendirme yapar ama analist olarak
   bir tarafın hukuki argümanlarının güçlü/zayıf yönlerini ayrı
   değerlendirmek gerekir.
   → Tarafları ayrı sütunlarda, güçlü/zayıf yönleriyle analiz et.

❌ HÜKMÜ OLDUĞU GİBİ AKTARMA
   Kararın tam metnini aktarmak yerine hukuki özü çıkarılmalıdır.
   → "Karar: X Mahkemesi, Y şirketinin davasını kabul etti" değil,
      hangi hukuki gerekçeyeyle kabul ettiği belirtilmeli.

❌ İÇTİHAT DEĞERİNİ ABARTMA
   Tek bir mahkeme kararı "içtihat" oluşturmaz.
   → En az 3 Yargıtay kararıyla desteklenmemiş bir kural
      "içtihat" olarak değil "gösterge" olarak nitelendirilmelidir.

❌ SONUÇ/ÖNERİ KISMINI ATLAMA
   En kritik kısım genellikle ihmal edilir.
   → "Bu karar ne anlama geliyor? Bir sonraki adım ne olmalı?"
      soruları açıkça yanıtlanmalıdır.

✅ DOĞRU YAPI
   Dosya bilgileri → Olgusal zemin → Talep matrisini çıkar →
   Savunma matrisini çıkar → Delil değerlendirmesi →
   Mahkeme değerlendirmesi → Hüküm detayı → İçtihat değeri →
   Stratejik öneri → Sonraki adımlar
```

## Quick Reference

| Görev | Kaynak | Detay |
|---|---|---|
| Yargıtay kararları | Lexpera / Legalbank | Daire, yıl, esas no ile arama |
| Danıştay kararları | danistay.gov.tr | İdari dava türleri |
| HMK (Medeni Usul) | mevzuat.gov.tr | 6100 sayılı Kanun |
| HMK giderler | HMK m. 323-340 | Yargılama giderleri çizelgesi |
| İstinaf/Temyiz | Lexpera Yargıtay | Bölge Adliye Mahkemeleri |
| Dosya erişimi | UYAP (uyap.gov.tr) | Avukat portali |
| İçtihat içerik | Yargıtay Kararları Dergisi | Aylık içtihat derlemeleri |
| Karşılaştırmalı içtihat | Istanbulli Bİlgbank | Yargıtay + Danıştay + AYM |
| Yasal süre hesaplama | Hukuk Takvimi | HMK süre hesaplama araçları |
| Vekalet ücreti | AVUKAT (barolar) | Baro asgari ücret tarifesi |

---

*Uyarı: Bu analiz aracı hukuki danışmanlık yerine geçmez. Gerçek dava dosyaları için mutlaka yetkili avukata danışılmalıdır. İçtihat değerlendirmesi yalnızca göstergesel niteliktedir.*


## 🌍 Universal Language Support
- **Turkish Native:** This skill natively supports Turkish. If the user prompt is in Turkish, all analysis, formatting, and output MUST be entirely in Turkish. You do not need explicit "write in Turkish" instructions.
