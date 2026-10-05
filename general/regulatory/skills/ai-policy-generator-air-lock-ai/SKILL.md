---
name: ai-policy-generator-air-lock-ai
title: AI Use Policy generator
description: Generate a polished three-page AI Use Policy for the user's company. Researches the company and sector, drafts the full policy in chat for the user to validate, then writes a print-ready HTML file plus a sidecar JSON. Use when the user asks for an "AI policy", "AI use policy", "EU AI Act policy", "AI policy one-pager", or any request to draft, generate, or update a company AI governance policy. Aligned to EU AI Act Articles 4, 5 and 50.
author: Air-Lock-AI
author_url: https://github.com/Air-Lock-AI/ai-policy-generator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# AI Use Policy generator

## When to use this skill

Activate on requests like:

- "create an AI policy", "draft an AI use policy", "generate an AI policy"
- "I need an AI policy for my company"
- "make an AI policy one-pager", "AI policy template"
- "update my AI policy" (re-run with sidecar JSON if present)
- "EU AI Act policy", "AI governance policy"

Do **not** use this skill for: technical AI safety reviews, model evaluation reports, or AI ethics whitepapers. Those are different documents.

## What this skill produces

Two files saved to the user's selected folder, only **after** the user has validated the draft in chat:

1. `ai-use-policy-{slug}-v{version}.html` — a three-page, print-ready policy document (cover, "the rules", "the duties"). Aligned to EU AI Act Articles 4, 5 and 50.
2. `ai-use-policy-{slug}-inputs.json` — a sidecar with every interview answer, used to re-run the skill with minimal questions next time.

The user opens the HTML, presses Cmd/Ctrl+P, and saves to PDF. See "Step 7" for the exact instructions to give them.

## Files in this skill

- `template.html` — the policy template with `{{PLACEHOLDER}}` markers
- `i18n/en.json`, `i18n/nl.json`, `i18n/fr.json`, `i18n/de.json` — translation packs for the static policy text
- `examples/sample-vandermeer.html` and `examples/sample-vandermeer-inputs.json` — a fictional filled example for reference

## Operating principle

**Ask everything first, then draft, then validate, then generate.** Three rules:

1. **Zero placeholders in the chat draft.** Anything you'd otherwise mark `[ to confirm ]` must be asked of the user before you write the draft. Asking small questions upfront is better than handing the user a draft full of gaps. Only acceptable inline marker is `[ to appoint ]` for DPO when the user explicitly chose it.
2. **The chat draft must mirror the HTML output, word for word on fixed text.** The clause body text is canonical (defined in `i18n/` and `template.html`); do not freelance, rephrase, expand, or invent new sentences. Your job is to substitute the user's variables into the canonical text and present that. If the chat draft promises content the HTML doesn't render, the user's approval is meaningless.
3. **Generate the HTML only after explicit user approval** ("approve", "go", "looks good").

**Do not assume the user's stack.** The two most common wrong assumptions to avoid:

- *That airlock (or any proxy) is installed.* Many companies have no AI governance layer. Ask.
- *That Claude is the AI client.* Many use ChatGPT, Gemini, Copilot, or several at once. Ask.

The policy is for **their** stack, not the template's defaults.

**Never add an extra `<div class="band">` for sector or optional content.** Each band has `break-inside: avoid` in print CSS, so a standalone extra band lands alone on its own physical page with sparse whitespace. **Add extra content as a `<div class="clause">` inside the most relevant existing band.** See the "Sector addendum" fragment pattern below.

---

## Step 0 — Greet and frame

Open with a short message:

> I'll draft a three-page AI Use Policy for your company, aligned to the EU AI Act (Articles 4, 5 and 50). I'll research the company, ask 12 short questions split across four batches (language and scope, AI tools in three flavours, sector specifics, then people and internals), draft the full policy here in chat with zero placeholders, you approve, then I generate the HTML. About 6 minutes.

Then go straight to Step 1.

## Step 1 — One big context question (free-text)

