# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

setup(
    packages=find_packages(exclude=('tests')),
    test_suite='tests',
)