---
name: uk-regulator-enumeration
created: 2026-04-27
retrieved: 2026-05-03
refresh_recommended_by: 2027-05-03
status: source-verified — M1 business-skill-improvements
audience: every advisor skill in the biz pack (`/slo-legal`, `/slo-accounting`, `/slo-equity`, `/slo-fundraise`, `/slo-hire`)
purpose: |
  Closed enumeration of UK regulators with statutory enforcement powers. The
  `gate-1-regulated` predicate in `references/biz/triage-gate.md` is evaluated by consulting
  THIS file, not by enumerating from training memory.

  Companion to `references/biz/jurisdiction-uk.md` (which is the prose-shaped overview);
  this file is the closed canonical enum the predicate evaluation MUST match against.
---

# UK regulator enumeration — `gate-1-regulated` source-of-truth

The advisor skills MUST consult this file when evaluating `gate-1-regulated`. Naming a regulator that is NOT on this list is a refusal pattern: either (a) the founder is not actually facing a regulated matter (probe further), or (b) the regulator is missing from this file and the founder should flag it as a content gap (do not bypass — extending the file is `/slo-architect` re-pass discipline).

## Schema

Each row is a `regulator_id` (kebab-slug, stable interface — referenced by intake forms in `references/biz/legal-intake-contract.md` etc.) plus structured metadata.

| Field | Type | Notes |
|---|---|---|
| `id` | string (kebab-slug) | Stable identifier for predicate evaluation |
| `display_name` | string | Human-readable name |
| `domain` | string | One-line description of regulatory scope |
| `statutory_basis` | string | Primary legislation (Act + year) |
| `default_route_to` | enum | `lawyer-specialist` / `lawyer` / `accountant` / `dpo` / `combined` |
| `cited_by` | list | Which advisor skills typically cite this regulator |
| `last_reviewed` | date (YYYY-MM-DD) | Annual cadence; stale > 12 months → refresh PR |

## Source verification register

Each row below is the authority audit surface for the closed enum. `last_checked` is the SLO verification date; `next_review_due` is the annual refresh date. `last_amended` records the revised-source position seen at retrieval time, not a legal opinion about every downstream amendment.

