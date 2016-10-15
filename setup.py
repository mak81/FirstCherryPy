# -*- coding: utf-8 -*-
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, '.')
from FirstCherryPy import __version__


setup(
    name="FirstCherryPy",
    version=__version__,
    description="CherryPy based microservice.",
    maintainer="",
    packages=["FirstCherryPy"],
    platforms=["any"]
)
