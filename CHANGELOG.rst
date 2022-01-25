=========
Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

[0.2.5] - 25 January 2022
=========================

Added
-----

- Default CSS for lists.

[0.2.4] - 21 January 2022
=========================

Added
-----

- Linting with pre-commit.

Updated
-------

- Breaking change: The package is now named ``sphinx-contributors``.
- Breaking change: The required Sphinx version is at least 3.0.
- Replaced Travis CI for GitHub Actions.
- Replaced ``setup.py`` for ``pyproject.toml``.

[0.2.3] - 25 November 2021
==========================

Added
-----

* [#1](https://github.com/dgarcia360/sphinx-contributors/issues/1): The directive supports an option to render contributor's avatars - thanks @segfaultxavi!
* [#3])(https://github.com/dgarcia360/sphinx-contributors/issues/3): The docs now explain how to render contributors in a grid view.
* [#4](https://github.com/dgarcia360/sphinx-contributors/issues/4): The directive supports an option to hide the number of commits done by a contributor.
* [#13](https://github.com/dgarcia360/sphinx-contributors/issues/13): Docs for this extesion are now hosted on ReadTheDocs.

Updated
-------

* The extension now raises a warning instead of an error if the repository cannot be retrieved. This is especially useful when trying to build docs without internet connection.

[0.2.2] - 03 August 2019
========================

Added
-----

* [#2](https://github.com/dgarcia360/sphinx-contributors/issues/2): The directive supports an option to limit the number of contributors.
* The directive supports an option to sort contributors per number of commits.
* The directive supports an option to exclude usernames from the contributors' list.

Changed
--------

* Before, the repository name was passed as an option. Now, the directive accepts the repository name as an argument.


[0.1.0] - 18 July 2018
=======================

Added
-----

* Initial code release
