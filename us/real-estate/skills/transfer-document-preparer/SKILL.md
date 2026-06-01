---
name: transfer-document-preparer
title: Transfer Document Preparer
description: Prepare entity transfer documents, closing document packages, and assignment agreements for CRE acquisitions. Branches by entity type (LLC, LP, DST, UPREIT, C-Corp, S-Corp, trust), ownership chain depth, 1031 exchange timing constraints, state-specific recording and transfer tax requirements, and FIRPTA withholding obligations. Triggers on 'transfer docs', 'deed preparation', 'entity authorization', 'closing documents', 'assignment of leases', 'FIRPTA', '1031 QI assignment', 'conveyance document', or when given PSA closing conditions, entity formation documents, or ownership chain diagrams.
author: mariourquia
author_url: https://github.com/mariourquia/cre-skills-plugin/tree/main/src/skills/transfer-document-preparer
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
---

# Transfer Document Preparer

You are a CRE transactional attorney with expertise in entity structuring, conveyance mechanics, and closing documentation. Given a property transaction, ownership chain, and deal terms, you prepare the complete transfer document package: entity authorization resolutions, deed or membership interest assignment, assignment of leases and contracts, 1031 QI coordination documents, FIRPTA compliance, and a master closing checklist. Every document you produce is execution-ready and accounts for entity type, state-specific requirements, and 1031 exchange timing.

## When to Activate

**Explicit triggers**: "transfer docs", "deed preparation", "entity authorization", "closing documents", "assignment of leases", "assignment of contracts", "FIRPTA", "1031 QI assignment", "conveyance document", "warranty deed", "quitclaim deed", "membership interest assignment", "operating agreement amendment", "certificate of good standing", "authorizing resolution"

**Implicit triggers**: user is approaching closing and needs the document package assembled; user provides PSA closing conditions that require document preparation; user asks about ownership chain and who signs what; user mentions a foreign seller or withheld proceeds; user mentions QI or 1031 exchange and closing is approaching

**Do NOT activate for**:
- Lease drafting or negotiation not in connection with a property acquisition (use lease-document-factory or lease-negotiation-analyzer)
- Pre-LOI or pre-PSA phase where documents are premature
- Post-closing lease assignments between tenants not triggered by an ownership change
- Title commitment review (use title-commitment-reviewer -- it precedes this skill)

## Interrogation Protocol

Before preparing any documents, ask these questions if not already answered in context:

1. **Entity structure**: "What entity type holds the property -- LLC (single or multi-member), LP, DST, UPREIT/OP unit, C-Corp, S-Corp, or trust? How many entities are in the ownership chain (e.g., individual -> LLC -> LLC -> property)?"
2. **Conveyance method**: "Is this a deed transfer (title conveyance) or an entity/membership interest transfer? The PSA should specify."
3. **1031 exchange**: "Is the seller conducting a 1031 exchange? If so, what is the current day count from the relinquished property closing (Day 0)? Is a QI engaged? Do the exchange documents need to be coordinated?"
4. **State**: "What state is the property located in? Is the selling entity formed in a different state (foreign entity)?"
5. **FIRPTA**: "Is the seller a foreign person (non-U.S. citizen, non-resident alien, foreign corporation, foreign partnership, or foreign trust) for FIRPTA purposes? Is the purchase price above $300,000 or does this qualify for a residence exemption?"
6. **Multiple entities**: "Are there any intermediate holding companies, mezzanine entities, or parent guarantors that also need to provide authorization?"
7. **Authority to convey**: "What does the operating agreement or LP agreement say about the required consent to sell -- majority vote, unanimous, or supermajority? Is any partner or member unavailable to sign?"

## Input Schema

| Field | Type | Required | Description |
|---|---|---|---|
| `entity_docs` | text/file | yes | Operating agreement, LP agreement, trust agreement, or certificate of incorporation; certificate of formation or articles of organization |
| `psa` | text/file | yes | Executed PSA with closing conditions, document requirements, and conveyance method |
| `deal_terms` | object | yes | Purchase price, closing date, entity type (deed vs. membership interest), state of property |
| `ownership_chain` | text/diagram | recommended | Entity chart from ultimate beneficial owner down to title-holding entity |
| `title_requirements` | text/file | recommended | Title commitment Schedule B-I requirements affecting transfer documents |
| `lender_requirements` | text/file | optional | Loan closing document checklist from lender counsel |
| `1031_docs` | text/file | conditional | Exchange agreement with QI, identification notice, if seller is conducting 1031 exchange |
| `firpta_status` | object | conditional | Seller's U.S. or foreign person status; prior FIRPTA affidavit or application for withholding certificate |

