---
name: prompt-pack-technology-transfer-agreement-sboghossian
title: Technology Transfer Agreement
description: Use when a transferor is permanently or substantially transferring technology (patents, know-how, trade secrets, technical processes) to a transferee, with delivery of technical documentation, training, ongoing support, and performance milestones. Distinct from a technology license (temporary use right) — a technology transfer involves the permanent or deep transfer of the technology itself. MENA-specific guidance covers UAE patent assignment mechanics, SAIP registration in KSA, export control compliance, and MENA government approval requirements for technology transfers.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-technology-transfer-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Technology Transfer Agreement

## When to use this

Use this skill when:
- A company (Transferor) is selling or permanently transferring ownership of a technology (including patents, know-how, technical processes, trade secrets, and related IP) to another company (Transferee).
- A company is being acquired and the technology transfer is part of the asset sale (as distinct from a share purchase — see [[prompt-pack-share-purchase-agreement]]).
- A government-funded technology development project requires the results to be transferred to a private commercialization entity.
- A company is spinning out a business unit and transferring the underlying technology to the new entity.
- A joint venture is dissolving and the technology it has developed needs to be allocated between the parties.

**Key distinction from technology licensing:** A technology license grants temporary use rights; the licensor retains ownership. A technology transfer (assignment) permanently transfers ownership (or transfers substantially all economic rights) to the transferee. The transferor will typically have no ongoing rights to use the technology unless a license-back is granted.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Transferor and transferee identities** | Determines IP assignment formalities; export control requirements | Ask |
| **Technology description** | What is being transferred — patents, know-how, software source code, technical documents, formulas | Ask; attach a detailed Schedule |
| **Transfer price / consideration** | Fixed lump sum; installments; royalty-on-future-revenue model (hybrid) | Ask |
| **Jurisdiction(s) of IP registration** | Patent assignments must be registered in each jurisdiction where the patent is registered; governs formal requirements | Ask |
| **Governing law** | Determines requirements for a valid assignment of IP | Ask |

## Optional inputs

- **License-back** — whether the Transferor retains a license to use the technology after transfer (e.g., in fields of use it currently operates in).
- **Training and technical support** — the Transferor's obligation to assist the Transferee in implementing the technology; critical for know-how transfers.
- **Performance milestones** — conditions or obligations on the Transferee (e.g., commercial use within 3 years, minimum production levels) tied to payment terms or reversionary rights.
- **Export control compliance** — if the technology is subject to US EAR, ITAR, EU dual-use, or KSA/UAE export controls.
- **Non-compete** — whether the Transferor agrees not to develop or deploy the same technology in competition with the Transferee for a defined period.

## Document structure

1. **Definitions**
   - **Technology:** all patents (listed in Schedule A), know-how, trade secrets, technical documentation, designs, formulas, processes, data, and any other IP comprising or necessary to practice [describe the technology].
   - **Know-how:** unpatented technical knowledge, experience, methods, and data necessary to practice the Technology.
   - **Background Technology:** IP owned by the Transferor that is not being transferred but may be necessary to use the transferred Technology; subject to a license-back if required.
   - **Improvements:** modifications or enhancements to the Technology created by either party.
   - **Effective Date:** date of transfer completion or, if staggered, defined per tranche.

2. **Assignment and transfer of technology**
   - **IP assignment:** Transferor hereby assigns and transfers to Transferee, with effect from the Effective Date, all right, title, and interest in and to the Technology, including:
     - All patents and patent applications listed in Schedule A (in all jurisdictions).
     - All know-how and trade secrets comprising the Technology.
     - All technical documentation, manuals, designs, drawings, and data embodying the Technology.
     - The right to apply for patent protection in any jurisdiction for inventions embodied in the Technology.
     - All existing licenses and sublicenses granted by Transferor in relation to the Technology (or state "Transferor will novate/terminate existing licenses as agreed").
   - **Form of assignment:** assignment of patents requires formal written instruments in each jurisdiction; the main Agreement is supplemented by jurisdiction-specific IP assignment deeds (see Schedule B for short-form assignments for registration).
   - **Title warranty:** Transferor represents that it is the sole owner of the Technology free and clear of all liens, encumbrances, and third-party rights.

