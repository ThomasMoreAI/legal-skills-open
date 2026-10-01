# Cookies and similar technologies

Cookie rules are in PECR, not in the UK GDPR. PECR supplies the prohibition; the UK GDPR supplies the standard of consent. Since 5 February 2026 PECR also supplies UK GDPR-level fines.

## Reg 6 PECR 2003 (SI 2003/2426)

Status as at 2026-08-05: reg 6 was substituted, and Schedule A1 inserted, by the Data (Use and Access) Act 2025 s 112 and Sch 12, in force 5 February 2026 (SI 2026/82).

Reg 6(1): subject to Schedule A1, a person must not store information, or gain access to information stored, in the terminal equipment of a subscriber or user. Storing or gaining access includes instigating the storage or access, and gaining access includes collecting or monitoring information automatically emitted by the terminal equipment.

The rule is technology-neutral. It covers cookies, localStorage, sessionStorage, IndexedDB, SDK identifiers, pixels, device fingerprinting and anything else that writes to or reads from the device.

## Schedule A1 — the exceptions

Status as at 2026-08-05: in force from 5 February 2026.

| Para | Exception | Condition |
|---|---|---|
| 2 | Consent | Clear and comprehensive information about the purposes, and consent given. Consent may be signified through browser or application settings where those genuinely express a choice |
| 3 | Transmission | Sole purpose of carrying out the transmission of a communication over an electronic communications network |
| 4 | Strictly necessary | Strictly necessary for the provision of an information society service requested by the subscriber or user — including protecting information, terminal equipment security, preventing or detecting fraud or technical faults, authentication, and maintaining the user's selections |
| 5 | Statistical purposes | Provider of the service collects information solely for statistical purposes about how the service is used, in order to make improvements. The user must be given information about the purposes and a simple means of objecting, free of charge |
| 6 | Website appearance or functionality | Sole purpose of enabling the website to adapt to the user's preferences or to improve its appearance or functionality. Same information and objection requirements as para 5 |
| 7 | Emergency assistance | Sole purpose of determining the geographical position of the terminal equipment in response to an emergency request |

The paras 5 and 6 exceptions are narrower than they look. They fail if:

- the data is used for anything beyond improving the service — for example advertising measurement, audience segmentation, or product analytics fed into a marketing stack
- the data is transmitted to a third party for that third party's own purposes
- no information is given, or objecting is not simple and free

Most standard analytics deployments transmit to a vendor that reserves rights to use the data for its own purposes. In that configuration the exception does not apply and consent is required. Do not tell a user "the DUAA means you can drop the analytics banner" without inspecting the vendor terms and the actual configuration.

## Consent standard

Consent takes its meaning from the UK GDPR: freely given, specific, informed and unambiguous, by a clear affirmative action, and as easy to withdraw as to give. Consequences:

- no pre-ticked boxes, no implied consent from continued browsing
- no non-essential cookie set before the user makes a choice
- reject must be available at the first layer, with equal prominence to accept
- granular choice per purpose, and a persistent way to change the decision
- a consent record with timestamp, the banner version and the choices made

## ICO enforcement

The ICO announced on 23 January 2025 that it would review the top 1,000 UK websites for cookie compliance, opening with a sweep of 200 sites and warning 134 operators. It reported in December 2025 that engagement had produced widespread change, with preliminary enforcement notices issued to a minority that did not fix the problems. The recurring findings were: no "reject all" at the first layer, banners that assert consent from continued use, and analytics or advertising tags firing before any choice.

Penalties: PECR Schedule 1 was replaced by DUAA s 115 and Sch 13 on 5 February 2026, applying DPA 2018 Parts 5–7 to PECR. Breaches of reg 6 attract the higher maximum under DPA 2018 s 157 — £17.5 million or 4% of total annual worldwide turnover, whichever is higher. The former £500,000 ceiling no longer applies.

## Template

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h1>Cookies</h1>

<p>
  We store information on your device, and read information from it, when you use this site.
  Some of it is necessary for the site to work. The rest we use only if you agree.
  You can change your choice at any time using the "Cookie settings" link in the footer.
</p>

<h2>What we use</h2>
<table>
  <tr><th>Name</th><th>Provider</th><th>Purpose</th><th>Category</th><th>Duration</th><th>Basis</th></tr>
  <tr>
    <td>[[name]]</td><td>[[provider]]</td><td>[[purpose]]</td>
    <td>[[strictly necessary / statistical / appearance / marketing]]</td>
    <td>[[duration]]</td>
    <td>[[PECR Sch A1 para 4 / para 5 / para 6 / consent under para 2]]</td>
  </tr>
</table>

<h2>Statistical and appearance technologies used without consent</h2>
<p>
  [[Only include this block where paras 5 or 6 genuinely apply.]]
  We use [[name]] solely to [[collect statistics about how this site is used so that we can improve it /
  remember your display preferences]]. The information is not shared with anyone for their own purposes.
  You can object at any time, free of charge, using [[link or control]].
</p>

<h2>Changing your choice</h2>
<p>[[link to the consent management interface]]</p>
```

## Checkpoints

- [ ] Load the site in a clean profile with the network tab recording. No non-exempt request fires before a choice is made
- [ ] Application tab: every cookie, localStorage and IndexedDB entry present before the choice is accounted for by a Schedule A1 exception
- [ ] "Reject all" on the first layer, visually equal to "Accept all"
- [ ] No pre-ticked categories, no "by continuing you agree"
- [ ] Granular choice per purpose
- [ ] Withdrawal as easy as giving consent, control permanently reachable from the footer
- [ ] Cookie table verified against the actual network log, not copied from the vendor's documentation
- [ ] For every para 5 or para 6 claim: vendor terms checked, no third-party own-purpose use, objection route live and free
- [ ] Consent log retained with timestamp, banner version and choices
- [ ] Embedded maps, video and fonts either self-hosted or behind consent
- [ ] Cookie information reachable without accepting anything
- [ ] No claim that cookie consent is a "GDPR" requirement — it is PECR reg 6
