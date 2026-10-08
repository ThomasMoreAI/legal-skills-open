---
name: draft-ip-assignment-sboghossian
title: IP Assignment Agreement
description: Use when drafting an Intellectual Property Assignment Agreement transferring ownership of a portfolio of IP rights (patents, trademarks, copyright, designs, trade secrets, software) from an assignor to an assignee. Covers required inputs, document structure including the critical further-assurances and power-of-attorney provisions, moral rights handling across civil-law and common-law jurisdictions (MENA, FR, UK, US), jurisdiction-by-jurisdiction registry perfection obligations, and common use cases including M&A IP cleanup, founder-to-company, and consultant-to-client transfers.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-ip-assignment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# IP Assignment Agreement

## When to use this

An IP Assignment Agreement transfers the legal ownership of intellectual property rights from the assignor (current owner) to the assignee (recipient). It is broader than a copyright assignment — it covers the full IP portfolio: patents and patent applications, trademarks, registered and unregistered designs, copyright, database rights, trade secrets, know-how, and software.

Use this skill when:
- A company is acquiring another company and needs to ensure full IP ownership follows the acquisition (M&A IP cleanup).
- A founder assigns pre-incorporation IP (code, designs, brand, domain names) to the newly formed company.
- A consultant or contractor is assigning IP created during a services engagement to the client.
- An employee is executing an assignment of inventions and work product as a condition of employment.
- A licensing arrangement converts to a full assignment after a license-to-own period.

Use [[draft-copyright-assignment]] for situations limited to literary, artistic, or software copyright only.

## Required inputs

| Input | Why it matters | Default |
|-------|----------------|---------|
| Assignor (current owner, legal entity type, jurisdiction) | Must be the true legal owner; chain of title verification recommended | — |
| Assignee (recipient entity, jurisdiction) | Determines which registration systems need updating | — |
| IP schedule (Schedule A — full enumeration) | Vague descriptions create ownership disputes; specificity is essential | Attached Schedule A |
| Consideration | Adequate consideration required; may be nominal but must be present | Acknowledged receipt of good and valuable consideration |
| Effective date | Date of transfer; may be retroactive to creation date | Date of signature |
| Future IP scope (if any) | Whether assignment covers work yet to be created | Not included by default |
| Warranties (title, no encumbrances, no third-party claims) | Core protection for Assignee | Standard set included |
| Governing law | Determines moral rights treatment and contract interpretation | Jurisdiction of IP registration |

## Optional inputs
- License-back to Assignor (if Assignor needs to continue using the IP)
- Royalty or earn-out (if consideration is partly contingent on commercial success)
- Non-assertion of moral rights (civil-law jurisdictions)
- Specific registry-filing obligations and timing

## IP Schedule — critical specificity

The IP Schedule (Annex A) must be as specific as possible:

**Patents and applications:**
- Application / registration number.
- Title of invention.
- Country of application.
- Filing date.
- Status (pending / granted / expired).

**Trademarks:**
- Mark name / logo.
- Registration number.
- Country of registration.
- Nice classification.
- Registered owner name to be updated.

**Copyright works:**
- Title of work.
- Type (software, literary, artistic, database).
- Creation date (or approximate period).
- Author(s).
- Registration number if registered.

**Domain names:**
- Full domain names list.
- Registrar.
- Expiry dates.

**Trade secrets / know-how:**
- Description at appropriate level of specificity (avoid disclosing the secret in a publicly filed document).
- Cross-reference to a separately held confidential schedule if needed.

**Software / code:**
- Repository name / location.
- Version or commit reference.
- Languages and frameworks.

## Document structure

### 1. Recitals
State the background: Assignor owns the IP listed in Schedule A; Assignee wishes to acquire ownership; the parties have agreed on consideration; the parties execute this assignment.

### 2. Definitions
Define: "IP Rights" (comprehensive — patents, copyright, trademarks, designs, database rights, trade secrets, know-how, and all other intellectual property rights, whether registered or unregistered, including applications and rights to apply); "Assigned IP" (the IP listed in Schedule A); "Effective Date".

