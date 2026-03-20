Reference
=========

Contributors directive
----------------------

.. rst:directive:: .. contributors:: username/repository [username/repository ...]

    One or more GitHub repositories, separated by spaces. When multiple repositories are specified, contributors are merged into a single list and contribution counts are summed for users who appear in more than one repository.

    .. code-block:: rst

       .. contributors:: dgarcia360/sphinx-contributors dgarcia360/other-repo
          :contributions:

    .. versionchanged:: 0.2.8
       Multiple repositories can now be specified.

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

    .. rst:directive:option:: names
      :type: boolean

      Whether to display real names (fetched from GitHub user profiles) instead of usernames. Falls back to the username if the user has not set a name on their GitHub profile.

      .. versionadded:: 0.2.8

    .. rst:directive:option:: include
      :type: string

      Comma separated GitHub usernames to add to the list of contributors. This is useful for including people who contributed via ``Co-authored-by`` commit trailers, since the GitHub REST API does not count those as contributors. Already listed contributors are not duplicated. For example: ``dgarcia360,otheruser``.

      .. versionadded:: 0.2.8

    .. rst:directive:option:: exclude
      :type: string

      Comma seperated usernames to exlude from the list of contributors, for example: ``dependabot[bot],pre-commit-ci[bot]``.

      .. versionadded:: 0.2.0

    .. note::

       The GitHub REST API used by this extension does not include contributors added via ``Co-authored-by`` commit trailers. Use the ``:include:`` option to manually add those contributors.
