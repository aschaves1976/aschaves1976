## Summary

<!-- What does this PR change and why? -->

## Type

- [ ] Visual change (requires design review)
- [ ] SVG structure / layer change
- [ ] Tooling / CI change
- [ ] Documentation only

## Checklist

- [ ] `python tools/validate_svg.py` passes
- [ ] `pytest tests/ -v` passes
- [ ] `python tools/build_banner.py` succeeds
- [ ] No edits to `dist/` without running build tools
- [ ] XML comments do not contain `--` (double hyphen)
- [ ] New symbols use `<use href="#id">` (no duplicated geometry)
- [ ] Documentation updated if behavior or structure changed

## Visual Impact

<!-- If applicable: before/after description or screenshot -->

## Related Issues

<!-- Fixes #123 -->