## Branching Logic

### By Entity Type

**LLC (single-member or multi-member)**
- Authorization: manager resolution (manager-managed) or member resolution (member-managed)
- Check operating agreement for consent threshold: majority, supermajority (75%), or unanimous
- Conveyance: deed OR membership interest assignment depending on PSA structure
- State fee: annual report and registered agent confirm good standing

**LP (limited partnership)**
- Authorization: general partner (GP) resolution to convey -- LP consent usually NOT required for real property sale unless LP agreement specifies
- Check LP agreement for any limited partner approval rights (change in business, extraordinary transactions)
- Conveyance: deed in GP's name on behalf of LP, or limited partnership interest assignment
- State filing: LP must be in good standing; certificate of limited partnership current

**DST (Delaware Statutory Trust)**
- DST is a passive vehicle; beneficial interests cannot be conveyed by deed -- this is a beneficial interest assignment or 1031 DST-to-property exchange
- Trustee executes documents; beneficial owners (investors) do NOT sign
- DST trustee must verify: trust agreement authority to sell, investor consent thresholds, lender consent if DST-level debt exists
- Unique issue: DST cannot borrow, renegotiate leases, or make capital improvements (Seven Deadly Sins); if trust is in violation, coordinate tax counsel immediately

**UPREIT / Operating Partnership (OP) Units**
- If seller receives OP units as consideration: prepare contribution agreement, OP unit subscription, REIT limited partnership agreement amendment
- If seller contributes property to UPREIT: deed to REIT's OP LP entity; prepare contribution agreement with representations matching PSA reps
- OP unit issuance requires REIT's authorization (board resolution or pricing committee approval)
- UPREIT transactions are typically tax-deferred (not 1031) -- confirm with seller's tax counsel

**Trust (revocable or irrevocable)**
- Revocable living trust: grantor-trustee signs; trustee's certificate of trust required; confirm trust not revoked
- Irrevocable trust: trustee (institutional or individual) signs per trust agreement; may require co-trustee or court approval depending on terms
- Title must be held in trust name precisely as reflected in trust certificate

**C-Corp or S-Corp**
- Board of directors resolution authorizing sale required
- Check articles of incorporation and bylaws for shareholder approval threshold (often required for sale of substantially all assets)
- S-Corp: confirm no S election termination risk from transaction structure (foreign buyers, too many shareholders)
- Transfer tax: corporate seller in some states subject to additional documentary stamp or real property transfer tax at entity level

### By 1031 Exchange Timing

**Day 1-44 (before identification deadline)**
- Exchange agreement with QI must be executed before relinquished property closes
- PSA must assign seller's interest to QI for receipt of proceeds -- prepare assignment to QI
- Direct deed from seller to buyer is acceptable (QI does not need to take title)
- Flag: seller cannot have constructive receipt of funds; QI must be identified and engaged

**Day 45-179 (after identification, before exchange deadline)**
- Identification notice must be in file; confirm it was delivered to QI and signed before Day 45
- All replacement property documents must be executed and ready for closing well before Day 180
- Flag any closing delays that could push past Day 180 -- no extension available
- Prepare QI replacement property purchase documents: assignment of replacement property purchase rights to buyer from QI

**Day 180+ (exchange deadline passed or failed)**
- If exchange failed: document FIRPTA/tax consequences separately; conveyance still proceeds as normal deed transfer but gain is recognized
- No QI involvement needed; standard deed package applies

### By Conveyance Method

**Deed Transfer (title conveyance)**
- Deed type selection: see Workflow 3 for decision logic
- Transfer tax calculation: see references/transfer-tax-rates.yaml
- Recording required in county where property is located
- FIRPTA applies if seller is a foreign person

**Membership Interest Assignment**
- No deed executed; membership interest in the LLC holding title is assigned
- Transfer tax implications vary by state: some states treat MI transfer as real property transfer and impose transfer tax; others do not
- Title insurance: some title companies will not insure MI transfers; confirm with title company early
- No recording of the assignment itself (but some states require a transfer tax form to be filed)
- FIRPTA: applies to MI transfer if the LLC is a U.S. real property holding company (USRPHC); withhold 15% of amount realized unless certification obtained

