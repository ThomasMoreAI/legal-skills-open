# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in Panya-AI, please report it responsibly.

### How to Report

1. **DO NOT** open a public GitHub issue
2. Email: siriwat@panya-ai.co.th
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

### Response Timeline

- **Acknowledgment**: Within 48 hours
- **Initial Assessment**: Within 5 business days
- **Fix Release**: Within 30 days (severity dependent)

## Security Measures

This project implements the following security practices:

- **Secret Scanning**: Gitleaks runs on every push and PR
- **Code Analysis**: SonarCloud + CodeQL scan for vulnerabilities
- **Dependency Updates**: Dependabot monitors for vulnerable dependencies
- **Environment Variables**: All secrets stored in GitHub Secrets / Vercel env vars
- **No Hardcoded Credentials**: Database URLs, API keys, and tokens are loaded from environment variables

## Supported Versions

| Version | Supported |
|---------|-----------|
| main    | ✅        |
| other   | ❌        |

## Responsible Disclosure

We appreciate responsible disclosure and will credit researchers who report vulnerabilities (unless they prefer to remain anonymous).
