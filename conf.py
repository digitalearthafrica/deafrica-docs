# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys

sys.path.insert(0, os.path.abspath('./sandbox/notebooks/Tools'))

# -- Project information -----------------------------------------------------

project = 'Digital Earth Africa'
copyright = '2021, DEAfrica Team'
author = 'DEAfrica Team'

# The full version, including alpha/beta/rc tags
release = '2021'

# -- General configuration ---------------------------------------------------
    
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "nbsphinx",
    "sphinx_rtd_theme",
    "sphinx.ext.autosectionlabel",
    "sphinx_build_compatibility.extension",
]

# Autodoc conf
autosummary_generate = ['sandbox/notebooks/Tools/index.rst']
autodoc_default_options = {
    'members': True,
}
autodoc_mock_imports = ['aiohttp',
                        'boto3',
                        'botocore',
                        'branca',
                        'dask',
                        'dask_ml',
                        'datacube',
                        'datacube_stats',
                        'dill',
                        'distutils',
                        'fsspec',
                        'fiona',
                        'folium',
                        'geopandas',
                        'geopy',
                        'hdstats',
                        'ipyleaflet',
                        'IPython',
                        'joblib',
                        'matplotlib',
                        'mpl_toolkits',
                        'numexpr',
                        'numpy',
                        'odc',
                        'osgeo',
                        'otps',
                        'packaging',
                        'pandas',
                        'pathos',
                        'psycopg2',
                        'pyproj',
                        'rasterio',
                        'rasterstats',
                        'rios',
                        'rsgislib',
                        'scipy',
                        'seaborn',
                        'shapely',
                        'skimage',
                        'sklearn',
                        'tqdm',
                        'traitlets',
                        'xarray']
autosummary_mock_imports = autodoc_mock_imports

napoleon_google_docstring = False
napoleon_numpy_docstring = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store',
                    '**.ipynb_checkpoints',
                    'sandbox/notebooks/DEAfrica_notebooks_template.ipynb',
                    ]

# Don't execute notebooks
nbsphinx_execute = 'never'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

try:
    import sphinx_rtd_theme

    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    html_theme_options = {
        'logo_only': True,
        'display_version': False,
    }
except ImportError:
    html_theme = 'alabaster'


html_baseurl = 'https://docs.digitalearthafrica.org/'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = '_static/logo.png'

html_favicon = '_static/favicon.png'

html_use_index = True

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# Use table-wrapping style
html_context = {
    'css_files': [
        '_static/theme_override.css',  # override wide tables in RTD theme
    ],
}

# Translation options
gettext_compact = "docs"  # makes a single "docs.po" file
gettext_location = False  # This causes the build to break?
locale_dirs = ['locales/']

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
on_gha = os.environ.get('GITHUB_ACTIONS', None) == 'True'
get_translation = os.environ.get('POEDITOR_PROJECT_ID', None) is not None

# If we are on ReadTheDocs, and translation is required, download the translation file from poeditor
if on_rtd and get_translation:
    import subprocess
    subprocess.run(["make", "fetchtranslation"])

# If we are on ReadtheDocs, load the latest version of the notebooks
if on_rtd or on_gha:
    import subprocess
    subprocess.run(["make", "fetchnotebooks"])
    subprocess.run(["make", "buildtools"])

