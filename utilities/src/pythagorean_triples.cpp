#include "../include/utilities.h"

template <typename T>
PythagoreanTriples::PythagoreanTripleGenerator<T>::PythagoreanTripleGenerator () {
    triples.push(std::make_tuple(3, 4, 5));
}

template <typename T>
std::tuple<T, T, T> PythagoreanTriples::PythagoreanTripleGenerator<T>::GetNextTriple() {
    auto next_triple = triples.top();
    triples.pop();
    T a, b, c;
    std::tie(a, b, c) = next_triple;
    add_new_triples(a, b, c);
    return next_triple;
}

template <typename T>
void PythagoreanTriples::PythagoreanTripleGenerator<T>::add_new_triples(T a, T b, T c) {
    std::vector<T> elements(3);

    // matrix multiplication using [[1, -2, 2], [2, -1, 2], [2, -2, 3]]
    elements[0] = a - 2 * b + 2 * c;
    elements[1] = 2 * a - b + 2 * c;
    elements[2] = 2 * a - 2 * b + 3 * c;
    std::sort(elements.begin(), elements.end());
    triples.push(std::make_tuple(elements[0], elements[1], elements[2]));

    // matrix multiplication using [[1, 2, 2], [2, 1, 2], [2, 2, 3]]
    elements[0] = a + 2 * b + 2 * c;
    elements[1] = 2 * a + b + 2 * c;
    elements[2] = 2 * a + 2 * b + 3 * c;
    std::sort(elements.begin(), elements.end());
    triples.push(std::make_tuple(elements[0], elements[1], elements[2]));

    // matrix multiplication using [[-1, 2, 2], [-2, 1, 2], [-2, 2, 3]]
    elements[0] = -a + 2 * b + 2 * c;
    elements[1] = -2 * a + b + 2 * c;
    elements[2] = -2 * a + 2 * b + 3 * c;
    std::sort(elements.begin(), elements.end());
    triples.push(std::make_tuple(elements[0], elements[1], elements[2]));
}

template class PythagoreanTriples::PythagoreanTripleGenerator<char>;
template class PythagoreanTriples::PythagoreanTripleGenerator<char16_t>;
template class PythagoreanTriples::PythagoreanTripleGenerator<char32_t>;
template class PythagoreanTriples::PythagoreanTripleGenerator<wchar_t>;
template class PythagoreanTriples::PythagoreanTripleGenerator<signed char>;
template class PythagoreanTriples::PythagoreanTripleGenerator<short int>;
template class PythagoreanTriples::PythagoreanTripleGenerator<int>;
template class PythagoreanTriples::PythagoreanTripleGenerator<long int>;
template class PythagoreanTriples::PythagoreanTripleGenerator<long long int>;
template class PythagoreanTriples::PythagoreanTripleGenerator<unsigned char>;
template class PythagoreanTriples::PythagoreanTripleGenerator<unsigned short int>;
template class PythagoreanTriples::PythagoreanTripleGenerator<unsigned int>;
template class PythagoreanTriples::PythagoreanTripleGenerator<unsigned long int>;
template class PythagoreanTriples::PythagoreanTripleGenerator<unsigned long long int>;

