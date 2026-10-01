# Internal DSG obligations

Nothing in this file goes on the website. These are the duties that must exist as records and processes, and they are the ones that carry criminal exposure. Wording from DSG Stand am 7. Juli 2025 and DSV Stand am 1. Dezember 2025. Status as at 2026-08-05.

## Register of processing activities — Art. 12 DSG, Art. 24 DSV

Art. 12 Abs. 1 DSG: controllers and processors each keep a register of their processing activities. Abs. 2 lists the minimum content for the controller: identity of the controller; purpose; description of the categories of data subjects and of the categories of personal data processed; categories of recipients; where possible the retention period or the criteria for determining it; where possible a general description of the data security measures under Art. 8; and, where data is disclosed abroad, the state and the safeguards under Art. 16 Abs. 2. Abs. 3 sets a shorter list for processors.

Art. 12 Abs. 5 DSG instructs the Federal Council to provide exemptions for undertakings with fewer than 250 employees whose processing carries a low risk. Art. 24 DSV implements it:

> Unternehmen und andere privatrechtliche Organisationen, die am 1. Januar eines Jahres weniger als 250 Mitarbeiterinnen und Mitarbeiter beschäftigen, sowie natürliche Personen sind von der Pflicht befreit, ein Verzeichnis der Bearbeitungstätigkeiten zu führen, ausser eine der folgenden Voraussetzungen ist erfüllt:
> a. Es werden besonders schützenswerte Personendaten in grossem Umfang bearbeitet.
> b. Es wird ein Profiling mit hohem Risiko durchgeführt.

Both carve-outs bite in ordinary web projects: a health or dating platform hits lit. a, a cross-site advertising stack can hit lit. b. The headcount is measured on 1 January, not on the day the question is asked. Keep the register anyway — it is the cheapest evidence that the other duties were considered.

## Data security — Art. 8 DSG, Art. 1–5 DSV

Art. 8 Abs. 1 DSG: controller and processor ensure data security appropriate to the risk through suitable technical and organisational measures. Abs. 2: the measures must make it possible to avoid breaches of data security. Abs. 3: the Federal Council issues minimum requirements — these are Art. 1–5 DSV, covering confidentiality, availability, integrity and traceability, and logging.

Art. 4 DSV requires logging for automated processing of besonders schützenswerte Personendaten at large scale or high-risk profiling, where preventive measures cannot ensure data protection. Art. 5 DSV requires a Bearbeitungsreglement for the same constellations.

Failure to comply with the Federal Council's minimum security requirements is punishable under Art. 61 lit. c DSG.

## Processors — Art. 9 DSG

Processing may be delegated by contract or by legislation if the data is processed as the controller itself may process it and no statutory or contractual duty of confidentiality prohibits the delegation (Abs. 1). The controller must satisfy itself that the processor can ensure data security (Abs. 2). Sub-processing requires the controller's prior approval (Abs. 3).

Art. 9 DSG contains no list of mandatory contract clauses comparable to Art. 28(3) GDPR. Where the GDPR also applies, use a GDPR-compliant processing agreement — it satisfies the DSG a fortiori. Delegating without meeting Art. 9 Abs. 1 and 2 is punishable under Art. 61 lit. b DSG.

## Data protection advisor — Art. 10 DSG

Voluntary for private controllers. Appointing one is worth doing where a DSFA is likely: under Art. 10 Abs. 3 in conjunction with Art. 23 Abs. 4 DSG the controller may then skip consulting the EDÖB, provided the advisor is professionally independent and free of instructions, exercises no incompatible activities, has the necessary expertise, and the controller publishes the advisor's contact details and notifies them to the EDÖB. Registration portal: dpo-reg.edoeb.admin.ch.

## Data protection impact assessment — Art. 22, 23 DSG

Art. 22 Abs. 1 DSG: the controller performs a DSFA in advance where a processing can entail a high risk to the personality or fundamental rights of the data subject. Abs. 2: the high risk arises in particular from the use of new technologies, and exists in particular for large-scale processing of besonders schützenswerte Personendaten and for systematic large-scale monitoring of public areas. Abs. 3: the DSFA describes the planned processing, evaluates the risks, and sets out the protective measures.

Abs. 4 exempts private controllers who are legally obliged to process the data. Abs. 5 permits omitting the DSFA where a certified system, product or service under Art. 13 DSG is used, or where a code of conduct under Art. 11 DSG is complied with that rests on a DSFA, provides protective measures, and has been submitted to the EDÖB.

