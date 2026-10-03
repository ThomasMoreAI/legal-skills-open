---
name: legal-intake-contract
created: 2026-04-27
status: active — hardened by biz-imp M2 on 2026-05-03
audience: /slo-legal advisor skill
purpose: |
  Structured-data CONTRACT that the skill MUST gather **conversationally** before
  entering `draft` mode. Closes the predicate-evaluation hallucination surface
  identified in the 2026-04-27 skill-pack review. The four hard-block gates in
  `references/biz/triage-gate.md` are evaluated against THIS structured input, not against
  free-form founder prose.

  This is NOT a form for the founder to fill. It is the destination shape of a
  conversational elicitation the skill drives — modeled on `/slo-ideate`'s seven
  forcing questions. The skill asks one question at a time, pushes back on vague
  answers, ladders down when the founder is unsure, and synthesizes the dialogue into
  the structured `intake_summary:` block. The founder never sees a form.

  Companion files: `accounting-intake-contract.md`, `equity-intake-contract.md`,
  `fundraise-intake-contract.md`, `hire-intake-contract.md` (all per issue #19).
---

# /slo-legal — pre-draft conversational intake contract

**Conversation is the UX.** This file is a structured destination contract for
the skill, not a founder-facing form. The founder experiences one question at a
time, with pushback on vague answers and an explicit restate-and-confirm loop
before the skill evaluates any hard-block gate.

The skill MUST gather every field below **through conversation** before entering `draft` mode. "Skill emits a form" is the wrong UX. "Skill asks one question, pushes if the answer is vague, moves on when the answer is concrete enough to evaluate the gate" is the right UX — same pattern as [`/slo-ideate`'s seven forcing questions](../../skills/slo-ideate/SKILL.md).

Empty / "I don't know" / hypothetical answers do not fall through to draft with an assumption. They are an explicit signal: either ask the founder to find the fact (e.g., "look at who emailed you the contract" for counterparty representation), or — if the fact genuinely cannot be known yet — route to `triage` rather than `draft`.

## How the skill uses this contract

The skill drives a conversational loop that produces the structured `intake_summary:` block. The loop is:

1. Founder invokes `/slo-legal draft <doc-type>`.
2. Skill begins the elicitation conversation. **One question at a time.** Do not dump the field list on the founder. Push on vague answers. Ladder down when the founder is unsure. The order in §"Required fields" below is the recommended ask-order, but the skill MAY adapt to the founder's framing (e.g., if the founder leads with "this is a non-UK contract", jump to F1 immediately and short-circuit).
3. As the founder answers, the skill synthesizes the response into the closed-enum / numeric / boolean shape required by the contract. Validates each value. Asks for clarification when ambiguous.
4. After all fields are gathered, skill **restates the situation in 3-5 sentences** and asks the founder to confirm (modeled on [`/slo-execute`'s 'Restate the milestone constraints in your own words'](../../skills/slo-execute/SKILL.md#L36)). On correction, skill re-asks the affected questions and re-synthesizes — never silently re-interprets.
5. On confirmation, skill evaluates the four gates against the structured input.
6. If any gate fires, the artifact is `triage`-shaped, not `draft`-shaped, with `gates_fired:` populated from this intake.

The structured `intake_summary:` block is the **output** of the conversation, not a UI surface. It lands in the artifact frontmatter (per `references/biz/artifact-schema.md`) so downstream tooling (`/slo-verify`, future audit / replay) can inspect what the skill thought it knew when it drafted.

## Conversation discipline (for the skill)

Borrowed verbatim from `/slo-ideate`'s anti-pattern set:

- **Do not ask all questions at once** — single-question, wait for answer, push if vague, then move on.
- **Do not accept hypotheticals** — "the contract value is probably around £5k" is not a value; ask "is that monthly, annual, or total — and ex-VAT?"
- **Do not soften pushback to keep the founder happy** — you are the advisor, not the cheerleader. If the founder is rounding, evading, or wishful, the gate evaluation will be wrong; the founder will be the one who pays the cost.
- **Restate, do not re-interpret silently** — if the founder corrects, ask "did I hear that right?" again. Re-interpretation without confirmation is the failure mode this whole flow exists to prevent.

## Required fields (the contract)

### F1. Jurisdiction

> Where will this contract be performed, and what governing law will it use?

- `jurisdiction_self`: enum — `uk-england-wales` | `uk-scotland` | `uk-northern-ireland` | `non-uk`
- `jurisdiction_counterparty`: enum — same set
- `governing_law_specified`: bool (is there a clause in the doc / situation specifying governing law?)
- `governing_law_value`: free-text (only required if `governing_law_specified: true`)

**Refusal**: any `non-uk` value → canonical "v1 supports UK only" error from `references/biz/jurisdiction-uk.md`. Do not draft. Do not produce a "for reference only" US/EU output.

### F2. Counterparty representation

> Is the other party represented by a lawyer in this matter? Are you being asked to sign a contract drafted by them?

- `counterparty_has_lawyer`: enum — `yes` | `no` | `unknown`
- `signing_their_paper`: enum — `yes` | `no` | `unknown` (i.e., is the contract being handed to the founder pre-drafted, vs the founder sending their paper)
- `counterparty_identity`: free-text (a name or role; used in `triage` memo body, not for gate evaluation)

**Predicate firing**: `gate-3-counterparty-has-lawyer-or-their-paper` fires on `yes` to either question. `unknown` is **not a fall-through to `no`** — refuse and ask the founder to find out (most common: ask the counterparty directly, or look at who the contract was sent from).

### F3. Deal value

> What is the total contract value, in GBP, exclusive of VAT, over the full term of the engagement?

- `deal_value_gbp_ex_vat`: number (total contract value over full term)
- `deal_value_basis`: enum — `total-contract-value` | `monthly-recurring` | `annual-recurring` | `one-off-fee` | `not-applicable`
- `deal_value_term_months`: number (only required if basis is recurring)
- `deal_value_known_with_confidence`: enum — `precise` | `estimated-within-25-percent` | `estimated-roughly` | `unknown`

The skill MUST compute total contract value from `deal_value_basis` + `deal_value_term_months`. Founders frequently quote monthly numbers when the gate measures total. Worked examples:

- £500/month × 24-month term → £12,000 ex-VAT total → **gate-2 fires**.
- £8,000 one-off fee → £8,000 ex-VAT total → **gate-2 fires**.
- £4,000/year × 1-year contract with auto-renewal → £4,000 first-term-only → **gate-2 may not fire BUT** flag the auto-renewal in `triage` body.
- VAT-inclusive £5,400 → ex-VAT £4,500 → gate-2 does not fire on value alone.

**Predicate firing**: `gate-2-deal-value-over-5k` fires on `> 5000`. **`unknown` confidence is a refusal**, not a fall-through. The skill must ask the founder to commit to an estimate; "I don't know" is the founder's signal that they need a triage memo, not a draft.

**Explicit-comprehension question (per critique S-1)**: before locking F3 the skill asks the founder to confirm the value in two framings, e.g., *"To confirm — you said £8,000 for a 4-month engagement. Is that £8,000 per month (= £32,000 total, 4× the gate-2 threshold) or £8,000 total over the 4 months? And is that figure inclusive or exclusive of VAT?"* This catches the most common misframing without requiring the founder to read the schema. The skill records the exact phrasing of the founder's confirmation in the artifact's `intake_summary.deal_value_confirmation:` field for downstream audit.

**Borderline cases (£4,500–£5,500)**: evaluate alongside the other three gates. If gate-1 / gate-3 / gate-4 also fire, route to triage regardless. If only gate-2 is borderline and other gates pass cleanly, the skill may draft but MUST surface the proximity in the artifact body: "Deal value £X is within 10% of the £5,000 triage threshold — solicitor review is recommended even by the skill's defensive defaults."

### F4. GDPR scope

> Does the document being requested relate to processing of personal data: privacy notice, ROPA, DPA, internal data-protection policy, lawful-basis statement, DPIA, DSAR procedure, breach-notification template, cookie policy, or anything else the ICO would expect to see in a controller's accountability file?

- `gdpr_document_requested`: bool
- `gdpr_document_type`: free-text (only required if `gdpr_document_requested: true`)
- `gdpr_data_in_scope`: bool (is personal data otherwise in scope, even if the document itself isn't a GDPR doc — e.g., a contractor SOW that includes shared-data processing terms?)

**Predicate firing**: `gate-4-gdpr-document` fires on `gdpr_document_requested: true` — **unconditional refusal of `draft` mode** for ANY GDPR-related document, locked decision 2026-04-25. Routes to triage with `route_to: dpo (or lawyer + dpo if no DPO)`. Reversal requires a fresh `/slo-architect` pass with new ICO enforcement evidence.

If `gdpr_data_in_scope: true` but `gdpr_document_requested: false` (e.g., a contractor SOW with data-handling clauses but the request is the SOW, not a DPA), the skill drafts the SOW but flags the data-handling clauses as "needs DPO review for adequacy" in the body.

### F5. Regulated sector

> Does the matter touch any regulator with statutory enforcement powers — see `references/biz/uk-regulator-enumeration.md`?

- `regulator_in_scope`: bool
- `regulator_id`: enum (closed list from `uk-regulator-enumeration.md`; only required if `regulator_in_scope: true`)
- `regulator_relationship`: enum — `regulated-business` | `regulated-counterparty` | `regulator-as-counterparty` | `incidental`

**Predicate firing**: `gate-1-regulated` fires on `regulator_in_scope: true` AND `regulator_relationship` ≠ `incidental`. The skill consults `references/biz/uk-regulator-enumeration.md` for routing — the default is `lawyer` but specific regulators (HMRC, ICO, Companies House, Pensions Regulator) override per the per-skill routing table.

**The skill does NOT enumerate regulators from training memory**. If the founder names a regulator not in the enumeration file, refuse: "Regulator <X> is not in the enumeration. Either (a) confirm it's not the body you mean and pick from the file, or (b) flag the gap as a follow-up so the enumeration can be extended via `/slo-architect` review (do not bypass)."

### F6. Doc-type and counterparty (artifact metadata)

These fields are not used for gate evaluation but must be captured for the artifact frontmatter:

- `doc_type`: enum — `nda` | `contractor-sow` | `ip-assignment` | `terms-and-conditions`
- `counterparty_kebab_slug`: free-text (used in artifact filename)
- `counterparty_legal_name`: free-text (used in artifact body; goes only to `docs/biz/legal/` confidential tier)

**Refusal**: `doc_type` outside the enum → "B2C T&Cs out of scope" / "v1 doc-types are: nda | contractor-sow | ip-assignment | terms-and-conditions" (matches existing `slo-legal` SKILL.md refusal patterns).

## Restate-and-confirm step

After the conversation has gathered F1–F6, the skill emits a 3-5 sentence restatement:

> Before I draft, let me restate what I understood:
> - You're a UK [England & Wales] founder asking for a [contractor SOW] for [Acme Logistics Ltd].
> - The deal value is [£3,200 ex-VAT total over a 4-month engagement] — under the £5,000 triage threshold.
> - The counterparty does NOT have a lawyer in this matter, and they're signing your paper, not theirs.
> - This is not a GDPR document, and no regulator is in scope.
> - Gates evaluated: gate-1 PASS, gate-2 PASS, gate-3 PASS, gate-4 PASS — proceeding to draft.
>
> **Did I get that right?**

On founder correction, the skill re-evaluates the four gates against the corrected input. On confirmation, the skill writes the intake values into the artifact frontmatter as `intake_summary:` and proceeds to draft.

## Frontmatter contract (per artifact)

The intake values land in the artifact frontmatter (extends `references/biz/artifact-schema.md`):

```yaml
intake_summary:
  jurisdiction_self: uk-england-wales
  jurisdiction_counterparty: uk-england-wales
  governing_law_specified: false
  counterparty_has_lawyer: no
  signing_their_paper: no
  deal_value_gbp_ex_vat: 3200
  deal_value_basis: total-contract-value
  deal_value_term_months: 4
  deal_value_known_with_confidence: precise
  gdpr_document_requested: false
  gdpr_data_in_scope: false
  regulator_in_scope: false
  doc_type: contractor-sow
  counterparty_kebab_slug: acme-logistics
gates_evaluation:
  gate-1-regulated: pass
  gate-2-deal-value-over-5k: pass
  gate-3-counterparty-has-lawyer-or-their-paper: pass
  gate-4-gdpr-document: pass
restated_and_confirmed: true
restated_at: 2026-04-27T14:32:00Z
```

The `gates_evaluation:` block is the structured complement to `triage_gate_passed: bool` — a downstream test (per issue #19 M2) asserts every drafted artifact carries it AND the values match the SKILL.md gate evaluation logic.

## Open extensions (runbook scope)

The runbook from issue #19 should also produce four sister contracts (same conversational-elicitation discipline, different domain fields):

- `accounting-intake-contract.md` — HMRC matter type, period, qualifying-activity claim type, FTE counts, founder-personal vs company-side.
- `equity-intake-contract.md` — current cap table as structured rows, share-class breakdown, SEIS/EIS status, AA application date.
- `fundraise-intake-contract.md` — round size GBP, planned signature date, AA application date, investor counsel y/n, lead investor identity, qualifying-trade VCM3000 audit date.
- `hire-intake-contract.md` — role, full/part-time, expected duration, exclusivity, equipment/premises, substitution, CEST output capture.

All five contracts share the F1 / F4 / F5 fields verbatim; the per-skill specifics extend. **None of the five is a form for the founder to fill.** Each is a structured destination shape for a conversational elicitation the skill drives.
