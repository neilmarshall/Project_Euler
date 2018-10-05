/*
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?

Solution: 7652413
*/

#include <cmath>

#include <algorithm>
#include <iostream>
#include <string>

bool is_prime(const long& n) {
    for (long p = 2; p <= static_cast<long>(sqrt(n)); p++) {
        if (n % p == 0)
            return false;
    }
    return true;
}

int main() {
    std::string s = "987654321";
    while (!s.empty()) {
        do {
            if (is_prime(std::stol(s))) {
                std::cout << s << std::endl;
                return 0;
            }
        } while (std::prev_permutation(s.begin(), s.end()));
        s = s.substr(1);
    }
}
