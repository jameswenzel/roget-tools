#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from setuptools import setup
from Roget import version

setup(
    name="Roget",
    py_modules=['Roget'],
    include_package_data=True,
    version=version,
    description="Python implementation of Roget's thesaurus",
    author="James Wenzel & Phillip R. Polefrone",
    author_email="wenzel.james.r@gmail.com",
    url="https://github.com/jameswenzel/Lyric-Wiki-Scraper",
    download_url=('https://github.com/jameswenzel/pylyrics3/tarball/'
                  '{0}'.format(version)),
    license="Apache License, Version 2.0",
    keywords=['roget', 'thesaurus', "roget's", 'dictionary', 'similie',
              'similies', 'semantic', 'space'],
    classifiers=[],
)