### 3. Assignment — the operative clause
> "With full title guarantee and for good and valuable consideration (the receipt and sufficiency of which is hereby acknowledged), the Assignor hereby assigns, transfers, and conveys to the Assignee, with immediate effect from the Effective Date, the entire right, title, and interest in and to the Assigned IP, including:
> (a) all rights to sue for past, present, and future infringement;
> (b) all rights to claim priority from any registered IP included in the Assigned IP;
> (c) all goodwill associated with the Assigned IP (for trademark assignments);
> (d) all extensions, renewals, continuations, continuations-in-part, divisional applications, and reissues of any patent or patent application included in the Assigned IP."

The phrase "full title guarantee" (English law) or equivalent is important — it triggers implied covenants of ownership and no encumbrances.

### 4. Future IP (if applicable)
> "The Assignor hereby assigns to the Assignee all Intellectual Property Rights in and to any works or inventions:
> (a) created by the Assignor in the course of performing services for the Assignee between [start date] and [end date]; or
> (b) derived from, based upon, or incorporating any part of the Assigned IP;
> automatically and without further action on the part of the Assignor upon creation."

### 5. Further assurances
> "The Assignor shall, at the Assignee's reasonable request and expense, execute and deliver such further documents, instruments, and agreements, and do such further acts and things, as may be reasonably required to give full effect to the assignment of the Assigned IP under this Agreement, including registering or recording this Agreement (or any short-form assignment) with any intellectual property registry in any jurisdiction."

This clause is essential: IP registry updates require jurisdiction-specific filings signed by the assignor; this clause ensures cooperation.

### 6. Power of attorney (irrevocable)
> "The Assignor hereby appoints the Assignee as its irrevocable attorney-in-fact, with full power and authority to execute and file on the Assignor's behalf any document or instrument necessary to register, record, or perfect the Assignee's title in the Assigned IP in any jurisdiction, in the event that the Assignor fails to do so within [30] days of a request."

This PoA, coupled with interest, is irrevocable at common law — it protects the Assignee if the Assignor becomes unavailable (dissolved, departed employee, hostile).

### 7. Representations and warranties (Assignor)
> "The Assignor represents and warrants to the Assignee that:
> (a) the Assignor is the sole and exclusive legal and beneficial owner of the Assigned IP;
> (b) the Assigned IP is free from all liens, charges, encumbrances, and third-party rights;
> (c) the Assignor has not granted any license, sub-license, or right to use the Assigned IP to any third party that is still in force;
> (d) the Assigned IP does not, to the best of the Assignor's knowledge, infringe any third party's intellectual property rights;
> (e) there is no pending or threatened litigation, opposition, or other proceeding challenging the validity or ownership of the Assigned IP;
> (f) the Assigned IP has not been abandoned and all maintenance fees and renewal fees have been paid."

### 8. Indemnification
> "The Assignor shall indemnify and hold harmless the Assignee from and against any losses, claims, damages, costs, and expenses arising from or in connection with any breach of the warranties set out in Clause [X]."

Consider whether the indemnification is capped or uncapped. For IP portfolio acquisitions in M&A, indemnification typically follows the acquisition agreement's overall indemnification regime.

### 9. Moral rights (jurisdiction-sensitive)
For civil-law jurisdictions (France, Germany, Lebanon, UAE, KSA):
> "To the extent permitted by applicable law, the Assignor hereby irrevocably waives and agrees not to assert any moral rights in or to the Assigned IP in connection with the Assignee's use, reproduction, modification, distribution, or other exploitation of the Assigned IP."

For French law (where full waiver is not valid):
> "The Assignor acknowledges and agrees that the Assignee may exercise the Assignee's full economic rights in the Assigned IP without the need for the Assignor's prior consent, including the right to modify, adapt, and create derivative works. The Assignor undertakes not to exercise any moral rights in a manner that would prevent or restrict the Assignee's exploitation of the Assigned IP."

### 10. Governing law and dispute resolution
Specify governing law. For multi-jurisdiction IP portfolios, the assignment agreement's governing law determines how the contractual relationship is interpreted; each jurisdiction's registry requirements still apply for perfection.

## Jurisdictional notes — moral rights and registration

