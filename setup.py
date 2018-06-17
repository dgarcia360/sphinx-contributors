# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='sphinxcontrib-ghcontributors',
    version='0.0.1',
    url='https://github.com/dgarcia360/sphinxcontrib-ghcontributors',
    # download_url='http://pypi.python.org/pypi/sphinxcontrib-ghcontributors',
    license='MIT',
    author='dgarcia360',
    author_email='dgarcia360@outlook.com',
    description='Sphinx extension for rendering the contributors list from GitHub repositories.',
    long_description="",
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    include_package_data=True,
    install_requires=['Sphinx>=1.1', 'requests'],
    packages=find_packages(),
    namespace_packages=['sphinxcontrib']
)