/*
A composite is a number containing at least two prime factors. For
example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

There are ten composites below thirty containing precisely two, not necessarily
distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n < 108, have precisely two, not necessarily
distinct, prime factors?

Notes:
    If n has exactly 2 primes factors then n = p.q, where p and q are primes
    and p (WLOG) is less than or equal to sqrt(n). q will then be a prime in
    the range [p, ..., n / p].

    So for prime up to sqrt(n), there will be as many numbers with exactly two
    prime factors as there are primes in the range [p, ..., n / p].

    Pseudocode algorithm:
        count = 0
        for primes p in [2, ..., sqrt(limit)]:
            for primes q in [p, ..., limit / 2]:
                count += 1
        return count

Solution: 17427258
*/

#include "utilities.h"

#include <cmath>

#include <iostream>

using namespace primes;

int PE_187(const int limit) {
    int count = 0;
    auto primes = get_primes_up_to_n(limit / 2);
    for (int i = 0; i < primes.size(); i++) {
        if (primes[i] > static_cast<int>(sqrt(limit))) { break; }
        for (int j = i; j < primes.size(); j++) {
            if (primes[i] * primes[j] > limit) { break; }
            count += 1;
        }
    }
    return count;
}

int main() {
    std::cout << PE_187(100000000) << std::endl;  // should give solution 17427258
}
