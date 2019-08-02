============================
sphinxcontrib-ghcontributors
============================

.. image:: https://travis-ci.org/dgarcia360/sphinxcontrib-ghcontributors.svg?branch=master
    :target: https://travis-ci.org/dgarcia360/sphinxcontrib-ghcontributors

**Sphinx extension to render GitHub contributors**

People who contribute to open-source projects could be spending their free time.
It does not matter if it is a code change, an epic, or fixing a small typo.
At the end of the day, this change makes the project better.
That's the reason why you should recognize every contribution!

Are you using `Sphinx`_  to document the open-source project?
Then `sphinxcontrib-ghcontributors`_ directive allows you to render all the usernames that have contributed to your repositories directly in your docs.

**Example**

*sphinx-doc/sphinx* top 10 contributors

..  ghcontributors:: sphinx-doc/sphinx

Add the extension to your project following the :doc:`installation instructions <installation>`.

.. toctree::
    :caption: Table of Contents
    :maxdepth: 2

    installation
    options
    changelog

.. _sphinxcontrib-ghcontributors: http://pypi.python.org/pypi/sphinxcontrib-ghcontributors
.. _Sphinx: http://www.sphinx-doc.org/en/master/