| Jurisdiction | Moral rights | Assignability | Registry for perfection |
|---|---|---|---|
| **France** | Inalienable; author's attribution + integrity rights cannot be assigned or permanently waived | Economic rights assignable; moral rights consent clause required | INPI (patents, trademarks); copyright registration optional |
| **Germany** | Inalienable; German copyright theory permits only exclusive licenses, not assignment of authorship | Economic rights: exclusive license achieves same effect; "assignment" terminology technically inaccurate under German law | DPMA (patents, trademarks) |
| **UK** | Waivable by written agreement (CDPA 1988 s.87) | Full assignment permitted; writing + signed required | IPO (patents, trademarks, designs) |
| **US** | Very limited (VARA for visual art only); work-for-hire doctrine may mean no assignment needed | Full assignment permitted; writing signed by assignor required | USPTO; copyright: Library of Congress optional but recommended within 3 months of publication |
| **UAE (onshore)** | Recognized; economic rights assignable | UAE Federal Law 38/1992 permits assignment of economic rights; writing required | Ministry of Economy (copyright); MOEIP (trademarks); UAE Patent Office (patents) |
| **KSA** | Moral rights inalienable; economic rights assignable | Arabic version required for registration | SAIP (Saudi Authority for Intellectual Property) |
| **Lebanon** | Moral rights inalienable (Law 75/1999); economic rights assignable | Writing required; bilingual recommended | Intellectual Property Directorate (MOE) |
| **DIFC / ADGM** | Waivable; English-law conventions apply | Full assignment; DIFC Courts enforce | Chosen law governs; UAE/international registry for perfection |

## Registry perfection checklist

An assignment is effective between the parties from the Effective Date. To be effective against third parties (subsequent assignees, creditors), the assignment must be **recorded at the relevant registry** in each jurisdiction where the IP is registered:

- Patents: filed with national patent office (USPTO, EUIPO, UKIPO, SAIP, UAE Patent Office).
- Trademarks: filed with trademark registry (same offices; EUIPO for EU marks).
- Copyright: optional in most jurisdictions but creates presumption of ownership.
- Domain names: transfer of registrar record via registrar's transfer procedure (ICANN registrars for .com/.net; country-code registrars for .sa, .ae, .lb, .fr).

Include in the further-assurances clause: specific obligation to cooperate in all registry filings within [30] days of the Effective Date.

## Use cases with specific notes

### M&A IP cleanup
- Conduct chain-of-title due diligence before drafting.
- Assignment should cover all IP created by founders, employees, and contractors if not previously assigned.
- Use representations and warranties in the acquisition agreement to address unknown IP (warranty that all material IP is properly owned; indemnity for breach).

### Founder-to-company assignment
- All IP created before incorporation that is related to the company's business must be covered.
- Often paired with [[draft-founders-agreement]] — the IP assignment is either incorporated into the founders' agreement or executed simultaneously.
- Consideration: typically nominal; founders receive shares in the company as consideration.

### Consultant / contractor to client
- Many consulting/services agreements have IP assignment clauses; if not, or if the scope is unclear, a standalone assignment is needed.
- Check whether the consultant used any third-party tools or open-source libraries — those may need separate licensing or cannot be assigned.
- Moral rights: consultant in a civil-law jurisdiction may retain moral rights; address explicitly.

## Common mistakes

1. **Vague IP description** — "all IP created in connection with the project" is litigated routinely; enumerate works in Schedule A.
2. **No power of attorney** — when the Assignor becomes unavailable (dissolved entity, departed employee), the Assignee cannot update registries without the PoA.
3. **No further-assurances clause** — the Assignee may need to file local assignments at dozens of registries; without this clause, the Assignor has no obligation to cooperate.
4. **Missing past-infringement rights** — the assignment should explicitly include "the right to sue for past infringement"; otherwise the Assignee may not be able to sue for infringements occurring before the Effective Date.
5. **Moral rights not addressed** — in civil-law jurisdictions, a blanket "IP assigned" clause without a moral rights provision leaves moral rights with the author, potentially creating constraints on Assignee's use.
6. **Domain names omitted** — domain names are often overlooked; they are not IP in the traditional sense but are essential for brand; include in Schedule A and trigger registrar transfer.

## Related skills

- [[draft-copyright-assignment]] — narrower assignment limited to copyright works only
- [[draft-consulting-agreement]] — services agreement that should include an IP assignment clause for deliverables
- [[draft-founders-agreement]] — founders' agreement with IP assignment provisions for pre-incorporation work
- [[draft-share-purchase-agreement]] — M&A transaction where IP forms part of the acquired assets
- [[review-ip-ownership]] — due diligence review of IP ownership chain before drafting
