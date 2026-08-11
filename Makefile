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
PAGES   := docs/index.html
BUILDER := web/build.py web/template.html
SOURCES := HANDBOOK.md HANDBOOK.cs.md \
           WALKTHROUGHS.md WALKTHROUGHS.cs.md \
           PROMPTS.md PROMPTS.cs.md

.DEFAULT_GOAL := help
.PHONY: help setup hooks build rebuild check clean

help:
	@echo "Handbook build targets:"
	@echo ""
	@echo "  make setup     create $(VENV), install dependencies, enable the git hook"
	@echo "  make hooks     enable the pre-commit hook only"
	@echo "  make build     regenerate $(TARGET) and $(PAGES) if any source changed"
	@echo "  make rebuild   regenerate it unconditionally"
	@echo "  make check     fail if either generated page is out of date"
	@echo "  make clean     remove $(VENV)"
	@echo ""
	@echo "$(TARGET) is the artifact fragment; $(PAGES) is the GitHub Pages site."
	@echo "After building, commit both and republish $(TARGET) to the artifact URL."

## Create the virtualenv and install requirements. The stamp file means this
## reruns only when requirements.txt changes.
setup: $(STAMP) hooks

$(STAMP): requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install --quiet --upgrade pip
	$(PIP) install --quiet --requirement requirements.txt
	@touch $@
	@echo "$(VENV) ready: $$($(PYTHON) --version)"

## Point git at the versioned hooks, so a commit cannot leave the generated
## page out of step with the Markdown. Undo with:
##   git config --unset core.hooksPath
hooks:
	@git config core.hooksPath .githooks
	@echo "pre-commit hook enabled (.githooks/)"

## Regenerate the page when a source, the template or the generator changed.
build: $(TARGET) $(PAGES)

# One run of the generator writes both files, so they share a rule.
$(TARGET) $(PAGES): $(STAMP) $(BUILDER) $(SOURCES)
	$(PYTHON) web/build.py

rebuild: $(STAMP)
	$(PYTHON) web/build.py

## Verify the committed page matches what the sources produce.
check: $(STAMP)
	$(PYTHON) web/build.py --check

clean:
	rm -rf $(VENV)
