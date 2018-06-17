from sphinxcontrib.ghcontributors import _render_contributor, _render_contributors_list, _get_gh_contributors


class TestContributorsDirective(object):

    def test_render_contributor(self):

        contributor = {'login': 'dgarcia360', 'contributions': 10, 'htmlurl': 'http://#'}
        rendered_contributor = _render_contributor(contributor)
        assert rendered_contributor.astext() == 'dgarcia360 - 10 contributions'

    def test_render_contributor_singular(self):

        contributor = {'login': 'dgarcia360', 'contributions': 1, 'htmlurl': 'http://#'}
        rendered_contributor = _render_contributor(contributor)
        assert rendered_contributor.astext() == 'dgarcia360 - 1 contribution'

    def test_render_contributors_list(self):

        contributors = [{'login': 'dgarcia360', 'contributions': 2, 'htmlurl': 'http://#'},
                        {'login': 'user', 'contributions': 1, 'htmlurl': 'http://#'}]
        rendered_contributors_list = _render_contributors_list(contributors)
        assert rendered_contributors_list.astext() == 'dgarcia360 - 2 contributions\n\nuser - 1 contribution'

    def test_get_gh_contributors_repository_not_exists(self):

        contributors = _get_gh_contributors('dgarcia360', 'reponotfound')
        assert contributors == []