| id | primary_authority | statute_url | commenced_date | last_amended | last_checked | next_review_due | confidence |
|---|---|---|---|---|---|---|---|
| `hmrc` | Taxes Management Act 1970; Income Tax Act 2007; ITEPA 2003 Chapter 10 | https://www.legislation.gov.uk/ukpga/1970/9/contents; https://www.legislation.gov.uk/ukpga/2007/3/contents; https://www.legislation.gov.uk/ukpga/2003/1/part/2/chapter/10 | 1970-03-12 / 2007-03-20 / 2003-03-06 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |
| `companies-house` | Companies Act 2006; Economic Crime and Corporate Transparency Act 2023 | https://www.legislation.gov.uk/ukpga/2006/46/contents; https://www.legislation.gov.uk/ukpga/2023/56/contents | 2006-11-08 / 2023-10-26 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |
| `pensions-regulator` | Pensions Act 2008 | https://www.legislation.gov.uk/ukpga/2008/30/contents | 2008-11-26 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |
| `ico` | Data Protection Act 2018; PECR 2003; Data (Use and Access) Act 2025 | https://www.legislation.gov.uk/ukpga/2018/12/contents; https://www.legislation.gov.uk/uksi/2003/2426/contents; https://www.legislation.gov.uk/ukpga/2025/18/contents | 2018-05-23 / 2003-12-11 / 2025-06-19 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |
| `ofcom` | Communications Act 2003; Online Safety Act 2023 | https://www.legislation.gov.uk/ukpga/2003/21/contents; https://www.legislation.gov.uk/ukpga/2023/50/contents | 2003-07-17 / 2023-10-26 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |
| `fca` | Financial Services and Markets Act 2000 | https://www.legislation.gov.uk/ukpga/2000/8/contents | 2000-06-14 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |
| `pra` | Financial Services and Markets Act 2000; Bank of England Act 1998 | https://www.legislation.gov.uk/ukpga/2000/8/contents; https://www.legislation.gov.uk/ukpga/1998/11/contents | 2000-06-14 / 1998-04-23 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |
| `cma` | Competition Act 1998; Enterprise Act 2002; Digital Markets, Competition and Consumers Act 2024 | https://www.legislation.gov.uk/ukpga/1998/41/contents; https://www.legislation.gov.uk/ukpga/2002/40/contents; https://www.legislation.gov.uk/ukpga/2024/13/contents | 1998-11-09 / 2002-11-07 / 2024-05-24 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |
| `asa` | CAP Code and ASA self-regulatory remit; Ofcom statutory backstop for broadcast | https://www.asa.org.uk/codes-and-rulings/advertising-codes/non-broadcast-code.html; https://www.legislation.gov.uk/ukpga/2003/21/contents | self-regulatory code / 2003-07-17 | code page current at source check | 2026-05-03 | 2027-05-03 | medium |
| `tsi` | Consumer Rights Act 2015; Consumer Protection from Unfair Trading Regulations 2008 | https://www.legislation.gov.uk/ukpga/2015/15/contents; https://www.legislation.gov.uk/uksi/2008/1277/contents | 2015-03-26 / 2008-05-26 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |
| `mhra` | Medicines Act 1968; Human Medicines Regulations 2012; Medical Devices Regulations 2002 | https://www.legislation.gov.uk/ukpga/1968/67/contents; https://www.legislation.gov.uk/uksi/2012/1916/contents; https://www.legislation.gov.uk/uksi/2002/618/contents | 1968-10-25 / 2012-08-14 / 2002-03-08 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |
| `cqc` | Health and Social Care Act 2008 | https://www.legislation.gov.uk/ukpga/2008/14/contents | 2008-07-21 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |
| `gmc` | Medical Act 1983 | https://www.legislation.gov.uk/ukpga/1983/54/contents | 1983-10-26 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |
| `nmc` | Nursing and Midwifery Order 2001 | https://www.legislation.gov.uk/uksi/2002/253/contents | 2002-02-12 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |
| `hcpc` | Health Professions Order 2001 | https://www.legislation.gov.uk/uksi/2002/254/contents | 2002-02-12 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |
| `hse` | Health and Safety at Work etc. Act 1974 | https://www.legislation.gov.uk/ukpga/1974/37/contents | 1974-07-31 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |
| `ehrc` | Equality Act 2006; Equality Act 2010 | https://www.legislation.gov.uk/ukpga/2006/3/contents; https://www.legislation.gov.uk/ukpga/2010/15/contents | 2006-02-16 / 2010-04-08 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |
| `ofgem` | Gas Act 1986; Electricity Act 1989; Utilities Act 2000 | https://www.legislation.gov.uk/ukpga/1986/44/contents; https://www.legislation.gov.uk/ukpga/1989/29/contents; https://www.legislation.gov.uk/ukpga/2000/27/contents | 1986-07-25 / 1989-07-27 / 2000-07-28 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |
| `ofwat` | Water Industry Act 1991 | https://www.legislation.gov.uk/ukpga/1991/56/contents | 1991-07-25 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |
| `ofsted` | Education and Inspections Act 2006; Care Standards Act 2000 | https://www.legislation.gov.uk/ukpga/2006/40/contents; https://www.legislation.gov.uk/ukpga/2000/14/contents | 2006-11-08 / 2000-07-20 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |
| `caa` | Civil Aviation Act 2012; Air Navigation Order 2016 | https://www.legislation.gov.uk/ukpga/2012/19/contents; https://www.legislation.gov.uk/uksi/2016/765/contents | 2012-12-19 / 2016-07-19 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |
| `environment-agency` | Environment Act 2021; Environmental Permitting Regulations 2016 | https://www.legislation.gov.uk/ukpga/2021/30/contents; https://www.legislation.gov.uk/uksi/2016/1154/contents | 2021-11-09 / 2016-12-06 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |
| `charity-commission` | Charities Act 2011 | https://www.legislation.gov.uk/ukpga/2011/25/contents | 2011-12-14 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |
| `oisc` | Immigration and Asylum Act 1999 Part V | https://www.legislation.gov.uk/ukpga/1999/33/part/V | 1999-11-11 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |
| `solicitors-regulation-authority` | Legal Services Act 2007; Solicitors Act 1974 | https://www.legislation.gov.uk/ukpga/2007/29/contents; https://www.legislation.gov.uk/ukpga/1974/47/contents | 2007-10-30 / 1974-07-31 | revised source current at source check | 2026-05-03 | 2027-05-03 | high |

## The enumeration (last-reviewed: 2026-04-27)

### Tax + corporate

| id | display_name | domain | statutory_basis | default_route_to | cited_by |
|---|---|---|---|---|---|
| `hmrc` | HM Revenue & Customs | Tax — corporation tax, VAT, PAYE/NI, R&D credits, SEIS/EIS, IR35 | Taxes Management Act 1970; Finance Acts; Income Tax Act 2007 (SEIS/EIS); ITEPA 2003 Chapter 10 (IR35) | `accountant` | `slo-accounting`, `slo-fundraise`, `slo-equity`, `slo-hire` |
| `companies-house` | Companies House | Company filings, registration, beneficial ownership, persons of significant control | Companies Act 2006; Economic Crime and Corporate Transparency Act 2023 | `accountant` | `slo-equity`, `slo-accounting` |
| `pensions-regulator` | The Pensions Regulator (TPR) | Workplace pensions auto-enrolment | Pensions Act 2008 | `accountant` | `slo-hire`, `slo-accounting` |

