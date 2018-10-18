OBJECTS = build/combinations.o build/primes.o build/pythagorean_triples.o build/totient.o

CXX = clang++ -std=c++11 -Wall -W

lib/libutilities($(OBJECTS)) : include/utilities.h $(OBJECTS)
	ar cr lib/libutilities.a $(OBJECTS)

$(OBJECTS) : build/%.o : src/%.cpp include/utilities.h
	$(CXX) -I/include -c $< -o $@

.PHONY : clean
clean :
	rm build/*.o
	rm lib/*.a

.PHONY : install
install:
	sudo cp lib/libutilities.a /usr/local/lib/
	sudo cp include/utilities.h /usr/local/include/

