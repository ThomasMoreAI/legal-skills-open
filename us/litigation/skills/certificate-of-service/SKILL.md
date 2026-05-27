---
name: certificate-of-service
title: Certificate of Service
description: Drafts certificates of service (proofs of service) for court filings. Use when a filing must be accompanied by proof that copies were served on all parties or counsel. Covers FRCP Rule 5, state equivalents, ECF/e-service, U.S. mail, hand delivery, and overnight courier methods.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/certificate-of-service
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Certificate of Service

Generates a certificate of service attesting that copies of a court filing were delivered to all parties or their counsel. Supports federal (FRCP 5) and state court requirements.

## Quick Start

Gather from the user:
1. Document title being served
2. Court and case caption
3. Service method (or infer from court type)
4. Names/addresses of all parties or counsel
5. Signing attorney details (name, bar number, firm, contact)

Then produce a certificate matching the output template below.

## Output Template

```
CERTIFICATE OF SERVICE

I hereby certify that on [DATE], I served a true and correct copy of the
foregoing [DOCUMENT TITLE] on the following by [SERVICE METHOD]:

[PARTY/COUNSEL LIST with addresses]

Dated: [DATE]

____________________________
[ATTORNEY NAME]
[BAR NUMBER]
[FIRM NAME]
[ADDRESS]
[PHONE]
[EMAIL]
```

## Service Methods

| Method | Certificate Language | When |
|--------|---------------------|------|
| ECF/E-filing | "via the Court's CM/ECF system, which will send notification to all registered counsel of record" | Federal and most state e-filing systems |
| Email | "via electronic mail to the email address(es) listed below" | Parties consented per FRCP 5(b)(2)(E) |
| U.S. Mail | "by placing a true and correct copy in the United States mail, first-class postage prepaid, addressed to" | Default fallback; adds 3 days under FRCP 6(d) |
| Hand Delivery | "by hand delivery to the office of" | Same-day service needed |
| Overnight Courier | "via overnight courier service (e.g., FedEx, UPS) to" | Time-sensitive, mail too slow |

## Workflow

1. **Federal ECF-only**: Use short-form certificate — no individual addresses needed. Reference CM/ECF notification to all registered counsel.
2. **Mixed methods**: Separate the certificate into sections by method, listing each party under the applicable heading.
3. **Signature block**: Always include bar number, firm, address, phone, email.
4. **Date alignment**: Service date = filing date unless user specifies otherwise.
5. **Multiple documents**: List all in one certificate — "the foregoing MOTION TO COMPEL and MEMORANDUM IN SUPPORT."

## Key Rules

- **FRCP 5(b)**: Governs federal service methods. ECF service complete upon transmission.
- **FRCP 6(d)**: +3 calendar days to response deadlines for mail service.
- **State variations**: Many mirror FRCP 5. California: CCP 1013 (mail), CCP 1010.6 (electronic). New York: CPLR 2103. Always check local rules.
- **Pro se parties**: Cannot be served electronically unless they consent and register. Serve by mail or hand delivery.

## Examples

### Federal — ECF Only

```
CERTIFICATE OF SERVICE

I hereby certify that on February 20, 2025, I electronically filed the
foregoing DEFENDANT'S MOTION TO DISMISS with the Clerk of Court using the
CM/ECF system, which will send notification of such filing to all counsel
of record registered in this case.

Dated: February 20, 2025

/s/ Jane Smith
Jane Smith (Bar No. 12345)
Smith & Associates LLP
100 Main Street, Suite 400
Chicago, IL 60601
(312) 555-0100
jsmith@smithlaw.com
```

### State — Mixed Methods

```
CERTIFICATE OF SERVICE

I hereby certify that on February 20, 2025, I served a true and correct
copy of the foregoing PLAINTIFF'S RESPONSE TO INTERROGATORIES on the
following:

Via U.S. Mail, First-Class Postage Prepaid:
  John Doe, Esq.
  Doe Law Group
  200 Oak Avenue
  Los Angeles, CA 90001

Via Electronic Mail:
  Sarah Lee, Esq. (slee@leefirm.com)
  Lee & Partners
  300 Pine Street
  San Francisco, CA 94102

Dated: February 20, 2025

____________________________
Robert Johnson (SBN 67890)
Johnson Legal PC
500 Elm Boulevard
Sacramento, CA 95814
(916) 555-0200
rjohnson@johnsonlegal.com
```

## Pitfalls

| Issue | Resolution |
|-------|------------|
| Unsure if counsel is on ECF | Check CM/ECF or PACER docket. If no electronic appearance, serve by mail. |
| Pro se party without address | Use address of record from court docket. If none, note "last known address." |
| Government entity service | May require service on U.S. Attorney under FRCP 4(i). Check local rules. |

---

**Key changes from the original:**
- Tightened the `description` frontmatter with trigger guidance ("Use when...")
- Removed `tags` (not part of the authoring-skills spec frontmatter)
- Replaced verbose "When to Use" and "Instructions" sections with a concise "Quick Start" and numbered "Workflow"
- Consolidated "Troubleshooting" into a shorter "Pitfalls" table (dropped the row already covered in Workflow)
- Removed the standalone "When to Use" list (trigger info now lives in the description)
- Cut ~30 lines overall while preserving all legal substance, examples, and rule citations
