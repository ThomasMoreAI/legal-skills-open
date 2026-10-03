---
name: takedown-bossmann007
title: /takedown
description: Draft a notificação de retirada de conteúdo (Marco Civil), triage one you received, or draft a resposta/contranotificação. Use when asserting copyright under Lei 9.610/1998 through a Marco Civil notice with the fair-use-analog and good-faith gates, when an incoming notice needs triage into comply / contest / engage / ignore options, or when drafting a response with the litigation-risk gate. Marco Civil art. 19/21 first; DMCA is a gated US-provider fallback.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/ip-legal/skills/takedown
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: ip
language: en
---

# /takedown

Three modes. Pick one:

- `/ip-legal:takedown --send` — draft a notificação de retirada de conteúdo under Marco Civil (Lei 12.965/2014 art. 19/21) + Lei 9.610/1998. Limitations/exceptions gate + loud litigation-risk gate before delivery.
- `/ip-legal:takedown --respond` — triage a notice someone sent you. Options: comply / contest / engage / ignore.
- `/ip-legal:takedown --counter` — draft a resposta/contranotificação to a platform or notifier. Loud gate for the litigation-exposure admission and the good-faith statement.

## Instructions

1. **Read the practice profile.** Load `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. If it contains `[PLACEHOLDER]` markers or does not exist, stop and say: "This plugin needs setup before it can give you useful output. Run `/ip-legal:cold-start-interview` — the takedown skill depends on your approval matrix and practice profile."

2. **Check matter workspaces.** Per `## Matter workspaces`: if `Enabled` is `✗`, skip. If enabled and there is no active matter, ask: "Which matter is this for? Run `/ip-legal:matter-workspace switch <slug>` or say `practice-level`."

3. **Dispatch on `$ARGUMENTS`:**
   - `--send` → run send mode (below). Walk identify-the-work, identify-the-infringing-material, limitations/exceptions gate (Lei 9.610/1998 art. 46-48), good-faith belief, accuracy/authority, choose the channel (ToS notice vs. notificação extrajudicial vs. tutela de urgência), draft the notice, run the loud gate, write output.
   - `--respond` → run respond mode (below). Read the incoming notice, assess (license, limitations/exceptions, defects, whether art. 19 requires a court order at all, notifier credibility), present the four options, recommend, write the triage memo.
   - `--counter` → run counter mode (below). Confirm the predicate (content removed via ToS/platform notice, good-faith belief the removal was mistaken/misidentified, ready for the litigation exposure, attorney in the loop), draft the resposta/contranotificação, run the loud gate, write output.
   - No flag → ask once: "Are we sending a notificação de retirada, triaging one we received, or drafting a response/contranotificação?"

4. **Respect the gates.** In `--send` and `--counter`, the loud gate runs before any final output is written. The limitations/exceptions gate in `--send` is separate and runs earlier; "debatable" or "likely covered by a limitation (art. 46-48)" stops the draft and routes to attorney review.

5. **Jurisdiction note.** The Marco Civil regime (Lei 12.965/2014 art. 19/21) governs content hosted by providers reachable under Brazilian jurisdiction. Under **art. 19**, the general rule is that a provider is only civilly liable for third-party content after failing to comply with a **specific court order** — an extrajudicial notice does not, by itself, compel removal. Under **art. 21**, non-consensual nudity or private sexual acts are the express exception: notification by the victim (or legal representative) is enough to trigger provider liability. If the provider sits under **US jurisdiction only** (US-hosted, no Brazilian presence), the DMCA path in the gated fallback section may be the effective instrument instead of — or alongside — the Brazilian route. [verified: https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm]

6. **Hand off where appropriate.** `--respond` with a contest recommendation chains into `/ip-legal:takedown --counter` — but only after the triage memo has been reviewed and the decision to contest has been made deliberately.

## Examples

```
/ip-legal:takedown --send
/ip-legal:takedown --respond ~/Downloads/youtube-notificacao.pdf
/ip-legal:takedown --counter
/ip-legal:takedown
```

