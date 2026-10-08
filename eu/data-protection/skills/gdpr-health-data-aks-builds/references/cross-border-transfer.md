# GDPR Cross-Border Transfer Workflow

A working reference for transferring personal data — including health data — out of the EEA under GDPR Chapter V. Covers Standard Contractual Clauses (SCCs), Transfer Impact Assessments (TIAs), supplementary measures, and the post-Schrems II framework. Verify the current text of GDPR Chapter V, the European Commission's current adequacy decisions, the SCC implementing decisions, and the most recent EDPB Recommendations on supplementary measures. Consult DPO and counsel for binding determinations.

## When Chapter V Applies

GDPR Chapter V (Articles 44-50) governs transfers of personal data to a **third country** (outside the EEA — which is the EU plus Iceland, Liechtenstein, and Norway) or to an **international organisation**. A "transfer" includes:

- Sending data to a third-country recipient
- Allowing a third-country entity to access EEA-hosted data
- Routing through third-country infrastructure (in some interpretations)

Verify the EDPB's "Guidelines on the concept of transfer" for the current scope.

## The Transfer Mechanisms — In Order of Preference

### 1. Adequacy Decision (Art. 45)
The European Commission may decide that a third country, territory, or specified sector ensures an adequate level of protection. Transfers to adequate countries do not require additional authorization.

