---
name: research-regulator-guidance-lookup-sboghossian
title: Regulator Guidance Lookup
description: 'Use when a user needs not the statute itself but the regulatory body''s official interpretation — FAQs, guidance notes, policy statements, circulars, and implementing instructions that control how a rule is applied in practice. MENA-primary: covers DFSA, FSRA, SAMA, CMA (KSA), SCA (UAE), CBUAE, BDL (Lebanon), FATF guidance, IFRS pronouncements, and EU Commission guidelines. Flags when guidance contradicts or softens the literal statutory reading — a critical distinction for compliance work.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/research/research-regulator-guidance-lookup
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# Regulator Guidance Lookup

Retrieve official interpretive guidance, FAQs, policy statements, circulars, and implementing instructions issued by regulatory authorities. Statutes state the rule; regulator guidance explains how the regulator will apply it — and the two can diverge in ways that are critical to compliance practice.

## When to use this

- The statute has been retrieved but its practical application is unclear
- A compliance team is designing a compliance program and needs to know the regulator's expectations, not just the law's text
- A license application is being prepared and the regulator's application guidance is needed
- A client received a regulator inquiry and guidance notes may clarify the position
- A transaction involves a regulated activity and the regulator's policy on a specific point needs to be confirmed
- The statutory rule appears to require X, but market practice is Y — guidance may explain the discrepancy

**Key principle**: In regulated financial, healthcare, and professional-services markets, regulator guidance often controls day-to-day compliance more than the parent statute. A statutory obligation that a regulator has informally relaxed in guidance creates less actual risk than the text alone suggests; a permissive statutory provision that the regulator has hardened in guidance creates more risk.

## Inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| Regulatory area or topic | Focuses the guidance search | Required |
| Regulator / jurisdiction | Different regulators in the same jurisdiction cover different sectors | Required |
| Specific statutory provision | Guidance is often organized by the statute article it interprets | Provide if known |
| Date sensitivity | Guidance is frequently superseded; recency matters | Default: current (post-supersession) guidance only |

## Regulator guidance sources

### UAE Financial Services

| Regulator | Jurisdiction | Guidance types | Source |
|-----------|-------------|----------------|--------|
| **DFSA** (Dubai Financial Services Authority) | DIFC | Policy Statements, Guidance Notes, Consultation Papers, Decision Notices; DFSA Rulebook itself is interpretive | dfsa.ae — Supervision & Policy |
| **FSRA** (Financial Services Regulatory Authority) | ADGM | Guidance Notes, Policy Statements, FAQs by topic area | adgm.com/fsra |
| **SCA** (Securities and Commodities Authority) | UAE onshore | Decisions, Chairman Resolutions, FAQs | sca.gov.ae |
| **CBUAE** (Central Bank of UAE) | UAE onshore (banking/payments) | Notices, Circulars, Standards (e.g., AML/CFT Standards, Open Banking Framework) | centralbank.ae |

### KSA Financial Services

| Regulator | Guidance types | Source |
|-----------|----------------|--------|
| **SAMA** (Saudi Arabian Monetary Authority) | Implementing Regulations, Circulars, FAQs on banking, insurance, payment systems, AML | sama.gov.sa |
| **CMA** | Resolutions, Notes on Interpretation, FAQs on capital markets rules | cma.org.sa |
| **ZATCA** | VAT guides by sector, ruling letters, technical guidance | zatca.gov.sa |

### Lebanon

| Regulator | Guidance types | Source |
|-----------|----------------|--------|
| **BDL** (Banque du Liban) | Circulars (most authoritative guidance on banking sector); BDL Basic Circular + Intermediate Circulars | bdl.gov.lb |
| **SIC** (Special Investigation Commission) | AML guidance, suspicious-transaction reporting requirements | sic.gov.lb |
| **Insurance Control Commission** | Insurance sector guidance | under Ministry of Economy |

**Lebanon note**: BDL Circulars are the primary operative legal instrument in much of the banking sector, sometimes more current and specific than the underlying statutes. The numbering runs to Circular No. 600+; always verify the supersession chain.

### Cross-jurisdictional frameworks

