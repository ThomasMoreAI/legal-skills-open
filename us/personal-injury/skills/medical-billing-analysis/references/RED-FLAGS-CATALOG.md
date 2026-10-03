# Red Flags Catalog

Stable-ID taxonomy of issues to surface in the Red Flags table of the output. Loaded by Step 6 of the parent SKILL.md.

**How to use.** When you identify a flag, record it in the output table with: ID | Name | Detail (specifics from this case) | Source (doc-label, p. N, Bates) | Suggested Attorney Action. IDs are stable so memos, deposition outlines, and demand-package cross-references can refer to them without ambiguity. Do not invent new IDs in a memo; if a finding doesn't fit, add it under the closest category and label `[NEW PATTERN — review needed]`.

**Severity.** Each row marked H (high — likely material to damages or admissibility), M (medium — meaningful but contained), L (low — note for completeness).

---

## A. Billing-Integrity Flags

| ID | Name | Pattern | Example | Suggested Action | Sev |
|---|---|---|---|---|---|
| RF-01 | **Unbundling** | Component CPTs billed separately when a comprehensive code exists; suspect modifier `-59` / X-modifier overrides | Surgical tray code billed alongside the inclusive procedure CPT | Cross-check NCCI PTP file `[VERIFY]`; flag for billing expert | H |
| RF-02 | **Upcoding (E/M)** | E/M level billed exceeds documented MDM or time | 99205 billed for a chart entry showing one self-limited problem and no data review | Pull the exact MDM/time language; flag for coding audit | H |
| RF-03 | **Upcoding (procedure)** | Procedure code at higher intensity than the operative note describes | "Complex" repair code with a note describing simple closure | Quote operative-note language; flag for billing expert | H |
| RF-04 | **Duplicate billing** | Same CPT, same date, same provider, same patient — billed twice; or facility + professional both billing the global service | Lab panel billed and unbundled components also billed separately | Identify pair; mark for write-off demand or billing dispute | H |
| RF-05 | **Phantom billing** | A charge with no corresponding chart entry on the date of service | DME line item with no order, dispense record, or note | Cite the absent record; recommend records subpoena or strike | H |
| RF-06 | **Split-date billing** | A single encounter split across two service dates to evade limits | Rehab session billed across two days when the note shows one | Flag for billing expert | M |
| RF-07 | **Add-on without primary** | Add-on CPT billed without the required primary code | +90785 (interactive complexity) billed without underlying psychotherapy code | Verify add-on edit pairing `[VERIFY]` | M |
| RF-08 | **Modifier `-25` overuse** | E/M billed with every minor procedure as if always separately identifiable | Pattern across many encounters | Trend analysis; OIG Work Plan area | M |
| RF-09 | **Modifier `-59`/X overuse** | NCCI override modifier on most claim pairs | Pattern suggests systemic unbundling | Flag for billing expert | H |
| RF-10 | **Professional/technical double-bill** | Same entity bills global plus `-26` and `-TC` | Imaging center billing all three components | Identify in EOB; flag duplicate | H |

---

## B. Reasonableness Flags

| ID | Name | Pattern | Example | Suggested Action | Sev |
|---|---|---|---|---|---|
| RF-11 | **Chargemaster-only billing** | No payer adjudication; chargemaster is the bill | Self-pay or LOP without payer EOB | Apply UCR benchmark methodology (`REASONABLENESS-METHODOLOGY.md`); flag for billing expert | H |
| RF-12 | **LOP-inflated billed amounts** | Billed amounts under LOP materially exceed market | Pain-management injection at 5× MPFS, all under LOP | Tag every LOP line; pull jurisdictional admissibility law `[VERIFY]` | H |
| RF-13 | **Out-of-network opportunism** | OON-only providers in a chain of LOP referrals | All imaging at OON facility despite in-network options | Flag referral-source disclosure | M |
| RF-14 | **Surprise billing** | Balance bill for emergency or for OON at in-network facility | ER physician balance-bill | Apply No Surprises Act analysis `[VERIFY]`; balance may be uncollectable | M |

---

## C. Referral-Pattern / Structural Flags

| ID | Name | Pattern | Example | Suggested Action | Sev |
|---|---|---|---|---|---|
| RF-15 | **Self-referral pattern** | Same-owner ASC, imaging, PT, or pharmacy in a tight referral loop | Treating physician owns the imaging center used | Hand off to `stark-law-aks-compliance`; preserve disclosure questions for deposition | H |
| RF-16 | **Volume-bonus referral indication** | Compensation tied to referral volume signals AKS exposure | Documents (if produced) showing volume-based comp | Hand off to `conducting-anti-kickback-analysis`; preserve depo questions | H |
| RF-17 | **Exclusive-referral chain** | Same set of providers used across many cases for the same firm | Pattern visible across multi-case practice | Flag for impeachment / bias cross-examination | M |

---

