# The privacy policy

Status as at 2026-08-05.

There is no such thing as "a US privacy policy". There is a document that has to satisfy every state law that reaches the business, plus CalOPPA, plus any sectoral regime — and that must not promise anything the business does not actually do, because every voluntary statement in it is enforceable under FTC Act § 5, 15 U.S.C. § 45, and under every state UDAP statute.

**Two failure modes, and they are opposite.** A template copied from another company **over-promises** (a "right to be forgotten", a "data protection officer", "we never sell your data") and creates § 5 exposure for commitments the business does not honour. A minimal policy **under-discloses** and misses a state's mandatory content. Both are produced by drafting from a template instead of from the intake answers and the actual tag list.

## Determine scope first

Do not start drafting. Run `state-privacy-scope.md` and establish which state laws apply, then `california-ccpa.md` if California is in scope. The content of the policy is a union of the applicable laws, not a fixed list.

Minimum floor even for a business under every comprehensive-law threshold:

- **CalOPPA** (Cal. Bus. & Prof. Code § 22575 et seq.) applies to any commercial site collecting personally identifiable information from Californians, with no threshold. It alone requires a conspicuously posted policy.
- **FTC Act § 5** makes whatever is published binding.
- Sectoral regimes (COPPA, GLBA, HIPAA, FERPA) apply on their own triggers regardless of size.

## Content

Sections that belong in nearly every US privacy policy:

1. **Identity and contact** — legal entity name, postal address, an email address, and a request channel. Under CCPA a toll-free number is required unless the online-only exception applies.
2. **Effective date and last-updated date.** CCPA requires an update at least once every 12 months (§ 1798.130(a)(5)). CalOPPA requires the effective date.
3. **Categories of personal information collected**, mapped to their sources. Use the statutory categories, not marketing language.
4. **Purposes** for each category. "To improve our services" is not a purpose; it is a placeholder.
5. **Sensitive personal information** identified separately, with purposes, and the limitation right if California applies.
6. **Categories of third parties** each category is disclosed to, and the character of the disclosure: sale, share for cross-context behavioural advertising, or disclosure to a service provider or processor under contract. Some states (Oregon among them) give consumers the right to obtain the **specific third parties** by name on request — see `state-privacy-scope.md`.
7. **Retention** — a period or the criteria used to determine it, per category. California requires this at collection as well.
8. **Rights and how to exercise them**, per state, including the response deadline and the appeal mechanism where a state requires one.
9. **Opt-out mechanisms** — sale/share opt-out, targeted advertising opt-out, profiling opt-out, and the treatment of opt-out preference signals.
10. **Children** — the age position, and the COPPA content if the service is child-directed.
11. **Automated decisionmaking and profiling**, if used.
12. **Security** — a factual statement. Never "your data is completely secure"; that is a § 5 deception waiting for a breach.
13. **International transfers**, if the business is also GDPR-exposed. Otherwise omit — a US-only policy does not need a transfer section, and adding one signals a copied EU template.
14. **Changes to the policy** and how they are notified.
15. **Do Not Track disclosure** — CalOPPA requires the operator to disclose how it responds. A truthful "we do not respond to Do Not Track browser signals; we do honour Global Privacy Control signals as described above" satisfies it.

## If the business receives EU data — the DPF after Trump v. Slaughter

Only relevant where item 13 applies. Certification under the EU-US Data Privacy Framework is what lets an EU exporter send you data without further paperwork, under Commission Implementing Decision (EU) 2023/1795. It is administered by the International Trade Administration and **enforced by the FTC** against your § 5 commitments.

On **29.06.2026** the Supreme Court held in *Trump v. Slaughter* that the FTC's for-cause removal protections are unconstitutional. That is a US constitutional holding, but its consequence is commercial and lands on the US side of the transfer:

- **Nothing about your certification changed.** The DPF list, the annual re-certification obligation and the § 5 exposure for claiming participation you no longer hold are all unaffected. A removed organisation must still apply the Principles to data it received while participating.
- **Your EU customers' basis is what is under pressure.** Decision 2023/1795 relies on FTC independence throughout. As at 05.08.2026: noyb asked the Commission on 29.06.2026 to repeal it and announced an annulment action (no filing confirmed); the EDPB wrote to Commissioner McGrath on 31.07.2026 asking for a close assessment; the Commission has not acted, and the decision remains in force.
- **Expect the paperwork, do not resist it.** EU counterparties will now ask for standard contractual clauses under Art 46(2)(c) GDPR as a documented fallback and for input into their transfer impact assessment — specifically on government access (FISA § 702, EO 12333, CLOUD Act) and on what redress an EU individual actually has. Having SCCs already executed turns a future withdrawal into a paperwork event; not having them turns it into a service interruption.
- **Do not say the DPF has been struck down** in customer-facing text, and do not say the ruling has no effect. Both are wrong, and a US privacy policy that overstates its EU position is a § 5 problem in the same way an overstated security claim is.

## The "sale" trap

