# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Esrum Cluster"
copyright = "2023-2024, CBMR Data Analytics; licensed under CC-BY 4.0"
author = "CBMR Data Analytics"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # https://github.com/executablebooks/sphinx-copybutton
    "sphinx_copybutton",
]

templates_path = ["_templates"]
exclude_patterns = [
    # Troubleshooting pages are included using `.. include` statements
    "**/*_troubleshooting.rst"
]

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

# Add an edit button to every page
html_theme_options = {
    "source_repository": "https://github.com/cbmr-data/cbmr-data.github.io/",
    "source_branch": "main",
    "source_directory": "esrum/source",
}

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

# Apply unreleased (after furu v2024.4.27) changes for better readability
pygments_style = "a11y-light"
pygments_dark_style = "a11y-dark"

# Exclude line numbers, prompts, and terminal output when copying from `console` blocks
copybutton_exclude = ".linenos, .gp, .go"
# Handle bash, R, and python prompts
copybutton_prompt_text = r"\$ |> |>>> "
copybutton_prompt_is_regexp = True
