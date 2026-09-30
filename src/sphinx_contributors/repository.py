import os
import re
import requests
import subprocess

from sphinx.util import logging

from .contributors import Contributor

logger = logging.getLogger(__name__)

email_pat = re.compile(r"(.*)\s+\<(.*)\>")


def _github_headers():
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return {"Authorization": "token " + token}
    return {}


def _github_get_paginated(url):
    results = []
    headers = _github_headers()
    while url:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()

        j = r.json()
        results.extend(r.json())

        url = r.links.get("next", {}).get("url")
    return results


def get_github_contributors(repo_name, options = {}):
    """
    Get all contributors from a github repository

    This function retrieves all contributors of a github.com hosted repository
    by querying the github API. It creates a dictionary of Contributor objects
    where the key is the contributors github login.
    If anonymous contributors are requested as well, i.e. contributors without
    a github login, their respective email address is used as key.
    """
    contributors = {}
    list_anonymous = options.get('anonymous', False)
    exclude = options.get('exclude', [])
    default_avatar = options.get('default_avatar', "")

    try:
        results = _github_get_paginated(
            f"https://api.github.com/repos/{repo_name}" \
            f"/contributors?per_page=100{'&anon=1' if list_anonymous else ''}"
        )

        for c in results:
            ctype = c.get("type", "")
            anonymous = False

            if ctype == "User":
                login = c.get("login")
            elif list_anonymous and ctype == "Anonymous":
                login = c.get("email")
                anonymous = True
            else:
                continue

            if login in exclude:
                continue

            html_url = c.get("html_url")
            contributions = c.get("contributions", 0)
            email = c.get("email", "")
            avatar = c.get("avatar_url", default_avatar)
            name = c.get("name", "")

            contributors[login] = Contributor(
                    login         = login,
                    url           = html_url,
                    contributions = contributions,
                    avatar_url    = avatar,
                    name          = name,
                    email         = email,
                    anonymous     = anonymous
                )
    except requests.exceptions.HTTPError as err:
        logger.warning(f"Error while retrieving data from github repository \"{repo_name}\" {err=}, {type(err)=}")
    except Exception as err:
        logger.warning(f"Error while decoding data from github repository \"{repo_name}\" {err=}, {type(err)=}")

    return contributors


def get_github_user_data(login, options = {}):
    try:
        r = requests.get(
            "https://api.github.com/users/" + login,
            headers=_github_headers(),
            timeout=10
        )

        r.raise_for_status()

        user = r.json()

        return Contributor(
                    login         = login,
                    url           = user.get("html_url", "https://github.com/" + login),
                    contributions = 0,
                    avatar_url    = user.get("avatar_url", options.get('default_avatar', "")),
                    name          = user.get("name", ""),
                    email         = user.get("email", ""),
                    anonymous     = False
                )
    except requests.exceptions.HTTPError as err:
        logger.warning(f"Error while retrieving user data for github login \"{login}\" {err=}, {type(err)=}")

    return None


def _git_shortlog(repo_name):
    try:
        r = subprocess.run(['git',
                            '-C', repo_name,
                            'shortlog',
                            '--summary',
                            '--numbered',
                            '--email'
                           ],
                           stdout=subprocess.PIPE,
                           timeout = 120)
        r.check_returncode()

        return r.stdout.decode()

    except subprocess.TimeoutExpired as err:
        logger.warning(f"git shorlog call timeout for local repo \"{repo_name}\" {err=}, {type(err)=}")
    except subprocess.CalledProcessError as err:
        logger.warning(f"git shorlog call was unsuccessful for local repo \"{repo_name}\" {err=}, {type(err)=}")
    except OSError as err:
        logger.warning(f"Error while calling git shortlog for local repo \"{repo_name}\" {err=}, {type(err)=}")

    return None


def get_local_contributors(repo_name, options = {}):
    contributors = {}

    rst_dir = options['rst_dir'] if 'rst_dir' in options else '.'
    exclude = options['exclude'] if 'exclude' in options else []
    default_avatar = options['default_avatar'] if 'default_avatar' in options else ""

    repo_path = os.path.join(rst_dir, repo_name)
    results = _git_shortlog(repo_path)

    if results is None:
        return contributors

    for r in results.split("\n"):
        rr = r.strip().split("\t")
        if len(rr) > 1:
            count, contributor = r.strip().split("\t")
            m = email_pat.match(contributor)
            if m:
                name, email = m.group(1), m.group(2)

                if name in exclude or email in exclude:
                    continue

                c = Contributor(
                      login         = email,
                      url           = "",
                      contributions = int(count),
                      name          = name,
                      email         = email,
                      avatar_url    = default_avatar,
                      anonymous     = True
                    )

                if email in contributors:
                    contributors[email].update(c)
                else:
                    contributors[email] = c

    return contributors


class Repository:
    def __init__(self, url, options = {}):
        self.url = url
        self.options = options
        self._get_contributors = None
        self._fill_user_data = None

        provider = options.get('provider', "github")

        if provider == "github":
            self._get_contributors = get_github_contributors
            self._fill_user_data = get_github_user_data
        elif provider == "local":
            self._get_contributors = get_local_contributors


    def get_contributors(self):
        """
        Query github reposirtory to get list of contributors
        """
        contributors = {}

        if callable(self._get_contributors):
            contributors = self._get_contributors(self.url, options = self.options)

        if callable(self._fill_user_data):
            # get more contributor data
            if self.options.get("show_names", False):
                for login in contributors.keys():
                    # skip lookup for anonymous contributors
                    if contributors[login].anonymous:
                        continue

                    d = self._fill_user_data(login, options = self.options)
                    if d:
                        contributors[login].update(d)

            # add all auxiliary contributors
            for login in self.options.get('include', []):
                # skip if we already have this contributor in our list
                if login in contributors:
                    continue

                d = self._fill_user_data(login, options = self.options)
                if d:
                    contributors[login] = d

        return contributors
