sphinx-contributors
===================

``sphinx-contributors`` is a Sphinx extension that automatically lists the people who have contributed to your GitHub repositories, right inside your documentation.

.. image:: https://raw.githubusercontent.com/dgarcia360/sphinx-contributors/master/docs/source/_static/example_avatars.png

Features
---------

- List contributors from one or multiple GitHub repositories in a single directive.
- Display real names, avatars, and contribution counts.
- Manually include contributors not detected by the API (e.g., ``Co-authored-by`` contributors).
- Exclude bots and specific users.
- Sort by most or least active, and limit the number shown.

Requirements
---------------------

- GitHub public repositories.
- Python 3.10+ and Sphinx 7.0+.

Installation
------------

#. Install ``sphinx-contributors`` using PIP.

   .. code-block:: bash

      pip install sphinx-contributors


#. Add the extension to your Sphinx project ``conf.py`` file.

   .. code-block:: python

      extensions = ['sphinx_contributors']

Usage
-----

Using the directive:

.. code-block:: rst

   ..  contributors:: sphinx-doc/sphinx

Renders:

.. image:: https://raw.githubusercontent.com/dgarcia360/sphinx-contributors/master/docs/source/_static/example.png

Check out the full documentation for more customizable options at https://sphinx-contributors.readthedocs.io/

Contributing
------------

We encourage public contributions!
Please review `CONTRIBUTING <https://sphinx-contributors.readthedocs.io/en/latest/contribute.html>`_ for details on our code of conduct and development process.

License
-------

Copyright (c) 2018 - present David Garcia (`@dgarcia360 <https://twitter.com/dgarcia360>`_).

Licensed under the `MIT License <https://github.com/dgarcia360/sphinx-contributors/blob/main/LICENSE.md>`_.
