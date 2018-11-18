.PHONY : all
all : bin/main.out bin/main.exe

bin/main.out : PE_187.cpp
	clang++ -std=c++11 -Wall -lutilities PE_187.cpp -o bin/main.out

bin/main.exe : PE_187.fs
	fsharpc PE_187.fs -o bin/main.exe

.PHONY : clean
clean :
	rm bin/main.*