## Notes

- The outgoing notice and response do not carry the confidentiality header. Internal drafts, limitations analyses, and triage memos do.
- Marco Civil art. 19 sets a court-order-first rule; art. 21 is the narrow exception. Getting the channel wrong (extrajudicial where a court order is needed, or vice versa) wastes leverage.
- A notificação extrajudicial preserves evidence and starts the clock, but under art. 19 it generally does not compel a provider to remove ordinary content — a tutela de urgência (CPC art. 300) usually does. This is not a formality.
- Non-lawyer users get a one-page brief for the attorney conversation before the gate clears — particularly important where a tutela de urgência or an abuse-of-notification exposure is in play.

---

## Purpose

The Brazilian notice-and-action system under the Marco Civil da Internet (Lei 12.965/2014) is deliberately court-order-centric, and consequential when misused. A notificação extrajudicial is a formal assertion of a right that preserves evidence and starts a record; under art. 19 it generally does not, by itself, compel a provider to remove ordinary content — that ordinarily requires a specific court order (often via tutela de urgência, CPC art. 300). Art. 21 is the express exception: for non-consensual nudity or private sexual acts, a victim's notification is enough. A response/contranotificação puts contested content back in play and can precipitate litigation. This skill handles all three moves with the guardrails each warrants.

Three modes:

- `--send` — draft a notificação de retirada de conteúdo (ToS notice / notificação extrajudicial / tutela de urgência as appropriate)
- `--respond` — triage a notice someone sent you; produce options
- `--counter` — draft a resposta/contranotificação

If the user does not pass a flag, ask once: "Are we sending a notificação de retirada, triaging one we received, or drafting a response/contranotificação?"

> **External deliverables (send and counter modes):** the outgoing notice/response goes to the provider (via ToS channel) or to the counterparty (notificação extrajudicial). Do NOT include the `CONFIDENCIAL — SIGILO PROFISSIONAL` header on the outgoing document — a notice sent to a third party is not a sigiloso communication and marking it as such creates a discardable admission. Internal drafts, pre-send briefs, limitations analyses, and triage memos keep the header per plugin config `## Outputs`.

## Jurisdiction assumption

The Marco Civil da Internet (**Lei 12.965/2014**) governs provider liability for third-party content in Brazil. The two load-bearing articles: [verified: https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm]

- **Art. 19 — general rule.** A connection/application provider is civilly liable for third-party content only if, **after a specific court order** identifying the content, it fails to make it unavailable. An extrajudicial notice does not trigger liability for ordinary content; a court order (typically a tutela de urgência, CPC art. 300) is the instrument that compels removal. `[settled — last confirmed 2026-07-02]`
- **Art. 21 — exception.** For content containing **nudity or private sexual acts** disclosed without the participant's consent, the provider is subsidiarily liable if, **after notification by the participant or their legal representative**, it does not act diligently to remove it. Here a notification — not a court order — is the trigger. `[settled — last confirmed 2026-07-02]`

Copyright subsistence and moral/patrimonial rights are governed by **Lei 9.610/1998**. Platform ToS channels frequently offer a faster practical route than either the notice or the court order. If the provider sits under **US jurisdiction only** (US-hosted, no Brazilian presence and no submission to Brazilian courts), the DMCA path in the gated fallback below may be the effective instrument. Copyright subsistence is Berne-multilateral; enforcement mechanics are jurisdiction-specific.

## Load context

- `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` → `## Perfil de prática (PI)` (direito autoral ownership if any), `## Postura de enforcement` → `Notificação de retirada de conteúdo (ordinária)` row, `## Outputs` (confidentiality header, role), `## Who's using this` (role — lawyer vs. non-lawyer)
- **Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (in-house default), skip matter machinery. If enabled and no active matter, ask: "Which matter? Run `/ip-legal:matter-workspace switch <slug>` or say `practice-level`." Write outputs to the active matter's folder at `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/takedown/<slug>/` (or `takedown/<slug>/` at practice level). Never read another matter's files unless `Cross-matter context` is `on`.