## D. Documentation Flags

| ID | Name | Pattern | Example | Suggested Action | Sev |
|---|---|---|---|---|---|
| RF-18 | **Charge without corresponding record entry** | Bill line with no clinical documentation that day | "OV 99214" billed; chart shows no encounter | Cite absence; demand corrected statement or strike | H |
| RF-19 | **Copy-paste cloning** | Identical narrative across multiple visits (vital signs, exam findings, plan) | Same paragraph in 12 PT notes | Quote the duplicates; cross-examine treater | M |
| RF-20 | **E/M documentation insufficient for level** | Chart does not support MDM/time required by E/M level billed | 99214 with no documented MDM elements | Cross-reference `CODE-VALIDATION.md`; flag for coding audit | H |
| RF-21 | **Late addenda / signature timing** | Addenda added after request for records or near litigation milestones | Addendum signed three weeks after DOS | Note timing; preserve metadata; cross-examine | M |
| RF-22 | **Boilerplate causation language** | Identical "more likely than not caused by the subject incident" sentence across providers | Same exact phrase in 5 different practice notes | Cross-examine for individualized analysis | M |

---

## E. Causation Flags

| ID | Name | Pattern | Example | Suggested Action | Sev |
|---|---|---|---|---|---|
| RF-23 | **Treatment gap > 30 days** | Material gap between incident and first treatment, or within course of treatment | 6-week gap between ER and first PT visit | Get client explanation in Checkpoint B; surface for opposing counsel preemption | H |
| RF-24 | **Treatment burst before milestone** | Sudden uptick in treatment frequency before deposition, demand, or mediation | 3 visits/week starting 30 days pre-deposition | Plot frequency over time; cross-reference deposition/demand calendar | M |
| RF-25 | **Mechanism inconsistency** | Different mechanism narratives across providers | "Side-impact" in ER vs. "rear-end" in PT intake | Quote each; impeachment material both ways | H |
| RF-26 | **Pre-existing same-body-part treatment not distinguished** | Records show prior care to claimed body part; current bill silent on aggravation vs. new injury | Prior lumbar PT; current bill treats lumbar pain as wholly new | Demand causation/aggravation opinion from treater; recategorize damages | H |
| RF-27 | **Missing contemporaneous causation statement** | No treating physician statement linking injuries to incident in the contemporaneous record | First causation statement appears in a litigation-only narrative report | Pull narrative reports; flag late-emerging opinions | H |
| RF-28 | **Symptom-onset inconsistency** | Onset described as immediate at one provider, delayed at another | "Immediate" in ER; "next morning" in chiro intake | Quote both; impeachment risk | M |

---

## F. IME / Peer-Review Flags

| ID | Name | Pattern | Example | Suggested Action | Sev |
|---|---|---|---|---|---|
| RF-29 | **Unaddressed contrary IME opinion** | IME concludes pre-existing or non-causation; treaters do not address | IME finds degenerative cause; treaters silent | Develop rebuttal via `expert-medical-record-omissions`; consider re-evaluation | H |
| RF-30 | **Treater inconsistency with IME** | Treater opinion shifts after IME without documented basis | Treater agrees pre-existing on follow-up note post-IME | Quote shift; cross-examine | H |
| RF-31 | **IME omission / selective review** | IME based on partial records; key positive findings omitted | IME report omits MRI showing herniation | Use `expert-medical-record-omissions` workflow | H |

---

## G. Lien / Collateral-Source Flags

| ID | Name | Pattern | Example | Suggested Action | Sev |
|---|---|---|---|---|---|
| RF-32 | **Medicare conditional payments not requested** | Client is Medicare-eligible; no CMS conditional payment letter on file | Patient over 65; no BCRC letter | Hand off to `lien-resolution-summary`; do not settle without CPL `[VERIFY]` | H |
| RF-33 | **ERISA plan not notified** | Plan reimbursement rights present; plan not put on notice | EOBs from self-funded ERISA plan; no notice file | Hand off to `lien-resolution-summary`; *McCutchen* / *FMC v. Holliday* `[VERIFY]` | H |
| RF-34 | **Hospital lien timing/perfection defect** | State hospital lien filed late or not perfected per statute | Lien filed beyond statutory window | Cite statute `[VERIFY]`; potential lien defeat | M |
| RF-35 | **Subrogation double-recovery exposure** | Same expense reflected in both medical specials and a paid lien | Bill paid by health insurer also presented as out-of-pocket | Reconcile to EOB; net-to-client correction | M |

---

## Adding a Flag Not in This Catalog

If a finding doesn't match any ID:
1. Use the closest category's letter (A–G).
2. Mark the row `[NEW PATTERN — review needed]` in the Suggested Action column.
3. Note in the memo's "Open Items" section that the catalog should be updated post-review.

Do not silently invent a new permanent ID. The catalog is the source of truth across all skills that consume it.
