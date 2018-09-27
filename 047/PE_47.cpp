/*
The first two consecutive numbers to have two distinct prime factors are:
    14 = 2 × 7
    15 = 3 × 5
The first three consecutive numbers to have three distinct prime factors are:
    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.
Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
NOTE: Solution = 134043
*/

#include "prime_factor_counter.h"

#include <iostream>

int solve(const int& limit) {

    int n = 1;
    while (n++) {
        if (count_unique_prime_factors(n) == limit) {
            for (int i = 1; i <= limit; i++) {
                if (i == limit) return n;
                if (count_unique_prime_factors(n + i) != limit) break;
            }
        }
    }
}

int main() {
    std::cout << solve(4) << '\n';
}
