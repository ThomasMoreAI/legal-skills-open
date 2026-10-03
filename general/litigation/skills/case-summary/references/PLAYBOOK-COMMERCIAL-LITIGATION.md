# Commercial Litigation Playbook

---
practice_area: commercial-litigation
triggers:
  filenames: [contract, agreement, MSA, SOW, PO, invoice, NDA, LOI, term-sheet, termination, default, cure, demand, ledger, remittance]
  content_signals: [breach of contract, fiduciary duty, unjust enrichment, quantum meruit, specific performance, consequential damages, liquidated damages, force majeure, condition precedent, material breach, covenant, indemnification, warranty, UCC, good faith and fair dealing]
defers_to:
  - deposition-summary: when depositions appear in the corpus
  - discovery-summary: when interrogatory/RFP/RFA responses appear
  - case-intake-initial-fact-memo: when the user wants a pre-suit fact memo
  - demand-letter: when the user's objective is pre-suit notice or cure demand
---

## Dimension extensions

### Parties & posture
Identify contracting entities with exact legal names (often differ from trade names). Capture guarantors, assignees, successors-in-interest, and notice-address/registered-agent information. Forum-selection and arbitration clauses belong here.

### Timeline
Subdivide into: formation, performance, notice/cure period, alleged breach, damages crystallization, mitigation window. Flag every contract-specified deadline (notice, cure, termination) against actual conduct.

### Evidence inventory
Expected types: the governing agreement(s), amendments, side letters, purchase orders, invoices, statements of work, project-management tickets, delivery receipts, chain-of-custody records, contemporaneous correspondence (email, Slack, texts), payment records and chargebacks, remedy-performance attempts.

### Claims & legal theories
Breach of contract (formation, performance, breach, damages), breach of the implied covenant of good faith and fair dealing, breach of warranty (express/implied/UCC), fraud in the inducement, fiduciary breach, unjust enrichment / quantum meruit, tortious interference, declaratory relief. For UCC transactions add 2-207, 2-313, 2-314, 2-315, 2-608, 2-709, 2-710, 2-712, 2-713, 2-714, 2-715 as applicable.

### Exposure / remedies
Expectation damages (direct, consequential, incidental), reliance damages, restitution / unjust enrichment, liquidated damages (if enforceable), specific performance, declaratory relief, attorney's fees (if contractual or statutory basis), prejudgment interest.

### Defenses
Failure of condition precedent, prior material breach by plaintiff, waiver, estoppel, ratification, accord and satisfaction, force majeure, impracticability/frustration, SOL (contract SOL often 3–6 years; UCC 2-725 is 4 years), unclean hands, economic-loss rule, parol-evidence rule, statute of frauds, unconscionability.

### Red flags & open threads
Admissions in emails ("we didn't deliver on time"), post-alleged-breach conduct inconsistent with claim (continued acceptance, continued payment), failure to mitigate, contractual-notice failures on the plaintiff side, forum/arbitration clauses that bar the chosen forum.

## Queries

### Parties & posture
- `"governing contract agreement parties entity"`
- `"forum selection arbitration venue clause"`
- `"notice address registered agent"`
- `"guarantor assignment successor"`

### Timeline
- `"contract formation effective date"`
- `"notice cure period expiration"`
- `"alleged breach date repudiation"`
- `"termination notice wind-down"`

### Evidence inventory
- `"purchase order invoice statement of work"`
- `"delivery acceptance rejection"`
- `"payment remittance chargeback"`
- `"correspondence email text message"`

### Claims & legal theories
- `"breach of contract material failure perform"`
- `"implied covenant good faith fair dealing"`
- `"breach of warranty UCC express implied"`
- `"fraud misrepresentation reliance"`
- `"unjust enrichment quantum meruit"`
- `"fiduciary duty breach"`
- `"tortious interference prospective advantage"`

