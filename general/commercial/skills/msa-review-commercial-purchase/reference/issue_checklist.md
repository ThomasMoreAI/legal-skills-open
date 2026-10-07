# Commercial Purchase MSA Issue Checklist

This checklist drives Pass 2 of the review. Issues are organized into four tiers calibrated for commercial-purchase priorities:

- **Tier 1** — Always reviewed in detail. Covered in both `comprehensive` and `quick_triage`.
- **Tier 2** — Reviewed in detail in `comprehensive` only. In `quick_triage`, surfaced only when materially deviant.
- **Tier 3** — Drafting cleanliness; rarely material on their own.
- **Tier 4** — Industry-specific provisions (when `industry_context` indicates).

For each item, classify: **Present and standard** / **Present but unusual** / **Missing** / **N/A**.

Items marked with † are particularly perspective-sensitive — the same clause language reads very differently depending on which side the user is on. See `perspective_lens.md` for how to flip the lens.

## Tier 1 — Always reviewed in detail

### 1.1 Price and Payment Terms †

**What it is:** the pricing structure, payment timing, currency, and price-adjustment mechanisms.

**What "standard" looks like:**
- Pricing specified in the MSA (rate sheet, price list) or in PO/Order Form with MSA framework controlling.
- Payment terms typically net 30 to net 60 days from invoice, with industry variation (automotive often net 45-60; commodity supply often net 30; services with milestones tied to completion).
- Currency specified; any FX-adjustment mechanism in cross-border deals.
- Price-adjustment provisions typically tied to specific indices (raw-material indexes, CPI, agreed escalation) with caps and floors.
- Late payment interest (1-1.5% per month or statutory rate, whichever is lower).
- Buyer's right to set off undisputed invoices against amounts owed by supplier (often present, sometimes negotiated).

**What's unusual:**
- **Open-ended price adjustment without caps** — supplier's right to increase price based on supplier's cost increases without index reference or buyer approval. Flag as critical for buyer.
- **"Most favorable customer" or "most favored nation" pricing** — buyer's claim to receive supplier's best pricing; uncommon and operationally complex. Flag whenever present.
- **Cost-plus pricing without audit rights** — buyer pays supplier's cost plus a margin, without ability to verify the cost. Flag for buyer.
- **Raw-material pass-through with no cap** — pricing that adjusts dollar-for-dollar with raw-material costs. Flag for buyer.
- **Payment terms over 90 days** — beyond market in most industries; flag.
- **Penalty interest or compounded late fees beyond statutory maximum** — flag (excess unenforceable in many jurisdictions).
- **Acceleration of all unpaid amounts on minor breach** — flag as material; converts ordinary disputes into existential financial events.
- **Buyer's right to withhold payment without specific dispute mechanism** — favors buyer; flag for supplier.
- **Supplier's right to suspend deliveries on any past-due invoice** — favors supplier; flag for buyer.

### 1.2 Delivery, Shipping, Risk of Loss, and Title †

**What it is:** when supplier must deliver, where, how risk of loss passes, and when title transfers.

