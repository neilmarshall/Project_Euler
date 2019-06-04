#include "utilities.h"

#include <algorithm>
#include <iostream>

using namespace primes;

int main() {
    auto phi = Phi<long>(1000000000);
    auto resilience = [&](long n){ return phi(n) / static_cast<double>(n - 1); };
    std::cout << "calculated totients..." << '\n';
    long n = 1;
    while (resilience(n++) >= 15499 / 94744.0) { if ( n % 100000 == 0) std::cout << n << '\n'; }
    std::cout << n << std::endl;
}
