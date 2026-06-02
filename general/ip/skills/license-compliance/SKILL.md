---
name: license-compliance
title: Open Source License Compliance
description: Open source license compliance including compatibility analysis, obligations tracking, and compliance workflows
author: melodic-software
author_url: https://github.com/melodic-software/claude-code-plugins/tree/main/plugins/compliance-planning/skills/license-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# Open Source License Compliance

Comprehensive guidance for open source license compliance before and during development.

## When to Use This Skill

- Evaluating open source dependencies for new projects
- Checking license compatibility between packages
- Understanding obligations for distribution
- Creating attribution notices and NOTICES files
- Establishing license policies for your organization

## License Categories

### Permissive Licenses

Allow use, modification, and distribution with minimal restrictions.

| License | Obligations | Commercial Use | Patent Grant |
|---------|-------------|----------------|--------------|
| **MIT** | Attribution | ✓ | No |
| **BSD-2-Clause** | Attribution | ✓ | No |
| **BSD-3-Clause** | Attribution, no endorsement | ✓ | No |
| **Apache-2.0** | Attribution, state changes, NOTICE | ✓ | Yes |
| **ISC** | Attribution | ✓ | No |

### Copyleft Licenses

Require derivative works to use the same license.

| License | Copyleft Scope | SaaS Trigger | Distribution Obligations |
|---------|---------------|--------------|-------------------------|
| **GPL-2.0** | Strong | No | Source disclosure |
| **GPL-3.0** | Strong | No | Source disclosure, anti-Tivoization |
| **LGPL-2.1** | Weak (library) | No | Source for library, linking allowed |
| **AGPL-3.0** | Strong + Network | Yes | Source disclosure on network use |
| **MPL-2.0** | File-level | No | Source for modified files |
| **EPL-2.0** | Module-level | No | Source for modified modules |

### Weak Copyleft vs Strong Copyleft

```text
Strong Copyleft (GPL):
┌──────────────────────────────────────────┐
│  Your Application (becomes GPL)          │
│  ┌──────────────────────────────────┐   │
│  │  GPL Library (linked/included)   │   │
│  └──────────────────────────────────┘   │
└──────────────────────────────────────────┘

Weak Copyleft (LGPL):
┌──────────────────────────────────────────┐
│  Your Application (any license)          │
│  ↓ dynamic link                          │
│  ┌──────────────────────────────────┐   │
│  │  LGPL Library (LGPL remains)     │   │
│  └──────────────────────────────────┘   │
└──────────────────────────────────────────┘
```

## License Compatibility

### Compatibility Matrix

```text
Inbound License → Outbound License Compatibility

FROM ↓ / TO →  | MIT | Apache | BSD | LGPL | MPL | GPL | AGPL
---------------|-----|--------|-----|------|-----|-----|------
MIT            |  ✓  |   ✓    |  ✓  |  ✓   |  ✓  |  ✓  |  ✓
Apache-2.0     |  ✗  |   ✓    |  ✗  |  ✓   |  ✓  |  ✓* |  ✓*
BSD-3-Clause   |  ✓  |   ✓    |  ✓  |  ✓   |  ✓  |  ✓  |  ✓
LGPL-2.1       |  ✗  |   ✗    |  ✗  |  ✓   |  ✗  |  ✓  |  ✓
MPL-2.0        |  ✗  |   ✗    |  ✗  |  ✗   |  ✓  |  ✓  |  ✓
GPL-2.0        |  ✗  |   ✗    |  ✗  |  ✗   |  ✗  |  ✓  |  ✗
GPL-3.0        |  ✗  |   ✗    |  ✗  |  ✗   |  ✗  |  ✓  |  ✓
AGPL-3.0       |  ✗  |   ✗    |  ✗  |  ✗   |  ✗  |  ✗  |  ✓

✓ = Compatible, ✗ = Incompatible
* GPL-3.0 only (Apache-2.0 incompatible with GPL-2.0)
```

### Common Compatibility Issues

| Issue | Example | Resolution |
|-------|---------|------------|
| GPL + Proprietary | Using GPL library in closed source | Use LGPL alternative or open source |
| Apache + GPL-2.0 | Combining Apache-2.0 with GPL-2.0 | Upgrade to GPL-3.0 |
| AGPL + SaaS | Using AGPL in web service | Open source your code or use alternative |
| Conflicting Copyleft | GPL + EPL in same binary | Separate into distinct programs |

## Obligation Analysis by Use Case

### Internal Use Only

| License Type | Obligations | Tracking Required |
|--------------|-------------|-------------------|
| Permissive | None | Minimal |
| Weak Copyleft | None | Minimal |
| Strong Copyleft | None (no distribution) | Minimal |
| AGPL | Source available if network service | Yes |

