/*
Euler discovered the remarkable quadratic formula. n^2 + n + 41. It turns out that the formula will produce 40
primes for the consecutive integer values 0 ≤ n ≤ 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is
divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 − 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 ≤ n ≤ 79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| ≤ 1000

where |n| is the modulus/absolute value of n (e.g. |11| = 11 and |−4| = 4), find the product of the coefficients, a and b,
for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

NOTE: Solution is given by a = -61 and b = 971, for a * b = -59,231 .
*/

#include "prime_checker.h"

#include <iostream>

int count_prime_runs(const int& a, const int& b, Prime_Checker& prime_checker) {
    int n = 0;
    while (prime_checker(n * n + a * n + b))
        n++;
    return n;
}

int main() {
    int max_prime_run = 0, max_a = 0, max_b = 0;
    
    Prime_Checker prime_checker;
    
    for (int a = -999; a < 1000; a++) {
        for (int b = -1000; b <= 1000; b++) {
            if (b == 0) continue;  // will never have primes of the form n^2 + a.n + 0
            int prime_run = count_prime_runs(a, b, prime_checker);
            if (prime_run > max_prime_run) {
                max_prime_run = prime_run;
                max_a = a;
                max_b = b;
            }
        }
    }
    
    std::cout << max_a << " * " << max_b << " = " << max_a * max_b << std::endl;
}
