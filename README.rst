#############################
sphinxcontrib-ghcontributors
#############################

Sphinx extension for rendering the contributors list from GitHub repositories.

*****
Usage
*****

This extension defines the directive `ghcontributors`, taking as an argument the GitHub username and repository.

.. code-block:: restructuredtext

    ..  ghcontributors::
        :owner: dgarcia360
        :repository: sphinxcontrib-ghcontributors


The contributors are sorted in descending order by the number of commits.

.. image:: https://github.com/dgarcia360/sphinxcontrib-ghcontributors/blob/master/docs/example.png
    :width: 150

************
Installation
************

Install the extension using pip:

.. code-block:: shell

    pip install sphinxcontrib-ghcontributors

Add ``sphinxcontrib.ghcontributors`` as an extension in ``conf.py``

.. code-block:: python

    extensions = ['sphinxcontrib.ghcontributors']
