# Terms of service, arbitration, Section 230, DMCA

Status as at 2026-08-05.

US terms of service are ordinary contract law, not a statutory disclosure. Nothing requires a site to publish terms. What the terms buy is a limitation of liability, an arbitration clause, a class-action waiver, a licence to user content, and a chosen forum — and none of those are worth anything if the contract was never formed. Formation is where US terms fail, not drafting.

## Formation — clickwrap, sign-in-wrap, browsewrap

The standard is reasonable notice plus an unambiguous manifestation of assent. It is state contract law, applied federally in arbitration motions.

| Pattern | Description | Enforceability |
|---|---|---|
| Clickwrap | Separate, unchecked checkbox: "I agree to the Terms of Service" with the terms hyperlinked, next to the action button | Routinely enforced |
| Sign-in-wrap | Text near the button: "By clicking Continue you agree to our Terms" | Grey zone; enforceable only if the notice is conspicuous and clearly ties the click to assent |
| Browsewrap | Terms linked only in the footer, no notice at the point of action | Routinely unenforceable |

*Berman v. Freedom Financial Network, LLC*, No. 20-16900 (9th Cir., 5 April 2022) is the controlling design authority in the Ninth Circuit and is followed widely. It refused to compel arbitration because the sign-in-wrap notice was not reasonably conspicuous. The practical requirements it establishes:

- The notice must be **visually distinct** — readable font size and colour contrast, not grey micro-text below the button.
- The hyperlink to the terms must be **identifiable as a hyperlink**, conventionally blue and underlined; the same-colour capitalised text of the surrounding sentence is not enough.
- The notice must **explicitly state that the action constitutes assent** to the linked terms.
- Both must be **adjacent to the button** the user actually presses.

Safest configuration: an unchecked checkbox that the user must tick, with the checkbox label stating assent and linking the terms, plus retention of a record of the acceptance (user, timestamp, terms version hash). Retain every version of the terms. A modification clause reserving the right to change terms unilaterally is generally unenforceable as to existing users without notice and a further manifestation of assent.

## Arbitration and class-action waivers

- **Federal Arbitration Act, 9 U.S.C. § 1 et seq.** Arbitration agreements are enforceable on the same footing as other contracts; state-law rules singling out arbitration are preempted.
- **Class-action waivers** in consumer arbitration agreements are enforceable — *AT&T Mobility LLC v. Concepcion*, 563 U.S. 333 (2011).
- Unconscionability remains the live defence and is where clauses now fail.

**Mass arbitration is the current practical risk.** Class waivers pushed plaintiffs' firms into filing thousands of individual arbitrations, each triggering a per-case administrative fee payable by the company. Clauses drafted to defuse that — batching, bellwether procedures binding non-participating claimants, restricted discovery, limited appeal, non-neutral arbitrator selection — are themselves being struck down. *Heckman v. Live Nation Entertainment, Inc.*, No. 23-55770 (9th Cir., 28 October 2024) held Ticketmaster's mass-arbitration protocol unconscionable, singling out the binding effect of bellwether determinations on batched claimants who had no notice of and no opportunity to participate in those proceedings. Do not copy an aggressive mass-arbitration protocol from another company's terms; the copied clause can invalidate the entire arbitration agreement and put the case back in court as a class action.

Practical positions: keep a genuine opt-out window from arbitration, keep bilateral arbitration meaningfully available, avoid binding claimants to proceedings they cannot participate in, and choose a mainstream administrator with published consumer rules.

## Choice of law and forum

Enforceable in most consumer contracts, subject to fundamental-policy limits of the consumer's home state. Several state consumer statutes cannot be waived by choice of law, and some state privacy statutes apply by residence regardless of the contract. Choice of law does not defeat a state privacy law, a state wiretap statute, or the FTC Act.

## Section 230 — 47 U.S.C. § 230

Protects a provider or user of an interactive computer service from being treated as the publisher or speaker of information provided by another information content provider (§ 230(c)(1)), and protects good-faith content moderation (§ 230(c)(2)).

It does **not** protect:

