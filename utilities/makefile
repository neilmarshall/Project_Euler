objects = build/combinations.o build/totient.o

lib/libutilities($(objects)) : $(objects)
	ar cr lib/libutilities.a $(objects)

build/combinations.o : include/utilities.h src/combinations.cpp
	g++ -std=c++11 -Wall -W -I/include -c src/combinations.cpp -o build/combinations.o

build/totient.o : include/utilities.h src/totient.cpp
	g++ -std=c++11 -Wall -W -I/include -c src/totient.cpp -o build/totient.o

.PHONY : clean
clean :
	rm build/*.o
	rm lib/*.a

