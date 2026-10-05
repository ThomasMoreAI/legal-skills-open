# Consent UI Anti-Patterns

Israeli DPA enforcement, GDPR DPAs, and the French CNIL have published repeated guidance on UI patterns that look compliant but are not. Any of these will cost you on enforcement even if the underlying law text is satisfied.

| Anti-pattern | Why it fails | Fix |
|-------------|--------------|-----|
| Pre-checked boxes for analytics / marketing | Consent must be explicit opt-in. CJEU *Planet49* (C-673/17) is the binding precedent. | Default unchecked; user must actively flip the switch. |
| "Accept" button styled larger/colored, "Reject" styled as a text link | Fails the equal-weight test. | Same component, same size, same visual prominence. |
| "Reject" hidden behind a "Customize" or "Learn more" submenu | Forces extra clicks to refuse, not to accept. | Reject + Accept on the first screen, side by side. |
| "By continuing to use the site, you accept cookies" banners | Implicit consent is invalid under GDPR and Amendment 13. | Banner blocks nothing visually, but trackers do not run until explicit choice. |
| Cookie wall ("You must accept cookies to read this article") | EDPB guidance treats conditioning service on consent to non-essential cookies as invalid. | Provide full service regardless of the choice; degrade only genuinely analytics-dependent features (e.g. hide a session-replay-powered debug button). |
| Single "Accept all" with no granular option on the first screen | GDPR Article 7(2) requires granularity for distinct purposes. | Either expose the per-category toggles on the first screen, or ensure "Customize" reaches them in one click. |
| Re-prompting every session | Consent fatigue, treated by DPAs as a dark pattern. | Re-prompt only on `CONSENT_VERSION` bump or after 12 months. |
| Burying the "withdraw consent" path | Amendment 13 Article 8C + GDPR Article 7(3) require withdrawal to be as easy as granting. | "Privacy preferences" link in the footer that opens the same dialog. |
| Storing a consent cookie without an expiry / with multi-year TTL | User has not re-consented; stale consent is no consent. | 12-month max. Bump `CONSENT_VERSION` whenever you add a tracker. |
| Loading the analytics SDK script and calling it with `consent=denied` instead of not loading it | Loading itself is a data transfer (IP, UA, referer). | Gate the `<script>` tag, not just the SDK's internal flag. |

The banner you ship is one layer. The other layers, a published privacy policy in Hebrew, a named Privacy Protection Officer where required under Amendment 13, a data subject request handling process, a breach response plan, and the database registration for public bodies and data brokers, all have to exist independently. No consent UI substitutes for those.
