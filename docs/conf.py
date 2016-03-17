#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sphinx_rtd_theme

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'solidfire-sdk-python'
copyright = '2014-2016, NetApp, Inc.  All Rights Reserved.'
author = 'Jason Ryan Womack'
version = '1.0'
release = '1.0.0.dev1'
language = 'en'

exclude_patterns = ['_build']
pygments_style = 'sphinx'
todo_include_todos = True


def setup(app):
    app.add_stylesheet("solidfire.css")


html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

html_static_path = ['_static']
htmlhelp_basename = 'solidfiredoc'

latex_elements = {}

latex_documents = [
    (master_doc, 'solidfire.tex', 'solidfire Documentation',
     'Author', 'manual'),
]

man_pages = [
    (master_doc, 'solidfire', 'solidfire Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'solidfire', 'solidfire Documentation',
     author, 'solidfire', 'One line description of project.',
     'Miscellaneous'),
]

epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

epub_exclude_files = ['search.html']
