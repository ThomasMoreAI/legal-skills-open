# King County Local Rules — KCLCR and KCDCLCR

Washington superior and district courts are each governed by
**statewide** rules (CR, CRLJ) **plus** a set of **local rules**
specific to the county. Local rules cannot conflict with the
statewide rules, but they fill in procedural details the statewide
rules leave to local practice: motion confirmation, working copies,
settlement conferences, case scheduling, e-filing, and more.

> **Fetch the current version before citing.** Local rules are
> amended more frequently than statewide rules. See
> `online-sources.md` for URL patterns.

## KCLCR — King County Local Civil Rules (Superior Court)

Applies to the **King County Superior Court**. Canonical URL:

```
https://kingcounty.gov/en/court/superior-court/courts-jails-legal-system/resources-research/local-rules
```

### Key KCLCR rules

| Rule | What it governs |
|------|-----------------|
| KCLCR 4 | Case scheduling orders, case types, assignment |
| KCLCR 7 | Motions — confirmation requirement, working copies, courtesy copies to judge |
| KCLCR 10 | Form of papers — local overlays on GR 14 |
| KCLCR 40 | Trial setting, readiness for trial |
| KCLCR 43 | Remote hearings, video appearance rules |
| KCLCR 56 | Summary judgment — confirmation, working copies |
| KCLCR 77 | Court organization, departments |
| KCLCR 98 | Probate |

### KCLCR 7 — Motion practice (the most-used local rule)

Adds to CR 7 and CR 6 the following King County specifics:

- **Confirmation of motion**: a motion must be confirmed in the
  electronic confirmation system by a deadline (typically the
  Thursday before the noted Friday hearing); an unconfirmed motion
  is automatically stricken
- **Working copies**: judges receive working copies by specific
  deadline (usually noon two days before the hearing) — current
  practice is electronic submission via the working-copies portal
- **Page limits**: motions and responses cannot exceed 12 pages
  (without leave of court); reply briefs 6 pages — **verify current
  length limits**
- **Over-length motions**: require prior leave; request via motion

### KCLCR 43 — Remote hearings

Most civil motions in King County Superior Court are heard on Zoom
by default. The local rule incorporates by reference the assigned
judge's posted Zoom ID. **Fetch the current judge-specific Zoom
details** from the judge's page on the King County Superior Court
site before finalizing a Note for Motion Docket.

### KCLCR 56 — Summary judgment

- Motion must be noted for **at least 28 calendar days** after
  service (matches CR 56(c))
- Response due **11 calendar days** before the hearing
- Reply due **5 calendar days** before the hearing
- **Confirmation** required by KCLCR 7

## KCDCLCR — King County District Court Local Civil Rules

Applies to the **King County District Court**, including divisions
at Burien (South), Redmond (East), Seattle, Maleng Regional Justice
Center. Canonical base URL (navigate to "Local Rules"):

```
https://kingcounty.gov/en/court/district-court/courts-jails-legal-system
```

The district court local rules are lighter than the superior court's
because district-court practice is more uniform (no case schedules,
simpler motion calendar). The **operational layer** for KCDC —
hearing dates, Zoom details, document codes — lives on the civil
filings page:

```
https://kingcounty.gov/en/court/district-court/courts-jails-legal-system/civil-filings
```

See `wa-kcdc/SKILL.md` for KCDC operational procedure (three-step
scheduling protocol, e-filing, courtroom assignments).

### Key KCDCLCR rules

| Rule | What it governs |
|------|-----------------|
| KCDCLCR 4 | Forms, caption, service |
| KCDCLCR 5 | Filing and service |
| KCDCLCR 7 | Motion practice — noting, confirmation |
| KCDCLCR 8 | Pleadings |
| KCDCLCR 10 | Form of papers |
| KCDCLCR 55 | Default |
| KCDCLCR 56 | Summary judgment (**some** KCDC divisions accept SJ motions; others require filing directly with the assigned judge — check the local practice for the division) |

### KCDCLCR 7 — Motion practice

Key differences from KCLCR 7:

- **Noting a hearing date** requires a **clerk-issued date**. The
  clerks email (CivilMGT@kingcounty.gov) assigns a specific date,
  time, and courtroom. Self-noted dates are rejected.
