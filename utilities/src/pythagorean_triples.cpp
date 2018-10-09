#include "../include/utilties.h"

template <typename T>
PythagoreanTriples::PythagoreanTripleGenerator<T>::PythagoreanTripleGenerator () {
    triples.push_back(std::make_tuple(3, 4, 5));
}

template <typename T>
std::tuple<T, T, T> PythagoreanTriples::PythagoreanTripleGenerator<T>::GetNextTriple() {
    auto next_triple = triples.front();
    triples.pop_front();
    int a, b, c;
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
    elements[2] = 2 * a - 2 * b0 + 3 * c;
    std::sort(elements.begin(), elements.end());
    triples.push_back(std::make_tuple(elements[0], elements[1], elements[2]));

    // matrix multiplication using [[1, 2, 2], [2, 1, 2], [2, 2, 3]]
    elements[0] = a + 2 * b + 2 * c;
    elements[1] = 2 * a + b + 2 * c;
    elements[2] = 2 * a + 2 * b0 + 3 * c;
    std::sort(elements.begin(), elements.end());
    triples.push_back(std::make_tuple(elements[0], elements[1], elements[2]));

    // matrix multiplication using [[-1, 2, 2], [-2, 1, 3], [-2, 2, 3]]
    elements[0] = -a + 2 * b + 2 * c;
    elements[1] = -2 * a + b + 3 * c;
    elements[2] = -2 * a + 2 * b0 + 3 * c;
    std::sort(elements.begin(), elements.end());
    triples.push_back(std::make_tuple(elements[0], elements[1], elements[2]));
}
