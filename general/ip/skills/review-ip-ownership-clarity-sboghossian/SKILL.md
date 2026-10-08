---
name: review-ip-ownership-clarity-sboghossian
title: IP Ownership Clarity Review
description: Use when reviewing contract clauses governing intellectual property ownership, assignment, and licensing across any engagement type. Covers work-product ownership, background IP carve-outs, foreground assignment language precision, moral rights, joint inventorship, improvements, open-source obligations, and registration formalities. Applies across jurisdictions with particular attention to US, UK, EU, DIFC/ADGM, Lebanon, Egypt, and France where moral-rights regimes differ materially.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-ip-ownership-clarity
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# IP Ownership Clarity Review

## When to use this

Use this skill when:
- Reviewing a services, development, or consulting agreement where IP is created during the engagement
- Reviewing an employment or contractor agreement to confirm IP assignment is effective
- Conducting M&A due diligence on the target's IP chain of title
- Reviewing an NDA or collaboration agreement that creates joint output
- A client suspects the counterparty may retain rights to work they commissioned

## Inputs

| Input | Why it matters | Default |
|---|---|---|
| Contract text | The IP, assignment, and license provisions | Required |
| Jurisdiction(s) | Default ownership rules differ substantially (work-for-hire, employee inventions) | Required |
| Nature of work | Software, creative content, inventions, mixed — dictates which regimes apply | Infer from context |
| Background IP inventory | What pre-existing IP each party brought in | Helpful; ask if unclear |
| Party perspective | Helps frame severity: vendor keeping IP vs client keeping IP | Ask if unclear |

## Review Methodology

### Step 1 — Identify who created what

Before reading the contract, map the categories of work product that will or have been created: software code, copyrightable content, inventions, data, know-how, training data, AI model outputs. Each category may have different default ownership rules.

### Step 2 — Check foreground IP assignment language

**The critical distinction**: "hereby assigns" vs "agrees to assign."

- **"Hereby assigns"** — present-tense, self-executing assignment; IP vests in the assignee on creation without further action. This is the correct standard for enforceable IP assignments.
- **"Agrees to assign"** or "will assign" — executory promise; requires a further assignment instrument. Until that instrument is executed, IP stays with the creator. This is the _Stanford v Roche_ trap in US law (Federal Circuit, 2011): an obligation to assign is not an assignment.

Enforce present-tense language. If the agreement says "agrees to assign," recommend: (1) amend to "hereby assigns" or (2) ensure a separate assignment instrument is executed contemporaneously with each deliverable.

### Step 3 — Background IP carve-out and license-back

Background IP is pre-existing IP each party owns before the engagement, or developed outside the scope of the engagement. A complete clause covers:

- **Definition**: what counts as background IP (by date, by category, by registration)
- **Carve-out**: background IP is not assigned — it remains with its original owner
- **License-back**: the party that retains background IP grants the other a license to use it as embedded in or necessary to use the deliverables. Scope of license matters: perpetual? royalty-free? sublicensable? limited to internal use only?

Flag if: (a) background IP is not defined or carved out — everything created "during the engagement" including pre-existing tools gets assigned; (b) license-back is too narrow (e.g., "for the purpose of this agreement only" — client cannot continue to use deliverables if agreement terminates).

### Step 4 — Moral rights

Moral rights protect an author's personal connection to their work (right of attribution, right of integrity, right to oppose derogatory treatment). Their treatability differs by jurisdiction:

| Jurisdiction | Moral rights regime | Waivable? |
|---|---|---|
| US | Very limited moral rights (VARA for visual art only; §106A Copyright Act) | Yes, for visual art |
| UK | Copyright, Designs and Patents Act 1988 — attribution + integrity rights | Yes, by contract |
| France | Droit moral — perpetual, inalienable, imprescriptible | No — cannot waive |
| Lebanon | Law No. 75 of 1999 on the Protection of Literary and Artistic Property — moral rights inalienable | No |
| Egypt | Intellectual Property Protection Law No. 82 of 2002 — moral rights perpetual | No |
| UAE (onshore) | Federal Law No. 38 of 2021 on Copyright — moral rights protected | No (generally) |
| DIFC / ADGM | English common-law copyright; DIFC IP Law — moral rights can be waived | Yes |

In civil-law jurisdictions (FR, LB, EG, UAE onshore): you cannot contractually waive moral rights. A clause that says "Author irrevocably waives all moral rights" is unenforceable in these jurisdictions. The practical consequence is that if the author is based in Lebanon or Egypt, they retain the right to be credited and to object to changes that harm their honor or reputation — even if they assign copyright. Flag this for clients commissioning creative or software work in these jurisdictions.

### Step 5 — Joint inventorship

