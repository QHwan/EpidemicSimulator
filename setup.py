from __future__ import print_function, absolute_import

from setuptools import setup, find_packages

####################################
VERSION = "0.0.1"
__version__ = VERSION
####################################

setup(
    name='EpidemicSimulator',
    version=__version__,
    author='QHwan Kim',
    author_email='poter102@snu.ac.kr',
    packages=find_packages(),
    )
