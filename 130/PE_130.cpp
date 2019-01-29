/*
A number consisting entirely of ones is called a repunit. We shall define R(k)
to be a repunit of length k; for example, R(6) = 111111.

Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that
there always exists a value, k, for which R(k) is divisible by n, and let A(n) 
be the least such value of k; for example, A(7) = 6 and A(41) = 5.

You are given that for all primes, p > 5, that p − 1 is divisible by A(p). For
example, when p = 41, A(41) = 5, and 40 is divisible by 5.

However, there are rare composite values for which this is also true; the first
five examples being 91, 259, 451, 481, and 703.

Find the sum of the first twenty-five composite values of n for which
GCD(n, 10) = 1 and n − 1 is divisible by A(n).

Solution: 149253
*/

#include "utilities.h"

#include <iostream>
#include <iterator>
#include <numeric>
#include <vector>

class RareCompositeGenerator {

    private:
        int n;

        // calculate A(n)
        static int A(const int& n) {
            int k = 2, r = 10 % n, a = (10 * r) % n;
            while ((r % n) != (n - 1)) {
                ++k;
                r = (r + a) % n;
                a = (10 * a) % n;
            }
            return k;
        }

    public:
        RareCompositeGenerator() { n = 3; }

        int operator() () {
            while (true) {
                n += 2;
                if (n % 5 != 0 && !primes::is_prime(n)) {
                    if ((n - 1) % A(n) == 0)
                        return n;
                }
            }
        }
};

int main() {
    std::vector<int> values;
    std::generate_n(back_inserter(values), 25, RareCompositeGenerator());
    std::cout << accumulate(values.begin(), values.end(), 0) << std::endl;
}
