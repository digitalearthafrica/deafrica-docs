# Configuration file for the Sphinx documentation builder.

import os
import sys

sys.path.insert(0, os.path.abspath("./sandbox/notebooks/Tools"))


# -- Project information -----------------------------------------------------

project = "Digital Earth Africa"
author = "Digital Earth Africa"
copyright = "2026 Digital Earth Africa"
release = "2026"


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

templates_path = ["_templates"]

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**/.ipynb_checkpoints",
    "sandbox/notebooks/DEAfrica_notebooks_template.ipynb",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

master_doc = "index"


# -- Autodoc and autosummary -------------------------------------------------

autosummary_generate = [
    "sandbox/notebooks/Tools/index.rst",
]

autodoc_default_options = {
    "members": True,
}

autodoc_mock_imports = [
    "aiohttp",
    "aiobotocore",
    "boto3",
    "branca",
    "dask",
    "dask_ml",
    "dask_gateway",
    "datacube",
    "fiona",
    "folium",
    "fsspec",
    "gdal",
    "geojson",
    "geopandas",
    "geopy",
    "hdstats",
    "ipyleaflet",
    "IPython",
    "ipywidgets",
    "joblib",
    "localtileserver",
    "matplotlib",
    "numexpr",
    "numpy",
    "odc",
    "odc.algo",
    "odc.geo",
    "odc.ui",
    "owslib",
    "packaging",
    "pandas",
    "plotly",
    "pyproj",
    "pystac_client",
    "dateutil",
    "pyTMD",
    "pytz",
    "rasterio",
    "rasterstats",
    "requests",
    "rioxarray",
    "skimage",
    "sklearn",
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

autosectionlabel_prefix_document = True


# -- Notebook configuration -------------------------------------------------

nbsphinx_execute = "never"

nb_execution_allow_errors = False
nb_execution_raise_on_error = True


# -- Translation configuration ----------------------------------------------

gettext_compact = "docs"
gettext_location = False
locale_dirs = ["locales/"]


# -- HTML output -------------------------------------------------------------

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "navbar_start": [
        "navbar-logo",
    ],
    "navbar_center": [
        "navbar-nav",
    ],
    "navbar_persistent": [
        "search-button-field",
    ],
    "navbar_end": [
        "theme-switcher",
        "navbar-icon-links",
    ],
    "navbar_align": "left",
    "header_links_before_dropdown": 6,

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
    "doc_css.css",
]

html_use_index = True
html_split_index = False
html_domain_indices = False
html_show_sourcelink = False

html_baseurl = os.environ.get(
    "READTHEDOCS_CANONICAL_URL",
    "https://docs.digitalearthafrica.org/",
)


# -- HTML template context ---------------------------------------------------

html_context = {}

if os.environ.get("READTHEDOCS", "") == "True":
    html_context["READTHEDOCS"] = True