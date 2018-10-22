from paver.easy import task
from paver.shell import sh

@task
def test():
	sh("python -m unittest discover")

@task
def clean():
	sh("rm pyutils/*.c pyutils/*.so")

@task
def setup():
	sh("python3 setup.py build_ext -i")

@task
def dist():
	sh("python3 setup.py sdist")

