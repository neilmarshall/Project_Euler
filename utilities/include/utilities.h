#ifndef UTILITIES_H
#define UTILITIES_H

#include <map>
#include <set>
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
}

#endif // UTILITIES_H