**Current adequacy decisions (verify against the European Commission's current list)**: Andorra, Argentina, Canada (commercial organizations under PIPEDA), Faroe Islands, Guernsey, Israel, Isle of Man, Japan (private-sector), Jersey, New Zealand, Republic of Korea, Switzerland, United Kingdom, Uruguay, and the **EU-US Data Privacy Framework (DPF)** for certified US organizations.

The EU-US DPF (adopted in 2023) replaced Privacy Shield (invalidated by Schrems II). Verify current status — the DPF has been subject to litigation, and any successor decision should be checked at the time of transfer. For US recipients, certify under the DPF where eligible; otherwise rely on SCCs + TIA.

### 2. Standard Contractual Clauses (Art. 46(2)(c)) — SCCs 2021/914
The Commission's 2021 modular SCCs (implementing Decision (EU) 2021/914) are the most common mechanism for transfers to non-adequate countries. Four modules cover:

- **Module 1**: Controller-to-controller
- **Module 2**: Controller-to-processor
- **Module 3**: Processor-to-processor
- **Module 4**: Processor-to-controller

The 2021 SCCs replaced the 2010 / 2004 versions. Old SCCs are no longer permitted for new transfers; verify the current Commission status.

The SCCs require:
- Signing by both data exporter and data importer
- Selection of the appropriate module
- Annexes describing the parties, the transfer, technical and organizational measures, list of sub-processors
- Adherence to the data subject rights and onward-transfer obligations

### 3. Binding Corporate Rules (Art. 47)
Internal rules approved by the lead supervisory authority for transfers within a corporate group. High-effort, multi-year approval process; useful for global enterprises.

### 4. Codes of Conduct / Certification (Art. 46(2)(e)/(f))
Emerging mechanisms; verify current approved codes and certifications.

### 5. Derogations for Specific Situations (Art. 49)
Limited and exceptional — explicit consent of the data subject, contract necessity, important reasons of public interest (e.g., public health), legal claims, vital interests, transfer from a public register, occasional and not repetitive transfers based on compelling legitimate interests. **Not for systematic transfers.** EDPB has been clear that derogations are last-resort and narrow.

## The Schrems II Framework

The CJEU's Schrems II judgment (C-311/18, July 2020) invalidated the EU-US Privacy Shield and clarified that SCCs alone may not be sufficient — the data exporter must:

1. **Identify the transfer** (purpose, data, recipient, country, mechanism)
2. **Identify the transfer tool** (SCCs, BCRs, etc.)
3. **Assess the law and practice of the third country** — does it provide essentially equivalent protection? (the **Transfer Impact Assessment** or TIA)
4. **Identify supplementary measures** if the law/practice falls short
5. **Take procedural steps** to formalize the supplementary measures (e.g., amend the SCCs annexes, contract-level commitments)
6. **Re-evaluate at appropriate intervals**

The EDPB issued **Recommendations 01/2020 on measures that supplement transfer tools** (verify current version, including any updates following the EU-US DPF) — this is the playbook for TIAs and supplementary measures.

## Transfer Impact Assessment (TIA) Components

A defensible TIA covers:

| Component | What to document |
|---|---|
| Description of the transfer | Categories of data, data subjects, purposes, frequency, volume, transfer mechanism |
| Country assessment | The third country's surveillance laws (signals intelligence, law enforcement access), judicial redress, data subject rights, recent case law |
| Importer assessment | Whether the importer is subject to surveillance laws (e.g., US FISA 702 for "electronic communications service providers"), historical government requests, transparency reports |
| Risk analysis | Realistic likelihood of access requests; data sensitivity (health data is high) |
| Supplementary measures | Technical (encryption with keys held in EEA, pseudonymization, split processing), contractual (notification of requests, challenge obligations, transparency), organizational (governance, training, audit) |
| Residual risk and decision | Proceed / proceed with conditions / do not proceed |
| Review cadence | Typically annual or on material change |

## Supplementary Measures

The EDPB Recommendations classify supplementary measures as:

### Technical
- **Encryption at rest with keys held exclusively in the EEA** — the importer cannot decrypt
- **Encryption in transit** to a level resistant to third-country surveillance
- **Pseudonymization with re-identification key in the EEA**
- **Split or multi-party processing** — no single recipient sees identifying data
- **Confidential computing** — TEE / SGX / SEV-SNP isolating the processing

### Contractual
- Importer's commitment to notify the exporter of any access request (where law permits)
- Importer's commitment to challenge legally unfounded requests
- Importer's transparency reporting
- Exporter's right to suspend transfers
- Audit rights

### Organisational
- Internal policies on government access requests
- Training
- Governance and reporting

For health data, **technical measures** are typically required — contractual alone is rarely sufficient. EDPB has been explicit that contractual measures by themselves cannot prevent foreign authority access.

## Onward Transfers

When the importer further transfers the data (e.g., to its own sub-processor in yet another third country), the same Chapter V analysis applies. The SCCs require flow-down obligations. Maintain a sub-processor inventory with the transfer mechanism for each.

## Health Data Considerations

Health data is **special category** under Art. 9, which elevates the sensitivity in the TIA's risk analysis:

- Even where SCCs + TIA would suffice for ordinary personal data, health data may require stronger supplementary measures
- Member State law (Art. 9(4) derogations) may impose additional restrictions on cross-border transfer of health data (verify each Member State)
- Research transfers under Art. 89 may have additional safeguards or, in some Member States, specific authorizations from the supervisory authority

## Workflow Summary

```
1. Is the recipient in an adequate country?
   YES → Adequacy decision is the mechanism. Done.
   NO  → Continue.

2. Is the recipient certified under a relevant framework (e.g., EU-US DPF)?
   YES → DPF is an adequacy mechanism for certified entities. Verify scope.
   NO  → Continue.

3. Choose a transfer tool (SCCs 2021/914 is the most common).

4. Perform a Transfer Impact Assessment (TIA).

5. Identify and implement supplementary measures (technical preferred for health data).

6. Document the TIA, the SCCs and annexes, the supplementary measures, and the decision.

7. Re-evaluate at defined intervals or on material change (legal, technical, importer's posture).

8. If residual risk is too high after supplementary measures, do not transfer.
```

## Common Pitfalls

- Assuming a "cloud region in country X" puts the data outside Chapter V scope when the provider's law of incorporation is in a third country with surveillance laws
- Using SCCs without a TIA — Schrems II made the TIA mandatory
- Relying on contractual measures alone for health data
- Ignoring sub-processor cascades
- Letting the TIA go stale — third-country law changes; verify periodically
- Treating the EU-US DPF as Privacy Shield with a new name — the DPF has new requirements; certify formally if relying on it

## Final Disclaimers

- Verify the European Commission's current list of adequacy decisions
- Verify the current SCC modules and any amendments
- Verify the current EDPB Recommendations on supplementary measures and any updated guidance post-DPF
- Verify each relevant Member State's national derogations on cross-border transfer of health data
- Consult DPO and counsel for binding determinations
