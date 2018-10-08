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

TEST(GetPrimesUnderN, ReturnsEmptyVectorForInputLessThanOne) {
    std::vector<int> test_vec;
    ASSERT_THAT(get_primes_under_n(1), test_vec);
}

TEST(GetPrimesUnderN, ReturnsPrimesStrictlyLessThanInput) {
    std::vector<int> test_vec {2, 3, 5, 7, 11, 13, 17, 19};
    ASSERT_THAT(get_primes_under_n(23), test_vec);
}

TEST(GetPrimesUpToN, ReturnsEmptyVectorForInputLessThanOne) {
    std::vector<int> test_vec;
    ASSERT_THAT(get_primes_up_to_n(1), test_vec);
}

TEST(GetPrimesUpToN, ReturnsPrimesUpToAndIncludingInput) {
    std::vector<int> test_vec {2, 3, 5, 7, 11, 13, 17, 19, 23};
    ASSERT_THAT(get_primes_up_to_n(23), test_vec);
}

TEST(GetPrimeFactors, ReturnsEmptyVectorForInputLessThanOne) {
    std::vector<int> test_vec;
    ASSERT_THAT(get_prime_factors(1), test_vec);
}

TEST(GetPrimeFactors, ReturnsVectorOfOneElementForPrimeInput) {
    std::vector<int> test_vec {13};
    ASSERT_THAT(get_prime_factors(13), test_vec);
}

TEST(GetPrimeFactors, ReturnsVectorOfNonUniqueFactorsForCompoundInput) {
    std::vector<int> test_vec {2, 2, 5, 5};
    ASSERT_THAT(get_prime_factors(100), test_vec);
}

TEST(GetUniquePrimeFactors, ReturnsEmptyVectorForInputLessThanOne) {
    std::vector<int> test_vec;
    ASSERT_THAT(get_unique_prime_factors(1), test_vec);
}

TEST(GetUniquePrimeFactors, ReturnsVectorOfOneElementForPrimeInput) {
    std::vector<int> test_vec {13};
    ASSERT_THAT(get_unique_prime_factors(13), test_vec);
}

TEST(GetUniquePrimeFactors, ReturnsVectorOfUniqueFactorsForCompoundInput) {
    std::vector<int> test_vec {2, 5};
    ASSERT_THAT(get_unique_prime_factors(100), test_vec);
}