**What "standard" looks like:**
- Delivery dates specified in PO with MSA framework on lead times, late-delivery remedies, and force majeure exclusions.
- Risk of loss governed by Incoterms (FOB Origin, FOB Destination, EXW, DDP, etc.) or UCC default rules.
- Title typically passes on delivery (when risk of loss passes) but can be separated.
- Buyer's right to inspect at supplier's facility (varies by goods and industry).
- Late-delivery remedies typically include cover purchase (buyer's right to source from alternate supplier and charge difference to supplier), liquidated damages (carefully scoped to avoid penalty), or termination for material breach.
- Packaging and labeling standards specified or referenced.

**What's unusual:**
- **Indefinite delivery commitments** — "supplier will ship as soon as practicable" without firm dates. Flag as critical for buyer.
- **Risk of loss passing at supplier's loading dock without compensating arrangement** — favors supplier; flag for buyer (especially for international or high-value shipments).
- **Title passing at payment rather than delivery** — favors supplier (allows reclamation if buyer becomes insolvent); flag for buyer in deals where production is paid for in advance.
- **No remedy for late delivery** — flag as material for buyer.
- **Liquidated damages structured as penalties** (e.g., $1000/day with no relationship to actual harm) — may be unenforceable; flag.
- **Blanket release of supplier from delivery obligations during force majeure with no cap on duration** — flag for buyer; combine with no-buyer-termination-right and supply continuity becomes uncertain.
- **Buyer's right to reject without inspection** — favors buyer; flag for supplier.
- **Deemed acceptance on receipt without inspection opportunity** — favors supplier; flag as critical for buyer when goods require destructive testing or specialized inspection.

### 1.3 Acceptance, Inspection, and Rejection †

**What it is:** buyer's rights to inspect goods, the inspection period, and the consequences of acceptance vs. rejection.

**What "standard" looks like:**
- Inspection period typically 30 days from delivery, with industry variation (capital equipment may have longer; commodity goods may have shorter or "deemed accepted on receipt" with reservation of warranty rights).
- Buyer's right to reject for non-conformance with specifications, with prompt notice to supplier.
- Supplier's right to cure non-conformance (typically 30 days) before buyer's rejection becomes final.
- Buyer's right to revoke acceptance under UCC §2-608 for hidden defects discoverable only after acceptance, within reasonable time.
- Disposition of rejected goods (return at supplier's expense, hold for supplier's instruction, etc.).

**What's unusual:**
- **Inspection period under 7 days** — flag as material; can be critical for goods requiring testing.
- **"Deemed acceptance on receipt"** without express reservation of warranty rights — flag as critical for buyer; effectively eliminates inspection.
- **No supplier cure right** — flag for supplier; standard UCC default allows cure within reasonable time.
- **No revocation right beyond acceptance period** — flag for buyer in deals where defects may emerge in use.
- **Buyer's obligation to pay for rejected goods pending dispute** — favors supplier; flag for buyer.
- **"Final and binding" inspection by supplier or supplier's designated inspector** — flag as critical for buyer; eliminates buyer's independent inspection.

### 1.4 Warranties (Express and Implied) †

**What it is:** supplier's affirmative warranties about the goods, the disclaimer of other warranties, and the warranty period.

**What "standard" looks like:**
- **Express warranties (supplier):** goods conform to specifications; goods are free from defects in material and workmanship; supplier has good title; goods do not infringe third-party IP; goods comply with applicable laws and regulations.
- **Warranty period:** typically 12-24 months from delivery for general goods; 12 months from acceptance or installation for capital equipment; longer for buyer-specified-design goods. Industry variation (automotive often 12 months/12,000 miles; medical devices longer).
- **Disclaimer:** of all other warranties, express or implied, including merchantability, fitness for a particular purpose, and non-infringement (typically already covered by express warranties and IP indemnity). Disclaimer must satisfy UCC §2-316 requirements (conspicuous, in writing for written contracts).
- **Buyer warranties:** none typically required, though some MSAs include buyer warranties around buyer-furnished specifications and materials.
- **Pass-through warranties:** for components incorporated into buyer's products, supplier's warranties typically pass through to buyer's customers (with limitations).

**What's unusual:**
- **Missing express warranty of conformance to specifications** — flag as critical for buyer; without this, buyer has no contractual basis to reject non-conforming goods.
- **Missing express warranty of title** — flag as critical for buyer.
- **Missing warranty of legal compliance** — flag as material; buyer needs supplier to warrant that goods comply with applicable laws.
- **Warranty period under 12 months for capital equipment or critical components** — flag as material for buyer.
- **Disclaimer of implied warranties without satisfying UCC §2-316 safe-harbor language** — typically not effective; flag.
- **"AS IS" goods warranty** — favors supplier; flag as critical for buyer in any non-trivial purchase.
- **Disclaimer of warranty for buyer-furnished specifications** — typical and acceptable when buyer dictates specifications; flag if it extends beyond buyer's actual specifications.
- **No warranty pass-through to buyer's customers** — flag as material for buyer in component-supply deals.
- **Warranty remedies limited to repair/replace at supplier's option** — typical; flag if combined with no right to refund or rescission for repeated defective replacements.

### 1.5 Warranty Remedies †

**What it is:** what buyer is entitled to when goods fail warranty.

**What "standard" looks like:**
- **Repair, replace, or refund** at supplier's option (sometimes buyer's option, depending on negotiation).
- **Time limits** for warranty claims (notice within reasonable time; supplier response within stated period).
- **Continuing warranty** on repaired or replaced goods (warranty period extended for repaired/replaced portion).
- **Cover purchase rights** if supplier fails to cure within stated period (buyer can source from alternate supplier and charge supplier).
- **Out-of-warranty remedies** — typically refund of purchase price (with depreciation) or credit against future purchases.