Use AskUserQuestion with a single broad question, multiple-option, with an explicit free-text fallback:

> Tell me about your company. Paste anything useful: website, sector, who your customers or users are, the kind of data you handle (financials, health, source code, claim files, etc.), country, anything else relevant. The more I have, the less I'll ask later.

Capture the full response. Extract:

- Company name and legal entity (e.g. "DAS / DAS Belgische Rechtsbijstandverzekeringsmaatschappij N.V.")
- City and country
- Sector (insurer, creative hub, SaaS, consultancy, healthcare, fintech, agency, education, manufacturing, etc.)
- Sensitive data classes
- Audience label (policyholders / patients / clients / residents / users / students)

## Step 2 — Research

WebSearch up to 5 targeted queries, only when the user has given a real lead:

1. `"{company}" {city}` — confirm legal entity, founding, parent group
2. `"{company}" CEO OR leadership` — find the CEO name
3. `EU AI Act high-risk {sector}` — Annex III high-risk flags relevant to the sector
4. `EU AI Act Article 4 5 50 {sector}` — sector-specific obligations
5. `data protection authority {country}` — local DPA name (GBA/APD Belgium, CNIL France, BfDI Germany, AEPD Spain, AP Netherlands, etc.)

**Never invent.** Names, emails, Slack handles, internal URLs that aren't on the public web → use `[ to confirm ]`.

## Step 3 — Structural questions (the ones that change the document's shape)

Before drafting, the following decisions change the **shape** of the document, not just its words. Ask them across **two AskUserQuestion calls** so they don't overwhelm the user.

### Call 1: language, proxy, scope

### Q1 — Output language

> What language should the policy be in?
>
> Options: English, Dutch, French, German.

Defaults to English. The skill ships `i18n/en|nl|fr|de.json`.

### Q2 — AI governance / proxy layer

> Does your company have an AI governance proxy that all AI tools go through?
>
> Options:
> - "Yes — airlock"
> - "Yes — other (Cloudflare AI Gateway, Portkey, LiteLLM, custom, …)" — ask for the name
> - "No, we connect to AI tools directly"
> - "Not sure yet"

If "Yes — airlock": include the `airlock · proxy connector (Required)` row, and the "airlock is the only approved proxy connector" sentence in the standfirst of the tools register.

If "Yes — other": replace `airlock` with the named proxy. Same role.

If "No" or "Not sure": **omit the proxy row entirely** and remove the proxy lead-sentence. The tools register starts directly with the user's approved AI tools.

### Q3 — Policy scope

> Who does this policy apply to?
>
> Options:
> - "Whole company (all staff, contractors, interns)" — default
> - "One department or team only" — ask which one (e.g. "Engineering only", "Marketing only")
> - "Specific cohort" — e.g. "Customer-facing staff", "EU staff only"

If a narrower scope is picked, the standfirst and clause 1 mention it explicitly: "Applies to [scope] at {{COMPANY}}." Everything else in the document stays the same.

### Call 2: AI tools — three separate questions

Three categories of AI must be asked **separately**, because users tend to forget the embedded and customer-facing ones.

### Q4 — AI clients (chat / assistant tools)

> Which standalone AI chat or assistant tools does your company use, or plan to use?
>
> Multi-select:
> - "Claude (Teams / Pro / Enterprise)"
> - "ChatGPT (Plus / Team / Enterprise)"
> - "Google Gemini / Workspace AI"
> - "Mistral Le Chat"
> - "GitHub Copilot / Cursor / Claude Code" (engineering)
> - "Other" — ask for the list
> - "None"

### Q5 — Embedded AI (features built into tools you already pay for)

> Beyond standalone chat tools, which AI features are embedded in software you already use? These are covered by this policy too.
>
> Multi-select:
> - "Microsoft 365 Copilot" (Word, Excel, Outlook, Teams, Recall)
> - "Salesforce Einstein"
> - "Notion AI"
> - "Slack AI"
> - "Adobe Firefly" (in Creative Cloud)
> - "Zoom AI Companion"
> - "Google Workspace AI" (Gemini in Docs, Gmail, Meet)
> - "Other / not sure" — ask for the list
> - "None"

