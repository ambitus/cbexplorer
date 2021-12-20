#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Build information for `cbexplorer` project
"""

from os import getenv, path
from distutils.core import Extension, setup

# from setuptools import find_packages

import cbexplorer as project

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    extras_require={
        "dev": [
            "appdirs==1.4.4",
            "astroid==2.6.6; python_version ~= '3.6'",
            "attrs==21.2.0",
            "autopep8==1.6.0",
            "black==19.10b0",
            "bleach==4.1.0; python_version >= '3.6'",
            "cached-property==1.5.2",
            "cerberus==1.3.4",
            "certifi==2021.10.8",
            "chardet==4.0.0",
            "charset-normalizer==2.0.7; python_version >= '3'",
            "click==8.0.3",
            "colorama==0.4.4; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "distlib==0.3.3",
            "docutils==0.18; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "flake8==4.0.1",
            "idna==3.3; python_version >= '3'",
            "importlib-metadata==4.8.2; python_version >= '3.6'",
            "iniconfig==1.1.1",
            "isort==5.10.1; python_version < '4' and python_full_version >= '3.6.1'",
            "keyring==23.2.1; python_version >= '3.6'",
            "lazy-object-proxy==1.6.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4, 3.5'",
            "mccabe==0.6.1",
            "orderedmultidict==1.0.1",
            "packaging==21.2",
            "pathspec==0.9.0",
            "pep517==0.12.0",
            "pip-shims==0.6.0; python_version >= '3.6'",
            "pipenv-setup==3.1.3",
            "pipfile==0.0.2",
            "pkginfo==1.7.1",
            "platformdirs==2.4.0; python_version >= '3.6'",
            "plette[validation]==0.2.3; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "pluggy==1.0.0",
            "py==1.11.0",
            "pycodestyle==2.8.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "pyflakes==2.4.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "pygments==2.10.0; python_version >= '3.5'",
            "pylint==3.0.0a4",
            "pyparsing==2.4.7",
            "pytest==6.2.5",
            "python-dateutil==2.8.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "readme-renderer==30.0",
            "regex==2021.11.10",
            "requests==2.26.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4, 3.5'",
            "requests-toolbelt==0.9.1",
            "requirementslib==1.6.1; python_version >= '3.6'",
            "rfc3986==1.5.0",
            "six==1.16.0",
            "toml==0.10.2; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "tomli==1.2.2; python_version >= '3.6'",
            "tomlkit==0.7.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "tqdm==4.62.3; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "twine==3.6.0",
            "typed-ast==1.5.0; python_version >= '3.6'",
            "urllib3==1.26.7; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4' and python_version < '4'",
            "vistir==0.5.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "webencodings==0.5.1",
            "wheel==0.37.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "wrapt==1.12.1",
            "zipp==3.6.0; python_version >= '3.6'",
        ]
    },
    install_requires=[
        "attrs==21.2.0",
        "certifi==2021.10.8",
        "click==8.0.3",
        "iniconfig==1.1.1",
        "jinja2==3.0.3",
        "markupsafe==2.0.1; python_version >= '3.6'",
        "more-itertools==8.11.0",
        "packaging==21.2",
        "pluggy==1.0.0",
        "py==1.11.0",
        "pyparsing==2.4.7",
        "pytest==6.2.5",
        "pyyaml==6.0",
        "six==1.16.0",
        "toml==0.10.2; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "wcwidth==0.2.5",
    ],
    name=project.__title__,
    version=project.__version__,
    description=project.__description__,
    long_description=long_description,
    url="",
    ext_modules=[],
    author=project.__author__,
    author_email=project.__author_email__,
    keywords="IBM",
    package_data={},
    data_files=[],
)
