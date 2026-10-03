# NOTICE File Templates

NOTICE files are required for Apache-2.0 licensed projects and recommended for attribution in any project.

---

## What is a NOTICE File?

A NOTICE file contains:
- Attribution for the project
- Attribution for third-party components
- Required legal notices from dependencies

**When Required:** Apache-2.0 Section 4(d) requires preserving NOTICE files from dependencies.

**When Recommended:** Any project using multiple open source components benefits from consolidated attribution.

---

## Basic NOTICE Template

**File:** `NOTICE` or `NOTICE.txt`

```
[PROJECT NAME]
Copyright [YEAR] [COPYRIGHT HOLDER]

This product includes software developed at
[ORGANIZATION NAME] ([ORGANIZATION URL]).
```

---

## NOTICE with Third-Party Components

```
[PROJECT NAME]
Copyright [YEAR] [COPYRIGHT HOLDER]

This product includes software developed at
[ORGANIZATION NAME] ([ORGANIZATION URL]).

=========================================================================

This product includes the following third-party components:

-------------------------------------------------------------------------
[COMPONENT NAME] ([VERSION])
-------------------------------------------------------------------------
Copyright [YEAR] [COMPONENT COPYRIGHT HOLDER]
Licensed under [LICENSE NAME]
[COMPONENT URL]

[Include any specific attribution text required by the component]

-------------------------------------------------------------------------
[NEXT COMPONENT NAME] ([VERSION])
-------------------------------------------------------------------------
Copyright [YEAR] [COMPONENT COPYRIGHT HOLDER]
Licensed under [LICENSE NAME]
[COMPONENT URL]

=========================================================================
```

---

## Example: Node.js Project NOTICE

```
My Awesome Project
Copyright 2024 Acme Corporation

This product includes software developed at
Acme Corporation (https://acme.example.com).

=========================================================================

Third-Party Components:

-------------------------------------------------------------------------
Express (4.18.2)
-------------------------------------------------------------------------
Copyright (c) 2009-2014 TJ Holowaychuk <tj@vision-media.ca>
Copyright (c) 2013-2014 Roman Shtylman <shtylman+expressjs@gmail.com>
Copyright (c) 2014-2015 Douglas Christopher Wilson <doug@somethingdoug.com>
Licensed under MIT
https://expressjs.com/

-------------------------------------------------------------------------
Lodash (4.17.21)
-------------------------------------------------------------------------
Copyright OpenJS Foundation and other contributors <https://openjsf.org/>
Based on Underscore.js, copyright Jeremy Ashkenas,
DocumentCloud and Investigative Reporters & Editors <http://underscorejs.org/>
Licensed under MIT
https://lodash.com/

-------------------------------------------------------------------------
Apache Commons Lang (3.12.0)
-------------------------------------------------------------------------
Apache Commons Lang
Copyright 2001-2023 The Apache Software Foundation

This product includes software developed at
The Apache Software Foundation (https://www.apache.org/).
Licensed under Apache-2.0
https://commons.apache.org/proper/commons-lang/

=========================================================================
```

---

## Example: Apache-2.0 Project NOTICE

```
Apache Kafka
Copyright 2024 The Apache Software Foundation

This product includes software developed at
The Apache Software Foundation (https://www.apache.org/).

=========================================================================

This product includes code from the following Apache projects:

* Apache ZooKeeper
* Apache Commons
* Apache Log4j2

This product includes code licensed from Confluent, Inc. under the
Apache License 2.0.

This product includes code from LZ4 (https://github.com/lz4/lz4-java),
licensed under the Apache License 2.0.

This product includes code from Snappy (https://github.com/xerial/snappy-java),
licensed under the Apache License 2.0.

=========================================================================
```

---

## Aggregating NOTICE Files

When your project uses Apache-licensed dependencies, you must include their NOTICE content:

### Process

1. Find all Apache-2.0 licensed dependencies
2. Check each for a NOTICE file
3. Include relevant portions in your NOTICE
4. Preserve original attribution text

### Script to Find NOTICE Files (Node.js)

```bash
# Find NOTICE files in node_modules
find node_modules -name "NOTICE*" -type f 2>/dev/null
```

### Script to Find NOTICE Files (Python)

```bash
# Find NOTICE files in site-packages
find $(python -c "import site; print(site.getsitepackages()[0])") \
  -name "NOTICE*" -type f 2>/dev/null
```

---

## THIRD-PARTY-LICENSES File

For comprehensive attribution, some projects use a separate file:

**File:** `THIRD-PARTY-LICENSES` or `THIRD-PARTY-LICENSES.txt`

```
Third-Party Licenses
====================

This file lists licenses for third-party software included in this project.

================================================================================
Package: [package-name]
Version: [version]
License: [SPDX-identifier]
URL: [package-url]
================================================================================

[FULL LICENSE TEXT FOR THIS PACKAGE]

================================================================================
Package: [next-package]
...
================================================================================
```

---

## Attribution in User Interfaces

For applications with UI, include attribution in "About" or "Legal" screens:

### Mobile App Example

```
Open Source Licenses

This application uses the following open source software:

• React Native (MIT)
  Copyright (c) Meta Platforms, Inc. and affiliates.

• Lodash (MIT)
  Copyright OpenJS Foundation and other contributors.

• Moment.js (MIT)
  Copyright (c) JS Foundation and other contributors.

[View full license texts]
```

### Web Application Example

```html
<!-- In your footer or dedicated page -->
<footer>
  <a href="/licenses">Open Source Licenses</a>
</footer>

<!-- /licenses page -->
<h1>Open Source Software</h1>
<p>This application uses the following open source components:</p>
<ul>
  <li><strong>React</strong> - MIT License - Copyright (c) Meta Platforms, Inc.</li>
  <li><strong>Express</strong> - MIT License - Copyright (c) Express Contributors</li>
  <!-- ... -->
</ul>
```

---

## Generating Attribution Automatically

### Node.js: license-checker

```bash
npx license-checker --production --csv > third-party-licenses.csv
npx license-checker --production --out licenses.json
```

### Python: pip-licenses

```bash
pip-licenses --format=markdown --output-file=THIRD-PARTY-LICENSES.md
pip-licenses --format=json --output-file=licenses.json
```

### Go: go-licenses

```bash
go-licenses csv ./... > third-party-licenses.csv
go-licenses save ./... --save_path=./third-party-licenses
```

---

## Legal Notice Requirements by License

| License | NOTICE Required | Attribution Required |
|---------|----------------|---------------------|
| MIT | No | Yes (copyright notice) |
| Apache-2.0 | Yes (if exists) | Yes |
| BSD-3-Clause | No | Yes (copyright notice) |
| GPL-3.0 | No | Yes (copyright + license) |
| LGPL-3.0 | No | Yes (copyright + license) |
| MPL-2.0 | No | Yes (per file) |
