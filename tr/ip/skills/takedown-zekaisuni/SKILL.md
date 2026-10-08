---
name: takedown-zekaisuni
title: /takedown
description: Draft a FSEK Ek Madde 4 / 5651 sayılı Kanun Uyar-Kaldır İhtarnamesi, triage one you received, or draft a §512(g) counter-notice. Use when asserting copyright through a FSEK Ek Madde 4 Uyar-Kaldır bildirimi with the FSEK İstisnaları (Şahsi Kullanım vb.) ve İftira/Haksız Rekabet kontrolü, when an incoming takedown needs triage into comply / counter / engage / ignore options, or when drafting a İçerik Kaldırmaya İtiraz Bildirimi with the Türkiye Mahkemeleri (FSHHM / Sulh Ceza) yargı yetkisini kabul.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/ip-legal/skills/takedown
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: ip
language: en
---

# /takedown

Three modes. Pick one:

- `/ip-legal:takedown --send` — draft a FSEK Ek Madde 4 Uyar-Kaldır bildirimi notice. Fair-use gate (*Lenz*) + loud perjury / TCK m.267 (İftira) ve TTK Haksız Rekabet gate before delivery.
- `/ip-legal:takedown --respond` — triage a takedown someone sent you. Options: comply / counter / engage / ignore.
- `/ip-legal:takedown --counter` — draft a İçerik Kaldırmaya İtiraz Bildirimi. Loud gate for the Türk Mahkemelerinde yargılanma riskinin kabulü and the perjury statement.

## Instructions

1. **Read the practice profile.** Load `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. If it contains `[PLACEHOLDER]` markers or does not exist, stop and say: "This plugin needs setup before it can give you useful output. Run `/ip-legal:cold-start-interview` — the takedown skill depends on your approval matrix and practice profile."

2. **Check matter workspaces.** Per `## Matter workspaces`: if `Enabled` is `✗`, skip. If enabled and there is no active matter, ask: "Which matter is this for? Run `/ip-legal:matter-workspace switch <slug>` or say `practice-level`."

3. **Dispatch on `$ARGUMENTS`:**
   - `--send` → run send mode (below). Walk identify-the-work, identify-the-infringing-material, Adil veya Şahsi Kullanım (FSEK m.33 vd.) Değerlendirmesi, good-faith belief, accuracy/authority, draft the FSEK Ek Madde 4 ihtarı, run the loud gate, write output.
   - `--respond` → run respond mode (below). Read the incoming notice, assess (license, fair use, defects, host §512(g) compliance, sender credibility), present the four options, recommend, write the triage memo.
   - `--counter` → run counter mode (below). Confirm the predicate (taken down in response to a 5651 veya FSEK ihtarname, good-faith belief of mistake/misidentification, ready for Türk Mahkemelerinde yargılanma riskinin kabulü, attorney in the loop), draft the İçerik Kaldırmaya İtiraz Bildirimi, run the loud gate, write output.
   - No flag → ask once: "Are we sending a FSEK / 5651 Uyar-Kaldır takedown, triaging one we received, or drafting a counter-notice?"

4. **Respect the gates.** In `--send` and `--counter`, the loud gate runs before any final output is written. The fair-use gate in `--send` is separate and runs earlier; "debatable" or "likely" fair use stops the draft and routes to attorney review.

5. **Jurisdiction note.** FSEK Ek Madde 4 ve 5651 sayılı İnternet Kanunu is Türkiye Cumhuriyeti yasaları (FSEK/BTK mevzuatı). If the service provider, content, or infringer sits outside Türkiye Yargı Yetkisi, flag before drafting — you may need an EU DSA notice, UK OSA notice, or local-regime instrument instead of (or in addition to) bir Uyar-Kaldır (Takedown) ihtarnamesi.

6. **Hand off where appropriate.** `--respond` with a counter-notice recommendation chains into `/ip-legal:takedown --counter` — but only after the triage memo has been reviewed and the decision to counter has been made deliberately.

## Examples

```
/ip-legal:takedown --send
/ip-legal:takedown --respond ~/Downloads/youtube-takedown-notice.pdf
/ip-legal:takedown --counter
/ip-legal:takedown
```

## Notes