### Distribution (Desktop/Mobile)

| License Type | Obligations |
|--------------|-------------|
| MIT, BSD, ISC | Include license/copyright in distribution |
| Apache-2.0 | Include license, NOTICE file, state changes |
| LGPL | Provide library source, allow relinking |
| GPL | Provide complete source code |
| MPL | Provide modified file source |

### SaaS (No Binary Distribution)

| License Type | Obligations |
|--------------|-------------|
| Permissive | None (no distribution) |
| GPL, LGPL | None (no distribution) |
| AGPL | **Must provide source to users** |

## License Compliance Implementation

### .NET Dependency Analysis

```csharp
// License scanning integration
public class LicenseComplianceChecker
{
    private readonly IPackageMetadataProvider _packageProvider;
    private readonly LicensePolicy _policy;

    public async Task<ComplianceReport> AnalyzeProject(
        string projectPath,
        CancellationToken ct)
    {
        var packages = await _packageProvider.GetPackages(projectPath, ct);
        var report = new ComplianceReport();

        foreach (var package in packages)
        {
            var license = await _packageProvider.GetLicense(package, ct);

            var evaluation = _policy.Evaluate(license);

            report.Packages.Add(new PackageLicenseInfo
            {
                PackageId = package.Id,
                Version = package.Version,
                License = license.SpdxIdentifier,
                LicenseUrl = license.Url,
                Category = license.Category,
                Status = evaluation.Status,
                Obligations = evaluation.Obligations,
                Issues = evaluation.Issues
            });
        }

        return report;
    }
}

public class LicensePolicy
{
    private readonly HashSet<string> _approved = new()
    {
        "MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC"
    };

    private readonly HashSet<string> _requiresReview = new()
    {
        "LGPL-2.1", "LGPL-3.0", "MPL-2.0", "EPL-2.0"
    };

    private readonly HashSet<string> _prohibited = new()
    {
        "GPL-2.0", "GPL-3.0", "AGPL-3.0"
    };

    public PolicyEvaluation Evaluate(LicenseInfo license)
    {
        if (_approved.Contains(license.SpdxIdentifier))
        {
            return new PolicyEvaluation
            {
                Status = PolicyStatus.Approved,
                Obligations = GetObligations(license.SpdxIdentifier)
            };
        }

        if (_requiresReview.Contains(license.SpdxIdentifier))
        {
            return new PolicyEvaluation
            {
                Status = PolicyStatus.RequiresReview,
                Obligations = GetObligations(license.SpdxIdentifier),
                Issues = new[] { "Copyleft license requires legal review" }
            };
        }

        if (_prohibited.Contains(license.SpdxIdentifier))
        {
            return new PolicyEvaluation
            {
                Status = PolicyStatus.Prohibited,
                Issues = new[] { "Strong copyleft incompatible with proprietary distribution" }
            };
        }

        return new PolicyEvaluation
        {
            Status = PolicyStatus.Unknown,
            Issues = new[] { $"Unknown license: {license.SpdxIdentifier}" }
        };
    }
}
```

### Attribution and NOTICE Files

```csharp
// NOTICE file generator
public class NoticeFileGenerator
{
    public string GenerateNotice(IEnumerable<PackageLicenseInfo> packages)
    {
        var sb = new StringBuilder();

        sb.AppendLine("THIRD-PARTY SOFTWARE NOTICES AND INFORMATION");
        sb.AppendLine("=============================================");
        sb.AppendLine();
        sb.AppendLine("This software includes the following third-party components:");
        sb.AppendLine();

        foreach (var pkg in packages.OrderBy(p => p.PackageId))
        {
            sb.AppendLine($"## {pkg.PackageId} ({pkg.Version})");
            sb.AppendLine($"License: {pkg.License}");
            sb.AppendLine($"URL: {pkg.LicenseUrl}");
            sb.AppendLine();

            if (!string.IsNullOrEmpty(pkg.Copyright))
            {
                sb.AppendLine(pkg.Copyright);
                sb.AppendLine();
            }

            if (!string.IsNullOrEmpty(pkg.LicenseText))
            {
                sb.AppendLine("License Text:");
                sb.AppendLine(pkg.LicenseText);
                sb.AppendLine();
            }

            sb.AppendLine("---");
            sb.AppendLine();
        }

        return sb.ToString();
    }
}
```

### .NET Project Configuration

