#include "../include/utilities.h"

#include <set>

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

template class primes::Phi<char>;
template class primes::Phi<char16_t>;
template class primes::Phi<char32_t>;
template class primes::Phi<wchar_t>;
template class primes::Phi<signed char>;
template class primes::Phi<short int>;
template class primes::Phi<int>;
template class primes::Phi<long int>;
template class primes::Phi<long long int>;
template class primes::Phi<unsigned char>;
template class primes::Phi<unsigned short int>;
template class primes::Phi<unsigned int>;
template class primes::Phi<unsigned long int>;
template class primes::Phi<unsigned long long int>;

