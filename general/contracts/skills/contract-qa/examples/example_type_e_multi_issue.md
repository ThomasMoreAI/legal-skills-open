# Worked Example — Type E: Multi-Issue Question

This example demonstrates Contract QA producing structured findings for a question that covers multiple distinct topics. The output uses subsections, one per issue, each with appropriate sub-format.

## Input

**Document:** SaaS Master Services Agreement (12-page MSA)

**Question:** "What protections do we have if the vendor goes bankrupt or stops operating?"

**Optional inputs:**
- contract_type: "MSA-SaaS"
- perspective: "our_side" (customer)
- jurisdiction: "Delaware"
- prior_context: not provided

**Relevant contract excerpts:**

> **§7.1 Source Code Escrow.** Vendor maintains source code for the Service in a third-party escrow administered by [Escrow Agent]. Customer is named as a Beneficiary under the escrow agreement. Source code shall be released to Customer upon the occurrence of any Release Condition, including Vendor's filing of a petition under any chapter of the United States Bankruptcy Code, Vendor's general assignment for the benefit of creditors, or Vendor's cessation of business operations for more than ninety (90) consecutive days.
>
> **§7.2 License Upon Release.** Upon a release of source code under Section 7.1, Customer is hereby granted a perpetual, irrevocable, non-exclusive license to use, modify, and maintain the source code solely for Customer's internal use of the Service for the same purposes for which the Service was being used immediately prior to the Release Condition.
>
> **§9.4 Termination Upon Insolvency.** Either party may terminate this Agreement immediately upon written notice if the other party (a) files a petition for bankruptcy or commences any proceeding under any bankruptcy or insolvency law; (b) is the subject of an involuntary bankruptcy proceeding that is not dismissed within sixty (60) days; (c) makes an assignment for the benefit of creditors; or (d) admits in writing its inability to pay debts as they become due.
>
> **§9.6 Effect of Termination.** Upon termination, the licenses granted hereunder shall terminate, except that the licenses set forth in Section 7.2 (Source Code Escrow License) shall survive in accordance with their terms. Customer's data shall be returned to Customer in accordance with Section 12.
>
> **§11 Bankruptcy Code Section 365(n).** All licenses granted by Vendor to Customer under this Agreement are licenses to "intellectual property" within the meaning of Section 101(35A) of the United States Bankruptcy Code. Customer's rights under this Agreement, including the licenses granted herein, shall be subject to the protections afforded under Section 365(n) of the United States Bankruptcy Code in any bankruptcy proceeding.
>
> **§12.2 Data Return.** Upon termination of this Agreement for any reason, Customer may, within thirty (30) days following termination, request that Vendor return Customer's data in a commercially reasonable format. After thirty (30) days, Vendor may destroy Customer's data without further obligation to Customer.

## Question classification

Type E — Multi-issue. The question asks broadly about a topic ("protections if vendor goes bankrupt") that has several distinct aspects: source code escrow, termination rights, IP licensing protections under Bankruptcy Code Section 365(n), and data return. Each aspect deserves its own sub-finding.

## Output

The contract has four distinct categories of bankruptcy and cessation protections, which work together to address different aspects of vendor failure. Two are strong (source code escrow with a perpetual license; explicit Section 365(n) language); one is standard (termination rights); one is weak and worth flagging (the 30-day data return window).

### Source code escrow with release on bankruptcy or cessation

**Operates as the primary continuity protection.** If the vendor files for bankruptcy, makes a general assignment for the benefit of creditors, or stops operating for 90+ days, the source code is released to you, and you receive a perpetual license to use, modify, and maintain it for your continued internal use of the service.

> "Vendor maintains source code for the Service in a third-party escrow administered by [Escrow Agent]. Customer is named as a Beneficiary under the escrow agreement. Source code shall be released to Customer upon the occurrence of any Release Condition, including Vendor's filing of a petition under any chapter of the United States Bankruptcy Code, Vendor's general assignment for the benefit of creditors, or Vendor's cessation of business operations for more than ninety (90) consecutive days."

[§7.1]

> "Upon a release of source code under Section 7.1, Customer is hereby granted a perpetual, irrevocable, non-exclusive license to use, modify, and maintain the source code solely for Customer's internal use of the Service for the same purposes for which the Service was being used immediately prior to the Release Condition."

[§7.2]

This is genuinely useful in worst-case scenarios: in a vendor bankruptcy, you have a path to continue operating without the vendor. The 90-day cessation trigger covers the "vendor still exists but has gone dark" scenario, which is more common than formal bankruptcy. Verify with your security/IT team that the escrow agent's release process actually works in practice — escrow is only as good as its execution; some escrow agreements have technical defects that prevent timely release.

### Termination rights upon insolvency

**Standard insolvency-termination clause.** You can terminate the agreement immediately on bankruptcy filing, involuntary bankruptcy proceeding not dismissed within 60 days, general assignment for creditors, or written admission of inability to pay debts.