**What's unusual:**
- **"Sole and exclusive remedy" language** for warranty failures — common but should not preclude UCC §2-719(2) remedy if exclusive remedy fails of essential purpose. Flag if combined with limitation of liability that swallows the warranty.
- **No supplier obligation to repair or replace defective goods** — flag as critical for buyer.
- **Warranty remedies capped at repair-replacement cost** without consequential damages for downtime — typical for goods purchases (different from services); flag if costs of repeated defects are operationally significant.
- **Repaired/replaced goods getting only the remainder of the original warranty period** — supplier-favorable; flag for buyer in deals where defective goods cause repeated replacement.
- **No cover-purchase rights** if supplier fails to cure — flag for buyer.

### 1.6 Intellectual Property and Indemnification †

**What it is:** allocation of IP rights (in the goods, in any tooling, in any improvements) and indemnification against third-party IP infringement claims.

**What "standard" looks like:**
- **Supplier IP:** supplier owns the IP in the goods (design, know-how, manufacturing process) unless the goods are designed to buyer's specifications, in which case ownership may be allocated differently.
- **Buyer-specified design:** if buyer provides specifications, buyer typically retains rights in those specifications and supplier warrants it has the right to manufacture per those specifications.
- **Tooling:** ownership specified — buyer-paid tooling typically vests in buyer; supplier-paid tooling typically vests in supplier; allocation should be explicit.
- **Improvements:** improvements developed during the relationship — ownership often allocated based on who paid for the development and what was the basis (general improvements to supplier's process vs. buyer-specific improvements).
- **IP infringement indemnity:** supplier indemnifies buyer against third-party IP infringement claims arising from the goods. Standard exceptions: buyer's modifications, combinations with buyer's products, buyer-furnished specifications.
- **Buyer indemnity:** buyer indemnifies supplier for IP claims arising from buyer-furnished specifications or buyer's combination/modification.

**What's unusual:**
- **No supplier IP indemnity** — flag as critical for buyer in any non-commodity goods purchase.
- **IP indemnity limited to US patents** — flag for buyer in deals where international markets are relevant.
- **Buyer-paid tooling vested in supplier without escrow or buyer access rights** — flag as critical for buyer in supply-continuity scenarios; if supplier fails or terminates, buyer may not be able to access the tooling.
- **All improvements vested in supplier** including those funded by buyer — flag for buyer.
- **All improvements vested in buyer** including those that incorporate supplier's pre-existing IP — flag for supplier.
- **Buyer indemnity scope extending beyond buyer's actual conduct** — flag for buyer.
- **No carve-outs to supplier IP indemnity** — favors buyer in some respects but creates uncertainty about supplier's coverage.

### 1.7 Limitation of Liability †

**What it is:** the cap on each party's aggregate liability and exclusion of damages categories.

**What "standard" looks like:**
- **Mutual cap** — typically expressed as the purchase price for the affected goods, the price of goods purchased in a defined period (e.g., the prior 12 months), or a fixed amount. Caps often vary by category (defective goods cap; total agreement cap).
- **Carve-outs** from cap typically include: confidentiality breach, indemnification obligations, gross negligence, willful misconduct, fraud, and bodily injury / death. Sometimes also: IP indemnification (often uncapped or super-capped), recall obligations.
- **Exclusion of consequential damages** typically mutual; standard carve-outs mirror cap carve-outs.
- **Industry variation** — automotive often has industry-standard exposure for warranty and recall; medical device has heightened exposure; commodity supply often has tight caps.

**What's unusual:**
- **Cap below the purchase price for the affected goods** — flag as critical for buyer.
- **Cap above the affected goods value but below 12 months of purchases** — flag as material for buyer in long-term supply.
- **Missing carve-out for IP indemnification** — flag as critical for buyer.
- **Missing carve-out for confidentiality, indemnification, gross negligence, willful misconduct, or bodily injury** — flag whichever side is disadvantaged.
- **Asymmetric caps in a mutual provision** — flag.
- **Cap that includes buyer's payment obligations** (drafting error) — flag.
- **Liquidated damages provisions** in addition to cap structure — flag.
- **Recall obligations not carved out from cap** in food/pharma/medical device contexts — flag as critical for buyer.

### 1.8 Term, Termination, and Supply Continuity †

**What it is:** how long the agreement lasts, how it renews, how it can be terminated, and what happens to supply commitments at end-of-term.

**What "standard" looks like:**
- **Term:** initial term commonly 1-5 years, with auto-renewal or expiration. Often shorter for commodity supply, longer for capital equipment programs and long-term supply commitments.
- **Termination for cause:** either party can terminate for material breach with notice and cure (typically 30-60 days).
- **Termination for convenience:** less common in supply MSAs than in services; sometimes buyer has convenience termination with proportional payment for in-process work.
- **Termination for insolvency:** standard; either party can terminate on the other's bankruptcy or insolvency.
- **Last-time-buy rights:** buyer's right to place a final order before supplier's discontinuation of the product, allowing buyer to stockpile for transition.
- **End-of-life notice:** supplier's obligation to provide advance notice before discontinuing a product (often 6-24 months).
- **Effect of termination:** supplier completes outstanding orders; tooling returned per ownership; spare parts obligation continues for stated period; survival of confidentiality, indemnification, payment, warranty, and limitation provisions.

**What's unusual:**
- **No supplier obligation on end-of-life notice** — flag as critical for buyer in single-source critical-supply or capital-equipment deals.
- **No last-time-buy rights** — flag as material for buyer.
- **No buyer access to tooling on supplier's termination** — flag as critical for buyer when buyer paid for tooling.
- **Supplier's right to terminate on minor buyer breach** — flag for buyer.
- **No spare parts obligation after end-of-production** — flag as material for buyer in capital equipment or long-life-cycle products.
- **Termination triggering cancellation charges or penalty payments** — flag.
- **Buyer's volume commitments triggering supplier's right to terminate if not met** — supplier-favorable; flag for buyer.
- **Supplier's obligation to continue supply during disputes** — favors buyer; flag for supplier (but standard for critical supply).

### 1.9 Supply Continuity, Capacity, and Force Majeure †

**What it is:** supplier's commitments to maintain supply, allocate capacity, and excuse non-performance during force majeure events.

**What "standard" looks like:**
- **Capacity allocation:** in long-term supply, supplier's commitment to allocate sufficient capacity to meet buyer's forecast or committed volumes.
- **Forecast vs. firm orders:** typical structure has buyer providing rolling forecasts (e.g., 12-month rolling, with first 90 days firm) with firm POs converting forecasts to commitments.
- **Force majeure:** mutual; excuses non-performance other than payment for events beyond reasonable control. Notice obligation; mitigation duty; termination right after extended FM.
- **Supplier failure / business continuity:** for critical supply, supplier obligated to maintain BC/DR plans, redundant facilities, or alternate sourcing arrangements.
- **Buyer's allocation right during FM:** supplier obligated to allocate available supply pro rata among customers during FM events affecting supply.

**What's unusual:**
- **Force majeure defined to include supplier's own operational failures** — flag as critical for buyer.
- **Force majeure with no termination right after extended duration** — flag as material for both sides.
- **No capacity-allocation commitment in long-term supply** — flag for buyer.
- **No business-continuity commitment in single-source critical supply** — flag as critical for buyer.
- **Supplier's right to allocate scarce supply at supplier's sole discretion** — flag for buyer.
- **Asymmetric force majeure** (excuses supplier's delivery but not buyer's payment, or vice versa) — typical and acceptable; flag if extreme.
- **No notice obligation during FM** — flag.

## Tier 2 — Reviewed in detail in `comprehensive` only

### 2.1 Confidentiality

Standard mutual confidentiality with carve-outs for publicly available information, prior knowledge, independent development, third-party receipt, and compelled disclosure. Term typically 3-5 years post-termination; longer for trade secrets in technical-supply relationships.

**Unusual:** missing entirely; one-sided when both parties share confidential information; no carve-out for trade secrets in technology-supply deals.

### 2.2 Change Orders and Modifications

**Standard:** changes to specifications, delivery schedules, or quantities require written change order; pricing adjustment for changes; supplier's obligation to honor reasonable changes vs. right to refuse extreme changes.

**Unusual:** unilateral change rights (either side); no pricing-adjustment mechanism for changes; "constructive change" provisions that allow one party to direct changes through informal communications.

### 2.3 Insurance Requirements

**Standard:** specified types and amounts (general commercial liability, products liability, professional liability where applicable, workers compensation, automobile if relevant); buyer added as additional insured on supplier's policies; certificates of insurance and endorsement provided.

**Unusual:** missing entirely; insurance amounts not commensurate with deal exposure; no additional-insured provision; no waiver of subrogation.

### 2.4 Audit and Inspection Rights †

**Standard:** buyer's right to audit supplier's facilities for quality and compliance, with reasonable notice; right to inspect supplier's records relevant to deal performance; pricing-related audit rights (especially in cost-plus or index-based pricing); industry-specific audit rights (PPAP audits for automotive; quality audits for medical device).

**Unusual:** no buyer audit rights; audit rights so narrow they don't cover the relevant operations; supplier's audit rights of buyer (occasionally appropriate but flag).

### 2.5 Recall Obligations

**Standard:** mutual cooperation in recall; allocation of recall costs based on responsibility (defect-caused recall = supplier; buyer-design-caused recall = buyer; complicated by combined causes); coordination with regulatory authorities.

**Unusual:** missing entirely in industries with recall risk (food, pharma, medical, automotive); buyer bears all recall costs regardless of cause; supplier liability for recall capped or excluded from cap.

### 2.6 Packaging, Labeling, and Marking

**Standard:** specifications referenced; country-of-origin marking per applicable law; labeling per regulatory requirements (FDA, FCC, etc.); special packaging requirements (anti-static, hazmat, etc.).

**Unusual:** vague packaging requirements; no labeling specifications; missing required regulatory marking provisions.

### 2.7 Set-Off Rights

**Standard:** buyer's right to set off undisputed amounts owed by supplier against amounts owed to supplier (often present, sometimes negotiated); supplier's similar rights are less common.

**Unusual:** broad set-off rights for disputed amounts (favors party with right; flag for other side); no set-off rights at all (typical for supplier; missing for buyer).

### 2.8 Assignment

**Standard:** mutual restriction with consent; carve-outs for change of control, M&A, internal reorganization. Either party retains right to assign to successor.

**Unusual:** unilateral right by one party; broad consent rights blocking legitimate M&A; assignment to direct competitor.

### 2.9 Governing Law and Venue

**Standard:** specified state's law and forum. UCC Article 2 applies in US sales of goods regardless of state; choice of state affects UCC interpretation, statute of limitations under §2-725 (4 years default; can be reduced to 1 year by agreement; cannot be extended), and warranty disclaimers under §2-316.

**Unusual:** no governing law specified; non-UCC jurisdiction in cross-border deal (CISG may apply unless excluded); foreign jurisdiction for US-only deal.

### 2.10 Dispute Resolution

**Standard:** specifies how disputes are resolved — court litigation, arbitration (AAA Commercial Rules common for purchase MSAs), or tiered (negotiation → mediation → arbitration).

**Unusual:** mass-arbitration prohibitions; mandatory pre-suit mediation that delays equitable relief; arbitration with class waiver in jurisdictions where consumer-protection rules invalidate.

## Tier 3 — Reviewed in detail in `comprehensive` only

Standard drafting cleanliness items: notice mechanics, integration / entire-agreement, amendment requirements, severability, waiver, counterparts, electronic signatures, definitions completeness, headings, order of precedence among MSA / PO / Quality Agreement / Specifications.

**Critical Tier 3 issue: order of precedence.** When the deal involves multiple documents (MSA, POs, Quality Agreement, Specifications, Drawings, Industry Standards), the order of precedence among these documents must be specified. If not specified, conflicts default to typical interpretive principles (specific overrides general; later overrides earlier) which may not match the parties' intent. Flag missing order-of-precedence as material.

## Tier 4 — Industry-specific provisions

Apply only when `industry_context` indicates the relevant industry overlay.

### 4.1 Automotive (PPAP, traceability, sub-tier flow-downs)

- Production Part Approval Process (PPAP) requirements per AIAG standards.
- Traceability requirements (lot, serial, date code).
- Sub-tier flow-downs (supplier must impose buyer's terms on its own suppliers).
- IATF 16949 quality system reference.
- Tooling lifecycle management.
- End-of-life parts obligations (15+ years common in automotive).

### 4.2 Medical Device (QSR, ISO 13485, FDA)

- ISO 13485 quality system requirements.
- FDA Quality System Regulation (21 CFR 820) compliance.
- Design history file obligations for design components.
- Adverse-event reporting cooperation.
- Recall coordination and regulatory cooperation.
- Sterility and biocompatibility requirements (if applicable).
- UDI (Unique Device Identification) marking.

### 4.3 Aerospace / Defense (ITAR, AS9100, AS9102)

- ITAR (International Traffic in Arms Regulations) compliance for defense articles.
- EAR (Export Administration Regulations) compliance.
- AS9100 quality system requirements.
- AS9102 first-article inspection requirements.
- Counterfeit parts prevention (DFARS).
- Cybersecurity requirements (DFARS 252.204-7012, NIST 800-171, CMMC).
- Country-of-origin tracking and reporting.

### 4.4 Food / Pharmaceutical Ingredients (FDA, FSMA, GMP)

- FDA Food Safety Modernization Act (FSMA) compliance.
- Good Manufacturing Practice (GMP) requirements.
- Traceability per FDA Final Rule 21 CFR 1.1330 (food) or 21 CFR Parts 210/211 (drugs).
- Allergen control programs.
- Country-of-origin and supply chain transparency.
- Adulteration warranties.

### 4.5 General regulatory / cross-industry

These apply across many industries:

- **REACH (EU chemicals regulation)** — declarations and substance-of-very-high-concern reporting.
- **RoHS (Restriction of Hazardous Substances)** — declarations and compliance certifications.
- **Conflict Minerals (Dodd-Frank §1502)** — sourcing reporting for tin, tantalum, tungsten, gold.
- **Prop 65 (California)** — warning labels for listed substances.
- **FCPA / UK Bribery Act** — anti-corruption representations and audit rights.
- **Modern Slavery / Forced Labor disclosures** — UK Modern Slavery Act, California Transparency in Supply Chains Act, US Uyghur Forced Labor Prevention Act.
- **Cybersecurity warranties** — for components with embedded software or connectivity.

## Severity calibration notes

Industry-specific overlays in Tier 4 typically add 1-3 material findings if the MSA does not adequately address the industry's requirements. A general-commercial MSA used in a regulated-industry context will surface significantly more issues than the same MSA used for general commodity supply.

Single-source critical-supply context elevates Tier 1.8 (term/termination) and Tier 1.9 (supply continuity) findings — issues that would be material in a multi-supplier context become critical in single-source critical supply.

Capital-equipment context elevates Tier 1.4 (warranties) and Tier 1.5 (warranty remedies) — capital equipment buyers depend on long warranty periods and effective remedies because the equipment is integrated into operations and replacement is operationally and financially significant.
