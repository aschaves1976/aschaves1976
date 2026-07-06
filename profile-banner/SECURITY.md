# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

This project distributes a static SVG banner and Python build tooling. There is
no runtime server, database, or user authentication surface in the core
product.

## Reporting a Vulnerability

If you discover a security issue (for example, unsafe behavior in build
scripts, path traversal in tooling, or malicious SVG constructs), please report
it responsibly.

**Preferred contact:** open a [GitHub Security Advisory](https://github.com/OWNER/REPO/security/advisories/new)
(private) or email the maintainer if a private channel is listed in the
repository profile.

Include:

1. Description of the vulnerability
2. Steps to reproduce
3. Impact assessment
4. Suggested fix (if any)

## Response Timeline

| Stage              | Target        |
| ------------------ | ------------- |
| Acknowledgment     | 48 hours      |
| Initial assessment | 7 days        |
| Fix or mitigation  | 30 days       |

## Scope

**In scope:**

- Python tools in `tools/`
- CI workflow in `.github/workflows/`
- SVG source that could affect renderers when embedded on GitHub

**Out of scope:**

- Third-party renderer bugs (browser, GitHub CDN)
- Social engineering targeting the maintainer's personal accounts

## Policy

- Do not test against production systems without permission
- Do not publicly disclose before a fix is available
- Good-faith reports are appreciated and will be credited when desired

## Safe Usage

- Review `dist/banner.svg` before embedding in public profiles
- Run validation (`python tools/validate_svg.py`) after accepting external SVG
  contributions
- Keep Python dependencies updated when using export tooling
