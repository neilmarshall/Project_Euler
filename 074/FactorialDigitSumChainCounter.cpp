#include "FactorialDigitSumChainCounter.h"

int FactorialDigitSumChainCounter::digit_factorial_sum(int n) {
    int t = 0;
    while (n >= 10) {
        t += factorial[n % 10];
        n /= 10;
    }
    return t + factorial[n];
}
        
int FactorialDigitSumChainCounter::get_chain_length(int n) {
    int chain = 1;
    std::set<int> seen;
    while (true) {
        n = digit_factorial_sum(n);
        if (seen.find(n) == seen.end()) {
            seen.insert(n);
            chain += 1;
        } else {
            break;
        }
    }
    return chain;
}

int FactorialDigitSumChainCounter::CountChainsOfLength(int chain_length) {
    int count = 0;
    for (int n = 1; n < limit; n++) {
        if (get_chain_length(n) == chain_length) { count += 1; }
    }
    return count;
}