Art. 23 DSG: if the DSFA shows residual high risk, the EDÖB must be consulted in advance; the EDÖB responds within two months, extendable by one month for complex processing. The Art. 10 advisor route avoids this.

## Breach notification — Art. 24 DSG, Art. 15 DSV

> 1 Der Verantwortliche meldet dem EDÖB so rasch als möglich eine Verletzung der Datensicherheit, die voraussichtlich zu einem hohen Risiko für die Persönlichkeit oder die Grundrechte der betroffenen Person führt.
> 2 In der Meldung nennt er mindestens die Art der Verletzung der Datensicherheit, deren Folgen und die ergriffenen oder vorgesehenen Massnahmen.
> 3 Der Auftragsbearbeiter meldet dem Verantwortlichen so rasch als möglich eine Verletzung der Datensicherheit.
> 4 Der Verantwortliche informiert die betroffene Person, wenn es zu ihrem Schutz erforderlich ist oder der EDÖB es verlangt.

Two differences from Art. 33 GDPR that get missed. First, the trigger is higher: only breaches **likely to lead to a high risk** are notifiable, whereas Art. 33 GDPR notifies unless a risk is unlikely. Second, there is **no 72-hour deadline** — the standard is "so rasch als möglich", which in practice means without culpable delay once the assessment is made. Art. 24 Abs. 6 DSG protects the notifying person: a notification made under this article may be used in criminal proceedings against them only with their consent.

Notification portal: databreach.edoeb.admin.ch. A separate cyberattack reporting duty for critical infrastructure operators exists elsewhere in federal law and is out of scope here.

## Criminal liability — Art. 60–64 DSG

This is the point generic templates get wrong. The sanctions are **criminal fines against natural persons**, mostly prosecuted only on complaint, not administrative fines against companies.

| Provision | Conduct | Sanction |
|---|---|---|
| Art. 60 Abs. 1 DSG | Intentionally giving false or incomplete information under Art. 19, 21, 25–27; intentionally failing to inform under Art. 19 Abs. 1 or 21 Abs. 1, or to supply the Art. 19 Abs. 2 particulars | Busse bis zu 250 000 Franken, auf Antrag |
| Art. 60 Abs. 2 DSG | Intentionally giving the EDÖB false information or refusing cooperation in an investigation (Art. 49 Abs. 3) | Busse bis zu 250 000 Franken |
| Art. 61 DSG | Disclosing abroad in breach of Art. 16 Abs. 1 and 2 without an Art. 17 exception; delegating to a processor without meeting Art. 9 Abs. 1 and 2; not meeting the minimum security requirements under Art. 8 Abs. 3 | Busse bis zu 250 000 Franken, auf Antrag |
| Art. 62 DSG | Breach of professional confidentiality regarding secret personal data | Busse bis zu 250 000 Franken, auf Antrag |
| Art. 63 DSG | Intentional non-compliance with an EDÖB order that carried a reference to this penalty | Busse bis zu 250 000 Franken |
| Art. 64 Abs. 2 DSG | Where a fine of at most CHF 50,000 is in play and identifying the responsible individual would require disproportionate investigation, the authority may fine the business instead (Art. 7 VStrR) | Busse bis zu 50 000 Franken against the business |

Negligence is not punishable under these provisions — each requires Vorsatz. That is not a reason to relax: the operative exposure is that a named individual, typically the person who signed off the privacy notice or the transfer, carries the risk personally.

## Checkpoints

- [ ] Register of processing activities kept, or the Art. 24 DSV exemption documented with the 1 January headcount and both carve-outs checked
- [ ] Register content matches Art. 12 Abs. 2 DSG point by point
- [ ] Technical and organisational measures documented against Art. 1–3 DSV
- [ ] Logging and Bearbeitungsreglement assessed against Art. 4 and 5 DSV
- [ ] Processor contracts in place for every recipient acting on instructions (Art. 9 DSG)
- [ ] Sub-processor approvals documented (Art. 9 Abs. 3 DSG)
- [ ] DSFA performed where Art. 22 Abs. 2 DSG is met, and filed (Art. 14 DSV)
- [ ] Residual high risk either consulted with the EDÖB or covered by the Art. 10 advisor route
- [ ] Breach response process names who assesses "high risk", who notifies, and by which channel
- [ ] Team knows that the DSG fine hits an individual, not the company
