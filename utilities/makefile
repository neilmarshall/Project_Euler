OBJECTS = build/combinations.o build/totient.o build/primes.o build/pythagorean_triples.o

lib/libutilities($(OBJECTS)) : include/utilities.h $(OBJECTS)
	ar cr lib/libutilities.a $(OBJECTS)

$(OBJECTS) : build/%.o : src/%.cpp
	g++ -std=c++11 -Wall -W -I/include -c $< -o $@

.PHONY : clean
clean :
	rm build/*.o
	rm lib/*.a

