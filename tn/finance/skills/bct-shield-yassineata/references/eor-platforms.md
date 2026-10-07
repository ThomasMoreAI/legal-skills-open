# EOR and payout platforms — Deel, Remote, Oyster, Payoneer, Wise

## Why this file exists

A growing number of Tunisian developers are paid through **EOR platforms** (Employer Of Record) such as **Deel**, **Remote**, **Oyster**, **Multiplier**, or via **Payoneer** / **Wise** as pure payout rails. These platforms look the same from a banking perspective ("euros land in my account") but they are **legally different**, and the difference matters for:

1. How the BCT views the inflow.
2. Whether the income is **employment** or **service-export revenue**.
3. What you owe to the fisc (IRPP/IS) and to the CNSS.
4. What paperwork you must keep to survive an audit.

> ⚠️ Most online advice does not separate these cases. Reading this file once will save you a year of confusion.

---

## The four buckets

### Bucket 1 — Genuine EOR contract (employment relationship)

**Platforms:** Deel (EOR product), Remote, Oyster, Multiplier, Velocity Global.

**What it actually is:**
You are an **employee** of a local entity of the platform in the platform's jurisdiction (often Deel-NL, Deel-IE, Remote-PT, etc.). Your foreign client pays the platform; the platform employs you on paper and pays you a "salary" net of foreign payroll taxes.

**Implications for you in Tunisia:**

- The platform is your **legal employer abroad**. You sign an employment contract, not a service contract.
- The payment that lands in your Tunisian account is **net salary in foreign currency**, not service-export revenue.
- **You do not invoice anyone.** No facture, no TVA, no export-services VAT 0% mention.
- **The fisc still wants its money.** Foreign-employer salary received by a Tunisian tax resident is taxable in Tunisia under IRPP (worldwide-income principle for residents).
- **CNSS:** ambiguous. Some setups deduct social charges in the platform's country; some don't. Even when they do, you are still a Tunisian resident with a Tunisian social-protection gap. You may need to enrol in CNSS as an independent / non-salarié to be covered locally. [REQUIRES MANUAL LEGAL VERIFICATION: official Tunisian position on CNSS coverage of residents employed by foreign EORs, as of 2026]
- **BCT:** the inflow is foreign-source income of a Tunisian resident. Under the OLD regime in force (the December 2025 forex announcement is **not** yet operational — see `bct-circulaires.md`), the standard repatriation/conversion rules apply. Holding it in PPR Devises is fine for the standard window; long-term retention is not yet a guaranteed right.

**Documents to keep:**
- The EOR employment contract.
- Monthly payslips from the platform (Deel/Remote provides these).
- Bank credit advice in foreign currency.
- Annual income summary from the platform.

### Bucket 2 — EOR contractor / "Deel Contractor" product

**Platforms:** Deel (contractor product), Remote (contractor), Oyster (contractor).

**What it actually is:**
You sign a **service contract** with the platform or with the foreign client through the platform. You are **not** an employee — you are a self-employed contractor. The platform handles payments only.

**Implications for you in Tunisia:**

- You are providing **export of services** to a non-resident.
- **You must invoice.** Either you on patente real, or your SUARL.
- TVA: 0% (export of services) — see `mo7aseb/references/tva-tn.md`.
- Income is BIC/BNC / IS depending on your status.
- BCT: standard export-services treatment, OLD regime still in force in practice.

**Documents to keep:**
- The platform's contractor agreement.
- The end-client contract / SOW if separate.
- Your **own invoice** issued to the platform (or to the end client — match what the contract says).
- Monthly Deel/Remote contractor statement.
- Bank credit advice.

### Bucket 3 — Marketplace platforms (Upwork, Toptal, Fiverr, Malt)

**What it actually is:**
You are a self-employed contractor; the platform is an intermediary that takes a commission. No employment relationship.

**Implications for you in Tunisia:**
- Same as Bucket 2 — export of services.
- **You invoice the platform or the end client** depending on the platform's setup:
  - Upwork: invoice Upwork (Upwork Global Inc, Delaware).
  - Toptal: invoice Toptal LLC.
  - Fiverr: invoice Fiverr International Ltd.
  - Malt: depends on the contract structure.
