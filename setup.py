from __future__ import with_statement
import os

from setuptools import setup, find_packages

from mezzanine_firestore import __version__ as version

VERSION = '1.0'
DESCRIPTION = 'Plugin for mezzanine'
with open("README.md", "r", encoding="utf8") as f:
    LONG_DESCRIPTION = f.read()

#setting up
setup(
    name = 'mezzanine_firestore',
    version = VERSION,
    author = "Eduardo Ceja",
    description = DESCRIPTION,
    # long_description = LONG_DESCRIPTION,
    long_description_content_type = "text/markdown",
    packages = find_packages(),
    install_requires = ["django", "future", "django-countries", "mezzanine"],

    license = "MIT",
    keywords = ['python', 'mezzanine'],
    clasifiers = [
        "License :: MIT License",
        "Operating System :: OS Independent",
        "Programming Languaje :: Python :: 3.6",
        ],
    zip_safe = False,
    python_requires = ">=3.6"
)