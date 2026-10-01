# Question 2 — processor, independent controller, or joint controller

The role is decided per **data flow**, not per company, and it is decided by the facts, not by the label in the contract. Art 4(7) GDPR: the controller determines the purposes and means. Art 4(8): the processor processes on behalf of the controller. Art 28(10): a processor that determines purposes and means of a processing "shall be considered a controller in respect of that processing". Art 26(1): where two or more controllers jointly determine purposes and means, they are joint controllers and must have an arrangement.

Authoritative guidance: EDPB Guidelines 07/2020 on the concepts of controller and processor in the GDPR, Version 2.0, adopted 07.07.2021.

Status as at 2026-08-05.

## The test

Ask in this order, for one flow at a time:

1. **Who decided that this processing would happen at all, and why?** The party that decides the *why* is a controller. Deciding the *how* alone (which encryption, which datacentre, which retention default within a range) does not make a controller — EDPB Guidelines 07/2020 call these "non-essential means" and permit the processor to decide them.
2. **Does the vendor process the data for any purpose of its own?** Product improvement, benchmarking, model training, fraud scoring across its whole customer base, ad measurement, "aggregated insights". If yes, it is a controller **for that purpose**, whatever the DPA says. Art 28(10).
3. **Did both parties jointly determine purposes and means, or does one party's participation only make sense because of the other's purpose?** Then joint controllership under Art 26. Joint does not mean equal: CJEU 29.07.2019, C-40/17 Fashion ID makes clear the responsibility is limited to the operations for which each party actually co-determines purposes and means.
4. **Does the vendor need the data to meet its own legal obligations?** AML, sanctions screening, tax, payment-scheme rules. A legal obligation that binds the vendor directly cannot be performed "on instructions" — it makes the vendor an independent controller for that slice.

A single vendor commonly produces two or three answers. Record each separately; each gets its own contract basis and its own notice sentence.

## Consequences of each answer

| Role | Contract needed | Legal basis | Notice treatment | Records |
|---|---|---|---|---|
| Processor | Art 28(3) DPA | Yours; the processor has none of its own | Named as a recipient / category of recipient (Art 13(1)(e)) | Your ROPA (Art 30(1)); the processor keeps its own under Art 30(2) |
| Independent controller | Data-sharing terms; **no** Art 28 DPA for that flow | Each party needs its own Art 6 basis for its own purpose | Disclosure to a separate controller must be disclosed, with the purpose | Your ROPA records the disclosure; theirs records the receipt |
| Joint controllers | Art 26(1) arrangement, essence made available to data subjects (Art 26(2)) | Both need a basis for the jointly determined operations | Essence of the arrangement must be available; data subjects may exercise rights against either (Art 26(3)) | Both record it |

## Cases that break the naive answer

### Analytics vendors that reserve their own use rights

The DPA says "processor". The main terms say the vendor may use "Service Data" or "Usage Data" to improve, develop and secure its services, or to produce aggregated statistics. Read both documents. Where the reserved use goes beyond what is strictly necessary to deliver the contracted service, the vendor is a controller for it, and your Art 28(3)(a) instruction-only clause is contradicted by the same contract. Findings to record: the exact clause reference, and whether the reserved use can be switched off.

### Ad platforms and social plugins — joint controllership

CJEU 29.07.2019, **C-40/17 Fashion ID GmbH & Co. KG v Verbraucherzentrale NRW**: the operator of a website that embeds a social plugin causing the visitor's personal data to be transmitted to the plugin provider is a joint controller — but only for the operations for which it actually determines purposes and means, namely the **collection** of the data and its **disclosure by transmission**. It is not responsible for the plugin provider's subsequent processing. The consequence the case is usually quoted for: the site operator, not the platform, must obtain the consent and provide the Art 13 information *before* the plugin loads.

