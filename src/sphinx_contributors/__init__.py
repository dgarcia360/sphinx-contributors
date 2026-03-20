"""
Contributors extension for Sphinx.
(c) 2018 - present David Garcia (@dgarcia360)
# This code is licensed under MIT license (see LICENSE.md for details)
"""

__version__ = "0.2.7"

from pathlib import Path

import requests
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util import logging

logger = logging.getLogger(__name__)


class Contributor:
    def __init__(self, login, url, contributions=0, avatar_url=""):
        self.contributions = contributions
        self.login = login
        self.url = url
        self.contributions = contributions
        self.avatar_url = avatar_url

    def build(self, class_name):
        container_class = class_name + "_contributor"
        image_class = container_class + "__image"
        username_class = container_class + "__username"
        contributions_class = container_class + "__contributions"

        node_container = nodes.container(classes=[container_class])

        if self.avatar_url:
            node_container += nodes.image(uri=self.avatar_url, classes=[image_class])

        node_username = nodes.paragraph(classes=[username_class])
        node_username += nodes.reference(text=self.login, refuri=self.url)
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
    def __init__(self, contributors, reverse=True, limit=10, exclude=[], avatars=False):
        self.contributors = sorted(
            [c for c in contributors if c.login not in exclude],
            key=lambda c: c.contributions,
            reverse=reverse,
        )[:limit]
        self.avatars = avatars

    def build(self, class_name):
        list_class = class_name + "_list"
        item_class = list_class + "__item"

        node_container = nodes.container(classes=[class_name])
        if self.avatars:
            node_container["classes"].append(class_name + "--avatars")
        node_list = nodes.bullet_list(classes=[list_class])

        for contributor in self.contributors:
            node_item = nodes.list_item(classes=[item_class])
            node_item += contributor.build(class_name)
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
        "class_name": directives.unchanged,
        "contributions": directives.flag,
        "exclude": directives.unchanged,
        "limit": directives.positive_int,
        "order": directives.unchanged,
    }

    def run(self):
        use_avatars = "avatars" in self.options
        class_name = self.options.get("class_name", "sphinx-contributors")
        show_contributions = "contributions" in self.options
        exclude = [_exclude.strip() for _exclude in self.options.get("exclude", "").split(",")]
        limit = self.options.get("limit", 10)
        order = self.options.get("order", "DESC") == "DESC"

        contributors = []
        try:
            r = requests.get(
                "https://api.github.com/repos/"
                + self.arguments[0]
                + "/contributors?per_page=100"
            )
            contributors = list(
                map(
                    lambda c: Contributor(
                        c.get("login"),
                        c.get("html_url"),
                        c.get("contributions") if show_contributions else 0,
                        c.get("avatar_url") if use_avatars else "",
                    ),
                    r.json(),
                )
            )
        except Exception:
            logger.warning("The repository " + self.arguments[0] + " does not exist.")
        return [
            ContributorsRepository(
                contributors,
                reverse=order,
                limit=limit,
                exclude=exclude,
                avatars=use_avatars,
            ).build(class_name)
        ]


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
