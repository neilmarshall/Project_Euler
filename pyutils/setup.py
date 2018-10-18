from setuptools import setup, find_packages
from Cython.Build import cythonize

setup(
    name="pyutils",
    version="0.4",
    packages=find_packages(),
    install_requires="Cython",
    ext_modules=cythonize("pyutils/c_pythagorean_triples.pyx")
)

