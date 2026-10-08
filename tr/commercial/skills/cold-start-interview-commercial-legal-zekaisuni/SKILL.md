---
name: cold-start-interview-commercial-legal-zekaisuni
title: /cold-start-interview
description: Run the commercial-legal setup interview for the Legal Turkish adaptation. Builds a Turkish-law commercial contracts practice profile with playbook side, KVKK/data posture, Turkish notice methods, TL approval thresholds, renewal tracking, escalation matrix, and output guardrails.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/commercial-legal/skills/cold-start-interview
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: commercial
language: tr
---

# /cold-start-interview

İlk kurulum mülakatını çalıştırır ve `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` dosyasını yazar. Bu dosya bütün commercial skill'lerin okuduğu pratik profilidir.

## Instructions

1. **Check current state.** Read `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`.
   - Missing or placeholders -> start interview.
   - Populated and no `--redo` -> ask before overwriting.
   - `--side sales|purchasing` -> ask only side-specific playbook questions.

2. **Use the template.** Use plugin template `commercial-legal/CLAUDE.md` as the output scaffold.

3. **Write only after review.** Before writing, summarize open gaps and ask whether to leave placeholders.

4. **Do not infer from ambient memory.** Use only the user's answers and documents explicitly shared in this session.

5. **Show summary and next steps.** Offer a test review after writing.

## `--check-integrations`

Probe only what can actually be tested. Do not mark an integration as connected merely because it is listed in `.mcp.json`.

Check:

- CLM / contract repository,
- e-signature,
- KEP or e-notice records if configured,
- document storage,
- messaging destination,
- UYAP only if the user actually uses it for dispute-linked matters.

Update `## Available Integrations` in the user profile.

## `--side sales|purchasing`

Re-run only the matching playbook section:

- `sales`: company sells goods/services; company is vendor/supplier.
- `purchasing`: company buys goods/services; company is customer/buyer.

Leave the other side untouched. Update `**Active side:**`.

## Opening Preamble

Say:

> `commercial-legal` ticari sözleşme işleri içindir: tedarikçi sözleşmeleri, SaaS/abonelikler, gizlilik sözleşmeleri, tadil geçmişi, yenileme/fesih takibi ve onay eskalasyonları.
>
> Kısa kurulum temel rol, taraf, yetki, entegrasyon ve varsayılan playbook alanlarını kurar. Tam kurulum gerçek playbook pozisyonlarınızı, TL onay eşiklerinizi, KVKK yaklaşımınızı, yenileme uyarılarınızı ve örnek imzalı sözleşmelerden çıkan kalibrasyonu ekler.
>
> Kısa mı, tam mı ilerleyelim?

Wait for the answer.

## Interview Sections

### Part 0 - Role and Practice Setting

Ask:

- Bu aracı kim kullanacak?
  - avukat / hukuk müşaviri / hukuk profesyoneli,
  - avukat erişimi olan hukuk dışı kullanıcı,
  - avukat erişimi olmayan hukuk dışı kullanıcı.
- Çalışma yapısı nedir?
  - kurum içi hukuk müşavirliği,
  - hukuk bürosu,
  - serbest avukat,
  - legal ops / sözleşme ekibi.
- Şirket veya müvekkil kim?
- Sektör ve faaliyet alanı nedir?
- Ana sözleşme akışı: satış tarafı, satın alma tarafı, ikisi de?

### Part 1 - Turkish Law Defaults

Ask:

- Varsayılan uygulanacak hukuk Türk Hukuku mu?
- Tercih edilen mahkeme/icra dairesi var mı?
- Tahkim kabul ediliyor mu? ISTAC/MTO/ad hoc?
- Bildirimlerde tercih: KEP, noter, iadeli taahhütlü, e-posta/portal?
- UYAP sadece dava/icra bağlantılı dosyalarda mı kullanılıyor?
- Arabuluculuk dava şartı kontrolü hangi dosyalarda kritik? 6325 sayılı Kanun ve özel dava şartı hükümleri için varsayılan yaklaşım ne olsun?

### Part 2 - Integrations

Ask:

- CLM veya sözleşme arşivi.
- E-imza sistemi.
- KEP/e-tebligat kayıtlarına erişim.
- Drive/SharePoint/iManage gibi belge deposu.
- Slack/Teams/e-posta bildirim kanalı.

### Part 3 - Playbook Side

If `sales` or `both`, ask sales-side positions:

- sorumluluk sınırı,
- dolaylı zararlar,
- tazminat/indemnity,
- cezai şart (TBK m.179-185),
- KVKK/DPA/yurt dışına aktarım,
- FSEK/IP ownership,
- süre/fesih/yenileme,
- bakiye hükümler / sözleşme sona erse de devam edecek yükümlülükler,
- damga vergisi (DVK/488) ve vergi uzmanı eskalasyonu,
- uygulanacak hukuk/yetki/tahkim,
- "asla kabul etmeyiz" listesi,
- tek en önemli deal-breaker.

If `purchasing` or `both`, ask the same for purchasing-side.

### Part 4 - NDA Triage

Ask GREEN/YELLOW/RED positions for:

- karşılıklılık,
- gizli bilgi tanımı,
- süre / bakiye hükümler (survival),
- istisnalar,
- residuals / hafızada kalan bilgi istisnası (TBK m.394-400, TTK m.54-55, KVKK ve rekabet hassasiyeti),
- cezai şart (TBK m.179-185),
- KVKK/data transfer,
- uygulanacak hukuk/yetki,
- rakipler arası hassas bilgi.

GREEN requires attorney-reviewed positions.

### Part 5 - Escalation and Approval

Ask:

- TL thresholds,
- approvers by issue type,
- imza yetkilileri,
- automatic escalation triggers,
- legal/business decision split,
- approval channel.

### Part 6 - Renewal Tracking

Ask:

- renewal register owner,
- alert horizon,
- alert destination,
- default notice methods,
- transit buffer assumptions,
- whether price escalation or FX exposure needs special alerts.

### Part 7 - Matter Workspaces

Ask whether matter workspaces are needed:

- In-house with one company -> usually off.
- Law firm or multi-client practice -> on.

If on, ask cross-matter context default and confidentiality levels.

### Part 8 - Seed Documents

Ask for recent signed agreements or playbook documents:

> Son 5-10 imzalı sözleşmeyi, playbook dokümanını veya onay matrisini paylaşabilirsiniz. Yoksa atlayabiliriz; eksikleri profilde açıkça işaretlerim.

Extract positions but mark anything uncertain as `[verify]` or `[PLACEHOLDER]`.

## Before Writing

Show:

```markdown
## Kurulum Özeti
- Rol:
- Taraf:
- Ana playbook pozisyonları:
- Onay matrisi:
- KVKK yaklaşımı:
- Yenileme takibi:
- Açık kalan sorular:
```

Ask:

> Bunları profiline yazayım mı? Açık kalan alanları placeholder olarak bırakabilirim.

## Output Profile

Write to:

`~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`

Use the template sections:

- Who We Are
- Who's Using This
- Turkish Law Defaults
- Available Integrations
- Matter Workspaces
- Playbook
- NDA Triage Positions
- Escalation and Approval Matrix
- Review Preferences
- Renewal Tracking
- Playbook Monitor Settings
- Outputs

## What this skill does not do

- It does not give legal advice for a specific contract.
- It does not run conflicts checks.
- It does not connect to UYAP, KEP, CLM, or e-signature systems by itself.
- It does not approve signature or sending.
- It does not silently fill legal positions the user skipped.
