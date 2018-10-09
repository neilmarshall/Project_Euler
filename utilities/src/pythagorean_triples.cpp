#include "../include/utilities.h"

template <typename T>
PythagoreanTriples::PythagoreanTripleGenerator<T>::PythagoreanTripleGenerator () {
    triples.push_back(std::make_tuple(3, 4, 5));
}

template PythagoreanTriples::PythagoreanTripleGenerator<char> ();
template PythagoreanTriples::PythagoreanTripleGenerator<char16_t> ();
template PythagoreanTriples::PythagoreanTripleGenerator<char32_t> ();
template PythagoreanTriples::PythagoreanTripleGenerator<wchar_t> ();
template PythagoreanTriples::PythagoreanTripleGenerator<signed char> ();
template PythagoreanTriples::PythagoreanTripleGenerator<short int> ();
template PythagoreanTriples::PythagoreanTripleGenerator<int> ();
template PythagoreanTriples::PythagoreanTripleGenerator<long int> ();
template PythagoreanTriples::PythagoreanTripleGenerator<long long int> ();
template PythagoreanTriples::PythagoreanTripleGenerator<unsigned char> ();
template PythagoreanTriples::PythagoreanTripleGenerator<unsigned short int> ();
template PythagoreanTriples::PythagoreanTripleGenerator<unsigned int> ();
template PythagoreanTriples::PythagoreanTripleGenerator<unsigned long int> ();
template PythagoreanTriples::PythagoreanTripleGenerator<unsigned long long int> ();

template <typename T>
std::tuple<T, T, T> PythagoreanTriples::PythagoreanTripleGenerator<T>::GetNextTriple() {
    auto next_triple = triples.front();
    triples.pop_front();
    T a, b, c;
    std::tie(a, b, c) = next_triple;
    add_new_triples(a, b, c);
    return next_triple;
}

template std::tuple<char, char, char> PythagoreanTriples::PythagoreanTripleGenerator<char> ();
template std::tuple<char16_t, char16_t, char16_t> PythagoreanTriples::PythagoreanTripleGenerator<char16_t> ();
template std::tuple<char32_t, char32_t, char32_t> PythagoreanTriples::PythagoreanTripleGenerator<char32_t> ();
template std::tuple<wchar_t, wchar_t, wchar_t> PythagoreanTriples::PythagoreanTripleGenerator<wchar_t> ();
template std::tuple<signed char, signed char, signed char> PythagoreanTriples::PythagoreanTripleGenerator<signed char> ();
template std::tuple<short int, short int, short int> PythagoreanTriples::PythagoreanTripleGenerator<short int> ();
template std::tuple<int, int, int> PythagoreanTriples::PythagoreanTripleGenerator<int> ();
template std::tuple<long int, long int, long int> PythagoreanTriples::PythagoreanTripleGenerator<long int> ();
template std::tuple<long long int, long long int, long long int> PythagoreanTriples::PythagoreanTripleGenerator<long long int> ();
template std::tuple<unsigned char, unsigned char, unsigned char> PythagoreanTriples::PythagoreanTripleGenerator<unsigned char> ();
template std::tuple<unsigned short int, unsigned short int, unsigned short int> PythagoreanTriples::PythagoreanTripleGenerator<unsigned short int> ();
template std::tuple<unsigned int, unsigned int, unsigned int> PythagoreanTriples::PythagoreanTripleGenerator<unsigned int> ();
template std::tuple<unsigned long int, unsigned long int, unsigned long int> PythagoreanTriples::PythagoreanTripleGenerator<unsigned long int> ();
template std::tuple<unsigned long long int, unsigned long long int, unsigned long long int> PythagoreanTriples::PythagoreanTripleGenerator<unsigned long long int> ();

template <typename T>
void PythagoreanTriples::PythagoreanTripleGenerator<T>::add_new_triples(T a, T b, T c) {
    std::vector<T> elements(3);

    // matrix multiplication using [[1, -2, 2], [2, -1, 2], [2, -2, 3]]
    elements[0] = a - 2 * b + 2 * c;
    elements[1] = 2 * a - b + 2 * c;
    elements[2] = 2 * a - 2 * b + 3 * c;
    std::sort(elements.begin(), elements.end());
    triples.push_back(std::make_tuple(elements[0], elements[1], elements[2]));

    // matrix multiplication using [[1, 2, 2], [2, 1, 2], [2, 2, 3]]
    elements[0] = a + 2 * b + 2 * c;
    elements[1] = 2 * a + b + 2 * c;
    elements[2] = 2 * a + 2 * b + 3 * c;
    std::sort(elements.begin(), elements.end());
    triples.push_back(std::make_tuple(elements[0], elements[1], elements[2]));

    // matrix multiplication using [[-1, 2, 2], [-2, 1, 3], [-2, 2, 3]]
    elements[0] = -a + 2 * b + 2 * c;
    elements[1] = -2 * a + b + 3 * c;
    elements[2] = -2 * a + 2 * b + 3 * c;
    std::sort(elements.begin(), elements.end());
    triples.push_back(std::make_tuple(elements[0], elements[1], elements[2]));
}

template void PythagoreanTriples::PythagoreanTripleGenerator<char> (char, char, char);
template void PythagoreanTriples::PythagoreanTripleGenerator<char16_t> (char16_t, char16_t, char16_t);
template void PythagoreanTriples::PythagoreanTripleGenerator<char32_t> (char32_t, char32_t, char32_t);
template void PythagoreanTriples::PythagoreanTripleGenerator<wchar_t> (wchar_t, wchar_t, wchar_t);
template void PythagoreanTriples::PythagoreanTripleGenerator<signed char> (signed char, signed char, signed char);
template void PythagoreanTriples::PythagoreanTripleGenerator<short int> (short int, short int, short int);
template void PythagoreanTriples::PythagoreanTripleGenerator<int> (int, int, int);
template void PythagoreanTriples::PythagoreanTripleGenerator<long int> (long int, long int, long int);
template void PythagoreanTriples::PythagoreanTripleGenerator<long long int> (long long int, long long int, long long int);
template void PythagoreanTriples::PythagoreanTripleGenerator<unsigned char> (unsigned char, unsigned char);
template void PythagoreanTriples::PythagoreanTripleGenerator<unsigned short int> (unsigned short int, unsigned short int, unsigned short int);
template void PythagoreanTriples::PythagoreanTripleGenerator<unsigned int> (unsigned int, unsigned int);
template void PythagoreanTriples::PythagoreanTripleGenerator<unsigned long int> (unsigned long int, unsigned long int, unsigned long int);
template void PythagoreanTriples::PythagoreanTripleGenerator<unsigned long long int> (unsigned long long int, unsigned long long int, unsigned long long int);
