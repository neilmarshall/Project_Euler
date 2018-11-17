from setuptools import setup, find_packages
from Cython.Build import cythonize

setup(
    name="pyutils",
    version="0.8",
    packages=find_packages(),
    install_requires="Cython",
    ext_modules=cythonize("pyutils/*.pyx"),
    exclude=["tests"]
)

