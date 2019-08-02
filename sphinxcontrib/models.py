# -*- encoding: utf-8 -*-
#
# (c) 2018-present David Garcia (@dgarcia360)
# This code is licensed under MIT license (see LICENSE.md for details)


from docutils import nodes


class Contributor:

    def __init__(self, login, url, contributions=0):
        self.contributions = contributions
        self.login = login
        self.url = url
        self.contributions = contributions

    def build(self):
        node_contributor = nodes.paragraph()
        node_contributor += nodes.reference(text=self.login, refuri=self.url)
        node_contributor += nodes.Text(' - ' + str(self.contributions) + ' ' +
                                       ('contributions' if self.contributions != 1 else 'contribution'))
        return node_contributor


class ContributorsRepository:

    def __init__(self, contributors, reverse=True, limit=10, exclude=[]):
        self.contributors = sorted([c for c in contributors if c.login not in exclude],
                                   key=lambda c: c.contributions,
                                   reverse=reverse)[:limit]

    def build(self):
        node_list = nodes.bullet_list()
        for contributor in self.contributors:
            node_contributor = nodes.list_item()
            node_contributor += contributor.build()
            node_list += node_contributor
        return node_list
