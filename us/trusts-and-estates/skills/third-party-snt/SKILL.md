---
name: third-party-snt
title: Third-Party Special Needs Trust
description: Drafts irrevocable third-party Special Needs Trusts funded by parents, grandparents, or other non-beneficiary parties to supplement government benefits without triggering Medicaid payback obligations. Use when drafting supplemental needs trusts, third-party SNTs, estate planning disability trusts, special needs trust agreements, or any trust intended to preserve SSI/Medicaid eligibility for a disabled beneficiary using third-party assets. Also trigger when the user asks about permissible SNT distributions, in-kind support and maintenance rules, ABLE account coordination, or remainder beneficiary planning for disability trusts.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/third-party-snt
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: trusts-and-estates
language: en
tags: [agreement, drafting, transactional]
---

# Third-Party Special Needs Trust

## Why This Skill Exists

Third-party SNTs fail for two reasons: they contain language that causes the trust corpus to be treated as an available resource for public benefits purposes, or they make distributions that constitute in-kind support and maintenance (ISM) and reduce or eliminate SSI. A trust that pays rent directly to a beneficiary's landlord without cost-benefit analysis can cost the beneficiary their entire SSI check. A trust that omits the spendthrift clause can be reached by creditors.

This skill produces a jurisdiction-aware, irrevocable third-party SNT that preserves SSI and Medicaid eligibility, uses solely supplemental distribution standards, requires no Medicaid payback at termination, and includes trustee guidance on ISM avoidance. The primary distinction from first-party/self-settled SNTs (42 U.S.C. § 1396p(d)(4)(A)) is that no payback provision is required or included — this trust holds assets that never belonged to the beneficiary. `[VERIFY state-specific treatment of third-party SNTs under applicable Medicaid manual]`

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Gather before drafting unless user says "use defaults":

1. **Grantor** — full legal name, relationship to beneficiary, state of residence
2. **Beneficiary** — full legal name, DOB, nature of disability, current benefit programs (SSI, Medicaid, SSDI), specific supplemental needs
3. **Trustee** — individual vs. corporate fiduciary, successor trustees, willingness to serve
4. **Funding plan** — immediate (asset schedule) or deferred (life insurance, retirement account beneficiary designation, pour-over from will)
5. **Remainder beneficiaries** — primary and contingent with shares/percentages
6. **Jurisdiction** — state trust execution formalities, state Medicaid manual rules for third-party SNTs
7. **ABLE account eligibility** — disability onset before age 26; if eligible, whether trustee should have authority to fund ABLE account
8. **Tax posture** — grantor vs. non-grantor trust preference; gift tax strategy (Crummey powers vs. lifetime exemption)

**If user doesn't respond**, apply and label defaults: sole and absolute discretion standard; no Crummey powers; non-grantor trust; standard spendthrift and anti-alienation; state-neutral template with `[VERIFY JURISDICTION]` flags on execution formalities.

---

## Step 1: Validate Intake and Map State Law

### Required Deliverable: State-Law Scaffold

| Topic | Required Confirmation |
|---|---|
| Trust execution formalities | Witness count, notary requirement, disqualifications `[VERIFY]` |
| Third-party SNT treatment | State Medicaid manual classification; whether trust is excluded resource `[VERIFY]` |
| Distribution standards | State law on sole/absolute discretion; enforceability of supplemental-only limitation |
| Investment authority | UPIA adoption status; prudent investor standard applicability `[VERIFY]` |
| Termination rules | State rules on trust termination, modification, and decanting |
| Tax treatment | Grantor/non-grantor implications under state income tax |

---

## Step 2: Draft the Trust Document

### Fixed Section Order

| Section | Contents |
|---|---|
| **Preamble** | Trust name, grantor, trustee, beneficiary, date, recitals of intent |
| **Art. I — Purpose & Intent** | Supplemental-only purpose; benefits preservation declaration (see template below) |
| **Art. II — Irrevocability** | Irrevocable from execution; no amendment except as permitted by law |
| **Art. III — Distribution Standards** | Sole and absolute discretion; permissible categories; prohibited distributions; ISM guidance |
| **Art. IV — Trustee Powers & Duties** | Investment, hiring advisors, tax authority, recordkeeping, ABLE account funding authority |
| **Art. V — Trustee Compensation & Succession** | Fee schedule or reasonable compensation; resignation/removal; successor appointment |
| **Art. VI — Administration** | Annual accountings, EIN, trust situs, tax filings |
| **Art. VII — Termination & Remainder** | Terminates at beneficiary death; NO Medicaid payback; remainder to designated beneficiaries |
| **Art. VIII — Tax Provisions** | Grantor vs. non-grantor election; gift tax treatment; tax allocation |
| **Art. IX — General Provisions** | Severability, governing law, spendthrift, anti-alienation |
| **Execution** | Grantor signature (notarized), trustee acceptance, notary acknowledgment |
| **Schedule A** | Initial trust assets (if funded at execution) |

### Purpose Statement Template

