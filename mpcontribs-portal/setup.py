# -*- coding: utf-8 -*-
import io, re, glob, os, datetime
from setuptools import setup

SETUP_PTH = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(SETUP_PTH, 'requirements.txt')) as f:
    required = f.read().splitlines()

setup(
    name = 'mpcontribs-portal',
    version = datetime.datetime.today().strftime('%Y.%m.%d'),
    description = 'MPContribs Portal',
    author = 'Patrick Huck',
    author_email = 'phuck@lbl.gov',
    url = 'https://portal.mpcontribs.org',
    packages = ['mpcontribs.portal'],
    install_requires = required,
    license = 'MIT',
    zip_safe=False,
    include_package_data=True
)