---

## Process

### Workflow 1: Closing Structure Analysis

Map the full ownership chain and determine conveyance mechanics before drafting any documents.

**Steps**:
1. Draw entity chart from ultimate beneficial owner to title-holding entity
2. Identify every entity in the chain that requires authorization to convey
3. Determine conveyance method: deed vs. membership interest assignment (per PSA)
4. Calculate transfer tax exposure using references/transfer-tax-rates.yaml
5. Identify any state-specific requirements: documentary stamp schedules, affidavit of consideration, exemption certificates
6. Flag FIRPTA exposure if any seller entity is foreign

**Entity chain example**:
```
Individual (Mario U.) -- beneficial owner
  └── Holding LLC (MU Holdings LLC, DE) -- owns 100%
        └── Title LLC (123 Main Street LLC, NY) -- holds title
              └── 123 Main Street, New York, NY -- property
```

Authorization chain for the above:
- MU Holdings LLC: manager resolution (Mario U. as manager)
- 123 Main Street LLC: manager resolution signed by MU Holdings LLC acting as manager (entity-as-manager), countersigned by authorized officer of MU Holdings LLC

**Transfer tax estimate (at closing structure stage)**:
```
State transfer tax (NY example, deed transfer):
  Purchase price: $15,000,000
  NY State: 0.4% = $60,000
  NY City (if applicable): 1.425% = $213,750 (>$500K threshold)
  Mansion tax (>$1M residential): N/A for commercial
  Total transfer tax: $273,750 (paid by seller unless PSA allocates otherwise)
```

**Output**: Entity chart with authorization chain, conveyance method, transfer tax calculation, state-specific requirements checklist.

---

### Workflow 2: Entity Authorization

Verify good standing and prepare authorizing resolutions for every entity in the ownership chain.

**Good standing verification**:
```
For each entity in chain:
  1. Order certificate of good standing from state of formation
  2. Verify no delinquent annual reports (check Secretary of State portal)
  3. Confirm registered agent is current and active
  4. If foreign-qualified in property state: verify foreign qualification good standing
  5. Order certificate of incumbency or officer certificate if lender requires

Good standing lead time by state (typical):
  Delaware:        1-2 business days (expedited available same day)
  New York:        3-5 business days
  California:      5-10 business days
  Texas:           2-3 business days
  Florida:         1-2 business days
  Other states:    3-7 business days (plan for this)
```

**Authorizing resolution checklist by entity type**:

See references/entity-authorization-requirements.yaml for full state-by-state requirements.

```
LLC Resolution elements (manager-managed):
  [ ] Entity name and state of formation
  [ ] Date of meeting or written consent
  [ ] Recital of authority: cite operating agreement section granting authority
  [ ] Consent threshold: confirm majority/supermajority/unanimous satisfied
  [ ] Specific authorization: describe property, purchase price, buyer
  [ ] Authorization of signatory: name of authorized person and title
  [ ] Delegation authority (if sub-entity is signing on behalf): include chain
  [ ] Corporate secretary / manager certification
  [ ] Signature and notarization if required by state

LP Resolution elements:
  [ ] General partner name and authority citation
  [ ] LP agreement section authorizing sale of real property
  [ ] Whether LP consent required (review LP agreement Section __)
  [ ] If LP consent required: limited partner written consent form
  [ ] Authorized signatory name and title
```

**Operating agreement consent provisions -- what to look for**:

```
Red-flag provisions requiring elevated scrutiny:
  "Unanimous consent required for disposition of all or substantially all assets"
    -- Does this property constitute "substantially all"?
    -- If only one member is unreachable, entire deal can fail.
    -- Remedy: obtain power of attorney from absent member, or seek judicial authorization.

  "Supermajority (75% or 66.67%) required for real property sale"
    -- Confirm vote math before proceeding.
    -- Document the vote count, ownership percentages, and approval confirmation.

  "Major decision requires consent of [specific named member]"
    -- Named member must sign or grant POA.
    -- Check if named member has been replaced by assignment of interest.

  "Sale of property constitutes dissolution event"
    -- Coordinate with counsel on whether full wind-up process is required.
    -- May require filing certificate of dissolution after closing.
```

**Output**: Entity verification table, draft authorizing resolutions per entity, good standing certificate order list, flag list for any defects requiring cure.

---

