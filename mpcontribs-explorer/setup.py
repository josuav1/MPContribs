# -*- coding: utf-8 -*-
import io, re, glob, os, datetime
from setuptools import setup

SETUP_PTH = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(SETUP_PTH, 'requirements.txt')) as f:
    required = f.read().splitlines()

setup(
    name = 'mpcontribs-explorer',
    version = datetime.datetime.today().strftime('%Y.%m.%d'),
    description = 'MP Contribution Cards Explorer',
    author = 'Patrick Huck',
    author_email = 'phuck@lbl.gov',
    url = 'https://portal.mpcontribs.org',
    packages = ['mpcontribs.explorer'],
    install_requires = required,
    license = 'MIT',
    zip_safe=False,
    include_package_data=True
)
