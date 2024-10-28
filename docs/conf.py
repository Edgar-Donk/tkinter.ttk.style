# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('./scripts/'))


# -- Project information -----------------------------------------------------

project = "'Putting on the Style'"
copyright = "2022, 'Edga Donk'"
author = "Edga Donk"

# The full version, including alpha/beta/rc tags
release = "2"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.autodoc",
    'sphinx.ext.napoleon',
    "sphinx.ext.autosummary",
    #'hidden_code_block'
    'sphinx.ext.autosectionlabel',
    # "numpydoc",
    'sphinx.ext.mathjax',
    'sphinx_exec_code',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx_copybutton',
]

napoleon_google_docstring = False
napoleon_numpy_docstring = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The root document.
root_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme_options = {
  "show_prev_next": True,
  # search bar options are ‘navbar’ and ‘sidebar’.
  "search_bar_position": "sidebar",
  #  "use_edit_page_button": True,

}

html_sidebars = {
"contributing": ["sidebar-search-bs.html", "custom-template.html"],
    "changelog": [],
}

# option for show/hide code
def setup(app):
    app.add_css_file('custom.css')

# html_logo = '_static/ben_style.png'

html_theme_options = {
   "logo": {
      "text": "Putting on the Style",
      "image_light": 'bigbenc.png',
      "image_dark": "bigbencneon.png",
   }
}

html_favicon = '_static/ben1.ico'