Each selected item gets a row in the approved-tools register, tier-tagged conservatively (Tier 1 if enterprise contract, Tier 2 if consumer/included). Access path defaults to "via your existing licence".

### Q6 — Customer-facing AI

> Do you operate any AI that customers or the public interact with directly?
>
> Multi-select:
> - "Website chatbot"
> - "AI in your product (recommendations, decisions, generated content)"
> - "Email auto-reply / triage"
> - "AI voice assistant or callbot"
> - "Other" — ask
> - "None"

If anything is selected, the policy's clause 6 (Transparency) becomes more specific. Examples added inline: "Our [chatbot / product feature] opens with 'I am an AI assistant'. Customers affected by an AI-supported decision are told and offered a human review." The policy also gains a one-sentence rule under clause 6 covering EU AI Act Art 50 obligations for the specific surfaces selected.

### Q7 — Sector addendum (with enumeration)

> Your sector is **{sector}**. Want an Annex III high-risk-uses clause inside the policy?
>
> Auto-suggest "Yes" when sector is one of: insurance, banking, employment / HR, healthcare, education, biometrics, critical infrastructure, justice, migration. Otherwise default to "No".

If yes, immediately follow with a multi-select for **which Annex III uses you actually do or plan in the next 12 months**. Show only the ones relevant to the user's sector. Example for an insurer:

> Which of these high-risk uses apply at your company?
>
> Multi-select:
> - "Insurance risk assessment (underwriting)"
> - "Pricing"
> - "Claims handling decisions"
> - "Policy eligibility / coverage determination"
> - "Fraud detection on customers"
> - "None of these (yet)"

The selected items become the named high-risk uses in the addendum clause. **Never invent.** If user picks "None of these (yet)", skip the addendum entirely with a note in chat: "Skipping the Annex III addendum since no high-risk uses are in scope today. Add it later if that changes."

### Q8 — Enforcement / detection

> How will policy breaches be detected? (This becomes one sentence in clause 9.)
>
> Options:
> - "Self-report only" — staff voluntarily flag
> - "Self-report + spot audits" — sample-based review by AI Officer
> - "Self-report + IT controls" — DLP, network monitoring, tool-side logging
> - "All three"
> - "Not decided yet" — defaults to "Self-report" with a note in clause 9

The selected method shows in clause 9 as: "Breach detection: [method]." Keeps the policy honest about how seriously it will be enforced.

**Never add a new `<div class="band">` for any of these.** Embedded AI tools, customer-facing AI examples, the Annex III addendum, the enforcement sentence — all go **inside existing bands** as new rows or clauses. See the fragment patterns below.

## Step 4 — People and internals (fill every placeholder NOW)

**The chat draft in Step 5 must have zero placeholders.** Every `[ to confirm ]` that would otherwise appear in the draft must be asked here. The user reads the draft to validate content, not to be reminded what they still owe.

Ask all of the following in **one AskUserQuestion call** (up to 4 questions, each with multi-choice options plus an explicit "Other / type the answer" path for free-text). If the user picks "Other", capture their typed value and use it.

### Q9 — CEO (signatory)

> Who signs as CEO? Research suggests **{ceo_from_research or '[no name found, type one']}**.
>
> Options:
> - "Confirm this name" (if research found one)
> - "Different name — type it"
> - "Use placeholder `[ CEO name ]` for now"

### Q10 — AI Officer (the named owner of this policy)

> AI Officer: name, email, Slack handle? This person owns the policy and is the incident contact.
>
> Options:
> - "Type all three" — captures name, email, slack
> - "Name only, fill the rest later"
> - "Use full placeholders"

When the user types, parse the format `Name <email> @slack` or any plain text. If anything missing, set the missing fields to `[ to confirm ]`.

