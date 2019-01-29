/*
A number consisting entirely of ones is called a repunit. We shall define R(k)
to be a repunit of length k; for example, R(6) = 111111.

Let us consider repunits of the form R(10^n).

Although R(10), R(100), or R(1000) are not divisible by 17, R(10000) is
divisible by 17. Yet there is no value of n for which R(10n) will divide by 19.
In fact, it is remarkable that 11, 17, 41, and 73 are the only four primes below
one-hundred that can be a factor of R(10^n).

Find the sum of all the primes below one-hundred thousand that will never be a
factor of R(10^n).

Solution: 453647705
*/

#include "utilities.h"

#include <iostream>
#include <numeric>
#include <vector>

class RareCompositeGenerator {

    private:
        long n;

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

        bool two_five_factor_test(long n) {
            while (n % 2 == 0) { n /= 2; }
            while (n % 5 == 0) { n /= 5; }
            return n == 1;
        }

    public:
        RareCompositeGenerator() { n = 1; }

        long operator() () {
            while (true) {
                n += 2;
                if (n != 2 && n != 5 && primes::is_prime(n)) {
                    if (!two_five_factor_test(A(n)))
                        return n;
                }
            }
        }
};

int main() {
    std::vector<long> primes;
    RareCompositeGenerator generator;
    while (true) {
        long prime = generator();
        if (prime >= 100000) { break; }
        primes.push_back(prime);
    }

    // add 2 and 5 as algorithm can't test for these
    std::cout << 2 + 5 + accumulate(primes.begin(), primes.end(), 0L) << std::endl;
}
