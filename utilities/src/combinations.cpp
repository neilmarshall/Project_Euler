#include "../include/utilities.h"

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

template class combinations::nCr_Calculator<char>;
template class combinations::nCr_Calculator<char16_t>;
template class combinations::nCr_Calculator<char32_t>;
template class combinations::nCr_Calculator<wchar_t>;
template class combinations::nCr_Calculator<signed char>;
template class combinations::nCr_Calculator<short int>;
template class combinations::nCr_Calculator<int>;
template class combinations::nCr_Calculator<long int>;
template class combinations::nCr_Calculator<long long int>;
template class combinations::nCr_Calculator<unsigned char>;
template class combinations::nCr_Calculator<unsigned short int>;
template class combinations::nCr_Calculator<unsigned int>;
template class combinations::nCr_Calculator<unsigned long int>;
template class combinations::nCr_Calculator<unsigned long long int>;

