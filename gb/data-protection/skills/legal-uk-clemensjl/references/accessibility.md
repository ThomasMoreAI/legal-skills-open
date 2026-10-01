# Accessibility

Two separate regimes. Every service provider is under the Equality Act 2010 duty. Public sector bodies are additionally under the 2018 Regulations, which are the only ones that mandate a published accessibility statement.

**The European Accessibility Act (Directive (EU) 2019/882) does not apply in the UK.** It has no UK implementing legislation. Citing it, or a national implementation such as the Austrian BaFG or the German BFSG, at a UK business is a straight import error. The reverse trap holds: a UK business selling into the EEA is caught by the EAA as implemented in each member state where it operates, which is a separate workstream.

## Equality Act 2010 — private sector

Status as at 2026-08-05: in force.

**Section 29** makes it unlawful for a service provider to discriminate against a person requiring the service. Section 29(7) applies the duty to make reasonable adjustments to service providers and to those exercising a public function. Schedule 2 sets out how the duty applies to services.

**Section 20** sets three requirements:

1. where a provision, criterion or practice puts a disabled person at a substantial disadvantage compared with a non-disabled person, take such steps as it is reasonable to have to take to avoid the disadvantage
2. where a physical feature causes that disadvantage, remove, alter or provide a reasonable means of avoiding it
3. where a disabled person would, but for an auxiliary aid, be at a substantial disadvantage, take such steps as it is reasonable to have to take to provide the auxiliary aid

Section 20(6): where the disadvantage relates to information, the steps include providing it in an accessible format. Section 20(7): the disabled person may not be required to pay any of the cost.

Two features distinguish the service-provider duty from the employment duty:

- it is **anticipatory**. The provider must consider in advance what disabled people generally need, not wait for an individual to ask.
- it is **continuing**. Compliance is reassessed every time the service changes.

A website is a means by which a service is provided, so an inaccessible checkout, an image-only PDF, an unlabelled form or a keyboard trap is a failure to make reasonable adjustments. Enforcement is by individual claim in the county court (sheriff court in Scotland) under s 114, not by a regulator, which is why breaches surface as claims and reputational complaints rather than as fines.

There is no statutory technical standard for the private sector. WCAG 2.2 level AA is the evidential benchmark: meeting it is the practical way to show the adjustment was reasonable, and failing a specific success criterion is the practical way a claimant shows it was not.

## Public Sector Bodies Accessibility Regulations 2018 (SI 2018/952)

Status as at 2026-08-05: in force.

- reg 4 — application, to public sector bodies as defined
- reg 6 — obligation to make websites and mobile applications accessible: perceivable, operable, understandable and robust
- reg 7 — disproportionate burden assessment, which must be carried out and documented before it can be relied on
- reg 8 — accessibility statement, published in an accessible format and kept up to date
- reg 9 — presumed conformity where the relevant harmonised standard is met
- reg 10 — monitoring and reporting
- regs 11–14 — enforcement

GOV.UK guidance sets the standard as WCAG 2.2 level AA. The Cabinet Office position is that the standard tracks the current version of WCAG, with a grace period after each new version is published. The Government Digital Service monitors compliance and the Equality and Human Rights Commission enforces.

## Accessibility statement template

Mandatory for public sector bodies (reg 8). Recommended, not required, for private-sector sites — where it is voluntary it must still be accurate, because an overstated claim is a misleading action under s 226 DMCC Act 2024.

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h1>Accessibility statement for [[website or app name]]</h1>
<p>This statement applies to [[scope: domains, subdomains, apps]].</p>

<h2>How accessible this website is</h2>
<p>
  This website is [[fully compliant / partially compliant / non-compliant]] with the Web Content
  Accessibility Guidelines version 2.2 AA standard.
  [[List the known problems, each mapped to the WCAG success criterion it fails.]]
</p>

<h2>Feedback and contact information</h2>
<p>
  If you need information on this website in a different format, contact
  <a href="mailto:[[address]]">[[address]]</a> or [[telephone]].
  We will reply within [[period]].
</p>

<h2>Reporting accessibility problems</h2>
<p>Tell us at <a href="mailto:[[address]]">[[address]]</a>.</p>

<h2>Enforcement procedure</h2>
<p>
  [[Public sector bodies only:]] If you are not happy with how we respond to your complaint,
  contact the Equality Advisory and Support Service at
  <a href="https://www.equalityadvisoryservice.com/">equalityadvisoryservice.com</a>.
</p>

<h2>Technical information about this website's accessibility</h2>
<p>
  [[Public sector bodies:]] [[Name]] is committed to making its website accessible, in accordance with
  the Public Sector Bodies (Websites and Mobile Applications) (No. 2) Accessibility Regulations 2018.
</p>

<h2>Non-accessible content</h2>
<p>[[Each item, the WCAG criterion it fails, the reason (non-compliance, disproportionate burden with a documented assessment, or content outside scope), and the date it will be fixed.]]</p>

<h2>Preparation of this statement</h2>
<p>
  This statement was prepared on [[date]] and last reviewed on [[date]].
  This website was last tested on [[date]] by [[who]] using [[method]].
</p>
```

## Checkpoints

- [ ] Every main flow completed with the keyboard alone, focus visible at every step
- [ ] Screen reader pass over sign-up, checkout or the primary conversion flow
- [ ] Form fields have programmatically associated labels; errors described in text, not colour alone
- [ ] Contrast measured against WCAG 2.2 AA thresholds, not judged by eye
- [ ] Images have meaningful alternative text; decorative images marked as such
- [ ] Video has captions; audio has a transcript
- [ ] Page zoom to 200% and 320 CSS pixel reflow tested
- [ ] `prefers-reduced-motion` respected
- [ ] PDFs and downloads are tagged and readable, or an accessible alternative is offered
- [ ] Public sector body: accessibility statement published, accurate, dated, with the enforcement paragraph (reg 8)
- [ ] Disproportionate burden claims backed by a documented assessment (reg 7)
- [ ] Private sector: no accessibility claim published that testing does not support
- [ ] No reference to the European Accessibility Act or a national EU implementation
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
