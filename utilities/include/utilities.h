#ifndef UTILITIES_H
#define UTILITIES_H

#include <map>
#include <set>
#include <vector>

namespace combinations {

    /* Efficiently calculates nCr using recursion and memoization to
       avoid integer oveflow */

    template<typename T>
    class nCr_Calculator {
        private:
            std::map<std::pair<const T, const T>, T> calculated_values;
        public:
            T operator () (const T&, const T&);
    };

}

namespace primes {

    /* Templated class to efficiently calculate Euler's totient function
       up to a given limit */

    template <typename T>
    class Phi {
        private:
            std::vector<T> totients;
        public:
            Phi(const T&);
            T operator () (const T& n) { return totients[n]; };
    };
}

#endif // UTILITIES_H

template<typename T>
T combinations::nCr_Calculator<T>::operator () (const T& n, const T& r) {

    /*
    Efficiently calculates nCr using recursion and memoization to
    avoid integers oveflow, based on the following truisms:

        nCr(n, 0) = nCr(n, n) = 1
        nCr(n, 1) = nCr(n, n - 1) = n
        nCr(n, r) = nCr(n, n - r)
        nCr(n, r) = nCr(n - 1, r - 1) + nCr(n - 1, r)
    */

    // first check for previously calculated values
    if (calculated_values.find(std::make_pair(n, r)) != calculated_values.end())
        return calculated_values.find(std::make_pair(n, r))->second;

    // else calculate value, and add to previously calculated values before returning

    T out_value;

    if (r == 0) {
        out_value = 1;
    } else if (r == 1) {
        out_value = n;
    } else if (r > n / 2) {
        out_value = (*this)(n, n - r);
    } else  {
        out_value = (*this)(n - 1, r - 1) + (*this)(n - 1, r);
    }

    calculated_values[std::make_pair(n, r)] = out_value;

    return out_value;
}

template <typename T>
primes::Phi<T>::Phi(const T& limit) {

    /* constructor function - pre-populates primes totients up to limit so
       Euler's totient function can be efficiently checked */

    // first generate primes
    std::vector<bool> flags = {false, false};
    for (T i = 2; i <= limit; i++)
        flags.push_back(true);
    for (T i = 2; i <= limit / 2; i++) {
        for (T j = 2; j <= limit / i; j++) {
            flags[i * j] = false;
        }
    }

    std::set<T> primes;
    for (T i = 2; i <= limit; i++) {
        if (flags[i])
            primes.insert(i);
    }

    // now pre-populate totients with each value of n up to limit
    for (T i = 0; i <= limit; i++)
        totients.push_back(i);

    // now for each prime p, multiply the totient of each multiple of that
    // prime by (p - 1) / p
    for (auto prime : primes) {
        T factor = 1;
        while (prime * factor <= limit) {
            totients[prime * factor] /= prime;
            totients[prime * factor] *= prime - 1;
            factor += 1;
        }
    }
}