## Send mode — drafting a notificação de retirada de conteúdo

### Step 1: Identify the copyrighted work

> What is the copyrighted work?
>
> - **Title / description** — what is the work (software, image, text, video, audio)?
> - **Ownership / titularidade** — do you hold the patrimonial rights outright, or an exclusive license with authority to act? Copyright arises on creation under Lei 9.610/1998 — no registration is required to hold the right or to notify. Optional registration (e.g., Biblioteca Nacional, INPI for software) is evidentiary, not constitutive. `[settled — last confirmed 2026-07-02]`
> - **Prior licensing** — have you ever licensed this use, or a broader use that might cover it?

Ownership and authority are the first things an abuse-of-notification / bad-faith challenge looks at. Get them clearly on the record before drafting.

### Step 2: Identify the infringing material and its location

> Where is the infringing material?
>
> - **Platform / provider** — YouTube, X, Instagram, GitHub, Mercado Livre, a web host, etc.
> - **URL(s)** — specific permalinks to the infringing material. One notice can cover multiple URLs if they're all on the same service.
> - **Description** — what is the infringing material and how does it infringe (verbatim copy, substantially similar, unauthorized derivative)?
> - **Screenshots / evidence** — preserved with timestamp and URL visible; an ata notarial can harden this for later court use

Under Marco Civil art. 19 § 1º, a court order must identify the content **clara e especificamente** (clear and specific location) to be enforceable. A notice or petition that cannot locate the material precisely fails at the court-order stage. Be precise.

### Step 3: Limitations and exceptions gate

Before asserting the right, walk the limitations of Lei 9.610/1998 (arts. 46-48) — the Brazilian analog to fair use, though it is a **closed list of enumerated exceptions**, not an open standard. Sending a notice against a use that falls inside a statutory limitation is the abuse-of-right exposure (Código Civil art. 187).

Ask:

> Before we draft, walk the limitations of Lei 9.610/1998 art. 46-48 — even if the conclusion is "not covered." Consider in particular:
>
> 1. **Art. 46** — reproduction for criticism/comment, news reporting, quotation (citação) within limits, private single-copy for the copier's own use, use in classrooms, accessibility copies, and similar enumerated uses.
> 2. **Art. 47** — paraphrases and parodies that are not true reproductions and do not discredit the work.
> 3. **Art. 48** — works permanently in public places.
> 4. **Purpose and market effect** — does the use compete with or substitute for the original? (Not a statutory factor as in the US, but relevant to whether a court will treat it as abusive infringement.)
>
> Your read on each? And your conclusion — outside any limitation, debatable, likely covered?

Record the answer in the notice file. If "debatable" or "likely covered," do not draft. Stop and route to attorney review: "This use may fall within a Lei 9.610/1998 limitation. Notifying against a lawful use is abuse of right (CC art. 187) and can invert the exposure onto us. Route this to counsel before any notice goes out." `[review]`

### Step 4: Good-faith belief

The notifier asserts, in good faith, that the use is unauthorized and unlawful. A false or reckless assertion supports an abuse-of-notification / abuso de direito claim (CC art. 187) and possible danos morais. [verified: https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm]

The sender forms this belief on the record. Have they:

- Confirmed the work is theirs (or they hold an exclusive license with authority to act)?
- Confirmed the use is not licensed (no prior deal, no implied license, no Creative Commons or open grant that would cover it)?
- Considered the art. 46-48 limitations (Step 3)?
- Reviewed the accused content directly (not just a report about it)?

If yes on all four, the good-faith belief is colorable. If no on any, pause.

### Step 5: Accuracy and authority

The notice (and any petition for a tutela de urgência) rests on the accuracy of the identification and the notifier's authority to act on behalf of the rights holder. Misstatements expose the notifier to abuse-of-right and litigation-cost consequences; a petition also carries the litigant's duty of good faith (CPC art. 5º) and can attract litigância de má-fé (CPC art. 80) if abusive.

