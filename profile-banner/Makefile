.PHONY: help validate build optimize export preview watch clean test structure all

PYTHON ?= python

help:
	@echo "Profile Banner — available targets"
	@echo "  validate   Run SVG validation"
	@echo "  build      Build dist/banner.svg"
	@echo "  optimize   Build dist/banner.min.svg"
	@echo "  export     Export PNG previews (optional deps)"
	@echo "  preview    Open browser preview server"
	@echo "  watch      Watch src/banner.svg and rebuild"
	@echo "  clean      Remove generated artifacts"
	@echo "  test       Run pytest suite"
	@echo "  structure  Validate repository structure"
	@echo "  all        validate + build + optimize + test"

validate:
	$(PYTHON) tools/validate_svg.py

build:
	$(PYTHON) tools/build_banner.py

optimize: build
	$(PYTHON) tools/optimize_svg.py

export: build
	$(PYTHON) tools/export_png.py

preview: build
	$(PYTHON) tools/preview.py

watch:
	$(PYTHON) tools/watch.py

clean:
	$(PYTHON) tools/clean.py

test:
	$(PYTHON) -m pytest tests/ -v

structure:
	$(PYTHON) tools/validate_structure.py

all: validate build optimize test structure