Under state law definitions, "sale" and "share" turn on the exchange of personal information for **monetary or other valuable consideration**, and on disclosure for cross-context behavioural advertising. Running Meta, Google Ads, TikTok or most advertising and attribution pixels is a sale or a share in nearly every case, whether or not money moves. Consequences:

- The policy must **say so** and the opt-out link must exist and work.
- A statement that the business "does not sell personal information" while those tags are live is a deception under § 5 and a straightforward state AG enforcement target. It is also the most common sentence in copied US privacy policies.

Verify against the network tab, not against the client's belief.

## Template skeleton

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h1>Privacy Policy</h1>
<p>Effective date: [[DATE]]. Last updated: [[DATE]].</p>

<h2>Who we are</h2>
<p>
  [[LEGAL ENTITY NAME]], [[STREET ADDRESS, CITY, STATE ZIP]], United States.
  Contact: <a href="mailto:[[EMAIL]]">[[EMAIL]]</a>[[, toll-free: [[NUMBER]]]].
</p>

<h2>Information we collect</h2>
<table>
  <tr><th>Category</th><th>Examples</th><th>Source</th><th>Purpose</th><th>Retention</th></tr>
  <tr><td>[[CATEGORY]]</td><td>[[EXAMPLES]]</td><td>[[SOURCE]]</td><td>[[PURPOSE]]</td><td>[[PERIOD OR CRITERIA]]</td></tr>
</table>

<h2>Sensitive information</h2>
<p>[[LIST, OR: We do not collect sensitive personal information.]]</p>

<h2>How we disclose information</h2>
<table>
  <tr><th>Category</th><th>Recipients</th><th>Nature of disclosure</th></tr>
  <tr><td>[[CATEGORY]]</td><td>[[CATEGORIES OF THIRD PARTIES]]</td><td>[[sale / share for cross-context behavioural advertising / service provider]]</td></tr>
</table>

<h2>Sale and sharing of personal information</h2>
<p>
  [[STATE THE TRUTH, VERIFIED AGAINST THE ACTUAL TAG LIST. If advertising or
  analytics tags are present, this section says that personal information is
  sold or shared, names the categories, and links the opt-out.]]
</p>

<h2>Your choices</h2>
<p><a href="[[URL]]">Do Not Sell or Share My Personal Information</a></p>
<p><a href="[[URL]]">Limit the Use of My Sensitive Personal Information</a></p>
<p>
  We [[do / do not]] honour the Global Privacy Control opt-out preference
  signal. We [[do / do not]] respond to Do Not Track browser signals.
</p>

<h2>Your rights</h2>
<p>[[PER-STATE RIGHTS BLOCK — see state-privacy-scope.md. State the response
deadline and, where required, the appeal process and how to contact the
state attorney general if an appeal is denied.]]</p>

<h2>Children</h2>
<p>[[SEE children-and-teens.md]]</p>

<h2>Security</h2>
<p>
  We maintain administrative, technical and physical safeguards designed to
  protect personal information. [[NO ABSOLUTE ASSURANCE.]]
</p>

<h2>Changes</h2>
<p>[[HOW CHANGES ARE NOTIFIED]]</p>
```

## What must not appear

| Do not write | Why |
|---|---|
| "Right to be forgotten" | Not a US concept. The US right is a right to delete, with statutory exceptions that are wider than Art 17 GDPR. |
| "We process your data on the basis of legitimate interests" | No US law has legal bases. Stating one imports an EU framework that no US regulator applies, and it may read as an admission that consent was not obtained where consent was required. |
| "Our Data Protection Officer can be contacted at…" | No US law requires a DPO. If a DPO is named, the business is held to having one. |
| "We are GDPR compliant" | An enforceable claim under § 5 unless it is true and demonstrable. |
| "We do not sell your personal information" (with ad tech live) | False under the statutory definition of sale/share. |
| "Your data is completely secure" / "military-grade encryption" | Absolute security claims are a standing § 5 exposure. |
| "This policy is governed by the laws of [state] and you consent to jurisdiction there" | Choice of law in a privacy notice does not displace a state privacy statute that applies by residence. |
| A cookie table copied from a European site | Lists cookies the site does not set, which is itself a misstatement. |

## Checkpoints

- [ ] Scope determined from `state-privacy-scope.md` before drafting, and written down
- [ ] Every category, purpose, recipient and retention period taken from the intake answers, not from a template
- [ ] Sale/share statement verified against a live network capture of the site
- [ ] Opt-out links present and functional
- [ ] Rights section matches the states actually in scope — no rights granted that the business will not honour, and none omitted that a state requires
- [ ] Appeal mechanism built where a state requires one
- [ ] Response deadlines stated and operationally achievable
- [ ] Policy reachable from every page without a login and without a consent banner blocking it
- [ ] Last-updated date within 12 months
- [ ] No GDPR vocabulary (legal basis, controller-only framing, DPO, right to be forgotten) unless the business is genuinely GDPR-exposed and the section is correct
- [ ] No absolute security claim
- [ ] Every `[[…]]` placeholder resolved or reported as outstanding
- [ ] Draft marker still present
