# -*- encoding: utf-8 -*-
#
# (c) 2018-present David Garcia (@dgarcia360)
# This code is licensed under MIT license (see LICENSE.md for details)


import requests
from docutils.parsers.rst import directives, Directive
from .models import ContributorsRepository, Contributor


class ContributorsDirective(Directive):

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        'limit': directives.positive_int,
        'order': directives.unchanged,
        'exclude': directives.unchanged,
    }

    def run(self):
        limit = self.options.get('limit', 10)
        order = self.options.get('order', 'DESC') == 'DESC'
        exclude = self.options.get('exclude', '').split(",")

        r = requests.get('https://api.github.com/repos/' + self.arguments[0] + '/contributors?per_page=100')
        if type(r.json()) == dict:
            raise ValueError('The repository ' + self.arguments[0] + ' does not exist.')
        contributors = list(map(lambda c: Contributor(c.get('login'),
                                                      c.get('html_url'),
                                                      c.get('contributions')), r.json()))
        return [ContributorsRepository(contributors, reverse=order, limit=limit, exclude=exclude).build()]


def setup(app):
    app.add_directive('ghcontributors', ContributorsDirective)