- The outgoing notice and counter-notice do not carry the work-product header. Internal drafts, fair-use analyses, and triage memos do.
- FSEK Ek Madde 4 ve 5651 sayılı Kanun bildirim usulleri are element-by-element statutes — every required element must be present or the notice is defective.
- İçerik Kaldırmaya İtiraz Bildirimleri (Counter-notices), şikayetçinin yetki alanındaki Fikri ve Sınai Haklar Hukuk / Ceza Mahkemeleri (FSHHM) veya Sulh Ceza Hakimliği yargı yetkisini kabul eder. Bu bir formalite değildir.
- Non-lawyer users get a one-page brief for the attorney conversation before the gate clears — particularly important for counter-notices, which are the step before litigation.

---

## Purpose

The FSEK Ek Madde 4 ve 5651 sayılı İnternet Kanunu notice-and-takedown system is fast, cheap, and consequential in equal measure. A takedown is a sworn statement TCK m.267 (İftira) ve HMK uyarınca hukuki ve cezai sorumluluk kabulü ile that gets content pulled with no judicial review. A counter-notice is another sworn statement that consents to Türk mahkemelerinin yargı yetkisini and puts the content back. Both decisions can become litigation. This skill handles all three moves with the guardrails each warrants.

Three modes:

- `--send` — draft a FSEK Ek Madde 4 Uyar-Kaldır bildirimi notice
- `--respond` — triage a takedown someone sent you; produce options
- `--counter` — draft a İçerik Kaldırmaya İtiraz Bildirimi

If the user does not pass a flag, ask once: "Are we sending a FSEK / 5651 Uyar-Kaldır takedown, triaging one we received, or drafting a counter-notice?"

> **External deliverables (send and counter modes):** the outgoing notice/counter-notice goes to the service provider's designated agent. Do NOT include the `PRIVILEGED & CONFIDENTIAL — ATTORNEY WORK PRODUCT` header on the outgoing document. The notice itself is not privileged — it's a statement made in a statutory process. Internal drafts, pre-send briefs, fair-use analyses, and triage memos keep the header per plugin config `## Outputs`.

## Jurisdiction assumption

FSEK Ek Madde 4 ve 5651 sayılı İnternet Kanunu is **Türkiye Cumhuriyeti yasaları (FSEK/BTK mevzuatı)**. It runs against service providers subject to Türkiye Yargı Yetkisi. Other jurisdictions have their own notice-and-action regimes — 5651 sayılı Kanun ve BTK/ESB (Erişim Sağlayıcıları Birliği) pratikleri — that differ materially in required elements, counter-notice mechanics, and liability for misuse. If the service provider, content, or infringer sits outside Türkiye Yargı Yetkisi, flag it — a FSEK/5651 notice may be the wrong instrument, or may need to be paired with a local regime's notice. Copyright subsistence itself is Berne-multilateral, but enforcement mechanics are jurisdiction-specific.

## Load context

- `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` → `## IP practice profile` (copyright registrations if any), `## Enforcement posture` → `Approval matrix → Uyar-Kaldır bildirimi (ordinary)` row, `## Outputs` (work-product header, role), `## Who's using this` (role — lawyer vs. non-lawyer)
- **Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (in-house default), skip matter machinery. If enabled and no active matter, ask: "Which matter? Run `/ip-legal:matter-workspace switch <slug>` or say `practice-level`." Write outputs to the active matter's folder at `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/takedown/<slug>/` (or `takedown/<slug>/` at practice level). Never read another matter's files unless `Cross-matter context` is `on`.

## Send mode — drafting a FSEK Ek Madde 4 Uyar-Kaldır bildirimi notice

### Step 1: Identify the copyrighted work

