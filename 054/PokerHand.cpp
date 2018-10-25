#include "PokerHand.h"

/* class constructor */
PokerHand::PokerHand(std::string input_string_) : input_string(input_string_) {

    // parse ranks and suits
    this->parse_ranks();
    this->parse_suits();
	
    // score hand
    hand_type = this->score_hand();
    rank_scores = this->score_ranks(hand_type);
}

/* load ranks in sorted order (and count ranks so can score hand) */
void PokerHand::parse_ranks() {
    std::map<char, Rank> rank_map = { {'2', TWO}, {'3', THREE}, {'4', FOUR},
        {'5', FIVE}, {'6', SIX}, {'7', SEVEN}, {'8', EIGHT}, {'9', NINE},
        {'T', TEN}, {'J', JACK}, {'Q', QUEEN}, {'K', KING}, {'A', ACE} };

    for (int i = 0; i < 5; ++i) { ranks.push_back(rank_map[input_string[2 * i]]); }
    std::sort(ranks.begin(), ranks.end());

    for (auto rank : ranks) {
        rank_counts.insert(std::make_pair(rank, std::count(ranks.begin(), ranks.end(), rank))); 
    }
}

/* load suits */
void PokerHand::parse_suits() {
    for (int i = 0; i < 5; ++i) { suits.push_back(input_string[2 * i + 1]); }
}

int rank_count_counter(const std::map<Rank, int>& rank_counts, int count) {
    int counter = 0;
    for (auto pair : rank_counts) {
        if (pair.second == count) { counter += 1; }
    }
    return counter;
}

/* score hand type :: flush, straight, etc... */
HandType PokerHand::score_hand() const {
    if (is_flush() && is_straight() && ranks[4] == ACE) {
        return ROYALFLUSH;
    } else if (is_flush() && is_straight()) {
        return STRAIGHTFLUSH;
    } else if (is_four_of_a_kind()) {
        return FOUROFAKIND;
    } else if (is_full_house()) {
        return FULLHOUSE;
    } else if (is_flush()) {
        return FLUSH;
    } else if (is_straight()) {
        return STRAIGHT;
    } else if (is_three_of_a_kind()) {
        return THREEEOFAKIND;
    } else if (is_two_pair()) {
        return TWOPAIR;
    } else if (is_pair()) {
        return ONEPAIR;
    } else {
        return HIGHCARD;
    }
}

/* check if hand is a flush */
bool PokerHand::is_flush() const {
    for (int i = 0; i < 4; ++i)
        if (suits[i] != suits[i + 1]) { return false; }
    return true;
}

/* check if hand is a straight */
bool PokerHand::is_straight() const {
    for (int i = 0; i < 4; ++i)
        if (ranks[i] != ranks[i + 1] - 1) { return false; }
    return true;
}

/* check if hand is four of a kind*/
bool PokerHand::is_four_of_a_kind() const {
    return rank_count_counter(rank_counts, 4) == 1;
}

/* check if hand is a full house */
bool PokerHand::is_full_house() const {
    return is_three_of_a_kind() && is_pair();
}

/* check if hand is three of a kind*/
bool PokerHand::is_three_of_a_kind() const {
    return rank_count_counter(rank_counts, 3) == 1;
}

/* check if hand is a two-pair*/
bool PokerHand::is_two_pair() const {
    return rank_count_counter(rank_counts, 2) == 2;
}

/* check if hand is a pair*/
bool PokerHand::is_pair() const {
    return rank_count_counter(rank_counts, 2) == 1;
}

