"""SVG parsing and validation helpers."""
from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path

SVG_NS = "http://www.w3.org/2000/svg"
XLINK_NS = "http://www.w3.org/1999/xlink"
NS = {"svg": SVG_NS, "xlink": XLINK_NS}

HREF_ATTRS = ("href", f"{{{XLINK_NS}}}href")


@dataclass
class ValidationResult:
    ok: bool = True
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, message: str) -> None:
        self.ok = False
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def read_text(path: Path) -> str:
    raw = path.read_bytes()
    if b"\x00" in raw:
        raise ValueError(f"NULL byte found in {path}")
    return raw.decode("utf-8")


def parse_svg(path: Path) -> ET.Element:
    text = read_text(path)
    try:
        return ET.fromstring(text)
    except ET.ParseError as exc:
        raise ValueError(f"Invalid XML in {path}: {exc}") from exc


def local_tag(tag: str) -> str:
    return tag.rsplit("}", 1)[-1] if "}" in tag else tag


def collect_ids(root: ET.Element) -> dict[str, int]:
    ids: dict[str, int] = {}
    for elem in root.iter():
        elem_id = elem.attrib.get("id")
        if elem_id:
            ids[elem_id] = ids.get(elem_id, 0) + 1
    return ids


def collect_hrefs(root: ET.Element) -> list[str]:
    hrefs: list[str] = []
    for elem in root.iter():
        for attr in HREF_ATTRS:
            value = elem.attrib.get(attr)
            if value and value.startswith("#"):
                hrefs.append(value[1:])
    url_pattern = re.compile(r"url\(#([^)]+)\)")
    for elem in root.iter():
        for value in elem.attrib.values():
            for match in url_pattern.findall(value):
                hrefs.append(match)
    return hrefs


def validate_structure(path: Path) -> ValidationResult:
    result = ValidationResult()
    text = read_text(path)

    if not text.lstrip().startswith("<?xml"):
        result.warn("Missing XML declaration")

    required_sections = [
        "SVG DEFINITIONS",
        "LAYER 01 - BACKGROUND",
        "LAYER 02 - AMBIENT LIGHTS",
        "LAYER 03 - TECH GRID",
        "LAYER 04 - ORGANIC CIRCUITS",
        "LAYER 05 - FLOATING GEOMETRY",
        "LAYER 06 - TYPOGRAPHY",
        "LAYER 07 - TECHNOLOGY CARDS",
        "LAYER 08 - DECORATIONS",
        "LAYER 09 - ANIMATIONS",
        "FOOTER",
    ]
    for section in required_sections:
        if section not in text:
            result.error(f"Missing required section comment: {section}")

    if "PROJECT.....: GitHub Profile Banner" not in text:
        result.error("Missing project metadata header")

    root = parse_svg(path)
    if local_tag(root.tag) != "svg":
        result.error("Root element must be <svg>")

    view_box = root.attrib.get("viewBox", "")
    if view_box != "0 0 1400 350":
        result.error(f"Unexpected viewBox: {view_box!r}")

    ids = collect_ids(root)
    duplicates = [id_ for id_, count in ids.items() if count > 1]
    if duplicates:
        result.error(f"Duplicate IDs: {', '.join(sorted(duplicates))}")

    hrefs = collect_hrefs(root)
    missing = sorted({href for href in hrefs if href not in ids})
    if missing:
        result.error(f"Broken references: {', '.join(missing)}")

    symbol_tags = []
    for elem in root.iter():
        if local_tag(elem.tag) == "symbol" and "id" in elem.attrib:
            symbol_tags.append(elem.attrib["id"])

    uses_without_symbol = []
    for elem in root.iter():
        if local_tag(elem.tag) != "use":
            continue
        target = None
        for attr in HREF_ATTRS:
            if attr in elem.attrib:
                target = elem.attrib[attr]
                break
        if target and target.startswith("#") and target[1:] not in ids:
            uses_without_symbol.append(target)

    if uses_without_symbol:
        result.error(f"<use> targets not found: {', '.join(sorted(set(uses_without_symbol)))}")

    if not symbol_tags:
        result.warn("No <symbol> definitions found")

    _validate_accessibility(root, result)

    return result


def _validate_accessibility(root: ET.Element, result: ValidationResult) -> None:
    """Check SVG accessibility metadata (warnings only)."""
    has_title = any(local_tag(elem.tag) == "title" for elem in root.iter())
    has_desc = any(local_tag(elem.tag) == "desc" for elem in root.iter())

    if not has_title:
        result.warn("Missing <title> element for accessibility")
    if not has_desc:
        result.warn("Missing <desc> element for accessibility")
    if root.attrib.get("role") != "img":
        result.warn('Root <svg> should have role="img"')
    if not root.attrib.get("aria-label"):
        result.warn("Missing aria-label on root <svg>")