If two or more parties will contribute to inventions, map:

- **Default rule**: under most patent systems (US, EPO, UAE), each co-inventor/co-owner can practice the patent independently without the consent of or accounting to the other, unless the agreement changes this.
- Flag if: no joint IP governance is specified; no provision for who pays prosecution costs; no mechanism to resolve disputes on whether to file, enforce, or license.

### Step 6 — Improvements and derivatives

If Party A licenses technology to Party B and Party B makes improvements:
- Who owns the improvements? (default: typically the improver, but many agreements grant the licensor an automatic license or assignment of improvements — "grant-back")
- Grant-back clauses can be anti-competitive in the EU (block exemptions under Technology Transfer Agreements regulation).
- In MENA: grant-backs are less regulated; flag commercial risk to licensor of losing control of improvements.

### Step 7 — Open-source obligations

Check whether deliverables incorporate open-source components subject to copyleft licenses (GPL, LGPL, AGPL, EUPL). Copyleft contamination can:
- Require disclosure of proprietary source code
- Void "work-for-hire" expectations
- Restrict commercial use

A complete agreement should require: (a) vendor to disclose all open-source components used; (b) vendor to represent no copyleft contamination of proprietary deliverables; (c) client approval for use of strong copyleft licenses.

### Step 8 — Registration and recordation formalities

IP assignments may require formal registration to be effective against third parties:

| Jurisdiction | Formality |
|---|---|
| US patents | USPTO recordation recommended; must be recorded within 3 months to defeat subsequent purchaser |
| EU trademarks | EUIPO recordation |
| UK post-Brexit | UKIPO recordation |
| UAE | Ministry of Economy IP registration; for DIFC, DIFC IP registry |
| KSA | Saudi Authority for Intellectual Property (SAIP) recordation |
| Lebanon | Ministry of Economy and Trade; Commerce Court registration for trademarks |

Flag agreements that are silent on who bears the cost and obligation of filing assignment recordals.

## What to Flag

| Severity | Issue |
|---|---|
| Critical | No assignment clause at all — default rules apply (often vest IP in creator) |
| Critical | "Agrees to assign" instead of "hereby assigns" — executory promise only |
| Critical | Background IP not carved out — vendor's pre-existing tools inadvertently assigned |
| Critical | No license-back of background IP necessary to use deliverables |
| High | Moral-rights waiver in civil-law jurisdiction (FR, LB, EG, UAE onshore) — unenforceable |
| High | Open-source disclosure obligation absent |
| High | No joint-IP governance for jointly-developed inventions |
| Medium | License-back scope too narrow (terminates with agreement) |
| Medium | No recordation obligation specified |
| Low | Definition of "Confidential Information" may overlap with "Background IP" — creates ambiguity |

## Output Format

```json
{
  "findings": [
    {
      "clause": "<section>",
      "issue": "<description>",
      "severity": "critical|high|medium|low",
      "jurisdictional_note": "<if applicable>",
      "suggested_fix": "<redline recommendation>"
    }
  ],
  "overall_risk_score": "<low|medium|high|critical>",
  "assignment_language_ok": true/false,
  "background_ip_carved_out": true/false,
  "license_back_adequate": true/false,
  "moral_rights_addressed": true/false,
  "open_source_addressed": true/false
}
```

## Jurisdictional Notes Summary

- **DIFC/ADGM**: English common-law treatment; broad freedom to assign and waive moral rights by contract
- **KSA**: IP ownership follows Shariah principles; employment inventions typically belong to employer if using employer resources; SAIP recordation required for patent assignments
- **UAE onshore**: Federal IP laws protect moral rights; work-for-hire only if expressly agreed and limited to specific statutory categories
- **Lebanon / Egypt**: Moral rights inalienable; assignment of copyright only covers economic rights; independent contractors own their work by default unless assigned in writing
- **France**: Droit moral perpetual; software authors (employees) do have reduced moral rights but moral rights still cannot be fully waived

## Common Mistakes

- Treating "work made for hire" as universally available — in most MENA jurisdictions this is not a recognized legal category; written assignment is always needed
- Assigning "all intellectual property rights" without specifying the territory — in some jurisdictions, assignments without territorial scope may be interpreted narrowly
- Omitting a representation that the assignor owns and has the right to assign — no covenant of title
- Using US-style IP assignment boilerplate without checking that "hereby assigns" language survives translation into Arabic (the Arabic equivalent must be similarly present-tense)

## Related Skills

- [[review-msa-deep-review]]
- [[review-nda-quick-check]]
- [[review-unusual-terms-detector]]
- [[review-missing-clauses]]
- [[draft-ip-assignment]]
- [[draft-consulting-agreement]]
