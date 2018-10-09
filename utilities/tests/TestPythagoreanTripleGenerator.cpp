#include "../include/utilities.h"

#include "gmock/gmock.h"

#include <tuple>

using namespace testing;
using namespace PythagoreanTriples;

class GeneratePythagoreanTriples : public Test {
    public:
        virtual void SetUp() override {
            ptg = new PythagoreanTripleGenerator<int>;
        }

        virtual void TearDown() override {
            delete ptg;
        }

        PythagoreanTripleGenerator<int>* ptg;
};

TEST_F(GeneratePythagoreanTriples, Returns345OnFirstCall) {
    auto expected_value = std::make_tuple(3, 4, 5);
    ASSERT_THAT(ptg->GetNextTriple(), Eq(expected));
}

TEST_F(GeneratePythagoreanTriples, Returns51213OnSecondCall) {
    auto expected_value = std::make_tuple(5, 12, 13);
    auto unused = ptg->GetNextTriple();
    ASSERT_THAT(ptg->GetNextTriple(), Eq(expected));
}

TEST_F(GeneratePythagoreanTriples, Returns2021293OnThirdCall) {
    auto expected_value = std::make_tuple(20, 21, 29);
    auto unused = ptg->GetNextTriple();
    unused = ptg->GetNextTriple();
    ASSERT_THAT(ptg->GetNextTriple(), Eq(expected));
}

TEST_F(GeneratePythagoreanTriples, Returns81517OnFourthCall) {
    auto expected_value = std::make_tuple(8, 15, 17);
    auto unused = ptg->GetNextTriple();
    unused = ptg->GetNextTriple();
    unused = ptg->GetNextTriple();
    ASSERT_THAT(ptg->GetNextTriple(), Eq(expected));
}
