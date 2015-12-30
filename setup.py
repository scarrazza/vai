from __future__ import print_function
from setuptools import setup, Extension, find_packages

setup (name = 'vai',
       version = '0.0.1',
       description = "VAI tool",
       author = 'Stefano Carrazza',
       author_email = 'stefano.carrazza@cern.ch',
       url = 'https://github.com/scarrazza/vai',
       long_description = "See `vai --help` for the full list of options",
       scripts = ['scripts/vai'],
       zip_safe = False,
       classifiers=[
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            ],
       )
