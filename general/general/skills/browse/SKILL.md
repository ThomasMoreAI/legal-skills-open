---
name: browse
title: Browse — Document Extraction & Web Research
description: 'Web browsing for legal work: extract contracts from portals, navigate legal research sites, pull documents from cloud storage, capture evidence screenshots.'
author: eigenlegal
author_url: https://github.com/eigenlegal/counsel-os/tree/main/skills/browse
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Browse — Document Extraction & Web Research

You are using a headless browser to access web resources for legal work. This skill enables extracting contracts from data rooms, navigating legal research sites, pulling documents from cloud storage web interfaces, and capturing screenshots as evidence.

## Use Cases

- **Data room extraction:** Pull contracts and exhibits from virtual data rooms (Intralinks, Datasite, Box, etc.)
- **Legal research:** Navigate case law databases, regulatory agency sites, corporate registries
- **Cloud storage access:** Download documents from Google Drive, SharePoint, Dropbox web interfaces
- **Portal navigation:** Access client portals, filing systems, government databases
- **Evidence capture:** Take full-page screenshots of web pages for litigation or compliance purposes
- **Contract import:** Extract agreement text from web-based contract management platforms

## Setup

The browse binary must be built first. If it hasn't been built:

```bash
cd [counsel-os directory]
bun install
bun run build
```

Install the Playwright browser if it has not been installed yet:
```bash
bunx playwright install chromium
```

## Finding the Binary

The helper script `browse/bin/find-browse` locates the browse binary. The binary can be at:
1. `browse/dist/browse` (compiled binary)
2. The active plugin root's `browse/dist/browse`
3. `~/counsel-os/browse/dist/browse`

## Command Reference

### Navigation

#### `goto <url>`
Navigate to a URL. Waits for DOM content to load.
```
goto https://dataroom.example.com/deal/project-alpha
```

#### `back` / `forward`
Navigate browser history.

#### `reload`
Reload the current page.

### Content Extraction

#### `text`
Extract all visible text from the current page. Use this to read contracts, agreements, and other documents displayed in web interfaces.
```
text
```
Returns the full text content of the page, stripped of HTML tags and navigation elements.

#### `snapshot`
Take an accessibility snapshot of the page. This returns structured page content with `@e1`, `@e2`, etc. refs for interaction.
```
snapshot
```

#### `links`
List all links on the current page with their text and URLs. Useful for navigating document indexes and data room file trees.
```
links
```

### Interaction

#### `click <element>`
Click an element. Use a CSS selector or an `@e`/`@c` ref from `snapshot`; plain visible text is not a selector.
```
snapshot
click @e3
click "button.download"
```

#### `fill <element> <value>`
Fill in a form field. Use a CSS selector or an `@e`/`@c` ref from `snapshot`.
```
fill @e4 "Master Services Agreement"
fill "input[name=email]" "user@example.com"
```

#### `select <element> <value>`
Select an option from a dropdown.
```
select @e5 "Contracts"
select "select[name=documentType]" "Contracts"
```

#### `hover <element>`
Hover over an element to reveal tooltips or dropdown menus.

#### `scroll [selector]`
Scroll to the bottom of the page, or scroll a specific selector/ref into view.
```
scroll
scroll @e12
```

### Screenshots & Evidence

#### `screenshot [filename]`
Take a screenshot of the current page. Use for evidence capture, documenting web page states, or recording counterparty portal content.
```
screenshot                           # saves /tmp/browse-screenshot.png
screenshot "/tmp/data-room-index.png"
```

Screenshots are full-page captures. Custom paths must be under `/tmp` or the current working directory.

#### Annotated screenshot
Use `snapshot -a` to create an annotated screenshot with ref labels.
```
snapshot -a -o /tmp/browse-annotated.png
```

### Advanced

#### `js <code>`
Execute JavaScript on the page. Use for extracting structured data, interacting with complex web apps, or working around non-standard interfaces.
```
js document.querySelectorAll('.contract-clause').forEach(c => console.log(c.textContent))
js document.title
```

#### `console`
Show the browser's console output. Useful for debugging JavaScript interactions.

#### `network`
Show recent network requests. Useful for finding API endpoints that serve document content directly.
```
network
```

#### `viewport <WxH>`
Set the viewport size. Useful when sites render differently on mobile/desktop.
```
viewport 1920x1080
viewport 375x812
```

#### `responsive [prefix]`
Capture mobile, tablet, and desktop screenshots.
```
responsive /tmp/browse-responsive
```

#### `diff`
Compare the current page state against the previous snapshot. Shows what changed after an interaction.

### Tab Management

#### `tabs`
List all open tabs.

#### `tab <index>`
Switch to a specific tab by index.

#### `newtab <url>`
Open a URL in a new tab.

#### `closetab`
Close the current tab.

### Cookie & Authentication

#### `cookie-import <file>`
Import cookies from a JSON file. Use this to access authenticated portals and data rooms without re-entering credentials.
```
cookie-import /tmp/dataroom-cookies.json
```

**Important for legal work:** Many data rooms and client portals require authentication. Cookie JSON paths must be under `/tmp` or the current working directory. For local Chromium browsers, prefer `cookie-import-browser`.

#### `cookie-import-browser [browser] [--domain <domain>]`
Import cookies from a supported local Chromium browser, either through the picker UI or directly for a domain.
```
cookie-import-browser chrome --domain docusign.com
```

### Chaining Commands

#### `chain`
Execute multiple commands in sequence. `chain` reads a JSON array from stdin.
```
echo '[["goto","https://dataroom.example.com"],["snapshot"],["text"]]' | browse chain
```

## Common Workflows

### Extract a Contract from a Data Room

```
1. cookie-import /tmp/dataroom-cookies.json
2. goto https://dataroom.intralinks.com/deal/12345
3. snapshot                                          # see the page structure
4. click @e3                                         # navigate to documents
5. click @e7                                         # find the right folder
6. links                                             # list available documents
7. click @e12                                        # open the document
8. text                                              # extract the text
```

### Research a Legal Question

```
1. goto https://www.law.cornell.edu/uscode/text/15/chapter-2A
2. text                                              # read the statute
3. screenshot "ftc-act-section-5.png"                # capture for reference
```

### Capture Evidence Screenshot

```
1. goto https://counterparty-website.com/terms-of-service
2. screenshot "/tmp/counterparty-tos-2026-03-13.png"
3. text                                              # extract text for analysis
```

### Download from Cloud Storage

```
1. cookie-import /tmp/google-drive-cookies.json
2. goto https://drive.google.com/drive/folders/abc123
3. links                                             # list files
4. snapshot                                          # get fresh refs
5. click @e8                                         # navigate to folder
6. click @e14                                        # select file
7. click @e20                                        # trigger download
```

## Security Notes

- **Cookie files contain credentials.** Store them securely and do not commit them to git.
- **Data room content is confidential.** Extracted text should be treated with the same confidentiality as the original document.
- **Screenshots may contain privileged information.** Label and store them appropriately.
- **Session cookies expire.** If access fails, re-export fresh cookies from your browser.