- the site's own content, or content the site materially co-develops
- claims under **federal criminal law** (§ 230(e)(1))
- claims relating to **intellectual property** (§ 230(e)(2)) — copyright and trademark claims are outside Section 230; the DMCA safe harbour is the separate mechanism for those
- claims under the **ECPA and similar state laws** (§ 230(e)(4)) — this is why state wiretap claims over tracking are not dismissed on Section 230 grounds
- certain **sex-trafficking** claims and state prosecutions added by FOSTA (§ 230(e)(5))

Section 230 is an immunity from suit for third-party content, not a general internet shield, and it does nothing for the site's own privacy, advertising or contract exposure.

## DMCA § 512 safe harbour — 17 U.S.C. § 512

Any site that stores material at the direction of users — comments, uploads, listings, profile images, reviews with photos — needs this. It is cheap, mandatory for the safe harbour, and almost always missed.

Conditions:

1. **Designate an agent with the U.S. Copyright Office** (§ 512(c)(2)). Since 1 December 2016 the designation must be made electronically through the Office's online system (37 CFR § 201.38). A fee applies per the Office's general fee schedule at 37 CFR § 201.3.
2. **Renew every three years.** 37 CFR § 201.38(c)(4): "A service provider's designation will expire and become invalid three years after it is registered with the Office, unless the service provider renews such designation by either amending it to correct or update information or resubmitting it without amendment." Renewal restarts the three-year period. An expired designation means no safe harbour. Put the renewal date in a calendar with an owner.
3. **Publish the agent's contact details** on the site in a location accessible to the public (§ 512(c)(2)).
4. **Adopt and reasonably implement a repeat-infringer policy**, and inform users of it (§ 512(i)(1)(A)). "Reasonably implemented" means actually terminating repeat infringers; a policy that exists only in the terms is worse than none, because it is evidence of what was promised.
5. **Accommodate standard technical measures** (§ 512(i)(1)(B)).
6. Operate notice-and-takedown per the elements in § 512(c)(3), and the counter-notification and put-back procedure in § 512(g).

## Template — public DMCA notice block

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h2>Copyright — DMCA Notices</h2>
<p>
  [[LEGAL ENTITY NAME]] has designated the following agent to receive
  notifications of claimed copyright infringement under 17 U.S.C. § 512(c)(2):
</p>
<p>
  Designated Agent: [[NAME OR TITLE]]<br>
  Address: [[STREET ADDRESS, CITY, STATE, ZIP]]<br>
  Telephone: [[NUMBER]]<br>
  Email: [[ADDRESS]]
</p>
<p>
  A notification must include the elements required by 17 U.S.C. § 512(c)(3),
  including a physical or electronic signature, identification of the
  copyrighted work claimed to be infringed, identification of the material to
  be removed and information reasonably sufficient to locate it, your contact
  information, a statement of good-faith belief that the use is not authorized,
  and a statement, under penalty of perjury, that the information is accurate
  and that you are authorized to act on behalf of the owner.
</p>
<p>
  Counter-notifications may be submitted under 17 U.S.C. § 512(g)(3).
  We terminate the accounts of repeat infringers.
</p>
<p>Designation last renewed with the U.S. Copyright Office: [[DATE]].</p>
```

## Checkpoints

- [ ] Terms accepted through an unchecked checkbox or an equivalently conspicuous mechanism, adjacent to the action button
- [ ] Hyperlink to the terms visually identifiable as a link
- [ ] Notice text states that the action constitutes agreement
- [ ] Acceptance records retained: user, timestamp, terms version
- [ ] Every historical version of the terms archived
- [ ] Arbitration clause reviewed against *Heckman*; no bellwether provision binding non-participating claimants
- [ ] Arbitration opt-out window present and honoured
- [ ] Class-action waiver present and severability clause drafted so its failure does not void the whole agreement
- [ ] If UGC is hosted: DMCA agent registered electronically with the Copyright Office
- [ ] Registration date recorded and a renewal reminder set for under three years (37 CFR § 201.38(c)(4))
- [ ] Agent contact details published on the site
- [ ] Repeat-infringer policy written **and** actually enforced
- [ ] No claim that Section 230 covers copyright, trademark, or wiretap claims
