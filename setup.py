from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='project-411',

    version='1.2.0',

    description='Simple chatbot',
    long_description=long_description,

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],

    packages=find_packages(exclude=['docs', 'tests']),
)
