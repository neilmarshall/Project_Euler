#ifndef UTILITIES_H
#define UTILITIES_H

#include <map>
#include <set>
#include <vector>

namespace combinations {

    /* Efficiently calculates nCr using recursion and memoization to
    avoid integers oveflow */

    template<typename T>
    class nCr_Calculator {
        private:
            std::map<std::pair<const T, const T>, T> calculated_values;
        public:
            T operator () (const T&, const T&);
    };

}

namespace primes {

    /* Templated class to efficiently calculate Euler's totient function up to a given limit */
    template <typename T>
    class Phi {
        private:
            std::set<T> primes;
        public:
            Phi(const T&);
            T operator () (T);
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

    /* constructor function - pre-populates primes up to limit so
       Euler's totient function can be efficiently checked */

    std::vector<bool> flags = {false, false};
    for (T i = 2; i <= limit; i++)
        flags.push_back(true);
    for (T i = 2; i <= limit / 2; i++) {
        for (T j = 2; j <= limit / i; j++) {
            flags[i * j] = false;
        }
    }

    for (T i = 2; i <= limit; i++) {
        if (flags[i])
            primes.insert(i);
    }
}

template <typename T>
T primes::Phi<T>::operator () (T n) {

    /* return Phi(n), i.e. Euler's totient function */

    if (primes.find(n) != primes.end())
        return n - 1;

    T product = n;
    for (auto prime : primes) {
        if (prime > n)
            break;
        if (n % prime == 0) {
            product /= prime;
            product *= prime - 1;
            n /= prime;
        }
    }

    return product;
}

