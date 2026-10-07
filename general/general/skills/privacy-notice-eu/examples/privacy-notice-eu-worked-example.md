# Worked Example — Pan-EU privacy notice (Website/App, Germany)

An end-to-end run: scope → intake summary → draft structure → Art. 13/14 verification → delivery.
Inputs are illustrative; jurisdiction specifics reflect the skill's reference files at authoring time.

---

## User prompt

> "We run a German e-commerce shop (cosmetics), targeting Germany only. We need a GDPR privacy notice.
> We use Stripe for payments, Google Analytics, a newsletter (Brevo), and ship via DHL. No AI."

---

## Step 1 — Scope, type & jurisdiction

- **Notice type:** Website / App → sub-type **E-commerce** (`references/NOTICE_TYPES.md`).
- **Jurisdiction:** Germany only → `references/DE.md` + `references/EU_COMMON.md` loaded.
- **Template:** no existing template → generate from `references/templates.md` (German).
- **Language:** single market, single language → German notice.

## Step 2 — Intake summary (confirmed with user)

```
NOTICE TYPE: Website / App (E-commerce)
CONTROLLER: [GmbH name, address, HRB no.], no DPO (below threshold; reassess)
JURISDICTION: Germany
DATA: identity, account, order/transaction, technical (IP/logs), cookies
PURPOSES + BASES:
  - Contract / order fulfilment ........ Art. 6(1)(b)
  - Account management ................. Art. 6(1)(b)
  - Tax/commercial retention ........... Art. 6(1)(c) (§ 147 AO, § 257 HGB)
  - Analytics (Google Analytics) ....... Art. 6(1)(a) consent (non-essential)
  - Newsletter (Brevo) ................. Art. 6(1)(a) consent (+ § 7 UWG soft opt-in if applicable)
PROCESSORS: Stripe (payments), Google (analytics), Brevo (email), DHL (shipping)
TRANSFERS: Google / Brevo → US sub-processors → SCCs / DPF status to confirm
COOKIES: essential + analytics + marketing → CMP required (consent before non-essential)
AI PROCESSING: none
RETENTION: orders 10y (tax); account until closure; analytics per CMP; newsletter until opt-out
```

**Flags surfaced:** (1) **DPA check** — confirm Art. 28 DPAs exist for Stripe/Google/Brevo/DHL;
(2) **transfers** — Google/Brevo US transfers need SCCs or DPF coverage; (3) **cookies** — analytics
and marketing require prior consent via a CMP; (4) no Art. 9 data; no DPIA indicators (<2).

## Step 3 — Draft structure (E-commerce section map)

Sections included: 1 Who we are · 2 What we collect · 3 Why + legal bases + retention · 4 Recipients/
processors · 5 International transfers · 6 Retention · 7 **Your rights** · 8 Cookies & tracking ·
10 Data security · 12 Changes · 13 Contact. **Section 9 (AI)** skipped (no AI). **Section 11
(children)** skipped (not directed at minors). A separate, prominent **WIDERSPRUCHSRECHT (Art. 21)**
box is included per German practice.

## Step 4 — Compliance verification (excerpt)

- ✅ Art. 13 mandatory disclosures present (controller, purposes, bases, recipients, transfers,
  retention, rights, complaint right, source where applicable).
- ✅ Supervisory authority = the competent **Landesdatenschutzbehörde** for the controller's seat
  (named from `references/DE.md`).
- ✅ Art. 21 objection presented separately and prominently.
- ⚠️ **Transfers:** notice names US transfer mechanism as SCCs/DPF — flagged for the user to confirm
  current DPF certification of Google/Brevo before publication.
- ✅ No placeholder text; update date present.

## Step 5 — Deliver

Notice generated as a formatted **.docx** (A4, numbered headings, purposes/retention + cookie tables,
TOC), via the docx generation capability (Markdown fallback if unavailable). Delivered with:

> Included: full German e-commerce privacy notice (13-section structure, adapted), separate Art. 21
> box, cookie + purposes/retention tables. **Open items:** confirm Art. 28 DPAs for all four
> processors; confirm US transfer mechanism (SCCs/DPF) for Google + Brevo; wire the notice to a CMP so
> analytics/marketing cookies fire only after consent. **Recommendation:** have counsel / your DPO
> review before publication — this is drafting assistance, not legal advice.

---

*This example shows the Website/App (e-commerce) path in Germany. Applicant, Employee, B2B, B2C, and
multi-jurisdiction notices follow their own section maps and intake profiles (see `SKILL.md` and
`references/NOTICE_TYPES.md`).*
