LIBS = -lgmock -lgmock_main -lgtest -lgtest_main

.PHONY : all
all : bin/main.out bin/test.out

bin/main.out : PE_89.cpp truncate.h
	clang++ -std=c++11 -Wall PE_89.cpp -o bin/main.out

bin/test.out : test_truncate.cpp truncate.h
	clang++ -std=c++11 -Wall ${LIBS} test_truncate.cpp -o bin/test.out

.PHONY : clean
clean :
	rm bin/*.out
