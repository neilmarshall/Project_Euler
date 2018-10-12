/*
Euler's Totient function, φ(n) [sometimes called the phi function], is used to
determine the number of positive numbers less than or equal to n which are
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than
nine and relatively prime to nine, φ(9)=6. 

The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the
ratio n/φ(n) produces a minimum.

Solution: 8319823
*/

#include "utilities.h"

#include <iostream>
#include <limits>
#include <set>

using namespace primes;

bool is_permutation(const int& m, const int& n) {
    std::string s1 = std::to_string(m);
    std::string s2 = std::to_string(n);
    if (s1.size() != s2.size()) { return false; }
    std::multiset<char> set1(s1.begin(), s1.end());
    std::multiset<char> set2(s2.begin(), s2.end());
    return set1 == set2;
}

int main () {

    const int LIMIT = 10000000;

    std::pair<double, int> phiratio_min = std::make_pair(std::numeric_limits<double>::infinity(), 0);
    std::pair<double, int> phiratio;

    std::unique_ptr< Phi<int> > phi(new Phi<int>(LIMIT));
    for (int n = 2; n < LIMIT; n++) {
        int m = (*phi)(n);
        if (is_permutation(m, n)) {
            phiratio = std::make_pair(static_cast<double>(n) / m, n);
            phiratio_min = std::min(phiratio_min, phiratio);
        }
    }

    std::cout << phiratio_min.second << std::endl;
}