- **Two-business-day e-filing window** after the clerks' date
  assignment
- **No motion confirmation** system like KCLCR 7
- **No working copies** (practice varies by judge; most KCDC judges
  do not require courtesy copies — confirm with the assigned
  division)
- **Page limits**: generally 12 pages for motion / response, 6 for
  reply — **verify at the current civil-filings page**

### Division-level variation

Within KCDC, individual divisions may have quirks — check the
division page off the KCDC civil-filings page:

- **South Division / Burien** — civil motions typically heard via
  Zoom; Note for Motion Docket form specifies the current Zoom meeting
  ID and dial-in
- **East Division / Redmond** — similar Zoom practice
- **Seattle Division** — may mix in-person and Zoom
- **Maleng Regional Justice Center** — if any civil motions heard
  there, see the current civil-filings page

### CRLJ vs CR — common pro se trap

KCDC practice follows **CRLJ**, not CR. A pro se defendant who
reads the statewide CR will find that:

- **CRLJ 6(d)** (notice periods) has specific windows that
  sometimes differ from CR 6(d)
- **CRLJ 26(f)** is the meet-and-confer rule (CR 26(i) is superior
  court)
- **CRLJ 37(a)** corresponds to CR 37(a)
- **CRLJ 55 / 56** exist but 56 is sometimes limited in district
  court practice

When drafting for KCDC, cite **CRLJ**, not CR. See
`references/civil-rules.md`.

## Changing / renumbered rules — verification checklist

Before filing, verify:

- [ ] The KCLCR or KCDCLCR cite still exists at the current URL
- [ ] The page limit has not changed
- [ ] The confirmation deadline (for KCLCR) has not changed
- [ ] The judge-specific Zoom / chambers info is current (KCLCR)
- [ ] The CivilMGT e-mail and clerks' turnaround time are current
      (KCDCLCR operational layer)

## Interaction with statewide rules

```
                  GR 14 (format)
                        │
             ┌──────────┼───────────┐
             │                      │
         KCLCR 10              KCDCLCR 10
      (superior court       (district court
       local overlays)       local overlays)

                   CR / CRLJ
                        │
             ┌──────────┼───────────┐
             │                      │
         KCLCR 7               KCDCLCR 7
       (motion practice      (motion practice
        + confirmation         + clerks' dates
        + working copies)       + two-business-day
                                 e-filing)
```

**Rule of thumb**:

- **Format**: GR 14 first, then local overlay
- **Motion practice**: statewide first, then local overlay
- **Operational** (e-file portal, Zoom, document codes): local only

## Filing workflow cross-checks

When `wa-file-packet` assembles a motion for filing:

### Superior court (KCLCR)

- [ ] Confirmation of motion (KCLCR 7)
- [ ] Working copies to judge (KCLCR 7)
- [ ] Page limits respected (KCLCR 7)
- [ ] Format per GR 14 + KCLCR 10
- [ ] Response deadline per statewide rule (e.g., CR 56)
- [ ] Judge-specific Zoom on Note for Motion Docket

### District court (KCDCLCR)

- [ ] Clerk-issued hearing date (KCDC operational, not in KCDCLCR)
- [ ] E-filing within 2 business days (KCDC operational)
- [ ] Page limits respected (KCDCLCR 7)
- [ ] Format per GR 14 + KCDCLCR 10
- [ ] Response deadline per CRLJ 6(d) + specific rule (56, 12, etc.)
- [ ] Current-form Note for Motion Docket with Zoom / dial-in

## Fetching current text

- **KCLCR** (Superior Court):
  `https://kingcounty.gov/en/court/superior-court/courts-jails-legal-system/resources-research/local-rules`
- **KCDCLCR** (District Court): navigate from
  `https://kingcounty.gov/en/court/district-court/courts-jails-legal-system`
- **KCDC civil filings** (operational, not rules):
  `https://kingcounty.gov/en/court/district-court/courts-jails-legal-system/civil-filings`

## Notes

- Local rules change **more often** than statewide rules — always
  fetch
- If a judge's standing order conflicts with a local rule, the
  standing order usually controls (for that judge)
- Other counties (Snohomish, Pierce, etc.) have their own local
  rules; this plugin currently covers King County. For other
  counties, fetch the superior court or district court local rules
  from the county's page.
