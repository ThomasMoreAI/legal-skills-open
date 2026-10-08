# Security Policy

## Overview

Kevin is an agent skill that runs entirely within the host agent's context window. It has no external dependencies, no API keys, no network calls, and no persistent storage. No data leaves the conversation.

That said, Kevin deals with sensitive legal content, so we take security seriously.

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.0.x   | Yes       |

## Reporting a Vulnerability

If you discover a security vulnerability in Kevin, please report it responsibly.

**Do not open a public GitHub issue for security vulnerabilities.**

Instead, email **kcass16@gmail.com** with:

- A description of the vulnerability
- Steps to reproduce (if applicable)
- The potential impact
- Any suggested fixes

We will acknowledge receipt within 48 hours and provide an initial assessment within 7 days.

## Scope

Since Kevin is a skill file (markdown-based prompts and knowledge), the attack surface is limited to:

- **Prompt injection via skill content:** Malicious modifications to SKILL.md or reference files that could cause the host agent to behave unexpectedly
- **Incorrect legal guidance:** Errors in regulatory citations, contract clauses, or compliance advice that could lead users to make harmful legal decisions
- **Outdated regulatory information:** Laws change; if Kevin's knowledge base references superseded regulations, that's a security-adjacent concern

## What Is NOT in Scope

- Vulnerabilities in the host AI agent (e.g., Claude, Cursor, Codex) — report to the respective vendor
- General legal disagreements about Kevin's guidance (open a regular issue or discussion instead)

## Responsible Disclosure

We follow coordinated disclosure. If you report a vulnerability:

1. We will work with you to understand and validate the issue
2. We will develop and test a fix
3. We will credit you in the release notes (unless you prefer anonymity)
4. We will publish the fix before any public disclosure

Thank you for helping keep Kevin and its users safe.
