============
Installation
============

Getting Started
===============

1. Install sphinxcontrib-ghcontributors using pip.

.. code-block:: console

    pip install sphinxcontrib-ghcontributors

2. Add the extension to your Sphinx project ``conf.py`` file.

.. code-block:: python

    extensions = ['sphinxcontrib.ghcontributors']

Usage
=====

The extension defines the directive `ghcontributors`. For each repository that you want to render its contributors, state the Github username and the repository name.

.. code-block:: rst

    ..  ghcontributors:: dgarcia360/sphinxcontrib-ghcontributors

Sphinx will render the 10 most active contributors for ``dgarcia360/sphinxcontrib-ghcontributors`` repo. You can extend the number of results, and as well exclude some users from the list adding optional filters.

.. code-block:: rst

    ..  ghcontributors:: dgarcia360/sphinxcontrib-ghcontributors
        :limit: 20
        :order: ASC
        :exclude: dgarcia360,sphinx

This directive will render the less active 20 contributors, ordered in ascending order, excluding ``dgarcia360`` and ``sphinx`` usernames from the list.

To see up to what point you can configure the directive, see the :doc:`options <options>` reference.
