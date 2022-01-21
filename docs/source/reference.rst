Reference
=========

Contributors directive
======================

.. rst:directive:: .. contributors:: username/repository

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
