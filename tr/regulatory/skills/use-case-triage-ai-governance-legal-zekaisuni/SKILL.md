---
name: use-case-triage-ai-governance-legal-zekaisuni
title: /use-case-triage (Yapay Zeka Kullanım Senaryosu Triyajı)
description: Önerilen bir Yapay Zeka (AI) kullanım senaryosunu şirket politikasına ve envantere göre inceler — Onaylı, Şartlı Onaylı veya Reddedildi (Onaylanmadı)  olarak sınıflandırır. KVKK, FSEK ve veri güvenliği risklerini saptayarak gerekli koşulları belirler.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/ai-governance-legal/skills/use-case-triage
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: regulatory
language: tr
---

# /use-case-triage (Yapay Zeka Kullanım Senaryosu Triyajı)

## Amaç

Bu skill, iş birimlerinden gelen "Şu amaçla X yapay zeka aracını kullanabilir miyiz?" veya "Verileri falanca LLM'e yükleyebilir miyiz?" sorularını, şirketin AI Kullanım Politikası'na, KVKK uyumuna ve FSEK risklerine göre triyajlar.

Çıktı bir hukuki mütalaa değil, Hukuk/Uyumluluk birimine (Privacy/Product Counsel) yönlendirilmeden önceki **ilk risk değerlendirmesi ve şartlar (conditions)** raporudur.

## İş Akışı

1. `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md` dosyasını oku. 
2. `## Yapay Zeka Kullanım Envanteri` ve `## Kırmızı Çizgiler (Red Lines)` bölümlerini kontrol et.
3. Senaryo belirsizse (hangi veri kullanılacak, hangi tool, vb.) eksik bilgileri netleştirmesi için kullanıcıya soru sor.
4. Kayıt (Registry) taraması yap → Kırmızı Çizgi (Red line) kontrolü yap → Sınıflandır.
5. Çıktı olarak: Sınıflandırma sonucu, gerekçe, KVKK/FSEK şartları (eğer şartlıysa), yönetişim seviyesi ve Hukuk/Ürün birimlerine handoff aktarımı sağla.

## Türkiye Uyarlama Katmanı (KVKK ve FSEK)

Değerlendirmeyi şu kriterlere göre yapın:

1. **KVKK (Kişisel Verilerin Korunması) Riskleri:**
   - **Veri Tipi:** Senaryo anomimleştirilmiş veri mi, genel kişisel veri mi, yoksa Özel Nitelikli Kişisel Veri mi içeriyor?
   - **Veri Aktarımı (KVKK m.9):** Bulut tabanlı (OpenAI, Anthropic) modeller veriyi yurt dışına gönderir. Sunucu Türkiye'de (On-Premise) değilse, KVKK m.9 aktarım kuralları (veya açık rıza) şartı triyajda açıkça belirtilmelidir.
   - **Otomatik Karar Alma:** İnsan müdahalesi olmadan karar alma (KVKK m.11) ciddi risk taşır (EU AI Act Yüksek Risk).

2. **Ticari Sır (TTK m. 54-55) & Avukatlık Sırrı (Av.K m.36):**
   - Kaynak kodu, şirketin finansal verileri, gizli evraklar public LLM'lere (ChatGPT Free vs.) girilemez. Enterprise sözleşmesi var mı kontrol et.

3. **FSEK (Fikri Mülkiyet / Telif) Riskleri:**
   - AI'ın ürettiği eserlerin/kodun FSEK ihlali doğurup doğurmadığı uyarısı eklenir.

## Sınıflandırma Mantığı

### 🔴 ONAYLANMADI (NOT APPROVED)
Eğer senaryo şunları içeriyorsa kırmızı bayrak çek:
- Müşteri, çalışan verisi veya Özel Nitelikli Veri'nin public bir AI aracına yüklenmesi.
- Biyometrik tanıma, yüz tanıma (EU AI Act Yasaklı/Yüksek Risk).
- Kaynak kodunun public bir LLM'e girilmesi.
- İnsan kararı gerektiren kritik konularda %100 otonom karar.

### 🟡 ŞARTLI ONAYLI (CONDITIONAL)
- Kurumsal sözleşme ile bağlanmış LLM (veri eğitime girmiyor - Zero Data Retention).
- Sadece anonim veri kullanımı.
- Çıktıda insan denetimi (Human-in-the-loop).

### 🟢 ONAYLI (APPROVED)
- Yalnızca kamuya açık (public) verilerin GPT ile özetlenmesi/çevirisi.
- Model eğitimi (training) için kullanılmama taahhüdü olan kurum-içi (On-Prem) uygulamalar.

## Çıktı Formatı

```markdown
# Yapay Zeka Kullanım Senaryosu Triyajı

**Senaryo:** [Kısa tanım]
**Kullanılacak Araç:** [Örn. ChatGPT Enterprise]

## Sonuç: 🔴 Onaylanmadı | 🟡 Şartlı Onaylı | 🟢 Onaylı

[Gerekçe]

## Zorunlu Şartlar (Conditions to Proceed)
[Eğer 🟡 Şartlı ise]
- **Veri Kısıtı:** [Örn: Sadece anonimleştirilmiş veri girilebilir]
- **Lisans Şartı:** [Örn: Enterprise versiyon kullanılmalı, opt-out aktif olmalı]
- **İnsan Denetimi (Human-in-the-loop):** [Son karar insan onayından geçmeli]

## Risk Analizi
- **KVKK:** [Yurt dışı aktarım riski, vb.]
- **FSEK/TTK:** [Kod mülkiyeti, ticari sır riski]

## Eskalasyon / Handoff
Bu projenin ilerlemesi için Privacy Counsel / DPO onayına ihtiyaç vardır.
```
