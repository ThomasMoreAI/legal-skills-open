# Worked Example — DPA Art. 28 review (REVIEW_QUICK)

An end-to-end `REVIEW_QUICK` run: mode routing → intake → Art. 28(3) coverage table → recommendation.
Inputs are illustrative; substance reflects the skill's reference material at authoring time.

---

## User prompt

> "Our vendor sent us their standard DPA for an EU SaaS analytics tool. We're the controller. Can we
> sign it? Quick check please — here's the text." *(attaches a short processor-favourable DPA)*

---

## Mode routing + intake

- **Mode:** `REVIEW_QUICK` (sign / no-sign decision, short turnaround).
- **Roles:** Controller = the user's company; Processor = the SaaS vendor. Confirmed — not a
  joint-controller pattern (vendor processes only on documented instructions).
- **Perspective:** controller-favourable.
- **Language:** EN.
- **Transfers:** Vendor discloses a US-based sub-processor for hosting → transfers **in scope** →
  `references/sccs-module-guide.md` loaded.
- **Special categories:** None indicated.

`references/art28-3-checklist.md` + `workflows/review-quick.md` loaded.

---

## Art. 28(3)(a)–(h) coverage

| Art. 28(3) | Obligation | Verdict | Reason |
|---|---|---|---|
| (a) | Process only on documented instructions (incl. transfers) | **WEAK** | Instruction clause present but silent on transfers-on-instruction |
| (b) | Confidentiality commitment for authorised persons | **PASS** | Personnel confidentiality covered |
| (c) | Art. 32 security measures | **GAP** | Annex 2 TOMs referenced but **not attached** |
| (d) | Sub-processor conditions | **WEAK** | General authorisation, but **no objection right** for the controller |
| (e) | Assist with data-subject rights | **PASS** | Assistance clause adequate |
| (f) | Assist with Art. 32–36 (security, breach, DPIA) | **WEAK** | Breach notice "without undue delay" — no fixed hour target |
| (g) | Delete/return at end + delete copies | **PASS** | Return-or-delete choice given to controller |
| (h) | Provide audit info + allow audits | **WEAK** | Audit limited to a third-party report only; no on-site right |

**Chapeau & framing:** subject matter, duration, nature, purpose present; **categories of data subjects
under-specified** in Annex 1.

**SCC adequacy (transfers):** DPA states "Parties will rely on SCCs" but **does not specify the module,
Annexes I–III, or a TIA**. As drafted, the transfer safeguard is **not yet operative**.

---

## Top 3 issues

1. **Annex 2 (TOMs) missing** — fails Art. 28(3)(c) + Art. 32 as drafted. Blocker.
2. **SCCs referenced but not executed** — no module / Annexes / TIA → transfers unprotected. Blocker.
3. **No sub-processor objection right** — controller can't object to new sub-processors (Art. 28(3)(d)).

## Recommendation

> **Do not sign as is.** Two blockers (missing TOMs; SCCs not operative). Request: (1) the completed
> Annex 2 TOMs; (2) the specific SCC module + populated Annexes I–III + confirmation of a TIA;
> (3) a sub-processor objection mechanism. Items (a), (f), (h) are negotiation polish — escalate to
> `REVIEW_NEG` if the vendor pushes back and the contract value warrants clause-by-clause work.
>
> **Practitioner's note:** send the three blockers as the must-haves before signature; treat the
> WEAK items as a secondary ask. Confirm classification and the transfer position with counsel before
> reliance — this is structured analysis, not legal advice.

---

*This example shows the REVIEW_QUICK path. `DRAFT`, `REDLINE`, `REVIEW_NEG`, and `JOINT_CONTROLLER`
modes follow their own output structures (see `SKILL.md`) and draw on `templates/` and `workflows/`.*
