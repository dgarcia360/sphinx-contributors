Installation
============

.. important:: sphinx-contributors is compatible with Sphinx 7.0+ using Python 3.10+.

Getting started
---------------

Follow these steps to add sphinx-contributors to your Sphinx project:

#. Install ``sphinx-contributors`` using PIP.

   .. code-block:: bash

      pip install sphinx-contributors

#. Add the extension to your Sphinx project ``conf.py`` file.

   .. code-block:: python

      extensions = ['sphinx_contributors']

#. Add a ``contributors`` directive to any ``.rst`` file.

   .. code-block:: rst

      .. contributors:: dgarcia360/sphinx-contributors
         :avatars:

   This renders all contributors with their avatars (use ``:limit:`` to show fewer):

   .. contributors:: dgarcia360/sphinx-contributors
      :avatars:

   See :doc:`Examples <examples>` for all available options.

GitHub API rate limits
----------------------

This extension uses the GitHub REST API. Unauthenticated requests are limited to **60 per hour**. Each ``contributors`` directive makes at least one API call, and options like ``:names:`` or ``:include:`` make additional calls per contributor. If you hit the rate limit, contributor lists will appear empty until it resets.

To increase the limit to **5,000 requests per hour**, set a ``GITHUB_TOKEN`` environment variable with a `GitHub personal access token <https://github.com/settings/tokens>`_. A fine-grained token with no extra permissions is sufficient for public repositories.

.. code-block:: bash

   # Locally
   export GITHUB_TOKEN=ghp_your_token_here

For CI/CD environments like **ReadTheDocs**, add the token as an environment variable in your project settings. For **GitHub Actions**, use a repository secret:

.. code-block:: yaml

   - name: Build docs
     env:
       GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
     run: make -C docs dirhtml
