# review-contract — Reference

Deeper per-clause guidance and a fully worked review example. The SKILL.md is the protocol; this file is the playbook annex it points to.

---

## Per-clause deep-dive table

| Clause | Standard "ask" position | Acceptable range | Common counterparty pushback | Sample fallback |
|---|---|---|---|---|
| **Limitation of Liability** | Mutual cap = 12 mo. fees; cyber sub-cap = 24 mo. fees or 2x general | Cap 6–12 mo., cyber cap ≥ 1.5x general | "We never go above 6 mo." | Accept 6 mo. general IF cyber sub-cap holds at 12+ mo. AND IP/confidentiality carved out |
| **Indemnification (IP)** | Vendor defends + indemnifies for IP infringement; control of defense; settlement consent | Defense control with consent-not-unreasonably-withheld | "We only refund unused fees" | Require modify/replace/refund AND indemnity for third-party IP claims, capped at general cap |
| **Indemnification (data breach)** | Vendor indemnifies for breach caused by its security failure; uncapped or at cyber sub-cap | At minimum cyber sub-cap level, mutual notice | "Breach indemnity is capped at general cap" | Move breach indemnity to cyber sub-cap; require regulatory-fine reimbursement carveout |
| **DPA** | Executed concurrent with MSA; SCCs for cross-border; 30-day sub-processor notice with right-to-object | DPA exists; sub-processor notice 14–30 days | "Sub-processors listed on website, no notice" | Require email push notification (not site-pull); 14 days minimum; right to terminate without penalty if material objection |
| **BAA** (PHI) | Required if any PHI; HIPAA Security Rule + Breach Notification Rule (60 days) | None — BAA is mandatory or no PHI flows | "We're not a Business Associate" | Walk away if PHI involved — no negotiation; or contractual prohibition on PHI ingress |
| **Right-to-audit** | Once/year, 30-day notice, NDA auditor, vendor-borne if material findings | SOC 2 Type II report in lieu of audit acceptable; pen-test summary annually | "SOC 2 only, no third-party audits" | Accept SOC 2 Type II + annual pen-test summary + right-to-audit triggered by incident |
| **Data residency** | Contractual commitment to specified region(s); change requires customer consent | Region commitment with 90-day notice for change | "Best-effort, no commitment" | Require contractual residency for data-at-rest; processing transit allowed with encryption |
| **Sub-processor change** | 30-day prior notice; right to object; termination without penalty if material | 14–30 days; documented objection process | "List on website, change anytime" | 14-day push notice via email; termination with refund of prepaid unused fees |
| **IP assignment (contractor)** | Work product assigned; pre-existing IP carved out; OSS contributions excluded | Assignment of deliverables only; explicit pre-existing schedule | "Everything you touch is ours" | Schedule of pre-existing IP; OSS license carve-out; assignment limited to deliverables defined in SOW |
| **Insurance** | Cyber-liability ≥ $5M; tech E&O ≥ $5M; CGL $2M; named additional insured | Cyber ≥ $2M for sub-$1M deals, ≥ $10M for enterprise | "We have GL only" | Required cyber-liability before go-live; COI annually; 30-day cancellation notice |
| **Governing law** | PR for PR-domiciled customer; DE/NY for US enterprise | Mutual home-state OR neutral (DE) | "Our home state, no exception" | Trade governing law for venue (or vice-versa); insist on PR Ley 75 carveout if dealer relationship |
| **PR Ley 75** (dealer protection) | Explicit acknowledgment if PR-domiciled distributor/dealer; just-cause termination | Cannot be waived for PR dealer relationships | Often missing entirely | Add Ley 75 acknowledgment; just-cause termination; severance formula reference |
| **Bilingual contracts** | English controls for negotiation; Spanish translation provided for PR signatory | Either language controls; signed bilingual addendum if required | "English-only, no Spanish version" | Provide Spanish courtesy translation; English controls; PR consumer disclosures in Spanish per local law |

---

## Worked example: SaaS MSA review (cybersecurity vendor processing personal data)

**Scenario:** the operator (PR-domiciled cybersecurity SaaS founder) is the **customer** evaluating "AcmeAnalytics" — a US-based SaaS analytics vendor that will ingest end-user behavioral data (PII, no PHI) from the operator's cybersecurity dashboard. Annual contract value: $48,000. AcmeAnalytics provided their standard MSA. Playbook (`legal.local.md`) defines positions for LoL, indemnification, DPA, IP, data residency, governing law.

### Findings — three representative clauses

#### Finding 1 — Limitation of Liability (RED)

**Clause read:** §11.1 — "In no event shall either party's aggregate liability exceed the fees paid by Customer in the three (3) months preceding the event giving rise to the claim. This cap applies to all claims, including those arising from data breach, security incident, or violation of data protection laws."

**Playbook position:** `[Playbook §4.2]` — General cap ≥ 12 months fees; **separate cyber sub-cap ≥ 24 months fees** for breach/security/data-protection claims.

**Deviation:** Cap is 3 mo. (vs. playbook 12 mo. minimum) AND cyber claims swallowed by general cap (vs. playbook required separate sub-cap).

**Severity:** **RED** — triggers two cybersec RED criteria simultaneously: cap < playbook floor AND no cyber sub-cap.

**Cyber-exposure sanity check:** Estimated 50,000 records at risk × $165/record (IBM 2024 baseline) = **$8.25M floor exposure**. Current cap = $48K × 3/12 = **$12,000**. Cap is 0.15% of floor exposure — catastrophic gap.

**Recommended redline (with playbook citation):**

