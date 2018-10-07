.PHONY: all
all : bin/TestCombinations.out bin/TestTotient.out

bin/TestCombinations.out : ./TestCombinations.cpp ../include/utilities.h ../src/combinations.cpp
	g++ -std=c++11 -Wall -W -lgmock -lgmock_main -lgtest -lgtest_main ./TestCombinations.cpp ../src/combinations.cpp -o bin/TestCombinations.out

bin/TestTotient.out : ./TestTotient.cpp ../include/utilities.h ../src/totient.cpp
	g++ -std=c++11 -Wall -W -lgmock -lgmock_main -lgtest -lgtest_main ./TestTotient.cpp ../src/totient.cpp -o bin/TestTotient.out

.PHONY: clean
clean :
	rm bin/TestCombinations.out
	rm bin/TestTotient.out