| Body | Guidance type | Relevance |
|------|--------------|-----------|
| **FATF** (Financial Action Task Force) | 40 Recommendations + Best Practices Guidance + Risk-Based Approach Guidance by sector | The global AML/KYC framework; all MENA regulators are FATF members or associate members; guidance shapes national regulator expectations |
| **IFRS / IFAC** | Technical pronouncements, interpretations (IFRICs), educational materials | Applies to financial reporting across all MENA jurisdictions that have adopted IFRS (UAE, KSA, Lebanon, EG) |
| **EDPB** (European Data Protection Board) | Guidelines, opinions, recommendations on GDPR application | Applies to organizations processing EU personal data regardless of location; relevant for MENA companies with EU operations |

### EU

| Body | Guidance type | Source |
|------|--------------|--------|
| **European Commission** | Implementation guidance on EU Directives; FAQ documents; interpretive communications | ec.europa.eu |
| **ESMA** (European Securities and Markets Authority) | Q&As on MiFID II, MAR, AIFMD, EMIR, etc. | esma.europa.eu |
| **EBA** (European Banking Authority) | Q&As on CRD/CRR, AML Directive implementation | eba.europa.eu |

### UK

| Body | Guidance type | Source |
|------|--------------|--------|
| **FCA** | Policy Statements, Consultation Papers, Guidance Consultations, Dear CEO letters | fca.org.uk |
| **PRA** | Supervisory Statements, Policy Statements | bankofengland.co.uk/prudential-regulation |
| **ICO** (Information Commissioner's Office) | GDPR guidance, enforcement notices | ico.org.uk |

## Output schema

```json
{
  "issuer": "name of regulatory body",
  "title": "full title of guidance document",
  "dateIssued": "ISO date",
  "reference": "circular number / policy statement number / reference code",
  "summary": "2–3 sentence description of the guidance content",
  "keyPositions": [
    "Specific interpretive positions stated in the guidance, each as one bullet"
  ],
  "divergenceFromStatute": "If the guidance softens, hardens, or clarifies the literal statutory reading, describe the divergence explicitly",
  "supersedes": ["list of earlier guidance documents this supersedes, if stated"],
  "supersededBy": "if this guidance has been superseded, identify the replacement",
  "currentStatus": "in-force | superseded | withdrawn | consultation-only",
  "linkToSource": "URL if available"
}
```

## Divergence flag — critical for compliance

The most practically important output field is `divergenceFromStatute`. Examples of common divergences:

- **Softening**: the statute requires X in all cases; DFSA Guidance Note says the requirement is waived for firms with assets below a threshold — relevant for a small DIFC firm.
- **Hardening**: the statute prohibits Y; a SAMA Circular extends the prohibition to instruments structured to achieve the same economic result — relevant for financial product design.
- **Clarification**: the statute is ambiguous on whether a specific activity requires a license; an FSRA FAQ confirms it does — or confirms it doesn't.

Always flag divergences prominently rather than leaving the reader to reconcile them.

## Supersession tracking

Guidance is frequently superseded. Before relying on a guidance document:
1. Check whether the document is marked "superseded" or "withdrawn" on the regulator's website.
2. Check whether the parent statute the guidance interprets has been amended since the guidance was issued — if so, the guidance may no longer reflect current law.
3. For BDL Circulars: check the BDL circular index for any later circular that expressly or impliedly supersedes the one in question.

## Limits

- Regulator guidance is not law — courts may interpret a statutory provision differently from how the regulator's guidance describes it. In a dispute, the court's interpretation is authoritative.
- Unpublished guidance (e.g., letters to specific firms) is not generally accessible. Where a compliance program is structured on the basis of unpublished guidance, it is vulnerable if the regulator's position changes.
- FATF guidance is non-binding on its own; it becomes binding when incorporated into national implementing regulations. Always verify the national regulatory implementation.

## Related skills

- [[research-regulation-lookup]]
- [[research-recent-amendments-tracker]]
- [[review-compliance-gap-analysis]]
- [[research-licensing-requirements-lookup]]
- [[research-beneficial-ownership-lookup]]