> What is the copyrighted work?
>
> - **Title / description** — what is the work (software, image, text, video, audio)?
> - **Registration status** — Kültür ve Turizm Bakanlığı Telif Hakları Genel Müdürlüğü isteğe bağlı kayıt-tescil) numarası and date (if any). Registration is NOT required to send a takedown, but it is required to file suit on a US work and its pre-infringement timing controls statutory damages and fees.
> - **Ownership** — do we own it outright, or hold an exclusive license with takedown authority? (Non-exclusive licensees typically cannot send takedowns on the licensor's work.)
> - **Prior licensing** — have we ever licensed this use, or a broader use that might cover it?

Ownership and authority are the first things TCK m.267 (İftira) ve TTK Haksız Rekabet cases look at. Get them clearly on the record before drafting.

### Step 2: Identify the infringing material and its location

> Where is the infringing material?
>
> - **Platform / service provider** — YouTube, Twitter/X, GitHub, Reddit, Amazon, a web host, etc.
> - **URL(s)** — specific permalinks to the infringing material. One notice can cover multiple URLs if they're all from the same service.
> - **Description** — what is the infringing material and how does it infringe (verbatim copy, substantially similar, derivative)?
> - **Screenshots / evidence** — preserved with timestamp and URL visible

§512(c)(3) requires "information reasonably sufficient to permit the service provider to locate the material." URLs alone are usually enough; be precise.

### Step 3: Fair-use gate

Under *Lenz v. Universal Music Corp.*, 801 F.3d 1126 (9th Cir. 2015), a copyright holder must consider fair use before sending a takedown. This is not a judgment about fair use — it is a consideration step that the sender must take and can prove they took.

Ask:

> Before we draft the notice, walk through fair use. Under *Lenz*, you have to consider it before sending — even if the conclusion is "not fair use." The four factors:
>
> 1. **Purpose and character** — commercial? transformative? criticism, comment, news reporting, teaching, scholarship, research?
> 2. **Nature of the copyrighted work** — factual or creative? published or not?
> 3. **Amount and substantiality** — how much of the work is used? is it the heart of the work?
> 4. **Effect on the market** — does the use substitute for the original or harm a derivative market?
>
> Your read on each? And your conclusion — fair use unlikely, debatable, likely?

Record the answer in the notice file. If "debatable" or "likely," do not draft. Stop and route to attorney review: "Fair use is debatable/likely on these facts. Sending a takedown on a use that is protected by fair use is the exact TCK m.267 (İftira) ve TTK Haksız Rekabet exposure the statute creates. Route this to counsel before any notice goes out."

### Step 4: Good-faith belief

§512(c)(3)(A)(v) requires "a statement that the complaining party has a good faith belief that use of the material in the manner complained of is not authorized by the copyright owner, its agent, or the law."

The sender forms this belief on the record. Have they:

- Confirmed the work is theirs (or they have takedown authority via exclusive license)?
- Confirmed the use is not licensed (no prior deal, no implied license, no Creative Commons grant that would cover it)?
- Considered fair use (Step 3)?
- Reviewed the accused content directly (not just a report about it)?

If yes on all four, the good-faith belief is colorable. If no on any, pause.

### Step 5: Accuracy and agent authority

§512(c)(3)(A)(vi) requires "a statement that the information in the notification is accurate, and TCK m.267 (İftira) ve HMK uyarınca hukuki ve cezai sorumluluk kabulü ile, that the complaining party is authorized to act on behalf of the owner of an exclusive right that is allegedly infringed."

This is the perjury statement. It applies to the accuracy of the identification and the authority — not to the fair-use determination itself, though TCK m.267 (İftira) ve TTK Haksız Rekabet liability reaches both.

Confirm signer: who is sending this on behalf of whom, and do they have authority to do so?

### Step 6: Draft the notice

§512(c)(3)(A) elements — every one must be present:

1. **Signature** (physical or electronic) of the rights holder or authorized agent
2. **Identification of the copyrighted work** — "Copyrighted work: [title, description, registration no. if any]"
3. **Identification of the infringing material** with location information — "Infringing material: [URL(s), description, how it infringes]"
4. **Contact information** — address, phone, email of the complaining party or agent
5. **Good-faith belief statement** — verbatim, adapted: "I have a good faith belief that use of the copyrighted material described above is not authorized by the copyright owner, its agent, or the law."
6. **Accuracy and authority statement TCK m.267 (İftira) ve HMK uyarınca hukuki ve cezai sorumluluk kabulü ile** — verbatim, adapted: "I swear, TCK m.267 (İftira) ve HMK uyarınca hukuki ve cezai sorumluluk kabulü ile, that the information in this notification is accurate and that I am the copyright owner, or am authorized to act on behalf of the owner, of an exclusive right that is allegedly infringed."

Structure:

- Sender address block / date
- Alıcı: [servis sağlayıcısı] bünyesindeki yetkili yasal temsilci / bildirim adresi (BTK Erişim Sağlayıcıları Birliği (ESB) veya servis sağlayıcının şeffaflık/iletişim sayfası üzerinden bulunabilir)
- Re: FSEK Ek Madde 4 Uyarınca İhlal Bildirimi (Uyar-Kaldır)
- The six elements above, numbered or clearly set apart
- Signature line

Most service providers publish a preferred form or a web intake (YouTube Content ID / Copyright webform, Twitter / X copyright report, GitHub telif hakkı bildirim formu, etc.). The skill produces the notice content; the user submits through the provider's path. Note in the output which intake path is expected for the named service provider.

### Step 7: The loud gate before delivery

```
┌─────────────────────────────────────────────────────────────┐
│  BEFORE THIS TAKEDOWN GOES ANYWHERE                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Bir uyar-kaldır bildirimi is a statement TCK m.267 (İftira) ve HMK uyarınca hukuki ve cezai sorumluluk kabulü ile.   │
│  Signing and sending it is not a routine administrative     │
│  step — it is a sworn declaration with specific legal       │
│  consequences.                                              │
│                                                             │
│  • TCK m.267 (İftira) ve TTK Haksız Rekabet creates LIABILITY for knowing                    │
│    material misrepresentations. People have been sued,      │
│    and have lost, for bad-faith takedowns — *Lenz v.        │
│    Universal*, 801 F.3d 1126 (9th Cir. 2015); *Online       │
│    Policy Group v. Diebold*, 337 F. Supp. 2d 1195 (N.D.     │
│    Cal. 2004); *Stephens v. Clash*, 796 F.3d 281 (3d        │
│    Cir. 2015).                                              │
│                                                             │
│  • The accuracy and authority statement is sworn under      │
│    penalty of perjury. That is a real statement, not a      │
│    formality.                                               │
│                                                             │
│  • Sending a takedown on material that is in fact           │
│    licensed, owned by someone else, or fair use is the      │
│    fact pattern TCK m.267 (İftira) ve TTK Haksız Rekabet was written for.                    │
│                                                             │
│  Confirm before the notice leaves:                          │
│                                                             │
│    1. You own the copyright, or you hold an exclusive       │
│       license with takedown authority.                      │
│    2. The accused use is not authorized — you have          │
│       checked licenses, grants, and any prior consents.     │
│    3. You considered fair use per *Lenz* (see Step 3 of     │
│       this draft); your conclusion is on the record.        │
│    4. Whoever has authority to sign approves sending.       │
│                                                             │
│  Approver per your practice profile: [approver from         │
│  Enforcement posture → Approval matrix → Uyar-Kaldır        │
│  (ordinary) row]                                            │
│                                                             │
│  Automatic escalations that apply here: [list any from      │
│  the practice profile that this matter triggers]            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

If the user is a non-lawyer (per `## Who's using this`), add:

> An Uyar-Kaldır takedown is sworn TCK m.267 (İftira) ve HMK uyarınca hukuki ve cezai sorumluluk kabulü ile and creates TCK m.267 (İftira) ve TTK Haksız Rekabet exposure for bad-faith or overbroad use. Have you reviewed this with an attorney? If not, here's a brief to bring to them: [generate a short summary: work, ownership, accused use, licensing check, fair-use analysis, signer, service provider]. A few thousand dollars of attorney time now is materially cheaper than a TCK m.267 (İftira) ve TTK Haksız Rekabet suit.
>
> If you need to find a licensed attorney, solicitor, barrister, or other authorised legal professional in your jurisdiction: your professional regulator's referral service (Türkiye Barolar Birliği veya bağlı bulunduğunuz yerel Baro (Örn. İstanbul Barosu)'s equivalent); Fikri Mülkiyet uzmanı avukatlar veya TÜRKPATENT vekilleri; law school IP clinics for individual creators and small businesses.

