#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# CONFIDENTIALITY NOTICE: THIS SOFTWARE CONTAINS CONFIDENTIAL INFORMATION OF
# NETAPP, INC. USE, DISCLOSURE OR REPRODUCTION IS PROHIBITED WITHOUT THE PRIOR
# EXPRESS WRITTEN PERMISSION OF NETAPP, INC.

"""SolidFire Python SDK"""

from setuptools import setup, find_packages
from codecs import open
import os
from distutils import dir_util
from distutils.command.clean import clean as _clean

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


class Clean(_clean):
    def remove_dir(self, dir_to_del):
        if os.path.exists(dir_to_del):
            dir_util.remove_tree(dir_to_del, dry_run=self.dry_run)

    def run(self):
        print('custom clean')
        self.remove_dir('build')
        self.remove_dir('dist')
        self.remove_dir('solidfire_sdk_python.egg-info')


setup(
    name='solidfire-sdk-python',

    version='1.5.0.87',

    description='SolidFire Python SDK',
    long_description=long_description,

    url='https://github.com/solidfire/solidfire-sdk-python',

    author='Adam Haid, Ariel Hoffman, Joel Arthur',
    author_email='adam.haid@netapp.com, ariel.hoffman@netapp.com, joel.arthur@netapp.com',

    license='Apache2',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Operating System :: OS Independent',

        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',

        'Topic :: Utilities',
        'Topic :: System :: Systems Administration',
        'Topic :: Software Development :: Libraries :: Application Frameworks',

        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='solidfire nas iscsi fibre channel storage api sdk',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['setuptools>=19.2',
                      'future>=0.15.2', 'enum34>=1.1.6', 'requests>=2.9.1'],

    # $> pip install -e ".[dev,test, docs, release]"
    extras_require={
        'dev': ['check-manifest'],
        'test': [
            'coverage',
            'pyhamcrest>=1.8.5',
            'pytest>=2.8.7',
            'pytest-flake8>=0.1'
        ],
        'docs': ['Sphinx>=1.3.5', 'sphinx_rtd_theme>=0.1.9', ],
        'release': ['twine>=1.6.5', ],
    },

    cmdclass={
        'clean': Clean,
    },
)
