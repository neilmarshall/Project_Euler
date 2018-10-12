/*
Starting with 1 and spiralling anticlockwise in the following way, a square
spiral with side length 7 is formed.

    37 36 35 34 33 32 31
    38 17 16 15 14 13 30
    39 18  5  4  3 12 29
    40 19  6  1  2 11 28
    41 20  7  8  9 10 27
    42 21 22 23 24 25 26
    43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the
side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?

Solution: 26241
*/

#include "utilities.h"

#include <iostream>

using namespace primes;

int main () {
    int prime_count = 0;
    int total_count = 1;
    int k = 0;
    while (k += 1) {
        // layer k has side length 2k+1, and diagonals at (2k-1)^2 + {0 / 2k / 4k / 6k}
        // obviously the first such diagonal will not be prime!
        for (int n = 1; n <= 3; n++) {
            if (is_prime((2 * k - 1) * (2 * k - 1) + 2 * n * k)) {
                prime_count += 1;
            }
        }
        total_count += 4;
        if (static_cast<double>(prime_count) / total_count < 0.1) { break; }
    }

    std::cout << 2 * k + 1 << std::endl;
}

