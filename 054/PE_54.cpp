/*
The file, poker.txt, contains one-thousand random hands dealt to two players.

Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You can
assume that all hands are valid (no invalid characters or repeated cards), each
player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?

Solution: 376
*/

#include "PokerHand.h"

#include <fstream>
#include <iostream>
#include <string>

int main() {
	
	std::string player1_handstring, player2_handstring, temp;
	int player1_total_score = 0;

	//Read poker hands into variables
	std::ifstream poker_hands("p054_poker.txt");
    while (getline(poker_hands, temp)) {
		player1_handstring="";
		player2_handstring="";
		for (int j = 0; j < 5; ++j) {
			player1_handstring += temp[3 * j];
			player1_handstring += temp[3 * j + 1];
			player2_handstring += temp[15 + 3 * j];
			player2_handstring += temp[15 + 3 * j + 1];
		}
		//Score poker hands
		PokerHand player1_hand(player1_handstring);
		PokerHand player2_hand(player2_handstring);
		if (player1_hand > player2_hand)
			++player1_total_score;
	}

	std::cout << "Player 1: Total numbers of hands won = " << player1_total_score << std::endl;
}
	