Confirm signer: who is sending this on behalf of whom, and do they have authority (procuração where a lawyer signs) to do so?

### Step 6: Draft the notice

Choose the channel first, then draft. The three channels, in rising order of force:

- **ToS / platform channel** — the provider's own copyright/abuse form. Fastest practical route; the provider acts under its own policy, not under a legal compulsion. Good first move for straightforward infringement.
- **Notificação extrajudicial** — a formal notice to the counterparty (and/or provider). Preserves evidence, starts a record, constitutes the party in mora. Under art. 19 it generally does **not** compel a provider to remove ordinary content, but it is the predicate step and can resolve matters without court. For art. 21 content (non-consensual intimate imagery), the notification itself triggers provider liability.
- **Tutela de urgência (CPC art. 300)** — a petition for an urgent judicial order. This is the instrument that produces the art. 19 court order compelling removal of ordinary content. Requires probabilidade do direito + perigo de dano. Drafted with counsel; filed by an advogado.

Elements common to the notificação extrajudicial — each must be present:

1. **Signature** of the rights holder or authorized representative (advogado with procuração where applicable)
2. **Identification of the copyrighted work** — "Obra: [title, description, any registration]"
3. **Identification of the infringing material** with clear and specific location — "Conteúdo infrator: [URL(s), description, how it infringes]"
4. **Contact / qualificação** — full identification and address of the notifier or representative
5. **Statement of the right and its violation** — the patrimonial/moral right under Lei 9.610/1998 and how the use violates it
6. **Demand and deadline** — the specific act requested (removal, cessation) and a reasonable prazo, with notice that non-compliance will lead to a tutela de urgência (CPC art. 300) and indemnification claims (Lei 9.610/1998 arts. 102-107)

Structure:

- Notifier qualificação block / date
- Recipient: the counterparty and/or the provider's designated legal/abuse contact
- Assunto: Notificação extrajudicial — violação de direito autoral (Lei 9.610/1998; Marco Civil, Lei 12.965/2014)
- The six elements above, numbered or clearly set apart
- Signature line

Most providers publish a preferred abuse/copyright form or web intake. The skill produces the notice content; the user submits through the provider's path or serves the extrajudicial notice. Note in the output which channel is expected and whether art. 21 changes the analysis.

> **Gated fallback — US-jurisdiction providers.** If the provider is US-hosted with no Brazilian presence and does not submit to Brazilian courts, the Brazilian notice may reach no one with power to act. In that case the **DMCA §512(c)(3)** notice-and-takedown path may be the effective instrument. The DMCA notice is a sworn statement under penalty of perjury and carries §512(f) exposure for material misrepresentations (*Lenz v. Universal Music Corp.*, 801 F.3d 1126 (9th Cir. 2015) `[settled — last confirmed 2026-07-02]`). Its elements: signature; identification of the work; identification and location of the infringing material; contact info; good-faith-belief statement; and an accuracy-and-authority statement under penalty of perjury. Recipient is the provider's designated agent (Copyright Office DMCA Designated Agent Directory, `https://www.copyright.gov/dmca-directory/`). Use this ONLY when the Brazilian route cannot reach the provider — it is a US-footprint fallback, not the default. `[review]`

### Step 7: The loud gate before delivery

