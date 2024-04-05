# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Esrum Cluster"
copyright = "2023, CBMR Phenomics"
author = "CBMR Phenomics"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = []

# Default language for code blocks (terminal sessions)
highlight_language = "console"

# Disable index page (not used)
html_use_index = False
# Disable the "View source" link on every page
html_show_sourcelink = False

# Prevent conversion of -- to emdashes
smartquotes = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# https://pradyunsg.me/furo/
# Install the "furo" theme with `pip install furo`
html_theme = "furo"

html_static_path = ["_static"]
html_css_files = [
    "css/playback.css",
    "css/theme.css",
]
html_js_files = [
    "js/custom.js",
    "js/libgif.js",
    "js/playback.js",
]
