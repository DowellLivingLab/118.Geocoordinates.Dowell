
from setuptools import setup, Extension
setup(
    ext_modules=[Extension('algorithm', ['algorithm.cpp'],),],
)


