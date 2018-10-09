#include "utilities.h"

#include <iostream>

using namespace primes;

int main () {
    int n = 0, prime_count = 0;
    do {
        n++;
        if (is_prime(n)) { prime_count += 1; }
    } while (prime_count < 10001);
    std::cout << "10,001st prime: " << n << std::endl;
}

