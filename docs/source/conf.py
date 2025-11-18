import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'Django Admin Trap'
copyright = '2024, jamil-codes'
author = 'jamil-codes'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'style_nav_header_background': '#343131',
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
}

html_css_files = [
    'custom.css',
]