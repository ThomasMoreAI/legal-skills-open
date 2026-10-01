# LINZ Title Memorials API Notes

## Public Sources Inspected

- LINZ Data Service NZ Property Titles layer 50804: `https://data.linz.govt.nz/layer/50804-nz-property-titles/`
  - Public catalogue/API metadata is available.
  - The layer description says it provides title information excluding ownership.
  - The public fields include title metadata such as `title_no`, `status`, `type`, `land_district`, and geometry, but not memorial or instrument text.
- LINZ Data Service Landonline Title Memorials Dataset 4748: `https://data.linz.govt.nz/set/4748-landonline-title-memorials-dataset/`
  - The set contains Landonline tables for title memorial analysis, including Action, Action Type, Title Action, and Title Memorial.
- Landonline: Title Memorial table 52006: `https://data.linz.govt.nz/table/52006-landonline-title-memorial/`
  - Public metadata describes one row for each current or historical memorial for a title.
  - Fields include `ttl_title_no`, `mmt_code`, action identifiers, status fields, and current/historical flags.
- Related public Landonline table metadata:
  - Action table 51702.
  - Action Type table 51728.
  - Title Action table 52002.
  - Title Instrument table 52012.
  - Title Instrument Title table 52013.
  - Statute table 51699.
  - System Code table 51648.
- LINZ land registration guidance on Building Act 2004 instruments: `https://www.linz.govt.nz/guidance/land-registration/land-registration-guide/subdivisions/registration-under-building-act-2004`
- MBIE Natural Hazard Provisions guidance: `https://www.building.govt.nz/assets/Uploads/projects-and-consents/Planning-a-successful-build/Scope-and-design/natural-hazard-provisions-guidance.pdf`

## Privacy and Access Boundary

The relevant LDS catalogue metadata is public, and some related Landonline row tables are downloadable or queryable through LDS services. The row tables needed to compute Building Act s73/s74 counts contain or join through title numbers, instrument identifiers, action identifiers, or other property-level records.

This skill therefore does not fetch feature samples, WFS rows, Kart repositories, exports, or data-table rows from title memorial, title action, title instrument, or title/title-link tables. It only returns metadata, field names, public access flags, feature counts, and aggregate-only OIA request text.

Do not output:

- individual Records of Title
- title numbers
- owner names
- addresses
- parcel identifiers
- instrument numbers
- memorial text
- unsuppressed cells small enough to identify a property

## Why Counts Need an Official Aggregate

Counting Building Act 2004 s73 natural-hazard title entries and s74(4) removals requires more than the simplified NZ Property Titles layer. It likely needs official interpretation of Landonline memorial, action, instrument, statute, and system-code fields, plus safe grouping such as territorial authority, land district, year, or hazard type.

The keyless safe path is to request aggregate counts from LINZ with suppression for small cells and no title-level fields.