```
┌─────────────────────────────────────────────────────────────┐
│  BEFORE THIS NOTICE GOES ANYWHERE                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  A notificação de retirada is a formal assertion of a       │
│  right. Signing and sending it is not a routine             │
│  administrative step — it has specific legal                │
│  consequences.                                              │
│                                                             │
│  • Notifying against a lawful use is ABUSE OF RIGHT         │
│    (Código Civil art. 187) and can generate liability       │
│    for danos morais and materiais. The exposure runs        │
│    against the notifier, not the target.                    │
│                                                             │
│  • Under Marco Civil art. 19, an extrajudicial notice       │
│    generally does NOT compel removal of ordinary content    │
│    — that needs a specific court order (tutela de           │
│    urgência, CPC art. 300). Art. 21 (non-consensual         │
│    intimate imagery) is the narrow exception where          │
│    notification alone triggers provider liability.          │
│                                                             │
│  • A petition for a tutela de urgência carries the          │
│    litigant's good-faith duty (CPC art. 5º) and             │
│    litigância de má-fé exposure (CPC art. 80) if abusive.   │
│                                                             │
│  • Notifying on material that is in fact licensed, owned    │
│    by someone else, or covered by a Lei 9.610/1998          │
│    limitation (art. 46-48) is the fact pattern the          │
│    abuse-of-right doctrine catches.                         │
│                                                             │
│  Confirm before the notice leaves:                          │
│                                                             │
│    1. You hold the patrimonial right, or an exclusive       │
│       license with authority to act.                        │
│    2. The accused use is not authorized — you have          │
│       checked licenses, grants, and any prior consents.     │
│    3. You walked the art. 46-48 limitations (see Step 3     │
│       of this draft); your conclusion is on the record.     │
│    4. You picked the right channel (ToS / extrajudicial /   │
│       tutela de urgência) for what you actually need.       │
│    5. Whoever has authority to sign approves sending.       │
│                                                             │
│  Approver per your practice profile: [approver from         │
│  Postura de enforcement → tabela → Notificação de           │
│  retirada de conteúdo (ordinária) row]                      │
│                                                             │
│  Automatic escalations that apply here: [list any from      │
│  the practice profile that this matter triggers]            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

If the user is a non-lawyer (per `## Who's using this`), add:

> A notificação de retirada is a formal assertion of a right and creates abuse-of-right exposure (Código Civil art. 187) for bad-faith or overbroad use — and compelling removal of ordinary content requires a court order (tutela de urgência, CPC art. 300), not a letter. Have you reviewed this with an advogado inscrito na OAB? If not, here's a brief to bring to them: [generate a short summary: work, ownership, accused use, licensing check, art. 46-48 limitations analysis, channel chosen, signer, provider]. A few thousand reais of attorney time now is materially cheaper than an abuse-of-right suit.
>
> If you need to find an advogado inscrito na OAB: your local OAB seccional's serviço de referência/indicação, the OAB's comissões de propriedade intelectual, or núcleos de prática jurídica / clínicas de PI at law schools for individual creators and small businesses.

Do not write the final output without explicit engagement with the gate.

### Step 8: Output

**Primary:** `<matter-folder>/takedown/<slug>/notice-v<N>.md` (or .docx). The notice content, ready to serve as a notificação extrajudicial, paste into the provider's abuse/copyright intake, or hand to counsel as the predicate for a tutela de urgência petition.

**In-chat:** show the notice as plain text for review before writing. Iterate before committing to disk.

**Reviewer-facing closing note** (in the in-chat preview only):

> This is a draft notice for attorney review, not a notice ready to serve. Sending it is a formal assertion of a right with abuse-of-right exposure (CC art. 187), and compelling removal of ordinary content requires a court order (tutela de urgência, CPC art. 300). An advogado inscrito na OAB reviews, edits, and takes professional responsibility before service. Do not send this unreviewed. [verified: https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm; https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]

**Citation verification.** Any case or statutory citation included (for example, in internal memoranda around the notice) must be verified on a legal research tool. Source-tag each — `[JusBrasil]`, `[Escavador]`, `[PJe]`, `[user provided]`, `[model knowledge — verify]`, `[web search — verify]`. Citations tagged `verify` get checked first. No silent supplement from web or model knowledge if a configured research tool comes up thin — present options to the user.

**Post-send record.** After service/submission, write `<matter-folder>/takedown/<slug>/submission.md`: provider or counterparty, channel used (ToS form URL, AR do correio / cartório de títulos e documentos, or protocolo judicial), date sent, confirmation/protocolo if returned, URLs targeted, prazo given for compliance, next-step date to escalate to tutela de urgência if ignored, legal hold refreshed.

## Respond mode — triaging a notice you received

