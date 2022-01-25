"""
Tests for collapse extension.
(c) 2022 - present David Garcia (@dgarcia360)
# This code is licensed under MIT license (see LICENSE.md for details)
"""

import subprocess
import sys
from pathlib import Path
from textwrap import dedent

from src.sphinx_contributors import Contributor, ContributorsRepository

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


def test_contributor_directive(tmp_path: Path) -> None:
    """
    The ``contributors`` directive runs with no errors.
    """
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
        .. contributors:: sphinx-doc/sphinx
        """,
    )
    source_file.write_text(source_file_content)
    destination_directory = tmp_path / "destination"
    args = [
        sys.executable,
        "-m",
        "sphinx",
        "-b",
        "html",
        "-W",
        # Directory containing source and configuration files.
        str(source_directory),
        # Directory containing build files.
        str(destination_directory),
        # Source file to process.
        str(source_file),
    ]
    result = subprocess.run(
        args=args,
        check=False,
        stderr=subprocess.PIPE,
    )
    assert result.returncode == 0
