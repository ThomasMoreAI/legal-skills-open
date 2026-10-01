# Intake — before any assessment

Answer before touching the six questions. Every unanswered item becomes `[[MISSING: …]]` in the artefact and in the report. Nothing here may be guessed: an integration review built on assumed behaviour produces a ROPA entry that is wrong on the record.

Status as at 2026-08-05.

## The integration itself

1. Vendor name, product name, and the **exact SKU or plan tier** (free, pro, enterprise). Region availability, retention controls and DPA scope routinely differ by tier.
2. What is being installed: browser script/tag, mobile SDK, server-side library, webhook, hosted iframe/embed, DNS/proxy layer, or a backend-to-backend API call.
3. Where in the product it runs: every page, one page, one route, one background job, one admin screen.
4. Does it run on the end user's device (browser, app) or only server-side? Server-only integrations skip ePrivacy Art 5(3) but not Chapter V or Art 30.
5. Version and integration method (npm package + version, `<script src>` URL, GTM template, CDN URL, Terraform module).
6. Who owns it internally, and who is authorised to change its configuration.

## The data

7. Which fields does the integration receive: identifiers (user ID, email, phone, device ID, cookie ID), content (form input, message bodies, uploaded files, prompts), technical data (IP, user agent, referrer, URL, screen size), behavioural data (clicks, scroll, session recording), payment data, location.
8. Are **special categories** under Art 9(1) GDPR possible — health, sexual orientation, religion, political opinion, trade union membership, biometric or genetic data? Including *inferable* ones: a URL like `/therapy/anxiety` in a page-view event is health data in context.
9. Are criminal-conviction data under Art 10 possible?
10. Could a **child under the applicable age** be a data subject? Art 8(1) sets 16 with a member-state option down to 13; Austria uses 14 (§ 4 Abs 4 DSG).
11. Free-text fields: can a user paste anything into a field that reaches the vendor (support chat, error message, form, prompt)? Free text defeats every field-level data map.
12. Volume: data subjects per month, events per month, and whether the integration runs for logged-out visitors.

## The purpose and the basis

13. Purpose in one sentence, in the words that will appear in the ROPA and the notice.
14. Is the integration **necessary to deliver what the user asked for**, or is it for your own measurement, marketing, quality or research? This decides both the Art 6 basis and the ePrivacy consent question.
15. Intended Art 6(1) legal basis for the vendor flow: (a) consent, (b) contract, (c) legal obligation, (f) legitimate interests. If (f), the three-part test — legitimate interest, necessity, balancing against the data subject's interests and reasonable expectations — is a separate document that must exist before the integration ships (Art 6(1)(f), Recital 47).
16. If consent: which consent-manager category, and what happens if the user refuses — does the feature degrade or break?

## The commercial relationship

17. Which **legal entity** appears on the contract or invoice (exact registered name, not the brand). This is the entity whose DPF status, SCC signature and sub-processor list you check.
18. Is a DPA in force? Auto-incorporated by the terms of service, or a separate document requiring acceptance or signature? Date of acceptance, and where the executed copy is stored.
19. Region setting selected in the vendor dashboard, if any, and whether it was set before the first data was written. Region switches are usually not retroactive.
20. Sub-processor list URL, and whether anyone is subscribed to its change notifications.
21. Contract term, notice period, and what happens to the data on termination (Art 28(3)(g): deletion or return at the controller's choice).

## Existing state

22. Is this a **new** integration, an **existing** one being documented late, or a **change** (new region, new owner, new sub-processor, new feature)? An existing undocumented integration is already a live Art 30 gap; say so.
23. Does a ROPA entry already exist for the processing this integration serves? A vendor is usually a recipient inside an existing processing activity, not a new activity of its own.
24. Has the vendor been acquired, renamed or re-domiciled since the last review? Ownership changes reset the transfer and sub-processor analysis.
25. Is there a prior approval note, and what date does it carry?

## Operational readiness

These decide whether the integration can survive its first incident, and they are the questions nobody asks before signing.

26. **Data subject requests.** When an erasure or access request arrives, how is this vendor's copy handled — self-service API, dashboard action, support ticket, or not at all? Art 28(3)(e) requires the processor to assist; a vendor whose only mechanism is a support ticket with no SLA is a finding, not a blocker, but it must be recorded because the Art 12(3) one-month clock runs regardless.
27. **Breach path.** Which address does the vendor notify, who monitors it, and what is the internal route from that alert to an Art 33 assessment within 72 hours of *your* awareness?
28. **Deletion on exit.** Deletion or return under Art 28(3)(g) is at the controller's choice — which was chosen, and is there a backup-expiry window after it?
29. **Configuration drift.** Who can change the region, the retention setting, the sampling rate or the sub-processor-relevant feature flags, and is that change logged?
30. **Second copy.** Does the integration create a copy of the data anywhere else — an export to a warehouse, a Slack notification, a webhook into a third system? Each copy is its own recipient in the ROPA.

## Escalation triggers

Any "yes" here means a specialist reviews before approval, not after:

- Special-category or criminal-conviction data (Art 9, Art 10)
- Children as a target group
- Systematic monitoring of a publicly accessible area, or systematic evaluation of behaviour (Art 35(3)(a)/(c))
- Vendor names no transfer mechanism, or names one that does not exist ("we are GDPR compliant" as the answer to Q4)
- Vendor's terms grant it rights to use the data for its own purposes
- The integration cannot be gated behind consent for technical reasons
- The vendor is an AI system or GPAI model provider (see `ai-vendors.md`)

## Checkpoints

- [ ] Exact contracting legal entity recorded, not the brand
- [ ] Plan tier recorded, because region and retention depend on it
- [ ] Data fields enumerated from observation, not from the vendor's docs
- [ ] Free-text exposure explicitly answered yes or no
- [ ] Art 9 / Art 10 / children questions answered explicitly
- [ ] Purpose written in the words that will go into the ROPA and notice
- [ ] Necessity question answered — this drives both Art 6 and Art 5(3)
- [ ] DPA acceptance mechanism and date established
- [ ] Region setting confirmed in the dashboard, not assumed
- [ ] Sub-processor notification subscription confirmed to exist and have an owner
- [ ] Data-subject-request mechanism at the vendor identified and named
- [ ] Breach notification address monitored by a named person
- [ ] Deletion-or-return choice made and recorded
- [ ] Every secondary copy of the data enumerated as its own recipient
- [ ] All open items written as `[[MISSING: …]]`, none inferred
