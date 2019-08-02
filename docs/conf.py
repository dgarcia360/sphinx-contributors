# -*- coding: utf-8 -*-
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinxcontrib.ghcontributors",
]


# Add stylesheet.
def setup(app):
    app.add_stylesheet('css/custom.css')


# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'sphinxcontrib-ghcontributors'
copyright = u'David Garcia <dgarcia360@outlook.com>'


# General information about the project.

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.1'
# The full version, including alpha/beta/rc tags.
release = '0.1.0'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'pyramid'

# Output file base name for HTML help builder.
htmlhelp_basename = 'sphinxcontrib-ghcontributors'