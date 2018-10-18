OBJECTS = build/TestCombinations.o build/TestPrimes.o build/TestPythagoreanTripleGenerator.o build/TestTotient.o
SOURCES = ../build/*.o

bin/TestAll.out : ../include/utilities.h $(OBJECTS)
	g++ -std=c++11 -Wall -W -lgmock -lgmock_main -lgtest -lgtest_main -o bin/TestAll.out $(SOURCES) $(OBJECTS)

$(OBJECTS) : build/%.o : %.cpp
	g++ -std=c++11 -Wall -W -c $< -o $@

.PHONY: clean
clean :
	rm bin/TestAll.out
	rm build/*.o

