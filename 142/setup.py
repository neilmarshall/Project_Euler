from setuptools import setup
from distutils.core import Extension
from Cython.Build import cythonize

ext_modules = [Extension(name="funcs", sources=["funcs.pyx"], libraries=["m"])]
setup(name='funcs', ext_modules=cythonize(ext_modules, annotate=True, force=True))
