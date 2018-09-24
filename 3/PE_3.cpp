//
//  main.cpp
//  C_PE_3 (largest prime factor)
//
//  Created by Neil Marshall on 18/11/2015.
//  Copyright © 2015 Neil Marshall. All rights reserved.
//

#include <iostream>
#include <vector>

/**
    Returns a vector of prime factors for a given integer.
*/
std::vector<long> factorize(long n) {

    std::vector<long> factors;
    long i = 2;
    while (n > 1) {
        while (n % i == 0) {
            factors.push_back(i);
            n /= i;
        }
        ++i;
    }

    return factors;

}

int main() {

    const long n = 600851475143;  // note: factors are 71, 839, 1471 and 6857

    std::vector<long> factors = factorize(n);

    std::cout << "Number to be factorised - " << n << "\n";
    std::cout << "Prime factors:" << "\n";
    for (auto factor : factors) std::cout << factor << " ";
    std::cout << std::endl;

}
