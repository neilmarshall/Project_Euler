#include "../include/utilities.h"

#include "gmock/gmock.h"

#include <memory>

using namespace testing;

class TotientGenerator : public Test {
    protected:
        virtual void SetUp() override {
            phi = new primes::Phi<int>(1000);
        }
        virtual void TearDown() override {
            delete phi;
        }
        primes::Phi<int>* phi;
};

TEST_F(TotientGenerator, ReturnsCorrectResults) {
    EXPECT_THAT((*phi)(1), Eq(1));
    EXPECT_THAT((*phi)(2), Eq(1));
    EXPECT_THAT((*phi)(3), Eq(2));
    EXPECT_THAT((*phi)(4), Eq(2));
    EXPECT_THAT((*phi)(5), Eq(4));
    EXPECT_THAT((*phi)(6), Eq(2));
    EXPECT_THAT((*phi)(7), Eq(6));
    EXPECT_THAT((*phi)(10), Eq(4));
    EXPECT_THAT((*phi)(15), Eq(8));
    EXPECT_THAT((*phi)(20), Eq(8));
    EXPECT_THAT((*phi)(50), Eq(20));
    EXPECT_THAT((*phi)(100), Eq(40));
    EXPECT_THAT((*phi)(250), Eq(100));
    EXPECT_THAT((*phi)(252), Eq(72));
}

