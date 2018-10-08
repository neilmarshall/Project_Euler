#include "../include/utilities.h"

#include <cmath>

template <typename T>
bool primes::is_prime (const T& n) {

    static_assert(std::is_integral<T>::value, "Type must be integral");

    if (n <= 1) { return false; }

    for (T p = 2; p <= static_cast<T>(sqrt(n)); p++) {
        if (n % p == 0) { return false; }
    }

    return true;
}

template bool primes::is_prime<char> (const char&);
template bool primes::is_prime<char16_t> (const char16_t&);
template bool primes::is_prime<char32_t> (const char32_t&);
template bool primes::is_prime<wchar_t> (const wchar_t&);
template bool primes::is_prime<signed char> (const signed char&);
template bool primes::is_prime<short int> (const short int&);
template bool primes::is_prime<int> (const int&);
template bool primes::is_prime<long int> (const long int&);
template bool primes::is_prime<long long int> (const long long int&);
template bool primes::is_prime<unsigned char> (const unsigned char&);
template bool primes::is_prime<unsigned short int> (const unsigned short int&);
template bool primes::is_prime<unsigned int> (const unsigned int&);
template bool primes::is_prime<unsigned long int> (const unsigned long&);
template bool primes::is_prime<unsigned long long int> (const unsigned long long&);

