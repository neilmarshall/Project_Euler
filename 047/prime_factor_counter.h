#ifndef PRIME_FACTOR_COUNTER_H
#define PRIME_FACTOR_COUNTER_H

#include <cmath>
#include <vector>

int count_unique_prime_factors(int n) {
    
    // indicator flags for primes up to sqrt(n)
    std::vector<bool> prime_flags = {false, false};
    for (int i = 2; i <= static_cast<int>(sqrt(n)); ++i) prime_flags.push_back(true);
    for (int p = 2; p <= static_cast<int>(sqrt(n)) / 2; p++) {
        for (int q = 2; q <= static_cast<int>(sqrt(n)) / p; q++) {
            prime_flags[p * q] = false;
        }
    }
    
    // vector of primes up to sqrt(n)
    std::vector<int> primes;
    for (int i = 2; i <= static_cast<int>(sqrt(n)); ++i) {
        if (prime_flags[i]) primes.push_back(i);
    }
    
    int unique_prime_factor_count = 0;
    for (auto prime : primes) {
        if (n % prime == 0) unique_prime_factor_count += 1;
        while (n % prime == 0) n /= prime;
    }
    if (n != 1) unique_prime_factor_count += 1;
    
    return unique_prime_factor_count;
}

#endif  /* PRIME_FACTOR_COUNTER_H */
