---
name: slim-license
title: License Writer
description: Detect project type and add appropriate NASA/Open Source licenses
author: NASA-AMMOS
author_url: https://github.com/NASA-AMMOS/slim/tree/main/static/marketplace/skills/slim-license
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# License Writer

## Overview

This skill helps you add appropriate open source licenses to your project. It supports both standard open source licenses and NASA JPL variants with institutional copyright headers.

## When to Use This Skill

- Starting a new project that needs a license
- Converting a private project to open source
- Updating or clarifying licensing for an existing project
- Ensuring NASA/JPL compliance for government projects

## Supported Licenses

### Standard Open Source Licenses
- **Apache 2.0**: Permissive license with patent protection
- **MIT**: Simple and permissive license

### NASA JPL Variants
- **Apache 2.0 + JPL Copyright**: Apache license with Caltech/JPL institutional headers
- **MIT + JPL Copyright**: MIT license with Caltech/JPL institutional headers

## Workflow

### Step 1: Check for Existing License

First, check if a LICENSE file already exists in the repository root:

```bash
ls -la LICENSE*
```

If a license exists, ask the user if they want to replace it or keep it.

### Step 2: Determine License Type

Ask the user:
1. **Which license would you like to use?**
   - Apache 2.0 (recommended for most projects)
   - MIT (simpler, more permissive)

2. **Is this a NASA JPL project?**
   - Yes: Use JPL variant with institutional copyright
   - No: Use standard open source license

### Step 3: Select and Apply License

Based on the user's choices, copy the appropriate license file from the assets directory:

- **Apache 2.0 + JPL**: `assets/LICENSE-APACHE-JPL`
- **MIT + JPL**: `assets/LICENSE-MIT-JPL`
- **Apache 2.0**: `assets/LICENSE-APACHE`
- **MIT**: `assets/LICENSE-MIT`

Copy the selected file to the repository root as `LICENSE`:

```bash
cp assets/LICENSE-[TYPE] LICENSE
```

### Step 4: Verify and Customize

1. Open the LICENSE file
2. If using a JPL variant, verify the copyright year is current
3. If needed, update the copyright holder information
4. Confirm the license is in place

### Step 5: Update Documentation

Remind the user to:
- Add a license badge to their README.md
- Reference the license in their documentation
- Add copyright headers to source files (optional but recommended)

## Quick Reference

### License Selection Guide

**Choose Apache 2.0 when:**
- You want explicit patent protection
- Your project includes significant original code
- You're concerned about patent litigation
- Industry standard for enterprise software

**Choose MIT when:**
- You want maximum simplicity
- Your project is a small utility or library
- You want to minimize license overhead
- Compatible with virtually any other license

**Use JPL variant when:**
- Project is funded by or developed at NASA JPL
- Institutional copyright attribution is required
- Government compliance is needed

## Assets Available

- `LICENSE-APACHE`: Standard Apache 2.0 License
- `LICENSE-APACHE-JPL`: Apache 2.0 with JPL/Caltech copyright
- `LICENSE-MIT`: Standard MIT License
- `LICENSE-MIT-JPL`: MIT with JPL/Caltech copyright

## Additional Resources

- [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
- [MIT License](https://opensource.org/licenses/MIT)
- [Choose a License](https://choosealicense.com/)
