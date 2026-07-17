# Minimal Makefile for Digital Earth Africa Sphinx documentation

SPHINXOPTS   ?= -v
SPHINXBUILD  ?= sphinx-build
SPHINXPROJ   = DigitalEarthAfrica
SOURCEDIR    = .
BUILDDIR     = _build
PYTHON       ?= python

# Running "make" without a target displays Sphinx help.
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help cleanall install-docs fetchnotebooks buildtools fetchtranslation Makefile


# Build any standard Sphinx target, for example:
# make html
# make clean
# make linkcheck
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


# Remove the complete Sphinx build directory.
cleanall:
	@echo "Removing $(BUILDDIR)..."
	@rm -rf "$(BUILDDIR)"
	@echo "Build directory removed."


# Install the documentation dependencies.
install-docs:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt


# Download or refresh the DE Africa Sandbox notebooks.
fetchnotebooks:
	@if [ ! -d "sandbox/notebooks/.git" ]; then \
		echo "Cloning DE Africa Sandbox notebooks..."; \
		git clone https://github.com/digitalearthafrica/deafrica-sandbox-notebooks.git sandbox/notebooks; \
	else \
		echo "Updating DE Africa Sandbox notebooks..."; \
	fi
	cd sandbox/notebooks && \
		git fetch origin && \
		git checkout main && \
		git reset --hard origin/main


# Install the notebook tools package without resolving its dependencies.
buildtools:
	$(PYTHON) -m pip install ./sandbox/notebooks/Tools --no-dependencies


# Install POEditor and download translation files.
fetchtranslation:
	$(PYTHON) -m pip install poeditor
	$(PYTHON) download_translations.py