Do not write the final output without explicit engagement with the gate.

### Step 8: Output

**Primary:** `<matter-folder>/takedown/<slug>/notice-v<N>.md` (or .docx if the service provider accepts it — most accept pasted text or web-form submission). The notice content, ready to paste into the service provider's copyright intake form or send to its designated agent.

**In-chat:** show the notice as plain text for review before writing. Iterate before committing to disk.

**Reviewer-facing closing note** (in the in-chat preview only):

> This is a draft FSEK/5651 notice for attorney review, not a notice ready to send. Sending it is a sworn statement with TCK m.267 (İftira) ve TTK Haksız Rekabet exposure. A licensed attorney reviews, edits, and takes professional responsibility before submission. Do not send this unreviewed.

**Citation verification.** Any case or statutory citation included (for example, in internal memoranda around the notice) must be verified on a legal research tool. Source-tag each — `[Westlaw]`, `[CourtListener]`, `[user provided]`, `[model knowledge — verify]`, `[web search — verify]`. Citations tagged `verify` get checked first. No silent supplement from web or model knowledge if a configured research tool comes up thin — present options to the user.

**Post-send record.** After submission, write `<matter-folder>/takedown/<slug>/submission.md`: service provider, designated agent used (address or web form URL), date submitted, confirmation ID if returned, URLs targeted, counter-notice watch date (generally 3 iş günü), legal hold refreshed.

