bin/TestAll.out : ../include/utilities.h ../src/*.cpp *.cpp
	g++ -std=c++11 -Wall -W -lgmock -lgmock_main -lgtest -lgtest_main ../src/*.cpp *.cpp -o bin/TestAll.out

.PHONY: clean
clean :
	rm bin/TestAll.out

