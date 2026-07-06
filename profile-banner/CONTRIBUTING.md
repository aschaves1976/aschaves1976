# Contributing

Thank you for your interest in the GitHub Profile Banner project. This
repository treats the SVG as production software: every change should be
validated, documented, and consistent with the established design system.

## Before You Start

1. Read [`README.md`](README.md) for project overview
2. Review [`docs/architecture.md`](docs/architecture.md) for SVG structure
3. Review [`docs/visual-guidelines.md`](docs/visual-guidelines.md) before any visual change
4. For animations, read [`docs/animation-guidelines.md`](docs/animation-guidelines.md)

## Development Setup

```bash
# Clone the repository
git clone <repo-url>
cd profile-banner

# Validate source SVG
python tools/validate_svg.py

# Run full test suite
pip install pytest
pytest tests/ -v

# Build artifacts
python tools/build_banner.py
python tools/optimize_svg.py
```

Or use Make:

```bash
make all
```

## What to Edit

| Goal | Edit only |
|------|-----------|
| Visual content | `src/banner.svg` |
| Validation rules | `tools/lib/svg_utils.py` |
| Build pipeline | `tools/*.py` |
| Documentation | `docs/`, `README.md` |

**Never edit `dist/` manually.** Generated files are overwritten by build tools.

## Pull Request Flow

1. Fork the repository and create a feature branch (`feature/short-description`)
2. Make focused changes with a clear scope
3. Run validation and tests locally
4. Update documentation when behavior or structure changes
5. Open a Pull Request using the provided template
6. Wait for review from a maintainer

## Commit Message Convention

Use clear, imperative messages:

```
Add pulse animation to anchor nodes
Fix broken href in layer-organic-circuits
Update typography guidelines for card labels
```

Prefixes (optional but encouraged):

| Prefix | Use |
|--------|-----|
| `feat:` | New feature or visual element |
| `fix:` | Bug fix |
| `docs:` | Documentation only |
| `chore:` | Tooling, CI, housekeeping |
| `refactor:` | Internal restructure without visual change |

## Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Layer group | `layer-{name}` | `layer-typography` |
| Symbol | `{semantic-name}` | `primary-node` |
| Gradient | `{purpose}-gradient-{variant}` | `background-gradient-main` |
| Filter | `filter-{effect}` | `filter-glow-subtle` |
| Animation group | `animation-{purpose}` | `animation-pulse-group` |

## SVG Rules

1. **Single source of truth:** `src/banner.svg` only
2. **Reuse symbols:** use `<use href="#symbol-id">`; never duplicate geometry
3. **XML comments:** must not contain `--` (double hyphen); use `======` delimiters
4. **Layer responsibility:** one concern per layer; see architecture doc
5. **Animations:** SMIL only in `layer-animations`; see animation guidelines
6. **IDs:** unique across the entire document

## Adding a New Component

1. Define `<symbol id="your-symbol">` inside `<defs>`
2. Include `<title>` (and `<desc>` when helpful) inside the symbol
3. Instantiate via `<use>` in the appropriate layer
4. Document the component in `docs/design-system.md`
5. Add validation if new structural rules apply

## Adding Documentation

- Place technical docs in `docs/`
- Reflect **actual project decisions**, not generic templates
- Cross-link related documents
- Update `CHANGELOG.md` under `[Unreleased]` for user-visible changes

## Code of Conduct

This project follows the [Contributor Covenant](CODE_OF_CONDUCT.md). By
participating, you agree to uphold this code.

## Questions

Open a [Feature Request issue](.github/ISSUE_TEMPLATE/feature_request.md) for
discussions before large changes.