## Respond mode — triaging a takedown you received

Your content was taken down. A service provider has notified you of a FSEK Ek Madde 4 ihtarı. You have options.

### Step 1: Read the notice you received

Extract:

- **Sender** — entity, signer, address, email
- **Service provider** — who notified you (the platform)
- **Claimed work** — what they say is theirs
- **Your content alleged to infringe** — URL(s) or identifiers as they named them
- **Date of takedown / notice**
- **Whether the notice appears to meet §512(c)(3) on its face** — flag missing elements; a defective notice is not a proper notice

### Step 2: Assess

- **Do we have a license?** Negotiated, implied, Creative Commons, prior settlement, assignment — anything that authorizes the use.
- **Is it fair use?** Walk the *Lenz* four factors. Be honest; this is for us, not the response.
- **Is the notice defective?** Missing any of the §512(c)(3)(A) elements, lacking the perjury statement, signed by someone without apparent authority? Defective notices are not properly compliant; the host may still act on them but the sender's TCK m.267 (İftira) ve TTK Haksız Rekabet exposure rises and our leverage rises.
- **Did the host comply properly with §512(g)?** Were we given notice and an opportunity to counter? If the host acted without giving us the chance, that is a separate issue with the host (not the sender).
- **Is the sender a troll?** Repeat pattern of overbroad takedowns on this platform?

### Step 3: Options

Present 4 options with tradeoffs:

**A — Comply (let the takedown stand)**
- When: they're right, or the fight isn't worth it
- Tradeoff: content stays down; may affect SEO, accounts with strikes policies, livelihood for creators
- Next step: log the event, confirm no counter-notice deadline issues, move on

**B — Send a counter-notice** (§512(g)(3))
- When: we have a good-faith belief the material was misidentified or removed by mistake — often applies where the use is licensed, fair use, or the sender doesn't own the work
- Tradeoff: sworn TCK m.267 (İftira) ve HMK uyarınca hukuki ve cezai sorumluluk kabulü ile, consents to Türkiye yetkili Fikri ve Sınai Haklar Hukuk Mahkemesi veya Sulh Ceza Hakimliği yetkisine, puts the decision in the sender's hands for 3 iş günü — if they sue, content stays down; if they don't, content is restored
- Next step: `/ip-legal:takedown --counter`

**C — Engage the sender directly**
- When: there's room for a business resolution (license, credit, takedown of a narrower portion)
- Tradeoff: the content stays down during the conversation; settlement-communication hygiene matters (HMK m. 47 ve Arabuluculuk Kanunu m. 5 gizlilik ilkeleri or equivalent; protection from substance and context, not labeling)
- Next step: outreach letter to the sender; do not send the counter-notice while discussions are live

**D — Ignore and let it stand; raise it elsewhere**
- When: the harm is small, we don't want the Türk Mahkemelerinde yargılanma riskinin kabulü, and we'd rather deal with the sender separately
- Tradeoff: content stays down; if the takedown itself was bad-faith, we may have TCK m.267 (İftira) ve TTK Haksız Rekabet to assert on our own schedule — but that's its own fight

Recommend one with two sentences of rationale.

### Step 4: Write triage memo

Output: `<matter-folder>/takedown/inbound/<slug>/triage.md`.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