> "§11.1 Each party's aggregate liability under this Agreement shall not exceed the **~~three (3)~~ twelve (12) months** of fees paid by Customer preceding the event. **Notwithstanding the foregoing, Vendor's liability for breach of its data-protection or information-security obligations under §7 (Security) and §8 (Data Protection) shall be capped at the greater of (a) twenty-four (24) months of fees or (b) US$5,000,000 [`Playbook §4.2 cyber sub-cap`]. Liability for IP infringement indemnity, breach of confidentiality, and gross negligence/willful misconduct is uncapped [`Playbook §4.3 carveouts`].**"

**Fallback 1:** General cap 6 mo. (below playbook but accept) IF cyber sub-cap holds at 12 mo. AND IP/confidentiality/willful misconduct carved out.

**Fallback 2 (walk-away):** Vendor refuses any cyber sub-cap above 3 mo. → escalate to outside counsel; recommend declining unless vendor names Customer as additional insured on $5M+ cyber-liability policy with direct-action endorsement.

---

#### Finding 2 — Data Processing Addendum (RED)

**Clause read:** §8.4 — "Vendor may engage sub-processors at its sole discretion. A current list is maintained at acmeanalytics.com/subprocessors. Customer's continued use constitutes consent." No DPA attached.

**Playbook position:** `[Playbook §6.1]` — DPA executed concurrent with MSA when personal data processed. Sub-processor changes require 30-day prior email notice, right to object, termination without penalty if material objection.

**Deviation:** No DPA at all (playbook hard requirement when PII flows). Sub-processor notice mechanism is pull-based (website), not push-based (email); no objection right; no termination right.

**Severity:** **RED** — triggers cybersec RED criterion "personal data processed with no DPA offered." Also exposes the operator to GDPR Art. 28 violation (data controller-processor contract required) and PR Ley 111 notification non-compliance risk.

**Recommended redline:**

> "§8.4 **The parties shall execute the Data Processing Addendum attached as Exhibit C concurrent with this Agreement and prior to any Processing of Personal Data [`Playbook §6.1`]. The DPA shall include Standard Contractual Clauses for any cross-border transfer.** Vendor may engage sub-processors **upon thirty (30) days prior written email notice to Customer's designated privacy contact. Customer may object on reasonable grounds; if objection cannot be resolved within fifteen (15) days, Customer may terminate the affected services without penalty and receive a pro-rata refund of prepaid unused fees [`Playbook §6.2 sub-processor clock`].**"

**Fallback 1:** Accept 14-day notice (vs. playbook 30) IF email-push notification AND termination right preserved.

**Fallback 2:** If vendor refuses DPA → walk away. DPA is non-negotiable per playbook AND GDPR/CCPA legal requirement; no business case overrides this.

---

#### Finding 3 — Governing Law / PR Ley 75 (YELLOW)

**Clause read:** §15.2 — "This Agreement shall be governed by the laws of the State of Delaware. Exclusive venue: state and federal courts located in New Castle County, Delaware."

**Playbook position:** `[Playbook §9.1]` — For PR-domiciled customer, prefer PR law + PR venue; acceptable fallback: mutual neutral (DE law OK) IF venue is reciprocal (each party sues in the other's home jurisdiction). `[Playbook §9.3]` — If counterparty relationship has dealer/distributor characteristics, add Ley 75 acknowledgment.

**Deviation:** Vendor unilaterally picks DE law + DE venue (no reciprocity). Customer would have to litigate in DE for any claim. **No Ley 75 issue here** — the operator is the customer, not a PR dealer of Vendor's product, so Ley 75 does not apply (call this out explicitly so the user knows it was checked).

**Severity:** **YELLOW** — outside preferred but within market range; pure venue burden, not regulatory.

**Recommended redline:**

> "§15.2 This Agreement shall be governed by the laws of the State of Delaware **without regard to conflict-of-laws principles**. **Each party may bring suit in the state or federal courts located in the other party's principal place of business; each party consents to personal jurisdiction in such venue [`Playbook §9.1 reciprocal venue fallback`].** Notwithstanding the foregoing, **either party may seek injunctive relief in any court of competent jurisdiction** to protect its IP or Confidential Information."

**Fallback 1:** DE law, DE venue, BUT Customer-initiated suits may also proceed in PR if Customer is plaintiff (asymmetric — accept if no other option).

**Fallback 2:** Trade venue concession for an unrelated win — e.g., extended termination-for-convenience notice or improved cyber sub-cap.

---

### Negotiation strategy summary (for this MSA)

- **Tier 1 (deal-breakers):** Findings 1 (cyber sub-cap) and 2 (DPA). Cannot sign without both addressed.
- **Tier 2 (strong preferences):** Reciprocal venue (Finding 3), 30-day sub-processor email notice.
- **Tier 3 (concession candidates):** Accept DE law if reciprocal venue granted; accept 6-mo. general cap if cyber sub-cap = 24 mo.

**Lead with:** Findings 1 + 2 as joint package — frame as "these are the two items that block signature." Trade Finding 3 venue concession to grease Tier 1 wins. Escalate to outside counsel only if vendor refuses any cyber sub-cap or refuses DPA.

---

## Notes on using this reference

- Every finding in a real review must cite either `[Playbook §X.Y]` or `[DEFAULT — market standard]`. Never produce a finding without citation.
- The worked example uses three clauses for brevity; a real MSA review will produce 8–15 findings.
- When playbook is silent on a clause, label `[DEFAULT]` and source the position from the per-clause table above.
- If the per-clause table conflicts with a loaded `legal.local.md`, the loaded playbook always wins.
