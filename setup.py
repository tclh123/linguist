#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='linguist',
      version='0.0.3',
      keywords=('linguist', 'detect', 'programming', 'language'),
      description='Language Savant',
      long_description='Language Savant',
      license='New BSD',

      url='https://github.com/liluo/linguist',
      author='liluo',
      author_email='i@liluo.org',

      packages=find_packages(),
      include_package_data=True,
      platforms='any',
      install_requires=['PyYAML',
                        'pygments>=1.6',
                        'pygments-github-lexers>=0.01',
                        'charlockholmes',
                        'mime>=0.02'],
      classifiers=[],
      scripts=['bin/pylinguist'])
