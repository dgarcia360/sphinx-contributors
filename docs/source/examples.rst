Examples
========

The ``contributors`` directive renders the contributors of a given GitHub repository in a Sphinx documentation page. This page shows the different options available.

Basic usage
-----------

List the top 10 contributors from a repository:

.. code-block:: rst

   .. contributors:: dgarcia360/sphinx-contributors

.. contributors:: dgarcia360/sphinx-contributors

With contribution counts
------------------------

Show how many contributions each user has made:

.. code-block:: rst

   .. contributors:: dgarcia360/sphinx-contributors
      :contributions:
      :limit: 5

.. contributors:: dgarcia360/sphinx-contributors
   :contributions:
   :limit: 5

With avatars
------------

Display contributor avatars:

.. code-block:: rst

   .. contributors:: dgarcia360/sphinx-contributors
      :avatars:
      :limit: 5

.. contributors:: dgarcia360/sphinx-contributors
   :avatars:
   :limit: 5

With real names
---------------

Show real names instead of usernames (fetched from GitHub profiles):

.. code-block:: rst

   .. contributors:: dgarcia360/sphinx-contributors
      :names:
      :limit: 5

.. contributors:: dgarcia360/sphinx-contributors
   :names:
   :limit: 5

Combining options
-----------------

Avatars, real names, and contribution counts together:

.. code-block:: rst

   .. contributors:: dgarcia360/sphinx-contributors
      :avatars:
      :contributions:
      :names:
      :limit: 5

.. contributors:: dgarcia360/sphinx-contributors
   :avatars:
   :contributions:
   :names:
   :limit: 5

Sorting order
-------------

Sort by least active contributors first:

.. code-block:: rst

   .. contributors:: dgarcia360/sphinx-contributors
      :contributions:
      :limit: 5
      :order: ASC

.. contributors:: dgarcia360/sphinx-contributors
   :contributions:
   :limit: 5
   :order: ASC

Excluding users
---------------

Exclude bots or specific users:

.. code-block:: rst

   .. contributors:: dgarcia360/sphinx-contributors
      :contributions:
      :exclude: dependabot[bot], pre-commit-ci[bot]
      :limit: 5

.. contributors:: dgarcia360/sphinx-contributors
   :contributions:
   :exclude: dependabot[bot], pre-commit-ci[bot]
   :limit: 5

Including additional contributors
---------------------------------

Manually add contributors not detected by the API (e.g., ``Co-authored-by`` contributors):

.. code-block:: rst

   .. contributors:: dgarcia360/sphinx-contributors
      :include: Peque
      :limit: 5

.. contributors:: dgarcia360/sphinx-contributors
   :include: Peque
   :limit: 5

Multiple repositories
---------------------

Merge contributors from multiple repositories into a single list. Contribution counts are summed for users who appear in more than one repository:

.. code-block:: rst

   .. contributors:: dgarcia360/sphinx-contributors dgarcia360/sphinx-collapse
      :contributions:
      :limit: 5

.. contributors:: dgarcia360/sphinx-contributors dgarcia360/sphinx-collapse
   :contributions:
   :limit: 5

For more information on how to style the list, see :doc:`Customization <customization>`.
