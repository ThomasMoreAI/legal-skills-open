# CENDOJ Toolkit — Compliance Checklist

Run through this checklist BEFORE every execution to confirm compliance with CENDOJ's terms of use.

## Pre-execution checklist

- [ ] **Use case is "uso particular"**. Check at least one applies:
  - [ ] Defending my own legal case (employee/citizen looking up case law for my dispute)
  - [ ] Lawyer preparing defense for a specific client case
  - [ ] Academic research on jurisprudence (with citation, non-commercial)
  - [ ] Personal legal study or preparation
- [ ] **Use case is NOT one of**:
  - [ ] Building a commercial legal database
  - [ ] Aggregating CENDOJ content for resale or commercial AI training
  - [ ] Republishing CENDOJ content as a competing service
  - [ ] Indiscriminate bulk extraction
- [ ] **Volume**: my expected download count is ≤ 50 docs per execution (if more, I have explicit
      need and use `--force-large`, still capped at 200)
- [ ] **Rate limit**: I will use `--delay 5` (or higher), the CENDOJ `robots.txt` `Crawl-delay`. I
      will NOT lower this.
- [ ] **Honest representation**: I understand I am running an automated script. The
      `--user-agent browser` option uses a browser-like UA because CENDOJ filters generic UAs; I
      accept this is necessary for the script to function.
- [ ] **Output use**: downloaded PDFs and their markdown derivatives will be stored locally for my
      use particular only. I will NOT publish or redistribute them as a commercial dataset.

## Post-execution checklist

- [ ] Stored downloads in a directory dedicated to my specific legal case
- [ ] Inventory (INVENTARIO.md) generated with SHA-256 hashes for each PDF
- [ ] If sharing with my lawyer: confirmed they use it as part of MY case (still uso particular)
- [ ] If citing in court submissions: ECLI/ROJ references included for traceability
- [ ] Did NOT upload the downloaded content to any public repository, AI training dataset, or
      commercial database

## Reporting commercial reuse

If your use case shifts to anything commercial or large-scale, STOP using this toolkit and request
formal authorization from CGPJ:

<https://www.poderjudicial.es/cgpj/es/Servicios/Centro-de-Documentacion-Judicial>

## Self-audit

This skill creates an audit trail automatically:

- Each script prints timestamped logs to stderr
- The download script generates an INVENTARIO.md with SHA-256 hashes per PDF
- Captures of the search results JSON preserve the search criteria and results

Keep these logs alongside your downloads. If CENDOJ or CGPJ ever query your usage, the audit trail
demonstrates you operated within "uso particular" and respected the technical constraints
(`Crawl-delay`).