3. **Know-how and technical documentation transfer**
   - Within [30/60] days of the Effective Date, Transferor will deliver to Transferee:
     - Complete technical documentation and specifications.
     - All source code, design files, and prototypes.
     - All test data, experimental results, and validation records.
     - A list of key technical personnel with expertise in the Technology.
   - **Know-how transfer plan:** agree a detailed schedule (Schedule C) specifying what will be delivered, when, and in what format.
   - **Verification:** Transferee has [30] days after delivery to verify completeness; disputes about completeness escalate to technical experts.

4. **Training and technical support**
   - **Initial training:** Transferor provides [X weeks/months] of training to Transferee's engineers and technical personnel.
   - **On-site assistance:** Transferor provides [X days] of on-site technical assistance to help Transferee implement the Technology in its facilities.
   - **Remote support:** Transferor provides [X hours/months] of remote technical support post-training.
   - **Documentation:** Transferor will update documentation based on questions arising during training.
   - **Knowledge transfer completeness:** both parties sign a "Knowledge Transfer Completion Certificate" confirming that the know-how has been successfully transmitted (this is the Transferee's acknowledgment and limits the Transferor's post-transfer support obligation).

5. **Consideration and payment**
   - **Lump sum:** [amount] payable [on execution / in installments per Schedule D].
   - **Milestone payments:** tied to: (a) delivery of technical documentation; (b) completion of training; (c) Transferee's successful implementation (first production run); (d) first commercial sale.
   - **Royalty tail:** in addition to upfront payment, [X%] of net revenue from sales of products incorporating the Technology, for [Y years] from first commercial sale.
   - **Consideration for know-how vs. patents:** consider separate valuations for patent-protected elements (value may decrease if patents expire) vs. know-how (value is ongoing if secrecy maintained).
   - **Tax:** clarify whether payments are inclusive or exclusive of VAT; address withholding tax on royalty components.

6. **Performance milestones and reversionary rights**
   - If the Transferee fails to commercialize the Technology within [X years], the Transferor may:
     - Require the Transferee to license the Technology back to the Transferor.
     - Or: reclaim ownership of specific patents if they have not been worked by the Transferee.
   - These provisions are not standard in all transfers; include where the Transferor has concerns about the Transferee's commercialization capability or where a government grant condition requires technology utilization.

7. **License-back to Transferor**
   - If the Transferor needs to continue using aspects of the Technology (e.g., in different products or markets), include a license-back:
     - Scope: non-exclusive license for the Transferor to use the Technology in [specified field / existing products].
     - Royalty: [royalty-free / agreed royalty].
     - Duration: perpetual or [X years].

8. **Background technology license**
   - If the Transferee needs access to Background Technology (IP retained by the Transferor but necessary to use the transferred Technology):
     - Licensor grants Transferee a non-exclusive license to use Background Technology solely as necessary to use the transferred Technology.
     - The Background Technology license is strictly limited to the stated purpose and terminates if the Transferee no longer uses the transferred Technology.

9. **IP registration and recordal**
   - Transferor must execute and deliver all documents necessary to record the assignment of patents in each jurisdiction.
   - Costs: Transferee bears the costs of patent assignment recordal.
   - Timeline: Transferor must sign and deliver jurisdiction-specific assignment documents within [15] business days of Transferee's request.
   - Cooperation: Transferor cooperates with patent prosecution for any pending applications being transferred; signs all necessary papers.

10. **Representations and warranties (Transferor)**
    - Sole owner of the Technology; no joint owners.
    - No liens, licenses, or encumbrances affecting the Technology (except disclosed licenses).
    - No pending or threatened IP infringement claims affecting the Technology.
    - Patents are valid and subsisting to the Transferor's knowledge.
    - Know-how has not been disclosed to any third party except under confidentiality obligations.
    - Technology does not infringe any third party's IP rights to the Transferor's knowledge.
    - No government funding restrictions apply to the transfer (see Jurisdictional notes on Bayh-Dole / government grant conditions).

