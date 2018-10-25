#include "PokerHand.h"

#include "gmock/gmock.h"

#include <sstream>

using namespace testing;

/*
 *  Test hands print to output stream correctly
 */

class APokerHand : public Test {
    public:
        PokerHand royal_flush = PokerHand("TDJDQDKDAD");
        PokerHand straight_flush = PokerHand("9DTDJDQDKD");
        PokerHand four_of_a_kind = PokerHand("6D6S6H6C2S");
        PokerHand full_house = PokerHand("6D6S6H2C2S");
        PokerHand flush = PokerHand("6DTDJDQDKD");
        PokerHand straight = PokerHand("9DTDJDQDKS");
        PokerHand three_of_a_kind = PokerHand("6D6S6H8C2S");
        PokerHand two_pair = PokerHand("6D6S8H8C2S");
        PokerHand pair = PokerHand("5D6S8H8C2S");
        PokerHand high_card = PokerHand("5D6S8H7C2S");
};

TEST_F(APokerHand, PrintsRoyalFlush) {
    std::stringstream ss;
    ss << royal_flush;
    ASSERT_THAT(ss.str(), Eq("Royal Flush (Ace, King, Queen, Jack, Ten)"));
}

TEST_F(APokerHand, PrintsStraightFlush) {
    std::stringstream ss;
    ss << straight_flush;
    ASSERT_THAT(ss.str(), Eq("Straight Flush (King, Queen, Jack, Ten, Nine)"));
}

TEST_F(APokerHand, PrintsFourOfAKind) {
    std::stringstream ss;
    ss << four_of_a_kind;
    ASSERT_THAT(ss.str(), Eq("Four of a kind (Six, Two)"));
}

TEST_F(APokerHand, PrintsFullHouse) {
    std::stringstream ss;
    ss << full_house;
    ASSERT_THAT(ss.str(), Eq("Full House (Six, Two)"));
}

TEST_F(APokerHand, PrintsFlush) {
    std::stringstream ss;
    ss << flush;
    ASSERT_THAT(ss.str(), Eq("Flush (King, Queen, Jack, Ten, Six)"));
}

        PokerHand high_card = PokerHand("5D6S8H7C2S");
TEST_F(APokerHand, PrintsStraight) {
    std::stringstream ss;
    ss << straight;
    ASSERT_THAT(ss.str(), Eq("Straight (King, Queen, Jack, Ten, Nine)"));
}

TEST_F(APokerHand, PrintsThreeOfAKind) {
    std::stringstream ss;
    ss << three_of_a_kind;
    ASSERT_THAT(ss.str(), Eq("Three of a kind (Six, Eight, Two)"));
}

TEST_F(APokerHand, PrintsTwoPair) {
    std::stringstream ss;
    ss << two_pair;
    ASSERT_THAT(ss.str(), Eq("Two pair (Eight, Six, Two)"));
}

TEST_F(APokerHand, PrintsPair) {
    std::stringstream ss;
    ss << pair;
    ASSERT_THAT(ss.str(), Eq("Pair (Eight, Six, Five, Two)"));
}

TEST_F(APokerHand, PrintsHighCard) {
    std::stringstream ss;
    ss << high_card;
    ASSERT_THAT(ss.str(), Eq("Highcard (Eight, Seven, Six, Five, Two)"));
}


/*
 *  Test hands versus lower-scoring hands
 */

class RoyalFlush : public Test {
    public:
        PokerHand royal_flush = PokerHand("TDJDQDKDAD");
        PokerHand straight_flush = PokerHand("9DTDJDQDKD");
        PokerHand four_of_a_kind = PokerHand("6D6S6H6C2S");
        PokerHand full_house = PokerHand("6D6S6H2C2S");
        PokerHand flush = PokerHand("6DTDJDQDKD");
        PokerHand straight = PokerHand("9DTDJDQDKS");
        PokerHand three_of_a_kind = PokerHand("6D6S6H8C2S");
        PokerHand two_pair = PokerHand("6D6S8H8C2S");
        PokerHand pair = PokerHand("5D6S8H8C2S");
        PokerHand high_card = PokerHand("5D6S8H7C2S");
};

TEST_F(RoyalFlush, BeatsStraightFlush) {
    ASSERT_THAT(royal_flush, Gt(straight_flush));
}

TEST_F(RoyalFlush, BeatsFourOfAKind) {
    ASSERT_THAT(royal_flush, Gt(four_of_a_kind));
}

TEST_F(RoyalFlush, BeatsFullHouse) {
    ASSERT_THAT(royal_flush, Gt(full_house));
}