/* score hand type :: flush, straight, etc... */
std::vector<Rank> PokerHand::score_ranks(const HandType& hand_type) const {
    std::vector<Rank> scorer(5, NA);
    Rank four_rank, three_rank, two_rank, high_card;
    std::vector<Rank> high_cards, pair_ranks;
    switch (hand_type) {
        case ROYALFLUSH: case STRAIGHTFLUSH: case FLUSH: case STRAIGHT: case HIGHCARD:
            scorer[0] = ranks[4];
            scorer[1] = ranks[3];
            scorer[2] = ranks[2];
            scorer[3] = ranks[1];
            scorer[4] = ranks[0];
            break;
        case FOUROFAKIND:
            for (auto rank : rank_counts) {
                if (rank.second == 4) { four_rank = rank.first; }
                if (rank.second == 1) { high_card = rank.first; }
            }
            scorer[0] = four_rank;
            scorer[1] = high_card;
            break;
        case FULLHOUSE:
            for (auto rank : rank_counts) {
                if (rank.second == 3) { three_rank = rank.first; }
                if (rank.second == 2) { two_rank = rank.first; }
            }
            scorer[0] = three_rank;
            scorer[1] = two_rank;
            break;
        case THREEEOFAKIND:
            for (auto rank : rank_counts) {
                if (rank.second == 3) { three_rank = rank.first; }
                if (rank.second == 1) { high_cards.push_back(rank.first); }
            }
            scorer[0] = three_rank;
            scorer[1] = *std::max_element(high_cards.begin(), high_cards.end());
            scorer[2] = *std::min_element(high_cards.begin(), high_cards.end());
            break;
        case TWOPAIR:
            for (auto rank : rank_counts) {
                if (rank.second == 2) { pair_ranks.push_back(rank.first); }
                if (rank.second == 1) { high_card = rank.first; }
            }
            scorer[0] = *std::max_element(pair_ranks.begin(), pair_ranks.end());
            scorer[1] = *std::min_element(pair_ranks.begin(), pair_ranks.end());
            scorer[2] = high_card;
            break;
        case ONEPAIR:
            for (auto rank : rank_counts) {
                if (rank.second == 2) { two_rank = rank.first; }
                if (rank.second == 1) { high_cards.push_back(rank.first); }
            }
            std::sort(high_cards.begin(), high_cards.end());
            scorer[0] = two_rank;
            scorer[1] = high_cards[2];
            scorer[2] = high_cards[1];
            scorer[3] = high_cards[0];
            break;
    }
    return scorer;
}

/* overload outstream operator */
std::ostream& operator << (std::ostream& out, const PokerHand& hand) {
    std::map<HandType, std::string> hand_type_map = { {HIGHCARD, "Highcard"},
        {ONEPAIR, "Pair"}, {TWOPAIR, "Two pair"}, {THREEEOFAKIND, "Three of a kind"},
        {STRAIGHT, "Straight"}, {FLUSH, "Flush"}, {FULLHOUSE, "Full House"},
        {FOUROFAKIND, "Four of a kind"}, {STRAIGHTFLUSH, "Straight Flush"},
        {ROYALFLUSH, "Royal Flush"} };
    std::map<Rank, std::string> rank_map = { {TWO, "Two"}, {THREE, "Three"},
        {FOUR, "Four"}, {FIVE, "Five"}, {SIX, "Six"}, {SEVEN, "Seven"},
        {EIGHT, "Eight"}, {NINE, "Nine"}, {TEN, "Ten"}, {JACK, "Jack"},
        {QUEEN, "Queen"}, {KING, "King"}, {ACE, "Ace"} };
    std::string outstring = hand_type_map[hand.hand_type];
    outstring += " (" + rank_map[hand.rank_scores[0]];
    for (int i = 1; i <= 4; i++) {
        if(hand.rank_scores[i] != NA) {
            outstring += ", " + rank_map[hand.rank_scores[i]];
        }
    }
    outstring += ")";
    out << outstring;
    return out;
}

/* equality comparison operator */
bool operator == (const PokerHand& p1, const PokerHand& p2) {

    if (p1.hand_type == p2.hand_type) {
        return p1.rank_scores == p2.rank_scores;
    }

    return false;
}

/* less than comparison operator */
bool operator < (const PokerHand& p1, const PokerHand& p2) {

    if (p1.hand_type == p2.hand_type) {
        return p1.rank_scores < p2.rank_scores;
    }

    return p1.hand_type < p2.hand_type;
}
