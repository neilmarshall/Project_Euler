#include "../include/utilities.h"
#include "gmock/gmock.h"

using namespace testing;
using namespace primes;

TEST(IsPrime, ReturnsFalseForZero) {
    ASSERT_THAT(is_prime(0), Eq(false));
}

TEST(IsPrime, ReturnsFalseForOne) {
    ASSERT_THAT(is_prime(1), Eq(false));
}

TEST(IsPrime, ReturnsTrueForTwo) {
    ASSERT_THAT(is_prime(2), Eq(true));
}

TEST(IsPrime, ReturnsTrueForOddPrime) {
    ASSERT_THAT(is_prime(17), Eq(true));
}

TEST(IsPrime, ReturnsFalseForCompoundNumber) {
    ASSERT_THAT(is_prime(15), Eq(false));
}

