/*
Consider the fraction, n / d, where n and d are positive integers. If n < d and
HCF(n,d) = 1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of
size, we get:

    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions
for d ≤ 1,000,000?

Note: The solution to this problem lies in recognising that a proper fraction
n / d is obtained when n, d are coprime. Therefore for each number d, there will
be phi(d) proper fractions that can be generated [phi(d) :: Euler's Totient
function].

Solution: 303963552391
*/

#include "utilities.h"

#include <iostream>
#include <memory>

int main() {

    using ull = unsigned long long;

    const ull LIMIT = 1000000;
    ull proper_fraction_count = 0;
    std::unique_ptr< primes::Phi<ull> > phi(new primes::Phi<ull>(LIMIT));
    for (ull d = 2; d <= LIMIT; d++) { proper_fraction_count += (*phi)(d); }

    std::cout << "Number of reduced proper fractions = " << proper_fraction_count << std::endl;
}
