# sphinxcontrib-ghcontributors


[![PyPI version](https://badge.fury.io/py/sphinxcontrib-ghcontributors.svg)](https://badge.fury.io/py/sphinxcontrib-ghcontributors)

[![Travis Status](https://travis-ci.org/dgarcia360/sphinxcontrib-ghcontributors.svg?branch=master)](https://travis-ci.org/dgarcia360/sphinxcontrib-ghcontributors)


People who contribute to open-source projects could be spending their free time.
It does not matter if it is a code change, an epic, or fixing a small typo.
At the end of the day, this change makes the project better.
That's the reason why you should recognize every contribution!

Are you using **Sphinx** to document the open-source project?
Then **sphinxcontrib-ghcontributors** directive allows you to render all the usernames that have contributed to your repositories directly in your docs.

![example](https://github.com/dgarcia360/sphinxcontrib-ghcontributors/blob/master/docs/_static/example.png)

## Installation

1. Install sphinxcontrib-ghcontributors using pip.

```
pip install sphinxcontrib-ghcontributors
```

2. Add the extension to your Sphinx project ``conf.py`` file.

```
extensions = ['sphinxcontrib.ghcontributors']
```

Usage
=====

The extension defines the directive `ghcontributors`. For each repository that you want to render its contributors, state the Github username and the repository name.

```
..  ghcontributors:: dgarcia360/sphinxcontrib-ghcontributors
```

Sphinx will render the 10 most active contributors. You can increase the number of results to show, and as well exclude some users from the list adding optional filters.

```
    ..  ghcontributors:: dgarcia360/sphinxcontrib-ghcontributors
        :limit: 20
        :order: ASC
        :exclude: dgarcia360,sphinx
```

This directive will render the less active 20 contributors, ordered in ascending order, excluding ``dgarcia360`` and ``sphinx`` usernames from the list.

## Roadmap

See the [open issues](https://github.com/dgarcia360/sphinxcontrib-ghcontributors/issues) for a list of proposed features.

## Contributing

Contributions are welcome and appreciated! Check [CONTRIBUTING.md](CONTRIBUTING.md) file.

##License

Copyright (c) 2018 David Garcia ([@dgarcia360] (https://davidgarcia.dev>)).

Licensed under MIT license (see [LICENSE.md](LICENSE.md) for details)