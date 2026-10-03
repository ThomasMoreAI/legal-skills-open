---
name: poland-digital-government
title: Poland Digital Government
description: Digital government. Use for public Polish portal guidance and safe human-in-the-loop operation with caller-owned tools.
author: Xopoko
author_url: https://github.com/Xopoko/poland/tree/main/skills/poland-digital-government
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: administrative
language: en
---

# Poland Digital Government

Use for choosing a Polish public portal, understanding public access
prerequisites, verifying a public official page, preparing an online procedure,
or assisting inside a protected service when the user explicitly requests it and
the host has a permitted caller-owned tool.

## Supported modes

- Offline: use bundled source IDs and packaged metadata.
- Public verification: Browser or the allowlisted source probe may inspect a
  public, unauthenticated official page.
- Preparation: produce reviewable field maps, questions, checklists, and drafts;
  keep personal values out of bundled plugin tools and durable artifacts.
- Protected assistance: establish the exact task scope, open the official
  service, yield control and pause capture for user-only authentication, then
  resume after the user says the session is ready.
- External effect: show the current target, material values, attachments, fees,
  timing, reversibility, and expected receipt; obtain fresh action-time
  confirmation before the consequential control.
- Manual fallback: when no permitted tool or capture-safe handoff exists, give
  semantic steps and continue from the user's reported page state.

The user chooses the identity provider and enters every password, passkey, PIN,
OTP, CAPTCHA/2FA response, and payment credential. With explicit task-scoped
authorization, the agent may inspect only the minimum relevant personal record
and fill necessary reviewable fields. Submission, sending, booking changes,
payment initiation, upload, download, account creation, and record changes
require action-time confirmation. The user applies signatures and attestations,
performs final payment authorization and irreversible destructive steps, and
places emergency calls. Never claim completion without a visible official
receipt or unambiguous final state.

Use the relevant domain skill for substantive content. For any public or
protected operation with a caller-owned Browser or Computer tool, apply
`../../references/automation-playbook.md`; automation is not a domain owner.
This plugin bundles no executable Browser or Computer adapter. Read
`../../references/browser-safety.md` before browser operation and
`../../references/digital-government-map.md` for portal ownership. For hands-on
navigation, read `../../references/portal-operator-playbooks.md` for supported
semantic phases, checkpoints, success evidence, and guided manual fallback;
re-discover current visible controls rather than relying on stored selectors or
coordinates.

Use the bundled digital-channel catalog to separate public guidance from the
protected service and to identify the responsible actor. In particular, do not
conflate Trusted Profile identity/signature with ePUAP correspondence; do not
treat mObywatel as a universal residence-card or status source; and treat MOS,
praca.gov.pl, e-Tax Office, and eZUS according to their domain and actor. For MOS
residence applications, route to `poland-stay-residence`; for employer-side
praca.gov.pl tasks, route to `poland-work-authorization`. Channel `stop_before`
entries are mandatory pause-and-classify points. The action registry and current
user checkpoint determine whether the agent may continue.
