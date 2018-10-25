#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std::rel_ops;  // this will provide !=, <=, > and >= if we provide == and < ourselves

enum HandType{HIGHCARD = 1, ONEPAIR, TWOPAIR, THREEEOFAKIND, STRAIGHT, FLUSH,
              FULLHOUSE, FOUROFAKIND, STRAIGHTFLUSH, ROYALFLUSH};

enum Rank{NA = 1, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK,
          QUEEN, KING, ACE};
	
class PokerHand {
    private:
        std::string input_string;
        std::vector<Rank> ranks;
        std::map<Rank, int> rank_counts;
        std::vector<char> suits;
        HandType hand_type;
        std::vector<Rank> rank_scores;
        void parse_ranks();
        void parse_suits();
        HandType score_hand() const;
        std::vector<Rank> score_ranks(const HandType&) const;
        bool is_flush() const;
        bool is_straight() const;
        bool is_four_of_a_kind() const;
        bool is_full_house() const;
        bool is_three_of_a_kind() const;
        bool is_two_pair() const;
        bool is_pair() const;

    public:
        PokerHand(std::string);
        friend std::ostream& operator << (std::ostream&, const PokerHand&);
        friend bool operator == (const PokerHand& p1, const PokerHand& p2);
        friend bool operator < (const PokerHand& p1, const PokerHand& p2);
};