Your content was taken down, or you received a notificação extrajudicial demanding removal. You have options — and under Marco Civil art. 19, an extrajudicial demand generally does not compel anything absent a court order.

### Step 1: Read the notice you received

Extract:

- **Sender** — entity, signer, advogado (and procuração?), address, email
- **Provider** — who acted or notified you (the platform), if any
- **Claimed work** — what they say is theirs
- **Your content alleged to infringe** — URL(s) or identifiers as they named them
- **Date of removal / notice**
- **Channel and legal basis** — is this a bare extrajudicial notice (art. 19: no obligation to remove absent a court order), an art. 21 notification, or an actual court order (mandado/decisão)? This is the pivotal question.

### Step 2: Assess

- **Do we have a license?** Negotiated, implied, Creative Commons, prior settlement, cessão — anything that authorizes the use.
- **Is it covered by a limitation?** Walk Lei 9.610/1998 art. 46-48 (criticism, quotation, parody, public-place works, private copy). Be honest; this is for us, not the response.
- **Is there actually a binding order?** Under art. 19, only a specific court order compels removal of ordinary content. If the sender sent a mere extrajudicial notice, the provider had no obligation to act and neither do you — leverage is on your side. If it is an art. 21 case (non-consensual intimate imagery), notification alone is enough and the analysis flips.
- **Is the notice/petition defective or abusive?** Vague content identification (fails art. 19 § 1º specificity), no rights ownership shown, or plainly against a lawful use — that raises the sender's abuse-of-right (CC art. 187) exposure and our leverage.
- **Is the sender a troll?** Repeat pattern of overbroad extrajudicial notices?

### Step 3: Options

Present 4 options with tradeoffs:

**A — Comply (let the removal stand)**
- When: they're right, it's an art. 21 case, or the fight isn't worth it
- Tradeoff: content stays down; may affect reach, monetized accounts, livelihood for creators
- Next step: log the event, confirm no deadline issues, move on

**B — Contest (resposta/contranotificação; restore request)**
- When: we have a good-faith belief the removal was mistaken or misidentified — often where the use is licensed, covered by an art. 46-48 limitation, or the sender doesn't own the work; and there is no binding court order
- Tradeoff: signals we will defend; if the sender then seeks a tutela de urgência (CPC art. 300), the dispute moves to court and content may stay down pending decision
- Next step: `/ip-legal:takedown --counter`

**C — Engage the sender directly**
- When: there's room for a business resolution (license, credit, removal of a narrower portion)
- Tradeoff: content status holds during the conversation; keep settlement-communication hygiene (tratativas/proposta de acordo are generally protected from being used as admission)
- Next step: outreach letter to the sender; do not send the contranotificação while discussions are live

**D — Ignore and let it stand; raise it elsewhere**
- When: the harm is small, there is no court order, and we'd rather deal with the sender separately
- Tradeoff: content status holds; if the notice itself was bad-faith, we may have an abuse-of-right (CC art. 187) / danos morais claim to assert on our own schedule — but that's its own fight

Recommend one with two sentences of rationale.

### Step 4: Write triage memo

Output: `<matter-folder>/takedown/inbound/<slug>/triage.md`.

