"""
Contributors extension for Sphinx.
(c) 2018 - present David Garcia (@dgarcia360)
# This code is licensed under MIT license (see LICENSE.md for details)
"""

__version__ = "0.2.4"

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

    def build(self):
        node_contributor = nodes.paragraph()
        if self.avatar_url:
            node_contributor += nodes.image(uri=self.avatar_url)
        node_contributor += nodes.reference(text=self.login, refuri=self.url)
        if self.contributions:
            node_contributor += nodes.Text(
                " - "
                + str(self.contributions)
                + " "
                + ("contributions" if self.contributions != 1 else "contribution")
            )
        return node_contributor


class ContributorsRepository:
    def __init__(self, contributors, reverse=True, limit=10, exclude=[]):
        self.contributors = sorted(
            [c for c in contributors if c.login not in exclude],
            key=lambda c: c.contributions,
            reverse=reverse,
        )[:limit]

    def build(self):
        node_list = nodes.bullet_list()
        node_list["classes"].append("contributors")
        for contributor in self.contributors:
            node_contributor = nodes.list_item()
            node_contributor += contributor.build()
            node_list += node_contributor
        return node_list


class ContributorsDirective(Directive):

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        "limit": directives.positive_int,
        "order": directives.unchanged,
        "exclude": directives.unchanged,
        "avatars": directives.flag,
        "contributions": directives.flag,
    }

    def run(self):
        limit = self.options.get("limit", 10)
        order = self.options.get("order", "DESC") == "DESC"
        exclude = self.options.get("exclude", "").split(",")
        use_avatars = "avatars" in self.options
        show_contributions = "contributions" in self.options

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
                contributors, reverse=order, limit=limit, exclude=exclude
            ).build()
        ]


def setup(app):
    app.add_directive("contributors", ContributorsDirective)
