Customization
-------------

The directive ``contributors`` generates an ``<ul>`` node with class ``sphinx-contributors``.
This makes the list is highly customizable through CSS.

.. tip:: See how to `add custom CSS to Sphinx Documentation <https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html>`_.

For example, the following CSS snippet makes the images round and smaller:

.. code-block:: css

  .sphinx-contributors img {
      border-radius: 50%;
      max-width: 60px;
  }

.. rst-class:: custom-contributors

.. contributors:: sphinx-doc/sphinx
    :avatars:
    :exclude: dgarcia360,sphinx
    :limit: 5
    :order: DESC
