# Question 3 — is there an Art 28 contract, and does it cover this flow

Applies only where question 2 produced "processor". For an independent controller there is no Art 28 contract to find, and demanding one is a category error. For joint controllers the instrument is an Art 26(1) arrangement, not a DPA.

Basis: Art 28 GDPR. Art 28(9): the contract must be in writing, including in electronic form. Art 28(7) allows the Commission to adopt standard contractual clauses for the controller-processor relationship; it did so in **Commission Implementing Decision (EU) 2021/915 of 4 June 2021** — a different instrument from the transfer SCCs in Decision (EU) 2021/914. Guidance: EDPB Guidelines 07/2020 v2.0 (07.07.2021), which state that the contract must do more than restate the wording of Art 28 and must contain concrete detail on how each obligation is met.

Status as at 2026-08-05.

## Is it in force at all

Three failure modes, in descending frequency:

1. **Published but never accepted.** The vendor hosts a DPA and requires the customer to accept it in the dashboard or return a signed copy. Nobody did. There is then no Art 28 contract and the processing has no lawful processor arrangement. This is a blocking finding.
2. **Incorporated by reference.** The master terms say the DPA "forms part of this agreement" or "applies where the customer is subject to the GDPR". This satisfies Art 28(9) if the reference is unambiguous and the referenced text is identified. Record the clause number of the incorporating sentence, not just the DPA URL.
3. **Signed against the wrong entity.** The DPA names one group company; the invoice names another. Art 28 binds the entity that processes. Reconcile the two, and record the discrepancy if it cannot be reconciled.

Also record the **amendment mechanism**. A clause permitting the vendor to change the DPA unilaterally on notice is common; it is not automatically invalid, but it means your evidence is a moving target. Archive a dated copy (PDF or `curl` output) at the moment of approval. A URL is not evidence of what the terms said when you signed.

## Art 28(3) content check

The contract must set out the subject matter, duration, nature and purpose of the processing, the type of personal data, the categories of data subjects, and the obligations and rights of the controller. Then, the eight lettered undertakings:

| Art 28(3) | Requirement | What to verify in the vendor's text |
|---|---|---|
| (a) | Processes only on documented instructions, including as regards transfers to a third country, unless required by Union or Member State law — then it informs the controller before processing unless that law prohibits it | Is there a carve-out permitting the vendor's own purposes? A carve-out contradicts (a) and re-opens question 2 |
| (b) | Persons authorised to process are bound by confidentiality or a statutory obligation | Usually present; check that it extends to sub-processor staff |
| (c) | Takes all Art 32 measures | Are the measures described, or only promised? EDPB Guidelines 07/2020 require concrete detail, typically a security annex |
| (d) | Respects Art 28(2) and (4) on engaging another processor | See the sub-processor section below |
| (e) | Assists the controller with appropriate technical and organisational measures for responding to data-subject requests under Chapter III | Is there an actual mechanism (API, export, deletion endpoint), or only a promise to "reasonably assist" for a fee? |
| (f) | Assists the controller in ensuring compliance with Arts 32 to 36 — security, breach notification, DPIA, prior consultation | Check the breach notification deadline; Art 33(2) says "without undue delay", so a contractual "within 72 hours of confirmation" is a weakening |
| (g) | At the controller's choice, deletes or returns all personal data at the end of the services and deletes existing copies, unless Union or Member State law requires storage | Is the choice actually yours, or does the vendor pick deletion? Is there a backup-expiry window, and how long? |
| (h) | Makes available all information necessary to demonstrate compliance with Art 28 and allows for and contributes to audits, including inspections, by the controller or a mandated auditor. Second sentence: immediately informs the controller if an instruction infringes the GDPR | See audit rights below |

A clause-by-clause map with the vendor's numbering is the deliverable. "The DPA covers Art 28" is not an assessment.

## What a DPA that is merely a web page is worth

It is worth exactly what the master terms make it worth.

- If the master terms incorporate it by reference and you accepted the master terms, it is a contract in electronic form and satisfies Art 28(9).
- If it is linked from a trust-centre page with no incorporating clause, it is marketing.
- Either way it fails as **evidence** unless archived. Under Art 5(2) you must be able to demonstrate compliance; a page the counterparty can rewrite is not a demonstration.

