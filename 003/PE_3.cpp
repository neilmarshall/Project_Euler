#include "utilities.h"

#include <iostream>

using namespace primes;

int main() {

    const long n = 600851475143;  // note: factors are 71, 839, 1471 and 6857

    auto factors = get_prime_factors(n);

    std::cout << "Number to be factorised - " << n << "\n";
    std::cout << "Prime factors:" << "\n";
    for (auto factor : factors) { std::cout << factor << " "; }
    std::cout << std::endl;

}
