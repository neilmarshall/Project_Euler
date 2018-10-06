#include "../include/utilities.h"

#include "gmock/gmock.h"

using namespace testing;

class CombinationsGenerator : public Test {
    public:
        combinations::nCr_Calculator<int> nCr;
};

TEST_F(CombinationsGenerator, ReturnsOneForZeroInput) {
    ASSERT_THAT(nCr(0, 0), Eq(1));
}

TEST_F(CombinationsGenerator, GeneratesOnesAtLowerBoundaries) {
    for (int n = 1; n <= 20; n++) {
        EXPECT_THAT(nCr(n, 0), Eq(1));
        EXPECT_THAT(nCr(n, n), Eq(1));
    }
}

TEST_F(CombinationsGenerator, GeneratesFourthRowCorrectly) {
    int FourthRow[] = {1, 4, 6, 4, 1};
    for (int r = 0; r <= 4; r++) {
        EXPECT_THAT(nCr(4, r), Eq(FourthRow[r]));
    }
}

TEST_F(CombinationsGenerator, GeneratesTenthRowCorrectly) {
    int TenthRow[] = {1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1};
    for (int r = 0; r <= 10; r++) {
        EXPECT_THAT(nCr(10, r), Eq(TenthRow[r]));
    }
}

