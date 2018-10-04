/*
Euler's Totient function, phi(n), is used to determine the number of numbers
less than n which are relatively prime to n.

For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively
prime to nine, phi(9)=6.

It can be shown that n=6 produces a maximum n / phi(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n / phi(n) is a maximum.

Solution: 510510
*/

#include <cmath>

#include <iostream>
#include <memory>
#include <vector>
#include <set>

class Phi {
    private:
        std::set<int> primes;

    public:
        Phi(const int&);
        int operator () (int);
};

int main() {

    const int LIMIT = 1000000;
    
    std::unique_ptr<Phi> phi(new Phi(LIMIT));

    std::pair<double, int> phiratio_max = std::make_pair(0., 0);
    std::pair<double, int> phiratio;
    for (int n = 2; n <= LIMIT; ++n) {
        phiratio = std::make_pair(static_cast<double>(n) / (*phi)(n), n);
        phiratio_max = std::max(phiratio_max, phiratio);
    }

    std::cout << "Maximum ratio = " << phiratio_max.first;
    std::cout << "; n = " << phiratio_max.second << std::endl;
}

Phi::Phi(const int& limit) {

    /* pre-populate primes up to limit */

    std::vector<bool> flags = {false, false};
    for (int i = 2; i <= limit; i++)
        flags.push_back(true);
    for (int i = 2; i <= limit / 2; i++) {
        for (int j = 2; j <= limit / i; j++) {
            flags[i * j] = false;
        }
    }
    
    for (int i = 2; i <= limit; i++) {
        if (flags[i])
            primes.insert(i);
    }
}

int Phi::operator () (int n) {

    /* return Phi(n) */
    
    if (primes.find(n) != primes.end())
        return n - 1;
    
    double product = 1;
    for (auto prime : primes) {
        if (prime > sqrt(n))
            break;
        if (n % prime == 0)
            product *= 1 - 1. / prime;
    }

    return static_cast<int>(n * product);
}
