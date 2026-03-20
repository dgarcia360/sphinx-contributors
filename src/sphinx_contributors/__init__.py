"""
Contributors extension for Sphinx.
(c) 2018 - present David Garcia (@dgarcia360)
# This code is licensed under MIT license (see LICENSE.md for details)
"""

__version__ = "0.3.0"

import os
from pathlib import Path

import requests
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util import logging

logger = logging.getLogger(__name__)


def _github_headers():
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return {"Authorization": "token " + token}
    return {}


def _github_get_paginated(url):
    results = []
    headers = _github_headers()
    while url:
        r = requests.get(url, headers=headers)
        results.extend(r.json())
        url = r.links.get("next", {}).get("url")
    return results


class Contributor:
    def __init__(self, login, url, contributions=0, avatar_url="", name=""):
        self.contributions = contributions
        self.login = login
        self.url = url
        self.avatar_url = avatar_url
        self.name = name

    @property
    def display_name(self):
        return self.name or self.login

    def build(self, class_name, avatars_only=False):
        container_class = class_name + "_contributor"
        image_class = container_class + "__image"
        username_class = container_class + "__username"
        contributions_class = container_class + "__contributions"

        node_container = nodes.container(classes=[container_class])

        if self.avatar_url:
            node_image = nodes.image(
                uri=self.avatar_url,
                alt=self.display_name,
                classes=[image_class],
            )
            node_image_link = nodes.reference("", refuri=self.url)
            node_image_link += node_image
            node_container += node_image_link

        if avatars_only:
            return node_container

        node_username = nodes.paragraph(classes=[username_class])
        node_username += nodes.reference(text=self.display_name, refuri=self.url)
        node_container += node_username

        if self.contributions:
            node_contributions = nodes.paragraph(classes=[contributions_class])
            node_contributions += nodes.Text(
                str(self.contributions)
                + (" contributions" if self.contributions != 1 else " contribution"),
            )
            node_container += node_contributions
        return node_container


class ContributorsRepository:
    def __init__(
        self,
        contributors,
        reverse=True,
        limit=None,
        exclude=[],
        avatars=False,
        avatars_only=False,
    ):
        sorted_contributors = sorted(
            [c for c in contributors if c.login not in exclude],
            key=lambda c: c.contributions,
            reverse=reverse,
        )
        self.contributors = (
            sorted_contributors[:limit] if limit else sorted_contributors
        )
        self.avatars = avatars
        self.avatars_only = avatars_only

    def build(self, class_name):
        list_class = class_name + "_list"
        item_class = list_class + "__item"

        node_container = nodes.container(classes=[class_name])
        if self.avatars or self.avatars_only:
            node_container["classes"].append(class_name + "--avatars")
        node_list = nodes.bullet_list(classes=[list_class])

        for contributor in self.contributors:
            node_item = nodes.list_item(classes=[item_class])
            node_item += contributor.build(class_name, avatars_only=self.avatars_only)
            node_list += node_item
        node_container += node_list
        return node_container


class ContributorsDirective(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        "avatars": directives.flag,
        "avatars_only": directives.flag,
        "class_name": directives.unchanged,
        "contributions": directives.flag,
        "exclude": directives.unchanged,
        "include": directives.unchanged,
        "limit": directives.positive_int,
        "names": directives.flag,
        "order": directives.unchanged,
    }

    def run(self):
        avatars_only = "avatars_only" in self.options
        use_avatars = "avatars" in self.options or avatars_only
        class_name = self.options.get("class_name", "sphinx-contributors")
        show_contributions = "contributions" in self.options
        show_names = "names" in self.options
        exclude = [
            _exclude.strip() for _exclude in self.options.get("exclude", "").split(",")
        ]
        include = [
            _include.strip()
            for _include in self.options.get("include", "").split(",")
            if _include.strip()
        ]
        limit = self.options.get("limit", None)
        order = self.options.get("order", "DESC") == "DESC"

        repositories = self.arguments[0].split()
        contributors_by_login = {}
        for repo_name in repositories:
            try:
                results = _github_get_paginated(
                    "https://api.github.com/repos/"
                    + repo_name
                    + "/contributors?per_page=100"
                )
                for c in results:
                    login = c.get("login")
                    if login in contributors_by_login:
                        if show_contributions:
                            contributors_by_login[login].contributions += c.get(
                                "contributions", 0
                            )
                    else:
                        contributors_by_login[login] = Contributor(
                            login,
                            c.get("html_url"),
                            c.get("contributions") if show_contributions else 0,
                            c.get("avatar_url") if use_avatars else "",
                        )
            except Exception:
                logger.warning("The repository " + repo_name + " does not exist.")
        contributors = list(contributors_by_login.values())

        existing_logins = {c.login for c in contributors}
        for login in include:
            if login in existing_logins:
                continue
            try:
                user = requests.get(
                    "https://api.github.com/users/" + login,
                    headers=_github_headers(),
                ).json()
                contributors.append(
                    Contributor(
                        login,
                        user.get("html_url", "https://github.com/" + login),
                        0,
                        user.get("avatar_url", "") if use_avatars else "",
                    )
                )
            except Exception:
                logger.warning("Could not fetch user: " + login)

        repo = ContributorsRepository(
            contributors,
            reverse=order,
            limit=limit,
            exclude=exclude,
            avatars=use_avatars,
            avatars_only=avatars_only,
        )

        if show_names:
            for contributor in repo.contributors:
                try:
                    user = requests.get(
                        "https://api.github.com/users/" + contributor.login,
                        headers=_github_headers(),
                    ).json()
                    contributor.name = user.get("name") or ""
                except Exception:
                    pass

        return [repo.build(class_name)]


def setup(app):
    # Add directive
    app.add_directive("contributors", ContributorsDirective)
    # Add CSS
    static_dir = str(Path(__file__).parent.joinpath("_static").absolute())
    app.connect(
        "builder-inited", (lambda app: app.config.html_static_path.append(static_dir))
    )
    app.add_css_file("sphinx_contributors.css")

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
