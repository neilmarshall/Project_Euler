from setuptools import setup
from Cython.Build import cythonize

setup(name="PE_74", ext_modules=cythonize("chain_length.pyx"))