Earlier in the same line: CJEU 05.06.2018, **C-210/16 Wirtschaftsakademie Schleswig-Holstein** — the administrator of a Facebook fan page is a joint controller with Meta for the visitor statistics, even though it receives only anonymised statistics and has no access to the underlying data.

Applied to the Meta pixel, Conversions API, TikTok pixel, LinkedIn Insight Tag and Google Ads remarketing tags: the collection-and-transmission phase is yours. A platform's "controller terms" or "business tools terms" typically allocate exactly this split; read them and record the clause. Where the platform offers a joint-controller addendum, the Art 26(2) essence must reach the data subject — a link buried in the platform's own policy is not you making it available.

### Payment providers — split roles

A payment service provider is normally a **processor** for executing the payment you instructed, and an **independent controller** for fraud prevention, chargeback handling, sanctions screening, AML and its own regulatory reporting, because those duties bind it directly. The practical consequences:

- Card and payment data flowing to the PSP is not covered by your Art 28 DPA for the fraud-prevention purpose.
- Your notice must name the PSP as a **separate controller** for that purpose, with its own privacy policy linked — not merely as a processor.
- The PSP's fraud tooling frequently runs a script in the user's browser that fingerprints the device. That is an Art 5(3) event and needs its own analysis (see `device-access.md`), even though fraud prevention is otherwise a strong legitimate interest.

### CDN, WAF and DNS providers

Processor for delivering your content and for filtering traffic on your instruction. Two carve-outs to check: (a) threat-intelligence and bot-reputation features that feed observed traffic into a cross-customer dataset — an own purpose; (b) any feature that terminates TLS and inspects request bodies, which expands the data categories far beyond "IP and URL". Record whether such features are enabled in your configuration, not whether they exist in the product.

### Hosting, IaaS and PaaS

Processor. The complication is not the role but the **scope**: the provider is a processor for the customer content you place there, and a controller for its own account, billing, security-log and abuse data. That controller slice is normally uncontroversial but still belongs in the notice as a disclosure.

### Support desks, chat widgets and CRMs

Processor for the ticket contents. Check whether the vendor uses conversation content to train its own models or to build cross-customer benchmarks — an increasingly common clause since 2024 and the single most frequent way a support tool silently becomes a controller.

## Wrong reasons for a role finding

- "We pay them, so they are our processor." The invoice does not decide (Art 4(7)).
- "The DPA says processor." Art 28(10) overrides a label contradicted by conduct.
- "They never see the data in the clear." Wirtschaftsakademie: a party can be a joint controller without any access.
- "They are big, so they are a controller." Size is irrelevant; the purpose determination is not.
- "We only send hashed e-mails." Hashing is pseudonymisation, not anonymisation (Recital 26); the role analysis is unchanged.

## Output for the assessment

```
Role finding — [[VENDOR]], flow: [[flow name]]
Role:            [[processor | independent controller | joint controller]]
Reason:          [[which purpose, decided by whom]]
Contract basis:  [[Art 28 DPA dated … | data-sharing terms § … | Art 26 arrangement dated …]]
Reserved uses:   [[clause reference + whether it can be disabled]]
Other flows:     [[second flow with a different role, or "none identified"]]
Verified on:     [[date]] against [[URL of the clause]]
```

## Checkpoints

- [ ] Each flow assessed separately, not the vendor as a whole
- [ ] Main terms read alongside the DPA for reserved use rights
- [ ] Any "improve our services" / "aggregated insights" / "model training" clause quoted with its reference
- [ ] Payment, fraud and AML flows split out from the payment-execution flow
- [ ] Ad, pixel and social-embed integrations analysed under Art 26 with the Fashion ID limitation stated
- [ ] Where joint controllership applies, the Art 26(2) essence is actually reachable by data subjects
- [ ] Art 28(10) considered where the label and the conduct diverge
- [ ] Cross-customer threat-intelligence or benchmarking features checked in the live configuration
- [ ] Finding block completed with a verification date and a clause URL