### Exposure / remedies
- `"expectation damages lost profits consequential"`
- `"liquidated damages clause enforceability"`
- `"reliance out-of-pocket"`
- `"specific performance unique"`
- `"attorneys fees prevailing party"`
- `"prejudgment interest rate accrual"`

### Defenses
- `"condition precedent failure"`
- `"prior material breach excuse"`
- `"waiver estoppel ratification"`
- `"accord and satisfaction settlement"`
- `"force majeure impracticability frustration"`
- `"statute of limitations accrual discovery rule"`
- `"parol evidence integration clause"`
- `"statute of frauds writing signed"`
- `"unconscionable adhesion"`

### Procedural status
- `"notice of claim demand letter response"`
- `"arbitration demand mediation agreement"`
- `"motion to compel arbitration"`

### Red flags
- `"continued performance after breach acceptance"`
- `"email admission acknowledgment fault"`
- `"failure to mitigate reasonable efforts"`

## Output sections

### Contract Framework — slots into IV Claims & legal theories

| Provision | Contract § | Plaintiff reading | Defendant reading | Evidence cited |
|---|---|---|---|---|
| | | | | |

Open with the 3–6 governing provisions in dispute. Quote the operative language exactly. Map each to the element it bears on.

### Breach Analysis — slots into IV Claims & legal theories

For each claim:

1. **Claim:** [e.g., Breach of MSA § 5.2]
2. **Elements:** formation, performance by plaintiff, breach by defendant, damages
3. **Evidence per element:** [Citations]
4. **Gap:** [Any element lacking evidence]

### Damages Methodology — slots into VI Exposure/remedies

**Expectation damages:**
- Direct: [Computation with citations]
- Consequential: [Foreseeability and causation chain, with citations]
- Incidental: [As itemized]

**Mitigation:**
- Reasonable efforts undertaken: [Citations]
- Mitigation credit applicable: [$ range]

**Alternative measures considered:** reliance, restitution — used only where expectation is unprovable.

**Statutory / contractual enhancements:**
- Liquidated damages clause: [Contract §, enforceability assessment]
- Fees: [Contractual or statutory basis — do not assert without basis]
- Prejudgment interest: [Rate, accrual date, authority `[VERIFY]`]

### Contractual Remedies — slots into VI Exposure/remedies

- Specific performance (availability depends on uniqueness of subject matter)
- Injunction (where the contract provides equitable-relief consent)
- Declaratory relief (where rights are contested prospectively)

## Quality checklist additions

- [ ] Each governing contract provision quoted exactly, not paraphrased
- [ ] Each claim element has at least one evidentiary citation
- [ ] Damages computation shows math and assumptions
- [ ] Mitigation addressed for every damages category
- [ ] Fee-shifting basis identified (contractual or statutory) or the claim is dropped
- [ ] Forum-selection / arbitration clause analyzed and forum selection justified
- [ ] Statute-of-limitations accrual date stated

## Remedies / exposure methodology

Commercial damages are expectation-measured unless expectation is unprovable or the plaintiff elects otherwise (reliance or restitution). Expectation damages = the position the plaintiff would have occupied had the defendant performed, minus costs avoided by the breach, minus amounts reasonably mitigable, plus incidental and consequential damages (foreseeable and proven).

Consequential damages require a Hadley v. Baxendale showing: the defendant knew or should have known of the special circumstances at contracting. Many commercial contracts exclude consequentials — the playbook always checks for such a waiver and flags it.

Liquidated-damages clauses are enforceable only if (a) actual damages were difficult to estimate at contracting and (b) the stipulated amount is a reasonable forecast, not a penalty. The playbook checks both prongs and cites authority `[VERIFY]` before relying on the clause.

Attorney's fees are unavailable absent a contractual or statutory basis. The playbook refuses to assert fee recovery without locating the basis in the record. Prejudgment interest rates are jurisdiction-specific — flag the governing statute and rate with `[VERIFY]`.

Specific performance and injunctive relief are equitable remedies available only where the subject matter is unique or the contract so provides. The playbook reports when the factual record supports such a remedy and when it does not.
