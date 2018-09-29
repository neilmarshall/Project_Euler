/*
The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:

    2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97

How many circular primes are there below one million?

NOTE: Solution = 55
*/

#include <cmath>

#include <iostream>
#include <string>

/* Return primality of n */
bool is_prime(int n) {
    for (int p = 2; p <= static_cast<int>(sqrt(n)); p++) {
        if (n % p == 0)
            return false;
    }
    return true;
}

/* Return circular primality of n */
bool is_circular_prime(int n) {
    std::string s = std::to_string(n);
    for (unsigned long i = 0; i < s.length(); i++) {
        if (!is_prime(stoi(s)))
            return false;
        s = s.substr(1) + s.substr(0, 1);
    }
    return true;
}

/* Return number of circular primes less than n */
int main() {

    int circular_prime_count = 0;

    for (int n = 2; n <= 1000000; n++) {
        if (is_circular_prime(n)) circular_prime_count += 1;
    }

    std::cout << circular_prime_count << std::endl;
}
