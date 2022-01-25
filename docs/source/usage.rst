Usage
=====

The ``contributors`` directive renders the contributors of a given GitHub repository in a Sphinx documentation page.

This example renders the top 5 contributors from the repository ``sphinx-doc/sphinx``, ordered in descending order, excluding ``dgarcia360`` and ``sphinx`` usernames from the list.

.. code-block:: rst

  .. contributors:: sphinx-doc/sphinx
      :contributions:
      :exclude: dgarcia360,sphinx
      :limit: 5
      :order: DESC

.. contributors:: sphinx-doc/sphinx
    :contributions:
    :exclude: dgarcia360,sphinx
    :limit: 5
    :order: DESC

This example renders the contributors avatars, whithout showing the number of contributions:

.. code-block:: rst

  .. contributors:: sphinx-doc/sphinx
      :avatars:
      :limit: 5
      :order: ASC

.. contributors:: sphinx-doc/sphinx
    :avatars:
    :limit: 5
    :order: ASC

For more information on how to style the list, see :doc:`Customization <customization>`.
