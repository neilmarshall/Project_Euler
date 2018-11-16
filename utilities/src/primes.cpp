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

template <typename T>
std::vector<T> primes::get_primes_under_n(const T& n) {

    static_assert(std::is_integral<T>::value, "Type must be integral");

    if (n <= 1) { return std::vector<T>(); }

    std::vector<bool> flags = {false, false};
    for (T p = 2; p <= n; p++) {
       flags.push_back(true);
    }
    for (T p = 2; p <= n / 2; p++) {
        if (flags[p]) {
            for (T q = 2; q <= n / p; q++) {
                flags[p * q] = false;
            }
        }
    }

    std::vector<T> primes;
    for (T i = 2; i < n; i++) {
        if (flags[i]) { primes.push_back(i); }
    }

    return primes;
}

template std::vector<char> primes::get_primes_under_n(const char&);
template std::vector<char16_t> primes::get_primes_under_n(const char16_t&);
template std::vector<char32_t> primes::get_primes_under_n(const char32_t&);
template std::vector<wchar_t> primes::get_primes_under_n(const wchar_t&);
template std::vector<signed char> primes::get_primes_under_n(const signed char&);
template std::vector<short int> primes::get_primes_under_n(const short int&);
template std::vector<int> primes::get_primes_under_n(const int&);
template std::vector<long int> primes::get_primes_under_n(const long int&);
template std::vector<long long int> primes::get_primes_under_n(const long long int&);
template std::vector<unsigned char> primes::get_primes_under_n(const unsigned char&);
template std::vector<unsigned short int> primes::get_primes_under_n(const unsigned short int&);
template std::vector<unsigned int> primes::get_primes_under_n(const unsigned int&);
template std::vector<unsigned long int> primes::get_primes_under_n(const unsigned long int&);
template std::vector<unsigned long long int> primes::get_primes_under_n(const unsigned long long int&);

template <typename T>
std::vector<T> primes::get_primes_up_to_n(const T& n) {

    static_assert(std::is_integral<T>::value, "Type must be integral");

    return get_primes_under_n(static_cast<T>(n + 1));
}

template std::vector<char> primes::get_primes_up_to_n(const char&);
template std::vector<char16_t> primes::get_primes_up_to_n(const char16_t&);
template std::vector<char32_t> primes::get_primes_up_to_n(const char32_t&);
template std::vector<wchar_t> primes::get_primes_up_to_n(const wchar_t&);
template std::vector<signed char> primes::get_primes_up_to_n(const signed char&);
template std::vector<short int> primes::get_primes_up_to_n(const short int&);
template std::vector<int> primes::get_primes_up_to_n(const int&);
template std::vector<long int> primes::get_primes_up_to_n(const long int&);
template std::vector<long long int> primes::get_primes_up_to_n(const long long int&);
template std::vector<unsigned char> primes::get_primes_up_to_n(const unsigned char&);
template std::vector<unsigned short int> primes::get_primes_up_to_n(const unsigned short int&);
template std::vector<unsigned int> primes::get_primes_up_to_n(const unsigned int&);
template std::vector<unsigned long int> primes::get_primes_up_to_n(const unsigned long int&);
template std::vector<unsigned long long int> primes::get_primes_up_to_n(const unsigned long long int&);

template <typename T>
std::vector<T> primes::get_prime_factors(T n) {

    static_assert(std::is_integral<T>::value, "Type must be integral");

    if (n <= 1) { return std::vector<T>(); }

    std::vector<T> factors;
    std::vector<T> primes = get_primes_up_to_n(static_cast<T>(sqrt(n)));
    for (auto p : primes) {
        while (n % p == 0) {
            factors.push_back(p);
            n /= p;
        }
    }

    if (n > 1) { factors.push_back(n); }

    return factors;
}

template std::vector<char> primes::get_prime_factors (char);
template std::vector<char16_t> primes::get_prime_factors (char16_t);
template std::vector<char32_t> primes::get_prime_factors (char32_t);
template std::vector<wchar_t> primes::get_prime_factors (wchar_t);
template std::vector<signed char> primes::get_prime_factors (signed char);
template std::vector<short int> primes::get_prime_factors (short int);
template std::vector<int> primes::get_prime_factors (int);
template std::vector<long int> primes::get_prime_factors (long int);
template std::vector<long long int> primes::get_prime_factors (long long int);
template std::vector<unsigned char> primes::get_prime_factors (unsigned char);
template std::vector<unsigned short int> primes::get_prime_factors (unsigned short int);
template std::vector<unsigned int> primes::get_prime_factors (unsigned int);
template std::vector<unsigned long int> primes::get_prime_factors (unsigned long int);
template std::vector<unsigned long long int> primes::get_prime_factors (unsigned long long int);

template <typename T>
std::vector<T> primes::get_unique_prime_factors(T n) {

    static_assert(std::is_integral<T>::value, "Type must be integral");

    std::vector<T> factors = get_prime_factors(static_cast<T>(n));

    factors.erase(std::unique(factors.begin(), factors.end()), factors.end());

    return factors;
}

template std::vector<char> primes::get_unique_prime_factors (char);
template std::vector<char16_t> primes::get_unique_prime_factors (char16_t);
template std::vector<char32_t> primes::get_unique_prime_factors (char32_t);
template std::vector<wchar_t> primes::get_unique_prime_factors (wchar_t);
template std::vector<signed char> primes::get_unique_prime_factors (signed char);
template std::vector<short int> primes::get_unique_prime_factors (short int);
template std::vector<int> primes::get_unique_prime_factors (int);
template std::vector<long int> primes::get_unique_prime_factors (long int);
template std::vector<long long int> primes::get_unique_prime_factors (long long int);
template std::vector<unsigned char> primes::get_unique_prime_factors (unsigned char);
template std::vector<unsigned short int> primes::get_unique_prime_factors (unsigned short int);
template std::vector<unsigned int> primes::get_unique_prime_factors (unsigned int);
template std::vector<unsigned long int> primes::get_unique_prime_factors (unsigned long int);
template std::vector<unsigned long long int> primes::get_unique_prime_factors (unsigned long long int);
