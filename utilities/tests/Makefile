OBJECTS = build/*.o
SOURCES = ../build/*.o

CXX = clang++ -std=c++11 -Wall -W
LIBS = -lgmock -lgmock_main -lgtest -lgtest_main

bin/TestAll.out : $(OBJECTS) $(SOURCES) ../include/utilities.h
	$(CXX) $(LIBS) -o bin/TestAll.out $(SOURCES) $(OBJECTS)

$(OBJECTS) : build/%.o : %.cpp ../include/utilities.h
	$(CXX) -c $< -o $@

.PHONY : test
test:
	bin/TestAll.out

.PHONY: clean
clean :
	rm bin/TestAll.out
	rm build/*.o

