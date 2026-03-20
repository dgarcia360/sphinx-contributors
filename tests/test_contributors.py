"""
Tests for sphinx-contributors extension.
(c) 2022 - present David Garcia (@dgarcia360)
# This code is licensed under MIT license (see LICENSE.md for details)
"""

from pathlib import Path
from textwrap import dedent
from unittest.mock import MagicMock, patch

from sphinx.application import Sphinx

from sphinx_contributors import Contributor, ContributorsRepository

_CLASS_NAME = "sphinx_contributors"


def test_contributor_build() -> None:
    """
    Initializing a contributor.
    """
    contributor = Contributor("dgarcia360", "http://#", contributions=10).build(
        _CLASS_NAME
    )
    assert contributor.astext() == "dgarcia360\n\n10 contributions"


def test_contributor_build_with_no_contribution() -> None:
    """
    Create a contributor with no contributions.
    """
    contributor = Contributor("dgarcia360", "http://#").build(_CLASS_NAME)
    assert contributor.astext() == "dgarcia360"


def test_contributor_build_with_one_contribution() -> None:
    """
    Create a contributor with one contribution.
    """
    contributor = Contributor("dgarcia360", "http://#", contributions=1).build(
        _CLASS_NAME
    )
    assert contributor.astext() == "dgarcia360\n\n1 contribution"


def test_contributor_repository_build() -> None:
    """
    Initializing a repository build.
    """
    contributors = [
        Contributor("dgarcia360", "http://#", contributions=2),
        Contributor("user", "http://#", contributions=1),
    ]
    contributor_repository = ContributorsRepository(contributors, reverse=True).build(
        _CLASS_NAME
    )
    assert (
        contributor_repository.astext()
        == "dgarcia360\n\n2 contributions\n\nuser\n\n1 contribution"
    )


def test_contributor_repository_build_empty() -> None:
    """
    Initializing a contributor repository with no contributors.
    """
    contributors = []
    contributor_repository = ContributorsRepository(contributors, reverse=True).build(
        _CLASS_NAME
    )
    assert contributor_repository.astext() == ""


def test_contributor_repository_build_order_desc() -> None:
    """
    The sort option (descending).
    """
    contributors = [
        Contributor("user", "http://#", contributions=1),
        Contributor("dgarcia360", "http://#", contributions=2),
    ]
    contributor_repository = ContributorsRepository(contributors, reverse=True).build(
        _CLASS_NAME
    )
    assert (
        contributor_repository.astext()
        == "dgarcia360\n\n2 contributions\n\nuser\n\n1 contribution"
    )


def test_contributor_repository_build_order_asc() -> None:
    """
    The sort option works (ascending).
    """
    contributors = [
        Contributor("dgarcia360", "http://#", contributions=2),
        Contributor("user", "http://#", 1),
    ]
    contributor_repository = ContributorsRepository(contributors, reverse=False).build(
        _CLASS_NAME
    )
    assert (
        contributor_repository.astext()
        == "user\n\n1 contribution\n\ndgarcia360\n\n2 contributions"
    )


def test_contributor_repository_build_with_limit() -> None:
    """
    The limit option works.
    """
    contributors = [
        Contributor("dgarcia360", "http://#", contributions=2),
        Contributor("user", "http://#", contributions=1),
    ]
    contributor_repository = ContributorsRepository(
        contributors, reverse=True, limit=1
    ).build(_CLASS_NAME)
    assert contributor_repository.astext() == "dgarcia360\n\n2 contributions"


def test_contributor_repository_build_exclude() -> None:
    """
    The exclude option works.
    """
    contributors = [
        Contributor("dgarcia360", "http://#", contributions=2),
        Contributor("sphinx", "http://#", contributions=1),
        Contributor("user", "http://#", contributions=1),
    ]
    exclude = "sphinx,user"
    contributor_repository = ContributorsRepository(
        contributors, reverse=True, limit=10, exclude=exclude
    ).build(_CLASS_NAME)
    assert contributor_repository.astext() == "dgarcia360\n\n2 contributions"


@patch("sphinx_contributors.requests.get")
def test_contributor_directive(mock_get, tmp_path: Path) -> None:
    """
    The ``contributors`` directive runs with no errors.

    Uses a mocked GitHub API response so the test works without network access.
    """
    mock_response = MagicMock()
    mock_response.json.return_value = [
        {
            "login": "testuser",
            "html_url": "https://github.com/testuser",
            "contributions": 42,
            "avatar_url": "https://github.com/testuser.png",
        },
    ]
    mock_get.return_value = mock_response

    source_directory = tmp_path / "source"
    source_directory.mkdir()
    source_file = source_directory / "index.rst"
    conf_py = source_directory / "conf.py"
    conf_py.touch()
    source_file.touch()
    conf_py_content = dedent(
        """\
        extensions = ['sphinx_contributors']
        """,
    )
    conf_py.write_text(conf_py_content)
    source_file_content = dedent(
        """\
        Test
        ====

        .. contributors:: sphinx-doc/sphinx
        """,
    )
    source_file.write_text(source_file_content)
    destination_directory = tmp_path / "destination"
    doctree_directory = tmp_path / "doctrees"

    app = Sphinx(
        srcdir=str(source_directory),
        confdir=str(source_directory),
        outdir=str(destination_directory),
        doctreedir=str(doctree_directory),
        buildername="html",
        warningiserror=True,
    )
    app.build()

    assert app.statuscode == 0
    mock_get.assert_called_once()