11. **Post-transfer obligations**
    - Transferor must not use the transferred Technology after the Effective Date except under any license-back.
    - Transferor must promptly refer to Transferee any inquiries or communications received from third parties about the Technology.
    - Non-compete: [if agreed] Transferor agrees not to develop or commercialize any technology substantially similar to the transferred Technology in [territory/field] for [X years].

12. **Export control compliance**
    - If the Technology is subject to export controls (US EAR/ITAR; EU dual-use Regulation; UAE Strategic Goods and Materials Regulation):
      - Transferor must identify any export control restrictions applicable to the Technology.
      - Transferee must obtain any required export licenses or authorizations.
      - The transfer is conditioned on obtaining required export approvals.
      - Neither party may transfer the Technology to any restricted country or entity.

13. **Confidentiality**
    - Know-how and trade secrets remain confidential even after transfer; both parties maintain confidentiality of information shared during the transfer process.
    - Transferee protects know-how with at least the same standard of care as its own trade secrets.

14. **Governing law and dispute resolution**

## Jurisdictional notes

### UAE — patent assignment
- UAE Patent Law (Federal Law No. 11 of 2021): patent assignments must be registered with the Ministry of Economy (IP Department) to be effective against third parties.
- Assignment of unregistered patents/patent applications: assignment must also be registered.
- Know-how: protected as trade secrets under UAE law; no formal registration requirement.

### KSA
- SAIP (Saudi Authority for Intellectual Property): patent assignments must be recorded with SAIP.
- Government-funded technology: if the technology was developed with Saudi government funding (KACST, KAUST, or research grants), check whether the funding terms require Saudi government approval or a first right of use before the technology is exported.
- WHT: 15% withholding tax on the purchase price attributed to know-how / royalties paid to non-resident transferors; obtain tax advice.

### Lebanon / Egypt
- Patent assignments must be registered with the national patent office (OAPEC for Arab region patents; national IP offices).
- MENA states are generally members of ARIPO-equivalent regional IP cooperation frameworks; verify applicable regional patent protection.

### Export control (US technology)
- US EAR: technology controlled under the Export Administration Regulations requires an export license for certain destinations and end uses; MENA transfers of US-origin technology require EAR compliance analysis.
- ITAR: military and dual-use technology may require US State Department authorization.

### EU
- EU technology transfers must comply with the Technology Transfer Block Exemption Regulation (TTBER) for competition law purposes.

## Drafting standards

- The technology description (Schedule A for patents; Schedule B for know-how) is the most important document in the transaction; inadequate description of what is being transferred is the most common cause of post-transfer disputes.
- A Know-how Transfer Completion Certificate is strongly recommended; it creates a clear record that the know-how transfer was completed and accepted.
- Patent assignment deeds should be prepared for each jurisdiction where the patent is registered, each in the required local form (may require local language, local notarization, local counsel).
- For government-funded technology: investigate conditions attached to research grants before drafting; the government may retain a license or may impose use-it-or-lose-it conditions that survive the transfer.

## Common mistakes

- **Incomplete patent list.** Missing patents from Schedule A means they are not transferred; the Transferor retains them; causes disputes post-closing.
- **Know-how transfer not structured.** "Transfer of all know-how related to the Technology" without a delivery plan or completion certificate leaves the Transferee with uncertain rights.
- **No export control analysis.** Failing to identify export-controlled technology before agreeing the transfer can result in an illegal transfer and regulatory violations.
- **Non-compete not included.** Without a non-compete, the Transferor may redevelop the same technology and compete directly with the Transferee.

## Related skills

- [[prompt-pack-technology-licensing-agreement]]
- [[prompt-pack-software-license-agreement]]
- [[prompt-pack-research-collaboration-agreement]]
- [[prompt-pack-standard-nda]]
- [[heuristic-always-state-jurisdiction-first]]