```text
This Trust is established solely to provide for the supplemental and extra
needs of the Beneficiary beyond those provided by any local, state, or
federal government program. It is the Grantor's intent that Trust assets
shall NOT supplant, replace, impair, or reduce any public benefits to which
the Beneficiary is or may become entitled.
```

### Permissible Distribution Categories

- Medical/dental care not covered by Medicaid
- Therapy, rehabilitation, habilitation services
- Education, vocational training, tutoring
- Entertainment, recreation, travel, companionship
- Assistive technology, communication devices, electronics
- Personal care attendants (beyond public benefit coverage)
- Vehicle purchase/modification, transportation
- Clothing, personal items, quality-of-life enhancements
- Legal, financial, and benefits planning services
- Trust-owned residence expenses (see ISM rules below)

### Prohibited Distributions — ISM Rules

| Prohibited | Compliant Alternative |
|---|---|
| Cash directly to beneficiary | Pay vendors/providers directly |
| Food purchases for beneficiary | Use ABLE account if available; accept ISM reduction if justified |
| Shelter costs paid to/for beneficiary | Trust purchases and holds title to residence; trustee pays carrying costs |
| Rent paid to beneficiary's landlord | Structure as trust-owned housing or accept ISM reduction with documented cost-benefit analysis |

> **Trustee instruction**: Before any distribution that could affect benefits, consult a public benefits specialist. Document the analysis in trust records.

### Remainder Distribution Template

```text
Upon the death of the Beneficiary, the Trustee shall distribute remaining
Trust assets to the following remainder beneficiaries, free of any obligation
to reimburse any governmental entity for benefits provided to the Beneficiary
during the Beneficiary's lifetime:
  [Remainder beneficiary designations with shares and contingencies]
```

---

## Step 3: Execute Compliance Verification

### Required Deliverable: Execution Checklist

| Item | Verification |
|---|---|
| Grantor signature | Notarized (best practice even if not required by state law) |
| Trustee acceptance | Signed acceptance of fiduciary duties |
| Witnesses | Per state requirement; disqualification screening completed |
| Notary acknowledgment | Venue and seal; state-prescribed language if applicable |
| Irrevocability | Unambiguously stated; no reserved amendment power |
| Spendthrift clause | Assets not assignable by beneficiary; not reachable by creditors |
| Discretionary standard | "Sole and absolute discretion" — no enforceable right to demand distributions |
| No payback clause | Explicitly disclaimed; no Medicaid reimbursement obligation |
| Defined terms | "Grantor," "Trustee," "Beneficiary," "Trust" used consistently; cross-references verified |

---

## Step 4: Produce Final Package

### Mandatory Front Matter

At the top of every output:

1. **Assumptions Used** — jurisdiction, funding plan, tax posture, key facts relied on
2. **Open Items / Needed Inputs** — missing data, unresolved jurisdictional questions, unverified citations

### Deliverable Package

1. Complete third-party SNT document
2. Execution compliance checklist (filled)
3. State-specific notes and `[VERIFY]` items for attorney review

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial package, ask:

1. Does the distribution standard and trustee discretion language match intent?
2. Are the remainder beneficiary designations and shares correct?
3. Is the funding plan (immediate vs. deferred) correctly reflected?
4. Should ABLE account funding authority be included or modified?
5. Does the tax posture (grantor vs. non-grantor) need adjustment?

---

## Quality Audit

Before finalizing, verify:

- [ ] Jurisdiction identified and state-law scaffold completed
- [ ] Irrevocability stated unambiguously
- [ ] Supplemental-only purpose statement included
- [ ] No Medicaid payback clause — explicitly disclaimed
- [ ] Sole and absolute discretion standard used throughout
- [ ] Spendthrift and anti-alienation clauses present
- [ ] ISM guidance included with prohibited/compliant alternatives
- [ ] Remainder distribution explicitly free of government reimbursement
- [ ] ABLE account coordination addressed if beneficiary qualifies
- [ ] Gift tax treatment addressed (Crummey powers flagged if needed)
- [ ] Grantor vs. non-grantor trust election specified
- [ ] Execution formalities match state requirements `[VERIFY]`
- [ ] Every statutory citation verified or marked `[VERIFY]`
- [ ] Assumptions and open items listed in front matter
- [ ] No first-party/self-settled SNT provisions (payback, age-65 restrictions)

---

## Guidelines

- **No Medicaid payback** — this is the defining characteristic of a third-party SNT; explicitly disclaim any reimbursement obligation in the termination article
- **Do not rely on memory** for state Medicaid manual treatment of third-party SNTs — require statute URLs or official guidance; flag with `[VERIFY]`
- **Gift tax**: if grantor wants annual exclusion eligibility, a Crummey power may be needed — flag for attorney review; otherwise contributions use lifetime exemption
- **ABLE coordination**: if beneficiary qualifies (disability onset before age 26), include trustee authority to fund ABLE account up to annual limit for food/shelter flexibility
- **Do not draft** first-party/self-settled SNT provisions — those require a separate skill
- **Do not advise** on clinical or benefits eligibility determinations — this is legal structuring only
- **Attorney review required** — include disclaimer and execution-readiness statement in final output