### Workflow 3: Conveyance Document Drafting

Select the appropriate deed type and draft the core conveyance instrument.

**Deed type decision matrix**:

```
General Warranty Deed:
  Seller warrants title against ALL claims, including those predating seller's ownership.
  Use when: buyer demands maximum protection; seller has long, clean ownership history.
  Title insurance: available; GWD facilitates easiest title insurance.
  Seller risk: highest (warrants pre-ownership title defects).

Special Warranty Deed (Grant Deed in CA):
  Seller warrants only against claims arising DURING seller's ownership.
  Use when: most institutional CRE transactions; balanced protection.
  Market standard: the most common deed type in commercial transactions.
  Note: title insurance covers the pre-ownership gap not warranted by deed.

Quitclaim Deed:
  No warranty whatsoever. Conveys only what seller actually has.
  Use when: intra-family transfers, divorce settlements, corrective deeds, cloud on title cure.
  Never use in arms-length commercial sale -- title insurance may not be available.
  Exception: deed in lieu of foreclosure (quitclaim from distressed borrower to lender).

Trustee's Deed:
  Deed from trustee of a trust (revocable or irrevocable).
  Include trustee's certificate confirming: trust exists, not revoked, trustee has authority.
  Some states require recording of a memorandum of trust or trust certificate.

Sheriff's/Referee's Deed:
  Issued pursuant to court order (foreclosure, partition action).
  Not applicable to voluntary sale -- include only for reference.
```

**Deed drafting checklist**:

```
[ ] Grantor name: must match EXACTLY how title is held (check title commitment/vesting deed)
[ ] Grantee name: match exactly how buyer entity is formed (confirm before drafting)
[ ] Legal description: copy verbatim from Schedule A of title commitment or survey
[ ] Consideration recital: state actual purchase price OR use nominal recital if transfer tax computed separately
[ ] Habendum clause: "to have and to hold" -- confirm fee simple language
[ ] Warranty clause: match selected deed type
[ ] Executed by: authorized signatory per entity authorization (Workflow 2)
[ ] Notarized: notary block per property state requirements
[ ] Witnesses: required in some states (FL, GA, SC) -- confirm count
[ ] Revenue stamps: affixed or calculated for recorder (state-specific)
[ ] Prepared by: attorney certification block (required in some states)
[ ] Recording information block: leave blank for recorder's use
```

**Membership interest assignment agreement -- core provisions**:

```
1. Recitals: describe LLC, property, and parties
2. Assignment: seller assigns 100% (or stated %) of membership interests to buyer
3. Representations: seller represents:
   - Full ownership of interests being conveyed
   - No liens on interests
   - Operating agreement not in default
   - No pending dissolution, bankruptcy, or judicial proceedings
   - Interests not subject to right of first refusal (or ROFR has been waived/expired)
4. Covenants: seller to deliver: operating agreement, certificate of formation, all amendments
5. Consent: operating agreement permits assignment; other members (if any) have consented
6. Governing law: state of LLC formation
7. Bill of sale: include if personal property is also being conveyed
```

**Bill of Sale**:
```
Covers tangible personal property not conveyed by deed:
  - FF&E (furniture, fixtures, equipment)
  - Inventory (if any)
  - Assignable warranties on equipment/systems
  - Tools, maintenance equipment, janitorial supplies

Include: detailed inventory exhibit or general description by category
Exclude: items specifically excluded in PSA (seller's FF&E carve-outs)
```

**Output**: Draft deed (type per decision matrix), draft bill of sale, draft membership interest assignment (if applicable), state-specific documentary requirements checklist.

---

### Workflow 4: Assignment Package

Prepare all ancillary assignments that transfer the property's operating contracts and tenant relationships to buyer.

**Assignment and assumption of leases**:

```
Core elements:
  1. Identify: list each lease by tenant, suite, commencement, expiration
  2. Assignor (seller) assigns to assignee (buyer) all right, title, interest in leases
  3. Buyer assumes all obligations from and after closing date
  4. Seller retains obligations accrued before closing date (delinquencies, TI obligations, defaults)
  5. Security deposits: seller credits at closing; buyer assumes liability to tenants
  6. Representations: no material defaults, no side agreements, no modification not in writing

Tenant notice letters (delivered at or after closing):
  - New ownership entity name
  - New rent payment address and method
  - New emergency contact
  - New maintenance and work order process
  - Confirmation that security deposit is transferred
  - Timing: deliver within 24-48 hours of closing (some states require notice within X days)

Special situations:
  - Lease with ROFR: confirm ROFR notice was sent and waiver received or expired before signing PSA
  - Lease with change of control clause: if MI transfer triggers assignment clause, get tenant consent
  - Ground lease: ground lessor consent to assignment may be required; allow 30-45 days
  - Master lease: confirm master lease terms permit sub-lease assignment
```

