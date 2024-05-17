# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OpenFOAM for ADA'
copyright = '2024, Atul Singh'
author = 'Atul Singh'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx_tabs.tabs',
]
templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'#alabaster'
html_static_path = ['_static']
html_css_files = [
        'custom.css', 
]

html_logo = "images/oflogo.png"

# Define custom roles
rst_prolog = """
.. role:: red
   :class: red

.. role:: blue
   :class: blue

.. role:: green
    :class: green
"""