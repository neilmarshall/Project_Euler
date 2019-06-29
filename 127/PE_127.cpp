// Solution:    18407904

#include "utilities.h"

#include <cmath>

#include <deque>
#include <iostream>
#include <vector>

long long RAD(std::vector<long long>&);

int main() {
    long long limit = 120000;  // 120000;
    std::vector<std::vector<long long>> prime_factors;
    for (long long n = 0; n <= limit; ++n) {
        prime_factors.push_back(primes::get_prime_factors<long long>(n));
    }
    long long c_total = 0;
    std::deque<std::vector<long long> > pairs;
    std::vector<long long> v1;
    v1.push_back(2);
    v1.push_back(1);
    pairs.push_back(v1);
    std::vector<long long> v2;
    v2.push_back(3);
    v2.push_back(1);
    pairs.push_back(v2);
    std::vector<long long> curr_pair;
    std::vector<long long> new_pair;
    long long c = 0;
    std::vector<long long> rF;
    long long r = 0;
    while (pairs.size() > 0) {
        curr_pair = pairs[0];
        pairs.pop_front();
        new_pair.clear();
        new_pair.push_back(2 * curr_pair[0] - curr_pair[1]);
        new_pair.push_back(curr_pair[0]);
        if (new_pair[0] + new_pair[1] < limit) {
            pairs.push_back(new_pair);
        }
        new_pair.clear();
        new_pair.push_back(2 * curr_pair[0] + curr_pair[1]);
        new_pair.push_back(curr_pair[0]);
        if (new_pair[0] + new_pair[1] < limit) {
            pairs.push_back(new_pair);
        }
        new_pair.clear();
        new_pair.push_back(curr_pair[0] + 2 * curr_pair[1]);
        new_pair.push_back(curr_pair[1]);
        if (new_pair[0] + new_pair[1] < limit) {
            pairs.push_back(new_pair);
        }
        c = curr_pair[0] + curr_pair[1];
        rF.clear();
        for (long long i = 0; i < prime_factors[curr_pair[0]].size(); ++i) {
            rF.push_back(prime_factors[curr_pair[0]][i]);
        }
        for (long long i = 0; i < prime_factors[curr_pair[1]].size(); ++i) {
            rF.push_back(prime_factors[curr_pair[1]][i]);
        }
        for (long long i = 0; i < prime_factors[c].size(); ++i) {
            rF.push_back(prime_factors[c][i]);
        }
        r = RAD(rF);
        if (r < c) {
            c_total += c;
        }
    }
    std::cout << c_total << std::endl;
}

long long RAD(std::vector<long long>& prime_factors) {
    long long x = 1;
    long long prev_fac = 0;
    for (long long i = 0; i < prime_factors.size(); ++i) {
        if (prime_factors[i] != prev_fac) {
            x *= prime_factors[i];
        }
        prev_fac = prime_factors[i];
    }
    return x;
}
