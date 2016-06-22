#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='nyroglancer',
    version='0.0.2',
    description='jupyter extension for neuroglancer',
    author='Jan Funke',
    author_email='jfunke@iri.upc.edu',
    url='https://github.com/funkey/nyroglancer',
    license = 'Apache License 2.0',
    packages = find_packages(),
    install_requires = [
        "Pillow>=3.2.0",
        "jupyter",
        "numpy",
        "neuroglancer>=0.0.5",
    ],
    use_2to3 = True,
)
