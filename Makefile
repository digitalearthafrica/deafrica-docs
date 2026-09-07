# Digital Earth Africa Sphinx documentation Makefile

SPHINXOPTS  ?= -v
SPHINXBUILD ?= sphinx-build
SOURCEDIR   := .
BUILDDIR    := _build
PYTHON      ?= python

NOTEBOOK_REPO := https://github.com/digitalearthafrica/deafrica-sandbox-notebooks.git
NOTEBOOK_DIR  := sandbox/notebooks
TOOLS_DIR     := $(NOTEBOOK_DIR)/Tools


.PHONY: help clean cleanall install-docs \
        fetchnotebooks buildtools fetchtranslation \
        gettext translations html-fr


# Display available Sphinx targets.
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


# Pass standard targets to Sphinx:
# make html
# make linkcheck
# make spelling
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


# Remove generated Sphinx files.
clean:
	@echo "Cleaning generated documentation..."
	@rm -rf "$(BUILDDIR)/html" \
	        "$(BUILDDIR)/doctrees" \
	        "$(BUILDDIR)/gettext"


# Remove the complete build directory.
cleanall:
	@echo "Removing $(BUILDDIR)..."
	@rm -rf "$(BUILDDIR)"
	@echo "Build directory removed."


# Install documentation dependencies.
install-docs:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt


# Clone or update the DE Africa Sandbox notebooks.
fetchnotebooks:
	@if [ ! -d "$(NOTEBOOK_DIR)/.git" ]; then \
		echo "Cloning DE Africa Sandbox notebooks..."; \
		git clone \
			--depth 1 \
			--branch main \
			"$(NOTEBOOK_REPO)" \
			"$(NOTEBOOK_DIR)"; \
	else \
		echo "Updating DE Africa Sandbox notebooks..."; \
		git -C "$(NOTEBOOK_DIR)" fetch \
			--depth 1 \
			origin main; \
		git -C "$(NOTEBOOK_DIR)" reset \
			--hard origin/main; \
		git -C "$(NOTEBOOK_DIR)" clean -fd; \
	fi


# Install the notebook tools package.
buildtools: fetchnotebooks
	@if [ ! -d "$(TOOLS_DIR)" ]; then \
		echo "Notebook tools directory not found: $(TOOLS_DIR)"; \
		exit 1; \
	fi
	$(PYTHON) -m pip install \
		--no-dependencies \
		--disable-pip-version-check \
		"$(TOOLS_DIR)"


# Download translation files from POEditor.
fetchtranslation:
	@if [ -z "$$POEDITOR_API_TOKEN" ]; then \
		echo "POEDITOR_API_TOKEN is not configured."; \
		exit 1; \
	fi
	@if [ -z "$$POEDITOR_PROJECT_ID" ]; then \
		echo "POEDITOR_PROJECT_ID is not configured."; \
		exit 1; \
	fi
	$(PYTHON) download_translations.py


# Generate gettext POT files.
gettext:
	@rm -rf "$(BUILDDIR)/gettext"
	$(SPHINXBUILD) \
		-E \
		-a \
		-T \
		-b gettext \
		"$(SOURCEDIR)" \
		"$(BUILDDIR)/gettext"


# Download and compile translations.
translations: fetchtranslation
	$(PYTHON) -m sphinx_intl build \
		--locale-dir locales


# Build the French documentation locally.
html-fr: translations
	$(SPHINXBUILD) \
		-E \
		-a \
		-T \
		-b html \
		-D language=fr \
		-D locale_dirs=locales \
		"$(SOURCEDIR)" \
		"$(BUILDDIR)/html/fr"