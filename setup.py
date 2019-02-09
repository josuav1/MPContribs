# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import io, re, glob, os, datetime
from setuptools import setup

SETUP_PTH = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(SETUP_PTH, 'requirements.txt')) as f:
    required = f.read().splitlines()

setup(
    name = 'mpcontribs',
    version = datetime.datetime.today().strftime('%Y.%m.%d'),
    description = "The Materials Project's Community Contribution Framework",
    author = 'Patrick Huck',
    author_email = 'phuck@lbl.gov',
    url = 'https://mpcontribs.org',
    packages = ['mpcontribs'],
    install_requires = required,
    license = 'MIT',
    keywords = ['materials', 'contribution', 'framework', 'data', 'interactive', 'jupyter'],
    scripts = glob.glob(os.path.join(SETUP_PTH, "scripts", "*")),
)
