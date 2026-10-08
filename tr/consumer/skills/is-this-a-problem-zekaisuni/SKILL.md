---
name: is-this-a-problem-zekaisuni
title: /is-this-a-problem
description: 'PM, marketing veya founder tarafindan gelen hizli "bu sorun olur mu?" sorularina Turk urun hukuku kalibrasyonuyla cevap verir. Kisa triage: temiz / bakmak gerekir / dur.'
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/product-legal/skills/is-this-a-problem
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: consumer
language: tr
---

# /is-this-a-problem

## Amac

Uzun memo yazmadan riski ayikla. Soru basitse kisa cevap ver; hukuki/teknik kaynak gerektiren yerde "emin degilim" demekten cekinme ve dogru skill'e yonlendir.

## Akis

1. Product profile `## Risk Kalibrasyonu` bolumunu oku.
2. Soruyu su tipe ayir: hukuki problem, ticari karar, UX/musteri deneyimi, policy karari, teknik guvenlik, marka/pazarlama.
3. Kalibrasyon pattern'leriyle eslestir.
4. Tuzak sorulardan biri varsa tek yakalayici soru sor.
5. Cikti: `Temiz`, `Bakmak gerekir`, veya `Dur`.

## Tuzak Sorular

| Soru gibi gorunur | Neden riskli olabilir | Tek soru |
|---|---|---|
| "Bu veriyi yeni feature'da kullanalim mi?" | KVKK'da yeni amac/aktarim/acik riza gerekebilir | Veriyi ilk toplarken kullaniciya hangi amaci soyledik? |
| "A/B testte farkli fiyat gosterelim mi?" | Tuketici, ayrimcilik, haksiz ticari uygulama, fiyat seffafligi | Segmentler nasil belirleniyor ve ayni urune farkli fiyat mi var? |
| "Ucretsiz deneme bitince otomatik ucret alalim mi?" | Abonelik, on bilgilendirme, cayma, acik onay | Kullanici odeme oncesi hangi ekranda neyi onayliyor? |
| "Musteri logosunu siteye koyalim mi?" | Marka/publicity/sozlesme izni ve endorsement imasi | Yazili logo/publicity izni var mi? |
| "Influencer bunu soylesin mi?" | Ortulu reklam ve ifsa | Is birligi acik ve gorunur sekilde belirtiliyor mu? |
| "En hizli/en iyi/tek cozum diyelim mi?" | Karsilastirmali/mutlak iddia kanit ister | Bu iddiayi destekleyen guncel, objektif kanit var mi? |
| "Yeni vendor'a veri gonderelim mi?" | KVKK, DPA, yurt disi aktarim, guvenlik | Hangi veri, hangi ulkeye, hangi sozlesme ile gidiyor? |
| "Sadece internal tool" | Calisan/musteri verisi yine KVKK kapsaminda olabilir | Kimin verisine erisiyor? |
| "AI sadece yardimci" | AI use-case, otomatik karar, veri egitimi, vendor sarti | AI ne karar veriyor, input/output kime etki ediyor? |
| "Cerez banner'ina dokunmadan tracking ekleyelim" | Aydinlatma/acik riza/cerez kategorisi degisebilir | Yeni tracking hangi amacla ve hangi kategoriyle calisiyor? |

## Cevap Formati

```markdown
[Temiz | Bakmak gerekir | Dur]

[Tek cumle karar ve neden.]

[Gerekirse tek sonraki adim: privacy triage / claims review / launch review / sektor uzmani / hukukcu onayi.]
```

Ornek:

```markdown
Bakmak gerekir - yeni vendor'a musteri verisi gidiyorsa KVKK, yurt disina aktarim ve guvenlik review kapisi aciliyor.

Sonraki adim: veri akisina bakip `/privacy-legal:use-case-triage` calistiralim.
```

## Ne zaman kullanma

- PRD veya kapsamli lansman varsa `launch-review`.
- Reklam metni/claim varsa `marketing-claims-review`.
- Tek risk derin karar gerektiriyorsa `feature-risk-assessment`.
- Guncel mevzuat/tutar/platform kuralina dayali kesin cevap isteniyorsa once resmi kaynak dogrula.
