import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

project = 'Leonardo da Vinci Knowledge Graph'
copyright = '2024, Stefany Simplicio'
author = 'Stefany Simplicio'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

html_theme = 'sphinx_rtd_theme'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_static_path = ['_static']