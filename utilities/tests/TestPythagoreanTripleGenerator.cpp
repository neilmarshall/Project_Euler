#include "../include/utilities.h"

#include "gmock/gmock.h"

#include <tuple>

using namespace testing;
using namespace PythagoreanTriples;

const auto& ituple = std::make_tuple<int, int, int>;

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
    auto expected_value = ituple(3, 4, 5);
    ASSERT_THAT(ptg->GetNextTriple(), Eq(expected_value));
}

TEST_F(GeneratePythagoreanTriples, Returns51213OnSecondCall) {
    auto expected_value = ituple(5, 12, 13);
    ptg->GetNextTriple();
    ASSERT_THAT(ptg->GetNextTriple(), Eq(expected_value));
}

TEST_F(GeneratePythagoreanTriples, Returns2021293OnThirdCall) {
    auto expected_value = ituple(20, 21, 29);
    ptg->GetNextTriple();
    ptg->GetNextTriple();
    ASSERT_THAT(ptg->GetNextTriple(), Eq(expected_value));
}

TEST_F(GeneratePythagoreanTriples, Returns81517OnFourthCall) {
    auto expected_value = ituple(8, 15, 17);
    ptg->GetNextTriple();
    ptg->GetNextTriple();
    ptg->GetNextTriple();
    ASSERT_THAT(ptg->GetNextTriple(), Eq(expected_value));
}

TEST_F(GeneratePythagoreanTriples, Calls567ReturnMatrixMultiplicationsOfCall2) {
    std::vector< std::tuple<int, int, int> > expected_values {
        ituple(7, 24, 25), ituple(48, 55, 73), ituple(28, 45, 53) };
    std::vector< std::tuple<int, int, int> > actual_values(7);
    std::generate(actual_values.begin(), actual_values.end(),
        [&](){ return ptg->GetNextTriple(); });
    actual_values.erase(actual_values.begin(), actual_values.begin() + 4);
    ASSERT_THAT(actual_values, Eq(expected_values));
}

