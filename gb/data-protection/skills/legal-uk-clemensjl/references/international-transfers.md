# International transfers

Two directions, two different regimes. Data leaving the UK is governed by UK GDPR Chapter V as amended by the DUAA. Data arriving from the EEA is governed by the European Commission's adequacy decisions for the UK. Confusing the two produces notices that cite EU SCCs for a UK export, which is not a valid UK mechanism on its own.

## Data leaving the UK

UK GDPR Arts 44–49 as amended by DUAA 2025 (Part 5, in force 5 February 2026). A restricted transfer needs one of:

**Adequacy regulations** made by the Secretary of State under DPA 2018 s 17A. These cover the EEA states, Gibraltar, and the countries the EU had found adequate before the end of the transition period, carried into UK law. The DUAA replaced the old adequacy test with a "data protection test" — whether the standard of protection in the destination is not materially lower than under UK law.

**Appropriate safeguards** under Art 46. In practice for a UK exporter:

| Instrument | What it is | When to use it |
|---|---|---|
| International Data Transfer Agreement (IDTA) | The ICO's standalone UK transfer agreement | UK-only transfers where no EU SCCs exist |
| International Data Transfer Addendum to the EU SCCs (the UK Addendum) | Bolts onto executed EU Commission SCCs and adapts them to UK law | Where the same supplier relationship already runs on EU SCCs |
| Binding corporate rules | Approved by the Commissioner | Intra-group transfers at scale |

The IDTA and the Addendum are standard data protection clauses issued by the Commissioner and laid before Parliament under DPA 2018 s 119A. Both remain valid. **Dates, confirmed against the ICO's own guidance page on 05.08.2026:** the Secretary of State laid the IDTA, the Addendum and a transitional-provisions document before Parliament on **02.02.2022**, and following Parliamentary approval they **came into force on 21.03.2022**.

The version strings matter, because the ICO prescribes how they are cited when incorporated into a commercial contract:

- IDTA: *"Part 4: Mandatory Clauses of the Approved IDTA, being the template IDTA A.1.0 issued by the ICO and laid before Parliament in accordance with s119A of the Data Protection Act 2018 on 2 February 2022, as it is revised under Section 5.4 of those Mandatory Clauses."*
- Addendum: *"Part 2: Mandatory Clauses of the Approved Addendum, being the template Addendum B.1.0 issued by the ICO and laid before Parliament in accordance with s119A of the Data Protection Act 2018 on 2 February 2022, as it is revised under Section 18 of those Mandatory Clauses."*

The "as it is revised under Section 5.4 / Section 18" tail is the auto-update hook. Keep it: it is what carries a contract across the ICO's planned update without a re-signature.

**UK Extension to the EU–US Data Privacy Framework.** The Data Protection (Adequacy) (United States of America) Regulations 2023 (SI 2023/1028) came into force on 12 October 2023. A UK exporter may transfer to a US organisation only if that organisation appears on the Data Privacy Framework List **and** has certified to the UK Extension specifically. Certification to the EU–US DPF alone is not enough. Check the listing before relying on it.

**Transfer risk assessment.** Where a safeguard under Art 46 is relied on, the exporter must assess whether the protection will be undermined in the destination. The ICO publishes a TRA tool as an alternative to the EU-style transfer impact assessment. Record the assessment; it is the first thing asked for on inspection.

**Derogations** under Art 49 (explicit consent, contract necessity, legal claims) are for occasional, non-repetitive transfers. They are not a basis for routine use of an overseas SaaS provider.

## Data arriving from the EEA

The European Commission adopted adequacy decisions for the UK on 28 June 2021 under the GDPR and the Law Enforcement Directive. They were technically extended on 24 June 2025 to 27 December 2025, and renewed on 19 December 2025. The renewed decisions run to 27 December 2031, subject to review and to a sunset clause, and the Commission's assessment took the DUAA changes into account.

Practical consequence: an EEA controller may still send personal data to the UK without additional safeguards. Do not draft an EEA-facing notice around SCCs for UK transfers, and do not describe UK adequacy as expiring in 2025.

## Where the transfer rules do not apply

Chapter V bites on a transfer to a controller or processor outside the UK. It does not bite where:

- the recipient is in the UK, even if the data physically sits on a server abroad under the UK entity's sole control — though the security duty under Art 32 still applies
- the data is made available to the data subject themselves
- the recipient is a UK-established branch of an overseas group and the data goes no further

Restricted transfer analysis is about the recipient's location and control, not about where a packet travels. Support access from an overseas office to a UK-hosted database is a restricted transfer; a UK-hosted database reachable over the public internet is not.

## Common configuration to check

| Setup | What it needs |
|---|---|
| US SaaS with a UK or EU data region | Still a restricted transfer if US staff can access support data. Check the vendor's sub-processor list and access model, not the marketing page about data residency |
| Vendor offering only EU SCCs | Execute the UK Addendum on top |
| Vendor claiming DPF certification | Verify the **UK Extension** entry specifically on the Data Privacy Framework List |
| Group company in a country with no UK adequacy | IDTA or binding corporate rules, plus a transfer risk assessment |
| Analytics or advertising vendor | Usually a controller in its own right for some purposes; the transfer analysis runs alongside the PECR consent analysis, not instead of it |

## The reverse trap

A UK business that offers goods or services to people in the EEA, or monitors their behaviour, is directly subject to EU GDPR under Art 3(2) in addition to UK law. That triggers an Art 27 EU representative, an EU-facing privacy notice citing Regulation (EU) 2016/679, an EU lead supervisory authority analysis, and EU cookie law for those users. This is a parallel workstream, not a variation of the UK one, and it is out of scope for this skill beyond flagging it.

## Template

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h2>Transfers outside the United Kingdom</h2>
<p>
  Some of the providers we use process personal data outside the UK. Where that happens we rely on
  one of the following:
</p>
<table>
  <tr><th>Recipient</th><th>Country</th><th>Purpose</th><th>Mechanism</th></tr>
  <tr>
    <td>[[provider]]</td><td>[[country]]</td><td>[[purpose]]</td>
    <td>[[UK adequacy regulations / UK Extension to the EU–US Data Privacy Framework /
        International Data Transfer Agreement / UK Addendum to the EU SCCs]]</td>
  </tr>
</table>
<p>
  You can request a copy of the safeguards we rely on by writing to
  <a href="mailto:[[address]]">[[address]]</a>.
</p>
```

## Checkpoints

- [ ] Every overseas recipient identified from the actual network log and vendor list, not from memory
- [ ] Each transfer mapped to one named mechanism
- [ ] EU SCCs never relied on alone for a UK export — the UK Addendum or the IDTA is executed
- [ ] For any US recipient claimed to be under the DPF: certification to the **UK Extension** verified on the Data Privacy Framework List
- [ ] Transfer risk assessment completed and stored for every Art 46 safeguard
- [ ] Art 49 derogations not used for routine, repeated transfers
- [ ] The notice offers a route to obtain a copy of the safeguards (Art 13(1)(f))
- [ ] UK adequacy for inbound EEA data described correctly: renewed 19 December 2025, running to 27 December 2031
- [ ] EEA-facing exposure assessed; if present, EU GDPR Art 27 representative flagged as a separate obligation
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