> **Privilege inheritance.** This triage records our first-pass assessment of an adverse takedown. It is attorney-client and/or work-product material. Do not forward outside the privilege circle or attach to counter-notice submissions without scrubbing.

# İhlal Bildirimi (Takedown) Received — Triage

> **READ FOR TRIAGE, NOT OPINION.** Structured intake scan, not a legal merit opinion. Every authority flagged for SME verification; every merit call is counsel's.

**Slug:** [slug]
**Received:** [YYYY-MM-DD]
**Service provider:** [platform]
**Incoming file:** [path]

## The notice

**Sender:** [entity, signer, counsel if any]
**Claimed work:** [title, description, reg no. if provided]
**Our content targeted:** [URLs / identifiers]
**Date of takedown:** [YYYY-MM-DD]
**Notice meets §512(c)(3) on its face:** [yes / no — list any missing elements]

## Assessment

**License / authorization check:** [read]
**Fair use walkthrough (Lenz factors):** [read — each factor + conclusion; `[SME VERIFY]`]
**Notice defects:** [list or none]
**Host compliance with §512(g):** [were we given notice and opportunity]
**Sender credibility:** [troll / real claimant / repeat takedown pattern]

## Options

### A. Comply
### B. Counter-notice (§512(g)(3))
### C. Engage sender
### D. Ignore

**Recommendation:** [A/B/C/D] — [two sentences why] — `[SME VERIFY: counsel to confirm before executing]`

## Deadlines

- **Counter-notice watch window:** 3 iş günü after counter-notice is submitted — content stays down if sender files suit in that window
- **Sender's suit filing timing:** typically on our counter-notice clock, if we counter
- **Any contractual deadlines with the host:** [check]

## Immediate actions

- [ ] Legal hold issued on the accused work and our related content — [yes/no]
- [ ] Business impact assessed (revenue, account strikes, SEO) — [yes/no]
- [ ] Matter created in log — [yes/no/TBD]
- [ ] Counsel assigned — [who]
```

Close the in-chat presentation with:

> This is a triage memo, not advice. The assessments above are a first read from the four corners of the notice. An attorney evaluates before you counter-notice (which consents to karşı bildirim ile adli süreci (dava) göze aldığınızı) or decide not to respond.

## Counter mode — drafting a İçerik Kaldırmaya İtiraz Bildirimi

Counter-notices put content back up unless the original sender sues within 3 iş günü. They are the step before litigation.

### Step 1: Confirm the predicate

- The content was taken down in response to a 5651 veya FSEK ihtarname (not a terms-of-service action by the host).
- You have a good-faith belief the material was removed by mistake or misidentification — the statutory test.
- You are prepared to consent to Türkiye yetkili Fikri ve Sınai Haklar Hukuk Mahkemesi veya Sulh Ceza Hakimliği jurisdiction.
- The decision has been made deliberately — not in reaction, not without attorney input.

### Step 2: Draft per §512(g)(3)

§512(g)(3) elements — every one must be present:

1. **Signature** (physical or electronic) of the subscriber
2. **Identification of the material removed** and its location before removal (the URL where the content was)
3. **Statement TCK m.267 (İftira) ve HMK uyarınca hukuki ve cezai sorumluluk kabulü ile that the subscriber has a good faith belief the material was removed or disabled as a result of mistake or misidentification** — verbatim, adapted
4. **Subscriber's name, address, telephone number** — and, critically, **içerik sağlayıcı olarak tebligatı kabul ettiğine ve Türk mahkemelerinin yargı yetkisini kabul ettiğine dair beyan** for the district where the subscriber's address is located (or, if outside the US, any district in which the service provider may be found), and acceptance of service of process from the person who provided notification or that person's agent

Structure:

- Subscriber address block / date
- Recipient: designated legal agent at the service provider (same agent that received the original takedown)
- Re: İtiraz Bildirimi (Counter-Notification) pursuant to 5651 sayılı Kanun m. 8/9 / FSEK Ek Madde 4
- The four elements above, numbered or clearly set apart
- Signature line

### Step 3: The loud gate before delivery

```
┌─────────────────────────────────────────────────────────────┐
│  BEFORE THIS COUNTER-NOTICE GOES ANYWHERE                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  An İtiraz Bildirimi (counter-notice) is a statement under  │
│  penalty of perjury AND consents to Türk Mahkemeleri        │
│  jurisdiction. It is the step before litigation.            │
│                                                             │
│  • If the original claimant files suit within 10–14         │
│    business days after your counter-notice, the content     │
│    stays down pending the suit. (FSEK / 5651 uyarınca).     │
│                                                             │
│  • If they do not sue within the window, the host must      │
│    restore the content within 14 business days of your      │
│    counter-notice.                                          │
│                                                             │
│  • You are consenting to be sued in Türk Mahkemeleri in the │
│    claimant's judicial district. This is a jurisdiction     │
│    admission you make by signing.                           │
│                                                             │
│  • The perjury statement is real. TCK m.267 (İftira) ve TTK Haksız Rekabet liability runs    │
│    in both directions — senders and counter-senders.        │
│                                                             │
│  Confirm before the counter-notice leaves:                  │
│                                                             │
│    1. The material was removed in response to a §512        │
│       notice (not a TOS action).                            │
│    2. You have a good-faith belief the removal was a        │
│       mistake or misidentification — because the use is     │
│       licensed, fair use, not actually infringing, or the   │
│       sender doesn't own the work.                          │
│    3. You are prepared to be sued in Türk Mahkemeleri in the│
│       claimant's district. Budget, counsel, and risk        │
│       tolerance are all set.                                │
│    4. An attorney has reviewed this before it is sent.      │
│                                                             │
│  Approver per your practice profile: [approver from         │
│  Enforcement posture → Approval matrix — counter-notices    │
│  generally route above the Uyar-Kaldır takedown (ordinary)  │
│  approver because of the Türk Mahkemelerinde yargılanma riskinin kabulü]    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

