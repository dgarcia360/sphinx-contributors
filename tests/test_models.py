# -*- encoding: utf-8 -*-
#
# (c) 2018 David Garcia (@dgarcia360)
# This code is licensed under MIT license (see LICENSE.md for details)


from sphinxcontrib.models import Contributor, ContributorsRepository


class TestModels(object):

    def test_contributor_build(self):
        contributor = Contributor('dgarcia360', 'http://#', 10).build()
        assert contributor.astext() == 'dgarcia360 - 10 contributions'

    def test_contributor_build_with_one_contribution(self):
        contributor = Contributor('dgarcia360', 'http://#', 1).build()
        assert contributor.astext() == 'dgarcia360 - 1 contribution'

    def test_contributor_repository_build(self):
        contributors = [Contributor('dgarcia360', 'http://#', 2),
                        Contributor('user', 'http://#', 1)]
        contributor_repository = ContributorsRepository(contributors, reverse=True).build()
        assert contributor_repository.astext() == 'dgarcia360 - 2 contributions\n\nuser - 1 contribution'

    def test_contributor_repository_build_empty(self):
        contributors = []
        contributor_repository = ContributorsRepository(contributors, reverse=True).build()
        assert contributor_repository.astext() == ''

    def test_contributor_repository_build_order_desc(self):
        contributors = [Contributor('user', 'http://#', 1),
                        Contributor('dgarcia360', 'http://#', 2)]
        contributor_repository = ContributorsRepository(contributors, reverse=True).build()
        assert contributor_repository.astext() == 'dgarcia360 - 2 contributions\n\nuser - 1 contribution'

    def test_contributor_repository_build_order_asc(self):
        contributors = [Contributor('dgarcia360', 'http://#', 2),
                        Contributor('user', 'http://#', 1)]
        contributor_repository = ContributorsRepository(contributors, reverse=False).build()
        assert contributor_repository.astext() == 'user - 1 contribution\n\ndgarcia360 - 2 contributions'

    def test_contributor_repository_build_with_limit(self):
        contributors = [Contributor('dgarcia360', 'http://#', 2),
                        Contributor('user', 'http://#', 1)]
        contributor_repository = ContributorsRepository(contributors, reverse=True, limit=1).build()
        assert contributor_repository.astext() == 'dgarcia360 - 2 contributions'

    def test_contributor_repository_build_exclude(self):
        contributors = [Contributor('dgarcia360', 'http://#', 2),
                        Contributor('sphinx', 'http://#', 1),
                        Contributor('user', 'http://#', 1)]
        exclude = 'sphinx,user'
        contributor_repository = ContributorsRepository(contributors, reverse=True, limit=10, exclude=exclude).build()
        assert contributor_repository.astext() == 'dgarcia360 - 2 contributions'
