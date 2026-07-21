# Configuration file for the Sphinx documentation builder.

import os
import sys
import subprocess

sys.path.insert(0, os.path.abspath("./sandbox/notebooks/Tools"))


# -- Project information -----------------------------------------------------

project = "Digital Earth Africa"
copyright = "2021, DEAfrica Team"
author = "DEAfrica Team"
release = "2021"


# -- General configuration ---------------------------------------------------

extensions = [
     "nbsphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosectionlabel",
    "sphinx_design",
    "myst_parser",
]

# Autodoc configuration
autosummary_generate = [
    "sandbox/notebooks/Tools/index.rst",
]

autodoc_default_options = {
    "members": True,
}

autodoc_mock_imports = [
    "aiohttp",
    "aiobotocore[boto3]",
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
    "pystac-client",
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
    "gcsfs",
]

autosummary_mock_imports = autodoc_mock_imports

napoleon_google_docstring = False
napoleon_numpy_docstring = True

nb_execution_allow_errors = False
nb_execution_raise_on_error = True

# Do not execute notebooks during the documentation build.
nbsphinx_execute = "never"

templates_path = ["_templates"]

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**.ipynb_checkpoints",
    "sandbox/notebooks/DEAfrica_notebooks_template.ipynb",
]


# -- Options for HTML output -------------------------------------------------

# -- Options for HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "header_links_before_dropdown": 6,
    "navbar_persistent": ["search-button-field"],
    "navbar_end": [
        "theme-switcher",
        "navbar-icon-links",
    ],
    "navbar_align": "left",

    "navigation_depth": 4,
    "show_nav_level": 2,
    "collapse_navigation": False,

    "secondary_sidebar_items": [
        "page-toc",
    ],
    
    "show_toc_level": 2,

    "back_to_top_button": True,
    "search_bar_text": "Search the docs",
    "show_prev_next": False,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/digitalearthafrica",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        },
    ],

    "logo": {
        "text": "",
        "image_light": "_static/logo.png",
        "image_dark": "_static/logo.png",
    },

        "secondary_sidebar_items": [
        "page-toc",
    ],

    "show_toc_level": 2,
    "navigation_depth": 4,
    "show_nav_level": 1,
    "collapse_navigation": False,
    
    "footer_start": [
        "deafrica-footer",
    ],

    "footer_center": [],

    "footer_end": [],
}

html_sidebars = {
    "index": [],
    "**": [
        "sidebar-collapse",
        "sidebar-nav-bs",
    ],

    
}

html_static_path = ["_static"]

html_logo = "_static/logo.png"
html_favicon = "_static/favicon.png"

html_css_files = [
    "theme_override.css",
    "deafrica_pydata.css",
]

html_use_index = True
html_show_sourcelink = False

html_js_files = [
    "external-links.js", 
    ("active-navbar.js", {"defer": "defer"}),
]

# Canonical URL
html_baseurl = os.environ.get(
    "READTHEDOCS_CANONICAL_URL",
    "https://docs.digitalearthafrica.org/",
)

# Tell Jinja templates when the build is running on Read the Docs.
if os.environ.get("READTHEDOCS", "") == "True":
    html_context = globals().get("html_context", {})
    html_context["READTHEDOCS"] = True

# -- copyright -----------------------------------------------------
copyright = "2026 Digital Earth Africa"

# -- Translation options -----------------------------------------------------

gettext_compact = "docs"
gettext_location = False
locale_dirs = ["locales/"]


# -- Build environment -------------------------------------------------------

on_rtd = os.environ.get("READTHEDOCS") == "True"
on_gha = os.environ.get("GITHUB_ACTIONS") == "True"

poeditor_project_id = os.environ.get("POEDITOR_PROJECT_ID")
poeditor_api_token = os.environ.get("POEDITOR_API_TOKEN")

has_poeditor_credentials = bool(
    poeditor_project_id and poeditor_api_token
)


def run_make_target(target: str, required: bool = True) -> None:
    """Run a Makefile target from the documentation root."""
    result = subprocess.run(
        ["make", target],
        check=False,
        text=True,
    )

    if required and result.returncode != 0:
        raise RuntimeError(
            f"Make target '{target}' failed with "
            f"exit code {result.returncode}."
        )


# Download translations only when both POEditor credentials are available.
if has_poeditor_credentials:
    run_make_target("fetchtranslation")

# buildtools already depends on fetchnotebooks, so only call buildtools.
if on_rtd or on_gha:
    run_make_target("buildtools")
