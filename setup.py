
from setuptools import setup
from debian_parser import VERSION

import io
import os
import sys

# Package meta-data.
NAME = 'debian_parser'
DESCRIPTION = 'A simple pure-python module to parse RFC822-like Debain data formats. Including Pacakges, Control, Release files.'
URL = 'https://github.com/ms7m/debian-packages-parser'
EMAIL = 'ms7mohamed@gmail.com'
AUTHOR = 'Mustafa Mohamed'
REQUIRES_PYTHON = '>=3.6.0'


here = os.path.abspath(os.path.dirname(__file__))
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    # If your package is a single module, use this instead of 'packages':
    py_modules=['debian_parser'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    include_package_data=True,
    license='GNU',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)