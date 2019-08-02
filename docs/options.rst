=======
Options
=======

.. code-block:: rst

    ..  ghcontributors:: sphinxcontrib-ghcontributors
        :limit: 10
        :order: ASC
        :exclude: dgarcia360,sphinx

.. list-table:: Directive Options
   :widths: 15 10 30
   :header-rows: 1

   * - Option
     - Value
     - Description
   * - limit
     - int
     - Maximum number of users to render. Default value is ``10``, and the maximum value is ``100``.
   * - order
     - DESC or ASC
     - Show most active or least active contributors. Default value is ``DESC``.
   * - exclude
     - string
     - List of usernames to exclude from the list. Separate multiple usernames with commas.