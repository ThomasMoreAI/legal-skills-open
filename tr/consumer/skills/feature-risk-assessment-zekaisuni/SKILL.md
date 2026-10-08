---
name: feature-risk-assessment-zekaisuni
title: Feature Risk Assessment
description: Tek bir ozellik veya urun riski icin derin Turk urun hukuku karar notu. Lansman review'da yeni/yuksek risk cikarsa, GC/yonetim karar istiyorsa veya regule sektor/AI/KVKK/tuketici riski yogunsa kullan.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/product-legal/skills/feature-risk-assessment
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: tr
practice: consumer
language: tr
---

# Feature Risk Assessment

## Amac

Lansman incelemesi genistir; bu skill tek riski derinlestirir. Cikti, karar verene "ne olabilir, ne kadar ciddi, hangi azaltimla ship edilebilir" sorularini yanitlayan 2-4 sayfalik karar notudur.

## Tetikleyiciler

- Kalibrasyon tablosunda olmayan yeni pattern.
- `Yuksek` veya `Bloke` bulgu.
- Tuketici checkout/abonelik, cocuk, saglik, finans, telekom, AI, yurt disina veri aktarimi, rekabet veya urun guvenligi riski.
- Reklam Kurulu/KVKK/sektor regulatoru ilgisi olabilecek konu.
- Liderlik "ship edersek ne olur?" diye soruyor.

## Yapı

```markdown
[GIZLI HUKUKI / URUN HUKUKU CALISMA TASLAGI - HUKUKCU INCELEMESINE TABIDIR]

Reviewer note
- Kaynaklar:
- Okuma kapsami:
- Dogrulanmasi gerekenler:
- Aksiyon oncesi:

# Ozellik Risk Degerlendirmesi: [Ozellik]

## 1. Ne inceleniyor

[Ozellik, kullanici, hedef pazar, yenilik ve neden eskale edildi.]

## 2. Riskler

### Risk [N]: [Kisa ad]

**Senaryo:** [Somut kotu senaryo]
**Etkilenenler:** [tuketici/musteri/calisan/ucuncu kisi/sirket]
**Olasilik:** [Dusuk/Orta/Yuksek + neden]
**Etki:** [Dusuk/Orta/Yuksek + neden]
**Mevcut azaltimlar:** [varsa]
**Bosluk:** [eksik kontrol]
**Kalan risk:** [kabul edilebilir mi?]
**Kaynak/dogrulama:** [etiket]

## 3. Regulator ve mevzuat gorunumu

[Yalnizca ilgiliyse; Ticaret Bakanligi/Reklam Kurulu/KVKK/BTK/BDDK/SPK/TİTCK/Rekabet/platform]

## 4. Secenekler

| Secenek | Aciklama | Risk azalimi | Maliyet / gecikme |
|---|---|---|---|
| A | Ship as designed | | |
| B | Sartli ship | | |
| C | Kapsam daralt / ertele | | |

## 5. Oneri

**Onerilen:** [Secenek]

[Neden, kalan risk, kim kabul etmeli.]
```

## Kalibrasyon

Profildeki risk istahi, sektor ve gecmis kararlar okunmadan genel hukuki risk notu yazma. Ayni risk fintech, saglik, cocuk urunu veya regule olmayan B2B arac icin farkli agirlikta olabilir.

## Handoff

- KVKK/veri varsa `/privacy-legal:pia-generation` veya `use-case-triage`.
- AI varsa `/ai-governance-legal:aia-generation`.
- Reklam iddiasi varsa `/product-legal:marketing-claims-review`.
- Regule sektor varsa ilgili uzman/hukukcu ve guncel resmi kaynak kontrolu.
