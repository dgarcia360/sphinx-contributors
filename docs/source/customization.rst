Customization
-------------

The directive ``contributors`` generates an ``<ul>`` node with class ``contributors``.
This makes the list is highly customizable through CSS.

.. tip:: See how to `add custom CSS to Sphinx Documentation <https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html>`_.

For example, the following CSS snippet turns the list into a grid:

.. code-block:: css

  .contributors {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
  }

  .contributors li {
      list-style: none;
      text-align: center;
  }

  .contributors li a {
      display: block;
  }

And, the following one sets a maximum width for avatar images:

.. code-block:: css

  .contributors li img {
      max-width: 150px;
  }
