# Coding Standards

Engineering conventions for SVG source and Python tooling.

## SVG Source (`src/banner.svg`)

### Structure

1. One file, one responsibility per layer
2. Section comments before every major block
3. Metadata header after `<svg>` opening
4. `<defs>` before any visible layers
5. Footer comment at end of document

### Comments

```xml
<!-- ====================================================== -->
<!-- SECTION NAME                                           -->
<!-- Objective     : Single line description                -->
<!-- Responsibility: What this block owns                     -->
<!-- ====================================================== -->
```

**Critical:** never use `--` inside XML comments.

### IDs

- Unique across entire document
- kebab-case: `main-title`, `circuit-layer-primary`
- Semantic, not positional: prefer `primary-node` over `node-1`

### Symbols and Use

```xml
<!-- Define once -->
<symbol id="primary-node" viewBox="0 0 16 16">
  <title>Primary circuit node</title>
  ...
</symbol>

<!-- Instantiate many times -->
<use href="#primary-node" x="111" y="194" width="16" height="16"/>
```

Never copy-paste circle/rect definitions for reusable elements.

### References

- Internal links: `href="#id"` or `url(#id)`
- All references must resolve (validated by `svg_utils.py`)

### Animations

- SMIL only: `<animate>`, `<animateTransform>`, `<animateMotion>`, `<set>`
- No JavaScript, no external CSS for motion
- All animation groups in `layer-animations`
- See [animation-guidelines.md](animation-guidelines.md)

### Accessibility

Required on root `<svg>`:

```xml
role="img"
aria-label="Descriptive label"
```

Required children:

```xml
<title>Short title</title>
<desc>Longer description for screen readers</desc>
```

Decorative elements: `aria-hidden="true"`.

### Typography

- Prefer inline `font-*` attributes in layer 06
- Use `<tspan dx>` for optical kerning, not manual x offsets per character

## Python Tooling (`tools/`)

### Style

- Python 3.10+
- Type hints on public functions
- `from __future__ import annotations`
- Docstrings on modules and CLI entry points

### Imports

Tools run from `tools/` directory:

```python
from lib.paths import BANNER_SRC
from lib.svg_utils import validate_structure
```

Tests use `pythonpath = ["tools"]` in `pyproject.toml`.

### CLI Conventions

- Exit code 0 on success, 1 on failure
- Print `[ok]`, `[warn]`, `[fail]` prefixed messages
- Never modify `src/banner.svg` from any tool

### Adding a New Tool

1. Create `tools/your_tool.py`
2. Use `lib.paths` for paths
3. Add to `Makefile` if user-facing
4. Document in `README.md`
5. Add tests if behavior is testable

## Git Conventions

- Do not commit `dist/*` except `.gitkeep` (generated in CI/local build)
- Do not commit `__pycache__/`
- Do not commit `preview.html`

## Validation Before PR

```bash
python tools/validate_svg.py
python tools/validate_structure.py
pytest tests/ -v
python tools/build_banner.py
```

Or: `make all`

## Related Documentation

- [Architecture](architecture.md)
- [Contributing](../CONTRIBUTING.md)
