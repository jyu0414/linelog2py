# Author: Yuji Sasaki <yuji@sasaki.dev>
# Copyright (c) 2022 Yuji Sasaki
# License: MIT License

from setuptools import setup
import os
import linelog2py

DESCRIPTION = "linelog2py: import LINE Talk History"
NAME = 'linelog2py'
AUTHOR = 'Yuji Sasaki'
AUTHOR_EMAIL = 'yuji@sasaki.dev'
URL = 'https://github.com/jyu0414/linelog2py'
LICENSE = 'MIT License'
DOWNLOAD_URL = 'https://github.com/jyu0414/linelog2py'
VERSION = linelog2py.__version__
PYTHON_REQUIRES = ">=3.6"

INSTALL_REQUIRES = [
]

EXTRAS_REQUIRE = {
}

PACKAGES = [
    'linelog2py'
]

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'Topic :: Text Editors :: Text Processing',
    'Topic :: Text Editors :: Word Processors'
]

with open(f'{os.environ["GITHUB_WORKSPACE"]}/README.md', 'r') as fp:
    readme = fp.read()
with open(f'{os.environ["GITHUB_WORKSPACE"]}/CONTACT.txt', 'r') as fp:
    contacts = fp.read()
long_description = readme + '\n\n' + contacts

setup(name=NAME,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      long_description=long_description,
      long_description_content_type='text/markdown',
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      python_requires=PYTHON_REQUIRES,
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE,
      packages=PACKAGES,
      classifiers=CLASSIFIERS
    )