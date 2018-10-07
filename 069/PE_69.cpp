/*
Euler's Totient function, phi(n), is used to determine the number of numbers
less than n which are relatively prime to n.

For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively
prime to nine, phi(9)=6.

It can be shown that n=6 produces a maximum n / phi(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n / phi(n) is a maximum.

Solution: 510510
*/

#include "../utilities/include/utilities.h"

#include <cmath>

#include <iostream>
#include <memory>
#include <vector>
#include <set>

int main() {

    const int LIMIT = 1000000;
    
    std::unique_ptr< primes::Phi<int> > phi(new primes::Phi<int>(LIMIT));

    std::pair<double, int> phiratio_max = std::make_pair(0., 0);
    std::pair<double, int> phiratio;
    for (int n = 2; n <= LIMIT; ++n) {
        phiratio = std::make_pair(static_cast<double>(n) / (*phi)(n), n);
        phiratio_max = std::max(phiratio_max, phiratio);
    }

    std::cout << "Maximum ratio = " << phiratio_max.first;
    std::cout << "; n = " << phiratio_max.second << std::endl;
}

