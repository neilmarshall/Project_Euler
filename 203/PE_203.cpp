/*
The binomial coefficients nCk can be arranged in triangular form, Pascal's
triangle. It can be seen that the first eight rows of Pascal's triangle
contain twelve distinct numbers: 1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21 and 35.

A positive integer n is called squarefree if no square of a prime divides n. Of
the twelve distinct numbers in the first eight rows of Pascal's triangle, all
except 4 and 20 are squarefree. The sum of the distinct squarefree numbers in
the first eight rows is 105.

Find the sum of the distinct squarefree numbers in the first 51 rows of
Pascal's triangle.


Solution = 34029210557338
*/

#include "utilities.h"
 
#include <cmath>
 
#include <algorithm>
#include <iostream>
#include <numeric>
#include <set>
#include <vector>
 
using namespace combinations;
using namespace primes;
 
std::vector<long> get_unique_combinatorics(const long& limit) {
    std::set<long> unique_combinatorics;
    nCr_Calculator<long> nCr = nCr_Calculator<long>();
    for (long n = 0; n < limit; n++) {
        for (long r = 0; r <= n; r++) {
            unique_combinatorics.insert(nCr(n, r));
        }
    }
    return std::vector<long> (unique_combinatorics.begin(),
            unique_combinatorics.end());
}
 
bool is_squarefree(const long& n, const std::vector<long>& primes) {
    for (auto prime : primes) {
        if (prime * prime > n) { break; }
        if (n % (prime * prime) == 0) { return false; }
    }
    return true;
}
 
int main() {
    auto unique_combinatorics = get_unique_combinatorics(51);
    auto max_prime = static_cast<long>(sqrt(*std::max_element(unique_combinatorics.begin(),
            unique_combinatorics.end()))) + 1;
    auto primes = get_primes_up_to_n(max_prime);

    auto end = std::remove_if(unique_combinatorics.begin(),
                              unique_combinatorics.end(),
                              [&](const long& n){ return !is_squarefree(n, primes); });

    std::cout << std::accumulate(unique_combinatorics.begin(), end, 0L) << std::endl;
}
