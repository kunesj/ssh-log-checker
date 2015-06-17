#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup

import sshlogchecker
from os.path import *

setup(name='sshlogchecker',
        version = sshlogchecker.__version__,
        description = 'Checking SSH logs, Linux only',
        long_description = open(join(dirname(__file__), 'README.md')).read(),
        author = 'Jiří Kuneš',
        author_email = 'jirka642@gmail.com',
        url = 'https://github.com/kunesj/sshlogchecker',
        packages = ['sshlogchecker'],
        include_package_data = True,
        license = "GPL3",
        entry_points = {
        'console_scripts': ['sshlogchecker = sshlogchecker.background_checker:main']
        },
        install_requires = [
          'setuptools',
          'appdirs',
          'python-dateutil'
          # python-qt4 
        ],
    )
