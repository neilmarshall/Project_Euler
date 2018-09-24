/*
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

Solution :: 137846528820
*/

#include <iostream>

long binomialcoeff(const long n, const long k) {
    long result = 1;
    for (long i = 1; i <= k; ++i) {
        result = result * (n + 1 - i) / i;
    }
    return result;
}

int main() {
    const long n = 20;
    std::cout << binomialcoeff(2 * n, n) << std::endl;
}

