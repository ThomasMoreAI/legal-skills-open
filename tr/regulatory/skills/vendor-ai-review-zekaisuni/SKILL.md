---
name: vendor-ai-review-zekaisuni
title: /vendor-ai-review (Tedarikçi AI / Copilot Sözleşme İncelemesi)
description: Tedarikçi sözleşmelerindeki Yapay Zeka (AI) kullanım şartlarını, model eğitimi izinlerini ve fikri mülkiyet atıflarını inceler. Veri sorumlusu/işleyen rollerini (KVKK), opt-out/opt-in politikalarını, TTK (ticari sır) ihlali yaratacak maddeleri  tespit eder.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/ai-governance-legal/skills/vendor-ai-review
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: tr
practice: regulatory
language: tr
---

# /vendor-ai-review (Tedarikçi AI / Copilot Sözleşme İncelemesi)

## Amaç

Tedarikçilerin (özellikle SaaS hizmetlerinin) kullanım koşullarında (Terms of Service) yer alan AI ve Copilot şartlarını incelemek. Temel soru: **"Müşteri (yani şirketimiz) olarak bu veriyle onların modelini eğitiyor muyuz?"**

Bu skill, AI maddelerini KVKK, FSEK ve TTK (Ticari Sır) riski açısından inceler ve ilgili maddelerin redline (düzeltme) önerisini oluşturur.

## İş Akışı

1. Sözleşmeyi tara ve **"Artificial Intelligence", "Machine Learning", "Model Training", "Data Usage", "Telemetry", "Copilot"** veya **"Output/Input"** kelimelerini bul.
2. Aşağıdaki **Türkiye ve Enterprise Odaklı AI Kontrol Listesini** (Checklist) uygula.
3. Kırmızı çizgileri saptayıp, Hukuk Kuralları çerçevesinde (Opt-out vs. Opt-in) redline taslağını sun.
4. Privacy/Data Protection birimine handoff yapılacak bir madde varsa raporla.

## Türkiye Odaklı AI Kontrol Listesi

### 1. Model Eğitimi (Training & Machine Learning)
- Sözleşme, tedarikçinin Customer Data'yı (Kişisel Veri, Loglar, Analitik Veriler dahil) kendi modellerini veya üçüncü parti (OpenAI vb.) modelleri eğitmek için **kullanılmasına (training)** izin veriyor mu?
- **Hedefimiz:** SIFIR eğitim yetkisi (Zero training rights) veya mutlak "Opt-out" (eğitimden çıkış) hakkı vermek. Redline hedefi: "Tedarikçi, Müşteri Verilerini ve Müşteri Çıktılarını hiçbir dil modelini (LLM) veya yapay zeka aracını eğitmek amacıyla YARARLANAMAZ."

### 2. Girdiler ve Çıktılar (Inputs and Outputs)
- Prompt (Girdi) ve Output (Çıktı) kime ait?
- **FSEK ve Sözleşme Riski:** Üretilen içeriğin/kodun mülkiyeti *Müşteriye* devrediliyor mu? Tedarikçi, bu çıktıları başka müşterilere gösterme veya saklama hakkına sahip mi?
- **Hedefimiz:** Çıktıların mülkiyetinin ve teliflerinin (FSEK uyarınca devredilebilen ekonomik haklar) münhasıran şirkete ait olması.

### 3. KVKK ve Yurt Dışı Veri Aktarımı (KVKK m.9)
- Girdiğimiz Müşteri verileri, tedarikçi tarafından üçüncü taraf AI modellerine (örn. OpenAI API) aktarılıyor mu?
- Eğer aktarılıyorsa bu tedarikçiler "Alt-Veri İşleyen" (Sub-processor) olarak listelenmiş mi?
- Verinin işlendiği sunucular nerede (ABD, AB)? Özel Nitelikli Kişisel Veri aktarım kısıtı var mı?

### 4. Sorumluluk ve Telif İhlali (Indemnification)
- Eğer aracın ürettiği bir görsel/kod, üçüncü bir kişinin telif hakkını (FSEK ihlali vs.) zedelerse, Tedarikçi sorumluluğu üstleniyor mu (IP Indemnity)? Yoksa sorumluluğu Müşteriye mi yıkıyor?

## Çıktı Formatı

```markdown
# Tedarikçi AI Sözleşmesi İncelemesi: [Kurum/Tool Adı]

## Genel Puan: 🔴 (Kritik Risk) | 🟡 (Dikkat / Opt-Out Gerekli) | 🟢 (Güvenli / Enterprise Standardı)

## 📌 En Büyük AI Riskleri
1. **[Örn: Müşteri verisiyle model eğitimi var - KVKK ve TTK Sır İfşası riski]**
2. **[Örn: Çıktıların mülkiyeti tam verilmemiş - FSEK Riske açık]**

## 🛑 Tespit Edilen Riskli Maddeler & Redline Önerileri

**Mevcut Madde (Özet):**
[Riskli maddenin atfı]

**Risk Türü:** [KVKK / FSEK / Ticari Sır]

**Türk Hukuku Beklentisi:** Şirket politikası ve KVKK gereği tedarikçi bu veriyi model eğitiminde kullanamaz.

**Düzeltme (Redline) Önerisi:**
*"Tedarikçi (Vendor), Müşteri Verilerini, Input'ları ve Output'ları doğrudan veya dolaylı olarak herhangi bir büyük dil modelini (LLM), makine öğrenmesini VEYA yapay zeka algoritmasını geliştirmek veya eğitmek için kullanamaz."*

## 🔄 Privacy / KVKK Handoff
[KVKK Müşavirinden açık rıza veya alt-işleyen teyidi alınıp alınmayacağı hakkında not.]
```