TEST_F(RoyalFlush, BeatsFlush) {
    ASSERT_THAT(royal_flush, Gt(flush));
}

TEST_F(RoyalFlush, BeatsStraight) {
    ASSERT_THAT(royal_flush, Gt(straight));
}

TEST_F(RoyalFlush, BeatsThreeOfAKind) {
    ASSERT_THAT(royal_flush, Gt(three_of_a_kind));
}

TEST_F(RoyalFlush, BeatsTwoPair) {
    ASSERT_THAT(royal_flush, Gt(two_pair));
}

TEST_F(RoyalFlush, BeatsPair) {
    ASSERT_THAT(royal_flush, Gt(pair));
}

TEST_F(RoyalFlush, BeatsHighCard) {
    ASSERT_THAT(royal_flush, Gt(high_card));
}

class StraightFlush : public Test {
    public:
        PokerHand straight_flush = PokerHand("9DTDJDQDKD");
        PokerHand four_of_a_kind = PokerHand("6D6S6H6C2S");
        PokerHand full_house = PokerHand("6D6S6H2C2S");
        PokerHand flush = PokerHand("6DTDJDQDKD");
        PokerHand straight = PokerHand("9DTDJDQDKS");
        PokerHand three_of_a_kind = PokerHand("6D6S6H8C2S");
        PokerHand two_pair = PokerHand("6D6S8H8C2S");
        PokerHand pair = PokerHand("5D6S8H8C2S");
        PokerHand high_card = PokerHand("5D6S8H7C2S");
};

TEST_F(StraightFlush, BeatsFourOfAKind) {
    ASSERT_THAT(straight_flush, Gt(four_of_a_kind));
}

TEST_F(StraightFlush, BeatsFullHouse) {
    ASSERT_THAT(straight_flush, Gt(full_house));
}

TEST_F(StraightFlush, BeatsFlush) {
    ASSERT_THAT(straight_flush, Gt(flush));
}

TEST_F(StraightFlush, BeatsStraight) {
    ASSERT_THAT(straight_flush, Gt(straight));
}

TEST_F(StraightFlush, BeatsThreeOfAKind) {
    ASSERT_THAT(straight_flush, Gt(three_of_a_kind));
}

TEST_F(StraightFlush, BeatsTwoPair) {
    ASSERT_THAT(straight_flush, Gt(two_pair));
}

TEST_F(StraightFlush, BeatsPair) {
    ASSERT_THAT(straight_flush, Gt(pair));
}

TEST_F(StraightFlush, BeatsHighCard) {
    ASSERT_THAT(straight_flush, Gt(high_card));
}

class FourOfAKind : public Test {
    public:
        PokerHand four_of_a_kind = PokerHand("6D6S6H6C2S");
        PokerHand full_house = PokerHand("6D6S6H2C2S");
        PokerHand flush = PokerHand("6DTDJDQDKD");
        PokerHand straight = PokerHand("9DTDJDQDKS");
        PokerHand three_of_a_kind = PokerHand("6D6S6H8C2S");
        PokerHand two_pair = PokerHand("6D6S8H8C2S");
        PokerHand pair = PokerHand("5D6S8H8C2S");
        PokerHand high_card = PokerHand("5D6S8H7C2S");
};

TEST_F(FourOfAKind, BeatsFullHouse) {
    ASSERT_THAT(four_of_a_kind, Gt(full_house));
}

TEST_F(FourOfAKind, BeatsFlush) {
    ASSERT_THAT(four_of_a_kind, Gt(flush));
}

TEST_F(FourOfAKind, BeatsStraight) {
    ASSERT_THAT(four_of_a_kind, Gt(straight));
}

TEST_F(FourOfAKind, BeatsThreeOfAKind) {
    ASSERT_THAT(four_of_a_kind, Gt(three_of_a_kind));
}

TEST_F(FourOfAKind, BeatsTwoPair) {
    ASSERT_THAT(four_of_a_kind, Gt(two_pair));
}

TEST_F(FourOfAKind, BeatsPair) {
    ASSERT_THAT(four_of_a_kind, Gt(pair));
}

TEST_F(FourOfAKind, BeatsHighCard) {
    ASSERT_THAT(four_of_a_kind, Gt(high_card));
}

class FullHouse : public Test {
    public:
        PokerHand full_house = PokerHand("6D6S6H2C2S");
        PokerHand flush = PokerHand("6DTDJDQDKD");
        PokerHand straight = PokerHand("9DTDJDQDKS");
        PokerHand three_of_a_kind = PokerHand("6D6S6H8C2S");
        PokerHand two_pair = PokerHand("6D6S8H8C2S");
        PokerHand pair = PokerHand("5D6S8H8C2S");
        PokerHand high_card = PokerHand("5D6S8H7C2S");
};

