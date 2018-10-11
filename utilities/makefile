objects = build/combinations.o build/totient.o build/primes.o build/pythagorean_triples.o

lib/libutilities($(objects)) : $(objects)
	ar cr lib/libutilities.a $(objects)

build/combinations.o : include/utilities.h src/combinations.cpp
	g++ -std=c++11 -Wall -W -I/include -c src/combinations.cpp -o build/combinations.o

build/totient.o : include/utilities.h src/totient.cpp
	g++ -std=c++11 -Wall -W -I/include -c src/totient.cpp -o build/totient.o

build/primes.o : include/utilities.h src/primes.cpp
	g++ -std=c++11 -Wall -W -I/include -c src/primes.cpp -o build/primes.o

build/pythagorean_triples.o : include/utilities.h src/pythagorean_triples.cpp
	g++ -std=c++11 -Wall -W -I/include -c src/pythagorean_triples.cpp -o build/pythagorean_triples.o

.PHONY : clean
clean :
	rm build/*.o
	rm lib/*.a

