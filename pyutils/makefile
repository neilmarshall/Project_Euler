.PHONY : test
test :
	python -m unittest discover

.PHONY : clean
clean :
	rm pyutils/*.c pyutils/*.so

.PHONY : setup
setup :
	python3 setup.py build_ext -i

.PHONY : dist
dist :
	python3 setup.py sdist