TEST_F(FullHouse, BeatsFlush) {
    ASSERT_THAT(full_house, Gt(flush));
}

TEST_F(FullHouse, BeatsStraight) {
    ASSERT_THAT(full_house, Gt(straight));
}

TEST_F(FullHouse, BeatsThreeOfAKind) {
    ASSERT_THAT(full_house, Gt(three_of_a_kind));
}

TEST_F(FullHouse, BeatsTwoPair) {
    ASSERT_THAT(full_house, Gt(two_pair));
}

TEST_F(FullHouse, BeatsPair) {
    ASSERT_THAT(full_house, Gt(pair));
}

TEST_F(FullHouse, BeatsHighCard) {
    ASSERT_THAT(full_house, Gt(high_card));
}

class Flush : public Test {
    public:
        PokerHand flush = PokerHand("6DTDJDQDKD");
        PokerHand straight = PokerHand("9DTDJDQDKS");
        PokerHand three_of_a_kind = PokerHand("6D6S6H8C2S");
        PokerHand two_pair = PokerHand("6D6S8H8C2S");
        PokerHand pair = PokerHand("5D6S8H8C2S");
        PokerHand high_card = PokerHand("5D6S8H7C2S");
};

TEST_F(Flush, BeatsStraight) {
    ASSERT_THAT(flush, Gt(straight));
}

TEST_F(Flush, BeatsThreeOfAKind) {
    ASSERT_THAT(flush, Gt(three_of_a_kind));
}

TEST_F(Flush, BeatsTwoPair) {
    ASSERT_THAT(flush, Gt(two_pair));
}

TEST_F(Flush, BeatsPair) {
    ASSERT_THAT(flush, Gt(pair));
}

TEST_F(Flush, BeatsHighCard) {
    ASSERT_THAT(flush, Gt(high_card));
}

class Straight : public Test {
    public:
        PokerHand straight = PokerHand("9DTDJDQDKS");
        PokerHand three_of_a_kind = PokerHand("6D6S6H8C2S");
        PokerHand two_pair = PokerHand("6D6S8H8C2S");
        PokerHand pair = PokerHand("5D6S8H8C2S");
        PokerHand high_card = PokerHand("5D6S8H7C2S");
};

TEST_F(Straight, BeatsThreeOfAKind) {
    ASSERT_THAT(straight, Gt(three_of_a_kind));
}

TEST_F(Straight, BeatsTwoPair) {
    ASSERT_THAT(straight, Gt(two_pair));
}

TEST_F(Straight, BeatsPair) {
    ASSERT_THAT(straight, Gt(pair));
}

TEST_F(Straight, BeatsHighCard) {
    ASSERT_THAT(straight, Gt(high_card));
}

class ThreeOfAKind : public Test {
    public:
        PokerHand three_of_a_kind = PokerHand("6D6S6H8C2S");
        PokerHand two_pair = PokerHand("6D6S8H8C2S");
        PokerHand pair = PokerHand("5D6S8H8C2S");
        PokerHand high_card = PokerHand("5D6S8H7C2S");
};

TEST_F(ThreeOfAKind, BeatsTwoPair) {
    ASSERT_THAT(three_of_a_kind, Gt(two_pair));
}

TEST_F(ThreeOfAKind, BeatsPair) {
    ASSERT_THAT(three_of_a_kind, Gt(pair));
}

TEST_F(ThreeOfAKind, BeatsHighCard) {
    ASSERT_THAT(three_of_a_kind, Gt(high_card));
}

class TwoPair : public Test {
    public:
        PokerHand two_pair = PokerHand("6D6S8H8C2S");
        PokerHand pair = PokerHand("5D6S8H8C2S");
        PokerHand high_card = PokerHand("5D6S8H7C2S");
};

TEST_F(TwoPair, BeatsPair) {
    ASSERT_THAT(two_pair, Gt(pair));
}

TEST_F(TwoPair, BeatsHighCard) {
    ASSERT_THAT(two_pair, Gt(high_card));
}

class Pair : public Test {
    public:
        PokerHand pair = PokerHand("5D6S8H8C2S");
        PokerHand high_card = PokerHand("5D6S8H7C2S");
};

TEST_F(Pair, BeatsHighCard) {
    ASSERT_THAT(pair, Gt(high_card));
}
