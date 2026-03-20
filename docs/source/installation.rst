Installation
============

.. important:: sphinx-contributors is compatible with Sphinx 7.0+ using Python 3.10+.

#. Install ``sphinx-contributors`` using PIP.

   .. code-block:: bash

      pip install sphinx-contributors

#. Add the extension to your Sphinx project ``conf.py`` file.

   .. code-block:: python

      extensions = ['sphinx_contributors']

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
