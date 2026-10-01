# Complaints and alternative dispute resolution

This area changed on 6 April 2026. Almost every UK legal template in circulation is out of date on it, and most also carry a dead EU link.

## What is now in force

The Digital Markets, Competition and Consumers Act 2024 Part 4 Chapter 4 (ss 291–310) and Schedules 25–27 came into force on 6 April 2026 by the Digital Markets, Competition and Consumers Act 2024 (Commencement No. 3 and Transitional Provisions) Regulations 2026 (SI 2026/284, made 11 March 2026).

The Alternative Dispute Resolution for Consumer Disputes (Competent Authorities and Information) Regulations 2015 (SI 2015/542) are **revoked**. Reg 19 of that instrument — the old duty to name an ADR entity on the website and in the terms — no longer exists. Do not cite it.

Chapter 4 replaces the voluntary accreditation model with a mandatory one:

- **s 293** — prohibition on acting as an ADR provider for consumer contract disputes without accreditation or an exemption
- **s 294** — prohibition on charging consumers fees, subject to exceptions
- **s 295 and Sch 25** — exempt ADR providers, including statutory ombudsman schemes
- **ss 296–298** — accreditation, variation, revocation and suspension
- **s 301 and Sch 26** — accreditation criteria
- **s 302** — enforcement notices
- **ss 303–306** — ADR information regulations and directions
- **s 308** — duty of trader to notify the consumer of ADR arrangements
- **Sch 27** — consequential amendments, including the revocation of SI 2015/542

Accreditation functions have been conferred on the Chartered Trading Standards Institute by regulations made in 2026.

## Section 308 — the trader duty

Status as at 2026-08-05: in force since 6 April 2026.

Where a trader receives a complaint from a consumer relating to a consumer contract, the trader must inform the consumer about any ADR or other arrangement that is available if the consumer is dissatisfied with the outcome. The information must be given when the trader communicates the outcome of its consideration of the complaint. "ADR or other arrangement" covers schemes the trader is obliged to participate in by legislation, by a term of the contract, or by other contractual arrangement. The duty is enforceable by an enforcement notice under s 302, and does not displace any other information requirement.

Two consequences for drafting:

1. The duty is triggered **at the point of responding to a complaint**, not by publishing a static page. Build it into the complaint response template, not only into the terms.
2. If the trader participates in no ADR scheme, s 308 requires nothing to be named — but a statement to that effect in the terms is honest and avoids the consumer assuming otherwise. Never invent an ADR body.

## The ODR platforms

**Do not link either.** The EU online dispute resolution platform was shut down by Regulation (EU) 2024/3228 and ceased operating on 20 July 2025. The UK stopped participating after the end of the Brexit transition period, and the UK-facing ODR obligations were removed then. There is no UK equivalent platform.

A live ODR link on a UK trader's site is a dead link that misdescribes the consumer's options — a misleading omission risk under s 227 DMCC Act 2024. Search the whole project, including shop system texts and email templates, for `odr`, `ec.europa.eu/consumers/odr`, `online dispute resolution` and `ODR platform`, and remove every hit.

## Sector schemes that do apply

Where the business operates in a regulated sector, membership of a statutory ombudsman scheme is usually compulsory and independent of the DMCC regime. Name the correct one, or none:

| Sector | Body |
|---|---|
| Financial services, consumer credit, insurance, payments | Financial Ombudsman Service, `financial-ombudsman.org.uk` |
| Energy supply | Energy Ombudsman, `energyombudsman.org` |
| Telecoms and broadband | Communications Ombudsman or CISAS, depending on the provider's membership |
| Property and lettings agency | The Property Ombudsman or Property Redress Scheme |
| Legal services | Legal Ombudsman, `legalombudsman.org.uk` |
| Rail and aviation | Rail Ombudsman; the CAA-approved aviation ADR bodies |

Check actual membership before naming a body. Naming a scheme the trader does not belong to is a misleading action under s 226 DMCC Act 2024.

## Template

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h2>Complaints</h2>
<p>
  If something has gone wrong, contact us at <a href="mailto:[[address]]">[[address]]</a> or
  [[postal address]]. We will acknowledge your complaint within [[period]] and give you our final
  response within [[period]].
</p>
<p>
  [[If the trader participates in an ADR scheme:]]
  If you are not satisfied with our final response, you can refer the complaint to
  [[name of the ADR body]], [[website]]. [[State whether the trader is obliged to use the scheme or
  has agreed to do so voluntarily.]]
</p>
<p>
  [[If the trader participates in no scheme:]]
  We are not a member of an alternative dispute resolution scheme. If we cannot resolve your
  complaint, you can seek advice from Citizens Advice at
  <a href="https://www.citizensadvice.org.uk/consumer/">citizensadvice.org.uk/consumer</a>
  or take the matter to court.
</p>
```

Complaint response template addition, satisfying s 308:

```text
This is our final response to your complaint.
[[If you are not happy with this outcome you can refer the matter to [[ADR body]] at [[website]]
within [[time limit]]. / We are not a member of an alternative dispute resolution scheme.]]
```

## Checkpoints

- [ ] Project-wide search for `odr`, `online dispute resolution`, `ec.europa.eu/consumers/odr` returns nothing
- [ ] No citation of the Alternative Dispute Resolution for Consumer Disputes (Competent Authorities and Information) Regulations 2015 — revoked 6 April 2026
- [ ] ADR information delivered in the complaint response itself, not only on a static page (s 308(3))
- [ ] Any named ADR body verified as a scheme the trader actually belongs to
- [ ] Where the trader belongs to no scheme, the terms say so plainly rather than staying silent
- [ ] Statutory ombudsman named where the sector requires membership
- [ ] Complaint handling timescales stated and met
- [ ] Data protection complaints routed separately under DPA 2018 s 164A — see `accountability-and-fee.md`
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
