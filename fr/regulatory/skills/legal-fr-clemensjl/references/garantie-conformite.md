# Garantie légale de conformité et vices cachés

Three regimes run in parallel and must be kept apart in the CGV: the **garantie légale de conformité** (Code de la consommation), the **garantie des vices cachés** (code civil), and any **garantie commerciale** the trader chooses to offer. A commercial guarantee never replaces the legal ones and saying so is an unfair term.

The current text comes from **ordonnance n° 2021-1247 du 29 septembre 2021**, in force in the Code de la consommation since 1 October 2021, applying to contracts concluded from 1 January 2022.

## Duration and presumption

Status as at 2026-08-05.

- **Article L217-3**: the seller answers for defects of conformity « qui apparaissent dans un délai de deux ans à compter de » delivery of the goods.
- **Article L217-7**: « Les défauts de conformité qui apparaissent dans un délai de vingt-quatre mois à compter de la délivrance du bien […] sont, sauf preuve contraire, présumés exister au moment de la délivrance. » For second-hand goods « ce délai est fixé à douze mois ».

The presumption is the operative point: for 24 months on new goods the consumer proves nothing about the origin of the defect. Reducing the guarantee below two years for new goods sold to a consumer is void.

## Remedies

- **Article L217-8**: the consumer is entitled to bringing the goods into conformity by repair or replacement or, failing that, to a price reduction or rescission of the contract, and may suspend payment.
- **Article L217-9**: the consumer chooses between repair and replacement.
- **Article L217-10**: conformity must be restored within a reasonable time not exceeding **thirty days**, and includes removal, taking back and installation of the repaired or replacement goods.
- **Article L217-12**: the seller may refuse the consumer's choice where it is impossible or entails disproportionate costs; any refusal must be reasoned in writing or on a durable medium.
- **Article L217-14**: price reduction or rescission where the seller refuses, where conformity is not restored within thirty days, or where the defect persists; immediately where the defect is grave enough to justify it. Rescission is excluded where the defect is minor.
- **Article L217-17**: on rescission, refund on receipt of the goods or proof of their return, at the latest within fourteen days, by the same means of payment and without additional cost.

## Article L217-13 — the six-month extension after repair

Status as at 2026-08-05. Verbatim:

« Tout bien réparé dans le cadre de la garantie légale de conformité bénéficie d'une extension de cette garantie de six mois.

Dès lors que le consommateur fait le choix de la réparation mais que celle-ci n'est pas mise en œuvre par le vendeur, la mise en conformité par le remplacement du bien fait courir, au bénéfice du consommateur, un nouveau délai de garantie légale de conformité attaché au bien remplacé. Cette disposition s'applique à compter du jour où le bien de remplacement est délivré au consommateur. »

Introduced by ordonnance n° 2021-1247 du 29 septembre 2021, article 9, applying to contracts concluded from 1 January 2022. This is a genuinely French rule with no counterpart in the German or Austrian implementations of directive (EU) 2019/771, and it has two operational effects: a repaired product carries a guarantee of 24 + 6 months, and a replacement after a failed repair restarts the full period. Support scripts and CGV built from a foreign template will state the wrong end date.

## Updates

Article L217-20 governs updates that are not necessary for conformity: the seller must inform the consumer clearly, sufficiently in advance and on a durable medium. For goods with digital elements the conformity duty extends to supplying the updates the consumer may reasonably expect.

## Digital content and digital services

Digital content and digital services have their own guarantee regime in the Code de la consommation, distinct from the regime for goods, including a conformity duty over the supply period for continuous supply and an update obligation. [[UNVERIFIED: the exact article range for the garantie légale de conformité applicable to contenus numériques et services numériques and the applicable presumption periods — confirm on Légifrance before quoting article numbers in a document]]

## Vices cachés

Articles 1641 to 1649 du code civil. The seller answers for hidden defects rendering the goods unfit for their intended use or so reducing that use that the buyer would not have bought them, or would have paid less. The action must be brought within **two years of discovery of the defect** (article 1648). This regime runs alongside the garantie légale de conformité and the consumer chooses; a CGV that presents the garantie légale de conformité as the only remedy is incomplete.

## Template — mandatory guarantee section in the CGV

```html
<!-- BROUILLON – non validé juridiquement -->
<h2>Garanties légales</h2>
<p><strong>Garantie légale de conformité.</strong> Le vendeur répond des défauts de
conformité qui apparaissent dans un délai de deux ans à compter de la délivrance du
bien (article L. 217-3 du code de la consommation). Les défauts qui apparaissent dans
un délai de vingt-quatre mois à compter de la délivrance sont présumés exister au
moment de la délivrance, sauf preuve contraire ; ce délai est de douze mois pour les
biens d'occasion (article L. 217-7).</p>
<p>Vous pouvez choisir entre la réparation et le remplacement du bien. La mise en
conformité intervient dans un délai qui ne peut excéder trente jours (article
L. 217-10). <strong>Tout bien réparé dans le cadre de la garantie légale de conformité
bénéficie d'une extension de cette garantie de six mois</strong> (article L. 217-13).
Si vous choisissez la réparation et que celle-ci n'est pas mise en œuvre, le
remplacement fait courir un nouveau délai de garantie légale de conformité.</p>
<p><strong>Garantie des vices cachés.</strong> Vous pouvez également invoquer la
garantie des vices cachés des articles 1641 à 1649 du code civil, dans un délai de
deux ans à compter de la découverte du vice.</p>
<p><strong>Garantie commerciale.</strong> [[description ou : nous n'offrons aucune
garantie commerciale]]. Elle s'ajoute aux garanties légales et ne les remplace pas.</p>
<p>Mise en œuvre des garanties : [[adresse postale, courriel, téléphone, procédure]].</p>
```

## Checkpoints

- [ ] Two-year period stated for new goods, twelve-month presumption for second-hand (art. L217-3, L217-7)
- [ ] The six-month extension after repair is stated explicitly (art. L217-13)
- [ ] The restart of the full period after replacement following a failed repair is stated
- [ ] Thirty-day limit for restoring conformity stated (art. L217-10)
- [ ] Refund within fourteen days on rescission (art. L217-17)
- [ ] Vices cachés mentioned alongside, with the two-year limit from discovery (C. civ. art. 1648)
- [ ] Commercial guarantee, if offered, described on a durable medium and stated not to replace the legal guarantees
- [ ] No reduction of the guarantee below two years for new goods sold to consumers
- [ ] No clause conditioning the guarantee on original packaging, registration, or use of an authorised repairer
- [ ] Support scripts and warranty end dates reflect the +6 months after repair
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
