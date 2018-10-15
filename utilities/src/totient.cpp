#include "../include/utilities.h"

template <typename T>
primes::Phi<T>::Phi(const T& limit) {

    /* constructor function - pre-populates primes totients up to limit so
       Euler's totient function can be efficiently checked */

    // generate prime flags
    std::vector<bool> flags = {false, false};
    for (T i = 2; i <= limit; i++)
        flags.push_back(true);
    for (T i = 2; i <= limit / 2; i++) {
        if (flags[i]) {
            for (T j = 2; j <= limit / i; j++) {
                flags[i * j] = false;
            }
        }
    }

    // generate primes from prime flags
    std::vector<T> primes;
    for (T i = 2; i <= limit; i++)
        if (flags[i]) { primes.push_back(i); }

    // pre-populate totients with each value of n up to limit
    for (T i = 0; i <= limit; i++)
        totients.push_back(i);

    // for each prime p, multiply the totient of each multiple of that
    // prime by (p - 1) / p
    for (auto prime : primes) {
        for (T factor = 1; factor <= limit / prime; factor++) {
            totients[prime * factor] /= prime;
            totients[prime * factor] *= prime - 1;
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

