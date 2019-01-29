/*
A number consisting entirely of ones is called a repunit. We shall define R(k)
to be a repunit of length k.

For example, R(10) = 1111111111 = 11×41×271×9091, and the sum of these prime
factors is 9414.

Find the sum of the first forty prime factors of R(109).

Solution: 843296
*/

#include "utilities.h"

#include <iostream>
#include <iterator>
#include <numeric>
#include <vector>

class RareCompositeGenerator {

    private:
        long n;
        long threshold;

        // calculate A(n)
        static long A(const long& n) {
            long k = 2, r = 10 % n, a = (10 * r) % n;
            while ((r % n) != (n - 1)) {
                ++k;
                r = (r + a) % n;
                a = (10 * a) % n;
            }
            return k;
        }

    public:
        RareCompositeGenerator() { n = 3; threshold = 10e9; }

        long operator() () {
            while (true) {
                n += 2;
                if (n % 5 != 0 && primes::is_prime(n)) {
                    if (threshold % A(n) == 0)
                        return n;
                }
            }
        }
};

int main() {
    std::vector<long> values;
    std::generate_n(back_inserter(values), 40, RareCompositeGenerator());
    std::cout << accumulate(values.begin(), values.end(), 0) << std::endl;
}
