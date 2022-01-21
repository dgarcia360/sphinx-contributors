sphinx-contributors
===================

``sphinx-contributors`` is a Sphinx extension that helps you recognize the people who have contributed to an open-source project.

.. image:: https://raw.githubusercontent.com/dgarcia360/sphinx-contributors/master/docs/source/_static/example_avatars.png

Features
---------

**Promote contributions**

The extension retrieves from GitHub the list of users who have contributed to a repository.

**Configurable**

The extension lets you define the number of contributors to show and sort them by the number of commits.

Supported platforms
---------------------

``sphinx-contributors`` only works with GitHub public repositories.

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
