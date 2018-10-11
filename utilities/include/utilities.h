#ifndef UTILITIES_H
#define UTILITIES_H

#include <map>
#include <queue>
#include <tuple>
#include <type_traits>
#include <vector>

namespace combinations {

    /* Efficiently calculates nCr using recursion and memoization to
       avoid integer oveflow */

    template<typename T>
    class nCr_Calculator {

        static_assert(std::is_integral<T>::value, "Type must be integral");

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

        static_assert(std::is_integral<T>::value, "Type must be integral");

        private:
            std::vector<T> totients;
        public:
            Phi(const T&);
            T operator () (const T& n) { return totients[n]; };
    };

    template <typename T>
    bool is_prime (const T&);

    template <typename T>
    std::vector<T> get_primes_under_n(const T&);

    template <typename T>
    std::vector<T> get_primes_up_to_n(const T&);

    template <typename T>
    std::vector<T> get_prime_factors(T);

    template <typename T>
    std::vector<T> get_unique_prime_factors(T);
}

namespace PythagoreanTriples {

    struct pythagorean_triple_comparer {
        template <typename T>
        bool operator () {
            return std::get<0>(t1) + std::get<1>(t1) + std::get<2>(t1) > std::get<0>(t2) + std::get<1>(t2) + std::get<2>(t2);
        }
    };
    
    template <typename T>
    class PythagoreanTripleGenerator {
        /*
         * Class that continuously generates distinct, primitive Pythagorean triples
         *
         * Source: https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples
         *
         * The class stores triples in a priority queue; triples are stored from smallest to
         * largest, where size is taken as the sum of the elements of the triple (so if
         * the triple were considered to form a right-angled triangle then the "size" would
         * be equal to the sum of the side lengths, i.e. the perimeter)
         */

        static_assert(std::is_integral<T>::value, "Type must be integral");

        private:
            std::priority_queue<std::tuple<T, T, T>, std::vector<std::tuple<T, T, T>, pythagorean_triple_comparer> triples;
            void add_new_triples(T, T, T);

        public:
            PythagoreanTripleGenerator ();
            std::tuple<T, T, T> GetNextTriple();
    };
}

#endif // UTILITIES_H
