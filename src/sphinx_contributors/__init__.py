"""
Contributors extension for Sphinx.
(c) 2018 - present David Garcia (@dgarcia360)
# This code is licensed under MIT license (see LICENSE.md for details)
"""

__version__ = "0.3.0"

import copy
import os
from os import path
from pathlib import Path
from docutils.parsers.rst import Directive, directives
from sphinx.util import logging, osutil

from .contributors import ContributorsRepository
from .repository import Repository


DEFAULT_CONTRIBUTORS_CONF = {
    "default_avatar" : "sc_user_avartar_default.svg",
}


def sc_path_static():
    """Returns path to packaged static files"""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "_static"))


def sc_path_static_append(app) :
    contributors_config = app.config.sphinx_contributors_conf

    if contributors_config['default_avatar'] == DEFAULT_CONTRIBUTORS_CONF['default_avatar']:
        contributors_config['default_avatar'] = Path(
                                                os.path.relpath(
                                                  os.path.join(sc_path_static(), contributors_config['default_avatar']),
                                                  app.builder.srcdir
                                                )
                                             ).as_posix()


def fill_contributors_conf_defaults(app, config, check_keys = True):
    """Handle user config"""
    contributors_conf = copy.deepcopy(DEFAULT_CONTRIBUTORS_CONF)
    contributors_conf.update(config.sphinx_contributors_conf)

    config.sphinx_contributors_conf = contributors_conf

    config.html_static_path.append(sc_path_static())


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
        "anonymous": directives.flag,
        "order": directives.unchanged,
        "provider": directives.unchanged,
    }

    def run(self):
        config = self.state.document.settings.env.config.sphinx_contributors_conf

        contributors_options = {
            # pass over and pre-process options taken from the directive call
            'provider' : self.options.get("provider", "github"),
            # compile list of additional users to exclude/exclude
            'exclude' : [
                _exclude.strip() for _exclude in self.options.get("exclude", "").split(",")
            ],
            'include' : [
                _include.strip()
                for _include in self.options.get("include", "").split(",")
                if _include.strip()
            ],
            'reverse' : self.options.get("order", "DESC") == "DESC",
            'rst_dir' : os.path.dirname(self.state_machine.document.attributes['source'])
                        if self.state_machine.document.attributes['source'] else ".",
            'anonymous' :  "anonymous" in self.options,
            'show_names' : "names" in self.options,
            'show_contributions' : "contributions" in self.options,
            'avatars_only' : "avatars_only" in self.options,
            'show_avatars' : "avatars" in self.options or "avatars_only" in self.options,
            'default_avatar' : config.get('default_avatar', ""),
            # store path to invoking rst source file in addition
            # to the other options set by this call of the contributors
            # directive
            'rst_source' : self.state_machine.document.attributes['source'],
            'limit': self.options.get('limit', None)
        }

        contributors_by_login = {}

        for r in self.arguments[0].split():
            repo = Repository(r, options = contributors_options)

            for k, v in repo.get_contributors().items():
                if k not in contributors_by_login:
                    contributors_by_login[k] = v
                else:
                    contributors_by_login[k].update(v)

        contributors = list(contributors_by_login.values())

        repo = ContributorsRepository(
            contributors,
            options = contributors_options,
            config = config
        )

        class_name = self.options.get("class_name", "sphinx-contributors")

        return [repo.build(class_name)]


def setup(app):
    app.add_config_value('sphinx_contributors_conf', DEFAULT_CONTRIBUTORS_CONF, 'html')

    # Early filling of sphinx_gallery_conf defaults at config-inited
    app.connect("config-inited", fill_contributors_conf_defaults, priority=10)
    app.connect("builder-inited", sc_path_static_append)
    #app.connect('env-updated', install_static_files)

    # Add directive
    app.add_directive("contributors", ContributorsDirective)

    # Add CSS
    app.add_css_file("sphinx_contributors.css")

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