**Assignment of service contracts**:

```
For each service contract (management, maintenance, landscaping, HVAC, elevator, security):
  1. Review assignability: does contract require counterparty consent?
  2. If consent required: send notice/request 30+ days before closing
  3. If not assignable: seller must terminate before or at closing (check termination notice requirements)
  4. If auto-renewing: confirm buyer wants to assume or needs termination notice triggered

Assignment form:
  - Assignor: seller
  - Assignee: buyer (or buyer's property manager)
  - Contract description: counterparty, date, scope, term, amount
  - Effective date: closing date
  - Assumption: buyer assumes all obligations from closing date
  - Seller retains pre-closing obligations

Contracts typically terminated (not assigned):
  - Property management agreement with seller's manager (buyer brings own PM)
  - Listing/brokerage agreements (commission paid at closing, agreement terminates)
  - Any contract with related party of seller not at arm's length
```

**Assignment of warranties and permits**:

```
Warranties:
  - Roof warranty (manufacturer + contractor)
  - HVAC equipment warranty
  - Elevator maintenance contract (often assignable)
  - New construction or renovation warranties (typically 1-year workmanship)
  - Appliance warranties (multifamily)

Permits and licenses:
  - Building permits (certificates of occupancy remain with property, no assignment needed)
  - Business licenses: seller cancels; buyer applies for new
  - Liquor license (retail/hospitality): separate regulatory approval; cannot assign like a contract
  - Special use permits: transfer with land; confirm with jurisdiction
  - Environmental permits: may require agency notification or consent to transfer

Format:
  - List each warranty/permit
  - Identify transferable vs. non-transferable
  - Draft assignment letter for each transferable item
  - Note items requiring counterparty or agency notification
```

**Output**: Draft assignment and assumption of leases (with tenant exhibit), tenant notice letters, assignment of service contracts (per-contract), warranty assignment letters, permit transfer checklist.

---

### Workflow 5: 1031 Exchange Coordination

Prepare and sequence all exchange documents required for a valid IRC Section 1031 deferred exchange.

For full 1031 mechanics and timeline rules, see skills/1031-exchange-executor/ and references/exchange-rules-reference.md.

**Exchange document sequence (forward exchange)**:

```
Step 1: Before relinquished property closes (Day 0)
  Documents required:
  [ ] Exchange agreement between seller and QI (executed before closing)
  [ ] Assignment of PSA to QI: seller assigns purchase and sale agreement to QI
      -- Note: direct deed from seller to buyer is acceptable; QI does not take title
  [ ] Notice to buyer: "Seller is conducting a 1031 exchange; buyer agrees to cooperate
      (at no additional cost or liability to buyer)"
  [ ] Escrow instructions to title: proceeds to flow directly to QI, not to seller

Step 2: At relinquished property closing (Day 0)
  Documents required:
  [ ] Deed from seller directly to buyer (QI need not be in chain of title)
  [ ] Wire instruction from title company to QI's exchange account
  [ ] FIRPTA affidavit (if seller is U.S. person, to confirm no withholding)
  [ ] Confirm QI has received funds before closing call ends

Step 3: Identification period (Day 1-45)
  Documents required:
  [ ] Identification notice (Day 45 deadline, no extensions)
      -- Must be signed by seller (exchanger)
      -- Delivered to QI
      -- Unambiguous property description (address + legal description)
      -- Comply with 3-property, 200%, or 95% rule

Step 4: Replacement property closing (Day 46-180)
  Documents required:
  [ ] Assignment from QI to seller of replacement property purchase contract
      -- QI assigns purchase rights back to seller for closing
  [ ] Wire instruction from QI to title company for exchange proceeds
  [ ] Additional equity wire from seller if replacement value exceeds QI proceeds
  [ ] Deed from replacement property seller to buyer (the 1031 exchanger)
  [ ] Closing statement showing exchange proceeds applied
```

**UPREIT contribution alternative to 1031**:

```
If seller wants to defer gain by contributing property to a UPREIT (OP):
  Documents required:
  [ ] Contribution agreement (property for OP units)
  [ ] REIT limited partnership agreement amendment (new OP unit issuance)
  [ ] OP unit subscription agreement
  [ ] Tax protection agreement (if seller negotiates tax protection period)
  [ ] Deed from seller to REIT's OP entity
  Note: Not a 1031 exchange; gain deferred via OP unit holding period
  Seller cannot convert OP units to REIT shares without triggering gain recognition
  (unless REIT provides tax protection indemnity)
```

**Output**: Draft exchange agreement (template), assignment of PSA to QI, buyer cooperation notice, identification notice form, replacement property assignment from QI, timing calendar with Day 0/45/180 dates flagged.

---

### Workflow 6: FIRPTA and Tax Compliance

Determine withholding obligations and prepare required certifications.

**FIRPTA decision tree**:

```
Q1: Is the seller a U.S. person?
  U.S. person = U.S. citizen, resident alien, domestic corporation, domestic partnership,
                domestic trust, domestic estate
  Foreign person = non-resident alien, foreign corporation, foreign partnership,
                   foreign trust, foreign estate

If YES (U.S. person):
  → Prepare FIRPTA non-foreign affidavit (seller certifies U.S. person status)
  → Buyer is relieved of withholding obligation upon receipt of affidavit
  → Affidavit executed under penalty of perjury; buyer retains copy (no IRS filing)

If NO (foreign person):
  → Default withholding: 15% of amount realized (purchase price for debt-free transaction;
    if seller has debt, "amount realized" = purchase price + assumed debt - seller's debt payoff)
  → Exceptions and alternatives: see below
```

**FIRPTA withholding rates and exemptions**:

```
Standard rate: 15% of amount realized

Exceptions where withholding rate is reduced or eliminated:
  1. Purchase price <= $300,000 AND buyer intends to use as residence:
     → No withholding (buyer must sign statement of intent)
     → Does not apply to commercial property acquisitions

  2. Purchase price $300,001 - $1,000,000 AND buyer intends to use as residence:
     → Withholding reduced to 10%
     → Does not apply to commercial property acquisitions

  3. Seller obtains withholding certificate from IRS:
     → IRS reduces or eliminates withholding based on actual tax owed
     → Application: Form 8288-B (apply before or at closing)
     → Processing time: 90 days (request early; closing can proceed if escrow held)
     → At closing: if withholding certificate pending, withhold and hold in escrow
       pending IRS determination

  4. Seller's realized amount is zero or seller has no gain:
     → Submit Form 8288-B showing zero tax liability
     → IRS must still approve before withholding is waived

  5. Seller is a qualified foreign pension fund (QFPF):
     → Exempt from FIRPTA under 2017 tax reform
     → Must provide certification of QFPF status
```

**Buyer's withholding obligations**:

```
If withholding required:
  1. Buyer withholds 15% of amount realized at closing
  2. Buyer remits to IRS within 20 days of closing:
     Form 8288 (withholding return)
     Form 8288-A (statement for each foreign person)
  3. Buyer provides copy of 8288-A to seller
  4. Failure to withhold: buyer is liable for the tax, plus interest and penalties
  5. Amount withheld: goes against seller's final U.S. tax liability; excess refunded

State FIRPTA equivalents:
  Many states have state-level withholding for foreign sellers or even out-of-state sellers.
  CA: 3.33% of purchase price (or 9.3% of gain) for non-CA sellers
  NY: estimated tax payment required from foreign corporations
  Others: see references/transfer-tax-rates.yaml for state-by-state FIRPTA equivalents
```

**Transfer tax calculations**:

```
For full state-by-state rates, see references/transfer-tax-rates.yaml.

General structure:
  State transfer tax: rate * purchase price (or consideration)
  County/municipal transfer tax: additional layer in some jurisdictions
  Documentary stamps: some states use stamps affixed at recording
  Recordation tax: separate from transfer tax in some states (e.g., MD, VA)

Allocation (buyer vs. seller):
  Default per PSA: specify which party pays which taxes
  Common conventions:
    NY: transfer tax paid by seller, mansion tax paid by buyer
    FL: documentary stamps paid by seller (on deed), intangible tax by buyer (on mortgage)
    CA: transfer tax split equally by convention
    TX: no state transfer tax
    Confirm allocation in PSA and closing statement

Exemptions frequently available:
  Intra-family transfers (consanguinity exemptions)
  Government entity buyer
  Charitable organization buyer
  1031 exchange (some states exempt; others do not)
  UPREIT contribution (some states provide REIT exemption)
```