### Data + privacy + communications

| id | display_name | domain | statutory_basis | default_route_to | cited_by |
|---|---|---|---|---|---|
| `ico` | Information Commissioner's Office | UK GDPR; PECR; DPA 2018; FOI; Direct marketing; DUAA 2025 | Data Protection Act 2018; UK GDPR (retained); PECR 2003; DUAA 2025 | `dpo` (or `lawyer + dpo` if no DPO) | `slo-legal` (gate-4 supersedes), `slo-marketing`, `slo-sales-funnel`, `slo-accounting` (records of processing) |
| `ofcom` | Office of Communications | Telecoms, broadcasting, postal services, online safety | Communications Act 2003; Online Safety Act 2023 | `lawyer-specialist` | `slo-legal`, `slo-marketing` |

### Financial services + competition + consumer

| id | display_name | domain | statutory_basis | default_route_to | cited_by |
|---|---|---|---|---|---|
| `fca` | Financial Conduct Authority | Financial services, regulated activities, AR/authorisation, consumer credit, financial promotion | Financial Services and Markets Act 2000 (FSMA) | `lawyer-specialist` | All four advisors |
| `pra` | Prudential Regulation Authority | Banks, insurers, investment firms — prudential regulation | FSMA 2000 + Bank of England Act 1998 | `lawyer-specialist` | `slo-fundraise` (rare; mostly when scaling into FS) |
| `cma` | Competition and Markets Authority | Mergers, anti-competitive conduct, consumer law (incl. DMCC 2024) | Competition Act 1998; Enterprise Act 2002; Digital Markets, Competition and Consumers Act 2024 | `lawyer-specialist` | `slo-fundraise` (round-related), `slo-legal` (B2B) |
| `asa` | Advertising Standards Authority | Non-broadcast and broadcast advertising; CAP Code; influencer disclosure | Self-regulatory; backed by Ofcom for broadcast | `lawyer-specialist` | `slo-marketing`, `slo-launch` |
| `tsi` | Trading Standards (via OPSS / local authorities) | Consumer protection, product safety, weights & measures, CRA 2015 enforcement | Consumer Rights Act 2015; Consumer Protection from Unfair Trading Regulations 2008 | `lawyer-specialist` | `slo-pricing` (B2C subscription), `slo-marketing` (B2C) |

### Health + life sciences + medicines

| id | display_name | domain | statutory_basis | default_route_to | cited_by |
|---|---|---|---|---|---|
| `mhra` | Medicines and Healthcare products Regulatory Agency | Medicines, medical devices, clinical trials | Medicines Act 1968; Human Medicines Regulations 2012; Medical Devices Regulations 2002 | `lawyer-specialist` + `accountant` (R&D context) | `slo-equity`, `slo-fundraise` |
| `cqc` | Care Quality Commission | Health and social care providers (England) | Health and Social Care Act 2008 | `lawyer-specialist` | All four advisors |
| `gmc` | General Medical Council | Medical practitioners | Medical Act 1983 | `lawyer-specialist` | Rare in seed-stage context; flag if relevant |
| `nmc` | Nursing and Midwifery Council | Nursing and midwifery practitioners | Nursing and Midwifery Order 2001 | `lawyer-specialist` | Rare |
| `hcpc` | Health and Care Professions Council | Allied health professionals (16 professions) | Health Professions Order 2001 | `lawyer-specialist` | Rare |

### Workplace + employment

| id | display_name | domain | statutory_basis | default_route_to | cited_by |
|---|---|---|---|---|---|
| `hse` | Health and Safety Executive | Workplace health & safety | Health and Safety at Work etc. Act 1974 | `lawyer-specialist` (employment) | `slo-hire` |
| `ehrc` | Equality and Human Rights Commission | Equality law enforcement | Equality Act 2006 + Equality Act 2010 | `lawyer-specialist` (employment) | `slo-hire`, `slo-marketing` (B2C anti-discrimination) |

### Utilities + sector regulators

| id | display_name | domain | statutory_basis | default_route_to | cited_by |
|---|---|---|---|---|---|
| `ofgem` | Office of Gas and Electricity Markets | Energy markets | Gas Act 1986; Electricity Act 1989; Utilities Act 2000 | `lawyer-specialist` | Rare |
| `ofwat` | Water Services Regulation Authority | Water and sewerage | Water Industry Act 1991 | `lawyer-specialist` | Rare |
| `ofsted` | Office for Standards in Education, Children's Services and Skills | Education and children's services | Education Acts; Care Standards Act 2000 | `lawyer-specialist` | Rare |
| `caa` | Civil Aviation Authority | Civil aviation, drones (UAS) | Civil Aviation Act 2012 + Air Navigation Order | `lawyer-specialist` | Rare; flag if drones / aviation in scope |