> "Either party may terminate this Agreement immediately upon written notice if the other party (a) files a petition for bankruptcy or commences any proceeding under any bankruptcy or insolvency law; (b) is the subject of an involuntary bankruptcy proceeding that is not dismissed within sixty (60) days; (c) makes an assignment for the benefit of creditors; or (d) admits in writing its inability to pay debts as they become due."

[§9.4]

This is conventional and works as expected. Note that termination rights in the contract are subject to bankruptcy-court oversight if the vendor actually files for bankruptcy — the automatic stay (11 U.S.C. §362) typically pauses contract termination until the bankruptcy court rules. The Section 365(n) protections (next finding) address this directly.

### Bankruptcy Code Section 365(n) protections

**Explicit Section 365(n) language is present and strong.** This is the legally important protection in a vendor bankruptcy.

> "All licenses granted by Vendor to Customer under this Agreement are licenses to 'intellectual property' within the meaning of Section 101(35A) of the United States Bankruptcy Code. Customer's rights under this Agreement, including the licenses granted herein, shall be subject to the protections afforded under Section 365(n) of the United States Bankruptcy Code in any bankruptcy proceeding."

[§11]

Background: under §365(n), if a debtor (vendor in bankruptcy) rejects an executory contract that includes IP licenses, the licensee (you) can elect to retain the licenses for the term of the contract and any extensions, in exchange for continued payment of royalties. Without this election, the licensee loses the IP rights when the contract is rejected. With explicit §365(n) language in the contract, the election is unambiguously available.

This works in concert with the source code escrow: escrow gives you the *materials* you need; §365(n) gives you the *legal right* to use them. Both matter.

### Data return — flagged as weak

**Only 30 days for data return; weak protection.** Worth flagging.

> "Upon termination of this Agreement for any reason, Customer may, within thirty (30) days following termination, request that Vendor return Customer's data in a commercially reasonable format. After thirty (30) days, Vendor may destroy Customer's data without further obligation to Customer."

[§12.2]

In a bankruptcy scenario, 30 days is short. The vendor's bankruptcy typically becomes public quickly, but the practical chaos — communications breakdowns, automatic stay litigation, debtor-in-possession transitions — can easily consume 30 days before you have a clear path to request return. Missing the window means the vendor (or its bankruptcy trustee) may destroy your data with no further obligation.

The "commercially reasonable format" qualifier is also weak. In a distressed vendor scenario, "commercially reasonable" may be whatever the vendor's reduced operational capacity can produce — which may not be the format you actually need.

This is the primary weakness in the bankruptcy protection package. In a clean negotiation, this should be: 90 days minimum, format specified (typically structured export of customer data with a documented schema), and accompanied by an obligation to maintain data accessibility for the return window even if other vendor operations cease.

### How these protections work together

The four protections form a layered defense:

- **Section 7.1/7.2 (escrow)** addresses the operational continuity question (can you keep running?).
- **Section 9.4 (termination)** addresses the contractual question (can you exit?).
- **Section 11 (Section 365(n))** addresses the legal question (can you retain your rights in the bankruptcy proceeding?).
- **Section 12.2 (data return)** addresses the data question (can you get your data back?).

The layered structure is good. The weak link is data return; the others are conventional and adequate.

**Recommendation:** Negotiate §12.2 to extend the data return window to at least 90 days and specify the data format. This is typically a low-friction negotiation — vendors generally accept 60–90 days for data return as standard. The other three sections do not need negotiation.

---

## What this example demonstrates

- **Multi-issue questions get structured findings.** Four sub-issues, four subsections, each with its own quote and analysis.
- **Each subsection uses the appropriate sub-format.** The escrow subsection is mostly Type B (interpretation — how does this work). The Section 365(n) subsection is Type B with educational context (background on the bankruptcy provision). The data-return subsection is Type C (this is a weak provision relative to standard). Sub-formats are picked per sub-issue, not forced into one shape.
- **Calibration is consistent throughout.** All four findings are calibrated to the customer perspective (what protections the customer has). A vendor-side review of the same clauses would emphasize different things (e.g., the escrow obligation's cost; the data destruction right's flexibility).
- **The closing paragraph identifies how the issues interact.** This is the value-add of structured findings over independent answers — the user sees the layered defense and the weak link.
- **Recommendation is specific and proportional.** One concrete negotiation ask (§12.2), with rationale; the other three sections explicitly do not need attention. The skill does not pad recommendations to fill space.
- **Educational context is brief and routed appropriately.** The §365(n) explanation is two sentences of background, enough for the user to understand the provision's significance. A full primer on bankruptcy law would be out of scope; routing to research would be appropriate if the user wanted more.
- **The answer demonstrates that "protections" is a multi-aspect concept.** A naïve answer would have just named the escrow clause and stopped. The skill identifies all four operative provisions and explains their interlocking roles. This is the value of multi-issue handling.
