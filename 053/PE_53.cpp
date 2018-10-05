/*
There are exactly ten ways of selecting three from five, 12345:

    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general, nCr = n! / r!(n − r)!, where r ≤ n, n! = n × (n − 1) × ... × 2 × 1,
and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater
than one-million?

Solution: 4075
*/

#include "../utilities/include/utilities.h"

#include <iostream>

int main() {

    const unsigned long LIMIT = 1000000;

    std::unique_ptr< combinations::nCr_Calculator<unsigned long> > nCr (new combinations::nCr_Calculator<unsigned long>);

    int count = 0;
    for (unsigned long n = 1; n <= 100; ++n) {
        for (unsigned long r = 1; r <= n; ++r) {
            count += ((*nCr)(n, r) > LIMIT ? 1 : 0);
        }
    }

	std::cout << count << std::endl;
}