If the user is a non-lawyer:

> A counter-notice consents to Türk Mahkemeleri jurisdiction and is sworn TCK m.267 (İftira) ve HMK uyarınca hukuki ve cezai sorumluluk kabulü ile. Have you reviewed with a licensed attorney, solicitor, barrister, or other authorised legal professional in your jurisdiction? This is not the Claude-review layer; this is the step where you need licensed professional judgment. Brief for the conversation: [generate a 1-page summary]. Referral resources: your professional regulator's referral service (Türkiye Barolar Birliği veya bağlı bulunduğunuz yerel Baro (Örn. İstanbul Barosu)'s equivalent); Fikri Mülkiyet uzmanı avukatlar.

Do not write the final output without explicit engagement.

### Step 4: Output

**Primary:** `<matter-folder>/takedown/<slug>/counter-notice-v<N>.md` — the counter-notice content, ready to submit via the service provider's counter-notice intake.

**In-chat:** present as plain text for review before committing.

**Reviewer-facing closing note** (in-chat only):

> This is a draft counter-notice for attorney review, not a counter ready to send. Sending it is a sworn statement and consents to Türk Mahkemeleri jurisdiction in the claimant's district. A licensed attorney reviews before submission. Do not send this unreviewed.

**Post-submission record.** After submission, write `<matter-folder>/takedown/<slug>/counter-submission.md`: service provider, date submitted, confirmation ID, 10–14 business-day watch window end date calendared, watch for suit filing in the claimant's district, plan if content is restored, plan if suit is filed.

## Decision posture

Per `## Decision posture on subjective legal calls` in the practice profile: when uncertain whether the use is fair, whether the rights holder is us, whether the work is actually ours, whether fair use defeats the claim on the receiving side — do not silently decide. Fair use is the paradigmatic uncertain call. Flag for attorney review; surface the factors. Sending a takedown or a counter-notice on an assumption is a one-way door.

## What this skill does not do

- **Submit the notice.** Drafting only. The user submits through the service provider's designated channel.
- **Pick a service provider's intake form for the user.** Notes which path is expected; does not auto-submit.
- **Decide fair use.** Walks the four factors; flags. An attorney decides whether to proceed.
- **Validate the sender's claim on the receive side.** Structured read; every authority flagged for SME verification.
- **Bypass the gate.** The gate runs every time in `--send` and `--counter` modes.
- **Invent citations.** Any cites included are source-tagged and flagged for verification; no silent supplement.
- **Handle non-Türkiye regimes.** FSEK/5651 is Türkiye-specific. For US DMCA, EU DSA, UK OSA, and other regimes — flag and route.