- TVA 0% export.

### Bucket 4 — Pure payout rails (Payoneer, Wise, direct SWIFT)

**What it actually is:**
Just a money-movement service. Not your counterparty. The counterparty is whoever generated the payment upstream (client, platform).

**Implications:**
- Legal classification depends on the **upstream** relationship, not on Payoneer / Wise.
- If upstream is a foreign company paying for your services → export of services (Bucket 2/3 logic).
- If upstream is an EOR paying you a salary → Bucket 1 logic.
- Payoneer in particular: be careful about holding balances long-term in the Payoneer account itself. Under the OLD BCT regime, repatriation timelines apply once the money "leaves" the platform; before that the position is grey.

---

## Decision tree

```
Does the platform issue you a payslip (bulletin de paie) every month?
│
├── YES  → Bucket 1 (EOR employment). No invoicing. IRPP only, CNSS gap to plug.
│
└── NO   → Does the platform call you a "contractor" in writing?
          │
          ├── YES → Bucket 2 (EOR contractor). You invoice the platform.
          │
          └── NO  → Is it a marketplace (you find clients on it)?
                    │
                    ├── YES → Bucket 3 (Marketplace). You invoice per platform terms.
                    │
                    └── NO  → Bucket 4 (Pure rail). Trace upstream and apply 1, 2, or 3.
```

---

## Tax cheat-sheet by bucket

| Bucket | Invoice? | TVA | IRPP/IS | CNSS | Personal-asset exposure |
|---|---|---|---|---|---|
| 1 — EOR employment | No | N/A | Yes (worldwide income) | Plug the gap with TN CNSS independent enrolment | Standard (you are an individual) |
| 2 — EOR contractor | Yes | 0% export | Yes (BIC/BNC or IS via SUARL) | Independent CNSS class | Patente: high · SUARL: protected |
| 3 — Marketplace | Yes | 0% export | Yes | Independent CNSS class | Patente: high · SUARL: protected |
| 4 — Pure rail | Depends on upstream | Depends | Yes | Depends | Depends |

---

## Common traps

1. **"I'm on Deel, I don't need to declare anything in Tunisia."**
   False. Tax residence is Tunisia → worldwide income is taxable in Tunisia. Foreign-payroll tax withholding **does not** automatically eliminate your Tunisian filing duty. A bilateral tax treaty may grant a credit, but you still file.

2. **"Deel is paying me, so I don't need an invoice."**
   Only true under Bucket 1 (genuine employment). Bucket 2 (Deel Contractor product) still requires you to invoice — Deel acts as a payment processor in that case.

3. **"Payoneer is my bank, I'll leave the balance there."**
   Payoneer is not a bank, and holding balances offshore is in the grey zone under the OLD BCT regime that is still in force today (Dec 2025 announcement, no application decrees yet). When in doubt, repatriate within the standard window.

4. **"I'm on patente forfaitaire so I'll just declare the 3%."**
   At a typical Deel / Upwork income level for a dev (3–6k EUR/month ≈ 120–240k TND/year), you are far above the 50k TND **services** forfaitaire cap. You are silently ineligible. See `mo7aseb/references/regime-forfaitaire.md`.

5. **"I don't need CNSS, my Deel contract covers me."**
   It does not, in Tunisia. Deel's home-country payroll deductions do not give you CNSS rights in Tunisia. If you fall sick here, you have no `assurance maladie`. Plug the gap. See `mo7aseb/references/cnss.md`.

---

## Sources

- `bct-circulaires.md` (forex rules — and the Dec 2025 announcement caveat)
- `compte-devises.md` (PPR Devises account practical setup)
- `mo7aseb/references/tva-tn.md` (export-services VAT 0% mechanics)
- `mo7aseb/references/regime-forfaitaire.md` (50k TND services cap)
- `mo7aseb/references/cnss.md` (independent enrolment)
- `data/sources.json` → `bct-cir-1993-13`, `tunisia-forex-deregulation-dec-2025-announcement`
