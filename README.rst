sphinxcontrib-ghcontributors
============================

``sphinxcontrib-ghcontributors`` is a Sphinx extension that helps you recognize the people who have contributed to an open-source project.

Example:

.. image:: https://raw.githubusercontent.com/dgarcia360/sphinxcontrib-ghcontributors/master/docs/_static/example-avatars.png

Installation
------------

#. Install ``sphinxcontrib-ghcontributors`` using PIP.

   .. code-block:: bash

      pip install sphinxcontrib-ghcontributors


#. Add the extension to your Sphinx project ``conf.py`` file.

   .. code-block:: python

      extensions = ['sphinxcontrib.ghcontributors']

Usage
-----

Using the directive:

.. code-block:: rst

   ..  ghcontributors:: dgarcia360/sphinxcontrib-ghcontributors

Renders:

.. code-block:: rst

   .. image:: https://raw.githubusercontent.com/dgarcia360/sphinxcontrib-ghcontributors/master/docs/_static/example.png

Check out the full documentation for more customizable options at https://sphinxcontrib-ghcontributors.readthedocs.io/

License
-------

Copyright (c) 2018 David Garcia (`@dgarcia360 <https://davidgarcia.dev>`_).

Licensed under MIT license (see `LICENSE.md <LICENSE.md>`_ for details)
