# Typography Guidelines

Typography specification for the GitHub Profile Banner.

## Font Stack

```
Inter, Segoe UI, system-ui, sans-serif
```

Inter is preferred; Segoe UI and system-ui provide Windows fallback. No web
font imports — relies on system fonts for zero-dependency SVG.

## Hierarchy

### Level 1 — Name (`#main-title`)

| Property | Value |
|----------|-------|
| Text | Alessandro Chaves |
| Size | 42px |
| Weight | 700 |
| Fill | `#FFFFFF` |
| Letter-spacing | -1.1px |
| Position | x=72, y=108 |

**Optical kerning** via `<tspan dx>`:

```xml
<tspan>A</tspan><tspan dx="-0.3">l</tspan><tspan>essandro</tspan>
<tspan dx="2"> </tspan>
<tspan>C</tspan><tspan dx="-0.2">h</tspan><tspan>aves</tspan>
```

### Depth Shadow (`#main-title-shadow`)

| Property | Value |
|----------|-------|
| Size | 42px |
| Weight | 700 |
| Fill | `#050816` @ 28% |
| Position | x=72, y=109 (+1px offset) |
| aria-hidden | true |

### Accent Bar (`#accent-bar`)

| Property | Value |
|----------|-------|
| Size | 88 × 2 px |
| Fill | `url(#accent-line-gradient)` |
| Opacity | 0.9 |
| Position | x=72, y=120 |

Guides the eye from name to subtitle.

### Level 2 — Professional Title (`#professional-title`)

| Property | Value |
|----------|-------|
| Text | Oracle Technical Consultant |
| Size | 16px |
| Weight | 500 |
| Fill | `#CBD5E1` @ 94% |
| Letter-spacing | 0.65px |
| Position | x=72, y=146 |

### Level 3 — Professional Summary (`#professional-summary`)

| Property | Value |
|----------|-------|
| Size | 12.5px |
| Weight | 400 |
| Fill | `#94A3B8` @ 88% |
| Letter-spacing | 0.15px |
| Lines | Two `<tspan>` lines at x=72 |

Text:

> Building reliable enterprise solutions through clean architecture,
> automation and continuous learning.

### Technology Badges

Small labels in typography layer (if present) use muted styling at 9–10px.

## Card Typography

Each technology card contains two text elements:

| Role | Size | Weight | Color |
|------|------|--------|-------|
| Title | 11px | 500 | `#CBD5E1` |
| Caption | 9px | 400 | `#94A3B8` @ 82% |

Position: x=54 (right of 24px icon + padding), y=31 (title), y=44 (caption).

Letter-spacing: title 0.18px, caption 0.12px.

## Contrast

| Pair | Ratio (approx.) | WCAG |
|------|-----------------|------|
| Name on background | > 12:1 | AAA |
| Title on background | > 7:1 | AAA |
| Summary on background | > 4.5:1 | AA |
| Card title on glass | > 4.5:1 | AA |

## Implementation Notes

- Typography uses **inline attributes** in layer 06, not CSS classes
- CSS classes in `<defs><style>` (`.main-title`, etc.) are legacy; inline
  values are authoritative after PR #3 refactor
- Do not animate position or scale on text elements
- Card opacity shimmer does not reduce text below AA contrast

## Editing Copy

To change text:

1. Locate `<!-- LAYER 06 - TYPOGRAPHY -->`
2. Edit `<text>` content only
3. Adjust `<tspan dx>` if name length changes significantly
4. Re-validate: `python tools/validate_svg.py`

## Related Documentation

- [Visual Guidelines](visual-guidelines.md)
- [Design System](design-system.md)
- [Composition Guidelines](composition-guidelines.md)
