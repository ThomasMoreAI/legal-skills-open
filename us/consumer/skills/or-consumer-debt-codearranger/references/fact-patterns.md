# Fact-Pattern Triage — Oregon Consumer-Debt Defense

Five common Oregon debt-defense fact patterns with the
defenses, counterclaims, and discovery approach for each.

> **NOT LEGAL ADVICE.** Real cases combine elements of
> multiple patterns. This triage is a starting point.

## Pattern 1: Debt-buyer suit on an unfamiliar account

**Facts**: Defendant receives summons and complaint. The
plaintiff (e.g., LVNV Funding, Velocity Investments, Cavalry
SPV) alleges defendant owes a charged-off credit-card account
originally with Bank of America. Defendant doesn't recognize
the account number or amount.

**Defenses**:
- ORCP 21 A(8): failure to state ultimate facts — the
  complaint lacks specifics about the chain of title
- Statute of limitations (ORS 12.080 — 6 years on open
  account)
- Lack of standing — Plaintiff cannot prove chain of title
- ORS 697.105: Plaintiff (if a debt buyer) may not be
  registered with DCBS

**Counterclaims**:
- FDCPA § 1692e/f/g (assuming Plaintiff is a "debt collector")
- Oregon UTPA (ORS 646.605) — broader; covers any "person"
- ORS 697.085 (if unregistered)

**Discovery focus**:
- Chain-of-title documents (RFPs 1–7)
- DCBS registration status
- Original cardholder agreement
- Monthly statements
- Validation notice records

**Likely outcome**: With good discovery, defendant typically
forces dismissal or favorable settlement. Plaintiff's
inability to produce authenticable chain-of-title is fatal in
most cases.

## Pattern 2: Original creditor collection on a known account

**Facts**: Defendant is sued by Bank of America (or other
original creditor) directly on a credit card defendant
recognizes. Defendant either acknowledges the underlying debt
but disputes amount, or denies certain charges as
unauthorized.

**Defenses**:
- Account stated — defendant timely objected
- Statute of frauds (ORS 41.580) — written-agreement claims
  must be in writing
- Identity theft / unauthorized use
- Statute of limitations
- Failure of consideration
- Comparative fault (if applicable)

**Counterclaims**:
- Oregon UTPA (ORS 646.605) — false / unfair conduct in
  collection
- Defamation (if false statements to credit bureaus)
- FCRA (15 USC § 1681s-2) — willful or negligent furnishing
  of inaccurate credit information
- ORS 697 does NOT apply (original creditor exempt)
- FDCPA does NOT apply (original creditor not a "debt
  collector")

**Discovery focus**:
- Account history (all transactions)
- Authorization for disputed charges
- Communications between defendant and creditor's collection
  department
- Defendant's prior disputes (account stated)

**Likely outcome**: Fact-intensive. Defendant often pursues
account-stated, identity-theft, or unauthorized-use defenses.
Result varies with documentation.

## Pattern 3: Time-barred debt (zombie debt) revival

**Facts**: Plaintiff sues on a debt that is past Oregon's
6-year SOL (ORS 12.080). Plaintiff alleges a recent partial
payment or written acknowledgment restarted the SOL.

**Defenses**:
- Statute of limitations (the strong, often dispositive
  defense)
- Under ORS 12.230, **payment alone does not revive** the
  SOL — only a **written promise to pay** can revive
- Even if a written promise existed, it must be unequivocal

**Counterclaims**:
- FDCPA § 1692e(2), e(5), f(1) — collecting on time-barred
  debt; threatening prohibited action
- Reg F § 1006.26(b) — time-barred debt collection without
  disclosure
- Oregon UTPA (ORS 646.605) — false representation of legal
  status

**Discovery focus**:
- Plaintiff's account history showing dates
- All communications with defendant since charge-off
- Any alleged "written promise to pay" — specifically the
  document plaintiff relies on for revival

**Likely outcome**: SOL defense is dispositive if defendant
can show the SOL ran. Counterclaims are strong if plaintiff
filed suit knowing the SOL had run.

## Pattern 4: Default judgment entered improperly

**Facts**: Defendant did not respond to the original
complaint (often because they did not receive it — defective
service, or the summons went to a wrong address). Default
judgment is entered. Defendant learns of the judgment when
garnishment begins.

**Approach**:

### Step 1: Motion to vacate (ORCP 71)

See `or-post-judgment/references/motion-to-vacate.md`. Show:
- Ground (typically ORCP 71 B(1) excusable neglect or
  B(4) void for defective service)
- Diligence (when learned; when filing)
- Meritorious defense (attach proposed answer)
- Lack of prejudice

### Step 2: Stay or exemption during pendency

Garnishment continues during the vacate motion. File a
Challenge to Writ of Garnishment under ORS 18.700+ to
claim exemptions; also a Motion to Stay Execution.

### Step 3: If vacated, go to Pattern 1 or 2

Once the judgment is vacated, the case is back at the
pleading stage. File the proposed answer with counterclaims.

**Likely outcome**: ORCP 71 motion success depends on facts
of service. Defective-service grounds (B(4) void) are
strong; "I didn't see the summons" (B(1) excusable neglect)
requires good facts.

## Pattern 5: Unregistered collection agency

**Facts**: Plaintiff is a collection agency (or debt buyer
treated as one) that has not registered with the Oregon
Department of Consumer and Business Services under ORS
697.015.

**Defenses**:
- ORS 697.105: lack of capacity to sue — unregistered
  collection agency cannot maintain an action
- Move to dismiss under ORCP 21 A(1) (no jurisdiction) or
  A(8) (failure to state)

**Counterclaims**:
- ORS 697.085 — private right of action for unregistered
  collection
- Oregon UTPA (ORS 646.605) — unregistered collection is
  unfair conduct
- FDCPA § 1692e(5) — threatening to sue is unlawful when
  the threatener lacks standing to sue

**Discovery focus**:
- Plaintiff's registration status (DCBS database lookup —
  screenshot for the record)
