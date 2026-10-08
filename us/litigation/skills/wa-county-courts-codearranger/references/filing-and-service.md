# Cross-county filing, service, and working-copy checklist

What's the same in every Washington county court — use this alongside the
county-specific entry in `district-court-directory.md`, the
`wa-statewide-format` skill (GR 14), and the `wa-file-packet` skill.

## The packet (noted civil motion)

1. **Motion** — the primary relief sought.
2. **Supporting memorandum** — argument; omit if the motion is
   self-contained.
3. **Supporting declaration(s)** — facts and authenticated exhibits.
4. **Proposed order** — grants the relief; one for each motion.
5. **Note for civil motion calendar / docket** — the county's scheduling
   form. Pull the current version from that court's website; some
   multi-division courts (e.g., Snohomish) publish a division-specific
   form.
6. **Certificate / declaration of service** — date, method, and recipient
   for every document served.

E-file each component as a **separate PDF** through the county's portal
(see the directory file for which portal each county uses — LINX in
Pierce; Odyssey/JIS-based portals elsewhere).

## Service

- **District court (courts of limited jurisdiction):** serve under
  **CRLJ 5** — email (if agreed/authorized), mail, or personal service —
  the **same day** you file.
- **Superior court:** serve under **CR 5**, same-day.
- Always attach a **Certificate of Service** or **Declaration of Service**
  to the filing showing date, method, and recipient. The statewide rule
  text is in `wa-law-references/references/court-rules/`.

## Working copies

- **Superior courts** generally **require working copies** (a courtesy
  paper or electronic-bench copy delivered to the assigned department) —
  check that county's LCR for the deadline and delivery method.
- **District courts** usually do **not** require working copies for
  routine civil-docket motions, but some require them for longer motions
  — confirm with the county's LCR/LCRLJ or with chambers.

## Hearing dates and confirmation — varies; read the local rules

- Some courts let you **self-note** onto a published civil calendar;
  others require an **emailed date request to a calendar clerk first**
  (the King County District Court model — see `wa-kcdc`). The county's
  civil-calendar page and local rules say which.
- Many **superior courts** require the moving party to **confirm** a
  contested hearing a set number of court days before it, or the matter
  is struck. District courts vary.
- **Continuances/strikes:** follow the county's procedure (often an agreed
  motion and proposed order, filed before the hearing) and notify the
  other parties.

## Deadlines

Compute every deadline with **CRLJ 6** (district court) or **CR 6**
(superior court) time computation, applying the **RCW 1.16.050** legal
holidays. Use the `wa-deadlines` skill (and
`plugins/wa-court-docs/scripts/case-calendar.py`) — never eyeball it.

## Format

All filings follow **GR 14** and the statewide drafting conventions in the
`wa-statewide-format` skill, *plus* anything additional in that county's
local rules. Run `plugins/wa-court-docs/scripts/format-check.py <file>`
before filing, then `wa-quality-check`.
