Usage
=====

The ``ghcontributors`` directive renders the contributors of a given GitHub repository in a Sphinx documentation page.

Syntax
------

.. rst:directive:: .. ghcontributors:: username/repository

    .. rst:directive:option:: limit
      :type: integer

      Number of contributors to list, between 1 and 100. The default value is 10.

      .. versionadded:: 0.2.2

    .. rst:directive:option:: order
      :type: string

      Results are sorted by the number of contributions. This parameter controls whether they are sorted by most active users first (``DESC``) or least active users first (``ASC``). Default is ``DESC``.

      .. versionadded:: 0.2.2

    .. rst:directive:option:: avatars
      :type: boolean

      Whether to include an image with the avatar returned by GitHub. Use CSS to customize the image size, since the returned images might vary.

      .. versionadded:: 0.2.3

    .. rst:directive:option:: contributions
      :type: boolean

      Whether to show the total number of contributions by each user or not.

      .. versionadded:: 0.2.3

Example
-------

This example renders the top 5 contributors from the repository ``sphinx-doc/sphinx``, ordered in descending order, excluding ``dgarcia360`` and ``sphinx`` usernames from the list.

.. code-block:: rst

  .. ghcontributors:: sphinx-doc/sphinx
      :limit: 5
      :order: DESC
      :exclude: dgarcia360,sphinx
      :contributions:

.. ghcontributors:: sphinx-doc/sphinx
    :limit: 5
    :order: DESC
    :exclude: dgarcia360,sphinx
    :contributions:

This example renders the contributors avatars, whithout showing the number of contributions:


.. code-block:: rst

  .. ghcontributors:: sphinx-doc/sphinx
      :limit: 5
      :order: ASC
      :avatars:

.. rst-class:: ghcontributors-avatar

.. ghcontributors:: sphinx-doc/sphinx
    :limit: 5
    :order: ASC
    :avatars:

For more information on how to style the list, see :doc:`Customization <customization>`.