- Plaintiff's bond
- Any history of registration violations

**Likely outcome**: Strong defense. Plaintiff cannot easily
cure unregistered status during litigation. Some plaintiffs
may attempt mid-suit registration, but the lack of
registration at filing is fatal under ORS 697.105.

## Triage decision tree

```
Did defendant recognize the account?
├── No → Pattern 1 (Debt-buyer)
│         Discovery: chain of title; OEC 803(6) foundation
│         Counterclaims: FDCPA + UTPA + ORS 697
│
└── Yes → Plaintiff is who?
          ├── Original creditor → Pattern 2 (Original creditor)
          │   Defenses: account stated; identity theft; SOL
          │   Counterclaims: UTPA; FCRA; defamation
          │
          └── Debt buyer / collection agency → Pattern 1
              modified — defendant recognizes the underlying
              account but disputes the assignment

Is the debt past SOL (ORS 12.080 6 years)?
├── Yes → Pattern 3 (Time-barred)
│         SOL defense + FDCPA / UTPA / Reg F counterclaims
│
└── No → Continue with pattern above

Has default been entered?
├── Yes → Pattern 4 (Default vacation)
│         ORCP 71 motion + stay/exemptions
│
└── No → Continue with pattern above

Is the plaintiff DCBS-registered?
├── No (or expired) → Pattern 5 (Unregistered)
│   Motion to dismiss under ORS 697.105
│   ORS 697.085 counterclaim
│
└── Yes → Continue with pattern above
```

## Combinations are the norm

Most cases combine elements. For example:

- Debt buyer suing on time-barred debt → Pattern 1 + Pattern 3
- Unregistered debt buyer suing on time-barred debt → 1 + 3 + 5
- Default already entered on a debt-buyer suit → 1 + 4

When in doubt, work through each pattern. The defenses and
counterclaims overlap, but the discovery focus and the
strongest argument vary.

## Strategic priorities

1. **Statute of limitations** — if available, this is usually
   dispositive
2. **Lack of capacity (ORS 697.105)** — if available, this is
   usually dispositive
3. **Chain of title** — strong but requires discovery to
   develop
4. **OEC 803(6) foundation** — strong but requires
   evidentiary hearing
5. **Counterclaims (FDCPA / UTPA / ORS 697)** — for
   leverage and recovery
6. **Default vacation** — necessary first step if default
   exists

The order of operations: (1) defenses first to dispose of the
case; (2) counterclaims for leverage and recovery; (3) chain-
of-title discovery to undermine plaintiff's case on the
merits.

## Cross-references

- `or-consumer-debt` SKILL — main bundle
- `references/utpa.md` — UTPA detail
- `references/fdcpa.md` — FDCPA detail
- `references/ors-697.md` — ORS 697 detail
- `references/chain-of-title.md` — chain-of-title doctrine
- `references/or-statutes-of-limitations.md` — SOL detail
- `references/examples/` — sample filings
- `or-post-judgment/references/motion-to-vacate.md` —
  ORCP 71 motion