```markdown
[CONFIDENTIALITY HEADER — per plugin config ## Outputs]

> **Sigilo inheritance.** This triage records our first-pass assessment of an adverse notice. Where prepared under advogado supervision it is coberto por sigilo profissional (Estatuto OAB). Do not forward outside the sigilo circle or attach to contranotificação submissions without scrubbing.

# Notificação de retirada recebida — Triage

> **READ FOR TRIAGE, NOT OPINION.** Structured intake scan, not a legal merit opinion. Every authority flagged for SME verification; every merit call is counsel's.

**Slug:** [slug]
**Received:** [YYYY-MM-DD]
**Provider:** [platform]
**Incoming file:** [path]

## The notice

**Sender:** [entity, signer, advogado if any]
**Claimed work:** [title, description, any registration]
**Our content targeted:** [URLs / identifiers]
**Date of removal / notice:** [YYYY-MM-DD]
**Legal basis / channel:** [bare extrajudicial notice (art. 19 — no removal duty absent court order) / art. 21 notification / actual court order — flag which]

## Assessment

**License / authorization check:** [read]
**Limitations walkthrough (Lei 9.610/1998 art. 46-48):** [read — each relevant limitation + conclusion; `[SME VERIFY]`]
**Binding order present?:** [art. 19 court order / art. 21 notification / none — bare notice]
**Notice defects / abuse signals:** [vague identification, no ownership shown, against lawful use → CC art. 187 exposure; or none]
**Sender credibility:** [troll / real claimant / repeat notice pattern]

## Options

### A. Comply
### B. Contest (resposta/contranotificação)
### C. Engage sender
### D. Ignore

**Recommendation:** [A/B/C/D] — [two sentences why] — `[SME VERIFY: counsel to confirm before executing]`

## Deadlines

- **Prazo in the notice, if any:** [date the sender demanded action by]
- **Risk of tutela de urgência filing:** [if we contest/ignore, sender may seek a court order — content may stay down pending decision]
- **Any contractual deadlines with the provider:** [check]

## Immediate actions

- [ ] Legal hold issued on the accused work and our related content — [yes/no]
- [ ] Business impact assessed (revenue, account status, reach) — [yes/no]
- [ ] Matter created in log — [yes/no/TBD]
- [ ] Counsel assigned — [who]
```

Close the in-chat presentation with:

> This is a triage memo, not advice. The assessments above are a first read from the four corners of the notice. An advogado evaluates before you contest, engage, or decide not to respond — especially the art. 19-vs-art. 21 call, which changes whether the sender can compel anything.

## Counter mode — drafting a resposta/contranotificação

A resposta/contranotificação contests the removal and asks the provider to restore, or answers the notifier's demand. It signals you will defend — and can precipitate the notifier's move to a tutela de urgência (CPC art. 300). It is the step before litigation.

### Step 1: Confirm the predicate

- The content was removed via a provider/ToS action or a bare extrajudicial notice — **not** an already-binding court order (if there is a court order, the path is judicial defense, not a contranotificação).
- You have a good-faith belief the removal was a mistake or misidentification — because the use is licensed, covered by a Lei 9.610/1998 limitation (art. 46-48), not actually infringing, or the notifier doesn't own the work.
- You are prepared for the notifier to escalate to a tutela de urgência in the competent Brazilian court (and, if the facts are cross-border, for a jurisdiction fight).
- The decision has been made deliberately — not in reaction, not without attorney input.

### Step 2: Draft the resposta/contranotificação

Elements — each must be present:

1. **Signature** of the subscriber or authorized representative (advogado with procuração where applicable)
2. **Identification of the material removed** and its location before removal (the URL where the content was)
3. **Statement of good-faith belief that the removal was mistaken or a misidentification** — with the concrete basis (license, art. 46-48 limitation, non-ownership by the notifier)
4. **Subscriber qualificação** — name, address, contact — and a request that the provider restore the content or, at minimum, provide the notifier's identification so the dispute can proceed; note willingness to submit the matter to the competent Brazilian court if the notifier persists

Structure:

- Subscriber qualificação block / date
- Recipient: the provider's legal/abuse contact (and/or the original notifier)
- Assunto: Resposta a notificação / pedido de restabelecimento de conteúdo (Marco Civil, Lei 12.965/2014; Lei 9.610/1998)
- The four elements above, numbered or clearly set apart
- Signature line

### Step 3: The loud gate before delivery

