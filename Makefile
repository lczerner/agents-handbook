# Build the published web version of the handbook from the Markdown sources.
#
#   make setup    create the virtualenv and install dependencies
#   make build    regenerate web/handbook.html
#
# Run `make` on its own for the full list.

VENV    := .venv
PYTHON  := $(VENV)/bin/python
PIP     := $(VENV)/bin/pip
STAMP   := $(VENV)/.installed

TARGET  := web/handbook.html
BUILDER := web/build.py web/template.html
SOURCES := HANDBOOK.md HANDBOOK.cs.md \
           WALKTHROUGHS.md WALKTHROUGHS.cs.md \
           PROMPTS.md PROMPTS.cs.md

.DEFAULT_GOAL := help
.PHONY: help setup build rebuild check clean

help:
	@echo "Handbook build targets:"
	@echo ""
	@echo "  make setup     create $(VENV) and install dependencies"
	@echo "  make build     regenerate $(TARGET) if any source changed"
	@echo "  make rebuild   regenerate it unconditionally"
	@echo "  make check     fail if $(TARGET) is out of date"
	@echo "  make clean     remove $(VENV)"
	@echo ""
	@echo "After building, republish $(TARGET) to the artifact URL in web/README.md."

## Create the virtualenv and install requirements. The stamp file means this
## reruns only when requirements.txt changes.
setup: $(STAMP)

$(STAMP): requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install --quiet --upgrade pip
	$(PIP) install --quiet --requirement requirements.txt
	@touch $@
	@echo "$(VENV) ready: $$($(PYTHON) --version)"

## Regenerate the page when a source, the template or the generator changed.
build: $(TARGET)

$(TARGET): $(STAMP) $(BUILDER) $(SOURCES)
	$(PYTHON) web/build.py

rebuild: $(STAMP)
	$(PYTHON) web/build.py

## Verify the committed page matches what the sources produce.
check: $(STAMP)
	$(PYTHON) web/build.py --check

clean:
	rm -rf $(VENV)
