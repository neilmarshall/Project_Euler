/*
The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains
21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

Solution: 997651
*/

#include <iostream>
#include <numeric>
#include <set>
#include <vector>

std::set<long> get_primes(long);

std::pair<long, long> get_chain(const std::set<long>&, const long&, const long&);

int main() {

    long n = 1000000;

    // calculate primes up to n - store as a set for sequential access and for checking inclusion
    std::set<long> primes = get_primes(n);

     // create pairs of consecutive prime chain lengths and consecutive prime sums,
     // retaining the pair with the maximum chain length
    std::pair<long, long> max_chain = std::make_pair(0, 0);
    for (long seed = 0; seed < primes.size(); ++seed) {
        std::pair<long, long> chain = get_chain(primes, seed, n);
        max_chain = max(max_chain, chain);
    }

    std::cout << "Solution: " << max_chain.second << " (chain length = " << max_chain.first << ")" << std::endl;
}

std::set<long> get_primes(long limit) {

    std::vector<bool> prime_indicator_flags = {false, false};
    for (long i = 2; i <= limit; ++i) {
        prime_indicator_flags.push_back(true);
    }
    
    for (long i = 2; i <= limit / 2; ++i) {
        for (long j = 2; j <= limit / i; ++j) {
            prime_indicator_flags[i * j] = false;
        }
    }

    std::set<long> primes;
    for (long i = 2; i <= limit; ++i) {
        if (prime_indicator_flags[i])
            primes.insert(i);
    }
    
    return primes;
}

std::pair<long, long> get_chain(const std::set<long>& primes, const long& seed, const long& limit) {

    std::pair<long, long> out_pair;

    auto it = primes.begin();
    for (int i = 0; i < seed; i++)
        ++it;
    
    long cumulative_sum = 0;

    do {
        cumulative_sum += *it;
        if (primes.find(cumulative_sum) != primes.end())
            out_pair = std::make_pair(std::distance(primes.begin(), it) - seed + 1, cumulative_sum);
        ++it;
    } while (cumulative_sum + *it <= limit);

    return out_pair;
}