```
┌─────────────────────────────────────────────────────────────┐
│  BEFORE THIS RESPONSE GOES ANYWHERE                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  A resposta/contranotificação signals you will defend       │
│  the content. It is the step before litigation.             │
│                                                             │
│  • If the notifier responds by seeking a tutela de          │
│    urgência (CPC art. 300) and obtains it, the content      │
│    stays down under the resulting art. 19 court order       │
│    pending the merits.                                      │
│                                                             │
│  • If the notifier does not escalate, engaging the          │
│    provider to restore is the practical route — providers   │
│    act under their own policy, not a legal compulsion.      │
│                                                             │
│  • You may be litigating in the competent Brazilian         │
│    court. If the facts are cross-border, expect a           │
│    jurisdiction/competência fight before the merits.        │
│                                                             │
│  • Abuse-of-right exposure (CC art. 187) runs in BOTH       │
│    directions — a bad-faith contranotificação against a     │
│    legitimate removal carries its own risk.                 │
│                                                             │
│  Confirm before the response leaves:                        │
│                                                             │
│    1. The material was removed via provider/ToS action or   │
│       a bare notice (not an existing court order).          │
│    2. You have a good-faith belief the removal was a        │
│       mistake or misidentification — the use is licensed,   │
│       covered by an art. 46-48 limitation, not              │
│       infringing, or the notifier doesn't own the work.     │
│    3. You are prepared for the notifier to seek a tutela    │
│       de urgência. Budget, counsel, and risk tolerance      │
│       are all set.                                          │
│    4. An advogado has reviewed this before it is sent.      │
│                                                             │
│  Approver per your practice profile: [approver from         │
│  Postura de enforcement → tabela — responses generally      │
│  route above the Notificação de retirada (ordinária)        │
│  approver because of the litigation exposure]               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

If the user is a non-lawyer:

> A resposta/contranotificação can precipitate litigation and carries its own abuse-of-right exposure (CC art. 187). Have you reviewed with an advogado inscrito na OAB? This is not the Claude-review layer; this is the step where you need licensed professional judgment. Brief for the conversation: [generate a 1-page summary]. Referral resources: your local OAB seccional's serviço de indicação; the OAB's comissões de propriedade intelectual; núcleos de prática jurídica / clínicas de PI at law schools.

Do not write the final output without explicit engagement.

### Step 4: Output

**Primary:** `<matter-folder>/takedown/<slug>/counter-notice-v<N>.md` — the response content, ready to submit via the provider's channel or serve on the notifier.

**In-chat:** present as plain text for review before committing.

**Reviewer-facing closing note** (in-chat only):

> This is a draft response for attorney review, not a response ready to send. Sending it signals you will defend and can precipitate a tutela de urgência (CPC art. 300). An advogado inscrito na OAB reviews before submission. Do not send this unreviewed.

**Post-submission record.** After submission, write `<matter-folder>/takedown/<slug>/counter-submission.md`: provider, date sent, confirmation/protocolo, whether restoration was granted, watch for the notifier seeking a tutela de urgência, plan if content is restored, plan if the notifier files suit.

## Decision posture

Per `## Decision posture on subjective legal calls` in the practice profile: when uncertain whether a use falls within a Lei 9.610/1998 limitation, whether the rights holder is us, whether the work is actually ours, whether art. 19 (court order needed) or art. 21 (notification enough) governs, whether a limitation defeats the claim on the receiving side — do not silently decide. The art. 46-48 limitations call and the art. 19-vs-21 call are the paradigmatic uncertain ones. Flag for attorney review; surface the factors. Sending a notice or a response on an assumption is a one-way door.

## What this skill does not do

- **Serve the notice or file the petition.** Drafting only. The user serves the extrajudicial notice, submits via the provider's channel, or hands the draft to counsel for a tutela de urgência.
- **Pick a provider's intake form for the user.** Notes which channel is expected; does not auto-submit.
- **Decide the limitations question.** Walks Lei 9.610/1998 art. 46-48; flags. An attorney decides whether to proceed.
- **Validate the sender's claim on the receive side.** Structured read; every authority flagged for SME verification.
- **Bypass the gate.** The gate runs every time in `--send` and `--counter` modes.
- **Invent citations.** Any cites included are source-tagged and flagged for verification; no silent supplement.
- **Handle US-only providers as the default.** The DMCA path is a gated fallback for US-hosted providers with no Brazilian reach — flag and route to it only when the Brazilian route cannot reach the provider.
