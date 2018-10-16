#ifndef FACTORIAL_DIGIT_SUM_CHAIN_COUNTER_H
#define FACTORIAL_DIGIT_SUM_CHAIN_COUNTER_H

#include <set>

class FactorialDigitSumChainCounter {
    private:
        constexpr static int factorial[] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};
        int limit;
        
        static int digit_factorial_sum(int);
        static int get_chain_length(int);

    public:
        FactorialDigitSumChainCounter(int _limit) : limit(_limit) {}
        int CountChainsOfLength(int);
};

#endif // FACTORIAL_DIGIT_SUM_CHAIN_COUNTER_H
