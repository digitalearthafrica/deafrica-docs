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
    
# # Add any Sphinx extension module names here, as strings. They can be
# # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# # ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "nbsphinx",
    "sphinx.ext.autosectionlabel",
]

# Autodoc conf
autosummary_generate = ['sandbox/notebooks/Tools/index.rst']
autodoc_default_options = {
    'members': True,
}
autodoc_mock_imports = [ "aiohttp",
    "aiobotocore[boto3]", # for boto3
    "branca",
    "dask[complete]",
    "dask-ml",
    "dask-gateway",
    "datacube[performance,s3]",
    "fiona",
    "folium",
    "fsspec",
    "gdal",
    "geojson",
    "geopandas",
    "geopy",
    "hdstats",
    "ipyleaflet",
    "ipython",
    "ipywidgets",
    "joblib",
    "localtileserver",
    "matplotlib",
    "numexpr",
    "numpy",
    "odc-algo",
    "odc-geo>=0.4.2",
    "odc-ui",
    "OWSLib",
    "packaging",
    "pandas",
    "plotly",
    "pyproj",
    "pystac-client",  # for pystac
    "python-dateutil",
    "pyTMD > 2",
    "pytz",
    "rasterio",
    "rasterstats",
    "requests",
    "rioxarray",
    "scikit-image",
    "scikit-learn",
    "scipy",
    "seaborn",
    "shapely",
    "tqdm",
    "xarray",
    "gcsfs"]

autosummary_mock_imports = autodoc_mock_imports

napoleon_google_docstring = False
napoleon_numpy_docstring = True

nb_execution_allow_errors = False
nb_execution_raise_on_error = True

# # Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# # List of patterns, relative to source directory, that match files and
# # directories to ignore when looking for source files.
# # This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store',
                    '**.ipynb_checkpoints',
                    'sandbox/notebooks/DEAfrica_notebooks_template.ipynb',
                    ]

# # Don't execute notebooks
nbsphinx_execute = 'never'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

html_theme_path = ["_themes", ]
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}

# Define the canonical URL if you are using a custom domain on Read the Docs
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "https://docs.digitalearthafrica.org/") 

# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    if "html_context" not in globals():
        html_context = {}
    html_context["READTHEDOCS"] = True
    
# # Add any paths that contain custom static files (such as style sheets) here,
# # relative to this directory. They are copied after the builtin static files,
# # so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = '_static/logo.png'

html_favicon = '_static/favicon.png'

html_use_index = True

# # If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# # # Use table-wrapping style
html_css_files = ['theme_override.css',]  # override wide tables in RTD theme

# Translation options
gettext_compact = "docs"  # makes a single "docs.po" file
gettext_location = False  # This causes the build to break?
locale_dirs = ['locales/']

on_rtd = True #os.environ.get('READTHEDOCS', None) == 'True'
on_gha = True #os.environ.get('GITHUB_ACTIONS', None) == 'True'
get_translation = True  #os.environ.get('POEDITOR_PROJECT_ID', None) is not None

# If we are on ReadTheDocs, and translation is required, download the translation file from poeditor
if on_rtd or get_translation:
    import subprocess
    subprocess.run(["make", "fetchtranslation"])

# If we are on ReadtheDocs, load the latest version of the notebooks
if on_rtd or on_gha:
    import subprocess
    subprocess.run(["make", "fetchnotebooks"])
    subprocess.run(["make", "buildtools"])