Practical rule: archive the DPA text, the sub-processor list and the security annex on the day of approval, with the retrieval date and the vendor's own "last updated" date recorded in the assessment.

## Sub-processors — Art 28(2) and Art 28(4)

Art 28(2): the processor must not engage another processor without prior **specific or general written authorisation**. Under a general authorisation, it must inform the controller of intended changes concerning the addition or replacement of sub-processors, **thereby giving the controller the opportunity to object**.

Art 28(4): the same data protection obligations set out in your contract must be imposed on the sub-processor by contract, and the initial processor **remains fully liable** to you for the sub-processor's performance. This is the chain that makes "our sub-processor's sub-processor" your problem in substance, even though your counterparty stays the same.

Verify, and record the answers:

- Which authorisation model applies — specific (a fixed list, changes need consent) or general (a list plus notice)?
- How is a change notified: e-mail to a named address, RSS, a page you must poll? A page you must poll does not "inform" you and is a deviation from Art 28(2).
- How many days' notice before the new sub-processor is used?
- What is the consequence of an objection? Almost always: the vendor may proceed and you may terminate. That is a commercial answer, not an unlawful one — but record whether termination is realistic for this integration, because an objection right you cannot exercise is not a safeguard in practice.
- Does the list state, per sub-processor, the **purpose** and the **location**? Location is what feeds question 4.
- Is anyone internally subscribed to the notifications, with a named owner? An unread notification defeats the whole clause.

## Audit rights — Art 28(3)(h)

The statutory right is to information plus audits **including inspections**. Most vendor DPAs narrow this to: an annual third-party report (SOC 2 Type II, ISO 27001 certificate), a questionnaire, on-site inspection only on cause, at your cost, under NDA, once per year, with notice.

That narrowing is standard and generally accepted in practice for large providers. What matters for the assessment:

- Record the narrowing as a **deviation**, with the clause reference. Do not record it as compliance.
- Confirm the substitute artefact actually exists and is current: request the SOC 2 report and check its period end date and the scope of systems covered. A report whose scope excludes the product you use is not a substitute.
- Confirm the right survives for sub-processors — Art 28(4) requires the same obligations down the chain, which in practice means the vendor must be able to obtain the evidence from its own suppliers.

## Assessment output

```
Art 28 assessment — [[VENDOR]] / [[contracting entity]]
DPA in force:       [[yes/no]] via [[incorporation by reference, clause § … | signed on [[date]]]]
DPA URL + version:  [[url]], vendor "last updated" [[date]], archived copy [[path]]
Art 28(7) SCCs:     [[uses Decision (EU) 2021/915 | bespoke text]]
Art 28(3) map:      (a) § …  (b) § …  (c) § …  (d) § …  (e) § …  (f) § …  (g) § …  (h) § …
Gaps:               [[lettered items not covered, or covered only by restatement]]
Reserved uses:      [[clause + effect on question 2]]
Sub-processors:     [[general/specific]] authorisation, [[n]] days' notice via [[channel]], objection → [[effect]]
Sub-processor list: [[url]], retrieved [[date]], notification owner [[name]]
Audit:              [[statutory | narrowed to …]] — deviation recorded
Breach notice:      [[contractual wording]] vs Art 33(2) "without undue delay"
Deletion:           [[controller's choice? backup window?]]
Verified on:        [[date]]
```

## Checkpoints

- [ ] Acceptance mechanism established: incorporated by reference, or signed, with a date
- [ ] Contracting entity on the DPA matches the entity on the invoice
- [ ] DPA text, security annex and sub-processor list archived with a retrieval date
- [ ] All eight Art 28(3) letters mapped to clause numbers, gaps named
- [ ] Instruction-only clause checked against reserved-use clauses elsewhere in the terms
- [ ] Breach notification wording compared against Art 33(2)
- [ ] Deletion/return: the choice is the controller's, and the backup expiry window is stated
- [ ] Sub-processor authorisation model, notice channel, notice period and objection consequence recorded
- [ ] A named person is subscribed to sub-processor change notifications
- [ ] Audit narrowing recorded as a deviation, substitute report obtained and its scope checked
- [ ] Unilateral amendment clause noted, with an archived dated copy as the countermeasure