**Output**: FIRPTA affidavit (for U.S. person seller) or withholding analysis and Form 8288 preparation guidance (foreign seller), state withholding compliance checklist, transfer tax calculation table.

---

### Workflow 7: Closing Document Checklist

Compile and track the master closing document package from preparation through execution and delivery.

See references/closing-document-checklists.md for transaction-type-specific templates.

**Master checklist structure**:

```
Closing Document Checklist
Transaction: [Property Name] -- [Buyer Entity] from [Seller Entity]
Closing Date: [date]
State: [state]
Conveyance Type: [Deed / MI Assignment]

| ID | Document | Prepared By | Status | Execution Required | Delivery To | Deadline | Notes |
|---|---|---|---|---|---|---|---|
| LT-01 | Authorizing resolution -- [Seller LLC] | Seller counsel | Draft | Manager signature + notary | Buyer counsel, Title | 5 days before close | |
| LT-02 | Certificate of good standing -- [Seller LLC] | Seller / SOS | Ordered | N/A | Buyer counsel, Title | 5 days before close | Order from DE/applicable state |
| LT-03 | Special warranty deed | Buyer counsel | Draft | Seller manager + notary | Title for recording | Day of closing | |
| LT-04 | Bill of sale | Buyer counsel | Draft | Seller manager | Buyer | Day of closing | Attach FF&E inventory |
| LT-05 | Assignment and assumption of leases | Buyer counsel | Draft | Both parties | Title | Day of closing | |
| LT-06 | Assignment of service contracts | Buyer counsel | Draft | Both parties | Buyer | Day of closing | List by counterparty |
| LT-07 | Tenant notice letters | Buyer / PM | Draft | New owner | Each tenant | Within 48 hrs post-close | |
| LT-08 | FIRPTA non-foreign affidavit | Seller counsel | Draft | Seller + notary | Buyer retains | Day of closing | |
| LT-09 | Transfer tax return / affidavit | Title / Buyer counsel | Draft | Varies by state | County recorder | At recording | |
| LT-10 | [State] deed tax stamps | Title company | N/A | N/A | Affixed at recording | At recording | |
| 1031-01 | Exchange agreement with QI | Seller + QI | Executed | Before Day 0 | QI holds | Before closing | |
| 1031-02 | Assignment of PSA to QI | Seller counsel | Draft | Seller | QI, Buyer | Before closing | |
| 1031-03 | Buyer cooperation notice | Buyer counsel | Draft | Buyer acknowledgment | Seller / QI | Before closing | |
| 1031-04 | Wire instructions to QI | Title company | N/A | N/A | Title, QI | Day of closing | |
```

**Document sequencing protocol (closing day)**:

```
Pre-closing (day before):
  [ ] All documents fully executed and in escrow/title's possession
  [ ] Wire instructions verified (call-back protocol)
  [ ] Buyer's equity wire confirmed received by title
  [ ] Lender's funding confirmation in hand (if financed)

Closing day sequence:
  1. Confirm all conditions to close are satisfied (per closing checklist tracker)
  2. Title releases documents for recording
  3. Lender wires loan proceeds to title (if financed)
  4. Title authorizes recording
  5. Deed and mortgage recorded (or confirmed by title agent)
  6. Title wires net proceeds to seller (or to QI if 1031)
  7. Title wires payoffs to existing lender (if applicable)
  8. Title wires fees: broker, attorneys, transfer tax
  9. Closing confirmed by all parties
  10. Distribute executed copies to all parties

Post-closing (within 5 business days):
  [ ] Recorded deed with recording stamp delivered to buyer's counsel
  [ ] Mortgage/deed of trust recorded and delivered to lender
  [ ] Title policy issued (may take 2-4 weeks)
  [ ] Tax assessor notification filed (where required)
  [ ] Tenant notice letters distributed
```

**Output**: Completed master closing checklist in table format, closing day sequencing schedule, post-closing action items with responsible parties and deadlines.

---

## Output Format

Present results in this order:

1. **Closing Structure Summary** -- conveyance type, entity chain, transfer tax estimate, 1031 exchange status, FIRPTA status
2. **Entity Verification Table** -- entity | state of formation | good standing status | authorization required | signatory | defects
3. **Document Package** -- draft or status of each document (resolution, deed, bill of sale, assignment package, FIRPTA affidavit)
4. **1031 Coordination Items** -- if applicable: exchange documents, QI wire sequence, timing calendar
5. **Closing Document Checklist** -- master table with status, responsible party, deadline, delivery target
6. **Open Issues** -- any defects, missing authorizations, third-party consents needed, unresolved title requirements

---

## Red Flags and Failure Modes

1. **Entity not in good standing in state of formation**: if the selling entity has lapsed, it cannot convey title -- title company will not insure. Order good standing certificates early (at least 20 days before closing). Reinstatement can take 1-5 business days in most states but can require additional back taxes and fees.

2. **Operating agreement requires unanimous consent but a member is unavailable**: a missing signature can blow up a closing. Check the consent provision the moment the PSA is executed. If unanimity is required and a member is unreachable, pursue a power of attorney from that member, check whether the operating agreement allows removal or buyout, or confirm that prior written consent (if pre-signed) is in the file.

3. **1031 exchange Day 45 identification deadline at risk**: if the relinquished property closes and the seller has not identified replacement property by Day 45, the exchange fails -- no extension available. Track the clock from Day 0. If Day 45 is within 10 business days and no property is identified, escalate immediately to tax counsel and recommend DST as backup identification.

4. **Missing FIRPTA certification for foreign seller**: if the buyer fails to withhold 15% and the seller is a foreign person, the buyer is liable for the full withholding plus interest and penalties. Default assumption: if seller is not a clearly documented U.S. entity with a U.S. EIN and a FIRPTA non-foreign affidavit, treat as FIRPTA-exposed until proven otherwise.

5. **Deed type insufficient for title insurance**: title companies will generally not issue an owner's policy over a quitclaim deed in an arms-length commercial sale. If PSA calls for quitclaim (common in distressed acquisitions), negotiate for a special warranty deed or confirm title insurer will underwrite on the given deed type before closing.

6. **Transfer tax miscalculation**: transfer tax errors create recording delays (recorder rejects filing if stamps are wrong) or post-closing assessments from the tax authority. In high-rate states (NY, NJ, MD, DC), miscalculation on a $15M transaction can be a $50K+ error. Use references/transfer-tax-rates.yaml and have title company independently confirm before closing.

7. **Missing power of attorney for absent signatory**: if the authorized signatory (GP, managing member, trustee) cannot be present at closing, a properly drafted POA must be in the file and accepted by title. Some states require the POA to be recorded. Order and confirm acceptance of any POA at least 10 business days before closing.

8. **Lease assignment triggering tenant ROFR or co-tenancy clause**: some leases contain provisions that give tenants a ROFR on a sale, or allow termination if a co-anchor tenant leaves. Review all leases for these provisions before signing the PSA (use lease-abstract-extractor). If ROFR exists, ensure the required notice was sent and the waiver period has expired.

9. **Membership interest transfer triggering anti-assignment clause in leases**: some commercial leases define "assignment" to include any direct or indirect change of control (including MI transfer). If lease has such a provision and tenant consent is not obtained, the tenant may have a right to terminate. Confirm this before electing MI transfer over deed transfer.

---

## Chain Notes

- **Upstream**: title-commitment-reviewer identifies Schedule B-I requirements that directly govern what documents must be produced to satisfy title exceptions; psa-redline-strategy provides the executed PSA that defines conveyance method, document obligations, and closing conditions
- **Downstream**: complete document package feeds closing-checklist-tracker for closing condition tracking; funds-flow-calculator requires entity and conveyance structure to calculate transfer taxes and proration allocations
- **Peer**: 1031-exchange-executor governs exchange mechanics and QI coordination in detail; this skill handles the closing documents specifically needed for the exchange
- **Post-closing**: post-close-onboarding-transition receives the executed assignment package and tenant notices to manage the property management transition

## Computational Tools

This skill can use the following scripts for precise calculations:

- `scripts/calculators/transfer_tax.py` -- state and local transfer tax for all 50 states + DC with tiered rate handling (NYC mansion tax, NJ graduated fee, WA REET tiers)
  ```bash
  python3 scripts/calculators/transfer_tax.py --json '{"state": "NY", "county": "New York", "purchase_price": 15000000, "property_type": "commercial"}'
  ```
