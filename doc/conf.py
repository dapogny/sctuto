# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sctuto'
copyright = ''
author = 'Charles Dapogny'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

#extensions = ['sphinx_togglebutton', 'sphinxcontrib.bibtex', 'sphinx_proof']
extensions = ['sphinx_togglebutton', 'sphinxcontrib.bibtex', 'sphinx_proof','sphinx_math_dollar', 'sphinx.ext.mathjax'
]

mathjax3_config = {
  "tex": {
    "inlineMath": [['\\(', '\\)']],
    "displayMath": [["\\[", "\\]"]],
    "macros": {
      "calC":'{{\\mathcal C}}',
      "bz":'{\\mathbf{0}}',
      "d":'{\\text{d}}',
      "dv":'{\\text{div}}',
      "e":'{\\varepsilon}',
      "be":'{\\textbf{e}}',
      "n":'{\\textbf{n}}',
      "t":'{\\textbf{t}}',
      "u":'{\\textbf{u}}',
      "p":'{\\textbf{p}}',
      "bj":'{\\textbf{j}}',
      "bF":'{\\textbf{F}}',
      "bU":'{\\textbf{U}}',
      "bV":'{\\textbf{V}}',
      "x":'{\\textbf{x}}',
      "y":'{\\textbf{y}}',
      "bX":'{\\textbf{X}}',
      "P": '{\\mathbb{P}}',
      "R": '{\\mathbb{R}}',
      "N": '{\\mathbb{N}}',
      "I":'{\\text{I}}',
      "Id":'{\\text{Id}}',
      "calT":'{{\\mathcal T}}',
      "Hdiv":'{H_{\\text{div}}}',
      "tr":'{\\text{tr}}',
      "bold": ['{\\bf #1}',1]
    },
    "loader": {'load': ['[tex]/boldsymbol']},
    "packages": {'[+]': ['boldsymbol']}
  }
}

bibtex_bibfiles = ['refs.bib']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

numfig = True

# The name of the Pygments (syntax highlighting) style to use.
highlight_language = "freefem"

# Prologue
rst_prolog = """
.. role:: pink
.. role:: maroon
.. role:: blue
"""

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_title = 'Numerical tours in scientific computing'
html_theme_options = {
  'logo': 'falcmill.png',
  'page_width': '85%',
  'body_max_width': 'none',
  'sidebar_width': '15%',
  'show_powered_by': 'False',
}
html_static_path = ['_static']
html_css_files = [
    "gen.css"
]

# -- Options Latex -------------------------------------------------------------
latex_elements = {
    'preamble': r"\usepackage{bm}",
}
