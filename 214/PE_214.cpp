/*
Let φ be Euler's totient function, i.e. for a natural number n, φ(n) is the
number of k, 1 ≤ k ≤ n, for which gcd(k,n) = 1.

By iterating φ, each positive integer generates a decreasing chain of numbers
ending in 1. E.g. if we start with 5 the sequence 5,4,2,1 is generated. Here
is a listing of all chains with length 4:

     5, 4, 2, 1
     7, 6, 2, 1
     8, 4, 2, 1
     9, 6, 2, 1
    10, 4, 2, 1
    12, 4, 2, 1
    14, 6, 2, 1
    18, 6, 2, 1

Only two of these chains start with a prime, their sum is 12.

What is the sum of all primes less than 40000000 which generate a chain of
length 25?

Solution: 1677366278943
*/

#include "utilities.h"

#include <iostream>

class ChainChecker {
    private:
        primes::Phi<long> totient;
        std::vector<long> primes;

        long calculate_chain(const long& n) {
            return n > 1 ? 1 + calculate_chain(totient(n)) : 1;
        }

    public:
        ChainChecker(long limit) : totient(primes::Phi<long>(limit)) {
            primes = primes::get_primes_up_to_n(limit);
        }

        long sum_of_chains(const long& length) {
            long sum = 0;
            for (auto prime : primes) {
                if (calculate_chain(prime) == length) { sum += prime; }
            }
            return sum;
        }
};

int main() {
    ChainChecker chain_checker(40000000L);
    std::cout << chain_checker.sum_of_chains(25) << std::endl;
}
