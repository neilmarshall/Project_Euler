.PHONY : all
all : bin/main.out bin/PokerHandTest.out

bin/main.out : PE_54.cpp PokerHand.cpp PokerHand.h
	clang++ -std=c++11 -Wall -W PE_54.cpp PokerHand.cpp -o bin/main.out

bin/PokerHandTest.out : PokerHandTest.cpp PokerHand.cpp PokerHand.h
	clang++ -std=c++11 -Wall -W -lgmock -lgmock_main -lgtest -lgtest_main PokerHandTest.cpp PokerHand.cpp -o bin/PokerHandTest.out

.PHONY : test
test :
	bin/PokerHandTest.out

.PHONY : clean
clean :
	rm bin/main.out
	rm bin/PokerHandTest.out

