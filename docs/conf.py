# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PythonBook'
copyright = '2022-today, LaoQi'
author = 'LaoQi'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
]

myst_enable_extensions = [
    "amsmath",
    "dollarmath"
]

source_suffix = ['.rst', '.md']

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_theme_options = {
    "repository_url": "https://github.com/qiwsir/PythonTutorialForSelf-learners",
    "use_repository_button": True,
    "show_navbar_depth": 1,
    "show_toc_level": 1,
    "logo_only": True,
    "home_page_in_toc": True
}
html_title = "LQLab"
html_logo = ".././_static/logo.png"
html_favicon = ".././_static/icon.ico"
