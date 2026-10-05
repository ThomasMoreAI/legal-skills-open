# E-Discovery Production Specifications

## Overview

Production specifications define the technical format for exchanging documents in litigation. Standardized specifications reduce disputes and ensure usability of produced materials.

## Standard Production Formats

### TIFF Production (Most Common)

**Image Specifications:**
- Format: Single-page TIFF (Group IV)
- Resolution: 300 DPI minimum
- Color: Black and white (color for specific document types)
- Page Size: 8.5" x 11" standard; larger as needed
- Orientation: Maintain original orientation

**File Naming Convention:**
```
[PREFIX][BATES NUMBER].[EXTENSION]
Example: ABC0000001.tif

Multi-page documents:
ABC0000001.tif (page 1)
ABC0000002.tif (page 2)
ABC0000003.tif (page 3)
```

### Native Production

**When to Produce Natively:**
- Spreadsheets (Excel) - formulas and multiple tabs
- Presentations (PowerPoint) - animations and embedded content
- Databases and structured data
- Audio and video files
- CAD drawings and technical files

**File Naming Convention:**
```
[BATES START]-[BATES END]_[ORIGINAL FILENAME]
Example: ABC0001000-ABC0001000_Budget_2024.xlsx
```

### PDF Production

**Specifications:**
- Format: PDF/A (archival format) preferred
- Searchable: OCR text layer required
- Bookmarks: Preserve document structure
- Native PDFs: Maintain original format

## Load File Specifications

### Concordance/Relativity DAT File

**Format:** ASCII delimited text file

**Delimiters:**
- Field separator: ¶ (ASCII 020, Paragraph)
- Text qualifier: þ (ASCII 254, Thorn)
- Newline within field: ® (ASCII 174)

**Standard Fields:**

| Field Name | Description | Example |
|------------|-------------|---------|
| BEGBATES | First Bates number | ABC0000001 |
| ENDBATES | Last Bates number | ABC0000003 |
| BEGATTACH | First Bates of attachment range | ABC0000001 |
| ENDATTACH | Last Bates of attachment range | ABC0000010 |
| CUSTODIAN | Document source/custodian | John Smith |
| FROM | Email sender | john@company.com |
| TO | Email recipients | jane@company.com |
| CC | Carbon copy recipients | bob@company.com |
| BCC | Blind copy recipients | hidden@company.com |
| SUBJECT | Email subject line | RE: Contract Discussion |
| DATESENT | Date email sent | 01/15/2024 |
| TIMESENT | Time email sent | 09:30:00 |
| DATERECEIVED | Date email received | 01/15/2024 |
| FILENAME | Original file name | Contract_Draft.docx |
| FILEPATH | Original file path | C:\Users\John\Documents |
| FILEEXT | File extension | docx |
| AUTHOR | Document author | John Smith |
| DATECREATED | Date created | 01/10/2024 |
| DATELASTMOD | Date last modified | 01/14/2024 |
| TITLE | Document title | Draft Agreement |
| PGCOUNT | Page count | 3 |
| DOCTYPE | Document type | Email |
| CONFIDENTIALITY | Confidentiality designation | CONFIDENTIAL |
| REDACTED | Redaction indicator | Y/N |
| NATIVELINK | Path to native file | .\NATIVES\ABC0001000.xlsx |
| TEXTPATH | Path to extracted text | .\TEXT\ABC0000001.txt |
| HASH | MD5 or SHA hash value | a1b2c3d4e5f6... |

**Sample DAT File:**
```
þBEGBATESþ¶þENDBATESþ¶þCUSTODIANþ¶þFROMþ¶þTOþ¶þSUBJECTþ¶þDATESENTþ
þABC0000001þ¶þABC0000003þ¶þJohn Smithþ¶þjohn@company.comþ¶þjane@company.comþ¶þRE: Contract Discussionþ¶þ01/15/2024þ
```

### Opticon OPT File (Image Cross-Reference)

**Format:** Comma-delimited

**Fields:**
1. BATES Number
2. Volume Name
3. Image Path
4. Document Break (Y/N)
5. Box/Folder (optional)
6. Page Count (optional)

**Sample OPT File:**
```
ABC0000001,001,IMAGES\0001\ABC0000001.tif,Y,,3
ABC0000002,001,IMAGES\0001\ABC0000002.tif,,,
ABC0000003,001,IMAGES\0001\ABC0000003.tif,,,
ABC0000004,001,IMAGES\0001\ABC0000004.tif,Y,,1
```

## Bates Numbering Standards