```xml
<!-- Enable license metadata in build -->
<PropertyGroup>
  <GeneratePackageOnBuild>true</GeneratePackageOnBuild>
</PropertyGroup>

<ItemGroup>
  <!-- Include NOTICE file in package -->
  <None Include="NOTICE.txt" Pack="true" PackagePath="" />

  <!-- Set license expression for your package -->
  <PackageLicenseExpression>MIT</PackageLicenseExpression>
  <!-- OR for file-based license -->
  <PackageLicenseFile>LICENSE.txt</PackageLicenseFile>
</ItemGroup>
```

## License Policy Template

### Organizational License Policy

```markdown
# Open Source License Policy

## 1. Purpose
This policy governs the use of open source software in [Organization] products.

## 2. License Categories

### 2.1 Approved Licenses (No Review Required)
- MIT
- Apache-2.0
- BSD-2-Clause
- BSD-3-Clause
- ISC
- Unlicense
- CC0-1.0

### 2.2 Requires Review
- LGPL-2.1, LGPL-3.0 (weak copyleft - usage context matters)
- MPL-2.0, EPL-2.0 (file/module-level copyleft)
- Creative Commons (varies by type)
- Dual-licensed packages

### 2.3 Prohibited
- GPL-2.0, GPL-3.0 (strong copyleft - unless project is GPL)
- AGPL-3.0 (network copyleft)
- SSPL (Server Side Public License)
- Any license with field-of-use restrictions
- Unknown or custom licenses without legal review

## 3. Process

### 3.1 New Dependency Addition
1. Check license using `dotnet-license-check` or equivalent
2. If Approved: Proceed, ensure attribution
3. If Requires Review: Submit to legal@company.com
4. If Prohibited: Find alternative or request exception

### 3.2 Distribution
Before any release:
1. Run license audit
2. Generate NOTICE file
3. Include required attribution
4. Archive source code for copyleft compliance

## 4. Exceptions
Exceptions require written approval from Legal and CTO.

## 5. Compliance Verification
- Automated scanning in CI/CD pipeline
- Quarterly manual audits
- Annual policy review
```

## SPDX Identifiers

### Common SPDX Identifiers

```text
Permissive:
MIT, Apache-2.0, BSD-2-Clause, BSD-3-Clause, ISC, Unlicense, CC0-1.0

Weak Copyleft:
LGPL-2.1-only, LGPL-2.1-or-later, LGPL-3.0-only, LGPL-3.0-or-later
MPL-2.0, EPL-2.0, OSL-3.0

Strong Copyleft:
GPL-2.0-only, GPL-2.0-or-later, GPL-3.0-only, GPL-3.0-or-later
AGPL-3.0-only, AGPL-3.0-or-later

Compound Expressions:
(MIT OR Apache-2.0)  - Choice
(LGPL-2.1-only AND MIT)  - Both apply
GPL-2.0-only WITH Classpath-exception-2.0  - Exception
```

## CI/CD Integration

### License Scanning Pipeline

```yaml
# GitHub Actions example
name: License Compliance Check

on:
  pull_request:
    paths:
      - '**/*.csproj'
      - '**/packages.lock.json'

jobs:
  license-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5

      - name: Setup .NET
        uses: actions/setup-dotnet@v4
        with:
          dotnet-version: '10.0.x'

      - name: Install license checker
        run: dotnet tool install --global dotnet-project-licenses

      - name: Check licenses
        run: |
          dotnet-project-licenses -i . \
            --allowed-license-types "MIT;Apache-2.0;BSD-2-Clause;BSD-3-Clause" \
            --output license-report.json \
            --output-type json

      - name: Upload license report
        uses: actions/upload-artifact@v4
        with:
          name: license-report
          path: license-report.json

      - name: Fail on prohibited licenses
        run: |
          if grep -q "GPL-" license-report.json; then
            echo "::error::Prohibited license detected"
            exit 1
          fi
```

## License Compliance Checklist

### Pre-Development

- [ ] Define license policy for project
- [ ] Identify project distribution model (SaaS/desktop/library)
- [ ] Determine outbound license for your code
- [ ] Establish dependency review process

### During Development

- [ ] Check license before adding each dependency
- [ ] Maintain attribution in NOTICE file
- [ ] Document any exceptions
- [ ] Run license scanning in CI

### Pre-Release

- [ ] Complete license audit
- [ ] Generate final NOTICE file
- [ ] Verify all attributions included
- [ ] Archive source for copyleft compliance
- [ ] Legal sign-off if required

## Cross-References

- **SBOM**: `sbom-management` for dependency tracking
- **Security**: `security-frameworks` for secure supply chain
- **Data Privacy**: Consider data handling in dependencies

## Resources

- [SPDX License List](https://spdx.org/licenses/)
- [Choose A License](https://choosealicense.com/)
- [FOSSA - License Compliance](https://fossa.com/)
- [OSI Approved Licenses](https://opensource.org/licenses/)
