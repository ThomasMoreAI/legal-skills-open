# Lawful Bases for Processing

Under Article 6(1) of the GDPR, processing is lawful only if at least one basis applies. For special category data (Article 9), a *second* condition from Article 9(2) is additionally required.

## Article 6(1) — general personal data

| Basis | When it fits | When it doesn't |
|---|---|---|
| (a) Consent | Processing genuinely optional; freely given, specific, informed, unambiguous | Employer/employee relationship (power imbalance); bundled with service |
| (b) Contract | Processing necessary to perform a contract with the data subject or take pre-contract steps at their request | Processing only *useful* to contract (use a different basis or consent) |
| (c) Legal obligation | EU/Member-State law mandates the processing (e.g., tax records) | Other jurisdictions' law (use Art. 49 transfer basis) |
| (d) Vital interests | Life-or-death situations | Routine processing |
| (e) Public task / official authority | Public-sector or statutory roles | Most private-sector processing |
| (f) Legitimate interests | Controller's or third party's interest, balanced against subject's rights | Processing of children's data for marketing (heavily constrained); no LIA performed |

### Consent quality checklist

- **Freely given** — no detriment for refusing; not a precondition for service unless necessary.
- **Specific** — one purpose per consent; granular toggles where multiple purposes exist.
- **Informed** — controller identity, purposes, data types, withdrawal mechanism.
- **Unambiguous** — clear affirmative action; no pre-ticked boxes (Art. 7; EDPB 05/2020).
- **Demonstrable** — record of consent with timestamp and version of notice shown.
- **Withdrawable** — as easy to withdraw as to give.

### Legitimate interests assessment (LIA)

When relying on Art. 6(1)(f), document a three-part test:

1. **Purpose test** — is there a legitimate interest?
2. **Necessity test** — is the processing necessary to achieve it? Could you use less data?
3. **Balancing test** — do data subjects' rights override the interest? Consider reasonable expectations, impact, safeguards.

Document the LIA. ICO and EDPB have published templates; use them as a starting point.

## Article 9(2) — special category data

Processing special category data is *prohibited* unless one of Art. 9(2) conditions applies *in addition to* an Art. 6 basis.

Common Art. 9(2) conditions:

- (a) Explicit consent
- (b) Employment / social security / social protection (Member-State law)
- (d) Not-for-profit body processing members' data
- (f) Legal claims or judicial proceedings
- (g) Substantial public interest (Member-State law)
- (h) Preventive/occupational medicine, medical diagnosis, care (by health professional or equivalent)
- (i) Public interest in public health
- (j) Archiving, research, statistical (with safeguards)

## Article 10 — criminal convictions

Additional restrictions; typically requires EU/Member-State law authorization.

## Purpose limitation (Art. 5(1)(b))

You cannot silently repurpose data. To reuse data for a new purpose, either:

- Show the new purpose is *compatible* with the original (compatibility assessment per Art. 6(4)), or
- Obtain a fresh lawful basis (often new consent).

Compatibility factors: link between purposes, context of collection, nature of data, possible consequences, safeguards (e.g., pseudonymisation).

## Choosing a basis — decision heuristic

1. Is there a law requiring the processing? → **(c) Legal obligation**.
2. Is it necessary for the contract the user signed up for? → **(b) Contract**.
3. Is the user genuinely choosing (e.g., marketing opt-in, optional analytics)? → **(a) Consent**.
4. Does the processing serve a business interest and not materially impact the user? → **(f) Legitimate interests** with a documented LIA.
5. Is any of the above special category? → Add an Art. 9(2) condition on top.

Document the basis in the ROPA entry for each processing activity. Switching bases mid-processing is problematic and rarely the right answer.