### Numbering Format

**Standard Format:**
```
[PREFIX][SEQUENTIAL NUMBER]
Examples:
- ABC0000001 (8 digits)
- DEFENDANT-00000001 (hyphenated)
- XYZ_0000001 (underscored)
```

**Best Practices:**
- Use consistent prefix throughout production
- Sufficient digits for anticipated volume (usually 7-9)
- No special characters except hyphen or underscore
- Sequential numbering (no gaps)

### Bates Stamp Placement

**Image Position:**
- Bottom right corner preferred
- Minimum 0.25" from edges
- Font: Arial or Courier, 10-12pt
- Color: Black text, may use gray background

**Native Files:**
- Bates reference in load file
- Placeholder slip sheets in image set
- Bates range in file name

### Attachment Handling

**Family Grouping:**
```
Parent Email:    ABC0000001-ABC0000003
Attachment 1:    ABC0000004-ABC0000010
Attachment 2:    ABC0000011-ABC0000015

BEGATTACH: ABC0000001
ENDATTACH: ABC0000015
```

## Metadata Standards

### Email Metadata

| Field | Source | Notes |
|-------|--------|-------|
| From | Header | Display name and address |
| To | Header | All recipients |
| CC | Header | All CC recipients |
| BCC | Header | If available |
| Subject | Header | Full subject line |
| Date Sent | Header | Date/time with timezone |
| Date Received | Header | Date/time with timezone |
| Importance | Header | High/Normal/Low |
| Attachments | Email | Count and names |
| Message ID | Header | Unique identifier |
| Conversation ID | Header | Thread identifier |

### Document Metadata

| Field | Source | Notes |
|-------|--------|-------|
| File Name | File system | Original name |
| File Path | File system | Original location |
| File Size | File system | In bytes |
| Date Created | File system | Creation date |
| Date Modified | File system | Last modified |
| Date Accessed | File system | Last accessed |
| Author | Application | Document author |
| Last Author | Application | Last modifier |
| Title | Application | Document title |
| Subject | Application | Document subject |
| Keywords | Application | Document keywords |
| Comments | Application | Document comments |
| MD5 Hash | Calculated | Integrity verification |

## Quality Control Specifications

### Pre-Production QC Checklist

```
IMAGE QC
[ ] All images render correctly
[ ] Bates numbers sequential
[ ] Bates stamps legible
[ ] Page orientation correct
[ ] Resolution meets specifications
[ ] Color applied where appropriate
[ ] Redactions applied correctly
[ ] Confidentiality stamps present

LOAD FILE QC
[ ] All Bates numbers present
[ ] Metadata fields populated
[ ] Date formats consistent
[ ] Delimiters correct
[ ] No encoding errors
[ ] Family relationships intact
[ ] Native links valid
[ ] Text file links valid

NATIVE FILE QC
[ ] Files open correctly
[ ] Naming convention followed
[ ] Hash values match
[ ] No password protection (or password provided)
[ ] Macros removed (if required)
[ ] Links preserved (if appropriate)

EXTRACTED TEXT QC
[ ] Text files present for all docs
[ ] OCR quality acceptable
[ ] Encoding consistent (UTF-8)
[ ] Redacted text removed
```

### Production Inventory

```
PRODUCTION SUMMARY

Production Volume: PROD001
Production Date: [Date]
Bates Range: ABC0000001 - ABC0050000
Document Count: 12,500
Image Count: 50,000
Native File Count: 250
Total Size: 15.2 GB

Contents:
- IMAGES folder (TIFF files)
- NATIVES folder (Native files)
- TEXT folder (Extracted text)
- DATA folder (Load files)
  - Production.dat
  - Production.opt
- README.txt (Production guide)

Confidentiality Designations:
- Confidential: 8,500 docs
- Highly Confidential - AEO: 2,000 docs
- Not Designated: 2,000 docs
```

## Delivery Specifications

### Media

**Electronic Transfer:**
- Secure FTP (SFTP)
- Cloud transfer (Relativity Transfer, etc.)
- Encrypted USB drives
- Encrypted hard drives

**Physical Media:**
- Hard drives (formatted ExFAT or NTFS)
- USB drives (32GB+)
- No optical media (CDs/DVDs)

### Encryption

- AES-256 encryption for transfer
- Password provided separately
- Chain of custody documentation

### Documentation

Each production should include:
1. Cover letter with bates range and counts
2. Production inventory/summary
3. Technical specifications used
4. Password for encrypted media
5. Exception log (if any issues)
6. Confidentiality log (by designation)
