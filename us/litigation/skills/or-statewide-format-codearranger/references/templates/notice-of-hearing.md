# Notice of Hearing Template (Oregon)

Oregon's analog to Washington's "Note for Motion Docket" is the
**Notice of Hearing**. Some local SLRs call it a "Notice of
Hearing on Motion" or "Notice of Oral Argument." It places a
motion on the court's calendar.

## Who files it

The **moving party** files the Notice of Hearing after the motion
is filed (or simultaneously, depending on local practice). The
Notice tells the court and the other parties when the motion will
be heard, where, and in what mode (in person / WebEx / phone).

## Local-rule variation

Some Oregon circuits do not require a separate Notice of Hearing —
the moving party requests a date in the motion itself or by
ex-parte contact with the judicial assistant. Always check the
**Supplemental Local Rules (SLR)** for the specific circuit before
filing:

- **Multnomah SLR 5.025** — Civil motions are set by request to
  the judicial assistant
- **Washington County SLR 5.045** — Notice of Hearing on Motion
  filed simultaneously with the motion
- **Lane SLR 7** — Hearing date obtained from the Court
  Administrator
- **Marion SLR 5.045** — Set by phone or email to chambers

See the relevant `or-multcc`, `or-wccc`, or `or-county-courts`
skill for the precise per-court protocol.

## Scaffolded markdown

```
            IN THE CIRCUIT COURT OF THE STATE OF OREGON
                  FOR THE COUNTY OF WASHINGTON

[PARTY A],                      │   Case No. 25CV12345
                                │
     Plaintiff,                 │   NOTICE OF HEARING ON
                                │   DEFENDANT'S MOTION TO
     v.                         │   COMPEL PRODUCTION OF
                                │   DOCUMENTS
[PARTY B],                      │
                                │   HEARING: [DATE] at [TIME]
     Defendant.                 │   PLACE: Courtroom [#]
                                │   BEFORE: Hon. [Judge]
                                │   MODE: [In person / WebEx]
────────────────────────────────────────────────────────────

TO:  Plaintiff [Name] and Plaintiff's counsel of record
     [Name, OSB #, Address, Email]

PLEASE TAKE NOTICE that Defendant's Motion to Compel Production
of Documents Under ORCP 46 A, filed [date], will be heard before
the Honorable [Judge name], Department/Courtroom [#] of the
Circuit Court of the State of Oregon for the County of
Washington, on:

       [DAY OF WEEK], [MONTH DAY], 20[YY] at [TIME] [AM/PM]
       Hearing mode: [In person / WebEx]
       WebEx information: [meeting ID, password, or URL]
                          (if remote)

The hearing was reserved by [request to judicial assistant /
ex-parte contact / SLR-prescribed method] on [date]; confirmation
is attached as Exhibit 1 to this Notice.

Defendant requests oral argument; estimated time:
[20 minutes / 30 minutes].

DATED this ____ day of __________, 20__.

______________________________________
[FULL NAME]
[Defendant, pro se / Attorney for Defendant, OSB # ______]
[Street Address]
[City, OR ZIP]
[Phone]
[Email]


                  CERTIFICATE OF SERVICE

[Per UTCR 1.090]
```

## What changes per court

| Court | Notice required? | How to reserve date |
|-------|------------------|---------------------|
| Multnomah | Yes, separate filing | Email judicial assistant for the assigned department |
| Washington Co | Yes, filed with motion | Call or email Civil Department for date |
| Clackamas | Sometimes | Set with judicial assistant; some judges by ex-parte motion |
| Lane | Yes | Court Administrator's office sets date |
| Marion | Yes | Chambers contact |
| Jackson | Yes | Judicial assistant of assigned judge |
| Deschutes | Yes | Court coordinator |

For the precise per-court protocol, use `or-schedule-hearing` to
draft the reservation contact (email or phone log) and then `or-
draft-note` to produce the Notice itself.

## Pro se filer notes

- A pro se filer must use the same Notice format as counseled
  parties. Pro se status does not change the requirements.
- Email is acceptable for ex-parte contact with the judicial
  assistant; phone is acceptable in many courts. Keep a written
  record (an email or a memo-to-file documenting the phone call)
  of the date reservation.
- Once the date is reserved, file the Notice on File and Serve in
  the same case as the motion, and serve all other parties under
  ORCP 9 (typically via the eService route — File and Serve
  defaults to email service of registered parties).

## What NOT to put on the Notice

- Argument or factual narrative — those belong in the motion and
  declaration. The Notice is a scheduling document, period.
- Exhibits to the underlying motion. The Notice may have one
  exhibit if needed (the chambers email confirming the date), but
  the substantive exhibits stay with the declaration.
