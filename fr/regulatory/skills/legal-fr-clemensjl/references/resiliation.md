# Résiliation en trois clics

France requires a permanent electronic cancellation functionality for consumer contracts concluded — or capable of being concluded — electronically. It is not the German Kündigungsbutton: the trigger, the wordings and the flow are different, and copying the German implementation produces a non-compliant flow with the right intentions.

## Article L215-1-1 du Code de la consommation

Status as at 2026-08-05. Version en vigueur depuis le 1er juin 2023. Created by loi n° 2022-1158 du 16 août 2022 portant mesures d'urgence pour la protection du pouvoir d'achat, article 15. Implementing text: **décret n° 2023-417 du 31 mai 2023**, creating articles D215-1 à D215-3.

Verbatim:

« Lorsqu'un contrat a été conclu par voie électronique ou a été conclu par un autre moyen et que le professionnel, au jour de la résiliation par le consommateur, offre au consommateur la possibilité de conclure des contrats par voie électronique, la résiliation est rendue possible selon cette modalité.

A cet effet, le professionnel met à la disposition du consommateur une fonctionnalité gratuite permettant d'accomplir, par voie électronique, la notification et les démarches nécessaires à la résiliation du contrat. Lorsque le consommateur notifie la résiliation du contrat, le professionnel lui confirme la réception de la notification et l'informe, sur un support durable et dans des délais raisonnables, de la date à laquelle le contrat prend fin et des effets de la résiliation.

Un décret fixe notamment les modalités techniques de nature à garantir une identification du consommateur et un accès facile, direct et permanent à la fonctionnalité mentionnée au deuxième alinéa, telles que ses modalités de présentation et d'utilisation. Il détermine les informations devant être fournies par le consommateur. »

The scope catch: the contract need not have been concluded online. If the trader offers electronic conclusion of contracts on the day the consumer cancels, electronic cancellation must be available even for a contract signed on paper or over the counter.

## Articles D215-1 à D215-3

Status as at 2026-08-05.

**D215-1** — the functionality is presented under the wording « **résilier votre contrat** » or an analogous formula free of ambiguity, in legible characters, and is **directement et facilement accessible à partir de l'interface en ligne** on which the trader allows contracts to be concluded electronically. In practice: reachable from the account area and, where the service can be subscribed to without an account, from the public interface; permanently, not buried behind a support ticket.

**D215-2** — the functionality contains fields collecting the consumer's identity, contact details (email or postal address), the contract references such as customer or contract number, the desired cancellation date, and, for electronic communications services, the telephone numbers concerned. Where a legitimate ground is required by law, a field allows the consumer to state it and the functionality indicates which supporting documents are needed, with access to a dematerialised form and a postal address.

**D215-3** — once the fields are completed, the consumer reaches « une page qui présente un récapitulatif de sa résiliation », which they can check and correct. The notification is then sent by activating a function bearing the wording « **notification de la résiliation** » or an analogous formula free of ambiguity, in legible characters.

So the mandated flow is: entry point « résilier votre contrat » → fields → summary page → « notification de la résiliation » → acknowledgement plus, on a durable medium, the end date and the effects.

## Related duty — tacit renewal

Article L215-1 obliges the trader, for contracts with tacit renewal concluded with consumers, to inform the consumer in writing of the possibility of not renewing, no earlier than three months and no later than one month before the end of the period allowing rejection of the renewal. Where the information is given late, the consumer may terminate the renewed contract at any time from the renewal date, free of charge. This duty is separate from L215-1-1 and is frequently omitted alongside it.

## Enforcement

Failure to provide the functionality is sanctioned by an administrative fine imposed by the DGCCRF. [[UNVERIFIED: the exact article of the Code de la consommation providing the administrative fine for breach of article L215-1-1 and its ceiling — confirm on Légifrance before stating an amount to the user]]

## Template — cancellation page

```html
<!-- BROUILLON – non validé juridiquement -->
<h1>Résilier votre contrat</h1>
<p>Vous pouvez résilier votre contrat en ligne, gratuitement, à tout moment.</p>

<form>
  <fieldset><legend>Vos informations</legend>
    Nom et prénom : [[champ]]<br>
    Adresse électronique ou postale : [[champ]]
  </fieldset>
  <fieldset><legend>Votre contrat</legend>
    Numéro de client ou de contrat : [[champ]]<br>
    Date de résiliation souhaitée : [[champ]]<br>
    [[services de communications électroniques : numéro(s) de téléphone concerné(s)]]
  </fieldset>
  <fieldset><legend>Motif légitime</legend>
    [[uniquement si la loi l'exige : champ de motif, justificatifs attendus,
    formulaire dématérialisé et adresse postale]]
  </fieldset>
  <button type="submit">Vérifier ma demande</button>
</form>

<!-- page suivante -->
<h2>Récapitulatif de votre résiliation</h2>
<p>[[reprise de toutes les informations saisies, avec possibilité de correction]]</p>
<button type="submit">Notification de la résiliation</button>

<!-- après envoi -->
<p>Nous avons bien reçu votre demande le [[date et heure]]. Votre contrat prendra fin
le [[date]]. Effets de la résiliation : [[effets]]. Une confirmation vous est adressée
par [[courriel / courrier]].</p>
```

## Checkpoints

- [ ] Entry point labelled « résilier votre contrat » or an unambiguous equivalent (D215-1)
- [ ] Direct, easy and permanent access from the online interface where contracts are concluded
- [ ] Available even where this consumer's contract was concluded offline, if the trader offers electronic conclusion today (L215-1-1 al. 1)
- [ ] Functionality free of charge, no login wall where the service can be subscribed without an account
- [ ] All D215-2 fields present, including the desired cancellation date
- [ ] Summary page before sending, with correction possible (D215-3)
- [ ] Confirmation control labelled « notification de la résiliation » or an unambiguous equivalent
- [ ] Acknowledgement of receipt sent, plus end date and effects on a durable medium (L215-1-1 al. 2)
- [ ] Tacit-renewal reminder implemented between three months and one month before the deadline (L215-1)
- [ ] No German « Verträge hier kündigen » wording and no two-button Kündigungsbutton flow imported
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
