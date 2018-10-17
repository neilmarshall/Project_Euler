/*
In the following equation x, y, and n are positive integers.

    1 / x + 1 / y = 1 / n

For n = 4 there are exactly three distinct solutions:

    1 / 5 + 1 / 20 = 1 / 4
    1 / 6 + 1 / 12 = 1 / 4
    1 / 8 + 1 / 8 = 1 / 4

What is the least value of n for which the number of distinct solutions
exceeds one-thousand?

Solution: 180180
*/

#include <iostream>

int main() {
    const long LIMIT = 1000;
    long n = 1;
    while (n++) {
        long count = 0;
        for (long x = n + 1; x <= 2 * n; x++) {
            if ((n * x) % (x - n) == 0) { count += 1; }
        }
        if (count > LIMIT) {
            std::cout << n << std::endl;
            break;
        }
    }
}