### Q11 — DPO and internal channels

> Two more contacts:
>
> - DPO name and email (or `[ to appoint ]` if you don't have one)
> - Internal AI help channel (Slack / Teams)
>
> Options:
> - "Type both"
> - "DPO only"
> - "Channel only"
> - "Use placeholders" — DPO becomes `[ to appoint ]`, channel becomes `#ai-help`

**Regulated-sector DPO informer.** If the sector is one of: insurance, banking, healthcare, public sector, large-scale data processor (>250 staff), and the user answers `[ to appoint ]` for DPO, add a one-line **informational note in the chat draft** (Step 6) above the contacts section:

> *Note: under GDPR Article 37 your sector requires a designated DPO. The policy keeps `[ to appoint ]` for now; consider opening that hire.*

This is **not a blocker**. The draft generates with `[ to appoint ]` as the user chose; the line is purely informational so they know it's a compliance gap.

### Q12 — Access path and internal links

> Last batch:
>
> - Where do people request access to the approved AI tools? (e.g. "IT helpdesk", "AI Officer", a URL)
> - Live register URL (where the approved-tools list is maintained internally)
> - Name of your disciplinary code (used in clause 10)
>
> Options:
> - "Type all three"
> - "Just the access contact, defaults for the rest" — register defaults to `intranet/ai-tools`, disciplinary code to "disciplinary code"
> - "All defaults"

After Q9-Q12, you have everything needed to draft with zero placeholders. **Do not start drafting until every required field is filled, either with a real value or an explicit user-chosen placeholder string.**

**Rule of thumb for the runtime agent:** if you're about to write `[ to confirm ]` into the draft and you didn't ask the user for that field, go back and ask. The only acceptable inline placeholders in the chat draft are `[ to appoint ]` (DPO when the company truly doesn't have one) and `[ CEO name ]` / similar explicitly-chosen labels — and only if the user explicitly chose that option.

## Step 5 — Assemble the draft (internal)

Build a complete draft of every placeholder. Use sensible defaults:

| Field | Default if unknown |
|---|---|
| Version | `1.0` |
| Effective date | Today (formatted "17 June 2026") |
| Review date | Today + 6 months |
| Review cadence | Every six months |
| Classification | `Internal · Confidential` |
| Standfirst | One sentence ending "Aligned to the EU AI Act." |
| Audience label | From sector (policyholders / clients / residents / patients / users / students) |
| CEO | `[ to confirm ]` if not in research |
| AI Officer | `[ to confirm ]` |
| DPO | `[ to appoint ]` for small companies, `[ to confirm ]` for sectors that legally need one (insurer, healthcare, fintech, public sector) |
| Incident report channel | `#ai-help` Slack channel placeholder |
| Live register URL | `intranet/ai-tools` placeholder |
| House rules | The four template defaults, plus sector-specific additions when relevant |

Hold this draft in working memory. **Do not write any files yet.**

## Step 6 — Present the FULL draft in chat for validation

**Critical rule: the chat draft must be a faithful preview of what the HTML will actually render. Do not freelance, rephrase, expand, or invent new clause text.** The clause body text is fixed in `i18n/{lang}.json` and `template.html`. Your job is to substitute the user's variables into the canonical text below and present the result. If you find yourself writing a fuller, prosier version because it "reads better", stop — the user will approve it, then open the PDF, and find different (shorter) text. That breaks trust.

The user-customisable parts are: standfirst, scope description, house rules list, tools register rows, sector addendum clause (if any), DPO informer note (if any), enforcement sentence in clause 9, and contact details. **Everything else is canonical.**

### Canonical text to render in the chat preview (English; for nl/fr/de use the matching i18n strings)

```
COVER
  AI Use Policy
  {{COMPANY}}
  {{LEGAL_ENTITY}} · {{CITY}}
  {{STANDFIRST}} Aligned to the EU AI Act.
  Version {{VERSION}} · Effective {{EFFECTIVE_DATE_LONG}} · Next review {{REVIEW_DATE_LONG}}
  Classification: {{CLASSIFICATION}}

THE RULES

Clause 1 — Purpose, scope, validity
  Keeps {{COMPANY}} compliant with the EU AI Act and protects the trust our community places in us. Applies to {{SCOPE_DESCRIPTION}}, and to AI built into tools we already run.

Clause 2 — Three things every {{COMPANY}} employee must do
  Three duty cards (fixed wording):
    01 · TRAIN — Complete AI literacy
      Finish the 30-minute AI literacy module within 30 days of joining; refresh yearly.
      (EU AI Act Art. 4, in force Feb 2025)
    02 · STAY ON LIST — Use only approved tools
      Run company work through the Approved AI Tools list (clause 5). No personal accounts, no shadow AI.
    03 · REPORT — Flag incidents same day
      If AI output is wrong, biased, harmful, leaked or risky, report to the AI Officer before close of business.

Clause 3 — Prohibited uses
  Banned · EU AI Act, Article 5 (5 fixed bullets):
    - No social scoring of staff, customers or users.
    - No emotion or mood detection in the workplace.
    - No manipulative or subliminal AI techniques.
    - No biometric scraping or mass surveillance.
    - No deepfakes of real people without consent.
  Banned · {{COMPANY}} house rules ({{N}} bullets — the four template defaults plus any user additions):
    {{HOUSE_RULES_LIST}}
  Full prohibited list → EU AI Act, Article 5

Clause 4 — What you can use with what data (4-row matrix, fixed)
  Public information → Any approved tool.
  Internal, non-sensitive → Approved tools only. No consumer or free-tier tools.
  Customer, employee, financial → Tier 1 enterprise tools only, with DPA on file.
  Source code, IP, trade secrets → Tier 1 only, with manager or AI Officer approval per use.

Clause 5 — Approved AI tools ({{COMPANY}} register)
  {{PROXY_LEAD_SENTENCE_IF_ANY}}
  Register rows:
    {{TOOLS_REGISTER}}
  Live register: {{LIVE_REGISTER_URL}} · request new connectors via the AI Officer.

  (If Q7 sector addendum = yes, append the following clause inside this band)
  Sector-specific high-risk uses (EU AI Act, Annex III)
    The following use(s) at {{COMPANY}} are classified high-risk under EU AI Act Annex III: {{ANNEX_III_USES_LIST}}. Each requires human oversight, logging, and an internal risk assessment before deployment.
    No high-risk system goes live without sign-off from the AI Officer and the DPO. Each high-risk use is logged in the AI register with the responsible reviewer named.

THE DUTIES

Clause 6 — Always tell people when AI is involved
  A chatbot's first message says "I am an AI assistant." AI-generated images, audio or video that could be mistaken for real carry an "AI-generated" label. (EU AI Act Art. 50, due 2 Aug 2026.)
  A candidate, partner or user affected by an AI-supported decision is told, and offered a human review on request.
  {{CUSTOMER_AI_SENTENCE_IF_ANY}}

Clause 7 — You stay accountable for what you ship
  AI errors are your errors.
  AI is a draft. You verify before sending, publishing, deploying or signing off. "The AI did it" is not a defence at {{COMPANY}}.

Clause 8 — Confidentiality and IP
  Do not paste anything into AI that you would not post publicly, unless the tool is Tier 1. Confidential business documents are Tier 1 by default.
  AI outputs are {{COMPANY}} property where the law allows. Tell your manager when a deliverable is AI-assisted.

Clause 9 — Incidents, same business day
  Output that's wrong, biased, harmful or leaked, or that could embarrass {{COMPANY}} or harm someone, goes to the AI Officer before close of business, with what you did, what it produced and what data was involved.
  Breach detection: {{ENFORCEMENT_METHOD}}.

Clause 10 — Sanctions
  Breach of this policy is treated under the {{COMPANY}} {{DISCIPLINARY_CODE}}, up to and including termination, and referral to authorities where required by law.

Clause 11 — Where to ask
  AI Officer: {{AI_OFFICER_NAME}} · {{AI_OFFICER_EMAIL}} · Slack {{AI_OFFICER_SLACK}} · channel {{AI_HELP_CHANNEL}}
  Data protection (DPO): {{DPO_NAME}} · {{DPO_EMAIL}}
  {{DPO_FALLBACK_IF_TO_APPOINT}}
  When in doubt, ask first. It is always cheaper than a leaked deck or a regulator's letter.
  {{DPO_REGULATED_SECTOR_INFORMER_IF_ANY}}

Clause 12 — Acknowledgement & review
  By continuing to use AI tools for {{COMPANY}} work, you acknowledge this policy. Owner: AI Officer · Version {{VERSION}} · Effective {{EFFECTIVE_DATE_LONG}} · Next review {{REVIEW_DATE_LONG}}, or sooner after any incident or significant regulatory change.

SIGNATURES
  {{CEO_NAME}} · Chief executive officer
  {{AI_OFFICER_NAME}} · AI Officer
```

Render the canonical text above in chat, with the `{{VARIABLES}}` resolved. Conditional pieces:

- `{{PROXY_LEAD_SENTENCE_IF_ANY}}` — only if Q2 selected a proxy. Format: "**{{PROXY_NAME}} is the only approved proxy connector.** Every other connector sits behind it: one URL, policy set once, every call audited."
- `{{CUSTOMER_AI_SENTENCE_IF_ANY}}` — only if Q6 picked any customer-facing AI. Format: "Specifically, our [{{CUSTOMER_AI_LIST}}] complies with EU AI Act Art. 50."
- `{{ENFORCEMENT_METHOD}}` — text from Q8 (e.g. "self-report only", "self-report plus IT controls").
- `{{DPO_FALLBACK_IF_TO_APPOINT}}` — only if DPO is `[ to appoint ]`: "Until appointed, route to the AI Officer."
- `{{DPO_REGULATED_SECTOR_INFORMER_IF_ANY}}` — only if regulated sector AND DPO is `[ to appoint ]`: "Note: under GDPR Article 37 your sector requires a designated DPO. The policy keeps `[ to appoint ]` for now; consider opening that hire."
- `{{ANNEX_III_USES_LIST}}` — comma-joined list from Q7 enumeration. Skipped if user selected "None of these (yet)".

**No "Gaps to fill" section.** If the draft contains any placeholder besides `[ to appoint ]` (DPO) or explicit user-chosen labels, you skipped Step 4. Go back and ask.

End the message with:

> Read through. When you're happy, reply `approve` and I'll generate the HTML. Otherwise tell me what to change.

## Step 7 — Iterate until approved

If the user replies with edits ("change the CEO to X", "drop the deepfake clause", "add a rule about client data exfiltration"), apply them, then re-send the **full** updated draft in chat. Repeat until the user explicitly approves.

**Do not** generate any file until the user has said "approve" / "go" / "looks good" or equivalent.

## Step 8 — Generate the HTML and JSON

Once approved:

1. Load `template.html` from this skill folder.
2. Load `i18n/{lang}.json` for the chosen language.
3. Do a literal string-replace of every `{{PLACEHOLDER}}` with the resolved value. Render the tools-register rows and the house-rules list as inline HTML (see "HTML fragment patterns" below).
4. If a proxy was named (Q2), use that name in the register row instead of `airlock`. If no proxy, omit the proxy row entirely and adjust the standfirst sentence above the register.
5. Compute the slug: `lowercase(company)`, strip non-alphanumerics, hyphens for spaces.
6. Write to the user's selected folder:
   - `ai-use-policy-{slug}-v{version}.html`
   - `ai-use-policy-{slug}-inputs.json`

The JSON sidecar holds every answer plus a `_meta` block with skill version, timestamp, and the proxy/clients selections. Example shape:

```json
{
  "_meta": { "skill_version": "1.1.0", "generated_at": "2026-06-22T11:00:00Z", "language": "en", "approved_in_chat": true },
  "identity": { "company": "DAS", "legal_entity": "DAS Belgische Rechtsbijstandverzekeringsmaatschappij N.V.", "city": "Brussels", "country": "Belgium", "classification": "Internal · Confidential", "sector": "insurance", "audience_label": "policyholders" },
  "dates": { "version": "1.0", "effective": "2026-06-22", "review": "2026-12-22", "cadence_months": 6 },
  "people": { "ceo": { "name": "Xavier de Launois", "title": "Chief executive officer" }, "ai_officer": { "name": "[ to confirm ]", "email": "[ to confirm ]", "slack": "[ to confirm ]", "channel": "#ai-help" }, "dpo": { "name": "[ to confirm ]", "email": "[ to confirm ]" } },
  "governance": { "proxy": null, "proxy_name": null, "clients": ["Claude Teams / Pro"] },
  "tools": [ { "name": "Claude Teams / Pro", "tier": "Tier 1", "access": "[ to confirm ]" } ],
  "house_rules": [ "..." ],
  "sector_addendum": true,
  "regulator": "GBA / APD"
}
```

## Step 9 — Tell the user how to get a PDF

After saving, send this exact instruction block:

> ✓ Generated. Two files in your folder:
>
> - `ai-use-policy-{slug}-v{version}.html` — the policy
> - `ai-use-policy-{slug}-inputs.json` — your answers, for re-runs
>
> **To save as PDF:**
> 1. Open the HTML in your browser. Click the floating **Save as PDF** button (top-right).
> 2. In the print dialog: Margins → **None**. Scale → **Default**. Background graphics → **on**. Headers and footers → **off**. Paper size → **A4**.
> 3. Save next to the HTML as `ai-use-policy-{slug}-v{version}.pdf`.
>
> To update later, run this skill again pointing at the JSON sidecar. It'll only ask what changed.

End with the file-presentation call for both files. Do not summarize the content of the policy itself.

---

## HTML fragment patterns

### Tools register rows (replaces `{{TOOLS_REGISTER_ROWS}}`)

For each tool:

```html
<div class="rrow"{{HIGHLIGHT}}><div class="tool">{{TOOL_NAME}}{{TOOL_NOTE_HTML}}</div><div class="tier">{{TIER}}</div><div>{{ACCESS}}</div></div>
```

- `{{HIGHLIGHT}}` adds `style="background:var(--indigo-wash);"` when the tool is the proxy row (airlock or other named proxy).
- `{{TOOL_NOTE_HTML}}` wraps any note in `<span style="color:var(--ink-400);font-weight:400;"> · {note}</span>`.

### Proxy lead-in sentence

When a proxy IS selected, render the lead sentence above the register table:

```html
<p style="margin:0 0 2mm;"><b style="color:var(--ink-900);font-weight:600;">{{PROXY_NAME}} is the only approved proxy connector.</b> <span class="lead">Every other connector sits behind it: one URL, policy set once, every call audited.</span></p>
```

When NO proxy is used, OMIT this paragraph entirely.

### House rules list (replaces `{{HOUSE_RULES_HTML}}`)

Each rule is `<div class="proh">` with the strong noun bolded:

```html
<div class="proh">No AI as <b>sole decision-maker</b> for hiring, performance, promotion or termination. A human always decides.</div>
```

Bold the most important noun. One sentence per rule.

### Sector addendum (when Q4 is yes)

**Do not create a new band.** A standalone band lands alone on a page because the per-band `break-inside: avoid` rule prevents it from packing with anything else. That looks bad.

Instead, **append the addendum as the last clause inside an existing band**, choosing the band by topic:

- For **risk-assessment, pricing, claims, eligibility, hiring, credit scoring, education-grading, biometric ID** → append to the "Data & approved tools" band (band 03), right after the tools register clause. The addendum extends "what you can use with what data" with "and these specific uses are high-risk under Annex III".
- For **prohibitions that go beyond Article 5 in a sector-specific way** → append to the "Banned, full stop" band (band 02), as a sub-section under the house rules.

Example clause to insert into band 03 for an insurer:

```html
<div class="clause">
  <h4><span class="cn">+</span> Sector-specific high-risk uses (EU AI Act, Annex III)</h4>
  <p>The following uses at {{COMPANY}} are classified high-risk under EU AI Act Annex III: <b>insurance risk assessment and pricing</b>, <b>claims-handling decisions</b>, and any <b>automated determination of policy eligibility or coverage</b>. Each requires human oversight, logging, and an internal risk assessment before deployment.</p>
  <p>No high-risk system goes live without sign-off from the AI Officer and the DPO. Each high-risk use is logged in the AI register with the responsible reviewer named.</p>
</div>
```

Keep the addendum to **two paragraphs maximum**, so the host band still packs cleanly with adjacent bands on the same physical page.

Sector-tailoring guidance (use general EU AI Act Annex III knowledge):

- **Insurance** → risk assessment, pricing, claims handling, eligibility determination
- **Banking / fintech** → credit scoring, fraud risk evaluation
- **Employment / HR** → CV screening, hiring decisions, performance evaluation, task allocation
- **Healthcare** → triage, diagnosis support, medical-device control
- **Education** → student admission, assessment, plagiarism detection
- **Biometrics** → remote biometric identification, categorisation
- **Critical infrastructure** → safety components in water, gas, electricity
- **Justice** → judicial decision support, evidence evaluation
- **Migration / border** → eligibility evaluation, document verification

If the sector doesn't appear above, ask the user to name the relevant Annex III uses before drafting the clause. Don't fabricate.

---

## Re-run behaviour

If the user invokes the skill in a folder that already contains an `ai-use-policy-*-inputs.json`, skip Steps 1-3 and load that JSON. Re-present the draft in chat (Step 5) with any updated dates (bump version, refresh effective date), then continue from Step 6. The user only re-validates the diff.

## Style and tone rules

- No em dashes anywhere in generated content. Use commas, periods, or colons.
- One sentence per house rule.
- Standfirst is one sentence ending "Aligned to the EU AI Act."
- Quote no regulator name you didn't verify. Use `[ to confirm ]` if unsure.
- Never invent a person's name, email, or Slack handle. Use `[ to confirm ]`.
- Never assume airlock or Claude. Defaults to placeholders, fills only when the user has answered Q2 and Q3.

## Long content — overflow behaviour

The cover (page 1) is fixed-height A4. Content pages grow with content. A JS splitter in the template automatically divides long sheets into discrete A4 cards at band boundaries. Page numbering ("part N of M") is rewritten after splitting to reflect the actual count.

Practical guidance:

- Do not trim clauses to fit a target page count. Write the policy at the right length, even if that means 4 or 5 physical pages.
- Append extra bands (sector addendum, etc.) to the same `<section class="sheet">`. The splitter handles the breaks.

## Defaults reference

If the user keeps every default, the policy should still be a credible draft. Defaults are deliberately conservative.

```
Company:           [ your company ]
Legal entity:      [ your legal entity ]
City:              [ your city ]
Country:           [ your country ]
Classification:    Internal · Confidential
Version:           1.0
Effective:         today
Next review:       today + 6 months
Cadence:           every six months
Audience label:    users
Standfirst:        How we use AI at [Company]: what's approved, what's off-limits, and who signs off before anything leaves the company. Aligned to the EU AI Act.
CEO:               [ to confirm ]
AI Officer:        [ to confirm ]
DPO:               [ to appoint ] (or [ to confirm ] for regulated sectors)
AI help channel:   #ai-help
Proxy:             none (until user confirms in Q2)
Clients:           none prefilled (until user confirms in Q3)
House rules:       the four template defaults
Regulator:         derived from country, or [ to confirm ]
```