### Sector-specific (environment + others)

| id | display_name | domain | statutory_basis | default_route_to | cited_by |
|---|---|---|---|---|---|
| `environment-agency` | Environment Agency (England) | Environmental permits, waste, water resources | Environment Act 2021; Environmental Permitting Regulations 2016 | `lawyer-specialist` | Rare |
| `charity-commission` | Charity Commission for England and Wales | Registered charities | Charities Act 2011 | `lawyer-specialist` (charity law) | If founder is operating CIC / charity vehicle alongside |
| `oisc` | Office of the Immigration Services Commissioner | Immigration advisers | Immigration and Asylum Act 1999 Part V | `lawyer-specialist` | Rare; flag if visa-sponsorship business |
| `solicitors-regulation-authority` | Solicitors Regulation Authority (SRA) | Solicitors and law firms | Legal Services Act 2007 | `lawyer-specialist` | If founder is a regulated legal-tech provider |

## Per-skill routing override patterns

The `default_route_to` value is the floor; advisor skills MAY override based on which regulator's domain is most relevant:

- **`/slo-accounting`** routes HMRC / Companies House / Pensions Regulator firings to **accountant** (overrides the gate-1 lawyer default per the per-skill override pattern). Cross-discipline matters (e.g., FCA-regulated activity with accounting consequences) route to **lawyer-specialist + accountant**.
- **`/slo-fundraise`** routes HMRC SEIS/EIS firings to **accountant** for the qualifying-trade determination; routes Companies House share-allotment firings to **lawyer + accountant**; routes FCA financial-promotion concerns to **lawyer-specialist**.
- **`/slo-equity`** routes Companies House cap-table firings to **lawyer + accountant** (cap-table changes are corporate-secretarial *and* tax-relevant).
- **`/slo-hire`** routes Pensions Regulator + HSE + EHRC firings — combined as appropriate.
- **`/slo-legal`** routes ICO firings to `dpo (or lawyer + dpo if no DPO)` per gate-4 supersedence.

## Predicate evaluation procedure

When `slo-legal` (or any advisor skill) evaluates `gate-1-regulated`:

1. Read `intake_summary.regulator_in_scope` from the structured intake form.
2. If `false`, gate-1 passes.
3. If `true`, read `intake_summary.regulator_id` and look it up in the table above.
4. **If `regulator_id` is not in the table, refuse**. Do not match heuristically. Either (a) the founder confirms it's not the body they mean and picks from the closed enum, or (b) the gap is flagged as a follow-up content extension.
5. If found, gate-1 fires unless `intake_summary.regulator_relationship == incidental`. Route to the regulator's `default_route_to`, applying the per-skill override pattern above.

## Adding a new regulator

This file is `status: stable-interface` — append-only without a `/slo-architect` re-pass; no removals or `id` renames.

**Append procedure**:

1. Add a row to the appropriate sub-table.
2. Bump `last_reviewed:` to the date of the append.
3. Add a structural-contract test in `crates/sldo-install/tests/` (per issue #19 M5 acceptance criteria) that asserts the new `id` is referenced by at least one advisor SKILL.md.
4. `/slo-critique` security-persona review of the new row before merge.

## Annual refresh

The file's `last_reviewed:` triggers a refresh PR when stale > 12 months. The skill emits a warning analogous to the cost-baseline staleness pattern in `/slo-legal` SKILL.md if any advisor skill consults a > 12-month-stale enumeration.

## Out of scope

- Devolved-administration variations beyond E&W (Scottish-only / NI-only regulators flagged in the `domain:` column rather than as separate rows).
- Self-regulatory bodies without statutory backing (these don't fire `gate-1-regulated`; they may be cited in body prose for completeness).
- Non-UK regulators (v1 jurisdiction stance per `references/biz/jurisdiction-uk.md`).

## Cross-references

- `references/biz/triage-gate.md` — the predicate this file resolves.
- `references/biz/jurisdiction-uk.md` — narrative version of UK regulator scope.
- `references/biz/legal-intake-contract.md` — F5 field uses `id` values from this file as the closed enum.
- `references/biz/hmrc-vcm-index.md` — HMRC VCM-specific anchors for SEIS/EIS firings.
- `references/biz/ico-duaa-index.md` — ICO DUAA 2025 anchors for ICO firings.
- `references/biz/ir35-cest-factors.md` — HMRC IR35 specifics for `slo-hire`.
